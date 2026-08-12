#!/usr/bin/env python3
"""Verify the hexagon answer and closed forms with sympy (exact algebraic where possible)."""
import sympy as sp

def critical_speed(n, dps=30):
    theta = sp.pi / n
    tan_th = sp.tan(theta)
    K = None
    for k in range(0, n + 1):
        val = sp.sin(k * theta) - (k + n) * tan_th * sp.cos(k * theta)
        if val < 0:
            K = k
    inner = 2 * sp.sin(K * theta) / ((K + n) * tan_th) - sp.cos(K * theta)
    inner = sp.Max(sp.Min(inner, 1), -1)
    alpha = sp.Rational(1, 2) * (K * theta + sp.acos(inner))
    lam = 1 / sp.cos(alpha)
    return K, alpha, lam

# Hexagon at high precision
K, alpha, lam = critical_speed(6)
print("n=6: K=", K, " alpha=", alpha.evalf(30), " V=", lam.evalf(30))
print("n=6 V rounded 8dp:", round(float(lam.evalf(20)), 8))

# Closed forms for triangle and square (from Abel et al.)
import math
V3_form = (3 + math.sqrt(5)) * math.sqrt(2)
V4_form = math.sqrt(2.5 * (7 + math.sqrt(41)))
K3, a3, l3 = critical_speed(3)
K4, a4, l4 = critical_speed(4)
print("\ntriangle: formula=(3+sqrt5)*sqrt2=%.10f  computed=%.10f  diff=%.2e" %
      (V3_form, float(l3.evalf(16)), abs(V3_form - float(l3.evalf(16)))))
print("square: formula=sqrt(5/2(7+sqrt41))=%.10f  computed=%.10f  diff=%.2e" %
      (V4_form, float(l4.evalf(16)), abs(V4_form - float(l4.evalf(16)))))

# Circle limit
lam10000 = critical_speed(10000)
print("\nn=10000 V=%.8f (circle oracle 4.60333885)" % float(lam10000[2].evalf(12)))

# High-precision hexagon for answer
print("\nHEXAGON ANSWER to 8 dp:", f"{float(lam.evalf(20)):.8f}")
