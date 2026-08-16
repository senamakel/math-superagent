#!/usr/bin/env python3
"""Check the crux of candidate 2 (gowers-u2-nilsequence-uniformity).

Candidate 2 claims: S(n) = sum_d <s, chi_{down d}> is "the sum of the degree-1
Fourier (Walsh) coefficients of s", so S(n)=o(n) is U^2-uniformity.

The U^2 norm / Gowers inverse theorem / Green-Tao nilsequence orthogonality all
live on the WALSH/Fourier basis chi_S(x)=(-1)^{<S,x>}.  The fold reads the
DOWN-SET indicator basis 1_{down d} = {x : x subset-of d}.  These are different
bases (the down-set basis is the zeta/Mobius/ANF basis, one is the Mobius
transform of the other).  We demonstrate on a small Boolean cube.
"""
import itertools

def downset_indicator(d, x):
    # x subset-of d
    return 1 if (x & d) == x else 0

def walsh_character(S, x):
    # (-1)^{<S,x>} = product over common bits
    return 1 if bin(S & x).count('1') % 2 == 0 else -1

m = 3
full = list(range(1 << m))  # 0..7 as subsets of {0,1,2}

# Build the down-set indicator matrix (rows indexed by d, cols by x)
# and the Walsh character matrix (rows indexed by S, cols by x)
down = [[downset_indicator(d, x) for x in full] for d in full]
walsh = [[walsh_character(S, x) for x in full] for S in full]

print("down-set indicator matrix rows (d=0..7) -- 0/1 valued, ragged")
for r in down:
    print(" ".join(str(v) for v in r))

print("\nWalsh character matrix rows (S=0..7) -- +/-1 valued")
for r in walsh:
    print(" ".join(("+" if v>0 else "-") for v in r))

# Are they the same basis? The Walsh rows are the characters. Check:
# is every down-set row equal to some Walsh row (i.e. to a character)?
from itertools import permutations
def rows_equal(a,b): return all(x==y for x,y in zip(a,b))
match = [False]*len(full)
for di, drows in enumerate(down):
    for wi, wrows in enumerate(walsh):
        if rows_equal(drows,wrows): match[di]=True
print("\nNumber of down-set rows that equal a Walsh character row:", sum(match), "of", len(full))

# The real point: is the down-set sum of a vector a Fourier (Walsh) sum?
# Take a generic test vector x (e.g. the all-ones, and a random one)
import random
def vector_fold_sum(x):
    # sum_d (-1)^{ XOR_{y in down d} x[y] }  -- this is what S(n) is (a Mobius/ANF fold)
    total=0.0
    for d in full:
        par=0
        for y in full:
            if downset_indicator(d,y): par ^= x[y]
        total += (-1)**int(par)
    return total

def vector_fourier_sum_U2(x):
    # sum of (Walsh coeff)^4 style / or sum of Walsh coeffs -- the U^2 expression
    # U^2 norm^4 = sum_S |<x,chi_S>|^4.  More to the point, the fold is over AND-sums.
    return sum(abs(sum(x[y]*walsh[S][y] for y in full))**4 for S in full)

for x in [ [1,0,1,0,1,0,1,0],  # even-alt-ish
           [1,1,1,1,1,1,1,1],  # all-ones (kernel-ish)
           [1,0,0,1,1,0,1,0],  # generic
         ]:
    print("\nx=",x)
    print("  fold (down-set Möbius) sum =", vector_fold_sum(x))
    print("  U^2 style (Walsh |coeff|^4) sum =", vector_fourier_sum_U2(x))
