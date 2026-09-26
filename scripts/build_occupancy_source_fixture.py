"""Rebuild the bounded SRD 5.2.1 occupancy EvidenceUnit from its source PDF."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import blake3
import fitz

from extraction.schemas import SurfaceAST, SurfaceASTNode
from extraction.stage_b import run_stage_b


SOURCE_URL = "https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf"
SOURCE_SHA256 = "8974902d109d6e63672d7c490bde9ccf052410503d9cfa768237154fbc5e3d87"
PAGE_INDEX = 13
SECTION = "Moving around Other Creatures"
PARAGRAPH = (
    "You can’t willingly end a move in a space occupied by another creature. "
    "If you somehow end a turn in a space with another creature, you have the Prone "
    "condition (see “Rules Glossary”) unless you are Tiny or are of a larger size "
    "than the other creature."
)


def build(pdf_path: Path, output_dir: Path) -> None:
    if sha256(pdf_path.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError("Source PDF digest does not match the audited SRD 5.2.1 copy")
    with fitz.open(pdf_path) as pdf:
        page = pdf[PAGE_INDEX]
        page_text = " ".join(page.get_text("text").split())
        if SECTION not in page_text or PARAGRAPH not in page_text:
            raise ValueError("The exact source section and paragraph are absent from PDF page 14")
        image_bytes = page.get_pixmap(matrix=fitz.Matrix(200 / 72, 200 / 72), alpha=False).tobytes("png")
    page_fingerprint = blake3.blake3(image_bytes).hexdigest()

    root = SurfaceASTNode(
        node_type="root", level=0, text="",
        children=[SurfaceASTNode(
            node_type="heading", level=4, text=SECTION,
            source_line_start=0, source_line_end=1,
            children=[SurfaceASTNode(
                node_type="paragraph", level=0, text=PARAGRAPH,
                source_line_start=1, source_line_end=2,
            )],
        )],
    )
    root_payload = root.to_dict()
    ast = SurfaceAST(
        page_fingerprint=page_fingerprint,
        content_hash=blake3.blake3(json.dumps(root_payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
        root=root, node_count=3, table_count=0,
    )
    result = run_stage_b(ast, content_version="srd-5.2.1-p14-manual-structural-transcript-v1")
    if len(result.units) != 1:
        raise ValueError("Expected exactly one bounded occupancy EvidenceUnit")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "stageA.surface.ast.json").write_text(
        json.dumps(ast.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (output_dir / "stageB.evidence_units.json").write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (output_dir / "source_manifest.json").write_text(
        json.dumps({
            "source_url": SOURCE_URL,
            "source_sha256": SOURCE_SHA256,
            "license": "CC BY 4.0 (SRD 5.2.1)",
            "pdf_page_index": PAGE_INDEX,
            "printed_page": 14,
            "section": SECTION,
            "page_fingerprint": page_fingerprint,
            "evidence_unit_id": result.units[0].unit_id,
            "method": "Exact paragraph transcribed from the source PDF into a minimal SurfaceAST, then run through Stage B",
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    build(args.pdf, args.output_dir)


if __name__ == "__main__":
    main()
