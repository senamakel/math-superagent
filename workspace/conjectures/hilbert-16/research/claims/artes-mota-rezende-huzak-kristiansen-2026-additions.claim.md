```claim
id: artes-mota-rezende-2024-infinite-nilpotent-normal-form
statement: >
  Every nondegenerate quadratic system with three real finite singular points
  plus either an infinite nilpotent elliptic-saddle or an infinite nilpotent
  saddle (class Q̂ES(A)) is brought by affine transformations and time rescaling
  to the 3-parameter normal form
    x' = cx + y − cx²,
    y' = ex + (−1 + (e+f)/c)y − ex² + 2xy,
  with c ∈ ℝ∖{0}, f ∈ ℝ⁺∪{0}, e ∈ ℝ. Portrait counts per Theorems 1–3:
  closures Q̂ES(A)¯/Q̂ES(B)¯/Q̂ES(C)¯ have 91/27/12 topologically distinct phase
  portraits; the classes themselves have 18/10/4; the bifurcation partitions of
  the normal forms (5)/(9)/(13) have 1274/89/14 parts. (Earlier draft of this
  claim said "Q̂ES(B) 8, Q̂ES(C) 14" — that matches none of these; corrected
  2026-08-18 against the held full text.) The normal form is derived from
  invariant-theoretic canonical form 10 of the
  Artés–Llibre–Schlomiuk–Vulpe book via invariants μ0=0, μ1≠0, η=0, M̃≠0, κ=0.
hypotheses: >
  Real quadratic polynomial differential systems; exactly one elemental
  infinite singular point and one triple infinite singular point of infinite
  nilpotent elliptic-saddle (types (1|2)^PHP-E, (1|2)^H-E, (1|2)^PEP-H) or
  nilpotent-saddle ((1|2)^HHH-H) type; nondegenerate finite singularities
  (family A: three real; B: one real + two complex; C: one real triple).
holds_here: yes
evidence: asserted-by-source (held full text, arXiv:2312.01222, IJBC 34(11):2430023, 2024)
falsifies: >
  A source showing the normal form is incomplete (a quadratic system of the
  class not reducible to it), or a different portrait count for the closures,
  or a corrigendum retracting the classification.
answers: null
note: research/sources/artes-mota-rezende-infinite-nilpotent-saddles-ar5iv.full.md
  (Prop 2, Theorems 1-3); librarian note research/librarian-cycle-2026-08-18-library-additions.md
bearing: >
  Normal-form classification of the infinite-nilpotent singularity class
  relevant to the open DRR graphics (I¹₆b),(H³₁₃),(DI₂b) through triple
  nilpotent points at infinity; supplies the exact algebraic normal forms the
  displacement-function analysis can start from.
```

```claim
id: huzak-kristiansen-2025-degenerate-entry-exit-dulac
statement: >
  For the planar slow-fast system (6.1) with invariant line y=0, turning point
  at x=0, and slow flow having a saddle-node of even order 2n: for n=1 there is
  a well-defined entry-exit relation as ε→0 and the associated Dulac map is
  smooth in (ε, ε log ε⁻¹); for n≥2 the entry-exit relation requires additional
  control parameters. Applied to the DRR graphics (I¹₂) and (I¹₄) through a
  nilpotent saddle-node at infinity (5-parameter family (6.2), invariant
  parabola y = ½x² − C₀/2): Theorem 6.1 gives the Dulac map
    Δ(x_in, ε) = Δ₀(x_in) + φ(x_in, ε, ε log ε⁻¹),
  φ C^k-smooth, φ(·,0,0)=0, with Δ₀ in closed form (Eq 6.8)
    x_out = −√( 2δ + e^{2K}(x_in²−2δ) / (β(e^K+1)√(x_in²−2δ) − 1)² ),
  K = λ₁π/√(−4λ₀−λ₁²), valid for x_in ∈ (0, 1/(β(e^K+1))).
hypotheses: >
  Planar slow-fast systems with invariant line {y=0}, turning point x=0, slow
  flow x' = −x^{2n}(1+o(1)); parameters 4λ₀+λ₁²<0, β>0, δ>0, small ε>0;
  DRR graphics (I¹₂),(I¹₄): A close to 1, C close to C₀>0, μᵢ close to 0 in
  family (6.2); n=1 entry-exit well-defined.
holds_here: yes
evidence: asserted-by-source (held full text, arXiv:2510.02770, 2025; numerical
  verification Matlab ODE15s tol 10⁻¹² reported in source)
falsifies: >
  A counterexample to the entry-exit formula (6.8) at n=1, a source showing the
  n≥2 conclusion wrong, or a corrigendum retracting Theorem 6.1.
answers: null
note: research/sources/huzak-kristiansen-degenerate-turning-point-2025.ar5iv.full.md
  (Sec 6, Thm 6.1, Eq 6.8); librarian note research/librarian-cycle-2026-08-18-library-additions.md
bearing: >
  Explicit Dulac-map entry-exit formula for two DRR graphics through nilpotent
  saddle-nodes at infinity — the displacement-map control needed for cyclicity
  arguments; methods transfer toward the open center-type infinite-nilpotent
  graphics.
```
