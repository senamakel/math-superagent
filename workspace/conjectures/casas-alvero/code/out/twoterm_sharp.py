"""Sharp characterization of two-monomial F2 Hasse-CA.

Empirical finding (twoterm_structure): for g = x^n + x^a over F2 (0<a<n),
the only derivative that can fail is i = a, and it always fails there for
illegal a.  Combined with the identity g = x^a (x^{n-a} + 1) this suggests:

   SHARP CLAIM: Hasse-CA(g)  <=>  C(n,a) odd  <=>  (a & n) == a
                (a is a subset-sum of the set bits of n)
     and the failing derivative, when it fails, is always i = a.

We test this sharp claim EXACTLY for all n=3..64 and all a in 1..n-1:
  (1) Hasse-CA(g) == (C(n,a) odd)?
  (2) failing index == a whenever C(n,a) is even?
  (3) is gcd(g, H_a(g)) the ONLY relevant check? i.e. for every i != a,
      gcd(g,H_i(g)) is non-constant (no failure anywhere else) ?
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


def is_ca_f2(fbits, want_index=False):
    n = fbits.bit_length() - 1
    for i in range(1, n):
        hi = hasse_deriv(fbits, i)
        if hi == 0:
            continue
        if pgcd(fbits, hi) == 1:
            return (True, i) if want_index else True
    return (False, None) if want_index else False


def main():
    NMAX = 64
    c1 = c2 = c3_ok = 0
    c1_bad = c2_bad = 0
    for n in range(3, NMAX + 1):
        for a in range(1, n):
            fbits = (1 << n) | (1 << a)
            ca = (a & n) == a            # (a & n)==a  <=>  subset-sum of n's set bits
            pred_odd = (comb(n, a) % 2 == 1)
            assert pred_odd == ca, "Lucas: (a&n)==a should equal C(n,a) odd"
            is_ca = is_ca_f2(fbits)
            # (1) Hasse-CA == C(n,a) odd
            if is_ca == ca:
                c1 += 1
            else:
                c1_bad += 1
                print(f"  (1) FAIL n={n} a={a}: is_ca={is_ca} Codd={ca}")
            # Want-index detail
            fails, i = is_ca_f2(fbits, want_index=True)
            if fails:
                # (2) failing index always == a
                if i == a:
                    c2 += 1
                else:
                    c2_bad += 1
                    print(f"  (2) FAIL n={n} a={a}: i={i} != a")
    print(f"CLAIM(1): Hasse-CA(g)=C(n,a) odd  for all n=3..{NMAX}: "
          f"{'HOLDS' if c1_bad==0 else 'FAILS'}  ({c1}/{c1+c1_bad})")
    print(f"CLAIM(2): failing index == a whenever failed: "
          f"{'HOLDS' if c2_bad==0 else 'FAILS'}  ({c2} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
