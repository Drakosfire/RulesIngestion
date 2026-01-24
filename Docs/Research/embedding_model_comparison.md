
# Embedding Model Comparison for TTRPG Ingestion

This report evaluates several leading text embedding models for their suitability in ingesting and retrieving content from tabletop roleplaying game (TTRPG) rulebooks. The evaluation considers multilingual support, input length, layout complexity, retrieval performance, licensing, and CPU inference efficiency.

## Evaluation Criteria

- **Semantic performance** on long-form, structured English text
- **Multilingual support** (not required but noted)
- **Input length and layout awareness**
- **Dense vs. sparse vs. hybrid vector support**
- **Licensing for commercial use**
- **CPU inference efficiency**
- **Support for RAG, semantic search, and classification**

## Summary Comparison Table

| Model                     | Max Length | Dim | License      | Highlights                                                                 | Notes                                                    |
|--------------------------|------------|-----|--------------|---------------------------------------------------------------------------|----------------------------------------------------------|
| **BGE-M3**               | 8192       | 1024| MIT          | Dense, sparse, multi-vector; long input, multilingual                     | Heavy for long docs, mature but older                    |
| **Qwen3-Embedding-0.6B** | 4096+      | 32-1024| Apache 2.0 | Instruction-aware; multilingual; reranker compatible                      | Prompt formatting matters                               |
| **EmbeddingGemma-300M**  | 2048       | 128-768| Apache 2.0 | Edge-device capable, low memory usage                                     | Smaller input size                                      |
| **Jina Embeddings v4**   | 4096+      | 128-2048| CC-BY-NC 4.0| Multimodal (text/image); adapter-based tasks                              | Non-commercial unless hosted via Jina                   |
| **all-mpnet-base-v2**    | 384        | 768 | Apache 2.0   | Proven sentence model, fine-tunable                                       | Short context, limited structure                        |
| **gte-multilingual-base**| 512        | 768 | Apache 2.0   | Compact, multilingual, elastic sparse + dense                             | Limited structured output                              |
| **Nomic Embed Text V2**  | 512        | 256-768| MIT         | Mixture-of-Experts, fast, compact                                         | Prompt formatting needed                                |

## Recommendations

- **Continue with BGE-M3** if performance is strong and long document support is essential.
- **Evaluate Qwen3-Embedding-0.6B** if you want instruction-aware behavior with good performance on structured input.
- **Consider Nomic Embed Text V2** for modern, efficient dense retrieval with open license and low memory footprint.
