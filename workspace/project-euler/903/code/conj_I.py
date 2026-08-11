#!/usr/bin/env python3
"""conj_I.py — I_n = sum_{(pi,i), 0<=i<n!} inv(pi^i) via conjugacy classes.

I_n = sum_{(pi,i)} inv(pi^i)  (total inversions over all power stacks).

Unlike f_n(k) (which pins element 0, NOT conjugation-invariant), I_n is a
conjugation-invariant statistic: for c pi c^{-1} the whole orbit is conjugated
and inv is preserved.  So

  I_n = sum_{lambda |- n} class_size(lambda) * (n!/lcm(lambda)) * S_inv(lambda),
  S_inv(lambda) = sum_{t=0}^{lcm(lambda)-1} inv(pi^t) for a representative pi.

power pi^t read analytically off cycles (position += t mod L).

Correct (unlike ccsum.py which pinned element 0).  Sanity: I_n must equal the
affine comb A_n*n(n-1)/2 + B_n*n(n-1)(n-2)/6 for the TRUSTED n=2..11, where
A_n,B_n come from out/extend_f.json.
"""
import json, math, time, os, sys

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
        for p in parts: d=d*p//math.gcd(d,p)
        m={}
        for p in parts: m[p]=m.get(p,0)+1
        denom=1
        for j,mj in m.items(): denom*=(j**mj)*math.factorial(mj)
        cs=nf//denom
        w=nf//d
        weight=cs*w
        # representative cycles
        perm=[0]*n
        nxt=0; cycles=[]
        for L in parts:
            cyc=list(range(nxt,nxt+L)); cycles.append(cyc)
            for j in range(L):
                perm[cyc[j]]=cyc[(j+1)%L]
            nxt+=L
        # S_inv: sum over t=0..d-1 of inv(pi^t)
        Sinv=0
        for t in range(d):
            pos_t=[((j if j<d else 0)) for j in range(0)]  # placeholder
            # image of each element under pi^t : element in cycle ci at position pos -> (pos+t)%L
            idx_ci={}; pos_in={}
            for ci,cyc in enumerate(cycles):
                for p,el in enumerate(cyc):
                    idx_ci[el]=ci; pos_in[el]=p
            img=[0]*n
            for el in range(n):
                ci=idx_ci[el]; Lc=len(cycles[ci])
                img[el]=cycles[ci][(pos_in[el]+t)%Lc]
            # inversions of img
            inv=0
            for a in range(n):
                for b in range(a+1,n):
                    if img[b]<img[a]: inv+=1
            Sinv+=inv
        total+=weight*Sinv
    return total

if __name__=="__main__":
    A_={2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,10:5514150297600,11:680309947699200}
    B_={3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,10:-85305830400,11:-9900701798400}
    lo=int(sys.argv[1]) if len(sys.argv)>1 else 2
    hi=int(sys.argv[2]) if len(sys.argv)>2 else 18
    res={}
    if os.path.exists("out/conj_I.json"): res=json.load(open("out/conj_I.json"))
    for n in range(lo,hi+1):
        t0=time.time()
        val=I_n(n)
        res[str(n)]=val
        json.dump(res,open("out/conj_I.json","w"))
        # sanity vs affine comb for trusted
        msg=""
        if n in A_:
            bc=B_.get(n,0)
            comb=A_[n]*n*(n-1)//2+bc*n*(n-1)*(n-2)//6
            msg="MATCH trusted" if comb==val else f"MISMATCH now={val} exp={comb}"
        print(f"n={n}: I_n={val}  ({time.time()-t0:.2f}s) {msg}",flush=True)
