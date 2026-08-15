#!/usr/bin/env python3
"""Final dichotomy check.
(A) Collapse: for EVERY period-2^k word, output_c == 0 for all c >= 2^k,
    and nu2 = wt(fold) <= 2^k - 1 for all m (checked to large m).
(B) Odd factor: for period with odd factor, #nonzero outputs grows roughly
    linearly in m (positive density), so nu2 ~ c*m.
(C) Sharpness: word [0..01] achieves wt = 2^k - 1.
"""
import functools, itertools, random
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def fold_cells(h,m):
    """cells[c] for c in 1..m-1 (valid encoder range), matching fold_weight_h."""
    cells={}
    for k in range(2,m+1):
        c=k-1
        s=0
        for i in range(k):
            if (i&c)==i:
                s^=h[m-k+i]
        cells[c]=s
    return cells

def periodic_h(word,m):
    L=len(word)
    return [int(word[j%L]) for j in range(m)]

def has_odd_factor(p):
    return p & (p-1) != 0

# (A) collapse for period-2^k: exhaustive small words, random large m
print("=== (A) Collapse: period 2^k => output_c=0 for c>=2^k ===")
for k in [1,2,3,4,5]:
    L=2**k
    viol=0
    for _ in range(400):
        word=''.join(random.choice('01') for _ in range(L))
        m=random.randint(max(L+2,30), 3000)
        cells=fold_cells(periodic_h(word,m),m)
        bad=[c for c in range(1,m) if c>=L and cells[c]==1]
        if bad: viol+=1; print("  VIOL k",k,"word",word,"m",m,"bad",bad[:5])
    print(f"  k={k} L={L}: 400 random words x random m: violations={viol}")
    # nu2 bound
    nu2max=0
    for _ in range(200):
        word=''.join(random.choice('01') for _ in range(L))
        m=random.randint(max(L+2,30), 5000)
        nu2max=max(nu2max, sum(cells.values()) if (cells:=fold_cells(periodic_h(word,m),m)) else 0)
    print(f"     -> max nu2 over 200 random words = {nu2max} (upper bound 2^k-1 = {L-1})")

# (C) sharpness
print("=== (C) Sharpness: word 0..01 achieves 2^k-1 ===")
for k in [1,2,3,4,5]:
    L=2**k
    word='0'*(L-1)+'1'
    m=2000
    cells=fold_cells(periodic_h(word,m),m)
    print(f"  k={k} L={L} word {word}: wt={sum(cells.values())} (2^k-1={L-1})")

# (B) odd factor grows linearly
print("=== (B) Odd-factor periods: #nonzero grows ~ linearly in m ===")
for p in [3,5,6,7,9,10,12,15]:
    word='0'*(p-1)+'1'   # single 1 in period
    cnts=[]
    for m in [200,400,800,1600]:
        cells=fold_cells(periodic_h(word,m),m)
        cnts.append(sum(1 for c,v in cells.items() if v==1))
    ratio=[cnts[i]/[200,400,800,1600][i] for i in range(4)]
    print(f"  period {p}: #nonzero at m=200,400,800,1600 = {cnts} ; density ~ {ratio[-1]:.3f}")
