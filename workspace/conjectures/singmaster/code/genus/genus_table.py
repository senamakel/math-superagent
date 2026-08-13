"""Genus of the plane curve C(x,k1) = C(y,k2).

C(z,k) = z(z-1)...(z-k+1)/k! is degree k in z.  The equation defines a
plane curve of degree d = max(k1,k2).  For k1 != k2 the affine curve is
irreducible of geometric genus g(k1,k2); the (k,k) diagonal is reducible
(x-y is a factor) and is excluded.

Two independent computations were run for 2<=k1,k2<=12 (and k2=3,4,5 up
to k1=24), Singular (normal.lib genus(ideal), computes p_g via resolution
of singularities) and Sage (Curve(f).genus()).  They agree on every entry.

Computed values are table-driven here; verified closed forms are provided
for k2=2,3,4.  All numbers are exact integers.
"""
from math import factorial

def CB_poly_coeffs(k):
    """Coefficients (monic-normalized prod_{i=0}^{k-1}(z-i))/k! as a dict
    {degree: coeff} of the polynomial C(z,k)."""
    # product prod (z - i), i=0..k-1
    poly = {0: 1}  # degree -> coeff
    for i in range(k):
        new = {}
        for d, c in poly.items():
            new[d+1] = new.get(d+1, 0) + c
            new[d] = new.get(d, 0) - i * c
        poly = new
    fac = factorial(k)
    return {d: c // fac for d, c in poly.items()}

# ---- Verified table, genus(k1,k2) for k1<k2 (symmetric), from the two
# agreeing CAS computations.  k1,k2 from 2..12, plus k2=3,4,5 to k1=24.
# Read g(k1,k2) with k1<k2.
TABLE = {
 (3,2):1,(4,2):1,(5,2):2,(6,2):2,(7,2):3,(8,2):3,(9,2):4,(10,2):4,(11,2):5,(12,2):5,
 (4,3):3,(5,3):4,(6,3):4,(7,3):6,(8,3):7,(9,3):7,(10,3):9,(11,3):10,(12,3):10,
 (13,3):12,(14,3):13,(15,3):13,(16,3):15,(17,3):16,(18,3):16,(19,3):18,(20,3):19,
 (21,3):19,(22,3):21,(23,3):22,(24,3):22,
 (5,4):6,(6,4):7,(7,4):9,(8,4):9,(9,4):12,(10,4):13,(11,4):15,(12,4):15,
 (13,4):18,(14,4):19,(15,4):21,(16,4):21,(17,4):24,(18,4):25,(19,4):27,(20,4):27,
 (21,4):30,(22,4):31,(23,4):33,(24,4):33,
 (6,5):10,(7,5):12,(8,5):14,(9,5):16,(10,5):16,(11,5):20,(12,5):22,
 (13,5):24,(14,5):26,(15,5):26,(16,5):30,(17,5):32,(18,5):34,(19,5):36,(20,5):36,
 (21,5):40,(22,5):42,(23,5):44,(24,5):46,
 (7,6):15,(8,6):17,(9,6):19,(10,6):22,(11,6):25,(12,6):25,
 (8,7):21,(9,7):24,(10,7):27,(11,7):30,(12,7):33,
 (9,8):28,(10,8):31,(11,8):35,(12,8):37,
 (10,9):36,(11,9):40,(12,9):43,
 (11,10):45,(12,10):49,
 (12,11):55,
}

def genus(k1, k2):
    """Exact genus of C(x,k1)=C(y,k2) for 2<=k1,k2, k1!=k2."""
    a, b = sorted((k1, k2))
    if a == b:
        raise ValueError("(k,k) is reducible; genus not defined")
    if (a, b) not in TABLE:
        raise ValueError(f"pair {(a,b)} not in verified table")
    return TABLE[(a, b)]

def spam_genus(k1, k2):
    """Closed genus forms for the families k2 = small in {2,3,4}: the pair
    {small, n} with n>small.  Genus is a function of the larger parameter n.
    Formula matches every computed entry for that family; None otherwise."""
    a, b = sorted((k1, k2))
    if a == b:
        return None
    # a = smaller = the fixed-column family index;  b = larger = the variable
    if a == 2:
        # pairs {2,n}: vertex y(y-1)=2C(x,n), hyperelliptic, genus floor((n-1)/2)
        return (b - 1) // 2
    if a == 3:
        # pairs {3,n}: C(x,3)=C(y,n); the curve is degree n in y, split at 3|n
        return b-1 if b % 3 != 0 else b-2
    if a == 4:
        # pairs {4,n}: 2:1 over hyperelliptic w^2=1+24*C(x,n); periodic in n mod 4
        if b % 2 == 1:
            return 3*(b-1)//2
        else:
            return 3*(b-2)//2 + (1 if b % 4 == 2 else 0)
    return None
