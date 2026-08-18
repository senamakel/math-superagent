# Refutation: claim `ueuclid-incontainer-fails-s1s2` is a quantity-mismatch, not a bug

**Status: refuted (the claim as stated is false).**

The claim asserts the on-disk primitive `code/lib/ueuclid.py` "fails its own
acceptance tests in-container (0/30 random ... 5/6 deterministic ... 65
FAILURES -- do not trust ueuclid yet)", with hand-check
`ueuclid(1,0,1,5,z=3)` returning S1=547, S2=2551 where "the correct values are
S1=426, S2=1578".

## Why the claim is wrong — the module is 1-INDEXED

The module's documented convention (docstring, and matching the canonical
fhq/LOJ138/OI-wiki universal-Euclidean sources on disk) is **1-indexed**:
over y = (p·t+q)/r for t = 1..n,
    S1 = sum_{t=1}^{n} z^{t-1} * floor((p·t+q)/r),  S2 likewise.

For (p,q,r,n,z) = (1,0,1,5,3): floor(t/1) = t for t=1..5, weights 3^0..3^4:
    S0 = 1+3+9+27+81 = 121
    S1 = 1·1 + 2·3 + 3·9 + 4·27 + 5·81 = 1+6+27+108+405 = 547
    S2 = 1·1 + 4·3 + 9·9 + 16·27 + 25·81 = 1+12+81+432+2025 = 2551

These are exactly what the module returns (S0=121, S1=547, S2=2551), and the
module's literal oracle `ueuclid_direct` (which loops the same 1-indexed sum)
agrees on every trial.

The claim's "correct" values S1=426, S2=1578 are the **0-indexed** sum
sum_{i=0}^{4} 3^i·i = 0+3+18+81+324 = 426 (S2 = 0+3+36+243+1296 = 1578) — a
*different quantity*, produced by the module's `ue0` wrapper:
    ue0(1,0,1,5,3): k = ceil((p-q)/r) = 1, q2 = q-p+k*r = 0
        ueuclid(1,0,1,5,3) -> S1=547, S2=2551
        S1' = 547 - 1*121 = 426,  S2' = 2551 - 2*1*547 + 121 = 1578
        dU' = 5 - 1 = 4 = floor((p*4+q)/r) = floor(4)

## What actually happened

The claim's author computed the 0-indexed quantity by hand, compared it against
the module's 1-indexed output, and declared the module broken. There is no
compose boundary-shift bug in S1/S2: the module's own acceptance run
(`code/out/ueuclid_main.captured.txt`, on disk) reports
"ALL MONOID TESTS PASSED (ueuclid == ueuclid_direct on every trial)",
30/30 random + 30/30 floor_sum + 6/6 deterministic. The claim's
"65 FAILURES -- do not trust ueuclid yet" banner does not appear in the actual
file on disk; the run on disk passes.

## Status of the real object

CONTEXT.md's Contradictions section (recording the claim
`ueuclid-incontainer-fails-s1s2` as "checked", "65 failures") records a false
alarm and should be corrected. The genuine open risk for the G4 wiring remains
the directive-10/11 hazard the module itself documents: the t-th R step carries
weight z^{t-1} and sits after floor((p·t+q)/r) U's — an off-by-one in *which*
power of 10 the j-th digit of the reduction carries passes every monoid test
but gives a wrong Psi. That hazard is about the *reduction's* indexing
(pinning S1/S2 against mech_psi at small k), not about a bug in the primitive's
arithmetic.

## Refuter verdict

`ueuclid-incontainer-fails-s1s2` (as stated — "the module's S1/S2 are wrong,
65 failures") is **refuted**: the module is internally consistent under its
documented 1-indexed convention and passes its own acceptance gate on disk.
The claim confuses the 1-indexed S1/S2 with the 0-indexed ue0 quantity.

## Search frame

The module's own `__main__` (python3 code/lib/ueuclid.py) and the captured
`code/out/ueuclid_main.captured.txt` cover (p,q,r,n,z) = (1,0,1,5,3) plus 30
random trials + 30 floor_sum + 6 deterministic. All pass on disk, contradicting
the claim's "65 failures".
