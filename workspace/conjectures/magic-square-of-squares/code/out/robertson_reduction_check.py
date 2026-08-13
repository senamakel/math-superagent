#!/usr/bin/env python3
"""Verify the Robertson/Bremner elliptic reduction on Bremner's 7-square witness.

Checks, in exact integer arithmetic:
  1. Bremner's parametrisation (2): every 3x3 magic square of rationals has the form
       a-b   a+b+c   a-c
       a+b-c  a     a-b+c
       a+c   a-b-c   a+b
     For the 7-square witness we recover (a,b,c) from the grid.
  2. E: y^2 = x(x^2-c^2); a point (X,Y) in 2E(Q)  <=>  {X, X-c, X+c} all rational squares.
  3. Doubling x-coordinate: x(2P) = (x^2+c^2)^2/(4y^2) on this curve.
  4. Which candidate x-coords a-b, a, a+b are x-coords of points in 2E(Q) for c.
"""
import math

def is_sq(n):
    if n < 0: return None
    r = math.isqrt(n)
    return r if r*r == n else None

# Bremner 7-square witness grid
grid = [[373**2, 289**2, 565**2],
        [360721, 425**2, 23**2],
        [205**2, 527**2, 222121]]
print("grid =")
for r in grid: print("  ", r)

# 1. Recover (a,b,c) from the parametrisation:
# center a = grid[1][1]; main diag {a-b, a, a+b} -> a-b = grid[0][0]
a = grid[1][1]
amb = grid[0][0]   # a-b
apb = grid[2][2]   # a+b
b = a - amb
print("a =", a, " b =", b, " a-b =", amb, " a+b =", apb)
assert apb == a + b
# anti-diagonal {a-c, a, a+c}: grid[2][0]=a+c? check: grid[2][0]=205^2, grid[0][2]=565^2
amc = grid[1][1]-grid[2][0] if False else None
# anti-diag entries: (0,2)=565^2, (1,1)=a, (2,0)=205^2
amc_lo = grid[2][0]  # a-c
apc_hi = grid[0][2]  # a+c
c = a - amc_lo
print("c (anti-diag diff) =", c, " a-c =", amc_lo, " a+c =", apc_hi)
assert apc_hi == a + c

# 2. The three candidate x-coords of points in 2E(Q): the main-diagonal AP {a-b, a, a+b}
for X in (amb, a, apb):
    Xmc = X - c
    Xpc = X + c
    sq = (is_sq(X), is_sq(Xmc), is_sq(Xpc))
    print(f"X={X}: X={X}^{sq[0] and is_sq(X)}  X-c={Xmc}->{sq[1]}  X+c={Xpc}->{sq[2]}  in2E={all(s is not None for s in sq)}")

# 3. doubling formula check on the curve: pick a rational point and verify x(2P)=(x^2+c^2)^2/4y^2
# We need a rational point. Use the fact x=373^2, x-c=23^2, x+c=527^2 gives y^2=x(x^2-c^2)
X0 = amb  # 373^2; X0-c=23^2, X0+c=527^2 all squares
import fractions as F
# y = sqrt(X*(X-c)*(X+c))
y0 = math.isqrt(amb*(amb-c)*(amb+c))
print("candidate rational point on E:", (amb, y0), "check y^2=x(x^2-c^2):",
      y0*y0 == amb*(amb*amb - c*c))
# doubling x by formula (x^2+c^2)^2/(4y^2):
num = (amb*amb + c*c)**2
den = 4*y0*y0
print("x(2P) formula =", num, "/", den, "=", F.Fraction(num, den))

# 4. Which of the four centre-line AP differences have BOTH endpoints + centre square?
print("\nfour centre line families through a=", a, " c=", c)
# differences of the four APs through centre: b, c, b-c, b+c (from parametrisation)
for d in sorted(set([b, c, abs(b-c), b+c])):
    lo = a - d; hi = a + d
    flags = (is_sq(lo) is not None, is_sq(a) is not None, is_sq(hi) is not None)
    print(f"  d={d}: a-d={lo}->{flags[0]}, a->{flags[1]}, a+d={hi}->{flags[2]}  both-ends-square={flags[0] and flags[2]}")
