# RLH-04 bounded cited-retrieval comparison

**Verdict:** product-ready for the exact SRD occupancy slice. Stable run digest: `7d9c7460bc0a81d08889626e3ea99f461ab02b0f78f66fbebc86508d53e3dbd4`.

The benchmark uses the single Stage B EvidenceUnit from the SRD 5.2.1 occupancy paragraph. Its first two queries are the canonical grounding questions in `Docs/Design/occupancy_vertical_slice_v1.md`. Three further questions probe paraphrase and the unsupported prone-ally allowance; that last question still requires the paragraph as evidence for a negative answer. One unrelated query expects an explicit no-result response.

DungeonMind is pinned to `54a419f99057d96e0c4e7620d8bd8ccc6816fb62`, semantic profile `rules.occupancy@1`, and published revision `rev:77293aef29dd5324f6b300da1ac970aa`. Search runs under a revision-pinned `KnowledgeReadContext`, then `EvidenceReadService` opens each admitted assertion's evidence. Every returned citation maps reversibly to EvidenceUnit `04786f12722f6b15ccb70b18995b060e473ac07115b43dfdba3ca59ae685061d`, the exact source artifact/revision, and the official PDF URI.

At top 3, both DungeonMind and the existing RulesIngestion BM25 implementation recovered the required EvidenceUnit for all five evidence-bearing queries; each scored MRR 1.0. DungeonMind returned no evidence for the unrelated query. The current `retrieval_lab.sparse_retrieval.bm25_rank` returned the sole corpus unit even for that zero-evidence query, so its no-result score was 0/1. Repeated DungeonMind reads at the frozen revision had identical membership and order. The Retrieval Lab benchmark sidecar validated with no missing gold IDs.

The one-unit corpus makes this a bounded product gate, not evidence of general ranking quality or parity with the mature PHB dense/hybrid baseline. That PHB substrate is absent from this owner checkout, and this SRD fixture has a different source identity. Latency is telemetry in the JSON artifact and excluded from its stable run digest. The follow-on graph experiment may assess broader retrieval or reasoning value independently.
