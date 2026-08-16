# Verify the k=2 case of Ho's generalized Boppana inequality ties back to the (3-sqrt5)/2 barrier
# Ho 2026 Theorem 1: alpha_k h(x^k) >= x^(k-1) h(x), alpha_k unique positive root of x(1+x)^(k-1)=1.
# For k=2: alpha_2 solves alpha(1+alpha)=1 -> alpha = (sqrt5-1)/2 = 1/phi (golden ratio inverse).
# Then alpha_2/(1+alpha_2) should equal (3-sqrt5)/2, the iid-entropy barrier.
# Also numerically check the inequality h(x^2)*phi >= x h(x) and equality point.

import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
alpha2 = 1 / phi
print("phi        =", sp.nsimplify(phi))
print("alpha2     =", sp.simplify(alpha2), " (should be (sqrt5-1)/2 = 1/phi)")
barrier = alpha2 / (1 + alpha2)
print("alpha2/(1+alpha2) =", sp.simplify(barrier), " (should be (3-sqrt5)/2 =", sp.simplify((3-sp.sqrt(5))/2), ")")
assert sp.simplify(barrier - (3-sp.sqrt(5))/2) == 0
print("tie-back OK: alpha_2/(1+alpha_2) == (3-sqrt5)/2")

# equality point x = 1/(1+alpha2) should be the saturation point of the barrier
x_eq = 1/(1+alpha2)
print("equality point 1/(1+alpha2) =", sp.simplify(x_eq), " should be 1/phi =", sp.simplify(1/phi))
assert sp.simplify(x_eq - 1/phi) == 0
print("equality point OK")

# numeric check of the inequality h(x^2) >= phi*x*h(x) near the saturation point
h = lambda z: -z*sp.log(z) - (1-z)*sp.log(1-z) if z>0 and z<1 else 0
for xt in [sp.Rational(1,100), sp.Rational(1,10), sp.Rational(1,2), x_eq, sp.Rational(99,100)]:
    lhs = h(xt**2)
    rhs = phi*xt*h(xt)
    print(f"x={sp.N(xt,5):>8}  h(x^2)-phi*x*h(x) = {sp.N(lhs-rhs,5):>12}")
print("ALL CHECKS DONE")
