#!/usr/bin/env python3
"""Search for the exact self-similar recursion of the Mersenne c_r/2 array
A_k (length 2^k - 1), tail-1 word.  The goal is a construction of A_{k+1}
from A_k that (a) is verified exactly to k-10 and (b) yields sum c_r = 3^k-3
by induction, lifting the checked conjecture toward a proof.

A_k arrays reproduced by the run's per-residue affine extraction.
"""
A = {
 2: [1,1,1],
 3: [1,3,2,2,1,2,1],
 4: [1,7,4,4,2,4,2,2,1,4,2,2,1,2,1],
 5: [1,15,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
}

# print A_5 with indices
a5 = A[5]
print("A_5 (i:val) len", len(a5))
for i,v in enumerate(a5):
    print(i, v)
