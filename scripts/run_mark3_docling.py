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
from extraction.pipeline import run_a_b


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
    args = parser.parse_args()
    source = args.pdf.resolve(strict=True)
    with pymupdf.open(source) as pdf:
        if args.threads < 1:
            parser.error("--threads must be positive")
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
                    "ranges": ranges, "pages": {}}
        (out / "source.json").write_text(json.dumps(manifest, indent=2))
        options = PdfPipelineOptions(do_ocr=False, accelerator_options=AcceleratorOptions(
            device=AcceleratorDevice.CPU, num_threads=args.threads))
        converter = DocumentConverter(format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=options)})
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
            doc = DoclingDocument.model_validate(ordered)
            doc.save_as_json(out / f"ordered-{first}-{last}.json")
            for n in range(first, last + 1):
                markdown, expected = export_page(doc, n)
                page_out = out / f"pdf-{n:03}"
                combined = run_a_b(source, n - 1, page_out, skip_ocr=True, raw_markdown_override=markdown)
                units = json.loads((page_out / "stageB.evidence_units.json").read_text())["units"]
                if combined["stage_a"]["table_count"] != expected or sum(u["unit_type"] == "table" for u in units) != expected:
                    raise ValueError(f"PDF page {n}: source tables were lost in Mark III")
                if not combined["all_gates_passed"]:
                    raise ValueError(f"PDF page {n}: Mark III gates failed; see {page_out}")
                manifest["pages"][n] = {"pdf_index": n - 1, "pdf_label": pdf[n - 1].get_label(),
                                          "tables": expected, "moves": [m for m in moves if m["page"] == n]}
                (out / "source.json").write_text(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
