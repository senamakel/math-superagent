#!/usr/bin/env python3
"""Per-residue-class density of the fold, to see whether leg(2)'s
'uniform positive-linear nu2 ~ c n' holds for ALL residue classes or only the
liminf (which needs every residue positive).  For h periodic period P, the
diagonal-n output is sum_{c<=T} f_r(c), r=(n-3) mod P,
f_r(c) = XOR_{j subset c} w[(r-j) mod P].
"""
import functools

def fast_zeta(seq,T):
    z=seq[:]; nb=T.bit_length()
    for b in range(nb):
        bit=1<<b
        for mask in range(T+1):
            if mask&bit: z[mask]^=z[mask^bit]
    return z

def minimal_period(word):
    L=len(word)
    for p in range(1,L+1):
        if L%p==0 and all(word[i]==word[i%p] for i in range(L)): return p
    return L

def density_f_r(w, P, r, a=3000, b=20000):
    # f_r(c) for a<=c<b: XOR_{j subset c} w[(r-j)%P]
    # build g_j = w[(r-j)%P] for j=0..b-1 then fast zeta
    g=[int(w[(r-j)%P]) for j in range(b)]
    Y=fast_zeta(g,b-1)
    return sum(Y[a:b])/(b-a), Y

for word in [[0,0,1],[0,0,0,0,1],[0]*6+[1],[0]*14+[1],[1,0],[0,0,0,1]]:
    P=minimal_period(word)
    w=word
    print(f"\n{P}-period word {w}")
    dens=[]
    for r in range(P):
        d,_=density_f_r(w,P,r)
        dens.append(d)
    print(f"   per-residue densities r=0..{P-1}: {[f'{d:.3f}' for d in dens]}")
    print(f"   min={min(dens):.3f} max={max(dens):.3f} mean={sum(dens)/P:.3f}")
