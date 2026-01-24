
# OCR Model Evaluation for TTRPG PDF Ingestion

This report compares open-source OCR models for extracting structured content from TTRPG rulebooks in PDF format. Focus is on handling tables, columns, font styles, and preserving layout.

## Requirements

- Input: scanned/vector PDFs
- Output: structured layout (tables, columns, bold/italic styles)
- Local CPU/GPU execution
- Open-source licensing for commercial use

## Models Evaluated

### PaddleOCR + PP-Structure

- **Strengths**: table recovery, layout awareness, Markdown/JSON output, reading order
- **Weaknesses**: heavier dependency (PaddlePaddle), prompt formatting critical

### PaddleOCR-VL

- **Strengths**: vision-language parsing, document layout, multi-modal potential
- **Weaknesses**: resource-heavy, no native Docling integration

### DocTR

- **Strengths**: Transformer-based OCR, PyTorch-native
- **Weaknesses**: weaker layout extraction vs. Paddle

### Tesseract (w/ HOCR)

- **Strengths**: lightweight, legacy fallback
- **Weaknesses**: poor layout accuracy, low confidence on modern fonts

### LayoutParser (OCR + structure recovery)

- **Strengths**: composable OCR + layout block detection; table models available
- **Weaknesses**: requires stitching multiple outputs

### Integration with Docling

- Docling uses `RapidOCR`, a lightweight ONNX-based wrapper around PaddleOCR models.
- You can replace the OCR engine via plugin or insert PaddleOCR results as Markdown/JSON into Docling’s structure.
- PaddleOCR's output aligns well with Docling’s internal document model (e.g. for tables and multi-column reading).

## Recommendations

- Use **RapidOCR (PaddleOCR)** with Docling for best out-of-the-box accuracy.
- For high-fidelity table extraction, evaluate **PP-StructureV3**.
- Maintain bounding boxes and styles during extraction for downstream entity recognition.
