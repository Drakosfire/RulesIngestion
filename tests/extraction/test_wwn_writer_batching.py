import asyncio
import json
from types import SimpleNamespace

import pytest

from scripts import run_wwn_writer as writer


def _row(name, ordinal):
    return {
        "pdf_page": 7,
        "unit": writer.EvidenceUnit(
            unit_id=name, unit_type="prose", text=f"The player may choose {name}.",
            structural_path=["Options"], ordering_key=ordinal, page_fingerprint="page",
            content_hash=name, source_line_start=ordinal, source_line_end=ordinal,
        ).to_dict(),
    }


def _annotation(name):
    return {
        "summary_1s": f"The player may choose {name}.",
        "summary_3b": "- The choice is available.",
        "topic_tags": [],
        "co_retrieval_hints": [],
        "mechanic_atoms": [],
        "questions_answered": ["Which option may the player choose?"],
        "lexical_anchors": [name],
    }


@pytest.mark.parametrize("interrupt", [False, True])
def test_group_retries_only_missing_units_and_replays_offline(tmp_path, interrupt):
    rows = [_row("first", 1), _row("second", 2)]
    args = SimpleNamespace(model="gpt-6-luna", effort="low")
    calls = []

    class Client:
        async def generate_structured(self, request):
            calls.append(request.schema_name)
            if len(calls) == 1:
                assert request.schema_name == "wwn_writer_page_annotations"
                parsed = {"annotations": [{"ref": 0, **_annotation("first")}]}
            else:
                assert request.schema_name == "wwn_writer_annotation"
                assert "choose second" in request.user_prompt
                assert "choose first" not in request.user_prompt
                if interrupt and len(calls) == 2:
                    raise asyncio.CancelledError
                parsed = _annotation("second")
            return SimpleNamespace(
                parsed=parsed, observation=SimpleNamespace(model_dump=lambda **_: {"input_tokens": 123})
            )

    client = Client()
    if interrupt:
        with pytest.raises(asyncio.CancelledError):
            asyncio.run(writer.annotate_group(client, rows, args, tmp_path))
        assert len(list(tmp_path.glob("*.json"))) == 1
    assert asyncio.run(writer.annotate_group(client, rows, args, tmp_path)) == 0
    count = len(calls)
    assert asyncio.run(writer.annotate_group(client, rows, args, tmp_path)) == 0
    assert len(calls) == count
    assert {json.loads(p.read_text())["unit_id"] for p in tmp_path.glob("*.json")} == {"first", "second"}
    receipt, = (tmp_path / "request-receipts").glob("*.json")
    assert json.loads(receipt.read_text())["observation"]["input_tokens"] == 123


def test_failed_group_cleans_up_sibling_before_closing_client(tmp_path, monkeypatch):
    import generationengine.client

    rows = [_row("first", 1), _row("second", 2)]
    rows[1]["pdf_page"] = 8
    source = tmp_path / "units.jsonl"
    source.write_text("".join(json.dumps(row) + "\n" for row in rows))
    events = []

    class Client:
        async def aclose(self):
            events.append("closed")

    async def group(_client, records, _args, _output):
        if records[0]["pdf_page"] == 7:
            await sibling_started.wait()
            raise ValueError("invalid cache")
        try:
            sibling_started.set()
            await asyncio.Future()
        finally:
            await asyncio.sleep(0)
            events.append("sibling cleaned up")

    monkeypatch.setattr(generationengine.client, "GenerationClient", Client)
    monkeypatch.setattr(writer, "annotate_group", group)
    args = SimpleNamespace(
        units=source, out_dir=tmp_path / "output", group_size=2, concurrency=2, limit=None,
    )
    sibling_started = asyncio.Event()
    with pytest.raises(ExceptionGroup) as failure:
        asyncio.run(writer.run(args))
    assert str(failure.value.exceptions[0]) == "invalid cache"
    assert events == ["sibling cleaned up", "closed"]
