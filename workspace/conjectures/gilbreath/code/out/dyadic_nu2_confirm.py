#!/usr/bin/env python3
"""Confirm nu2 (right-diagonal {0,2}-suffix count, from lib.rightdiag) satisfies
nu2 <= fold_weight <= 2^k - 1 for period-2^k periodic 2-then-odds sequences,
matching the empirical table's O(1) verdict. Also confirm odd-factor periods
give nu2 that grows (positive density) on generic words."""
from lib.rule90fold import fold_weight_h
from lib.rightdiag import delta_diagonal, cycle_and_nu2
import random

def period_seq(word, n):
    seq=[2,3]
    L=len(word)
    for j in range(n-2):
        bit=int(word[j%L])
        seq.append(seq[-1]+(2 if bit else 4))
    return seq

def halved_bits(seq):
    return [((seq[c+1]-seq[c])//2)%2 for c in range(len(seq)-1)]

random.seed(2)
print("=== nu2 vs fold_weight for period-2^k ===")
for k in [1,2,3,4]:
    P=2**k
    for word in ['0'*(P-1)+'1','01' if P==2 else '0'*P+'1'] if False else []:
        pass
    # a few words per period
    words=set(['0'*(P-1)+'1', '1'*P])
    for _ in range(10):
        words.add(''.join(random.choice('01') for _ in range(P)))
    for word in words:
        for n in [150, 350]:
            seq=period_seq(word,n)
            h=halved_bits(seq)
            m=n-2
            hab = h[2:2+m] if len(h)>=2+m else h[2:]+[0]*(2+m-len(h))
            fw=fold_weight_h(hab,m)
            d=delta_diagonal(seq,n-1)
            tau,nu2=cycle_and_nu2(d)
            assert nu2<=fw and fw<=P-1, (word,n,nu2,fw,P)
    print(f"  period {P}: nu2<=fold_wt<=2^k-1={P-1} held on {len(words)} words x n in {{150,350}}")

print("=== odd-factor period: nu2 grows (generic words) vs collapses (constant words) ===")
for p in [3,5,6,7,9,12,15]:
    for word in ['0'*p, '1'*p, '0'*(p-1)+'1']:
        vs=[]
        for n in [200,400,800]:
            seq=period_seq(word,n)
            h=halved_bits(seq); m=n-2
            hab=h[-m:] if len(h)>=m else h+[0]*(m-len(h))
            fw=fold_weight_h(hab,m)
            d=delta_diagonal(seq,n-1)
            tau,nu2=cycle_and_nu2(d)
            vs.append(nu2)
        tag = ("CONSTANT-collapse" if word in ('0'*p,'1'*p) else "generic")
        print(f"  period {p} word {word[:4]}.. ({tag}): nu2 at n=200,400,800 = {vs}")
