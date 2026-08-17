"""Verify the explicit degree-6 bad-prime witness from Graf von Bothmer et al
2007, Remark 3.2 (research/sources/grafvonbothmer2007_infinitely_many_html.full.md:199).

The quadrinomial  P = X^6 + c4 X^4 + X^3 + c2 X^2  with
    c4 = 3144481702696843
    c2 = 2707944513497181
is a Casas-Alvero polynomial (in the Hasse formulation) over
    F_p,  p = 7390044713023799,
but is NOT a pure power.  This is the paper's explicit witness that CA can hold
over Q while still being false over a specific large characteristic p.

We verify exactly through the canonical oracle lib.casas_alvero:
  - is_ca_hasse(P, p) must be True   (hypothesis holds)
  - is_pure_power(P, p) must be False (not a power of a linear factor)

Guard set (must pass before trusting the produced result):
  - (x-1)^6 over Q is a pure power -> is_ca True, is_pure_power True
  - x^{p+1}-x^p over F_p is a Hasse-CA non-pure-power (the canonical witness)
"""
import sys
from lib.casas_alvero import is_ca, is_ca_hasse, is_pure_power, is_counterexample

p = 7390044713023799
c4 = 3144481702696843
c2 = 2707944513497181

ok = True

# ---- guard set ----
# (x-1)^6 over Q
guard_q = (__import__('sympy').symbols('x') - 1) ** 6
if not (is_ca(guard_q, 0) and is_pure_power(guard_q, 0)):
    print("GUARD FAIL: (x-1)^6 over Q not pure power"); ok = False

# canonical char-p witness x^{p+1}-x^p for a small p, Hasse formulation
from sympy import symbols
x = symbols('x')
small = 5
w = x**(small+1) - x**small
if not (is_ca_hasse(w, small) and not is_pure_power(w, small)):
    print("GUARD FAIL: x^{p+1}-x^p Hasse-CA non-pure-power"); ok = False

# ---- the actual witness ----
P = x**6 + c4*x**4 + x**3 + c2*x**2

ca = is_ca_hasse(P, p)
pp = is_pure_power(P, p)
ce = is_counterexample(P, p)

print(f"p = {p}")
print(f"P = X^6 + {c4} X^4 + X^3 + {c2} X^2")
print(f"is_ca_hasse(P, p)      = {ca}   (expected True)")
print(f"is_pure_power(P, p)    = {pp}   (expected False)")
print(f"is_counterexample(P,p) = {ce}   (expected True)")

# also the ordinary-derivative formulation for contrast
ca_ord = is_ca(P, p)
print(f"[contrast] is_ca (ordinary derivatives) = {ca_ord}")

if not (ca and not pp and ce):
    print("WITNESS CHECK FAILED"); ok = False

# also verify the factors present (paper's proof: X divides low Hasse derivatives,
# X-1-like factor at top) - just report distinct roots
mono = __import__('sympy').Poly(P, x, modulus=p).monic()
_, factors = mono.factor_list()
print("distinct linear/irreducible factors:", len(factors),
      [str(f) for f, _ in factors])

print("ALL CHECKS PASSED" if ok else "FAILED")
sys.exit(0 if ok else 1)
