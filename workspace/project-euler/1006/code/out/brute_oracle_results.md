# PE1006 naive oracle — verified results

Run on the brute-force oracle `code/brute.py`.

## Worked examples reproduced (both match)

- `Psi(3) = 20302` — length-3 subwords `001,010,100,101` → 1²+10²+100²+101²=20302. ✓
- `Psi(10) mod 101001001 = 10699667`. ✓
- Distinct length-k Fibonacci subword count = k+1, for every k in 1..20. ✓

## Psi table (k=1..20) from the oracle

    1       1
    2       101
    3       20302
    4       2042402
    5       204252402
    6       30445654403
    7       3054587854503
    8       407470828064704
    9       40849095449084804
    10      4085011557551094804
    11      508703259827952296805
    12      50970528087268072496905
    13      5097153010831280092506905
    14      609915603287332682295508906
    15      61091760630937672902595709006
    16      7129296283596175714952815919207
    17      713949748580120079919974836939307
    18      71395994978232510500422176938949307
    19      8141620537963671762570662587340151308
    20      815164074836507597029594703627460351408

## Bug found and fixed

The workspace oracle originally built only `2k+4` symbols of the Fibonacci
word before sliding the window. That is provably insufficient: the shortest
prefix that already contains all k+1 distinct length-k factors is about 2k
(measured 35 for k=15, 104 for k=50), so at k=15 the oracle found only 15 of
the 16 factors and reported a wrong Psi(15). Bound changed to `4k+8`; all
counts now match k+1 for k=1..20.

(Note: the memory/scratch servers were unresponsive at the time this was
recorded, so this finding is stored here on disk rather than in Cognee.)
