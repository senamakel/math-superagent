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

## Remaining open: one gap in BACKWARD.md

`G-boundary-uniform-count` is the only open gap across all skeletons. It asks
for an absolute constant C bounding the number of boundary (small-k)
representations per a. Everything else (interior via MRSTT, small-a via
Lane-Clark, genus formula proved) is in place. The boundary gap is the
Singmaster conjecture itself distilled to its MRSTT-open edge.

## Completed / no further action

- [x] Riemann-Hurwitz genus derivation — proved, filed at `research/notes/genus-closed-form-derived-by-riemann-hurwitz.md`, capture `code/out/verify_riemann_hurwitz_full.captured.txt` (171 pairs, ALL CHECKS PASSED)
- [x] Matveev (2,3) refuted at root (Lambda=0, vacuous); propagated to BACKWARD.md gaps G-matveev-kummer-check and G-constant-evaluation (both refuted)
- [x] Integrality independently reproduced (`code/out/integrality_reproduced.captured.txt`)
- [x] verify_superelliptic_formula.py executed
- [x] verify_riemann_hurwitz.py runs (bisection fix)
- [x] Mason-Stothers refuted
- [x] Search stopped; library sufficient
- [x] MRSTT effectiveness confirmed; witness double-failure stated

## Ledger discipline

- asserted=22, checked=4, proved=2 (genus-closed-form-integrality + genus R-H closed form)
- Every bound must be run against `code/out/witnesses.json`. Any lemma implying
  B<8 is refuted by 3003. State counting convention on every claim.
- The genus closed form is effective and uniform in (m,n), but gives nothing
  for Singmaster (Faltings is per-pair and ineffective). Say so whenever cited.