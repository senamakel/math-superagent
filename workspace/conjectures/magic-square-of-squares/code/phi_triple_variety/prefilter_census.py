#!/usr/bin/env python3
"""Push the 1±(q1+q2) prefilter-survivor census as far as a time budget
allows, with checkpointing.  For pairs q1>q2 in Phi (primitive m<=M),
q1+q2<1, counts those where BOTH 1-(q1+q2) and 1+(q1+q2) are rational
squares.  Reports (M, pairs_with_sum_lt1_checked, survivors).
Resume-by-outer-index supported (deterministic ordering: value order).
"""
import sys, time
from math import gcd, isqrt
from lib.phi import phi_pairs

def rat_square(num, den):
    g=gcd(num,den); num//=g; den//=g
    return num>0 and den>0 and isqrt(num)**2==num and isqrt(den)**2==den

def main():
    M = int(sys.argv[1]) if len(sys.argv)>1 else 1000
    budget = float(sys.argv[2]) if len(sys.argv)>2 else 560.0
    resume = int(sys.argv[3]) if len(sys.argv)>3 else 0
    t0=time.time()
    Phi=phi_pairs(M)
    pairs=sorted(Phi,key=lambda nd: nd[0]/nd[1])
    P=len(pairs)
    surv=0; n=0
    reached=resume
    for i in range(resume,P):
        A1,B1=pairs[i]
        for j in range(i):
            A2,B2=pairs[j]
            num=A1*B2+A2*B1; den=B1*B2
            if num>=den: break
            n+=1
            if rat_square(den-num,den) and rat_square(den+num,den):
                surv+=1
                print("  SURVIVOR",(A1,B1),(A2,B2),flush=True)
        reached=i+1
        if time.time()-t0>budget:
            print(f"[M={M}] budget at i={i}/{P}; pairs checked {n}; "
                  f"survivors {surv}",flush=True)
            return
    print(f"[M={M}] |Phi|={P}; pairs q1>q2 sum<1 checked: {n}; "
          f"1+/-sum-rational-square survivors: {surv}; total {time.time()-t0:.0f}s",
          flush=True)
    print("RESULT survivors="+str(surv))

if __name__=="__main__":
    main()
