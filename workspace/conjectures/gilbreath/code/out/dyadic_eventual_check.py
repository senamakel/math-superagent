#!/usr/bin/env python3
"""Test leg (1) under the EXACT hypothesis of the claim: h EVENtUALLY periodic
with minimal period 2^k (a pre-period followed by a 2^k-periodic tail), and
confirm nu2 stays O_k(1) (bounded).  Also test the sharpness of the <= 2^k-1
bound in the purely periodic case, and record the eventual bound V_k.
"""
import itertools, functools

def fast_zeta(seq, T):
    z=seq[:]
    nb=T.bit_length()
    for b in range(nb):
        bit=1<<b
        for mask in range(T+1):
            if mask & bit:
                z[mask]^=z[mask^bit]
    return z

def nu2_of(h, T):
    """fold weight: count of ones among Y_1..Y_T where Y=Z(g), g_j=h[T-j]."""
    g=[h[T-j] for j in range(T+1)]
    Y=fast_zeta(g,T)
    return sum(Y[1:T+1])

# build h[j] for j=0..JMAX: preperiod 'pre' then 'tail' (tail minimal period 2^k)
def build_evperiodic(pre, tailword, JMAX):
    L=len(tailword); P=len(pre)
    h=[]
    for j in range(JMAX+1):
        if j < P: h.append(pre[j])
        else: h.append(int(tailword[(j-P) % L]))
    return h

print("leg(1) eventual-periodic (pre-period + 2^k tail): nu2 over n, bounded?")
rows=[]
for k in [1,2,3]:
    L=2**k
    tail=[0]*(L-1)+[1]
    for pre in [[], [1], [0],[0,0,1],[1,1,0,0]]:
        h=build_evperiodic(pre, tail, 6000)
        maxnu=0
        for n in [100,300,600,1200,2500,5000]:
            T=n-2
            v=nu2_of(h,T)
            maxnu=max(maxnu,v)
        rows.append((k,len(pre),maxnu))
        print(f"  k={k} prelen={len(pre)} pre={pre} max nu2 over n<5000 = {maxnu}")
print("\n(all should be O_k(1), independent of n — bounded as n grows)")

print("\nleg(1) sharpness: is max nu2 == 2^k - 1 for some word?")
for k in [1,2,3,4]:
    L=2**k; best=0; bestw=None
    for bits in itertools.product([0,1],repeat=L):
        w=list(bits)
        if [w[i % (L//2)] for i in range(L)]==w and L>2:  # has smaller period 2^{k-1}?
            pass
        # just track max over all words (including non-minimal)
        h=[int(bits[j%L]) for j in range(6000)]
        T=2000; g=[h[T-j] for j in range(T+1)]; Y=fast_zeta(g,T)
        v=sum(Y[1:T+1])
        if v>best: best, bestw=v, w
    print(f"  k={k}: max nu2 over all 2^{k}-periodic words = {best}  (2^k-1={L-1})")
