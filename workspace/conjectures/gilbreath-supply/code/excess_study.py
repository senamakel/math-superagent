#!/usr/bin/env python3
"""Study the excess sequence E(n) = nu2(n) - (n-2)/2.

Since nu2(n) = wt(Phi_n h) = #{d in [2,n-1]: T(n,d)=1}, and there are n-2
depth values, define the signed excess
    E2(n) = 2*nu2(n) - (n-2)   (an integer).
If E2(n)/n -> 0 then nu2(n)/n -> 1/2, which is SUPPLY pointwise (any c<1/2).

We compute nu2(n) exactly for the real prime h via lib.nu2.fold_nu2 (SOS
submask transform, exact), and report growth of |E2(n)|, its max, and whether
it looks bounded.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)   # length >= n+1 needed for fold_nu2 up to n=N
    E2 = {}
    maxabs = 0
    maxabs_n = 0
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        e2 = 2 * v - (n - 2)
        E2[n] = e2
        if abs(e2) > maxabs:
            maxabs = abs(e2)
            maxabs_n = n
    # report growth of max |E2| over dyadic prefixes
    print(f"N={N}  max|E2| over [2,{N}] = {maxabs} at n={maxabs_n}")
    for k in range(2, 12):
        m = 1 << k
        if m > N: break
        M = max(abs(E2[n]) for n in range(2, m + 1))
        # ratio M/n at that point
        print(f"  prefix n<=2^{k}={m}: max|E2| = {M}  (max|E2|/m = {M/m:.4f})")
    # last few excess values
    tail = sorted(E2.keys())[-12:]
    print("tail E2 at", [(n, E2[n]) for n in tail])
    # write full excess to file for sequence tools
    with open(f"excess_E2_{N}.txt", "w") as f:
        for n in range(2, N + 1):
            f.write(f"{n} {E2[n]}\n")
    print("wrote excess_E2_%d.txt" % N)

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1000)
