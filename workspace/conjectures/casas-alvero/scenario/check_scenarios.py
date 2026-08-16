"""Verify Castryck's scenario counts for d=12 are Stirling numbers S(11, t+1)."""
from collections import Counter

# Stirling numbers of second kind by recurrence S(n,k) = k*S(n-1,k)+S(n-1,k-1)
def stirling2(n, k):
    if k == 0 or k > n:
        return 0
    S = [[0]*(k+1) for _ in range(n+1)]
    S[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i,k)+1):
            S[i][j] = j*S[i-1][j] + S[i-1][j-1]
    return S[n][k]

def bell(n):
    return sum(stirling2(n, k) for k in range(n+1))

scenarios_type = [1, 1023, 28501, 145750, 246730, 179487, 63987, 11880, 1155, 55, 1]
total = sum(scenarios_type)

S = [stirling2(11, t + 1) for t in range(11)]
print("source scenario counts (type 0..10):", scenarios_type)
print("Stirling S(11,1)..S(11,11):          ", S)
print("match:", scenarios_type == S)
print("source total:", total, " Bell(11):", bell(11), " match:", total == bell(11))

# Independent brute force: enumerate RGS length 11, count by max value (type)
def rgs_by_max(n):
    counts = Counter()
    def rec(i, m):
        if i == n:
            counts[m] += 1
            return
        for v in range(m + 2):
            rec(i + 1, max(m, v))
    counts = Counter()
    # s_1 = 0 fixed (first entry of an RGS is 0)
    rec(1, 0)
    return counts

c = rgs_by_max(11)
brute = [c[t] for t in range(11)]
print("brute-force RGS counts by max (type 0..10):", brute)
print("brute matches Stirling:", brute == S, " total:", sum(brute))
