# Thread: Uniformity bound from Garcia-Fritz–Pasten on the Robertson curve

```thread
question: Does the Garcia-Fritz–Pasten theorem (Theorem 1.8: AP length ≤ C^(r+1) on
  elliptic curves) combine with the Robertson reduction to give a finiteness
  result for the 3×3 MSS?  Specifically: a full MSS requires an AP of length 3
  on the Robertson curve E_e: y² = x(x²−e⁴).  If rank(E_e) can be bounded from
  above by something provably small, then length-3 APs may be ruled out by the
  C^(r+1) bound if C can be made effective and small enough.

status: effective-constant-advance-hms-2026

rests_on: robertson-elliptic-reduction, bremner-conjecture-proved,
  hms-2026-bremner-effective-constant, patterns-bremner-2026-no-mismatch-for-2E-Q

resolved-questions:
  - doubled-point-x2P: RESOLVED 2026-08-13 (director, from the paper on disk).
    GFP §1.1 defines an AP as "a sequence of points P₁,…,P_M in E(Q) whose
    x-coordinates… form a non-trivial arithmetic progression in Q." The Robertson
    reduction requires an AP of x(2Qᵢ) with Qᵢ ∈ E(Q). Since 2Qᵢ ∈ E(Q), set
    Pᵢ = 2Qᵢ — the GFP theorem bounds every AP in E(Q) including those from
    doubled points. No mismatch. The approach is sound on definitions.
  - effective-constant-hms: RESOLVED 2026-08-13 (director, from HMS full text
    on disk). Harrison–Mudgal–Schmidt (arXiv:2603.06483, 132KB HTML,
    Theorem 1.1) proves Bremner's conjecture with an **effectively computable**
    constant C ≥ 1: any AP, GP, or consecutive squares in x- or y-coordinates
    of a rank-r E/Q has length ≤ C^(1+r). This advances GFP's ineffective C
    to an effective one — the bound is in-principle decidable. However, C is
    built from David–Philippon + PFR constants and is almost certainly >> 3,
    so C^(r+1) < 3 fails for any plausible rank. Corollary 2.2 extends to
    generalised arithmetic progressions of arbitrary rank k. Corollary 2.2
    gives the bound |P| ≤ D^(1+r) for proper GAPs P in C(Γ) — this applies
    to the four-centre-AP configuration with the stronger conclusion that
    even a generalised AP meeting the MSS conditions would be bounded.
    Research request exact-reduction-magic-507c is now CLOSED: the
    definitional question is settled (GFP/HMS apply to doubled points), and
    the constant-size blocker is identified precisely.
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
    P ∈ E(Q)) applies VERBATIM, and HMS Theorem 1.1 (effective constant) likewise.
    The uniform-height approach is NOT refuted on the "x(2P) vs x(P)" crux.
    Its only blocker is the constant size: C is astronomically large
    (David–Philippon + PFR), so C^(r+1) < 3 is false for any plausible r.

immediate-steps:
  0. DP07 lane (2026-08-13, librarian): GGK state on p. 3 that David–Philippon
     (IMRP 2007, Thm 1.13) is the ONLY prior uniform-ML result with a completely
     explicit constant, for subvarieties of self-products of a single elliptic
     curve — the shape of the MSS AP-of-x-coordinates condition (a curve in E^2
     cut out by x(P1)−x(P0) = x(P2)−x(P1)).  Obtain DP07's statement + constant
     and check whether its explicit C can reach C^(1+r) < 3 for the ranks
     attainable by E_c.  Until this is done the effective-constant blocker stands:
     DGH (genus ≥ 2 only), Kühne (g ≥ 2), GGK (existential c(g,d)) and HMS
     (effective but astronomically large, David–Philippon + PFR based) all fail
     to give C^(1+r) < 3.  This is the one open lane to turn the uniform bound
     into a numerical contradiction.
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