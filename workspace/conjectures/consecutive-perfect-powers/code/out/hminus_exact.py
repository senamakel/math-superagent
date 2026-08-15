"""Exact verification of the relative class number formula
   h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (-1/2 * B_{1,chi})
   with B_{1,chi} = (1/p) * sum_{a=1}^{p-1} chi(a) a  (primitive odd chi).
Known values (OEIS A061653 / Washington): h^-(Q(zeta_p)):
   p=3->1, 5->1, 7->1, 11->1, 13->1, 23->3, 31->9, 37->37, 43->211.
Uses mpmath at high precision; result must round to the exact integer.
"""
import mpmath as mp

KNOWN = {3:1, 5:1, 7:1, 11:1, 13:1, 23:3, 31:9, 37:37, 43:211}

def primitive_root(p):
    # genuine primitive root: g^((p-1)/r) != 1 for EVERY prime divisor r of p-1
    n = p - 1
    prime_divs = []
    d = 2
    m = n
    while d * d <= m:
        if m % d == 0:
            prime_divs.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        prime_divs.append(m)
    for g in range(2, p):
        if all(pow(g, n // r, p) != 1 for r in prime_divs):
            return g
    raise ValueError("no primitive root found (should not happen for prime p)")

def rel_class_number(p, digits=60):
    mp.mp.dps = digits
    g = primitive_root(p)
    # exponent table: a = g^e
    logtab = {}
    v = 1
    for e in range(p-1):
        logtab[v] = e
        v = (v*g) % p
    P = mp.mpf(2)*p
    for k in range(1, p-1, 2):          # odd characters
        s = mp.mpc(0, 0)
        for a in range(1, p):
            e = logtab[a]
            w = mp.expj(mp.mpf(2)*mp.pi*k*e/(p-1))
            s += w*a
        B1 = s / p
        P = P * (mp.mpf(-1)/2 * B1)
    return P

ok = True
for p, known in KNOWN.items():
    val = rel_class_number(p)
    r = round(val.real)
    diff = abs(val.real - r) + abs(val.imag)
    good = diff < 10**-40 and r == known
    ok = ok and good
    print(f"p={p:3d}  h^- (exact claim) = {known:>5}   computed real={mp.nstr(val.real,25)}  imag={mp.nstr(val.imag,15)}  diff<1e-40={diff<10**-40}  match={good}")
print("ALL MATCH:", ok)
