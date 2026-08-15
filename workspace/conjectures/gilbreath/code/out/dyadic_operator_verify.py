#!/usr/bin/env python3
"""Direct verification of the two operator facts behind the dyadic-collapse
proof, on the cyclic F2 space:
  (i)  sigma = I + S  (Rule-90 one step = XOR of a cell and its right neighbour),
       where S is the cyclic shift on the length-P word.
  (ii) For P a power of 2: sigma^P = (I+S)^P = I + S^P = I + I = 0  (Frobenius),
       hence sigma^d = 0 for ALL d >= P  =>  every tail cell at encoder index
       c >= P is 0  =>  nu2 <= P-1.
And the contrast: for P with odd factor, sigma^P != 0 (Lucas: (1+x)^P has
intermediate terms), so no such finite collapse.
"""
import itertools, functools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def sigma_word(v):
    """Rule-90 XOR-difference on the cyclic word: sigma v [c] = v[c] xor v[c+1]."""
    P=len(v)
    return [v[c]^v[(c+1)%P] for c in range(P)]

def sigma_power(v, d):
    """= (I+S)^d v  = sum_{i submask d} S^i v   (Lucas).  Also == iterating sigma d times."""
    P=len(v)
    out=[0]*P
    for i in submasks(d):
        for c in range(P):
            out[c]^= v[(c+i)%P]
    return out

def sigma_power_iter(v, d):
    w=list(v)
    for _ in range(d):
        w=sigma_word(w)
    return w

for P in [1,2,4,8,16,3,5,6,7,12,15]:
    is_pow2 = (P & (P-1))==0
    # check operator identity: sigma_iter == subset-zeta form
    ok=True
    for vbits in itertools.product([0,1],repeat=P) if P<=4 else [(0,)*P,(1,)*P,[0]*(P-1)+[1]]:
        v=list(vbits)
        d=max(1,P)
        if sigma_power_iter(v,d)!=sigma_power(v,d):
            ok=False
    # check collapse: sigma^d v = 0 for d>=P iff pow2
    maxnz_pow2 = True
    sum_over_d=[]
    for d in range(P, P+3):
        for v in itertools.product([0,1],repeat=P) if P<=4 else [(0,)*P,(1,)*P,[0]*(P-1)+[1]]:
            if any(sigma_power(list(v),d)):
                maxnz_pow2=False
    sumd=[sum(1 for v in itertools.product([0,1],repeat=P) if any(sigma_power(list(v),d))) for d in range(1,2*P+1)] if P<=8 else None
    print(f"P={P} pow2={is_pow2}: op-identity-ok={ok}, all-zero-at-d>=P={maxnz_pow2}")
