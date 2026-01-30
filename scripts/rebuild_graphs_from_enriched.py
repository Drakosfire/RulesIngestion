from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from enrichment import EnrichedChunk, build_chunk_graph


def _load_enriched(path: Path) -> Tuple[str, List[EnrichedChunk]]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    doc_id = payload.get("document") or path.stem.replace(".enriched", "")
    chunks: List[EnrichedChunk] = []
    for raw in payload.get("chunks", []):
        try:
            chunks.append(EnrichedChunk(**raw))
        except TypeError as exc:
            raise ValueError(f"Invalid chunk payload in {path}: {exc}") from exc
    return doc_id, chunks


def _write_graph(path: Path, graph_payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(graph_payload, handle, indent=2)


def rebuild_graphs(enriched_dir: Path, ruleset_id: str | None) -> List[Path]:
    enriched_files = sorted(enriched_dir.glob("*.enriched.json"))
    if not enriched_files:
        raise FileNotFoundError(f"No enriched outputs found in {enriched_dir}")
    written: List[Path] = []
    for enriched_path in enriched_files:
        doc_id, chunks = _load_enriched(enriched_path)
        graph = build_chunk_graph(doc_id, chunks, ruleset_id=ruleset_id)
        graph_path = enriched_dir / f"{doc_id}.graph.json"
        _write_graph(graph_path, graph.to_dict())
        written.append(graph_path)
        print(f"✅ rebuilt: {graph_path}")
    return written


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rebuild graph JSON files from existing enriched outputs."
    )
    parser.add_argument(
        "--enriched-dir",
        required=True,
        help="Path to enriched outputs directory (contains *.enriched.json)",
    )
    parser.add_argument(
        "--ruleset-id",
        default=None,
        help="Ruleset ID to embed in graph nodes (defaults to doc_id)",
    )
    args = parser.parse_args()
    enriched_dir = Path(args.enriched_dir).resolve()
    rebuild_graphs(enriched_dir, ruleset_id=args.ruleset_id)


if __name__ == "__main__":
    main()
