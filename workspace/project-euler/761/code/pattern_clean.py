#!/usr/bin/env python3
"""Clean check of K(n) structure: period-7 differences and exact recurrence."""
import math

def K_of_n(n):
    th = math.pi / n
    t = math.tan(th)
    best = None
    for k in range(0, n + 1):
        val = math.sin(k * th) - (k + n) * t * math.cos(k * th)
        if val < 0:
            best = k
    return best

NMAX = 500
Ks = [K_of_n(n) for n in range(3, NMAX + 1)]
diffs = [Ks[i] - Ks[i-1] for i in range(1, len(Ks))]
# diffs[i] = K(n) where n = i+4, i.e. diffs[0]=K(4)-K(3)
print("diffs for n=4..20:", diffs[:17])
PAT = [0,1,0,1,0,0,1]
# diffs index i corresponds to n=i+4; idx should be i % 7
breaks = [(i+4, diffs[i], PAT[i % 7]) for i in range(len(diffs)) if diffs[i] != PAT[i % 7]]
print("breaks in period-7 pattern (first 10):", breaks[:10])
print("total breaks:", len(breaks))

# exact recurrence check a(n)=a(n-1)+a(n-7)-a(n-8) for n>=11 (K index n=3..)
bad = None
for i in range(8, len(Ks)):
    # Ks[i] corresponds to n = i+3
    if Ks[i] != Ks[i-1] + Ks[i-7] - Ks[i-8]:
        bad = i + 3
        break
print("recurrence a(n)=a(n-1)+a(n-7)-a(n-8) first fail at n=", bad, " (None=holds to NMAX)")

# floor(3n/7) comparison
dev = [n for n in range(3, NMAX+1) if K_of_n(n) != math.floor(3*n/7)]
print("n where K(n)!=floor(3n/7) (first 20):", dev[:20])

# what is the phase offset? K(n) - floor(3n/7)
print("K(n)-floor(3n/7) for n=3..24:", [K_of_n(n)-math.floor(3*n/7) for n in range(3,25)])

# Closed-form via recurrence: K(n) = K0 + sum of period-7 diffs.
# differences period (from n=4): [0,1,0,1,0,0,1] starting idx0 at n=4.
# So for n>=4, K(n)=K(3) + count of 1s in diffs[0 .. n-4].
ones = PAt = [0,1,0,1,0,0,1]
def K_rec(n):
    if n < 3: return None
    if n == 3: return 1
    m = n - 4  # number of diffs from n=4..n
    full, rem = divmod(m, 7)
    cnt = full * sum(PAT) + sum(PAT[:rem])
    return 1 + cnt
# compare
mism = [(n, K_of_n(n), K_rec(n)) for n in range(3, NMAX+1) if K_rec(n) != K_of_n(n)]
print("K_rec vs exact mismatches (first 10):", mism[:10])
