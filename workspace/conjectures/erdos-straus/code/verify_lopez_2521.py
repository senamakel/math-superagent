#!/usr/bin/env python3
"""Verify Lopez 2024's Type B solution for 2521 and basic Type A/B congruence
invariants, against exact arithmetic. 2521 == 1 (mod 840), an open class."""
from fractions import Fraction

def solves(n, x, y, z):
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)

# Lopez Type B solution for p=2521: (638, 55462, 804199) = 11(58, 2*2521, 29*2521)
n = 2521
print("2521 == 1 mod 840:", 2521 % 840 == 1)
sol = (638, 55462, 804199)
print("Lopez Type B (638,55462,804199) solves 4/2521:", solves(n, *sol))
print("factor of 11:", sol[0]/11, sol[1]/11, sol[2]/11)
print("  up=2*2521:", 2*n, " vp=29*2521:", 29*n)

# Type B congruence p == -n (mod 4 d n -1): Lopez says moduli 87 and 1275
for modplus in (87, 1275):
    pass
# 87 = 4*? -1 -> d*n with n: 2521 = -n mod (4dn-1).  4dn-1 = 87 -> 4dn=88 -> dn=22.
# n must satisfy 2521 + n == 0 mod 87.  2521 mod 87: 2521 = 28*87 + 85 = 2436+85=2521. so 2521==85==-2 mod87 -> n=2, dn=22 -> d=11. good.
print("87 = 4*11*2 -1; n=2 check 2521+n=2523, 2523/87=", 2523/87, " integer:", 2523 % 87 == 0)
# 1275 = 4*d*n -1 -> 4dn = 1276 -> dn = 319 = 11*29; n=29, d=11: 2521+29=2550, /1275=2.
print("1275 = 4*11*29-1; n=29 check 2521+29=2550, /1275=", 2550/1275)

# Construct the Type B solution from (d,n)=(11,29): u = (p+n)/(4dn-1)
d, nn = 11, 29
u = (n + nn) // (4*d*nn - 1)
print("u = (p+n)/(4dn-1) =", u, "-> sol (duv, dup, dvp) with v=n=29:",
      (d*u*nn, d*u*n, d*nn*n))
print("matches Lopez:", (d*u*nn, d*u*n, d*nn*n) == (638, 55462, 804199))

# Type A check: p has a Type A solution iff exists t>=0, w | k+1+t, w == -1 mod 3+4t
# p=4k+1 -> k=630.  Type A also equivalent to exists d,n: p == -4d mod (4dn-1).
def has_typeA(k, cap):
    for t in range(0, cap):
        m = 3+4*t
        for w in range(1, k+1+t+1):
            if (k+1+t) % w == 0 and w % m == (m-1):
                return (True, t, w)
    return (False, None, None)

k = (n-1)//4
print("Type A exists (Lopez says NO for 2521):", has_typeA(k, 60))
# sanity: check 193 too (k=48). Lopez says 193 also lacks Type A.
print("193 Type A (should be False):", has_typeA((193-1)//4, 60))
# 66529 should have Type A
print("66529 Type A (should be True):", has_typeA((66529-1)//4, 200))
