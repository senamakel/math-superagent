#!/usr/bin/env python3
"""Examine the second-entry sequence s_k = A_k(1) in {0,2} (the conjecture object).
Also examine the fluctuation dev(n)=2*nu2-n for residue periodicity.
"""
import json
from collections import Counter

with open("code/out/blocks_depth1000.json") as f:
    data = json.load(f)
s = data["s"]  # 1000 values in {0,2}
print("s length:", len(s), "value counts:", Counter(s))

# run structure
def runs(seq):
    out=[]
    cur=seq[0]; c=1
    for x in seq[1:]:
        if x==cur: c+=1
        else:
            out.append((cur,c)); cur,c=x,1
    out.append((cur,c))
    return out
rs = runs(s)
from collections import defaultdict
byv=defaultdict(list)
for v,c in rs: byv[v].append(c)
for v in (0,2):
    print(f"runs of {v}: count={len(byv[v])} mean={sum(byv[v])/len(byv[v]):.3f} max={max(byv[v])}  first15={byv[v][:15]}")
# longest run overall
print("longest run:", max(rs,key=lambda t:t[1]), "first few runs:", rs[:12])

# consecutive pattern: Markov-ish? count transitions
tr=Counter()
for i in range(len(s)-1):
    tr[(s[i],s[i+1])]+=1
print("transitions:", dict(tr))

# dev residue periodicity: count dev mod 2, mod 4 over dense n
nu2={}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2[int(p[0])]=int(p[1])
dev=[2*nu2[n]-n for n in sorted(nu2)]
print("dev mod 2:", Counter(d%2 for d in dev))
print("dev mod 4:", Counter(d%4 for d in dev))
print("dev even count:", sum(1 for d in dev if d%2==0), "/", len(dev))
