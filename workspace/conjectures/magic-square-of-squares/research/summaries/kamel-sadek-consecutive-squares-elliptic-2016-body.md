# Kamel & Sadek, "On sequences of consecutive squares on elliptic curves", Glasnik Matematički 52(1) (2017) 45–52

Source: arXiv:1602.05862 (2026-08 full text html at
`research/sources/kamel-sadek-consecutive-squares-elliptic-2016-body.full.md`;
journal ref Glasnik Matematički Series III 52/1 (2017) 45–52, so it is
peer-reviewed). Published journal paper; claim extracted below is
`kamel-sadek-consecutive-squares-rank-5`, status proved.

## What it establishes

For C/Q in the affine family `y² = a x³ + b x + c`, a **sequence of consecutive
squares** on C is `(x_i, y_i) ∈ C(Q)`, `i=1..n`, with `x_i = (u+i)²` for a fixed
`u ∈ Q` (Definition 2.1, 2.3).

- **Proposition 2.2 (finiteness):** any such sequence is finite. Reducing
  `y² = a x³+b x+c` under `x ↦ x²` gives the genus-2 hyperelliptic curve
  `C: y² + a₁x²y + a₃y = x⁶ + a₂x⁴ + a₄x² + a₆`, and the sequence points become
  points `(u+i, y) ∈ C(K)`; by Faltings such a curve has finitely many K-points.
- **Corollary 3.4 (main):** for any non-trivial 5-term sequence of consecutive
  rational squares `t₀²,(t₀+1)²,(t₀+2)²,(t₀+3)²,(t₀+4)²`, there are **infinitely
  many** elliptic curves `E_m: y² = a_m x³ + b_m x + c_m` (`m ∈ Z∖{0}`) whose
  five `x`-coordinates `(t₀+i)²` are the x-coordinates of rational points; those
  five points are **linearly independent** in `E_m(Q)`, so `rank E_m(Q) ≥ 5`
  (Remark 3.5).
- The construction runs through an elliptic surface over `Q(t,p,q,w)` of
  **positive rank** (Theorem 3.3), then specialises to `E_m` and uses
  Silverman's specialisation theorem to transfer a non-torsion point. One
  explicit member: `E₁` with the five points `(1²,d),(2²,e),(3²,f),(4²,g),(5²,h)`
  all rational (Corollary 3.4 proof).

## Adjacent context the paper documents (cited, not proved here)

- **Long APs of x-coordinates on elliptic curves exist.** The introduction
  records that *infinitely many elliptic curves with length-8 arithmetic
  progressions of rational points* are known (attributions: Bremner,
  Experiment. Math. 8 (1999) 409–413 for arithmetic-progression sequences;
  Campbell, MacLeod, Ulas for longer quartic-elliptic constructions up to
  14-term APs).
- **Bremner's question** (Bremner 1999, Experiment. Math. 8): does a sequence
  of rational points in E(Q) exist whose x-coordinates form an AP in Q, and how
  long can it be / on how many curves? This is precisely the setting of the
  `uniformity-bremner-ap-bound` thread and of the Garcia-Fritz–Pasten / HMS
  AP-length theorems (`bremner-conjecture-proved`, `hms-2026-bremner-effective-constant`).

## Bearing on THIS problem

Three points:

1. **A generic "APs of x-coordinates are short" argument is provably dead.**
   Since infinitely many elliptic curves admit APs of length ≥ 8 (cited
   results) and consecutive-square sequences of length 5 (this paper, rank ≥ 5),
   the obstruction for the 3×3 MSS is **not** that APs of x-coordinates on
   elliptic curves are generically short. The force in the
   `uniformity-bremner-ap-bound` thread must come from the SPECIFIC
   `2E(Q)`-membership of the three points, AND from the specific curve family
   `E_c: y² = x(x²−c²)` (or `E: y²=x(x²−c²)` with c the AP difference), NOT from
   a generic AP-length bound alone. This matches the thread's "risks" row and
   the CLOSED `exact-reduction-magic-507c` conclusion (a length-3 AP is the
   minimal non-trivial length; C^(1+r) < 3 is unobtainable). Note however the
   present paper's family `y² = ax³+bx+c` is the general one, not the special
   `x(x²−c²)` form the MSS requires — the incompatible-with-MSS point is that
   the constructions here are for the general family, giving no direct bearing
   on the special congruent-number-form curve.
2. **The doubled-point caveat is untouched.** The paper's points are ordinary
   points of E(Q); it says nothing about forcing them into `2E(Q)` (the MSS
   requirement, `robertson-elliptic-reduction`). So it provides existence of
   long APs but not of long APs of doubled points — the hard part remains.
3. **A precedent for "rank ≥ 5 from long square sequences".** If a way were
   ever found to force `2E(Q)` membership for such a 5-term sequence, this paper
   is the template for the rank argument. Not directly actionable now.

## What would falsify the extract

A 5-term consecutive-square sequence on a curve of the special form
`y² = x(x²−c²)` with all points in `2E(Q)` would not falsify this claim (the
claim is about the general family) but would change its bearing — nothing in
CONTEXT.md's Established section claims any such sequence on the special form,
and none is known.
