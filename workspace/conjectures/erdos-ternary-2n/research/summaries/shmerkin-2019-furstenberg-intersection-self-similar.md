# Shmerkin, "On Furstenberg's intersection conjecture, self-similar measures, and the L^q norms of convolutions"

Source: Annals of Mathematics 189 (2019) 319–391, DOI 10.4007/annals.2019.189.2.1. Full text (HTML abstract capture): `research/sources/shmerkin-2019-furstenberg-intersection-self-similar.full.md`.

## What it establishes

- Settles Furstenberg's intersection conjecture: for `×p`- and `×q`-invariant closed `A, B ⊂ [0,1]` with `log p / log q ∉ ℚ`, `dim_H((uA+v)∩B) ≤ max{0, dim_H A + dim_H B − 1}` — the same statement Wu proved, via an independent route through `L^q` dimensions of dynamically driven self-similar measures (extending Hochman's inverse theorem for entropy; uses Tao–Vu asymmetric Balog–Szemerédi–Gowers and Bourgain constructions).
- Among other applications: Bernoulli convolutions have an `L^q` density for all finite `q` outside a zero-dimensional set of exceptions.

## What it does NOT do for this problem

Same limitation as Wu and as Lagarias's dimension theorems (see `LAGARIAS-DIMENSION-SET-NOT-INTEGERS`): it bounds the **dimension** of the intersection of two ×p / ×q-invariant subsets of `[0,1]`. Erdős's conjecture needs a statement about which **integers** `n` have `2^n ∈ S` (the digit-{0,1} Cantor set in `Z_3`). The dimension result does not say `1 ∉ E(Z_3)` nor that `2^n ∉ S` for n > 8. It is the flagship ×2×3 result and confirms the dimension landscape, but it is not a route to the conjecture.

## Status

Sourced, peer-reviewed (Annals). Full text is an abstract-level HTML capture; theorem statement reliable, method details not fully in library.

```claim
id: SHMERKIN-FURSTENBERG-LQ
statement: Furstenberg's intersection conjecture settled via L^q dimensions of
  dynamically driven self-similar measures: for ×p/×q-invariant closed A,B in
  [0,1] with log p/log q ∉ ℚ, dim_H((uA+v)∩B) ≤ max{0, dim_H A + dim_H B − 1}.
hypotheses: A,B closed, respectively ×p- and ×q-invariant, p,q multiplicatively
  independent.
holds-here: yes as a dimension theorem (p=2,q=3); same as Wu — bounds set
  dimension, not which integers lie in S. Not a route to the conjecture.
status: proved (Annals 2019)
bearing: independent confirmation of the ×2×3 dimension bound; reinforces the
  standing limitation that dimension statements about S or the exceptional set
  cannot be the deliverable.
anchor: research/sources/shmerkin-2019-furstenberg-intersection-self-similar.full.md
follows-from: WU-FURSTENBERG-INTERSECTION
```
