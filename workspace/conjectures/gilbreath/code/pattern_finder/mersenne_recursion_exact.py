#!/usr/bin/env python3
"""Find the EXACT recursion R_{k+1} = g(R_k) for the Mersenne per-residue
half-constant arrays R_k (c_r/2), then use it to prove sum R_k = (3^k-3)/2
by induction.  This would elevate the documented Mersenne sum identity from
verified-numerically to PROVED (a genuine deliverable).
"""
# R_k for k=2..8 (from independent recomputation, confirmed to k=10)
R = {
 2: [1, 1, 1],
 3: [1, 3, 2, 2, 1, 2, 1],
 4: [1, 7, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 5: [1, 15, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
}

P = {k: 2**k - 1 for k in R}

print("Check the working hypothesis R_{k+1}[r] = 2*R_k[r] for r=2..P_k-1,")
print("R_{k+1}[0]=1, and identify the remaining entries of R_{k+1}.\n")
for k in (2, 3, 4):
    Rk = R[k]; Rn = R[k+1]; Pk = P[k]
    # test 2*R_k on the overlap r=2..Pk-1 (Rn has length Pk+1 = 2^{k+1}-1)
    # Rn[0:Pk] should be the first Pk entries
    first = Rn[:Pk]
    match = all(first[r] == 2*Rk[r] for r in range(2, Pk))
    print(f"k={k}: Rn[0:{Pk}] == 2*Rk on r=2..{Pk-1}? {match}")
    print("   Rn[0] =", Rn[0], " Rn[1] =", Rn[1], " 2*Rk[1] =", 2*Rk[1])
    # depending on match, align Rn[0:Pk] with positions
    # does Rn[0:Pk] equal 2*Rk except index 0,1?  find all mismatches
    mism = [(r, Rn[r], 2*Rk[r]) for r in range(Pk) if Rn[r] != 2*Rk[r]]
    print("   mismatches in Rn[0:Pk] vs 2*Rk:", mism[:6])
    # given Rn length = Pk+1 = 2^{k+1}-1, compare the tail Rn[Pk:] with Rk
    tail = Rn[Pk:]
    print(f"   Rn[{Pk}:] =", tail, " len", len(tail), "== Rk?", tail == Rk)
    print()
