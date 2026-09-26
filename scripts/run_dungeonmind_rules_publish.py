"""Publish and reopen the RLH-02 occupancy package through DungeonMind vNext."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dungeonmind.infrastructure.memory.vnext_knowledge import (
    InMemoryKnowledgeRevisionRepository,
)

from semantic_lifting.dungeonmind_export import FIXTURE, publish_occupancy


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=FIXTURE)
    parser.add_argument(
        "--output", type=Path, default=FIXTURE / "dungeonmind_publication_witness.json"
    )
    parser.add_argument(
        "--postgres", action="store_true", help="Use DUNGEONMIND_DATABASE_URL"
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Reopen an existing PostgreSQL witness in a new process",
    )
    args = parser.parse_args()
    if args.postgres:
        url = os.environ.get("DUNGEONMIND_DATABASE_URL")
        if not url:
            raise ValueError("DUNGEONMIND_DATABASE_URL is required for --postgres")
        from dungeonmind.infrastructure.postgres.database import PostgresDatabase
        from dungeonmind.infrastructure.postgres.vnext_knowledge import (
            PostgresKnowledgeRevisionRepository,
        )

        def make_repository():
            return PostgresKnowledgeRevisionRepository(PostgresDatabase(url))

        if args.verify_only:
            expected = json.loads(args.output.read_text())
            reader = make_repository()
            reopened = reader.get_revision(
                expected["space_id"], expected["published_revision_id"]
            )
            head = reader.get_head(expected["space_id"])
            if (
                reopened is None
                or head is None
                or head.head_revision_id != expected["published_revision_id"]
                or reopened.graph_payload_sha256 != expected["reopened_payload_sha256"]
                or reopened.graph_payload["assertions"]
                != expected["reopened_assertions"]
                or reopened.graph_payload["evidence"] != expected["reopened_evidence"]
            ):
                raise ValueError("Independent-process PostgreSQL reopen drift")
            print(
                json.dumps({"verified_revision_id": expected["published_revision_id"]})
            )
            return
        writer = make_repository()
        result = publish_occupancy(args.fixture, writer)
        reader = make_repository()
        reopened = reader.get_revision(
            result["space_id"], result["published_revision_id"]
        )
        if (
            reopened is None
            or reopened.graph_payload_sha256 != result["reopened_payload_sha256"]
        ):
            raise ValueError("Independent PostgreSQL repository reopen failed")
        result["repository_kind"] = "postgresql"
        result["independent_reopen"] = True
    else:
        if args.verify_only:
            raise ValueError("--verify-only requires --postgres")
        result = publish_occupancy(args.fixture, InMemoryKnowledgeRevisionRepository())
        result["repository_kind"] = "memory"
        result["independent_reopen"] = False
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "repository_kind": result["repository_kind"],
                "published_revision_id": result["published_revision_id"],
                "accepted": len(result["accepted_candidate_ids"]),
                "excluded": len(result["excluded_candidate_ids"]),
            }
        )
    )


if __name__ == "__main__":
    main()
