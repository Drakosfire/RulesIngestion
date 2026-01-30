# Blind Evaluation

This directory contains blind evaluation batches for testing the traversal system on unseen queries.

## Protocol

1. **Generate random pages** - Run `generate_pages.py` to get random page numbers
2. **Create questions** - Open PDF, read page, write natural question
3. **Find gold chunk** - Use `find_chunks.py` to identify the gold chunk ID
4. **Add to batch file** - Add entry to `batches/batch_NNN.json`
5. **Commit** - Commit the batch file (no code changes!)
6. **Run eval** - `uv run pytest tests/test_blind_eval.py -v`
7. **Analyze** - Review failures, document root causes

## Directory Structure

```
blind_eval/
├── README.md           # This file
├── generate_pages.py   # Random page generator
├── find_chunks.py      # Helper to find chunks on a page
├── batches/            # Batch JSON files
│   ├── batch_001.json
│   └── ...
└── results/            # Evaluation results
    ├── batch_001_results.json
    └── ...
```

## Batch File Format

```json
{
  "metadata": {
    "batch_id": "001",
    "created_by": "human",
    "pdf_source": "PZO22003_PlayerCore.pdf",
    "created_at": "2026-01-27T10:00:00Z"
  },
  "queries": [
    {
      "id": "blind_001_01",
      "source_page": 142,
      "question": "What happens if I try to cast a spell while grabbed?",
      "gold_chunk_ids": ["sf2e-playercore-chunk-12345"],
      "expected_answer_summary": "Grabbed imposes conditions that affect spellcasting",
      "notes": "Page covers the Grabbed condition"
    }
  ]
}
```

## Running Blind Eval

```bash
# Run all blind eval batches
uv run pytest tests/test_blind_eval.py -v

# Run specific batch
uv run pytest tests/test_blind_eval.py -v -k "batch_001"

# Generate detailed report
uv run python blind_eval/run_eval.py --batch 001 --verbose
```
