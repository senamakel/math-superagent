"""Verify numeric claims used in the scholar digest of the four new sources.

1. Six open residues {1,121,169,289,361,529} are all quadratic residues mod 840
   (1^2, 11^2, 13^2, 17^2, 19^2, 23^2).
2. c0 = lim u_n^{2^-n}, u_0=1, u_{n+1}=u_n(u_n+1) reproduces the
   four-unit-fractions source's c0 = 1.5979102...
"""
def quad_residues(mod):
    return {(a*a) % mod for a in range(mod)}

residues = [1,121,169,289,361,529]
qr840 = quad_residues(840)
print("QR mod 840 contains all six open residues:", all(r in qr840 for r in residues))
print("841 = 29^2 odd square in class 1 mod 840:", (29*29) % 840)

u = 1
seq = [u]
for _ in range(10):
    u = u*(u+1)
    seq.append(u)
print("u_n (A007018) first 6:", seq[:6])
est = seq[-1]**(1/2**10)
print("c0 estimate from u_10:", repr(est))
