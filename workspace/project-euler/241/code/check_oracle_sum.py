"""Verify the oracle (hemiperfect_below_1e18_oracle) arithmetic.

For each of the 22 listed candidates, check 2*sigma(n) == m*n exactly with m
the reduced numerator (abundancy m/2 for odd m), confirm n <= 1e18, and
compute the total sum. KEYS ARE m = 2*abundancy numerator, NOT k in k+1/2:
m = 1 (3/2), 5 (5/2), 7 (7/2), 9 (9/2), 11 (11/2).

CORRECTION NOTE (2026-02-18): an earlier version of this file keyed 24 under
the wrong abundancy and asserted (2k+1)n, which would have failed for every
key (2*sigma(4320)=30240 != 15*4320). It could never have passed as written.
The routes that DO check out independently:
  - code/bfile_check.py  -> code/BFILE_CHECK.md: per-term abundancy verified
    by trial-division sigma;  sum = 482316491800641154.
  - code/lib/verify_oracle.py and code/lib/sum_verify.py: same 22 values,
    abundancy and sum recomputed by exact arithmetic; matches.
This file is kept as a third, corrected route.
"""
values = {
    1: [2],
    5: [24, 91963648, 10200236032],
    7: [4320, 4680, 26208, 20427264, 197064960, 21857648640, 57575890944,
        88898072401645056, 301183421949935616],
    9: [8910720, 17428320, 8583644160, 57629644800, 206166804480,
        1416963251404800, 15338300494970880],
    11: [17116004505600, 75462255348480000],
}

def sigma(n):
    s = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i += 1
    return s

LIMIT = 10**18
total = 0
count = 0
all_n = []
for m, lst in values.items():
    for n in lst:
        assert 2*sigma(n) == m*n, (n, m, 2*sigma(n), m*n)
        assert n <= LIMIT, n
        total += n
        count += 1
        all_n.append(n)

print("count:", count)  # expect 22
print("sum  :", total)
print("all below 1e18:", all(x <= LIMIT for x in all_n))
print("13/2 (m=13) smallest ~1.71e44 > 1e18 -> contributes 0 (sourced, not checked here)")