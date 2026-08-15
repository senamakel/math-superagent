#!/usr/bin/env python3
"""Discover the exact recursion for the Mersenne per-residue half-constant
array R_k = c_r/2, length P_k = 2^k - 1, for the tail-1 word.

The affinity structure nu2(n+P) = nu2(n) + c_{n mod P} (exact, per residue)
is established for P = 2^k - 1.  We have sum c_r = 3^k - 3 (confirmed to k=8).
Here we nail the exact self-similar recursion R_{k+1} = F(R_k).

Print R_k for k=2..7 and test candidate recursions:
  Candidate A: R_{k+1} = 2*R_k  (value-scaling) with index mapping
  Candidate B: block decomposition
We look at R_k and R_{k+1} side by side to fit F exactly.
"""
Rs = {
 2: [1, 1, 1],
 3: [1, 3, 2, 2, 1, 2, 1],
 4: [1, 7, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 5: [1, 15, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 6: [1, 31, 16, 16, 8, 16, 8, 8, 4, 16, 8, 8, 4, 8, 4, 4, 2, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 16, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
}

def double_and_add1(A):
    # 2*value, except replace the last 1 by...  test: R_{k+1}[1:] vs 2*R_k
    return [2 * x for x in A]

for k in (2, 3, 4, 5):
    Rnext = Rs[k + 1]
    R = Rs[k]
    P = len(R)
    print(f"k={k}->{k+1}: len R={P}, len Rnext={len(Rnext)}")
    print("  R      =", R)
    print("  Rnext  =", Rnext)
    # Rnext = [1] ++ T where T = Rnext[1:]
    T = Rnext[1:]
    print("  T=Rnext[1:] =", T)
    # is R = 2*R_k for T in some window?  Check T[0:len(R)]
    print("  T[0:P]  =", T[:P])
    print("  2*R     =", double_and_add1(R))
    print()
