#!/usr/bin/env python3
"""Pin down nu2(n) convention and check the ratio for 50<=n<=80 carefully.

Cross-check two routes:
  Route A (fold / Lucas): nu2(n) = #{d in [2,n-1] : T(n,d)=1}, T = XOR of
    h[n-1-d+o] over ALL submasks o of d (o from 0 to d, including d itself
    and 0).
  Route B (literal triangle): build the prime diff triangle rows, read the
    right diagonal, and the maximal {0,2} suffix. (This gave 0 everywhere
    because the bottom cell is 1 -- so the measured object is the fold.)
"""
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok=True; r=isqrt(cand)
        for p in ps:
            if p>r: break
            if cand%p==0: ok=False; break
        if ok: ps.append(cand)
        cand+=2
    return ps

def nu2_fold_A(n, h):
    cnt=0
    for d in range(2,n):
        t=0; base=n-1-d; sub=d
        while True:
            t ^= h[base+sub]
            if sub==0: break
            sub=(sub-1)&d
        cnt+=t
    return cnt

def nu2_fold_B(n, h):
    """Omit the full submask d (proper submasks 0..d-1). Compare with A."""
    cnt=0
    for d in range(2,n):
        t=0; base=n-1-d
        sub=(d-1)&d
        while True:
            t ^= h[base+sub]
            if sub==0: break
            sub=(sub-1)&d
        cnt+=t
    return cnt

def main():
    N=81
    ps = primes_upto_index(N+3)
    h=[((ps[j+1]-ps[j])//2)%2 for j in range(N+2)]
    print(" n  nu2A  A/n   nu2B  B/n")
    for n in range(50,N):
        A=nu2_fold_A(n,h); B=nu2_fold_B(n,h)
        print(f"{n:3d} {A:5d} {A/n:.4f} {B:5d} {B/n:.4f}")

if __name__=="__main__":
    main()
