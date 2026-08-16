# Sanity check of two identities I am about to write into approach proposals.
# (1) Hasse-derivative tower = Taylor jet:  f(x+t) = sum_i H_i f(x) t^i.
# (2) In A = K[x]/(f), an element g is a zero divisor iff gcd(f, g) != 1.
#     In the squarefree case A = prod_j K[x]/(x-beta_j), and g vanishes at
#     beta_j iff (x - beta_j) divides gcd(f, g).
import sympy as sp

x, t = sp.symbols('x t')

def H(f, i):
    """Hasse derivative H_i f = f^{(i)}/i!  (exact over Q)."""
    return sp.diff(f, x, i) / sp.factorial(i)

# (1) Taylor identity f(x+t) == sum_i H_i f(x) t^i, test n=4..6
for n in [4, 5, 6]:
    a = sp.symbols('a1:'+str(n+1))
    f = x**n + sum(a[k-1]*x**(n-k) for k in range(1, n+1))
    lhs = sp.expand(f.subs(x, x+t))
    rhs = sp.expand(sum(H(f, i)*t**i for i in range(n+1)))
    assert sp.simplify(lhs - rhs) == 0, f"Taylor identity failed at n={n}"
print("(1) Taylor/Hasse identity holds for n=4,5,6")

# (2) zero divisor test on A = K[x]/(f), concrete f = (x-1)^2 (x-2)^3 degree 5
f = sp.expand((x-1)**2 * (x-2)**3)
n = sp.degree(f, x)
# element g with a root at beta=1 (zero divisor) and at no root (unit)
g1 = x - 1          # gcd(f, g1) = x-1  -> zero divisor
g2 = x - 7          # gcd(f, g2) = 1    -> unit
print("gcd(f, x-1) =", sp.gcd(f, g1))
print("gcd(f, x-7) =", sp.gcd(f, g2))

# verify: H_i f is a zero divisor in A  iff  some root beta_j of f has H_i f(beta_j)=0
roots = sp.roots(f, x)
for i in range(1, n):
    Hi = H(f, i)
    vals = [sp.simplify(Hi.subs(x, r)) for r in roots]
    is_zd = sp.gcd(f, Hi) != 1
    has_zero = any(v == 0 for v in vals)
    assert is_zd == has_zero, f"zero-divisor vs root test failed at i={i}"
print("(2) g zero-divisor in A  <=>  g vanishes at some root of f  : verified for f=(x-1)^2(x-2)^3")
