#!/usr/bin/env python3
"""Verify the two structural facts the dyadic-collapse proof uses, using the
FAST subset-zeta transform (O(T log T)) so the complexity is cleanly polynomial
in input size T.

  (a) The subset-zeta transform Z (Y_c = XOR_{j submask of c} g_j) is an F2
      involution: Z^2 = identity.  (The intermediate sum over k with j⊆k⊆c has
      2^{|c|-|j|} terms, even unless j==c.)
  (b) Leg-2 contrapositive: if Y is eventually zero (Y_c=0 for c>=C) then
      g=Z(Y) is periodic with period a power of 2 (> C).  So if g has minimal
      period with an odd factor >1, Y is NOT eventually zero and nu2 is
      unbounded.
"""
import random

def fast_zeta(seq, T):
    """seq[0..T]; returns Zseq[c] = XOR_{j submask c} seq[j], for c=0..T.
    Standard O(T log T) subset-zeta (in-place, XOR, F2)."""
    z=seq[:]
    # iterate over bits; nbits = bit length of T
    nb = T.bit_length()
    for b in range(nb):
        bit=1<<b
        for mask in range(T+1):
            if mask & bit:
                z[mask] ^= z[mask ^ bit]
    return z

random.seed(7)
# (a) involution: Z(Z(g)) == g on levels 0..T
print("(a) subset-zeta involution Z^2 = id over F2")
ok=True
for T in [5, 20, 63, 127, 255]:
    for _ in range(40):
        g=[random.randint(0,1) for _ in range(T+1)]
        Zg=fast_zeta(g,T)
        Z2g=fast_zeta(Zg,T)
        if Z2g!=g:
            ok=False; print("  involution fail T",T); break
    if not ok: break
print("  Z^2 = identity on levels 0..T:", ok)

# (b) contrapositive: Y_c=0 for c>=C  =>  g=Z(Y) periodic with period 2^R>C
print("\n(b) Y eventually zero (c>=C) forces g periodic with period power of 2")
for C in [5, 9, 17, 33]:
    R=0
    while (1<<R) <= C: R+=1          # 2^R > C
    T=300
    pd=1<<R
    inert=True
    for _ in range(400):
        Y=[random.randint(0,1) if c<C else 0 for c in range(T+1)]
        g=fast_zeta(Y,T)
        for j in range(1, T+1):
            if g[j]!=g[j % pd]:
                inert=False; break
        if not inert: break
    print(f"  C={C} (2^R={pd}): all {400} trials g is period-dividing-{pd}: {inert}")

# (c) sanity: for g the natural prime-less periodic words used in Leg(2), the
#     corresponding Y is NOT eventually zero (so nu2 unbounded).
print("\n(c) minimal-period odd-factor words give non-eventually-zero Y")
def yseq(word, T):
    L=len(word)
    h=[int(word[i%L]) for i in range(T+1)]
    return fast_zeta(h,T)
for word in [[0,0,1],[0,0,0,0,1],[0]*5+[1],[0]*6+[1],[0]*14+[1]]:
    T=240
    Y=yseq(word,T)
    last_zero_run=0
    # longest suffix of zeros of Y on levels 100..T
    run=0; best=0
    for c in range(100,T+1):
        if Y[c]==0: run+=1; best=max(best,run)
        else: run=0
    print(f"  word len={len(word)}: nonzero levels >=100 present: {any(Y[c]==1 for c in range(100,T+1))}, longest zero-run in [100,{T}]={best}")
