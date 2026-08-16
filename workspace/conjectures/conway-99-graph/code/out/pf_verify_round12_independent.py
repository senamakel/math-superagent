"""Independent re-derivation of round-12's tight-coclique family identities."""
import sympy as sp

u = sp.symbols('u', integer=True, positive=True)
k = u**2 + u + 2
v = 1 + k**2 / 2            # symbolic rational expression, exact in Q(u)
s = -(u+1)

alpha = sp.simplify(v * (-s) / (k - s))
dC = sp.simplify(alpha * (k - s) / v)

print("k        =", sp.factor(k))
print("v        =", sp.factor(v))
print("alpha    =", sp.factor(alpha))
print("d_C      =", sp.factor(dC), "   d_C - (-s) =", sp.factor(dC - (-s)))
print("alpha*k/v =", sp.factor(alpha * k / v))

vp, kp, lam = alpha, dC, 2
b = sp.simplify(v - vp)
r = sp.simplify(lam * (vp - 1) / (kp - 1))
print("b        =", sp.factor(b))
print("r        =", sp.factor(r), "   r - k =", sp.factor(r - k))
print("b*k' - v'*r =", sp.factor(b*kp - vp*r))
print("b*C(k',2) - lam*C(v',2) =", sp.factor(b*kp*(kp-1)/2 - lam*vp*(vp-1)/2))

print("\n--- exact integer table over the five feasible members ---")
for uu in (1,3,4,10,31):
    kk = uu*uu+uu+2
    vv = 1 + kk*kk//2
    ss = -(uu+1)
    al = sp.Rational(vv*(-ss), kk-ss)
    dc = sp.simplify(sp.Rational(al*(kk-ss), vv))
    bb = vv - al
    rr = sp.simplify(sp.Rational(2*(al-1), dc-1))
    print(f"u={uu:>2} k={kk:>4} v={vv:>7} s={ss:>3} alpha={al} dC={dc} b={bb} r={rr}  dC==-s:{dc==-ss}  r==k:{rr==kk}")
