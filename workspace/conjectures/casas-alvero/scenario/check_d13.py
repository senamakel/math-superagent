"""Attack the general scenario-count law at degree d=13, beyond every degree
the run has verified on disk (d=2..8, d=12).

Law under test: for degree d, the number of scenarios of type t equals the
Stirling number S(d-1, t+1), and the total is Bell(d-1).  A scenario is a
restricted growth string (s_1,...,s_{d-1}) with s_1=0 and s_j <= max{s_i:i<j}+1;
type = max entry.

We brute-force enumerate RGS of length n=d-1=12 (s_1=0 fixed) and count by
max entry, comparing against the Stirling row.  This pushes one degree beyond
what the workspace already computed, so it either re-confirms the law or
falsifies it at the first new degree.
"""
from collections import Counter

def stirling2(n, k):
    if k == 0 or k > n:
        return 0
    S = [[0]*(k+1) for _ in range(n+1)]
    S[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            S[i][j] = j*S[i-1][j] + S[i-1][j-1]
    return S[n][k]

def bell(n):
    return sum(stirling2(n, k) for k in range(n+1))

def rgs_by_max(n):
    """Count RGS of length n (s_1=0 fixed) by maximum entry, iteratively."""
    counts = Counter()
    # state: (index i, current max m); s_1=0 so start at i=1,m=0
    stack = [(1, 0)]
    # we must accumulate counts at leaf i==n.  Use explicit recursion via stack.
    counts.clear()
    # do it recursively but count leaves
    def rec(i, m):
        if i == n:
            counts[m] += 1
            return
        for v in range(m + 2):
            rec(i + 1, max(m, v))
    rec(1, 0)
    return counts

d = 13
n = d - 1  # 12
S = [stirling2(n, t+1) for t in range(n)]
c = rgs_by_max(n)
brute = [c[t] for t in range(n)]
type_ok = (S == brute)
total_ok = (sum(brute) == bell(n))
print(f"degree d={d}, n=d-1={n}")
print("by-type Stirling S(12,1..12):", S)
print("brute RGS counts by max     :", brute)
print("by-type match:", type_ok)
print("total brute:", sum(brute), " Bell(12):", bell(n), " match:", total_ok)
