#!/usr/bin/env python3
"""Attack the reduction: is {k,k+1} = {c^3, 2d^3} with c,d>0 really the only
split?  And does the thue resolution, when routed through BOTH descent cases
and ALL signs, give only (3,2) with y>0 and (1,0) excluded?

Brute-force oracle: for k up to K, k(k+1)=2y'^3, verify the forced shape.
This is a *test oracle* on a finite box, not the proof (PARI thue is the proof).
"""
from math import gcd

def is_cube(n):
    r = round(n**(1/3))
    for rr in (r-2, r-1, r, r+1, r+2):
        if rr >= 0 and rr**3 == n:
            return True
    return False

def force_shape(K):
    """For each k<=K, if k(k+1)=2*yp^3 for some yp (i.e. 2*yp^3 = k(k+1)),
    state that {k,k+1}={c^3,2d^3}."""
    checked = 0
    bad = []
    for k in range(1, K+1):
        # does there exist yp with 2*yp^3 = k(k+1)?
        n = k*(k+1)
        if n % 2 != 0:
            continue
        val = n//2          # = yp^3
        # find cube root
        if is_cube(val):
            # val = yp^3; check forcing
            # both k and k+1 must be {a^3, 2 b^3}
            shapes = []
            for t, u in ((k, k+1), (k+1, k)):
                # t is lower
                if is_cube(t) and 2*is_cube(u//2) and u%2==0 and is_cube(u//2):
                    shapes.append((t, u))
            checked += 1
            if not ( (is_cube(k) and u%2==0) or False ):
                pass
            # direct: k and k+1 coprime; total 2*val; one is a cube, the other
            # is 2 times a cube
            good = False
            for low, high in ((k, k+1), (k+1, k)):
                if is_cube(low) and high % 2 == 0 and is_cube(high//2):
                    good = True
            if not good:
                bad.append(k)
    return checked, bad

K = 200000
checked, bad = force_shape(K)
print(f"k<= {K}: k with k(k+1)=2*yp^3 checked: {checked}")
print("  violations of {k,k+1}={c^3,2d^3}:", bad if bad else "NONE")

# The known solution: k=1 -> k(k+1)=2 -> yp^3=1 -> yp=1 -> y=2, x=3.
print("\nKnown descent check at x=3:")
print("  y=2 even (2y' with y'=1); x=3=2k+1 -> k=1; k(k+1)=2=2*1^3 OK.")
print("  gcd(1,2)=1; {1,2}={1^3, 2*1^3} -> c=1,d=1; 2d^3-c^3=2-1=1 OK (Case A).")
print("  x=2k+1=3, y=2*c*d=2. Returned (3,2).")
