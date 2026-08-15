"""Probe the increment structure of the nu2 walk and its deviation.

nu2(n) from nu2_dense.txt (n=1..30000, exact, sieve 1e6).
Questions:
  (A) how much can nu2 change in one step? min/max nu2(n+1)-nu2(n)
  (B) how much can the deviation e(n)=2*nu2(n)-n change in one step?
  (C) is e(n) ever monotone nondecreasing over long stretches? (run-length structure)
  (D) does nu2(n) itself stay close to a walk? record the increment multiset
"""
import sys

def read_nu2(path):
    vals = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = line.split()
            if len(p) == 2:
                n, v = int(p[0]), int(p[1])
                vals[n] = v
    return vals

nu2 = read_nu2("code/out/nu2_dense.txt")
ns = sorted(nu2.keys())
print(f"n range: {ns[0]}..{ns[-1]}  count={len(ns)}")

# increments of nu2
incs = [nu2[ns[i+1]] - nu2[ns[i]] for i in range(len(ns)-1)]
from collections import Counter
c = Counter(incs)
print("\n(A) nu2(n+1)-nu2(n) distribution over consecutive n:")
print("    min", min(incs), " max", max(incs))
print("    top increments:", c.most_common(12))
valset = sorted(set(incs))
print("    distinct values:", valset)

# increments of deviation e = 2*nu2 - n
e = {n: 2*nu2[n] - n for n in ns}
eincs = [e[ns[i+1]] - e[ns[i]] for i in range(len(ns)-1)]
ce = Counter(eincs)
print("\n(B) e(n+1)-e(n) = 2*nu2(n+1)-2*nu2(n)-1  distribution:")
print("    min", min(eincs), " max", max(eincs))
print("    top:", ce.most_common(12))
print("    distinct:", sorted(set(eincs)))

# (C) longest monotone (>=0 = nondecreasing step) runs of e
maxrun = 0; cur = 0; bestinfo = None
for i in range(len(eincs)):
    if eincs[i] >= 0:
        cur += 1
        if cur > maxrun:
            maxrun = cur
            bestinfo = (ns[i]-maxrun+1, ns[i]+1)  # roughly
    else:
        cur = 0
print(f"\n(C) longest nondecreasing run of e: {maxrun} steps")
# longest strictly increasing
maxrun2=0; cur2=0
for i in range(len(eincs)):
    if eincs[i] > 0:
        cur2+=1; maxrun2=max(maxrun2,cur2)
    else:
        cur2=0
print(f"    longest strictly-increasing run of e: {maxrun2} steps")

# (D) distribution of nu2 increments: how often 0, +/-1, +/-2...
total = len(incs)
for d in [-3,-2,-1,0,1,2,3]:
    print(f"    inc={d}: {c.get(d,0)}  ({100*c.get(d,0)/total:.2f}%)")
print(f"    |inc|>=2 count: {sum(v for k,v in c.items() if abs(k)>=2)}  ({100*sum(v for k,v in c.items() if abs(k)>=2)/total:.2f}%)")
