# Mohammadian & Tayfeh-Rezaie, "On a family of diamond-free strongly regular graphs" (2013) — summary

**Source**: A. Mohammadian & B. Tayfeh-Rezaie, arXiv:1303.0473 (2013).
Full text held (ar5iv conversion):
`research/sources/mohammadian-diamond-free-srg-ar5iv.full.md`.

> This file is the abstract landing-page record. The complete digest of the
> paper's content lives in `research/summaries/mohammadian-diamond-free-srg-ar5iv.md`
> (claim `diamond-free-srg-iff-pq-2602-grounding`). This note exists so the abstract
> landing page is not mistaken for a separate source.

## What the source establishes (abstract)

The existence of a partial quadrangle PQ(s,t,μ) is equivalent to the existence of a
diamond-free strongly regular graph
`srg(1 + s(t+1) + s²t(t+1)/μ,  s(t+1),  s−1,  μ)`.

- A PQ(2, (n³+3n²−2)/2, n²+n) exists iff n ∈ {1, 2, 4}.
- A PQ(3, (n+3)(n²−1)/3, n²+n) satisfying a specific non-collinearity condition
  exists only for n ∈ {−2, 2, 3} and probably n = 10.

## Bearing on srg(99,14,1,2)

The first equivalence is the load-bearing one: with λ=1, μ=2, s−1=1 ⇒ s=2,
s(t+1)=14 ⇒ t+1=7 ⇒ t=6, μ=2, giving **exactly PQ(2,6,2)** and confirming the
run's adopted `pq-2-6-2-classification` reformulation as a theorem with citation.
See the ar5iv summary for the full derivation and the note that the paper's own
main theorem (λ=2, g=k negative-Latin-square family, n∈{−2,2,3,10}) does NOT apply
to 99 (which has g=44 ≠ k=14, μ=2).

## Status
`sourced` (abstract verified; full text at the ar5iv name), and the (99,14,1,2)→
PQ(2,6,2) parameter solve is verified by hand and by `code/out/check_pq_parameter_map.py`.

**Do not re-fetch**: this is the same paper as the ar5iv record; the full digest is
there.

[[mohammadian-diamond-free-srg-ar5iv.full]]
