#!/usr/bin/env python3
"""Structural probe of the quadratic-complement pattern in the Bautin
monomial counts.

Question being attacked:  a_d = (dim(h) - c(h))/2  with h=d-2 and
c(h) = (h^2 + 14 h + 8)/8 for even h >= 4.  We have shown this equals
"half the monomials minus a quadratic correction".  A standard reason a
coefficient set of a polynomial is exactly half the monomials is that the
polynomial is ODD under an order-2 sign/permutation symmetry of the
variables, pairing each monomial with its image and forcing zero on the
fixed monomials.  If that were true, c(h) would equal the number of
sigma-fixed monomials of degree h for ONE permutation sigma, for all h.

We test: does there exist ANY permutation-and-signing involution sigma on
the 5 coefficient variables (A,C,D,E,F) that makes L_d odd (L_d(sigma x) =
-L_d(x))?  Effectively the fixed-monomial counts c(h) must come from a
single consistent involution.  We compute the fixed-monomial count function
of every permutation involution and compare against c(h) = 7,10,16,23,31,40,50.

Exact sympy rational arithmetic only.
"""
import itertools
import sympy as sp

# c(h) for h = 2,4,6,8,10,12,14 (d = 4..16)
c = {2: 7, 4: 10, 6: 16, 8: 23, 10: 31, 12: 40, 14: 50}
vars_ = ["A", "C", "D", "E", "F"]
n = 5


def fixed_count(perm, h):
    """Number of degree-h monomials fixed by the permutation perm of indices."""
    # monomial exponents e[0..4], sum e = h; fixed iff e == permuted
    count = 0
    perms_apply = perm
    for e in itertools.product(range(h + 1), repeat=4):
        s = sum(e)
        if s > h:
            continue
        e5 = h - s
        efull = e + (e5,)
        mapped = tuple(efull[perms_apply[i]] for i in range(n))
        if mapped == efull:
            count += 1
    return count


def all_involutions():
    """All permutations of 5 elements that are involutions (sigma^2 = id),
    as tuples sigma with new_index = perm[old_index] meaning variable i moves
    to position perm[i]."""
    out = []
    for perm in itertools.permutations(range(n)):
        if all(perm[perm[i]] == i for i in range(n)):
            out.append(perm)
    return out


print("== Each permutation-involution's fixed-degree-h monomial count, h=2,4,6,8 ==")
print("target c(h) =", [c[h] for h in (2, 4, 6, 8)])
invol = all_involutions()
print("number of permutation involutions on 5 letters:", len(invol))
hit = False
for perm in invol:
    counts = tuple(fixed_count(perm, h) for h in (2, 4, 6, 8))
    target = tuple(c[h] for h in (2, 4, 6, 8))
    if counts[:3] == target[:3]:
        hit = True
        print("  MATCH candidate perm", perm, "counts", counts)
if not hit:
    print("NO permutation involution reproduces the fixed counts (7,10,16,23...):")
    print("  c(h) is NOT the fixed-monomial-count of a single variable permutation,")
    print("  so a simple oddness (sign-permutation) symmetry does NOT explain a_d.")
    print("  Sequence of permutation-fixed counts for h=4:", 
          sorted({fixed_count(p, 4) for p in invol}))
    print("  (observed c(4) = 10 must be among these for a pairing explanation;",
          "check if 10 is present ->", 9 in {fixed_count(p, 4) for p in invol} or 10 in {fixed_count(p,4) for p in invol})
