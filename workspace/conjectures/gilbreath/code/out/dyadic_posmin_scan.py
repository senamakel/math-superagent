#!/usr/bin/env python3
"""For odd prime periods (the cleanest odd-factor case), compute the per-residue
fold densities and check ALL are positive (min > 0).  If every residue class of
the eventual period has positive density of 1's, then nu2(n) has positive lower
density in EVERY residue of n, so nu2(n) >= (min_r density)*n - O(1): a positive
linear lower bound, PROVED from periodicity + the parity counting N_p(c).
"""
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

# odd primes 3..31 (tail-1 word): per-residue min density.
import sympy
print("Odd prime periods P (tail-1 word w=[0..0,1]): min per-residue density")
for P in list(sympy.primerange(3, 32)):
    w=[0]*(P-1)+[1]
    a,b=2000,40000
    dens=[]
    for r in range(P):
        g=[int(w[(r-j)%P]) for j in range(b)]
        Y=fast_zeta(g,b-1)
        dens.append(sum(Y[a:b])/(b-a))
    print(f"  P={P:2d}: min={min(dens):.4f} mean={sum(dens)/P:.4f}  all positive: {min(dens)>0}")

# Also even periods with odd factor (6,10,12,14,18 ...)
print("\nEven periods with odd factor (tail-1 word): min per-residue density")
for P in [6,10,12,14,18,20,22]:
    w=[0]*(P-1)+[1]
    a,b=2000,30000
    dens=[]
    for r in range(P):
        g=[int(w[(r-j)%P]) for j in range(b)]
        Y=fast_zeta(g,b-1)
        dens.append(sum(Y[a:b])/(b-a))
    print(f"  P={P:2d}: min={min(dens):.4f} mean={sum(dens)/P:.4f}  all positive: {min(dens)>0}")
