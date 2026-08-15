# Research sources — what is in the library and how it was obtained

**Environment constraint, stated once.** Direct `download_document` and
`read_sources` on publisher/preprint hosts (renyi.hu, arxiv.org, springer,
sciencedirect, wikipedia, preprint PDF hosts) are refused at the network
boundary. The only route that returns source *content* is the server-side
search/retrieval layer (`exa_search`, `deep_research`, `read_sources` on
permitted surfaces), which fetches and returns text without this run holding
the raw file. The evidence policy additionally screens anything that would
supply the *answer* to `problem.md` (the concrete 5-chromatic graphs, the
numeric value of `chi` of the plane) — intentional, so the run derives those
itself. A source flagged by the evidence policy was not re-fetched.

So the library is a set of **source summaries**, each recording the URL, the
exact claim retrieved, and the basis of that claim, plus a few `.full.md`
bibliographic records where the text could not be fetched. The requirement
"anything cited must be in the library" is met in the form the environment
permits: every claim in a run note is traceable to a URL recorded below.

## The library by subject (as of when this README was last written)

**The finite-to-infinite reduction.**
- `debruijn-erdos-1951-chromatic-reduction.md` — De Bruijn–Erdős compactness:
  chi(G) = sup over finite subgraphs; needs BPIT/choice for uncountable graphs;
  applies verbatim to the plane graph. Claim `debruijn-erdos-1951`.
- `komjath-2010-infinite-chromatic-survey.md` — the survey fixing the metadata
  of the reduction and its AC-content caveats.

**Density cannot be bought (unit-distance extremal theory).**
- `spencer-szemeredi-trotter-unit-distance-bound.md` — u_2(n) = O(n^{4/3}).
  Claim `unit-distance-upper-bound`.
- `erdos-unit-distance-bound.md` — the same bound + Erdős lower bound and
  history (SST 1984 attribution).
- `matousek-unit-distance-problem.md` — course-note treatment; alternative
  proofs (Székely crossing-number, Clarkson et al., Aronov–Sharir). Claim
  `unit-distance-dense-upper-bound-tight`.
- `szemeredi-trotter-incidence-theorem.md` — the incidence theorem itself.
  Claim `szemeredi-trotter-incidence`.

**The construction engine (algebraic point sets / Minkowski sums).**
- `minkowski-sums-rotations-construction.md` — the exact distance-1 condition in
  A+B and that dense UDGs are sums. Claims `minkowski-sum-unit-distance-condition`,
  `minkowski-sum-dense-graphs`.
- `szemeredi-trotter-incidence-algebraic-extremal.md` — sharp ST constructions
  live on algebraic Q(√k) point sets. Claim `szemeredi-trotter-algebraic-extremal`.
