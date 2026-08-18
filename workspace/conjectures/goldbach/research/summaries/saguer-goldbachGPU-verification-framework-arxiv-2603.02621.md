> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/saguer-goldbachGPU-verification-framework-arxiv-2603.02621.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2603.02621 | converted from HTML -->

## What is in it

- Computer Science > Mathematical Software
- Title: GoldbachGPU: An Open Source GPU-Accelerated Framework for Verification of…
  - Submission history
  - Access Paper:
    - Current browse context:
    - References & Citations
  - BibTeX formatted citation
    - Bookmark
- Bibliographic and Citation Tools
- Code, Data and Media Associated with this Article
- Demos
- Recommenders and Search Tools
- arXivLabs: experimental projects with community collaborators


## What it claims

Abstract: We present GoldbachGPU, an open-source framework for large-scale computational verification of Goldbach's conjecture using commodity GPU hardware. Prior GPU-based approaches reported a hard memory ceiling near 10^11 due to monolithic prime-table allocation. We show that this limitation is architectural rather than fundamental: a dense bit-packed prime representation provides a 16x reduction in memory footprint, and a segmented double-sieve design removes the VRAM ceiling entirely. By inverting the verification loop and combining a GPU fast-path with a multi-phase primality oracle, the framework achieves exhaustive verification up to 10^12 on a single NVIDIA RTX 3070 (8 GB VRAM), with no counterexamples found. Each segment requires 14 MB of VRAM, yielding O(N) wall-clock time and O(1) memory in N. A rigorous CPU fallback guarantees mathematical completeness, though it was never invoked in practice. An arbitrary-precision checker using GMP and OpenMP extends single-number verification to 10^10000 via a synchronised batch-search strategy. The segmented architecture also…

Comm…

*[digest of a 7292 character source; every section, statement, and proof in full at `research/sources/saguer-goldbachGPU-verification-framework-arxiv-2603.02621.full.md`]*
