# Hu & Shen, "Erdős-Gyárfás Conjecture for P_{10}-free Graphs", Discrete Math. 347 (2024) (arXiv:2308.05675)

[[research/sources/hu-shen-P10-free-erdos-gyarfas.full.md]] · source URL: https://doi.org/10.48550/arxiv.2308.05675

## What it establishes

Every **P10-free graph with minimum degree at least 3 contains a cycle of length 4 or 8**. Since 4 and 8 are powers of two, the Erdős–Gyárfás conjecture holds for the class of P10-free graphs.

## Why it matters

This is one of the settled restricted classes (between Gao–Shan's P8-free and Hegde–Sandeep–Shashank's P13-free). It fills the chain: P8-free (Gao–Shan 2022) → P10-free (Hu–Shen 2023/2024) → P12-free (stronger C4-or-C8, Hegde et al.) → P13-free (Hegde et al. 2024). The library previously cited this class only via abstracts; now the primary arXiv full text is on disk.

Method note: the proof is structural (longest induced paths/cycles, θ-graph and hole-length analysis), NOT computer-assisted — unlike the P13-free result. Worth distinguishing in ROOT.md: P8, P10, P12 are structural proofs; P13 is computer-assisted.

**Claim block** (fenced for CLAIMS.md):

```claim
id: EG-P10-free-C4C8
statement: Every P10-free graph G with δ(G)≥3 contains a cycle of length 4 or 8; hence the Erdős–Gyárfás conjecture holds for P10-free graphs.
hypotheses: G simple, P10-free (no induced path on 10 vertices), δ≥3.
holds-here: yes — this is a settled restricted class; a candidate minimal counterexample cannot be P10-free.
status: proved (source; primary arXiv full text on disk)
bearing: one of the chain P8/P10/P12/P13-free settled classes bounding where a counterexample can live.
anchor: research/summaries/hu-shen-P10-free-erdos-gyarfas.md
```
