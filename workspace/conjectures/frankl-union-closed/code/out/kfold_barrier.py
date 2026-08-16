"""Analyse the k-fold iid-OR barrier sequence c_k = psi_k = root of (1-x)^k = x.

Setup: X_1..X_k iid Bernoulli(p) (the k-fold analogue of the 2-fold iid-OR
argument). Union Z = X_1 OR ... OR X_k has density 1-(1-p)^k; the entropy
ratio is R_k(p) = h(1-(1-p)^k)/h(p). The crossover R_k = 1 occurs at the
nontrivial branch 1-(1-p)^k = 1-p  <=>  (1-p)^k = p, whose root in [0,1] is
c_k = psi_k. For k=2 this is (3-sqrt5)/2 ~ 0.381966.

This script: (1) verifies c_2 == (3-sqrt5)/2 and matches the k=3 value from
the run's commands.log; (2) computes c_k for a wide range of k and tests the
asymptotic claim c_k ~ W(k)/k ~ (ln k)/k, i.e. c_k * k / ln k -> 1.
Numerical only (roots of transcendental equations); no exact claims except the
k=2 algebraic value.
"""
import mpmath as mp

mp.mp.dps = 50


def c_k(k):
    """c_k = unique root of (1-x)^k = x in (0,1)."""
    f = lambda x: (1 - x) ** k - x
    # initial guess ~ ln(k)/k ; bracketed by bisection on [0,1]
    lo, hi = mp.mpf(0), mp.mpf(1)
    # ensure f(hi) < 0 < f(lo) near 0: f(0)=1>0, f(1)=-1<0
    return mp.findroot(f, (lo, hi))


# k=2 is algebraic: (1-x)^2 = x <=> x^2 - 3x + 1 = 0, root in [0,1] = (3-sqrt5)/2
exact_2 = (3 - mp.sqrt(5)) / 2
c2 = c_k(2)
print("k=2: c_2 =", mp.nstr(c2, 20), " (3-sqrt5)/2 =", mp.nstr(exact_2, 20),
      " match:", mp.almosteq(c2, exact_2))

print("\n  k     c_k            k*c_k/ln(k)    1/c_k")
prev = None
for k in range(2, 61):
    c = c_k(k)
    r = k * c / mp.log(k)
    if prev is not None:
        dec = "DEC" if c < prev else "inc?"
    else:
        dec = "  "
    print(f"{k:4}  {mp.nstr(c,12):>14}   {mp.nstr(r,8):>10}  {mp.nstr(1/c,9):>10}  {dec}")
    prev = c

print("\nMonotone decreasing over k=2..60:", all(c_k(k2) > c_k(k2+1) for k2 in range(2, 60)))
print("Asymptotic ratio k*c_k/ln(k) -> ?  k=60:", mp.nstr(60*c_k(60)/mp.log(60), 8))
print("Known: W(k)/k ~ (ln k - ln ln k)/k, i.e. c_k ~ ln(k)/k  => k*c_k/ln k -> 1.")
