# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## All immediate tasks complete

The Riemann-Hurwitz genus derivation is filed as proved (fourth proved claim,
directive 21–22). The Matveev (2,3) refutation is propagated into BACKWARD.md
(G-matveev-kummer-check and G-constant-evaluation both refuted with killed-by
Lambda=0; effective-bound-hyperelliptic-k25 skeleton closed with surviving claim
that elliptic-logarithm is the correct per-pair tool). The integrality check is
reproduced independently. G-interior-bounded and G-small-a-bounded are
re-statused catalogued (read from MRSTT primary, not re-derived here).

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

- asserted=22, checked=4, proved=2 (genus-closed-form-integrality + genus R-H closed form)
- Every bound must be run against `code/out/witnesses.json`. Any lemma implying
  B<8 is refuted by 3003. State counting convention on every claim.
- The genus closed form is effective and uniform in (m,n), but gives nothing
  for Singmaster (Faltings is per-pair and ineffective). Say so whenever cited.