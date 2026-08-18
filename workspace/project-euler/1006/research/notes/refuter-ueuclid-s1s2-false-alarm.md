# Refuter finding: `ueuclid-incontainer-fails-s1s2` is a false alarm

**Attacked:** the claim `ueuclid-incontainer-fails-s1s2`, recorded as *checked*
in CONTEXT.md and `derived/CLAIMS.md`: "The O(log) ueuclid monoid in
code/lib/ueuclid.py fails its own acceptance tests in-container (0/30 random vs
the direct oracle, 0/30 S1-at-z=1 vs plain floor_sum, 5/6 deterministic);
S1/S2 are wrong — compose boundary-shift bug."

This claim is **false**. The module is 1-indexed; the claim's hand-check
computed a 0-indexed quantity and pronounced the 1-indexed output wrong.

## The decisive case (exact arithmetic)

`ueuclid(1,0,1,5,z=3)` under the module's documented 1-indexed convention
(docstring; matches fhq/LOJ138/OI-wiki universal-Euclidean on disk):

    S1 = sum_{t=1}^{5} 3^(t-1) * floor((1*t+0)/1)
       = 1·1 + 3·2 + 9·3 + 27·4 + 81·5 = 1+6+27+108+405 = 547
    S2 = 1·1² + 3·2² + 9·3² + 27·4² + 81·5² = 1+12+81+432+2025 = 2551
    S0 = 121

The module returns exactly S0=121, S1=547, S2=2551. The claim's "correct"
S1=426, S2=1578 are the **0-indexed** sum sum_{i=0}^4 3^i·i = 0+3+18+81+324=426
(S2 = 0+3+36+243+1296=1578), a different quantity that the module's `ue0`
wrapper computes correctly:

    ue0(1,0,1,5,3): k = ceil((p-q)/r)=1, q2 = q-p+k·r = 0
        ueuclid(1,0,1,5,3) -> S1=547, S2=2551
        S1' = 547 - 1·121 = 426      S2' = 2551 - 2·1·547 + 1²·121 = 1578
        dU'  = 5 - 1 = 4 = floor((1·4+0)/1)   ✓

So there is **no compose boundary-shift bug**: the on-disk captured run
`code/out/ueuclid_main.captured.txt` reports "ALL MONOID TESTS PASSED
(ueuclid == ueuclid_direct on every trial)" — 30/30 random, 30/30 floor_sum,
6/6 deterministic. The "65 FAILURES -- do not trust ueuclid yet" banner the
claim quotes does not appear in the file on disk.

## What this corrects in the record

CONTEXT.md's Contradictions/Gaps sections instruct the run to "fix the compose
S1/S2 dU cross terms" of `ueuclid.py` before anything else. That instruction is
wrong: there is no bug to fix, and the module already passes acceptance 1-3.
The claim `ueuclid-incontainer-fails-s1s2` should be marked closed/refuted.

The genuine, still-live hazard (per directive 10/11) is *reduction* indexing —
an off-by-one in which power of 10 the j-th digit of the telescoped `v` carries
would pass every monoid test yet give a wrong Psi. That is untested until the
G4 wiring runs against mech_psi at small k; it is not a defect in the primitive.

```claim
id: ueuclid-s1s2-false-alarm-refuted
status: checked
contradicts: ueuclid-incontainer-fails-s1s2
statement: Claim `ueuclid-incontainer-fails-s1s2` is false. code/lib/ueuclid.py
is 1-indexed; for (1,0,1,5,3) S1=547, S2=2551 are the correct 1-indexed values,
not 426/1578. The on-disk module passes its own acceptance gate (ALL MONOID
TESTS PASSED) and my hand arithmetic confirms, so there is no compose
boundary-shift bug in S1/S2 to fix.
hypotheses: the module's own documented 1-indexed convention and the captured
code/out/ueuclid_main.captured.txt
holds-here: yes
bearing: the primitive is sound on disk; the run should stop debugging "the
compose dU bug" and proceed to the G4 wiring, pinning reduction indexing against
mech_psi at small k. The remaining risk is reduction indexing, not the monoid.
search-frame: hand exact-arithmetic check of the deterministic case
(1,0,1,5,z=3) against the module's documented 1-indexed convention
(S1=547, S2=2551 confirmed term-by-term), plus the captured
code/out/ueuclid_main.captured.txt run of the module's own __main__ showing
30/30 random vs ueuclid_direct, 30/30 S1-at-z=1 vs floor_sum, 6/6 deterministic,
and the large-n sanity (dU = 381966011250351898 = floor((514229*10^18+3)/1346269)) —
all exactly matching ueuclid_direct; within this frame (the module's own
acceptance suite and the one decisive case) no failure was found, so
ueuclid-incontainer-fails-s1s2 is a false alarm, not a smaller unchecked bug.
```
