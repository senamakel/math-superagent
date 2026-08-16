#!/usr/bin/env python3
"""Analyse the K*-witness separating functional: what does S^2 actually see at
order K that C_1..C_K does not pin down? Find, for the n=8 witness pair (and
general n), the exact monomials of S^2 that differ between same-fibre strings.

S(n)^2 = sum_{d,d' in [2,n-1]} prod_{j in M_d △ M_{d'}} x_j, x_j=(-1)^{h_j}.
Two strings in the same C_1..C_K fibre differ in S^2 iff some symmetric-
difference product (monomial) differs between them, i.e. iff some M_d△M_{d'}
is not a union of (K+1)-grams determined by the histogram.

Here we compute for n=8 the witness pair h=00000010 (bit6), h'=00000100 (bit5)
and list, term by term in the double sum, which (d,d') monomials differ.
"""
import itertools, sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def row_masks(n):
    # M_d for d in [2,n-1], as n-bit masks (positions 0..n-1)
    masks = {}
    for d in range(2, n):
        m = 0
        for o in range(1 << d):
            if o & d == o:  # o submask of d
                pos = n - 1 - d + o
                m |= 1 << pos
        masks[d] = m
    return masks

def monomial_value(mask, h):
    """prod_{j in mask} x_j = prod (-1)^{h_j}."""
    v = 1
    for j in range(len(h)):
        if mask >> j & 1:
            v *= -1 if h[j] else 1
    return v

n = 8
masks = row_masks(n)
h = [0,0,0,0,0,0,1,0]   # bit 6
hp = [0,0,0,0,0,1,0,0]  # bit 5

print("n=8, h=00000010, h'=00000100")
print("row masks M_d:")
for d in sorted(masks):
    print("  d=%d M_d=%s" % (d, bin(masks[d])[2:].zfill(n)))

# Compute S^2 term by term
def S2_term_wise(hh):
    acc = 0
    for d1 in sorted(masks):
        for d2 in sorted(masks):
            A = masks[d1] ^ masks[d2]
            acc += monomial_value(A, hh)
    return acc

print()
print("S^2 by monomial sum: h->%d, h'->%d (should be 0 and 4)" %
      (S2_term_wise(h), S2_term_wise(hp)))

# Which monomials (d,d') differ between h and h'?
print()
print("monomials (d1,d2) whose product differs between h and h':")
diff = 0
for d1 in sorted(masks):
    for d2 in sorted(masks):
        A = masks[d1] ^ masks[d2]
        vh = monomial_value(A, h)
        vhp = monomial_value(A, hp)
        if vh != vhp:
            diff += 1
            # print the index set
            idx = [j for j in range(n) if A >> j & 1]
            print("  (d1=%d,d2=%d) A=%s idx=%s  prod_h=%+d prod_h'=%+d" %
                  (d1, d2, bin(A)[2:].zfill(n), idx, vh, vhp))
print("total differing monomial count:", diff)

# Now: which (d,d') have M_d△M_d' NOT determined by C_1 histograms?
# A monomial product differs iff the index set of A contains exactly one of
# {5} or {6}? Let's check: h has 1 at 6 only, h' has 1 at 5 only. Product
# differs iff A contains 6 XOR-iff... product over A of x_j. h: x_6=-1 others +1.
# So prod_h(A) = (-1)^{[6 in A]}; prod_h'(A)=(-1)^{[5 in A]}. Different iff
# [6 in A] != [5 in A], i.e. A contains exactly one of {5,6}.
print()
print("those differing are exactly the A with |A∩{5,6}|=1 (one of the two bits):")
bad = 0
for d1 in sorted(masks):
    for d2 in sorted(masks):
        A = masks[d1] ^ masks[d2]
        if ((A>>5)&1) != ((A>>6)&1):
            bad += 1
print("  count:", bad, "(== %d differing monomials above)" % diff)

# What is the widest such A (max index span) that separates them?
print()
maxspan = 0; arg = None
for d1 in sorted(masks):
    for d2 in sorted(masks):
        A = masks[d1] ^ masks[d2]
        if ((A>>5)&1) != ((A>>6)&1):
            lo = (A & -A).bit_length()-1
            hi = A.bit_length()-1
            span = hi - lo + 1
            if span > maxspan:
                maxspan = span; arg = (d1,d2)
print("max index-span among separating monomials:", maxspan, "at (d1,d2)=", arg)
