# Scholar digest — what the library establishes for the unit-distance colouring problem

This note records, for each source that bears on the problem, what it actually
establishes, whether its hypotheses hold here, and what it lets the run
compute, bound, or rule out. The durable source-backed findings are also stored
in Cognee via `remember_memory`. This is the synthesis a later agent reads to
avoid re-deriving or re-fetching.

## Fractional chromatic tier — the adopted LP route (new this run)

**`fractional-chromatic-number-lp-definition.md`** (claims
`fractional-chromatic-lp-duality`, `fractional-chromatic-chain`, both
`asserted` from four agreeing primary treatments) fixes the mechanism the
adopted `fractional-chromatic-lp-lower-bound` approach rests on: `chi_f(G)` is
the optimum of the independent-set covering LP; its dual (fractional clique
`omega_f`) has the same rational optimum by strong LP duality; and
`max{omega,|V|/alpha} <= rho <= chi_f <= chi`. Because `chi_f` has NO
ceil-identity like `chi = ceil(chi_c)` (which killed the circular-chromatic
line), `chi_f > 4` on a constructible UDG is a one-sided, LP-dual-certifiable
route to `chi >= 5`, strictly easier than 4-colouring SAT. Critical caveat
(from the approach file, not a source theorem): exact `chi_f` computation is
NP-hard in general, cheap here only because n <= ~26 makes the independent-set
polytope enumerable. Calibration values `chi_f(C5)=5/2`, `chi_f(diamond)=3`
(diamond chordal/perfect) are asserted-by-source but **now computed and `checked`**: `chi_f(Moser)=7/2` and
`chi_f(Moser+Moser)=7/2` (both < 4), recorded in
`code/out/fractional-chromatic-values.md` (checked; exact rational dual for
Moser — `frac_chro_verify_rational.txt`). This retires the "OPEN computation"
status. [[code/out/fractional-chromatic-values.md]] [[research/sources/fractional-chromatic-number-lp-definition.md]]
[[research/sources/scheinerman-ullman-fractional-chromatic-number.md]]

## Henneberg / rigidity construction grammar (new this run)

**`laman-henneberg-generic-rigidity-theorem.md`** (claim
`laman-henneberg-generic-rigidity`, `asserted`) — a plane graph is generically
rigid iff Laman/(2,3)-tight; every such graph is built from K2 by H1 (add a
vertex on two unit circles — exact quadratic) and H2 (remove uv, add vertex
joined to u,v,w — a circumradius-1 coincidence). **Critical caveat:** the
completeness is *generic* (arbitrary edge lengths), NOT all-unit; there is no
theorem that all-unit Laman graphs are reachable by unit-preserving moves, and
Owen–Power show generic Laman realizations are generally not solvable by
radicals, so H2 pushes the coordinate field beyond tame quadratics. Grounds the
adopted rigidity-matroid-henneberg approach. [[research/sources/laman-henneberg-generic-rigidity-theorem.md]]

## Regular-polytope projection source sets (new this run)

**`regular-4-polytope-projection-quaternions.md`** (claim
`regular-4-polytope-projections`, `asserted`) — 24-cell vertices = 24
permutations of (+-1,+-1,0,0) (exact integers, order 1152, dodecagonal Petrie
projection); 600-cell = 120 unit icosians in Q(sqrt5) (H4, order 14400,
triacontagonal projection). A rank-2 Coxeter-plane projection Q = (a.x)^2+(b.x)^2
is NOT a homothety (different source lengths equalize to one planar length),
so projected sets give genuinely new dense UDGs for the forced-pair harness.
Chromatic number of these projections is uncomputed. First-step check: the
equalization counterexample (24-cell pair under rows a=(0,1,3,0), b=(0,0,0,1))
must reproduce symbolically or the projection line is dead there.
[[research/sources/regular-4-polytope-projection-quaternions.md]]

## Distance-graph origin (new this run)

