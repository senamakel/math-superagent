"""Reconstruct the Category VII magic square from Bremner II's parametrization
at (lam,p,q)=(13,9,2), and identify which grid entry the quartic (12) square
root 12682 corresponds to.

Category VII:  +-b+c = S, +-(a-b)+c = S, -a+c = S, c = S.
c = m^2+n^2 = r^2+s^2 = u^2, b = 2mn, a-b = 2rs, a = u^2 - v^2.
m = a'b'+gd, n = a'g - b'd, r = a'g + b'd, s = a'b' - gd   (paper calls a' -> alpha)
With g=1 -> b' = lam.
First eq of (11): alpha:delta:rho = lam(p^2-q^2)+2pq : (p^2-q^2)-2lam pq : (lam^2+1)(p^2+q^2)
"""
import math

lam, p, q = 13, 9, 2
g = 1
b = lam  # beta

alpha = lam*(p*p - q*q) + 2*p*q
delta = (p*p - q*q) - 2*lam*p*q
rho_free = (lam**2+1)*(p*p+q*q)  # rho = u/gamma (gamma=1)

print("alpha =", alpha, " delta =", delta, " rho(=u) =", rho_free)

# second eq of (11):  alpha^2(1-4l+l^2) + delta^2(1+4l+l^2) = sigma^2
sigma2 = alpha**2*(1-4*lam+lam**2) + delta**2*(1+4*lam+lam**2)
print("sigma^2 =", sigma2, " sigma =", math.isqrt(sigma2), " sqrt^2 ==", math.isqrt(sigma2)**2 == sigma2)

m = alpha*b + g*delta
n = alpha*g - b*delta
r = alpha*g + b*delta
s = alpha*b - g*delta
print("m,n,r,s =", m, n, r, s)
print("m^2+n^2 =", m*m+n*n, " r^2+s^2 =", r*r+s*s, " u^2 =", rho_free**2)

u = rho_free
c = u*u
bpar = 2*m*n
apart = 2*r*s
a = 2*r*s + 2*m*n
v2 = u*u - a
print("a =", a, "  b =", bpar, "  c =", c)
print("v^2 =", v2, " v =", math.isqrt(v2))

# grid from standard form:
# [a+c  -a-b+c  b+c
#  -a+b+c  c  a-b+c
#  -b+c  a+b+c  -a+c]
grid = [[a+c, -a-bpar+c, bpar+c],
        [-a+bpar+c, c, a-bpar+c],
        [-bpar+c, a+bpar+c, -a+c]]
def issq(x):
    if x < 0: return "neg"
    t = math.isqrt(x)
    return t if t*t == x else None
print("\nUnscaled grid + square-roots (None = not square):")
for row in grid:
    rws = [issq(x) for x in row]
    print(row, "->", rws)

print("\nGrid / 34^2 (scaled by 1156):")
for row in grid:
    print([x//1156 for x in row])
