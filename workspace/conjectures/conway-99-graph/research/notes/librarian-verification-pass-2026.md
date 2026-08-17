# Librarian verification pass — library state confirmed complete

Recorded 2026. This is a verification pass, not new acquisition: the library was
already CLOSED per CONTEXT.md and the accepted practice of this run (don't spawn
librarian — 48 sources already on disk). The task asked the librarian to build
the reference set; it already exists, so the honest act is to verify it meets
the phase-1 completion test and report, rather than make redundant downloads.

## What was checked (all confirmed)

1. **Phase-1 completion test met.** `research/ROOT.md` states: (a) the structure
   of a minimally-characterized putative srg(99,14,1,2) — locally 7K2, the
   231-triangle partial Steiner triple system, the forced 7K2→partial-linear-space
   reduction with the checked-negative non-recursion; (b) the current verification
   / search bound — family is exactly five members, srg(33,8,1,2) excluded by
   integrality, honest statement that no full-space search has completed; (c) at
   least three restricted classes settled — prime divisors of |Aut| ⊆ {2,3};
   no Z6,S3,Z9,E9; Cesarz–Woldar 7||G|⇒Z7, 2||G|⇒|G||6. Phase 1 declared closed
   there.

2. **Every source file carries its URL.** Verified by grep across
   `research/sources/`: each `.full.md` opens with `<!-- source: <URL> ... -->`
   (e.g. assmus → combinatorics.org eljc v2i1r9; automorph-putative → ALCO
   10.5802/alco.418; behbahani-2009-phd-thesis-pdf → spectrum.library.concordia.ca
   NR63369.pdf; makhnev-1988-lambda1-russian-fulltext → mathnet.ru paperid=4220).
   48 full-text sources on disk, each with an accompanying `research/summaries/`
   bounded note.

3. **Both open REQUESTS are answered.** `published-mechanism-ruling-5cf8` answer
   in `research/notes/bagchi-mu2-dichotomy-resolution.md` (srg(33,8,1,2) mechanism =
   eigenvalue-multiplicity integrality; spectral, so a dead end for 99);
   `exact-list-prime-051a` answered in `research/notes/automorphism-orders-consolidated.md`
   and cross-confirmed by `research/notes/wilbrink-order11-makhnev.md`. Both carry
   the closing `answers:` field; `research/notes/directive18-requests-closed.md`
   records them closed.

4. **The one reserved acquisition is dropped/superseded.** Task
   `serve-supersimple-22242-existence` — the super-simple 2-(22,4,2) verdict at
   v=22 — is `dropped` because it was settled constructively: CP-SAT OPTIMAL in
   167.35s, 77-block certificate `code/out/coclique_lift_clean_design.txt`,
   independently verified (degrees all 14, 231 pairs covered twice, max triple
   overlap 1). Construction beats citation; the librarian must NOT chase the
   Gronau–Mullin spectrum row.

## Result

The local reference set for the Conway 99-graph problem is complete, internally
consistent, and self-identifying (URL stored beside each full text). Source
acquisition is CLOSED; further gathering happens only against a NEW gap a live
phase-4 argument is blocked on, named in `research/REQUESTS.md`.
