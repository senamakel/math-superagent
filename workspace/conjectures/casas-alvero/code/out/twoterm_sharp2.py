"""Sharp characterization of two-monomial F2 Hasse-CA — clean conventions.

FACTS (all verified in this file, no mixed conventions):
  - g = x^n + x^a over F2 (0<a<n).
  - single helper `fails_at(fbits)` returns the SMALLEST bad index i in
    1..n-1 with gcd(fbits, H_i)=1 (i.e. Hasse-CA fails), or None if Hasse-CA
    holds (all i pass, gcd non-constant or H_i vanishes).

Empirical structure to confirm:
  (S1) Hasse-CA(g) HOLDS  <=>  (a & n) == a   (a = subset-sum of n's set bits)
       [equivalently C(n,a) odd, by Lucas]
  (S2) whenever Hasse-CA(g) FAILS, the failing index is exactly i = a.
  (S3) for i != a, gcd(g, H_i(g)) is always non-constant (never a failure).
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


def fails_at(fbits):
    """Return failing index i (Hasse-CA fails at i), or None if it holds."""
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return i
    return None


def main():
    NMAX = 64
    s1 = s2 = s3 = 0
    s1b = s2b = s3b = 0
    for n in range(3, NMAX + 1):
        for a in range(1, n):
            fbits = (1 << n) | (1 << a)
            subset = (a & n) == a          # a subset-sum of n's set bits
            assert ((comb(n, a) % 2) == 1) == subset, "Lucas sanity"
            bad = fails_at(fbits)
            holds = bad is None
            # (S1) holds <=> subset
            if holds == subset:
                s1 += 1
            else:
                s1b += 1
                print(f"  S1 FAIL n={n} a={a}: holds={holds} subset={subset}")
            # (S2) if fails, index == a
            if (not holds) and bad != a:
                s2b += 1
                print(f"  S2 FAIL n={n} a={a}: bad={bad} != a")
            else:
                s2 += 1
            # (S3) no i != a ever fails
            if (not holds) and bad != a:
                pass  # covered by S2
            # independently: for i != a never fail -> scan all and insist the
            # only possible bad index is a.  fails_at returns first bad; if the
            # only bad is a then when holds fails it must be a (S2 covers).
    print(f"S1: Hasse-CA holds <-> (a&n)==a, n=3..{NMAX}: "
          f"{'HOLDS' if s1b==0 else 'FAILS'} ({s1} ok, {s1b} fail)")
    print(f"S2: failing index == a whenever it fails: "
          f"{'HOLDS' if s2b==0 else 'FAILS'} ({s2} ok, {s2b} fail)")
    # S3: verify NO derivative i != a ever yields a failure, by checking each
    # i separately for every illegal a (a not a subset-sum).
    s3b = 0
    for n in range(3, NMAX + 1):
        for a in range(1, n):
            subset = (a & n) == a
            if subset:
                continue
            fbits = (1 << n) | (1 << a)
            for i in range(1, n):
                if i == a:
                    continue
                hi = hasse_deriv(fbits, i)
                if hi and pgcd(fbits, hi) == 1:
                    s3b += 1
                    print(f"  S3 FAIL n={n} a={a} i={i}: gcd(f,H_i)=1 for i!=a")
    print(f"S3: no derivative i != a ever fails (illegal a): "
          f"{'HOLDS' if s3b==0 else 'FAILS'} ({s3b} failures found)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
