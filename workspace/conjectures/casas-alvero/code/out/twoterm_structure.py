"""Symbolic/structural proof check for the two-monomial submask law.

Claim: over F2, g = x^a + x^n (0<a<n, degree n) satisfies Hasse-CA iff a is a
proper nonempty subset-sum of the set bits of n.

Facts used (each verified here for the range):
  - Hasse-CA over F2: gcd(g, H_i(g)) non-constant for all i=1..n-1, where
    H_i(x^j) = C(j,i) x^{j-i} (ordinary Hasse, no i! factor).
  - Over F2, C(j,i) = 1 iff (i & j)==i (Lucas).

We verify the two directions as separate exact facts over a wide n range:

Direction A (necessity, structure): if a is NOT a proper nonempty subset-sum
of n's bits, then g fails Hasse-CA.  Specifically we hypothesize that the
FAILING derivative is i = a (H_a(g)) -- check that when a has a bit not in n's
support, or when a has bits beyond... let us record the exact failing index.

Direction B (sufficiency, structure): if a IS a proper nonempty subset-sum of
n's bits, then g satisfies Hasse-CA: gcd(g,H_i(g)) non-constant for every i.

We don't prove these here (that would need a theorem); we VERIFY the exact
mechanics of the two directions to understand the structure, then report what
would have to be true for the law to be wrong (attack step).
"""
from math import comb


def hasse_deriv(fbits, i):
    out = 0
    j = 0
    fb = fbits
    while fb:
        if fb & 1:
            if (i & j) == i:
                out |= 1 << (j - i)
        fb >>= 1
        j += 1
    return out


def pmod(a, b):
    bl = b.bit_length()
    while a.bit_length() >= bl:
        a ^= b << (a.bit_length() - bl)
    return a


def pgcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, pmod(a, b)
    return a


def is_ca_f2(fbits):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return True, i      # return (fails, failing index)
    return False, None


def set_bits(n):
    return [1 << b for b in range(n.bit_length()) if (n >> b) & 1]


def subset_sums(bits):
    sums = {0}
    for b in bits:
        sums |= {s + b for s in sums}
    return sums


def main():
    NMAX = 64
    # For each non-legal a, record the failing derivative index i
    from collections import Counter
    fail_idx = Counter()
    # For each legal a, confirm no derivative fails.
    legal_ok = True
    legal_n = 0
    for n in range(3, NMAX + 1):
        bits = set_bits(n)
        ss = subset_sums(bits)
        legal = {a for a in ss if 0 < a < n}
        for a in range(1, n):
            fbits = (1 << n) | (1 << a)
            fails, i = is_ca_f2(fbits)
            if a in legal:
                legal_n += 1
                if fails:
                    legal_ok = False
                    print(f"  LEGAL a={a} n={n} FAILED at i={i}  (unexpected)")
            else:
                if not fails:
                    print(f"  ILLEGAL a={a} n={n} PASSED (unexpected)")
                else:
                    fail_idx[i] += 1
    print(f"all legal a (n=3..{NMAX}) satisfy Hasse-CA: {legal_ok} ({legal_n} cases)")
    print("\nfailing-derivative-index histogram for illegal a (direction A):")
    print("  most common failing index i:", fail_idx.most_common(6))
    # Check: is the failing index always == a for these two-monomial polys?
    always_a = True
    for n in range(3, NMAX + 1):
        bits = set_bits(n)
        ss = subset_sums(bits)
        legal = {a for a in ss if 0 < a < n}
        for a in range(1, n):
            if a in legal:
                continue
            fbits = (1 << n) | (1 << a)
            fails, i = is_ca_f2(fbits)
            if fails and i != a:
                always_a = False
                print(f"  n={n} a={a}: failing index {i} != a")
    print(f"\nfailing index is always == a (for illegal a): {always_a}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
