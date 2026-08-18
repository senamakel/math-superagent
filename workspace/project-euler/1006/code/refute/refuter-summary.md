# Refuter summary — PE1006

## What I attacked

The most consequential *live asserted* statement the run is holding: the checked
claim **`ueuclid-incontainer-fails-s1s2`** — that the on-disk primitive
`code/lib/ueuclid.py` "fails its own acceptance tests in-container
(0/30 random, 0/30 floor_sum, 5/6 deterministic, 65 FAILURES)" because of a
"compose boundary-shift (dU) bug" in S1/S2. This claim steers the whole G4
critical path (it tells the run to stop everything and "fix the compose dU bug"
before acceptance 4, the anchors, and Psi(10^18)).

## Why it is false

The module is **1-indexed** by its own documented convention
(S1 = Σ_{t=1}^n z^(t-1)·floor((p·t+q)/r)). For the claim's decisive case
`(p,q,r,n,z)=(1,0,1,5,3)`:

- S1 = 1·1+3·2+9·3+27·4+81·5 = **547**
- S2 = 1+12+81+432+2025 = **2551**

The module returns exactly these, and the on-disk captured run
`code/out/ueuclid_main.captured.txt` reports **ALL MONOID TESTS PASSED**
(30/30+30/30+6/6). The claim's "correct" S1=426, S2=1578 are the **0-indexed**
sum Σ_{i=0}^4 3^i·i = 426 (a different quantity), which the module's `ue0`
wrapper computes correctly:
S1' = 547 − 1·121 = 426, S2' = 2551 − 2·1·547 + 121 = 1578, dU' = 4.

**Verdict: refuted.** There is no compose boundary-shift bug in the primitive's
S1/S2. The run should stop "debugging the compose dU bug".

## Also investigated

- **Directive-9 Claim 1** (the k+1 distinct factors = the last k+1 windows of
  q_n q_n): confirmed by hand at k=3 (length-8 standard word → windows
  {101,010,100,001}) and k=5 (length-13 → 6 windows == 6 factors). The TPTP
  encoding `d9-claim1-k3.p` yields a *spurious* counterexample (model-founder
  introduces an unconstrained extra element and declares it a factor) — an
  encoding artifact, **not** reported as a real refutation.
- **M = 101001001 primality** — asserted-unchecked, but not FOL-encodable for
  this engine; left as-is.

## Four-answer result

`refuted` — the claim `ueuclid-incontainer-fails-s1s2` is refuted (identified a
quantity mismatch in its hand-check and confirmed the module passes its own
gate on disk).

## Files

- `research/notes/refuter-ueuclid-s1s2-false-alarm.md` — the finding + claim block
- `code/refute/ueuclid-S1-index-refutation.md` — refutation record with exact arithmetic
- `code/refute/check_M_and_claim3.py`, `code/refute/check_d9_claim1.py` — checkers (not run; no shell here)
- memory recorded via `remember_memory`
