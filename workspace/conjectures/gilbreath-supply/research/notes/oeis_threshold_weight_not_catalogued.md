# OEIS miss — SUPPLY threshold-weight sequence is not catalogued

Author: librarian. Status: finding (negative, definitive for the lookup).

The third pass's central deliverable is the threshold WEIGHT
`w*(n) = θ_mean(n)·n` at which linear supply becomes typical over the weight-w
sphere. I submitted two consecutive-term lists to the OEIS:

- `3,3,3,4,3,5,7,11,16,24,35,52,77`  (n = 8..4096)
- `3,3,5,7,11,16,24,35,52,77,112,164,349,738`  (n = 8..2^18)

**Neither matches any catalogued sequence** (both lookups returned no entry).
This is a definitive negative: a miss from the OEIS is a result, not a dead end.

**Bearing.** No closed form for `w*(n)` is going to be *looked up* — the
sublinear-exponent structure (`w ~ n^0.55`, measured-not-proved, fitted over
n ≤ 32768) has to come from the problem itself, not from an existing sequence
catalogue. Nobody should re-run this lookup; the structure is the Krawtchouk-
parity mean `θ_mean(n) = min{w: Σ_{d=2}^{n-1} P_d(w) ≥ 0.4n}` (claim
`threshold-mean-exact-parity-formula`), and its growth is a combinatorial
statement about that quantity, not a catalogued sequence.

Stored in Cognee (this run): the miss and the directive-45 exponent verdict.
