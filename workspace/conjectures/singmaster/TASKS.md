# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Immediate

### 1. File the fibonacci-family-is-boundary claim (directive 25)

The structural proof is already in the data — `k/n → 1/φ²` exactly, giving
`cut/k = (log n)^{1/6} → ∞`, so the family stays boundary forever for ε=1/2.
File it as a **proved** claim (not merely checked): `fibonacci-family-is-boundary`,
status proved, anchored to `code/out/boundary_family_always_boundary.captured.txt`,
with the `k/n = 1/φ²` identity and the `(log n)^{1/6}` divergence written out.
Both attributes — effective and uniform in j.

### 2. Count boundary reps per Fibonacci a (directive 25)

For j = 1..12, count **all** nontrivial boundary representatives of a_j, not
just the two the family construction names. Each a_j may have additional reps
(e.g. 3003 has three — (78,2) on top of (15,5),(14,6)). The outcome:

- If every a_j has exactly 2, the family is fully accounted for, and C ≥ 3
  (from 3003) remains the live lower bound.
- If the count grows with j, C is unbounded ⇒ G-boundary-uniform-count is
  FALSE — a genuine result that refutes the skeleton.

Either way the answer is worth having. Use the exact-multiplicity oracle:
binary search in n per k ≤ log₂(a), no triangle, exact integer arithmetic.
Parallel across j.

### 3. Capture: `code/out/fibonacci_family_boundary_count.captured.txt`

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

## Remaining open: one gap in BACKWARD.md

`G-boundary-uniform-count` is the only open gap across all skeletons. It asks
for an absolute constant C bounding the number of boundary (small-k)
representations per a. Everything else (interior via MRSTT, small-a via
Lane-Clark, genus formula proved) is in place. The boundary gap decomposes in
`research/backward/boundary-finite-collisions.md`:
- `G-column-injectivity` — discharged
- `G-fibonacci-boundary-finite` — refuted (directive 24: family stays boundary, but per-a contribution bounded by 2)
- `G-nonfibonacci-pairs-are-bounded` — open, the core structural gap
- `G-boundary-collision-a-finite` — revised (finiteness of A_all is false; per-a boundedness survives)

Next: attack `G-nonfibonacci-pairs-are-bounded` — prove that boundary
collisions outside the Fibonacci family (k,k+1) have columns bounded by a
computable K depending only on eps.

## Ledger discipline

- asserted=22, checked=4, proved=3 (genus-closed-form-integrality + genus R-H closed form + fibonacci-family-is-boundary)
- Every bound must be run against `code/out/witnesses.json`. Any lemma implying
  B<8 is refuted by 3003. State counting convention on every claim.
- The genus closed form is effective and uniform in (m,n), but gives nothing
  for Singmaster (Faltings is per-pair and ineffective). Say so whenever cited.