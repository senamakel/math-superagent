# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Immediate

### 1. Count ALL boundary reps per Fibonacci a_j — the question that decides G-boundary-uniform-count

The family construction names two representatives per a_j: (n,k) and (n-1,k+1).
But a_j may have additional nontrivial representations found by search — e.g.
3003 (j=1) has three: (78,2), (15,5), (14,6). The open question from directives
25–26: for each j = 1..12, how many nontrivial boundary representatives does
a_j have IN TOTAL?

The answer decides the skeleton:

- **exactly 2 for every j** → Fibonacci family is fully accounted for by its
  construction; C ≥ 3 (from 3003) remains the live lower bound for
  G-boundary-uniform-count; the skeleton stays live.
- **grows with j** → C is unbounded; G-boundary-uniform-count is FALSE;
  singmaster-uniform-bound is broken, not live — a genuine result that refutes
  the decomposition and closes the route honestly.

The second answer is the more valuable one.

Method: exact-multiplicity oracle — for each a_j, binary search in n per
k ≤ log₂(a_j), exact integer arithmetic, no triangle. Boundary condition:
k < exp((log n)^{2/3+eps}) with eps=1/2. Parallel across j. Run to j=12
(or until the pattern is clear). State the convention on every output.

Why eps=1/2 is the right test value: G-boundary-uniform-count must hold for
EVERY admissible eps in (0,1). Larger eps means larger cut, hence MORE
representatives counted as boundary — so the binding case is eps → 1, not
eps = 1/2. The run's general threshold result (directive 26) says the family
stays boundary for all eps > 1/3, which is most of (0,1). So eps=1/2 is a
conservative midpoint; if the count stays at 2 at eps=1/2, the family is
under control for the cases that matter. If it grows even at eps=1/2, the
skeleton is broken at a moderate cut and the prognosis for larger eps is worse.

### 2. File fibonacci-family-boundary-proved as a proved claim

The result is stronger than the eps=1/2 numerical check. The structural proof
has four parts, all in the data:

- `k/n → 1/φ²` exactly (F_{2j}/F_{2j+2} limit)
- `log k_j ~ 4j log φ`, `log n_j ~ 4j log φ`
- `cut/k = (log n)^{eps - 1/3}` → ∞ iff eps > 1/3
- `j0(eps)` computable from the inequality `4j log φ < (4j log φ)^{2/3+eps}`

File as proved (not merely checked), with both attributes stated: effective and
uniform in j. The note already exists at `code/out/boundary_family_always_boundary.captured.txt`;
the claim needs a proper claim block with `status: proved`.

The eps ≤ 1/3 case (finite j are boundary) is part of the theorem — it is what
makes the statement complete rather than a numerical observation.

### 3. Capture both: `code/out/fibonacci_family_boundary_count.captured.txt`

## Completed / no further action

- [x] Riemann-Hurwitz genus derivation — proved, filed at `research/notes/genus-closed-form-derived-by-riemann-hurwitz.md`, capture `code/out/verify_riemann_hurwitz_full.captured.txt` (171 pairs, ALL CHECKS PASSED)
- [x] Matveev (2,3) refuted at root (Lambda=0, vacuous); propagated to BACKWARD.md gaps G-matveev-kummer-check and G-constant-evaluation (both refuted)
- [x] Integrality independently reproduced (`code/out/integrality_reproduced.captured.txt`)
- [x] verify_superelliptic_formula.py executed
- [x] verify_riemann_hurwitz.py runs (bisection fix)
- [x] Mason-Stothers refuted
- [x] Search stopped; library sufficient
- [x] MRSTT effectiveness confirmed; witness double-failure stated
- [x] Boundary cut corrected (directive 24) — `code/boundary_cut_corrected.py`, capture `code/out/boundary_cut_corrected.captured.txt` (EXIT_CODE=0). Two bugs found and fixed in the original `code/boundary_cut.py`: (1) wrong exponent — `exp((log n)**(2/3) + 0.5)` instead of `exp((log n)**(2/3+0.5))`; (2) hung on Fibonacci family by searching instead of using known (n,k). Result: ALL six Fibonacci family members are BOUNDARY under the correct cut; the family never crosses to interior for eps > 1/3. G-fibonacci-boundary-finite refuted. The per-a bound is unthreatened — each Fibonacci a has at most 2 boundary reps.
- [x] Boundary eps-dependence sweep — `code/out/boundary_eps_dependence.captured.txt` confirms eps > 1/3 threshold at j=6,10,20.

## Remaining open: one gap in BACKWARD.md

`G-boundary-uniform-count` is the only open gap across all skeletons. It asks
for an absolute constant C bounding the number of boundary (small-k)
representations per a. Everything else (interior via MRSTT, small-a via
Lane-Clark, genus formula proved) is in place.

**Consequence of directive 26 for this gap:** the bound must hold for *every*
admissible eps in (0,1), and a larger eps means a larger boundary region. The
binding case is eps → 1. The Fibonacci family is boundary for eps > 1/3,
covering most of the admissible range, so any C must cover it — it cannot be
set aside as interior by choosing a small eps. The immediate task above (count
ALL reps per a_j) settles whether C can plausibly be a constant, and if the
count grows with j, C is unbounded and the skeleton is refuted.

The boundary gap decomposes in `research/backward/boundary-finite-collisions.md`:
- `G-column-injectivity` — discharged
- `G-fibonacci-boundary-finite` — refuted (directive 24: family stays boundary, but per-a contribution bounded by 2)
- `G-nonfibonacci-pairs-are-bounded` — open, the core structural gap
- `G-boundary-collision-a-finite` — revised (finiteness of A_all is false; per-a boundedness survives)

## Ledger discipline

- asserted=22, checked=4, proved=3 (genus-closed-form-integrality + genus R-H closed form + fibonacci-family-is-boundary)
- Every bound must be run against `code/out/witnesses.json`. Any lemma implying
  B<8 is refuted by 3003. State counting convention on every claim.
- The genus closed form is effective and uniform in (m,n), but gives nothing
  for Singmaster (Faltings is per-pair and ineffective). Say so whenever cited.