# Resolution of the Barber balanced-independent-set formula /2 contradiction

Source: Ben Barber, "A note on balanced independent sets in the cube", arXiv:1210.4029.
The library's note (`research/sources/barber-balanced-independent-cube-2012.md`)
transcribes the odd-n maximum balanced independent set of Q_n two ways:
- prose: `2^{n-1} - 2^{n-2}(n-1)`          (formula A)
- claim block / re-derived ledger: `2^{n-1} - 2^{n-2}(n-1)/2`  (formula B)
These differ by a factor of 2 for odd n. A brute-force checker with a README is
at `code/out/verify_barber_balanced.{py,README.md}` for a runner to execute.

## Hand resolution at small n (no shell available this session)

Balanced = equal even/odd parity counts, independent. Max size must be even.

**n=3 (odd).** Even vertices: 000 (w0), 011,101,110 (w2). Odd: 001,010,100,111.
- Any two even vertices together neighbour ALL four odd vertices: 000 forbids
  the three weight-1 vertices {001,010,100}; every weight-2 vertex's neighbour
  set includes 111 plus two weight-1s, so the union always covers {001,010,100,111}
  = all odd. Hence NO balanced independent set of size 4 exists.
- {000,111} is a balanced independent set of size 2 (000 and 111 differ in 3 bits).
So max balanced independent set of Q_3 = **2**, which matches **formula B**
(`4 - 2·2/2 = 2`) and refutes formula A (`4 - 4 = 0`).

**n=2 (even).** Q_2 is a 4-cycle; every even-odd pair (00/01, 00/10, 11/01, 11/10)
is adjacent, so no balanced set of size 2 exists; max balanced = **0**. The even
formula `2^{n-1} - 2^{n-3}(n-2)` gives 2 at n=2 — wrong at the small-n edge, exactly
the failure the summary already flagged. The general claim (strictly smaller than
2^{n-1} for n>1) holds from n=3.

## Conclusion
The claim-block reading `2^{n-1} - 2^{n-2}(n-1)/2` for odd n is the correct one
(checked by hand at n=3); the even-n formula must be taken as holding for n >= 4,
with the n=2 edge degenerate. The contradiction is resolved in favour of the
claim-block transcription. Not load-bearing for the D(S) problem (it is the d=0
extremal scaffold only). A runner should confirm n=4,5 against the checker.

```claim
id: barber-balanced-formula-odd-half
statement: The largest balanced independent set of Q_n (half even, half odd
  parity, independent) has size 2^{n-1} - 2^{n-2}(n-1)/2 for odd n, < 2^{n-1}
  for n>1. (Rejects the mis-transcribed 2^{n-1} - 2^{n-2}(n-1).)
hypotheses: n odd, n >= 3; balanced = equal parity counts, independent.
holds-here: yes for odd n >= 3 (hand-checked n=3: value 2, matches; formula A
  gives 0 and is refuted). Even-n edge n=2 degenerates to 0 (formula invalid there).
status: checked (n=3 by hand; n>=4 to be confirmed by brute force at
  code/out/verify_barber_balanced.py)
contradicts: balanced-independent-set-max-smaller-than-parity (the odd-n
  transcription 2^{n-1}-2^{n-2}(n-1) that appears in the source file's prose and
  is refuted by the n=3 hand-check; that claim's own block has the /2)
bearing: pins the d=0 extremal scaffold; not load-bearing for D(S).
anchor: code/out/verify_barber_balanced.py; research/sources/barber-balanced-independent-cube-2012.md
```