**`eggleton-erdos-skilton-1985-colouring-real-line.md`** (claim
`eggleton-erdos-skilton-1985-real-line`) — origin paper of G(R,D)/G(Z,D)
distance graphs; `chi(G(Z,D)) <= |D|+1` for finite integer D. Ancestor of the
periodic-tier (Zhu 1998, Barajas–Serra 2005, Liu 2008). Does NOT settle the
open plane unit-distance Hadwiger–Nelson problem — the lattice analogue only.
[[research/sources/eggleton-erdos-skilton-1985-colouring-real-line.md]]

## The two verified run artifacts (not asserted-by-source — machine-checked)

- **Calibration (gating check, PASSED).** 7-vertex Moser spindle, exact
  coordinates in `Q(sqrt3, sqrt11, sqrt33)`, all 11 unit edges certified
  symbolically (no tolerance; full 21-pair scan finds exactly those 11, no
  spurious edge), 4-colourable with witness `[0,1,2,0,1,2,3]`, not 3-colourable.
  Confirmed four independent routes (PySAT Cadical153, Minisat22, brute-force,
  numeric+symbolic rebuild). k-colouring counts agree exactly brute-force == SAT
  (k=1..5: 0,0,0,384,5040). Artifacts in `code/out/`.
  [[code/out/calibrate_moser.captured.txt]]
- **Forced-pair crux is dead for the two bases tried.** Moser spindle (10
  qualifying pairs, k=4) and Moser+Moser sum (26v, 69e, 256 pairs, k=4): NONE
  of the |u-v|>=1/2 pairs is forced monochromatic; the sum is 4-colourable. The
  diamond k=3 base case DOES hold (tips forced equal). A forced pair under 4
  colours needs a strictly richer base graph. [[code/out/forced_pair.captured.txt]]

## Sources and what each establishes

### Finite-to-infinite reduction (the load-bearing step)
- **de Bruijn–Erdős 1951**: `chi(G) = sup{ chi(H) : H finite subgraph }`. For
  the plane graph, `chi(plane) >= 5` iff some finite unit-distance graph is not
  4-colourable. The finite-to-infinite step needs a compactness/choice
  principle (BPIT / Tychonoff / Rado selection; equivalent to BPI, valid in
  ZFC); not needed for the sup direction. holds-here: yes.
  Claim `debruijn-erdos-1951`, asserted-by-source.
  [[research/sources/debruijn-erdos-1951-chromatic-reduction.md]]
  [[research/sources/debruijn-erdos-1951-reduction.md]] (proof-detail duplicate)

- **Komjáth 2010 survey**: fixes the metadata of the reduction and its
  choice-content caveats (higher-infinite chromatic numbers are incompactable;
  Payne constructed a UDG whose chi depends on the axiom system). For the
  finite lower/upper bounds (4 and 7) no choice issue arises. helps: only as
  metadata. [[research/sources/komjath-2010-infinite-chromatic-survey.md]]

### Density cannot be bought
- **Spencer–Szemerédi–Trotter 1984**: `u_2(n) = O(n^{4/3})` max unit distances
  among n plane points. Consequence: a UDG on n vertices has O(n^{4/3}) edges,
  so high chromatic number is not bought by density — it must come from
  algebraic rigidity. Erdős lower bound `n^{1+O(1/log log n)}`. holds-here: yes.
  Claim `unit-distance-upper-bound` (+ `erdos-unit-distance-bound`,
  `matousek-unit-distance-problem` which also records the Székely,
  Clarkson-et-al, Aronov–Sharir alternative proofs).
- **Szemerédi–Trotter incidence theorem 1983**: `I(P,L)=O(m^{2/3}n^{2/3}+m+n)`
  incidences between m points and n lines; equivalently `|L_r| = O(n^2/r^3 + n/r)`
  r-rich lines. The machinery under the unit-distance bound. Claim
  `szemeredi-trotter-incidence`.
