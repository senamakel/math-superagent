"""Exact symbolic verification of Boppana's binary-entropy inequality,
second pass: monotonicity structure + attempted factorization (avoiding the
giant-integer blowup by evaluating logs pointwise at high precision).
"""
import sympy as sp

t = sp.Symbol('t', real=True, nonnegative=True)
phi = (1 + sp.sqrt(5)) / 2

def h_nats(x):
    return -x * sp.log(x) - (1 - x) * sp.log(1 - x)

Dnat = sp.simplify(h_nats(t**2) - phi * t * h_nats(t))   # difference in nats
print("D in nats expanded:")
print(sp.expand(Dnat))
print("\ncollected:")
print(sp.collect(sp.expand(Dnat), [sp.log(t), sp.log(1-t), sp.log(1+t)]))

# --- exact evaluation over a fine grid, high-precision per point ---
print("\n=== grid check D(t) >= 0 (high precision, no .simplify) ===")
from fractions import Fraction
grid = [Fraction(k, 200) for k in range(1, 200)]
minv, argmin = None, None
for g in grid:
    v = float(sp.N(Dnat.subs(t, g), 40))
    if minv is None or v < minv:
        minv, argmin = v, g
print(f"min over k/200 grid: D({argmin}) = {minv:.15f}  (t0={float(1/phi):.6f})")
print("-> strictly >= 0 on every grid point? ",
      all(float(sp.N(Dnat.subs(t, g), 40)) >= -1e-28 for g in grid))

# --- derivative / monotonicity: is t0 the unique interior zero & minimizer? ---
Dp = sp.diff(Dnat, t)
print("\n=== derivative structure ===")
probes = ["1/10","1/4","2/5","9/20","1/2","11/20","3/5","3/4","9/10"]
for p in probes:
    val = float(sp.N(Dp.subs(t, sp.Rational(p)), 40))
    print(f"  D'({p}) = {val:+.6e}")

# t0 exactly
print("  D'(t0) =", float(sp.N(Dp.subs(t, 1/phi), 40)))

# --- The clean structural factorization: substitute the exact root identity ---
# t0^2 + t0 = 1 is what makes lhs == rhs at t0. Show exactly that the equality
# holds by the chain: t0^2 = 1 - t0, h symmetric, phi*t0 = 1.
print("\n=== exact equality chain at t0 (already proven above); reconfirm in nats ===")
t0 = 1/phi
diff_at = sp.simplify(h_nats(t0**2) - phi * t0 * h_nats(t0))
print("h(t0^2) - phi*t0*h(t0) in nats =", diff_at, "-> zero?", diff_at == 0)
print("(3-sqrt5)/2 - 1/phi^2 =", sp.simplify((3-sp.sqrt(5))/2 - 1/phi**2))
print("phi*(3-sqrt5)/2 ... exact links: phi - 2 = sqrt5-3+1 ... check 1/phi^2+1/phi:")
print("1/phi^2 + 1/phi =", sp.simplify(1/phi**2 + 1/phi), "  (should be 1)")
