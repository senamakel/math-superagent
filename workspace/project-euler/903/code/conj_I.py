#!/usr/bin/env python3
"""conj_I.py (fixed) — I_n = sum_{(pi,i), 0<=i<n!} inv(pi^i) via conjugacy classes.

inv is conjugation-invariant (renumbering labels preserves which pairs invert),
and the cyclic-subgroup sum of inv is likewise |<pi>| constants across a class,
so I_n = sum over cycle types lambda of
    class_size(lambda) * (n!/lcm(lambda)) * S_inv(lambda),
S_inv(lambda) = sum_{t=0}^{lcm(lambda)-1} inv(pi^t)  for a representative.

Power pi^t read analytically off cycles (image of element = cycle[ (pos+t)%L ]).

PROOF-OF-CORRECTNESS (oracle): I_n must equal the affine comb
A_n*n(n-1)/2 + B_n*n(n-1)(n-2)/6 computed from the TRUSTED extend_f.json A_n,B_n
for n=2..11 (these are themselves verified by independent enumeration).  Only
after matching n=2..11 exactly do we trust the extension to larger n.
"""
import json, math, time, os, sys
from math import gcd

def partitions(n):
    parts=[0]*n; out=[]
    def rec(rem, mx, idx):
        if rem==0:
            out.append(list(parts[:idx])); return
        for p in range(min(mx,rem),0,-1):
            parts[idx]=p; rec(rem-p,p,idx+1)
    rec(n,n,0); return out

def I_n(n):
    nf=math.factorial(n)
    total=0
    for parts in partitions(n):
        d=1
        for p in parts: d=d*p//gcd(d,p)
        m={}
        for p in parts: m[p]=m.get(p,0)+1
        denom=1
        for j,mj in m.items(): denom*=(j**mj)*math.factorial(mj)
        cs=nf//denom
        w=nf//d
        weight=cs*w
        # representative cycles (consecutive integers)
        cycles=[]; nxt=0
        for L in parts:
            cycles.append(list(range(nxt,nxt+L))); nxt+=L
        # element -> (cycle idx, pos-in-cycle)
        idxc={}; pos={}
        for ci,cyc in enumerate(cycles):
            for p_,el in enumerate(cyc):
                idxc[el]=ci; pos[el]=p_
        # S_inv = sum over t=0..d-1 of inv(pi^t)
        Sinv=0
        for t in range(d):
            img=[0]*n
            for el in range(n):
                ci=idxc[el]; Lc=len(cycles[ci])
                img[el]=cycles[ci][(pos[el]+t)%Lc]
            inv=0
            for a in range(n):
                for b in range(a+1,n):
                    if img[b]<img[a]: inv+=1
            Sinv+=inv
        total+=weight*Sinv
    return total

if __name__=="__main__":
    A_=json.load(open("out/extend_f.json"))
    # trusted A_n,B_n (B requires n>=3; n=2 has single entry, B=0)
    Atr={int(k):v[0] for k,v in A_.items()}
    Btr={int(k):(v[1]-v[0]) if len(v)>=2 else 0 for k,v in A_.items()}
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 2
    hi=int(sys.argv[2]) if len(sys.argv)>2 else 20
    res={}
    if os.path.exists("out/conj_I.json"): res=json.load(open("out/conj_I.json"))
    for n in range(lo,hi+1):
        t0=time.time()
        val=I_n(n)
        res[str(n)]=val
        json.dump(res,open("out/conj_I.json","w"))
        msg="NOTRUST"
        if n in Atr and n in Btr:
            comb=Atr[n]*n*(n-1)//2+Btr[n]*n*(n-1)*(n-2)//6
            msg="MATCH trusted" if comb==val else f"MISMATCH now={val} exp={comb}"
        print(f"n={n}: I_n={val}  ({time.time()-t0:.2f}s) {msg}",flush=True)