- **Sharp ST constructions live on algebraic fields**: Guth–Silier 2025 show
  extremal incidence constructions are algebraic — built from `Q(sqrt k)`
  point sets; and over ANY number field `K/Q` with a product-closed
  (nice/integral) basis. The algebraic closure of the basis is what produces
  density; replacing the algebraic generator by a transcendental collapses the
  construction. This is the sourced justification for searching *algebraic*
  constructions (the run's `Q(sqrt3,sqrt11,sqrt33)` universe) rather than
  random points. Claims `szemeredi-trotter-algebraic-extremal`,
  `number-field-extremal-constructions`.

### Construction engine
- **Minkowski-sum unit-distance condition**: `|(a1+b1)-(a2+b2)|=1 iff
  |(a1-a2)+(b1-b2)|=1` — an immediate vector identity, holds for all A,B. The
  exact computation governing which pairs of A+B are edges. Claim
  `minkowski-sum-unit-distance-condition`. **Verified derived, not asserted.**
- **Minkowski sums give dense UDGs / spindling**: many densest-known small
  UDGs are Minkowski sums (9-vertex triangle+triangle; 21-vertex triangle +
  6-wheel; G_49 = 6-wheel+6-wheel used in a chi>=5 line). A unit distance in
  the sum can arise many ways (density). Rotation of one summand creates extra
  unit distances. Claims `minkowski-sum-dense-graphs` (asserted-by-source).
- **Eisenstein lattice `Z[omega]`**: triangular lattice, norm
  `x^2-xy+y^2`; unit vectors are the six powers of a primitive 6th root
  (all six 60-deg directions, modulus exactly 1); a lattice point is at unit
  distance iff N=1. Exact coordinates in `Q(sqrt(-3))` + symbolic norm checks
  give provable unit edges; the run's 60-deg rotations are its symmetries.
  Claim `einstein-lattice-unit-distance`. NOTE: 3rd vs 6th root distinction —
  omega alone gives only three directions.

### Exact-arithmetic backbone
- **Maehara 1991**: rigid-UDG distances are exactly the algebraic numbers;
  equivalently rigid-UDG coordinates are algebraic (each edge a quadratic with
  rational data). Floating point is never legitimate here. Claim
  `maehara-algebraic-rigid-distances`.
- **Kempe universality / linkages**: the constructive half — every algebraic
  number is realisable, via Kempe-style linkages. Claim `kempe-universality`.
  Boundary: it is about tracing curves, not colouring; carries no chromatic
  statement.
- **Exact O(n^2) certification**: planarity (rank-2) + e_max=0 over edges +
  min separation > 0 + no extra unit distance among non-edges, all exact. The
  published analogue of the run's `unit_graph`. Claim
  `exact-coordinate-certification`.

### Structural colouring theory (size-bound direction)
- **k-critical graphs**: min degree >= k-1, so a 5-critical UDG has min degree
  >= 4 and >= 2n edges; every k-chromatic graph contains a k-critical subgraph.
  Hajós construction classifies k-chromatic graphs but is NOT
  unit-distance-preserving, so the run needs its own construction engine.
  Claims `k-critical-minimum-degree`, `critical-minimum-degree`.
- **Totally unfaithful UDGs**: certificate in the opposite direction — bounds
  which graphs CANNOT be unit-distance embeddings. Claim (none yet in
  CLAIMS.md for this; definition only).

### Method
- **SAT shrinking + spindling (Polymath)**: SAT "4-colouring under which H has
  a monochromatic triple", DRAT core extraction, shrinking, spindling — the
  computer-assisted language that matches the run's forced_pair harness at
  small scale. Claim `sat-shrinking-core-extraction`.
- **SAT k-colourability encoding**: at-least-one + properness CNF, exact and
  complete; independently calibrated by the run. Claim
  `sat-k-colourability-encoding`.

## The established size-bound result (updates the stale N=10 bound)

The run has machine-verified the size-bound deliverable **through N = 11**,
which the older CONTEXT.md / backward notes under-recorded as N=10. Verified
claim blocks in `code/out/census-kernel-n11-result.md` (ids
`sharp-nbhd-local`, `sharp-kernel-4color-n11`, `size-bound-udg-4color-n11`):

**Every unit-distance graph in R^2 on at most 11 vertices is 4-colourable;
every 5-chromatic unit-distance graph has at least 12 vertices.**

Three machine-checked steps: (1) `sharp-critical-degree` — a 5-chromatic graph
contains a 5-critical subgraph with min degree >= 4 (exhaustively verified over
all 33,866 graphs on <= 6 vertices); (2) `sharp-nbhd-local` — a unit-distance
graph is K4-free, K2,3-free, and every neighbourhood induces a graph of max
degree <= 2 (exact sympy/Groebner certificate); (3) `sharp-kernel-4color-n11` —
every graph on <= 11 vertices with min-deg>=4 + K4-free + K2,3-free +
nbhd-maxdeg<=2 is 4-colourable (228 members at n=11, all 4-colourable by
Cadical SAT with proper witnesses AND independent backtracking; enumeration
complete over all 28 residue classes of `nauty-geng 11 -d4`).

Also corrected: `minkowski-sum-unit-distance-condition`, `einstein-lattice-unit-distance`,
`sat-k-colourability-encoding` are `checked` (captured outputs exist), not
`asserted` as the stale CONTEXT noted.

## New this run — Hoffman eigenvalue bound (spectral warm-up of the adopted theta approach)

**Hoffman 1970** (claim `hoffman-eigenvalue-bound`; canonical note now at
`research/sources/hoffman-eigenvalue-bound.md`). For any finite simple graph G
with at least one edge and adjacency eigenvalues `lambda_max >= ... >= lambda_min`,
`chi(G) >= 1 - lambda_max/lambda_min`. General (not necessarily regular) graphs.
This is the cheap polynomial **warm-up/filter** of the adopted
`lovasz-theta-vector-chromatic` approach: RHS > 4 on a constructed UDG would
certify `chi >= 5` polynomially (where SAT cannot scale). Status `asserted`
(Hoffman 1970, restated by Abiad–Bosma–van Veluw arXiv:2407.02544 and
Elphick–Wocjan). The run has NOT yet computed `1 - lambda_max/lambda_min` on
Moser, Moser+Moser, or any Minkowski sum — that value is a computation, not a
lookup (REQUESTS OPEN). **Ledger fix this pass:** this claim previously had no
CLAIMS.md row and the two source files pointed at each other in a circular
redirect; both files were corrected and the row added.

## New this run — Lovász neighborhood-complex theorem (topological colouring)

**Lovász 1978** (JCT-A 25:319-324; stated verbatim by Kozlov arXiv:math/0505563,
Babson-Kozlov): for any finite simple graph G with neighborhood complex N(G)
(vertices = non-isolated vertices; simplices = subsets sharing a common
neighbour; homotopy-equivalent to Hom(K2,G)), if N(G) is k-connected for some
k >= -1 then `chi(G) >= k + 3`. Equivalently `chi(G) >= conn(N(G)) + 3`.
Calibration: Petersen KG(5,2), chi=3, conn(N(G))=0, 0+3=3 ✓.
**Bearing here:** conn(N(G)) >= 2 would certify chi(G) >= 5 polynomially. But
the neighborhood-complex-topological approach is **refuted** as a 5-certifier:
certifying 2-connectivity needs hard homotopy-triviality, and Lovász's own
theorem caps the value at chi=3 on the triangular lattice. Kept only as a
cheap negative filter. Claim `lovasz-neighborhood-theorem-chi-ge-conn-plus-3`,
asserted-by-source, not machine-checked.
[[research/sources/lovasz-1978-neighborhood-complex-theorem.md]]

## New this run — graph-product chromatic tier (negative control for the construction engine)

The construction engine's crux — can combining 4-colourable UDGs force
chi > 4 — sits in graph-product chromatic theory. The primary tier that frames
it (all asserted-by-source, general graph theory; the unit-distance analogue is
the run's own OPEN computation):
- **El-Zahar–Sauer 1985** (Combinatorica 5:121-126): the tensor product of two
  4-chromatic graphs has chi = 4. Claim `el-zahar-sauer-product-4chromatic`.
- **Tardif 2001** (CMUC 42:353-355): chi(G×H) >= (1/2)·min{chi_f(G),chi_f(H)}.
  Claim `tardif-product-fractional-lower-bound`.
- **Duffus–Sands–Woodrow 1985** (JGT 9:487-495): Cartesian
  max{chi(G),chi(H)} <= chi(G□H) <= chi(G)chi(H); tensor chi(G×H) <=
  min{chi(G),chi(H)}. Claim `duffus-sands-woodrow-product-chromatic`.
**Consequence:** generic product/combination of 4-colourable graphs stays at
chi<=4, so any chi>4 unit-distance construction must get its rigidity from
*geometry* (Minkowski-sum coincidences), not generic product structure. This is
the negative control consistent with the run's measured Moser+Moser = 4.
[[research/sources/el-zahar-sauer-1985-product-of-4-chromatic-graphs.md]]
[[research/sources/tardif-2001-product-fractional-chromatic.md]]
[[research/sources/duffus-sands-woodrow-1985-product-chromatic.md]]

## Addendum — machine-checked verdicts this session

Three results were *computed* (status: checked), extending but not overturning
the digest above. They are all *negative*: they retract apparent challenges to
the size-bound result, not new constructions.

1. **`kernel-4color-tptp-refutation-is-false-positive` (checked).** A FOL/TPTP
   model-finder "refuted" the sharp-kernel-4color claim via a free
   `has_colour` predicate. Hand-decoding the 8-vertex model showed it IS a
   genuine C_8 member (all four kernel conditions hold) and IS 4-colourable
   (witness `[0=C,1=D,2=A,3=D,4=A,5=B,6=C,7=B]`, proper on all 16 edges). The
   "refutation" is an encoding artifact: "G is 4-colourable" is existential,
   its negation universal, and a single model cannot witness the universal —
   the model-finder left a vertex formally uncoloured. So the SZS "refuted"
   verdict does NOT contradict `sharp-kernel-4color` or the N=11 bound.
   [[code/out/false_positive_refutation_kernel_4color.md]] A fresh independent
   re-check program (`code/verify_tptp_false_positive.py`) was written but
   NOT run (no exec tool in this environment); its four conditions + colouring
   counts await a run.
2. **`mycielski-kernel-refutation-false` (checked).** The proposed
   counterexample to `sharp-kernel-4color` via the 5-critical core of
   `Mycielski^2(C5)` fails `K2,3`-freeness (vertices 0,2 share neighbours
   1,6,12), so is NOT in C_23. "Triangle-free ⇒ K2,3-free" is false. The
   graph is abstract, not a plane unit-distance graph, so the N=11 plane size
   bound is untouched. The shipped `refute_mycielski_kernel.py` had a broken
   `mycielski()` (self-refuting 15/41-edge output). [[code/out/refute_kernel_verify.md]]
3. **`sharp-critical-degree` now `checked`** (was asserted): every chi=k graph
   contains a k-critical subgraph (greedy deletion); every vertex-critical
   graph has min-degree >= k-1. Verified by complete exact enumeration over all
   33,867 graphs on <=6 vertices with a fresh SAT oracle (critoracle)
   cross-checked against satcolor (0 mismatches), 0 violations; the 173
   5-chromatic graphs <=6 all reduce to a 5-critical subgraph with delta>=4.
   This is condition (a) of the kernel C_N. The check exposed a soundness bug
   in `lib.coloring` (False/UNSAT direction unreliable — pins `order[0]` but
   the symmetry break tests vertex index 0); satcolor/critoracle agree, so the
   calibration and N=11 census stand. [[research/backward/5chromatic-udg-min-size.md]]
   [[code/out/verify_critical_min_degree2.txt]] [[code/out/verify_5critical_conclusion.txt]]

Net: the strongest verified result ("every unit-distance graph on <=11
vertices is 4-colourable") survives every refutation attempt on disk, and the
FOL/TPTP route is now recorded as the *wrong vehicle* for colourability claims.

## Sources that do not help (and why)
- **Komjáth survey** — only fixes choice-content metadata; no constructive
  leverage. Read once, keep for citation.
- **Kempe universality** — technique behind Maehara's converse; no chromatic
  statement, only the algebraic-coordinate justification.
- **Totally unfaithful UDGs** — a bound on non-embeddability, in the opposite
  direction from construction; not directly load-bearing for the current
  forced-pair/size-bound push.
- **Szemerédi–Trotter (incidence/extremal)** — bounds counts, not chromatic
  numbers; they steer the search toward algebraic constructions and justify
  the exact-field universe, but do not themselves construct anything.

## Contradictions and caveats found
1. **Two de Bruijn–Erdős notes** (`debruijn-erdos-1951-chromatic-reduction.md`
   and `debruijn-erdos-1951-reduction.md`) are duplicates; CLAIMS.md keys on
   the first. Read as one source.
2. **RESOLVED — `scholar_verify_claims.py` / `verify_sources.py` DID run.**
   An earlier CONTEXT.md flagged these as "written but never run", but
   `code/out/commands.log` proves they executed with captured output:
   `verify_sources.captured.txt` (Eisenstein 6 unit vectors |z|^2=1; Minkowski
   T+T = 6v/9e/chi=3) and `scholar_verify_claims.captured.txt`
   (minkowski-sum identity on 2000 exact Q(sqrt3) pairs; eisenstein N==1 iff
   unit over [-12,12]^2; sat 4-colourable=True / 3-colourable=False; ALL
   PASSED), plus `scholar_verify_library.captured.txt`. So
   `minkowski-sum-unit-distance-condition`, `einstein-lattice-unit-distance`,
   `sat-k-colourability-encoding` are legitimately **`checked`** — CLAIMS.md's
   marking is correct and should be trusted. (The earlier CONTEXT.md claim is
   stale.)
3. **Eisenstein root-of-unity subtlety**: the primitive 3rd root omega gives
   three directions; the full six-unit-distance directions need the primitive
   6th root (1+omega). Not a contradiction, but a trap for construction code.
4. **The combinatorial K4/K_{2,3} size-bound universe is falsified in spirit**:
   the 23-vertex triangle-free 5-chromatic Mycielski graph is K4-free, so
   K4-freeness cannot imply 4-colourability. The sharper geometric
   neighbourhood-universe skeleton is the honest one.

## What the run still lacks (internal derivations, not fetches)
- The general chromatic effect of **spindling** (which pairs forced to differ;
   how the constraint propagates). REQUESTS OPEN.
- Whether **Minkowski sums of 4-colourable UDGs can ever raise chi above 4**.
   REQUESTS OPEN (this is the computation, not a source gap).
- Pushing the size-bound census **past N=11** (to N=12+). The neighbourhood
   structure lemma is now DONE and certified
   (`sharp-nbhd-local`, `sharp_nbhd_cert.captured.txt`) — the geometric edge over
   K4-freeness the combinatorial skeleton needed is in place; what remains is
   scaling the C_N enumeration.
- The exact **7-colour hexagonal-tiling margin** (chi<=7 upper bound) — task
   input to derive, not fetched. REQUESTS row says derive it.
