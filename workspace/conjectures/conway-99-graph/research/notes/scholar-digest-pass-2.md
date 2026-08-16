# Scholar digest pass 2 — verify the new library, correct stale claims

This pass verified the reference library (already well-digested by the prior
scholar pass) against the full texts, promoted the run's now-computed
verifications from asserted to checked, and corrected stale "paywalled/
unverified" framing for Makhnev 1988 that the Reimbayev and Bondarenko-
Radchenko digests still carried.

## Verified complete / control artifacts now on disk
- `code/out/oracle_verification.captured.txt`: rook(3)=srg(9,4,1,2) PASS,
  bvls_graph()=srg(243,22,1,2) PASS (2673 edges), negative controls failing on
  the exact count path. Promotes claims c4/c5 to checked.
- BvLS built independently as explicit Cayley graph on Z3^5
  (code/out/check_bvls_cayley.py), vertex-transitive by construction.
- Makhnev 1988 condition (*) gate passed on both controls, n3=0
  (code/out/makhnev-1988-condition-captured.txt).
- Reimbayev hexagon identity checked exactly on both controls
  (code/out/hexagon_identity_verified.captured.txt): n12 = formula + n3, n3=0.
- g-reduce negative control (code/out/g_reduce_control.captured.txt): outer
  design's collinearity graph leaves the family.
- c7 (mu=2 common neighbours nonadjacent) captured: holds on both controls.
- srg99-not-vertex-transitive deduction written, arithmetic checked.
- order6-n3-not-forced: order-6 counting does not force n3>=1 at 99.

## Claims corrected this pass (stale framing)
Added `follows-from: makhnev1988-condstar-theorems` to `reimbayev-hexagon-bound-n3-pivot`
and `follows-from: makhnev1988-condstar-theorems, order6-n3-not-forced` to
`reimbayev-order-six-subgraph-counts`, and updated their status to note the
Makhnev conditional is now sourced and the hexagon identity/n3=0 are checked.
Corrected the bondarenko-radchenko and the two reimbayev landing-page digests
that still described Makhnev 1988 as paywalled/unverified.

## Requests
Both REQUESTS rows closed: exact-list-prime-051a and published-mechanism-ruling-5cf8.
Gap makhnev-1988-condstar closed by the Russian full-text summary.

## Not useful (already recorded, confirmed here)
brouwer-haemers chapter (paywalled preview); makhnev-2013-local-subgraphs
(paywalled, body absent); vanlint-brouwer-1984 (garbled OCR, do not cite);
zehavi-oliveira (solvable variant, not the problem); keramatipour SAT
(no boundary value, confirms enumeration is wrong method).

## Still lacking
- n3=0 for a putative (99,14,1,2) still only a conjecture; needs a k=14-specific
  geometric constraint.
- Existence of (99,14,1,2) open; no 9/243-surviving nonexistence claim.
- Lou & Murin forbidden-order-9 lead untraceable; lead only.
- Behbahani-Lam-Östergård 2012 full text paywalled; the two 4-vertex SRG
  families' spectra unknown.
