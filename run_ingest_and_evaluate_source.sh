#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
ENV_FILE="$ROOT_DIR/../.env.development"
SOURCE_DIR="$ROOT_DIR/Rules/StarFinder2e/PlayerCore/source"
OUTPUT_ROOT="$ROOT_DIR/Rules/StarFinder2e/PlayerCore/outputs"
RUN_SLUG="$(date +%Y-%m-%d_%H-%M-%S)"
RUN_DIR="$OUTPUT_ROOT/runs/$RUN_SLUG"
REPORT_DIR="$RUN_DIR/reports"
RULESET_ID="sf2e-playercore"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck source=/dev/null
  source <(grep -E '^[A-Za-z_][A-Za-z0-9_]*=' "$ENV_FILE")
  set +a
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "❌ Source directory not found: $SOURCE_DIR"
  exit 1
fi

if [[ -z "${OPENAI_API_KEY:-}" ]]; then
  echo "❌ OPENAI_API_KEY is required for --auto-config and LLM enrichment."
  exit 1
fi

mkdir -p "$RUN_DIR"

echo "📄 Running rules ingestion pipeline on all PDFs..."
cd "$ROOT_DIR"
shopt -s nullglob
pdfs=("$SOURCE_DIR"/*.pdf)
if [[ ${#pdfs[@]} -eq 0 ]]; then
  echo "❌ No PDFs found in $SOURCE_DIR"
  exit 1
fi

for pdf_path in "${pdfs[@]}"; do
  stem="${pdf_path##*/}"
  stem="${stem%.pdf}"
  safe_stem="$(echo "$stem" | tr ' ' '-' | tr -cd 'A-Za-z0-9-')"
  doc_id="sf2e-playercore-${safe_stem}"
  echo "➡️  Processing: $stem"
  uv run python rules_ingestion_pipeline.py "$pdf_path" \
    --output-dir "$RUN_DIR" \
    --doc-id "$doc_id" \
    --auto-config \
    --ruleset-id "$RULESET_ID" \
    --llm-pre-enrich \
    --llm-review \
    --llm-review-limit 10
done

echo "🧩 Merging enriched outputs..."
uv run python merge_enriched_outputs.py \
  --enriched-dir "$RUN_DIR/enriched" \
  --output-prefix "merged"

echo "📊 Running embedding benchmarks (qwen, nomic, gte) with strict + expanded gold..."
cd "$ROOT_DIR/../DungeonMindServer"
uv run python -m ruleslawyer.evaluation_harness \
  --queries-dir "$RUN_DIR/enriched" \
  --chunk-source enriched \
  --model-id qwen3-embedding-0.6b \
  --model-id nomic-embed-text-v2 \
  --model-id gte-multilingual-base \
  --model-name Qwen/Qwen3-Embedding-0.6B \
  --model-name nomic-ai/nomic-embed-text-v2-moe \
  --trust-remote-code \
  --both \
  --report-dir "$REPORT_DIR"

echo "✅ Benchmark complete."
