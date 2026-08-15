#!/usr/bin/env python3
"""Grounding checks for the three live candidate approaches.

Candidate 2 (filtered-complex-spectral-sequence): the load-bearing claim is that
the signed forward-difference operator D, with row k+1 = D(row k) where
D(row)(i) = row(i) - row(i+1), satisfies D^2 = 0 ("it is a cochain complex").
This is the premise for calling the signed triangle a chain complex and running
a spectral sequence on it. Check directly.

Candidate 3 (quiver-cluster-mutation): the load-bearing claim is that the scalar
map (a,b) |-> (|a-b|, b) is the (symmetrized) tropical limit of a rank-2 cluster
mutation x' = (y^m + 1)/x. Check whether any such m reproduces |a-b| for all
a,b and whether cluster-mutation-type relations (rational, Laurent) can express
|a-b|.
"""
from fractions import Fraction

print("=== Candidate 2: is the signed difference operator square-zero? ===")

def D(row):
    """Signed forward difference, length -1."""
    return [row[i] - row[i+1] for i in range(len(row)-1)]

# Try several rows, including the prime gaps scaled / generic.
trials = []
trials.append([2, 3, 5, 7, 11])            # primes
trials.append([0, 1, 2, 3, 4])            # arithmetic
trials.append([7, 11, 13, 17, 19, 23])    # another prime block
trials.append([1, 4, 2, 8, 6])            # arbitrary
for row in trials:
    d1 = D(row)
    d2 = D(d1)
    d3 = D(d2)
    zero2 = all(x == 0 for x in d2)
    zero3 = all(x == 0 for x in d3)
    print(f"row={row}")
    print(f"   D(row)      = {d1}")
    print(f"   D^2(row)    = {d2}  all-zero={zero2}")
    print(f"   D^3(row)    = {d3}  all-zero={zero3}")

# Analytic statement: D = (1 - shift).  D^k applies (1-X)^k to the
# generating function.  D^2 = 0 would need (1-X)^2 = 0, false.
print("\nClaim 'D^2 = 0 because Pascal's matrix is invertible':")
print("  d2 nonzero above already shows D^2 != 0 on generic rows.")
print("  Invertibility of the difference matrix does NOT imply square-zero:")
print("  forget about chain-complex / spectral-sequence framing at D.")


print("\n=== Candidate 1: is the leading-block region an L^nat-convex check? ===")
# The candidate wants the block (longest prefix with |h_i - h_{i+1}| <= 1)
# to be a discrete-Lipschitz / L-convex region.  Quick sanity: L-convex
# functions are submodular + translation-submodular.  We only record that
# the named theory exists; no LA-convex theorem about difference-op dynamics
# is in the literature.  No computation refutes or confirms preservation here.

print("\n=== Candidate 3: does |a-b| satisfy a rank-2 cluster mutation? ===")
# Rank-2 mutation (mutable variable x, co-cluster y):  x*x' = y^m + 1.
# Tropical semifield (log convention): x' = max(m*y, 0) - x  (if sum=max).
# Check against m=1,2.
def trop_mut(x, y, m):
    # multiplicative-log tropical:  ln x' = max(m ln y, 0) - ln x
    from math import log, exp
    return exp(max(m*log(y), 0.0) - log(x))
for m in [1, 2, 3]:
    print(f"m={m}: tropical rank-2 mutation x'=max(m log y,0)-log x")
    for (a, b) in [(5, 3), (3, 5), (4, 4), (7, 2)]:
        v = trop_mut(a, b, m)
        print(f"   (a,b)=({a},{b}) -> x'={v:.3f}   |a-b|={abs(a-b)}")
        if abs(v - abs(a-b)) < 0.01:
            print("        MATCHES |a-b|")
# Conclusion: no m makes the tropical mutation equal |a-b|; it is a
# max/min (range) form, not the cluster Laurent/monomial form.
print("\nNo integer m reproduces |a-b| for all pairs: the tropical mutation is")
print("max(m*log y,0)-log x (a rational-Laurent form); |a-b| = max-min is a")
print("range, not a cluster mutation.")
