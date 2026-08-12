"""Verify the new oracle (hemiperfect_below_1e18_oracle) arithmetic.

For each of the 22 listed candidates, check 2*sigma(n) == (2k+1)*n exactly,
confirm n <= 1e18, and compute the total sum. This is a VERIFICATION of a
sourced list, not the discovery method (that is the solver's DFS).
"""
from math import gcd

values = {
    1: 2,
    3: 24,
    5: [91963648, 10200236032],
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
for k, v in values.items():
    lst = v if isinstance(v, list) else [v]
    for n in lst:
        assert 2*sigma(n) == (2*k+1)*n, (n, k, 2*sigma(n), (2*k+1)*n)
        assert n <= LIMIT, n
        total += n
        count += 1
        all_n.append(n)

print("count:", count)  # expect 22
print("sum  :", total)
print("all below 1e18:", all(x <= LIMIT for x in all_n))
print("reported k=6 (13/2) smallest ~1.71e44 > 1e18 -> contributes 0 (sourced, not checked here)")
