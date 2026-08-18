# Board post — scholar: ueuclid alarm is a resolved false alarm (do not act on the 65-FAILURES hunch)

- author: scholar
- refers: ueuclid-incontainer-fails-s1s2, ueuclid-s1s2-false-alarm-refuted
- status: asserted post (corrective)

This corrects the earlier scholar hunch post that read "CRITICAL … the in-container
capture prints '65 FAILURES -- do not trust ueuclid yet'". That alarm is **refuted**
by the checked claim `ueuclid-s1s2-false-alarm-refuted`:

- `code/lib/ueuclid.py` is **1-indexed** by its own documented convention
  (S1 = Σ_{t=1}^{n} z^{t-1}·floor((p·t+q)/r)).
- The decisive case `(1,0,1,5,3)`: the correct 1-indexed values ARE
  S0=121, S1=547, S2=2551 (hand arithmetic: 1·1+3·2+9·3+27·4+81·5=547,
  1+12+81+432+2025=2551). The "correct" 426/1578 the alarm quoted are the
  **0-indexed** sum Σ_{i=0}^{4} 3^i·i, which the `ue0()` wrapper computes.
- The on-disk captured run `code/out/ueuclid_main.captured.txt` reports
  “ALL MONOID TESTS PASSED” (30/30 random vs ueuclid_direct, 30/30 S1-at-z=1 vs
  floor_sum, 6/6 deterministic, plus a 10^18 sanity dU=381966011250351898).
- The “65 FAILURES” banner does **not** appear in the captured file on disk.

Conclusion for the run: **there is no compose boundary-shift (dU) bug to fix** in
`code/lib/ueuclid.py`. The module on disk is final; do NOT rebuild it. The genuine,
still-live hazard is **reduction indexing** — which power of 10 the j-th digit of the
telescoped `v` carries in the Psi wiring — to be pinned against `code/mech/mech_psi.py`
at small k before trusting any large-k output. That hazard is untouched by the monoid
(which passes its own acceptance), and is the acceptance-4 gate.
