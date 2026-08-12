#!/usr/bin/env python3
"""PE 761 hexagon closed form, fully exact with sympy (no floats).

For n=6, theta=pi/6, t=tan(theta)=1/sqrt(3), K=2:
    alpha = 1/2*( K*theta + acos(2*sin(K*theta)/((K+n)*t) - cos(K*theta)) )

We verify, with exact algebra:
  (1) the acos argument == -1/8
  (2) cos(alpha) == (sqrt(21)-3)/8  via half-angle formulas with a=arccos(-1/8)
  (3) V = 1/cos(alpha) == 8/(sqrt(21)-3) == (6+2*sqrt(21))/3, rationalized
  (4) numeric value of (6+2*sqrt(21))/3 to 30 digits and rounding to 8 dp
  (5) K=2 correctness: sin(2t)-(2+n)t*cos(2t)<0 and sin(3t)-(3+n)t*cos(3t)>0
"""
import sympy as sp

theta = sp.pi/6
t = sp.tan(theta)            # = 1/sqrt(3)
K, n = 2, 6

# ---------------------------------------------------------------
# (1) The acos argument equals -1/8
# ---------------------------------------------------------------
arg = 2*sp.sin(K*theta)/((K+n)*t) - sp.cos(K*theta)
arg_exact = sp.simplify(arg)
print("(1) acos argument =", arg_exact, " ; == -1/8 ?",
      sp.simplify(arg_exact - sp.Rational(-1, 8)) == 0)

# ---------------------------------------------------------------
# (2) cos(alpha) via half-angle with a = arccos(-1/8)
# ---------------------------------------------------------------
# alpha = 1/2*(pi/3 + a)  where a = arccos(-1/8)
# Put 2*alpha = pi/3 + a, so alpha = (pi/3 + a)/2.
a = sp.acos(sp.Rational(-1, 8))
alpha = sp.Rational(1, 2)*(K*theta + a)
print("alpha =", sp.simplify(alpha))

# cos(2*alpha) = cos(pi/3 + a) = cos(pi/3)cos(a) - sin(pi/3)sin(a)
# cos a = -1/8, sin a = sqrt(1-1/64) = sqrt(63)/8 = 3sqrt(7)/8
cos2a = sp.cos(sp.pi/3)*sp.Rational(-1, 8) - sp.sin(sp.pi/3)*(3*sp.sqrt(7)/8)
cos2a = sp.simplify(cos2a)
print("cos(2*alpha) =", cos2a, " = -1/16 - 3sqrt(21)/16")

# half-angle: cos(alpha)^2 = (1 + cos(2*alpha))/2  (alpha in (0, pi/2), cos>0)
cos_alpha_sq = (1 + cos2a)/2
# exact: (1 - 1/16 - 3sqrt21/16)/2 = (15 - 3sqrt21)/(32) = 3(5-sqrt21)/32
cos_alpha_sq = sp.simplify(cos_alpha_sq)
print("cos(alpha)^2 =", sp.together(cos_alpha_sq))
print("   == ((sqrt21 - 3)/8)^2 ?",
      sp.simplify(cos_alpha_sq - ((sp.sqrt(21) - 3)/8)**2) == 0)

# Direct: is cos(alpha) == (sqrt21 - 3)/8 ?
cand = (sp.sqrt(21) - 3)/8
print("cos(alpha) == (sqrt21-3)/8 (positive branch, by construction of half-angle)?")
print("   (sqrt21-3)/8 > 0 ?", bool(sp.N(cand) > 0), "; cos(alpha) from squared =",
      sp.sqrt(cos_alpha_sq))
print("   check: sqrt(cos_alpha_sq) - cand == 0 ?",
      sp.simplify(sp.sqrt(sp.simplify(cos_alpha_sq)) - cand) == 0)

# ---------------------------------------------------------------
# (3) V = 1/cos(alpha) = 8/(sqrt21-3) = (6+2sqrt21)/3
# ---------------------------------------------------------------
V1 = 1/cand
V2 = sp.Rational(8, 1)/(sp.sqrt(21) - 3)
V3 = (6 + 2*sp.sqrt(21))/3
print("(3) 1/cos(alpha)    =", sp.radsimp(V1))
print("    8/(sqrt21-3)    =", sp.radsimp(V2))
V3sim = sp.radsimp(V3)
print("    (6+2sqrt21)/3   =", V3sim)
print("    all equal ?",
      sp.simplify(V1 - V2) == 0 and sp.simplify(V2 - V3) == 0)
# rationalize 8/(sqrt21-3): multiply by (sqrt21+3)/(sqrt21+3)
rat = sp.radsimp(V2)
print("    rationalized 8/(sqrt21-3) =", sp.together(rat))
print("    equals (6+2sqrt21)/3 ?",
      sp.simplify(rat - V3) == 0)

# ---------------------------------------------------------------
# (4) numeric value to 30 digits + rounding to 8 dp
# ---------------------------------------------------------------
val = sp.N(V3, 30)
print("(4) (6+2sqrt21)/3 =", val)
val_round = round(float(sp.N(V3, 40)), 8)
print("    rounded to 8 dp =", f"{val_round:.8f}")

# ---------------------------------------------------------------
# (5) verify K=2: f(2)<0, f(3)>0 with f(K)=sin(Kt)-(K+n)*t*cos(Kt)
# ---------------------------------------------------------------
def f(k):
    return sp.simplify(sp.sin(k*theta) - (k + n)*t*sp.cos(k*theta))

f2 = f(2)
f3 = f(3)
print("(5) f(2) =", f2, "  <0 ? ", bool(sp.N(f2) < 0))
print("    f(3) =", f3, "  >0 ? ", bool(sp.N(f3) > 0))
# exact signs
print("    f(2) exact value =", f2, "  (approx", sp.N(f2), ")")
print("    f(3) exact value =", sp.radsimp(f3))
