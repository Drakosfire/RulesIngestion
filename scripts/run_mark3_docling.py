#!/usr/bin/env python3
"""Convert a native-text PDF with Docling and preserve its tables in Mark III."""

import argparse
import hashlib
import json
import re
import sys
from importlib.metadata import version
from pathlib import Path

import pymupdf
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import AcceleratorDevice, AcceleratorOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.transforms.serializer.html import HTMLTableSerializer
from docling_core.transforms.serializer.markdown import MarkdownDocSerializer, MarkdownParams
from docling_core.types.doc import DoclingDocument

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from extraction.docling_order import repair
from extraction.creature_carryover import bind_continuation, continuation_scopes
from extraction.gates_b import run_stage_b_gates
from extraction.pdf_outline_scope import fill_missing_scope, outline_scope
from extraction.pipeline import run_a_b
from extraction.schemas import EvidenceUnit


def export_page(doc: DoclingDocument, page: int) -> tuple[str, int]:
    expected = sum(any(p.page_no == page for p in t.prov) for t in doc.tables)
    markdown = MarkdownDocSerializer(
        doc=doc, params=MarkdownParams(pages={page}),
        table_serializer=HTMLTableSerializer(),
    ).serialize().text
    if len(re.findall(r"<table\b", markdown, re.I)) != expected:
        raise ValueError(f"PDF page {page}: source table count differs from HTML export")
    return markdown, expected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--range", dest="ranges", action="append", help="Inclusive 1-based range, e.g. 38-41")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--outline-scope", action="store_true", help="Fill missing heading paths from PDF bookmarks")
    args = parser.parse_args()
    source = args.pdf.resolve(strict=True)
    with pymupdf.open(source) as pdf:
        if args.threads < 1:
            parser.error("--threads must be positive")
        destinations = outline_scope(pdf.get_toc()) if args.outline_scope else {}
        ranges = []
        seen = set()
        for text in args.ranges or [f"1-{len(pdf)}"]:
            lo, _, hi = text.partition("-")
            first, last = int(lo), int(hi or lo)
            if not 1 <= first <= last <= len(pdf) or seen.intersection(range(first, last + 1)):
                parser.error(f"invalid or overlapping PDF page range: {text}")
            ranges.append((first, last))
            seen.update(range(first, last + 1))
        out = args.out_dir.resolve()
        out.mkdir(parents=True, exist_ok=False)
        with source.open("rb") as stream:
            source_hash = hashlib.file_digest(stream, "sha256").hexdigest()
        manifest = {"source": str(source), "sha256": source_hash,
                    "docling": version("docling"), "docling_core": version("docling-core"),
                    "ranges": ranges, "outline_scope": args.outline_scope, "pages": {}}
        (out / "source.json").write_text(json.dumps(manifest, indent=2))
        options = PdfPipelineOptions(do_ocr=False, accelerator_options=AcceleratorOptions(
            device=AcceleratorDevice.CPU, num_threads=args.threads))
        converter = DocumentConverter(format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=options)})
        previous_texts = []
        previous_end = 0
        for first, last in ranges:
            result = converter.convert(source, page_range=(first, last))
            if result.status.value != "success":
                raise RuntimeError(f"Docling conversion {first}-{last}: {result.status}: {result.errors}")
            raw = result.document
            if set(raw.pages) != set(range(first, last + 1)):
                raise ValueError("Docling PDF page numbers differ from the requested range")
            raw.save_as_json(out / f"docling-{first}-{last}.json")
            ordered = raw.export_to_dict()
            moves = repair(ordered, pdf)
            context = previous_texts if previous_end + 1 == first else []
            scopes = continuation_scopes({"texts": context + ordered["texts"]})
            previous_texts = [
                item for item in ordered["texts"]
                if any(span["page_no"] == last for span in item["prov"])
            ]
            previous_end = last
            doc = DoclingDocument.model_validate(ordered)
            doc.save_as_json(out / f"ordered-{first}-{last}.json")
            for n in range(first, last + 1):
                markdown, expected = export_page(doc, n)
                page_out = out / f"pdf-{n:03}"
                combined = run_a_b(source, n - 1, page_out, skip_ocr=True, raw_markdown_override=markdown)
                units = json.loads((page_out / "stageB.evidence_units.json").read_text())["units"]
                if combined["stage_a"]["table_count"] != expected or sum(u["unit_type"] == "table" for u in units) != expected:
                    raise ValueError(f"PDF page {n}: source tables were lost in Mark III")
                stage_b_passed = combined["stage_b"]["gates_passed"]
                if args.outline_scope or n in scopes:
                    scoped = bind_continuation(
                        [EvidenceUnit.from_dict(u) for u in units], n, scopes.get(n)
                    )
                    if args.outline_scope:
                        scoped = fill_missing_scope(scoped, n, destinations)
                    ast = json.loads((page_out / "stageA.surface.ast.json").read_text())
                    diagnostics = run_stage_b_gates(scoped, ast_dict=ast, is_standalone=(n == 1))
                    stage_b_passed = all(g.passed for g in diagnostics)
                    (page_out / "stageB.outline_scoped.json").write_text(json.dumps({
                        "units": [u.to_dict() for u in scoped],
                        "gates_passed": stage_b_passed,
                        "gate_details": [g.to_dict() for g in diagnostics],
                    }, ensure_ascii=False, indent=2))
                if not combined["stage_a"]["gates_passed"] or not stage_b_passed:
                    raise ValueError(f"PDF page {n}: Mark III gates failed; see {page_out}")
                manifest["pages"][n] = {"pdf_index": n - 1, "pdf_label": pdf[n - 1].get_label(),
                                          "tables": expected, "moves": [m for m in moves if m["page"] == n]}
                (out / "source.json").write_text(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
