"""Validate the relative class number formula h^-(Q(zeta_p)) = 2p * prod_{chi odd} (-1/2 B_{1,chi}).

B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) * a   (primitive odd chi mod p).

The quotient field is Q(zeta_{p-1}); the product over the (p-1)/2 odd characters
is a real algebraic number, and 2p * prod is exactly the integer h^-. Here we
evaluate each character value exp(2*pi*i*k*e/(p-1)) with high precision using
mpmath and round the (exactly-integer) result, checking against known values:

  p=3  -> 1
  p=5  -> 1
  p=7  -> 1
  p=11 -> 1
  p=13 -> 1
  p=23 -> 3
  p=31 -> 9
  p=37 -> 37

No sympy.Float (whose missing .real broke the previous version) and no
field-simplification explosion: high-precision evaluation + rounding to the
small known integer is exact in effect for these sizes, and the answers are
known in advance so a checkpoint is a genuine check, not a guess.
"""
import mpmath as mp

mp.mp.dps = 60  # plenty: h^- is a small integer, product is a sum of roots of unity

def primitive_root(p):
    for g in range(2, p):
        if pow(g, (p-1)//2, p) != 1:
            return g

def odd_k(p):
    return list(range(1, p-1, 2))

def rel_class_number(p):
    """Return h^- as a float rounded from high-precision evaluation."""
    g = primitive_root(p)
    logtab = {}
    val = 1
    for e in range(p-1):
        logtab[val] = e
        val = (val*g) % p
    prod = mp.mpf(1)
    for k in odd_k(p):
        s = mp.mpc(0)
        for a in range(1, p):
            e = logtab[a]
            s += mp.e**(mp.mpc(0, 2)*mp.pi*k*e/(p-1)) * a
        B1 = s / p
        prod = prod * (mp.mpf(-1)/2 * B1)
    h = 2*p*prod
    return h.real, h.imag

KNOWN = {3:1, 5:1, 7:1, 11:1, 13:1, 23:3, 31:9, 37:37}
PRIMES = [3,5,7,11,13,23,31,37]

all_match = True
for p in PRIMES:
    real, imag = rel_class_number(p)
    rounded = round(real.real if hasattr(real,'real') else real)
    ok = abs(real - rounded) < 1e-6 and abs(imag) < 1e-6 and rounded == KNOWN[p]
    if not ok:
        all_match = False
    print(f"p={p:3d}  h^- = {rounded}  (real={mp.nstr(real,6):>12} imag={mp.nstr(imag,6):>10})  expected {KNOWN[p]}  {'OK' if ok else 'CHECK'}")

print(f"ALL MATCH: {all_match}")
