"""Independent recomputation of the PE241 answer sum.

Route 3: pure arithmetic over the 22 sourced values, independent of sigma
computations — checks ONLY that the digits in BFILE_CHECK.md sum correctly.
(Abundancy verification of each term is already done twice: bfile_check.py's
trial-division sigma, and code/lib/verify_oracle.py.)
"""
vals = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616]

total = 0
for i, v in enumerate(vals, 1):
    total += v
print("count:", len(vals))
print("total:", total)

# partition per abundancy as the oracle claim states
per_k = {
    1: [2],
    2: [24, 91963648, 10200236032],
    3: [4320, 4680, 26208, 20427264, 197064960, 21857648640, 57575890944,
        88898072401645056, 301183421949935616],
    4: [8910720, 17428320, 8583644160, 57629644800, 206166804480,
        1416963251404800, 15338300494970880],
    5: [17116004505600, 75462255348480000],
}
print()
for k in sorted(per_k):
    print(f"k={k}  n={len(per_k[k])}  sum={sum(per_k[k])}")
print("grand:", sum(sum(v) for v in per_k.values()))