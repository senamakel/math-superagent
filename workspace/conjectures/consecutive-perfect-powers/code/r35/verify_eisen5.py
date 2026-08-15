"""Verify the Eisenstein 5th-power formula by direct integer tuple arithmetic.

Z[w], w^2 = -1 - w.  alpha = u + v*w.  Formula claimed:
   (u+v*w)^5 = R + S*w with
   R = u^5 - 10 u^3 v^2 + 10 u^2 v^3 - v^5
   S = 5 u^4 v - 10 u^3 v^2 + 5 u v^4 - v^5
Checked against direct integer (non-symbolic) ring powering for many (u,v).
"""
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def mul(a, b):
    r1, s1 = a; r2, s2 = b
    return (r1*r2 - s1*s2, r1*s2 + r2*s1 - s1*s2)  # order verified: see below
def powc(a, n):
    r = (1, 0); b = a
    while n:
        if n & 1: r = mul(r, b)
        b = mul(b, b); n >>= 1
    return r

def formula(u, v):
    R = u**5 - 10*u**3*v**2 + 10*u**2*v**3 - v**5
    S = 5*u**4*v - 10*u**3*v**2 + 5*u*v**4 - v**5
    return (R, S)

ok = True
for u in range(-8, 9):
    for v in range(-8, 9):
        direct = powc((u, v), 5)
        f = formula(u, v)
        if direct != f:
            print(f"MISMATCH u={u} v={v}: direct={direct} formula={f}")
            ok = False
print("all direct==formula:", ok)

# Sanity of ring: w^3 = 1, w^2 = -1-w
print("w^2:", powc((0, 1), 2), " expect (-1,-1)")
print("w^3:", powc((0, 1), 3), " expect (1,0)")
