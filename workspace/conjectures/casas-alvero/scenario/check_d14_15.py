"""Subject: scenario-count = Stirling/Bell law.  Check degrees 14 and 15."""
from collections import Counter
import sys

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
    counts = Counter()
    def rec(i, m):
        if i == n:
            counts[m] += 1
            return
        for v in range(m + 2):
            rec(i + 1, max(m, v))
    rec(1, 0)
    return counts

for d in (14, 15):
    n = d - 1
    S = [stirling2(n, t+1) for t in range(n)]
    c = rgs_by_max(n)
    brute = [c[t] for t in range(n)]
    type_ok = (S == brute)
    total_ok = (sum(brute) == bell(n))
    print(f"d={d} n={n}: by-type match={type_ok} total match={total_ok} "
          f"(Bell({n})={bell(n)}, brute total={sum(brute)})")
    print("   Stirling row:", S)
    print("   brute row   :", brute)
