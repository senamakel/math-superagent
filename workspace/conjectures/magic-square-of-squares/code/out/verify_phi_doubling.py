"""Verify the identity Phi = Im(w^2) for w on the norm-one torus of Q(i).

Run's established Phi: f(m,n) = 4mn(m^2-n^2)/(m^2+n^2)^2.
Claim: f(m,n) = Im(w(t)^2) where w(t) = (1-t^2 + 2ti)/(1+t^2) and t = n/m.
"""
from sympy import symbols, simplify, expand, I, Rational

m, n, t = symbols('m n t', real=True)

# w(t) is a norm-one Gaussian rational (rational point on unit circle)
w = (1 - t**2 + 2*I*t) / (1 + t**2)

# Im(w^2) symbolically
w2 = simplify(w**2)
im_w2 = simplify(w2.as_real_imag()[1])
g_t = simplify(expand(im_w2))
print("Im(w(t)^2) =", simplify(g_t))

# substitute t = n/m and compare with f(m,n)
g_nm = simplify(g_t.subs(t, n/m))
f = 4*m*n*(m**2 - n**2) / (m**2 + n**2)**2
diff = simplify(g_nm - f)
print("Im(w(n/m)^2) - f(m,n) =", diff)
assert simplify(diff) == 0, "IDENTITY FAILED"

# numeric check on Bremner's realised differences
# q_v = 5544/7225 in Phi via (m,n)=(9,2) [e=425=5*(81+4)]
for (mm, nn) in [(9, 2), (4, 3)]:
    val = 4*mm*nn*(mm**2 - nn**2)/(mm**2 + nn**2)**2
    tt = Rational(nn, mm)
    gt = simplify(g_t.subs(t, tt))
    print(f"(m,n)=({mm},{nn}): f={val}, Im(w^2)={gt}, equal={val==gt}")

print("IDENTITY VERIFIED")
