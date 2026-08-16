"""Confirm the general law: for degree d, the number of scenarios of type
t equals the Stirling number S(d-1, t+1), and the total is Bell(d-1).

Scenario = restricted growth string (s_1,...,s_{d-1}) with s_1=0 and
s_j <= max{s_i:i<j}+1.  Type = max entry.  Count of RGS of length n=d-1
with max value t is S(n, t+1).
"""
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

# Brute-force count RGS of length n by max value
def rgs_by_max(n):
    from collections import Counter
    counts = Counter()
    def rec(i, m):
        if i == n:
            counts[m] += 1
            return
        for v in range(m + 2):
            rec(i + 1, max(m, v))
    rec(1, 0)  # s_1 = 0 fixed
    return counts

print("degree d | n=d-1 | by-type S(n,t+1) matches brute RGS? | total==Bell(n)")
for d in range(2, 9):
    n = d - 1
    S = [stirling2(n, t+1) for t in range(n)]
    c = rgs_by_max(n)
    brute = [c[t] for t in range(n)]
    type_ok = (S == brute)
    total_ok = (sum(brute) == bell(n))
    print(f"  d={d:2d} | n={n:2d} | {type_ok} | {total_ok} (Bell(n)={bell(n)})")
