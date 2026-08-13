# Approach: Uniform height bounds via Garcia-Fritz & Pastén (2026)

```approach
idea: Apply the uniform Mordell-Lang / height-uniform Mordell framework
(Dimitrov–Gao–Habegger 2021, Kühne 2021), as specialised by Garcia-Fritz &
Pastén (arXiv:2604.04850, 2026) to arithmetic progressions of x-coordinates on
elliptic curves, to the specific MSS elliptic curve E_c: y² = x(x²−c²).

A 3×3 magic square of squares gives three points in 2E_c(Q) whose
x-coordinates are c−u, c, c+u — an arithmetic progression of length 3.
Garcia-Fritz & Pastén prove (conditional on uniform rank bounds for the
family) that long APs of x-coordinates of rational points force large rank.
For the MSS family with a fixed short AP-length of 3, the theorem runs in
reverse: if the rank of every E_c in the family is bounded by some R, then
the height of any AP-3 configuration is uniformly bounded. If that height
bound is effective, the problem reduces to a finite search — the first
reduction of the full 3×3 MSS to a finite (height-bounded rather than simply
exhaustive) computation that does not go through the K3 surface.

mechanism: The machinery is not the K3 surface, not Chabauty, not root
numbers, and not 2-descent. It is the uniform Mordell-Lang conjecture
(proved independently by Dimitrov–Gao–Habegger and by Kühne in 2021): for a
family of subvarieties of abelian varieties over number fields, the set of
rational points in the subvariety is a finite union of translates of
algebraic subgroups, and — crucially — the number of such components and
their complexity are bounded uniformly across the family. Garcia-Fritz &
Pastén apply this to the specific subvariety of E³ (three copies of the same
elliptic curve) cut out by the condition x(P₁), x(P₂), x(P₃) in arithmetic
progression. The "unlikely intersection" analysis determines whether this
subvariety contains a translate of a positive-dimensional algebraic subgroup
(G_m or E itself). If it does not (i.e. the subvariety is "non-degenerate"),
then the uniform bound applies.

For the MSS problem the three points are not arbitrary — they come from
2E_c(Q), i.e. each x-coordinate is the x-coordinate of 2Q for some Q. The
AP condition is exactly x(2Q₁) = c−u, x(2Q₂) = c, x(2Q₃) = c+u, giving
x(2Q₂) − x(2Q₁) = x(2Q₃) − x(2Q₂) = u. This is a specific subvariety of
E³ × E³ (six copies) with nine coordinates (three x(2Q) in AP plus the
6-point condition). Whether the Garcia-Fritz–Pastén non-degeneracy analysis
applies to this doubled-point variant (rather than to arbitrary points) is
the first thing to verify.

The payoff: if non-degenerate and conditional on rank ≤ R for all E_c, the
height of c, u, v is uniformly bounded, and the 3×3 MSS either does not exist
(if the bound on AP length is < 3) or lives inside an explicitly computable
finite box. This is a fundamentally different type of result from all
previous approaches: it does not attempt to prove non-existence directly but
instead reduces the problem to a finite — possibly enormous but finite —
computation whose size depends on the rank bound R, not on an arbitrary
search parameter.

status: adopted-but-ineffective-as-stated
The crux is RESOLVED in favour of the approach: the MSS AP is genuinely an AP of
x(P) for points P ∈ E(Q) (the doubled points 2P₀, 2P₁, 2P₂ are themselves points of
E(Q)), so Garcia-Fritz–Pastén Theorem 1.8 (AP length ≤ C^(r+1)) applies verbatim;
it is NOT a doubled-point AP outside the theorem's scope.  The blocker is no longer
non-degeneracy but EFFECTIVENESS: C is an absolute constant that is not explicit in
the paper, and the inequality C^(rankEe+1) < 3 would be needed for non-existence.
The Bremner-witness curve (rank 2) already admits an AP of length 3 in E(Q) whose
x-coords are a−b,a,a+b (realising 2 of the 3 doubled points), so any C with C^3 ≥ 3
is compatible with reality — as is any plausible effective C.  Without an explicit
C (or a rank bound forcing C^(r+1) < 3), the bound C^(r+1) cannot be checked
against 3, and the approach proves a theorem that may be true but is not
computationally actionable.  Crux-resolution and witness ranks:
research/summaries/bremner-on-squares-of-squares-1999.md claim `robertson-elliptic-reduction`.
killed-by: —

resolution: crux-resolved; effective-C gap remains
speculation-vs-established: ESTABLISHED (literature): Dimitrov–Gao–Habegger
  (2021) and Kühne (2021) proved the uniform Mordell-Lang conjecture;
  Garcia-Fritz & Pastén (2026, arXiv:2604.04850) apply it to APs of
  x-coordinates on elliptic curves, giving a uniform bound conditional on
  uniform rank bounds, with explicit constants for the family y² = x³ + ax + b
  over Q. SPECULATION: (a) that the Garcia-Fritz–Pastén non-degeneracy
  analysis extends from arbitrary points to points in 2E(Q) — the
  doubled-point condition changes the subvariety; (b) that the explicit
  constant C(R) for the family E_c: y² = x(x²−c²) (c a square) yields a
  bound B(R) on AP length with B(R) < 3 for some plausible small R; (c) that
  a uniform rank bound for the family E_c is available (a major open problem,
  though the family is thin — quadratic twist by squares — so it may reduce
  to bounding the rank of y² = x³ − x over Q-extensions).
first-step: |
  Step 2 below is now DONE (crux resolved): the non-degeneracy question is settled
  in the approach's favour by the reduction itself — the MSS AP points 2P₀, 2P₁, 2P₂
  are points of E(Q), so they fall inside the scope of Theorem 1.8 (APs of x(P),
  P ∈ E(Q)), no separate doubled-point subvariety analysis is needed.  Remaining
  concrete moves, in order:

  1. **Compute explicit C for the family** E_c: y² = x(x²−c²), c a square, in the
     sense of the conditional uniform-rank theorem.  The paper gives the *structure*
     (AP length ≤ C^(r+1)) but C is an absolute constant that is not made explicit
     in garcia-fritz-pasten-bremner-uniformity-2026.full.md.  Determine whether
     C(R, L) — or the underlying Dimitrov–Gao–Habegger constant c(2,1) for genus-2
     curves — has been bounded by anyone (the paper cites [25] Yu–Yuan–Zhou,
     "Quantitativity on the number of rational points", arXiv:2602.01820, for an
     explicit height-uniform bound; check whether that bound is effective enough to
     pin C below 3^(1/(r+1))).

  2. **Bound the rank of** E_e: y² = x(x²−e⁴) (equivalently E_c with c = e²) **for
     e admitting many sum-of-two-squares representations.**  The Bremner-witness
     curve (c = 138600, not a square!) has rank 2; the rank of E_c for c = e²
     (c square) is likely smaller but unboundedness is unproved.  A uniform bound
     R with C^(R+1) < 3 would give non-existence; but the Bremner witness already
     shows rank ≥ 2 curves with AP-3 happen, so R must be small AND C small —
     quantify both before committing further effort here.

  3. **If C and R are in hand**, plug L = 3: "Conditional on rk E_c(Q) ≤ R, any 3×3
     MSS has |entries| ≤ H(R, 3)", a finite computation.  If C cannot be made
     explicit, record the approach as a reduction (MSS ⇒ AP-3 on E_c of bounded
     height, effective bound unavailable) rather than a contradiction — which is
     the honest status.

  Guard: the uniform-rank-boundedness conjecture (ranks of all elliptic curves over
  Q uniformly bounded) is a major open problem; the conditional result is real but
  conditional.  The run must not present an effective-C gap as closed.

precedent:
  - V. Dimitrov, Z. Gao, P. Habegger, "Uniformity in Mordell-Lang for
    curves", Ann. of Math. 194 (2021), 237–298 — proof of uniform
    Mordell-Lang for curves in abelian varieties.
  - L. Kühne, "Equidistribution in families of abelian varieties and
    uniformity", J. Eur. Math. Soc. (2021) — independent proof.
  - N. Garcia-Fritz & H. Pastén, "A note on Bremner's conjecture and
    uniformity", arXiv:2604.04850 (2026) — applies uniform Mordell-Lang
    to APs of x-coordinates on elliptic curves; conditional on uniform rank
    bounds, gives a uniform bound on AP length; explicit constants worked out
    for the family y² = x³ + ax + b.
    (library: research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md)
  - A. Bremner, "On squares of squares II", Acta Arith. 99 (2001) 289–308 —
    the MSS elliptic curve E: y² = x(x²−c²) and the condition that the three
    relevant points lie in 2E(Q).
  - Rome & Yamagishi (2024, arXiv:2406.09364) — n×n MSS exist for all n ≥ 4;
    the 3×3 case is the sole remaining case, confirming that any structural
    obstruction must be specific to n = 3.
  - NOT subsumed by Bremner II (2001): the K3 surface encodes the geometry of
    the generic fibre; uniform Mordell-Lang bounds the height of specific
    rational points on specific fibres using a completely different
    Diophantine-geometric principle (unlikely intersections, not
    Néron-Severi/singular-fibre geometry). The K3 route asks "does S have
    rational points?"; the uniformity route asks "how large can the
    coordinates of a rational point be, given the rank?"
  - NOT subsumed by the refuted root-number-parity approach: root numbers are
    analytic (L-function signs); uniform Mordell-Lang is about heights and
    algebraic subgroups — the two frameworks operate in different categories.
  - Genuinely different from every approach in this run's APPROACHES.md: all
    previous approaches are either geometric (K3, Chabauty, Faltings),
    arithmetic (root numbers, 2-Selmer), or combinatorial (Gaussian integer
    factorisations, S-unit equations). This is the first approach to use the
    uniform Mordell-Lang / unlikely-intersections machinery, which was proved
    only in 2021 and first applied to elliptic-curve AP problems in 2026.
```