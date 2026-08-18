# Artés–Mota–Rezende 2024: infinite nilpotent elliptic-saddle / saddle class — summary

[[artes-mota-rezende-infinite-nilpotent-saddles-ar5iv.full]]

**Source:** J. C. Artés, M. C. Mota, A. C. Rezende, "Phase portraits for
quadratic systems possessing an infinite elliptic–saddle or an infinite
nilpotent saddle", arXiv:2312.01222; IJBC 34(11):2430023 (2024).
Full text: `research/sources/artes-mota-rezende-infinite-nilpotent-saddles-ar5iv.full.md`
(3465 lines); abstract page: `...-arxiv.full.md`. URL: https://arxiv.org/abs/2312.01222

## What the source establishes

**Object.** The class Q̂ES of real quadratic systems with exactly one elemental
infinite singular point and one triple infinite singular point which is an
infinite nilpotent elliptic–saddle (types (1|2)^PHP-E, (1|2)^H-E, (1|2)^PEP-H)
or a nilpotent saddle (type (1|2)^HHH-H). Three families by finite singularities:
Q̂ES(A) three real (3-dim normal form), Q̂ES(B) one real + two complex (3-dim),
Q̂ES(C) one real triple (2-dim).

**Proposition 2 (normal form).** Every nondegenerate quadratic system with three
real finite singular points plus an infinite nilpotent elliptic-saddle or
nilpotent saddle is affinely/time-rescaled to
x′ = cx + y − cx²,  y′ = ex + (−1 + (e+f)/c)y − ex² + 2xy,
c ∈ ℝ∖{0}, f ∈ ℝ⁺∪{0}, e ∈ ℝ (family Q̂ES(A)). Derivation: from invariant-
theoretic canonical form 10 of the Artés–Llibre–Schlomiuk–Vulpe book via the
invariant conditions μ₀=0, μ₁≠0, η=0, M̃≠0, κ=0; the proof is explicit
(translation f = F−1, rescaling (x,y,t)→(x,(m/d)y,t/m), then (x,y,t)→(−x+1,y,−t)).

**Portrait counts (CORRECT, per Theorems 1–3 and the abstract).**
- Q̂ES(A) closure: **91** topologically distinct phase portraits (family A itself:
  **18**); bifurcation partition of normal form (5): **1274** parts.
- Q̂ES(B) closure: **27** portraits (family B: **10**); partition: **89** parts.
- Q̂ES(C) closure: **12** portraits (family C: **4**); partition: **14** parts.
- Ten portraits in A and six in B possess exactly one simple limit cycle; C has
  no limit cycles. Portrait families with one infinite family of nondegenerate
  graphics, degenerate graphics (line filled with singular points), and
  finite+infinite graphic combinations are enumerated.

## What it implies here

- The normal form is a concrete algebraic object for the exact singularity type
  (infinite nilpotent points) that the open DRR graphics (I¹₆b, H³₁₃, DI₂b) pass
  through — a starting point for displacement-function analysis, and a Lean-
  friendly algebraic statement. The classification itself is topological
  (portrait geometry), **not** a cyclicity result: no bound on limit-cycle
  numbers near these graphics is proved here, so it does not close any DRR row.
- The degenerate-graphic portraits (line at infinity filled with singular points,
  e.g. 4.5L₁, P₄₄, 1L₁, P₃, P₁) are the phase-portrait side of the same
  degenerate-singularity phenomena the run studies; useful for choosing the
  normal-form box for the missing second-type Dulac maps, not for the zero count.

## Evidence class
`asserted-by-source` — classification theorems read in the held full text; not
independently formalised or recomputed. Claim
`artes-mota-rezende-2024-infinite-nilpotent-normal-form` (asserted). Falsifier:
a quadratic system of the class not reducible to the normal form, or different
portrait counts, or a corrigendum.

## Correction to the filed claim
The claim block's counts "Q̂ES(B) has 8, Q̂ES(C) has 14" do **not** match this
source. Correct values: closures 91/27/12, classes 18/10/4, partition parts
1274/89/14. The claim has been amended (see `research/claims/artes-mota-rezende-huzak-kristiansen-2026-additions.claim.md`).
