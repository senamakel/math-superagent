# Thread: Uniformity bound from Garcia-Fritz–Pasten on the Robertson curve

```thread
question: Does the Garcia-Fritz–Pasten theorem (Theorem 1.8: AP length ≤ C^(r+1) on
  elliptic curves) combine with the Robertson reduction to give a finiteness
  result for the 3×3 MSS?  Specifically: a full MSS requires an AP of length 3
  on the Robertson curve E_e: y² = x(x²−e⁴).  If rank(E_e) can be bounded from
  above by something provably small, then length-3 APs may be ruled out by the
  C^(r+1) bound if C can be made effective and small enough.

status: resolved-effectiveness-blocks-non-existence

rests_on:
  - robertson-elliptic-reduction (Established)
  - bremner-conjecture-proved (Garcia-Fritz–Pasten Theorem 1.8, newly downloaded)
  - height-uniform-mordell (Dimitrov–Gao–Habegger 2020)
  - uniform-mordell-lang (Gao–Ge–Kühne 2021)

resolved-questions:
  - doubled-point-x2P: RESOLVED 2026-08-13 (director, from the paper on disk).
    GFP §1.1 defines an AP as "a sequence of points P₁,…,P_M in E(Q) whose
    x-coordinates… form a non-trivial arithmetic progression in Q." The Robertson
    reduction requires an AP of x(2Qᵢ) with Qᵢ ∈ E(Q). Since 2Qᵢ ∈ E(Q), set
    Pᵢ = 2Qᵢ — the GFP theorem bounds every AP in E(Q) including those from
    doubled points. No mismatch. The approach is sound on definitions.
  - curve-form-and-rank: CLARIFIED/VERIFIED 2026-08-13 (tool_builder, exact Sage).
    The Robertson curve is E: y² = x(x²−c²) where c is the common difference of
    the anti-diagonal AP {a−c, a, a+c} — NOT the centre e² and NOT e⁴ (the
    thread's "E_e: y²=x(x²−e⁴)" was loose).  For Bremner's 7-square witness:
    centre a = 425², anti-diagonal {205²,425²,565²} ⇒ c = 138600.  Computed:
    E: y² = x³ − 138600²·x has rank 2, torsion order 4.  Main diagonal
    {373²,425²,565²}: x(373²)=139129 and x(425²)=180625 are in 2E(Q) (both
    {X, X±c} all squares); x(565²)=319225 is NOT (X−c=425² square but
    X+c=457825 not a square) — so exactly 2 of the 3 doubled points are
    realised, matching a 7-square near-miss (not an MSS).  This is the
    concrete witness-level check grounding the claim
    `robertson-elliptic-reduction`.
  - crux-applicability: SETTLED 2026-08-13 (tool_builder).  The MSS AP is an
    AP of x(P) for the points P = 2Pᵢ ∈ E(Q) (since Pᵢ ∈ E(Q) ⇒ 2Pᵢ ∈ E(Q)),
    so Garcia-Fritz–Pastén Theorem 1.8 (AP length ≤ C^(r+1) for APs of x(P),
    P ∈ E(Q)) applies VERBATIM.  The uniform-height approach is NOT refuted on
    the "x(2P) vs x(P)" crux.  Its only blocker is the ineffective constant C:
    non-existence needs C^(rankEe+1) < 3, and since C is not explicit (and the
    rank-2 witness curve already contains an AP-3), no contradiction follows.
    Status of approach uniform-height-bound-elliptic-ap:
    adopted-but-ineffective-as-stated.

immediate-steps:
  1. Determine the exact form of the Robertson curve for an MSS centre e.
     The reduction: three points of 2E(Q) on E: y² = x(x²−c²) with
     x-coordinates in AP.  (X,Y) ∈ 2E(Q) iff {X, X±c} are all rational squares.
  2. What is known about rank(E_e) when e = lcm(mᵢ²+nᵢ²) for a putative
     Φ-quadruple?  The K3 surface in Bremner II gives NS rank 12; does this
     bound the rank of the specialised elliptic curve?
  3. The constant C in Theorem 1.8 is NOT explicit in the Garcia-Fritz–Pasten
     paper — it comes from Rémond's quantitative Mordell–Lang bounds as made
     height-uniform by Gao–Ge–Kühne. The Dimitrov–Gao–Habegger constant c(g,d)
     for genus 2, d=1 is also not explicit. So the bound is ineffective for
     computation. Even if C were explicit, it's almost certainly >> 3, so
     C^(r+1) would permit length-3 APs for any plausible r.  The theorem
     reframes the problem as bounding rank(E_e) but does not close it.
  4. Alternative: Theorem 1.2 gives a conditional result: *if* ranks of
     elliptic curves over Q are uniformly bounded, *then* so are AP lengths.
     The uniform rank boundedness conjecture is widely believed (Park–Poonen–
     Voight–Wood heuristic).  If we assume it, the MSS problem reduces to a
     finite computation — though still possibly beyond reach.  This would be
     a genuine partial result: "Assuming uniform boundedness of ranks, the
     3×3 MSS conjecture is decidable by finite computation."

risks:
  - The constant C is ineffective — no numerical contradiction can be extracted
    from Theorem 1.8 alone.  C^(r+1) is almost certainly >> 3 for any plausible
    rank.
  - The MSS requires an AP of length 3, which is the minimal non-trivial length;
    even a moderate C gives C^(r+1) ≥ C² ≥ 4 for r ≥ 1, so length-3 is never
    excluded.
  - The conditional reduction to a finite computation (Theorem 1.2) is genuine
    but the computation is likely beyond reach.

next: scholar to claim-block the GFP paper with exact theorem statements;
  symbolic_math to write the Robertson curve and AP condition as exact
  polynomial equations; research to find rank(E_e) for small e with many
  sum-of-two-squares representations.
```