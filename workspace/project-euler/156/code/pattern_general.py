import sys
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

# Derived identity (exact, from the place-value closed form):
#   f(k*10^m, d) = m*k*10^(m-1) + (10^m if k>d) + (1 if k==d), for 1<=k<=9, m>=1, d in 1..9
def closed(k, m, d):
    v = m*k*10**(m-1)
    if k > d: v += 10**m
    if k == d: v += 1
    return v

fails = []
checked = 0
for m in range(1, 14):
    for k in range(1, 10):
        for d in range(1, 10):
            n = k*10**m
            got = f_place_value(n, d)
            exp = closed(k, m, d)
            checked += 1
            if got != exp:
                fails.append((m,k,d,n,got,exp))
print(f"checked {checked} triples (m in 1..13, k,d in 1..9): identity holds = {len(fails)==0}")
print("failures:", fails[:10])

# Consequence: k*10^10 is a solution of f(n,d)=n  <=>  k <= d-1 (k in 1..9) plus k=0->0
print("\nConsequence check for m=10 (the problem's range):")
bad = []
for d in range(1,10):
    for k in range(0,10):
        n = k*10**10
        is_sol = (f_place_value(n,d)==n)
        pred = (k <= d-1)
        if is_sol != pred: bad.append((d,k))
print("  k*10^10 sol  <=>  k<=d-1 holds:", len(bad)==0, "bad:", bad)

# Also: how does the solution set split into 'block multiples' vs sparse?
# For d with only block solutions (d=5,9) the whole set is k*10^10. Confirm counts.
import os
for d in [5,9]:
    sols=[int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
    pred=[k*10**10 for k in range(d)]
    print(f"d={d}: full solution set == [k*10^10 for k in 0..{d-1}]? {sols==pred}")
