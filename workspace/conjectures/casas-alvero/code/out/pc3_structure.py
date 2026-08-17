"""Enumerate ALL F2 Hasse-CA counterexamples at pc=3 degrees (n=7,11,13,19,21,25)
and look for a unified structural form.  pc=3 profile is rigid {2:6,4:5,6:3};
we want a structural explanation (a family of polynomials) behind it.

Interesting hypothesis from n=7 factorization: every support-6 counterexample
may equal x^a(x+1)^(n-a) for some a; every support-4 may be a different form.
Let's test: for each ce, check whether it equals x^a * (x+1)^(n-a) (the
'x,a-shifted 1-family'), and whether it has the shape x^u (x+1)^v * q.
We test the cleanest candidate: the full set = products over the set-bits.

F2 note: for n with pc=3, bits {b0,b1,b2}.  A natural construction:
f = (x^{b0} + x^0)^? ... Actually test: is every ce of degree n equal to
x^a (x+1)^(n-a) for some a?  That would give only pc(n)=... supports.
Let's just list membership.
"""
from math import comb


def hasse_deriv(fbits, i):
    out = 0; j = 0; fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i: out |= 1 << (j - i)
        fb >>= 1; j += 1
    return out


def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0: continue
        if pgcd(fbits, hi) == 1: return False
    return True


def is_pure_f2(fbits, n):
    if fbits == (1 << n): return True
    bits = 0
    for j in range(n + 1):
        if comb(n, j) % 2 == 1: bits |= 1 << j
    return fbits == bits


def xa_x1_family(n):
    """f = x^a (x+1)^(n-a): supports generated over F2 by Lucas on n-a."""
    fam = set()
    for a in range(1, n):
        bits = 0
        for j in range(n - a + 1):
            if comb(n - a, j) % 2 == 1:
                bits |= 1 << (a + j)
        fam.add(bits)
    return fam


def support(fb):
    return [j for j in range(fb.bit_length()) if (fb >> j) & 1]


def bits_of(n):
    return [b for b in range(n.bit_length()) if (n >> b) & 1]


def main():
    for n in (7, 11, 13, 19, 21, 25):
        if (1 << n) > 100_000:
            print(f"n={n}: skip (2^n too large for full enumeration)")
            continue
        fam = xa_x1_family(n)
        ces = []
        for v in range(1 << n):
            fb = (1 << n) | v
            if is_ca_f2(fb) and not is_pure_f2(fb, n):
                ces.append(fb)
        counts = {}
        for fb in ces:
            s = support(fb)
            counts[len(s)] = counts.get(len(s), 0) + 1
        infam = sum(1 for fb in ces if fb in fam)
        print(f"n={n} pc={len(bits_of(n))} bits={bits_of(n)} ce={len(ces)} "
              f"counts={dict(sorted(counts.items()))} "
              f"in x^a(x+1)^(n-a) family: {infam}/{len(ces)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
