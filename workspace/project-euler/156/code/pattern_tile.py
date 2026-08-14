import os
from collections import defaultdict

# Hypothesis: within digit d, block k (floor(n/10^10)=k) solutions equal
# k*10^10 + block-0 solutions (a translational self-similarity of the solution set).
# d=1 has only block 0. d=5,9 each block is just [k*10^10].
print("Testing: block_k == {k*10^10 + x : x in block_0}  (translation self-similarity)")
for d in range(1,10):
    sols=[int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
    grp=defaultdict(list)
    for n in sols: grp[n//10**10].append(n)
    ks=sorted(grp)
    block0=grp[ks[0]]
    allmatch=True
    details=[]
    for k in ks[1:]:
        expected=sorted([k*10**10+x for x in block0])
        if grp[k]==expected:
            details.append((k,"match"))
        else:
            allmatch=False
            details.append((k,f"DIFF {grp[k]}"))
    print(f"d={d}: blocks={ks} translation-selfsimilar={allmatch} {details}")
