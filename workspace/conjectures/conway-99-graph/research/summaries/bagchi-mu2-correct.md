# CORRECTION — Bagchi, "On strongly regular graphs with μ ⩽ 2" (2006)

<!-- source: correction record. Full corrected record at
research/sources/bagchi-mu2-correct.full.md. This summary replaces an
auto-digest of a WRONG download (arXiv:math/0512558, a pre-Lie / left-symmetric
algebra paper by Gichev) that was not about strongly regular graphs. -->

## What this source is

Bhaskar Bagchi, "On strongly regular graphs with μ ⩽ 2," Discrete Mathematics.
Not fully downloadable this run (403). The abstract + proof excerpt were
captured; this is a lead with a serious subtlety, recorded in full in the
sources file and the note `research/notes/bagchi-mu2-dichotomy-resolution.md`.

## Verified theorem (Thm 4)

Any srg with μ = 2 is either a **grid graph** or satisfies **k ≥ 12λ(λ+3)**.
Also: μ = 1 ⟹ k ≥ (λ+1)(λ+2).

## The subtlety (why this does NOT obviously rule out 99)

The grid conclusion is reached only via K₁,₁,₂-freeness: for μ=2 and
k < 12λ(λ+3), a result of Brouwer–Neumaier (1988) makes the graph K₁,₁,₂-free,
and a K₁,₁,₂-free srg is either a GQ collinearity graph or k ≥ (λ+1)(λ+2).
Since a GQ's t+1 = μ = 2, it is a grid.

For (99,14,1,2): k=14 < 48, so IF the graph is forced K₁,₁,₂-free it is a grid —
impossible. But BvLS (243,22,1,2) also has k=22 < 48 and is not a grid, yet
exists — so BvLS must NOT be K₁,₁,₂-free. The whole question reduces to:
**does BvLS contain an induced K₁,₁,₂? (expected yes), and would a putative
99-graph be forced K₁,₁,₂-free?** This is exactly the negative-control test
GOAL demands.

## Status

Bagchi full text not in library; theorem verified from abstract + proof excerpt
only. Lemma 1 and the Brouwer–Neumaier [5] condition are a gap. Do NOT rely on
a naive reading of Thm 4.
