#!/usr/bin/env python3
"""Attack the MA(1)-boundary finding for a parity artifact.

D(n)=2nu2(n)-n satisfies D(n) == n (mod 2) EXACTLY (2nu2 even => -n mod 2).
So D ALWAYS alternates parity. Could that alone explain rho1(I)=-0.5?

Tests:
 1) Confirm the parity identity exactly.
 2) Parity-detraod D: define U(n) such that removal of the deterministic alternating
    part leaves white noise. Simplest: look at D on even n only, and odd n only
    (two subsequences, each ~constant-parity). Check acf of each subsequence.
 3) Simulate a pure alternation: A(n) = (n mod 2) -> I(n)=A(n+1)-A(n)=±1,
    rho1(I) = ?  -> check whether alternation alone gives -0.5.
 4) The real question: after removing alternation, is there still a slow trend;
    is the residual white?
"""
import math, random

def load():
    nu2={}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            p=line.split()
            if len(p)==2: nu2[int(p[0])]=int(p[1])
    return nu2

def acf(xs,maxlag):
    m=sum(xs)/len(xs); xc=[x-m for x in xs]; v=sum(x*x for x in xc)
    return [sum(xc[i]*xc[i+lag] for i in range(len(xs)-lag))/v for lag in range(1,maxlag+1)]

def var(xs):
    m=sum(xs)/len(xs); return sum((x-m)**2 for x in xs)/len(xs)

def main():
    nu2=load(); ns=sorted(nu2); D=[2*nu2[n]-n for n in ns]; N=len(D)
    # 1) parity identity
    ok = all((D[i]-((i+1)%2))%2==0 for i in range(N))
    print("D(n) == n (mod 2) exactly for all %d n: %s" % (N, ok))

    # 2) pure alternation surrogate
    random.seed(2)
    A=[(i+1)%2 for i in range(N)]
    IA=[A[i+1]-A[i] for i in range(N-1)]
    print("pure alternation: rho1(I_A)=%.3f" % acf(IA,1)[0])

    # real I
    I=[D[i+1]-D[i] for i in range(N-1)]
    print("real: rho1(I)=%.3f" % acf(I,1)[0])
    print("real: acf(D) lags1..6: %s" % " ".join("%.3f"%a for a in acf(D,6)))

    # 3) subsequences by parity (each approx same parity if we subtract alternating)
    # Actually D alternates parity, so even n -> even D? D(n)==n mod2: n even -> D even.
    Deven  = [D[i] for i in range(N) if (i+1)%2==0]
    Dodd   = [D[i] for i in range(N) if (i+1)%2==1]
    print("acf(Deven)  lags1..8:", " ".join("%.3f"%a for a in acf(Deven,8)))
    print("acf(Dodd)   lags1..8:", " ".join("%.3f"%a for a in acf(Dodd,8)))
    print("Var(Deven)=%.1f Var(Dodd)=%.1f" % (var(Deven), var(Dodd)))

    # 4) Does |D| grow? runmax on even subsequence only
    cm=0
    prev=0
    for i in range(N):
        if i>=1000 and (i+1)%2==0:
            pass
    # windowed std of D (full) - already known to grow. Report again cleanly
    w=3000
    stds=[math.sqrt(var(D[i:i+w])) for i in range(0,N,w)]
    print("std(D) per 3000-window:", ["%.1f"%s for s in stds])

    # 5) trend: mean of D in each window (should be ~0 if no deterministic drift)
    means=[sum(D[i:i+w])/len(D[i:i+w]) for i in range(0,N,w)]
    print("mean(D) per window:", ["%+.1f"%m for m in means])
    # if means ~0 but std grows => amplitude modulation, not drift
    print("=> if means≈0 and std grows: |D| amplitude ~ c*sqrt(n) * white sign, i.e. sublinear.")

if __name__=="__main__":
    main()