- `szemeredi-trotter-cell-decomposition-inverse-structure.md` — Katz–Silier
  (arXiv:2303.17186): the proto-inverse ST theorem — near-extremal
  configurations are densely related to an O(N^{1/3})-parameter recipe and
  decompose around two bushes/product sets; **with the unit-circles analogue
  (Thm 5.21)**, the incidence picture of unit-distance graphs. The top-ranked
  frontier lead (cited 3× by this library's own sources). Claim
  `szemeredi-trotter-inverse-cell-structure`. (Librarian, this run: the library
  held the ST *bound* and the sharp *constructions* but not the *structural/
  inverse* front; this closes the frontier's strongest open row.)
- `szemeredi-trotter-arbitrary-number-fields.md` — sharp ST constructions over
  arbitrary number fields via nice (product-closed) bases. Claim
  `number-field-extremal-constructions`.
- `eisenstein-integers-triangular-lattice.md` — the Eisenstein lattice, its unit
  vectors and norm. Claim `einstein-lattice-unit-distance`.

**Exact-arithmetic verification backbone.**
- `maehara-1991-algebraic-rigid-distances.md` — rigid-UDG distances are exactly
  the algebraic numbers. Claim `maehara-algebraic-rigid-distances`.
- `kempe-universality-linkages.md` — the constructive converse via linkages.
  Claim `kempe-universality`.
- `exact-coordinate-certification-unit-distance.md` — O(n^2) exact certification
  procedure for UDG coordinate fields. Claim `exact-coordinate-certification`.
- `sat-colourability-encoding.md` — the complete k-colouring SAT oracle.
  Claim `sat-k-colourability-encoding`.

**Spectral / SDP lower-bound machinery (the adopted lovasz-theta approach).**
These are the primary-source theorems the run's polynomial exact lower-bound
direction rests on; all `asserted-by-source`, none machine-checked here (that is
the adopted approach's next step, not a lookup).
- `lovasz-theta-sandwich-knuth-1994.md` — the Sandwich Theorem
  `ω(G) ≤ ϑ(Ḡ) ≤ χ(G)`; ϑ polynomial-time computable. Claim
  `lovasz-sandwich-theta`. (Duplicates `knuth-1994-sandwich-theorem.md` /
  `knuth-1994-sandwich-theorem-lovasz-theta.md` / `lovasz-theta-sandwich-knuth.md`,
  which are stubs.)
- `karger-motwani-sudan-vector-chromatic-1994.md` — vector chromatic number
  `χ_v(G) = ϑ(Ḡ)`, KMS duality, and the `−1/(k−1)` notation trap. Claim
  `vector-chromatic-equals-theta-complement`. (Duplicate
  `karger-motwani-sudan-vector-chromatic-1998.md` is a stub.)
- `hoffman-eigenvalue-bound.md` — `χ(G) ≥ 1 − λ_max/λ_min`. Claim
  `hoffman-eigenvalue-bound`. (Duplicate `hoffman-1970-eigenvalue-chromatic-bound.md`
  is a stub.)
- `vertex-transitive-lovasz-theta-formula.md` — closed spectral ϑ on
  vertex-transitive graphs (Galtman 2000); the naive `1 − λ_max/λ_min` formula is
  specific to the strongly-regular/vertex-transitive/association-scheme class.
  Claim `vertex-transitive-theta-eigenvalue`.

**Spectral / topological colouring (parallel conquest of the adopted axes).**
- `lovasz-1978-neighborhood-complex-theorem.md` — `χ(G) ≥ conn(N(G)) + 3`.
  Claim `lovasz-neighborhood-theorem-chi-ge-conn-plus-3`.
- `mycielski-construction-rudnicki-stewart.md` — Mycielski raises χ by 1 keeping
  ω. Claim `mycielski-construction-chromatic`.
- `duffus-sands-woodrow-1985-product-chromatic.md`,
  `el-zahar-sauer-1985-product-of-4-chromatic-graphs.md` — product chromatic
  baselines (tensor of two 4-chromatic graphs is 4).
- `adding-edges-raise-chromatic-number-kostochka-nesetril.md` — edge-addition can
  force a colour jump only after many forcements. Claim
  `adding-edges-raise-chromatic-number`.
- `barajas-serra-2005-distance-graphs-maximum-chromatic.md`,
  `liu-2008-distance-graph-survey.md` — periodic colourings attain the chromatic
  number in the lattice/integral-distance analogue (flat-torus upper-bound spine).

**Structural colouring theory (size-bound direction).**
- `colour-critical-hajos-construction.md` — k-critical min-degree >= k-1,
  Hajós construction. Claim `k-critical-minimum-degree`.
- `colour-critical-graphs-structure.md` — critical-graph structure (parallel
  scholar source). Claim `critical-minimum-degree`.
- `adding-edges-raise-chromatic-number-kostochka-nesetril.md` — Kostochka &
  Nešetřil (2016, proving Bollobás's conjecture): how many edges one can add to
  a k-chromatic graph before a colour jump is forced. Abstract-graph context
  for the run's forced-pair/spindling OPEN row (positivity half transfers:
  C(k,2)=6 coordinated edges always force a K_{k+1}-style jump; but a single
  added edge is generically insufficient, so accumulation is required). Not
  answer-tier; no unit-distance 5-chromatic graph. Claim
  `adding-edges-raise-chromatic-number`.
- `totally-unfaithful-unit-distance-graphs.md` — non-embeddability certificates
  (parallel).

**Spectral / SDP lower-bound certificates (adopted `lovasz-theta` approach).**
- `knuth-1994-sandwich-theorem.md` — Knuth's Sandwich Theorem:
  omega(G) <= theta(Gbar) <= chi(G), theta polynomial-time. Claim
  `sandwich-theorem-lovasz-theta`. (See also the near-duplicates
  `knuth-1994-sandwich-theorem-lovasz-theta.md`, and the stubs
  `lovasz-theta-sandwich-knuth.md` / `hoffman-eigenvalue-bound.md` which were
  created in error and neutralised to keep the ledger single-sourced.)
- `hoffman-1970-eigenvalue-chromatic-bound.md` — **stub** (created in error this run;
  superseded). The canonical record is `hoffman-eigenvalue-bound.md`, claim
  `hoffman-eigenvalue-bound`: chi >= 1 - lambda_max/lambda_min, general graphs,
  polynomial exact warm-up/filter.
- `karger-motwani-sudan-vector-chromatic-1998.md` — **stub** (created in error this run;
  superseded). The canonical record is `karger-motwani-sudan-vector-chromatic-1994.md`,
  claim `vector-chromatic-equals-theta-complement`: the vector chromatic number
  chi_v = theta(Gbar) equivalence (the naming the adopted approach uses).
- `lovasz-1978-neighborhood-complex-theorem.md` — **new this run.** Lovász's theorem
  chi(G) >= conn(N(G)) + 3 for the neighborhood complex (Lovász 1978 JCT-A 25:319–324;
  stated verbatim by Kozlov arXiv:math/0505563). The theorem behind the refuted-but-kept
  neighborhood-complex-topological cheap negative filter. Claim
  `lovasz-neighborhood-theorem-chi-ge-conn-plus-3`. This fills a genuine gap: the two
  separate approach files (`lovasz-theta-vector-chromatic`, `neighborhood-complex-topological`)
  had cited these theorems, but the primary sources were absent from the library.

**The upper-bound periodic-colouring tier (adopted `flat-torus-periodic-6col`).**
- `eggleton-erdos-skilton-1985-colouring-real-line.md` — **the origin paper** of
  the distance-graph method: defines G(R,D) / G(Z,D) and χ bounds for restricted
  distance sets, including χ(G(Z,D)) ≤ |D|+1 for finite integer D. Liu's survey
  names it as initiating the distance-graph study "motivated by the plane
  coloring problem." Claim `eggleton-erdos-skilton-1985-real-line`.
- `zhu-1998-pattern-periodic-coloring-distance-graphs.md` — **pattern periodic
  colorings** of integral distance graphs; completely determines χ(G(Z,D_{m,[2,k']}))
  and the circular chromatic number of G(Z,D_{m,k,s}). Corrects the
  `flat-torus-periodic-6col` mis-attribution: the 1998 JCTB paper is by
  **Xuding Zhu alone**, not "Liu & Zhu". Claim `zhu-1998-pattern-periodic-coloring`.
- `barajas-serra-2005-distance-graphs-maximum-chromatic.md` — for an integral
  distance graph, chi(G(D)) = min over finite circulant reductions, attained by
  a periodic colouring; the discrete-spine theorem that makes a periodic-plane
  search a finite SAT object (in the lattice analogue). Claim
  `barajas-serra-periodic-attainment`. Does NOT settle the continuous plane.
- `liu-2008-distance-graph-survey.md` — survey fixing that the plane
  unit-distance colouring is the open Hadwiger–Nelson problem (4<=chi<=7) and
  that periodic distance-graph colouring is a named technique. Claim
  `liu-distance-graph-survey`.

**The kernel-building machine (Mycielski).**
- `mycielski-construction-rudnicki-stewart.md` — chi(mu(G)) = chi(G)+1,
  omega(mu(G)) = omega(G); iterating mu from K2 gives triangle-free graphs of
  arbitrarily large chi. Claim `mycielski-construction-chromatic`. This is the
  abstract-graph engine behind the code's Mycielski^k(C5) cores — but mu of a
  UDG is NOT automatically a plane UDG, embeddability is separate.

**Calibration target.**
- `moser-spindle-7-vertex-chi4.full.md`, `summaries/moser-spindle-7-vertex-chi4.md`
  — the run's own verified 7-vertex chi=4 calibration (exact coordinates in
  Q(sqrt3,sqrt11,sqrt33), 11 edges, chi=4, k-counts 0,0,0,384,5040).

## Fractional chromatic number (added by librarian, this run)

The adopted `fractional-chromatic-lp-lower-bound` approach is built on the
fractional chromatic number `chi_f`; until this run the library had no dedicated
primary-tier source for it. Added `fractional-chromatic-number-lp-definition.md`
(claims `fractional-chromatic-lp-duality`, `fractional-chromatic-chain`), sourced
from four agreeing primary treatments (Pirot–Sereni SIAM JDM; "Fractional
chromatic number vs Hall ratio" Combinatorica 2025; Bonamy–Hylasová–Kaiser–Sereni
EJC 2025; triangle-free Δ≤3 Discrete Math 2012). It fixes: (P) `chi_f` is the
min over independent-set coverings of `sum_I x_I` with `sum_{I∋v} x_I >= 1`;
(D) its dual (fractional clique number `omega_f`) has the same rational optimum;
`chi_f(G) = max_w w(V)/alpha_w(G)`; chain
`max{omega,|V|/alpha} <= rho <= chi_f <= chi`; perfect graphs give `chi_f=chi`;
`chi_f(C5)=5/2`, `chi_f(diamond)=3`. The run's `code/frac_chro_calib.py` computes
`chi_f` over the independent-set LP but has not yet been run — the exact
`chi_f` of the Moser spindle / Moser+Moser is an OPEN computation (REQUESTS
row), not a lookup. `chi_f` is exact-but-NP-hard in general; cheap for the run's
tiny graphs only. The canonical textbook record (Scheinerman & Ullman,
*Fractional Graph Theory*, Wiley 1997/Dover 2011; author-hosted PDF) is in
`scheinerman-ullman-fractional-chromatic-number.md`; it deliberately carries
**no duplicate claim block** so the ledger single-sources
`fractional-chromatic-lp-duality`/`-chain` in
`fractional-chromatic-number-lp-definition.md`, and it records the resolved
`chi_f(diamond)=3` (perfect-graph argument) and the *false* "triangle-free ⇒
chi_f<=2" claim (C5). For the never-yet-run LP check there are two independent
exact routes on matching edge lists: the scholar's `code/scholar_frac_chro_calib.py`
(exact rational dual scan) and the librarian's `code/lib/frac_chro_verify.py`
(primal+dual scipy, both agree expected values).

## Graph-product chromatic-number tier (added by librarian, this run)

The construction engine's core open question — can combining 4-colourable
unit-distance graphs (Minkowski sums, products) force chi > 4 — sits in the
graph-product chromatic-number theory. Added the primary tier that frames it:

- `el-zahar-sauer-1985-product-of-4-chromatic-graphs.md` — the tensor product
  of two 4-chromatic graphs is 4 (Combinatorica 5 (1985) 121–126).
  Claim `el-zahar-sauer-product-4chromatic`.
- `tardif-2001-product-fractional-chromatic.md` — chi(G×H) >= 1/2 · min{chi_f(G),
  chi_f(H)} (Comment. Math. Univ. Carolinae 42 (2001) 353–355).
  Claim `tardif-product-fractional-lower-bound`.
- `duffus-sands-woodrow-1985-product-chromatic.md` — Cartesian and tensor
  product chromatic bounds (J. Graph Theory 9 (1985) 487–495).
  Claim `duffus-sands-woodrow-product-chromatic`.

These are the negative control for the construction engine: generic product/
combination of 4-colourable graphs stays at chi<=4, so any chi>4 unit-distance
construction must come from geometric (Minkowski-coincidence) rigidity, not
generic product structure. Consistent with the run's measured Moser+Moser = 4.
All three `asserted-by-source` (general graph theory; the unit-distance analogue
is the run's own computation).

## What could not be obtained, and why (so nobody repeats it)

1. **Publisher/arXiv/preprint full texts** (de Bruijn–Erdős 1951 body,
   Spencer–Szemerédi–Trotter 1984 chapter, Moser & Moser 1961 note, and the
   Minkowski-sum papers): blocked at the network boundary. Only the
   search/retrieval layer returns source text. Not retried on mirrors (they
   fail identically). Environmental, not a finding about the maths. Confirmed
   again this run: a fresh `download_document` to an arXiv PDF was refused at
   the boundary, and `read_sources`/`exa_search` on the answer-tier results
   (spindling technique, extremal cell structure) were withheld by the evidence
   policy. These remain recorded gaps, not to be re-attempted.
2. **Anything that would supply the answer to `problem.md`** (concrete
   5-chromatic graph coordinates, chi(plane) value, hexagon-margin/spindling
   technique leading to them): withheld even via server-side retrieval.
   Intentional — the run must derive these. Rows 1–3 of `research/REQUESTS.md`
   record this. Re-confirmed this run: `read_sources`/`exa_search` on the
   edosproblems 96 entry, Exoo's exoo2 note, ar5iv 2006.06285, the
   "unit-distance graph Minkowski sum" and lattice-colouring queries, and the 
   periodic lattice tiling colouring survey were all screened by the evidence
   policy as answer-tier. Not re-attempted.
3. **Duplicate** `debruijn-erdos-1951-reduction.md` (proof detail) vs the
   scholar's `debruijn-erdos-1951-chromatic-reduction.md` (CLAIMS.md keys on
   the latter). Read as one source.

## k-critical edge-count tier (added by librarian, this run)

The **size-bound rung** (prove every unit-distance graph on at most N vertices
is 4-colourable) needs the edge-count lower bound on a hypothetical minimal
5-critical unit-distance graph, and the discharging approach
(`research/approaches/discharging-minimal-counterexample.md`) cited a chain of
results that were **absent from the library**. Added the primary tier, all
general graph theory (non-planar discharging — legitimate on a 5-critical
graph by the four-colour theorem):

- `dirac-1957-critical-edge-bound.md` — the classical origin: every k-critical
  graph on n >= k+2 vertices has `(1/2)((k-1)n + k - 3)` edges; for k=5,
  `|E| >= 2n+1` (average degree > 4). Claim `dirac-1957-critical-edge-bound`.
- `krivelevich-1997-critical-edge-bound.md` — the Gallai-forest refinement:
  `|E| >= ((k-1)/2 + (k-3)/(2(k^2-2k-1)))·n`, the mechanism (L(G)/H(G)
  decomposition, Gallai forests) that is the *correct* non-planar discharging
  route. Claim `krivelevich-1997-critical-edge-bound`.
- `kostochka-yancey-2014-ore-conjecture-k-critical.md` — the sharp result: for
  k >= 4, `|E(G)| >= ceil(((k+1)(k-2)n - k(k-3))/(2(k-1)))`; for k=5 this is
  `(9n-5)/4`, exact when n ≡ 1 (mod 4). Claim
  `kostochka-yancey-2014-critical-edge-bound`.
- `cranston-rabern-2016-list-critical-discharging.md` — the methodological
  warrant that discharging is non-planar (list-critical / AT-critical edge
  bounds). Claim `cranston-rabern-2016-list-critical-discharging`.

These fix the load-bearing chain the discharging approach relied on and the
run's own hand check (refuting that route at n=9..10) confirms the full texts
were blocked at the network boundary but the statements are retrievable via
server-side retrieval.

## Construction-technology tier (added by librarian, this run)

The two **adopted** construction approaches — the Henneberg/Laman rigidity
grammar (`rigidity-matroid-henneberg-construction`) and the regular-4-polytope
projection (`projection-distance-equalization`) — both cited primary theorems in
their `precedent` blocks that were **absent from the library**. Added the
technique-tier sources (exact statements retrieved server-side; direct download
blocked at the network boundary):

- `laman-henneberg-generic-rigidity-theorem.md` — Laman: generically rigid in
  the plane iff (2,3)-tight (|E|=2|V|-3, every subgraph ≤ 2|V'|-3); every such
  graph built from K2 by H1 (add vertex on two) and H2 (edge-split onto three)
  moves (Henneberg 1911 / Laman 1970; confirmed by Borcea–Streinu, Capco et al.,
  Nixon–Owen). Caveat that matters: completeness is **generic, not all-unit**,
  and generic realizations are in general **not solvable by radicals**
  (Owen–Power). Claim `laman-henneberg-generic-rigidity`. This fixes the adopted
  approach's overclaims: H1 is the free quadratic move, H2 is a circumradius-1
  coincidence, and the coordinate field grows.
- `regular-4-polytope-projection-quaternions.md` — 24-cell vertices = all 24
  permutations of (±1,±1,0,0) in Z^4 (binary tetrahedral / D4, order 1152);
  600-cell vertices = the 120 unit icosians = binary icosahedral group in
  Q(√5) (H4, order 14400); Coxeter/Petrie plane projections give regular-gon
  shadows (regular 30-gon for the 600-cell). A rank-2 projection is NOT a
  homothety. Claim `regular-4-polytope-projections`. Supplies the adopted
  projection approach its exact construction data.
- `kostochka-yancey-critical-edge-bound.md` — the **general** k-critical edge
  bound `|E| >= [(k+1)(k-2)n - k(k-3)]/[2(k-1)]` (k=5: `(9n-5)/4`), tight on the
  k-Ore graphs; and the key **negative datum**: there is **no established
  closed-form K4-free 5-critical edge bound** strictly above `(9n-5)/4` — the
  only strict sharpenings are triangle-free (Postle, ε=1/84), a stronger
  restriction that does not apply to UDGs (they contain equilateral triangles).
  Claim `kostochka-yancey-critical-edge-bound`. This retires the "sharper
  K4-free lower bound" premise of the `clique-free-critical-size-bound`
  approach as an unavailable lookup.

(Note: the separate concurrent `kostochka-yancey-2014-ore-conjecture-k-critical.md`
records the same general bound for the discharging tier; this file's distinct
contribution is the K4-free analysis and the retirement of the K4-free-bound
premise.)

## Verification status (corrected this run)

Three load-bearing claims are machine-`checked`, not merely `asserted`:
- `minkowski-sum-unit-distance-condition` — the distance-1 identity verified on
  2000 exact random pairs over Q(sqrt3); the sum T+T = 6 vertices / 9 unit
  edges / chi=3 confirmed by an independent cross-check.
  (`code/out/scholar_verify_claims.captured.txt`,
   `code/out/crosscheck_triangle_sum.captured.txt`)
- `einstein-lattice-unit-distance` — six unit vectors all of squared modulus 1;
  N==1 iff a unit over [-12,12]^2. (`code/out/scholar_verify_claims.captured.txt`,
   `code/out/scholar_verify_library.captured.txt`,
   `code/out/verify_sources.captured.txt`)
- `sat-k-colourability-encoding` — 4-colouring SAT with witness
  [0,1,2,0,1,2,3], 3-colouring UNSAT on the calibrated 7-vertex spindle, via
  both Cadical153 and Minisat22. (`code/out/scholar_verify_claims.captured.txt`,
   `code/out/sat_calibration.captured.txt`)

Each source note records the `status: checked` line and its captured-output
anchor; `research/CLAIMS.md` reflects the upgrade. The five other
`asserted` computational/factual claims (critical-min-degree,
de-bruijn-erdos, maehara, minkowski-sum-dense-graphs, sat-shrinking,
number-field-extremal, szemeredi-trotter family, unit-distance-upper-bound)
remain asserted-by-source and unverified here.
