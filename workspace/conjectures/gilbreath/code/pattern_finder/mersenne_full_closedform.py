#!/usr/bin/env python3
"""Complete recursive closed-form generator for Mersenne c_r/2 arrays, tested
against the independently-computed arrays.  If the closed form reproduces the
computed arrays exactly, we have a full description of the whole structure.

Recursion (pinned from verified data):
  P_k has length 2^k - 1.
  Let h = P_k[0 : 2^(k-1)]  (first half, length 2^(k-1))
      t = P_k[2^(k-1) : ]   (tail, length 2^(k-1)-1)
  Observed:
    t == P_{k-1} except t[1] = P_{k-1}[1] + 1.        (tail recursion)
    h[:-1] == 2*P_{k-1} except h[0]=1 fixed, h[1]=2*P_{k-1}[1]+1; h[-1]=h[-2]=2.
  We assert this generator exactly and check against lib.rightdiag computed arrays.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2

def build_seq(word, n_terms):
    q=[2,3]; per=len(word)
    while len(q)<n_terms:
        bit=word[(len(q)-2)%per]; q.append(q[-1]+(2 if bit else 4))
    return q[:n_terms]

def nu2_seq(word,nmax):
    q=build_seq(word,nmax+1); out={}
    for k,dd in enumerate(incremental_diagonals(q)):
        if k>=2: out[k]=cycle_and_nu2(dd)[1]
    return out

def computed_P(k):
    P=2**k-1; nmax=min(P*4+300,20000); nmin=P+150
    vals=nu2_seq([0]*(P-1)+[1],nmax)
    seen={}
    for n in range(nmin,nmax-P+1):
        d=vals[n+P]-vals[n]; r=n%P
        if r in seen and seen[r]!=d: raise RuntimeError(f"not affine k={k}")
        seen[r]=d
    return [seen[r]//2 for r in range(P)]

# closed-form generator
def gen_P(k):
    assert k>=2
    if k==2: return [1,1,1]
    Pkm = gen_P(k-1)
    # Pkm length m = 2^(k-1)-1
    h = [1] + [2*Pkm[1]+1] + [2*x for x in Pkm[2:]] + [2]
    # h length: 1+1+(m-2)+1 = m+1 = 2^(k-1)  (verified against computed first halves)
    t = list(Pkm); t[1] = Pkm[1]+1
    return h + t

ok=True
for k in range(2,12):
    gen=gen_P(k)
    comp=computed_P(k)
    match=(gen==comp)
    ok = ok and match
    print(f"k={k:2d} len={len(gen):5d} generator==computed: {match}")
print("ALL MATCH" if ok else "MISMATCH FOUND")
