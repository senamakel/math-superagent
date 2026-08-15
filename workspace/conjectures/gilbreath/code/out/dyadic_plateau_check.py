#!/usr/bin/env python3
"""Confirm that for EVENTUALLY-(2^k)-periodic h (preperiod + power-of-2 tail),
nu2(q_T) is BOUNDED as T->oo (plateaus), not just on the tested range.
Rationale: for T large the fold window [T-c, T-1] for c >= some threshold is
entirely inside the 2^k tail, whose fold is exactly zero beyond the tail's
2^k level (leg-1 exact).  Verify the plateau.
"""
def fast_zeta(seq,T):
    z=seq[:]; nb=T.bit_length()
    for b in range(nb):
        bit=1<<b
        for mask in range(T+1):
            if mask&bit: z[mask]^=z[mask^bit]
    return z

def build_evperiodic(pre, tailword, JMAX):
    L=len(tailword); P=len(pre)
    return [int(pre[j]) if j<P else int(tailword[(j-P)%L]) for j in range(JMAX+1)]

def nu2_of(h,T):
    g=[h[T-j] for j in range(T+1)]
    Y=fast_zeta(g,T)
    return sum(Y[1:T+1])

print("nu2(q_T) plateau for eventually-2^k-periodic h (preperiod+tail):")
case_id=0
for k in [1,2,3,4]:
    L=2**k
    tail=[0]*(L-1)+[1]
    for pre in [[], [1],[0],[0,1,0],[1,1,0,0],[0,0,0,1,0]]:
        h=build_evperiodic(pre,tail,800000)
        prev=None; vals=[]
        for T in [5000,20000,100000,400000,799998]:
            v=nu2_of(h,T)
            vals.append(v)
            prev=v
        plateau = (vals[-1]==vals[-2]==vals[-3] if len(vals)>=3 else True)
        print(f"  k={k} pre={str(pre):>12}: nu2 at T=5k,20k,100k,400k,800k = {vals}  plateau={plateau}")
