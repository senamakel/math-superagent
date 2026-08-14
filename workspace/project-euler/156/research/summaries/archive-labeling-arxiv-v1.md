# Khovanova & Marton, "Archive Labeling Sequences" — arXiv v1 (superseded)

**Source:** https://arxiv.org/pdf/2305.10357v1 (arXiv:2305.10357v1 [math.HO], 25 Apr 2023). Full text: `research/sources/archive-labeling-arxiv-v1.full.md`.

## What it establishes (and why the run does not use it)

- v1 contains the paper's core material up through its Section 8: the VHS-sticker/Google-Labs motivation, the definitions of f_d(x), a≥(d), a=(d), and (for the run, incidentally) early Lemma 5.1: for x > 10^10, z(x + 10^10) ≥ z(x) + 10^10 — the "translation by 10^10 adds at least 10^10 count" fact behind the periodicity; Theorem 5.2 (a=(0) not well-defined); Lemma 6.1 (the skip lemma in z-notation).
- **It does NOT contain Section 9** ("All Your Base", the base-b bound with Prop 9.1 as numbered in v2). The summary's Section 9 numbering in v1 differs; the v1 document ends without the bound x ≤ d·b^b and without the base-b proof.

## Why this matters here

- The finite search bound the run's G2 rests on (x ≤ d·10^10) is proven in **v2 / the published AMM version**, not in v1. Anyone opening v1 while looking for Prop 9.1 will not find it. Use `research/sources/archive-labeling-arxiv-latest.full.md` (v2) or the published `archive-labeling-amm-published.full.md`.
- v1's Lemma 6.1 is propositionally the same skip fact as v2's Lemma 7.1 (that v2 restates in the run's notation); v1 is a faithful record of the paper's development but adds nothing v2 lacks.

## Does not settle

- Nothing that v2 does not already establish more completely; treat as historical preprint, not the citation for the bound.