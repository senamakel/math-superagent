#!/usr/bin/env python3
"""Directive 14: closed-form biquadratic character (2/(2^p+i))_4 in Z[i].

Question: does the biquadratic character of 2 modulo the Gaussian factor
2^p + i constrain which rational prime divisors r | Phi_{4p}(2) can be
3-Higgs, beyond the known ONE-WAY per-divisor test
    (2/r)_4 = +1  <=>  r ≡ 1 (mod 16)  <=>  v2(r-1) >= 4  =>  r not 3-Higgs.

Two independent evaluations of (2/(2^p+i))_4 (exact, all integer/rational
arithmetic; the symbol value is a complex 4th root of unity i^k):

  (A) DIRECT / multiplicativity:
      (2/(2^p+i))_4 = prod_{pi^e || 2^p+i} (2/pi)_4^e ,   (Jacobi-style
      extension to a composite Gaussian denominator, exactly the paper's
      divisor-transference product identity).  Each (2/pi)_4 is computed
      inside the residue field F_q = Z[i]/(pi), N(pi)=q, as
      c = 2^((q-1)/4) mod q compared with the class of i (identical to
      code/heven_gauss.py's quartic_char and its per-divisor rows).

  (B) SUPPLEMENTARY LAWS on the primary associate alpha = -i*(2^p+i)
      = a + bi with a = 1, b = -2^p  (a odd, b even, a+b ≡ 1 mod 4 => alpha
      is PRIMARY).  Derivation from 2 = -i*(1+i)^2 and Williams(1976)/
      Wikipedia supplementary laws:
        [-1/pi]_4 = (-1)^{(a-1)/2}
        [ i/pi]_4 = i^{-(a-1)/2}
        [1+i/pi]_4 = i^{(a-b-1-b^2)/4}
      =>
        [2/pi]_4 = [-i/pi]_4 * [1+i/pi]_4^2
                 = i^{(a-1)/2} * i^{(a-b-1-b^2)/2}
                 = i^{(2a - b - 2 - b^2)/2}.
      For a=1, b=-2^p this exponent is (2^p - 2^{2p})/2 = 2^{p-1}(1-2^p),
      which is ≡ 0 (mod 4) for every odd prime p >= 3 (2^{p-1} divisible
      by 4, (1-2^p) odd).  Hence [2/alpha]_4 = i^0 = 1 identically.

The deliverable questions:
  (a) closed form of (2/(2^p+i))_4 as a function of p (mod 16): answer 1.
  (b) does any residue class of p force a head r ≡ 1 mod 16?  A head is a
      SINGLE divisor r with (2/r)_4 = +1.  The product identity is a
      character-sum identity over ALL divisors taken mod 4; even if the
      product were i^1 = i, that would only say the total count of
      (+,-,+,i,-i) classes is pinned mod 4, never that a single r has
      (2/r)_4 = +1.  And here the product is identically 1, so it says
      nothing at all.  Any r ≡ 1 mod 16 could in principle have its
      +1 compensated by other factors.  Conclusion (b): NO residue class
      forces a head; the class-level information is vacuous.
  (c) verdict.  Because the product is identically 1 (0 = exponent mod 4),
      the global biquadratic character of 2 captures exactly nothing about
      the divisor set beyond what the per-divisor mod-16 test already
      gives.  Line CLOSED-no-constraint.

Every output number is exact (int/rational arithmetic and sympy
factorint); the only float-free exact machinery is used throughout.
"""
import sys
from math import gcd, isqrt
from sympy import factorint

def fmt_i(k):
    return {0: "+1", 1: "+i", 2: "-1", 3: "-i"}[k % 4]

def v2_of(n):
    return (n & -n).bit_length() - 1

def cornacchia(q, x):
    a, b = q, x % q
    while b * b > q:
        a, b = b, a % b
    u = b
    w2 = q - u * u
    w = isqrt(w2)
    assert w * w == w2 and w > 0
    return (u, w)

def factor_gauss(p):
    """Factor 2^p + i in Z[i].  Returns rows [(q,e,su,sv)] (su+sv i)^e."""
    a = 2 ** p
    z = (a, 1)
    N = a * a + 1
    fN = factorint(N)
    rows = []
    for q, e in sorted(fN.items()):
        q = int(q)
        assert q % 4 == 1
        x = a % q
        assert (x * x) % q == q - 1
        u, v = cornacchia(q, x)
        assert u * u + v * v == q
        pi_div = ((a * u + v) % q == 0) and ((u - a * v) % q == 0)
        pb_div = ((a * u - v) % q == 0) and ((a * v + u) % q == 0)
        assert pi_div != pb_div
        su, sv = (u, v) if pi_div else (u, -v)
        rows.append((q, e, su, sv))
    # verify product == 2^p + i up to a unit
    pr = (1, 0)
    for _q, e, su, sv in rows:
        for _ in range(e):
            pr = (pr[0] * su - pr[1] * sv, pr[0] * sv + pr[1] * su)
    ok = any(pr == (uu[0] * z[0] - uu[1] * z[1], uu[0] * z[1] + uu[1] * z[0])
             for uu in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    assert ok, p
    return rows

def quartic_char_div(q, su, sv):
    """2 is a 4th power mod Gaussian prime pi=su+sv i?  returns k (i^k)."""
    c = pow(2, (q - 1) // 4, q)
    if c == 1:
        return 0
    if c == q - 1:
        return 2
    i_cls = (-su * pow(sv, q - 2, q)) % q
    assert (i_cls * i_cls) % q == q - 1
    if c == i_cls:
        return 1
    assert c == (q - i_cls) % q
    return 3

def supplementary_closed_form(p):
    """[2/alpha]_4 exponent k with alpha = -i*(2^p+i) primary, a=1,b=-2^p.
    Returns k mod 4 via (2a-b-2-b^2)/2 mod 4, computed exactly."""
    two_p = 2 ** p
    a, b = 1, -two_p
    num = 2 * a - b - 2 - b * b
    assert num % 2 == 0
    k = (num // 2) % 4
    return k

def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    picked = [p for p in primes if p <= pmax]
    assert picked

    print("Directive 14: (2/(2^p+i))_4 closed form, exact computation.")
    print("primes p checked: %s (p <= %d)\n" % (picked, pmax))
    print("%-5s %-6s %-28s %-26s %s" % (
        "p", "p%16", "direct (prod (2/pi)_4^e)", "supplementary [2/alpha]_4",
        "match"))
    rows_p16 = {}
    allmatch = True
    total_rows = 0
    for p in picked:
        rows = factor_gauss(p)
        total_rows += len(rows)
        k_dir = 0
        head_list = []
        for q, e, su, sv in rows:
            kk = quartic_char_div(q, su, sv)
            k_dir = (k_dir + e * kk) % 4
            if (q - 1) % 16 == 0:
                head_list.append(q)
        k_sup = supplementary_closed_form(p)
        match = (k_dir == k_sup)
        allmatch = allmatch and match
        rows_p16.setdefault(p % 16, []).append((p, k_dir, k_sup, head_list))
        print("%-5d %-6d %-28s %-26s %s" % (
            p, p % 16, fmt_i(k_dir), fmt_i(k_sup), "OK" if match else "FAIL"))

    print("\nClosed form by p mod 16: all values tabulated above; "
          "every row is %s." % fmt_i(0))
    print("Identically (2/(2^p+i))_4 = %s = i^0 = 1  for all odd primes p>=3."
          % fmt_i(0))

    print("\nPer-residue-class summary (p mod 16 -> distinct (k_dir, k_sup)):")
    for r16 in sorted(rows_p16):
        vals = set((k, ks) for (_p, k, ks, _h) in rows_p16[r16])
        print("  p%%16=%d: %s" % (r16, ", ".join("[dir=%s sup=%s]" %
              (fmt_i(k), fmt_i(ks)) for (k, ks) in sorted(vals))))

    # ---- per-p head existence is independent of the product value ----
    print("\nHead check: for each p, any divisor r ≡ 1 (mod 16) present?")
    n_any_head = 0
    for r16 in sorted(rows_p16):
        for (p, k_dir, k_sup, hl) in rows_p16[r16]:
            has = len(hl) > 0
            n_any_head += int(has)
            print("  p=%d  (2/(2^p+i))_4=%s  heads=%s  %s"
                  % (p, fmt_i(k_dir), hl if has else "none",
                     "(product=1 yet head present!)" if (has and k_dir == 0)
                     else ""))
    print("primes with >=1 head: %d / %d" % (n_any_head, len(picked)))

    print("\nTotal Gaussian divisor rows enumerated: %d (all exact factors)."
          % total_rows)
    print("All supplementary == direct matches: %s" % allmatch)

    print("\n" + "=" * 72)
    print("VERDICT")
    print("(a) closed form: (2/(2^p+i))_4 = 1 identically (p any odd prime).")
    print("(b) no residue class of p forces a head r≡1 mod 16: the product")
    print("    is identically 1, and even a non-1 product value would only")
    print("    pin the total count of the four character classes mod 4,")
    print("    never force one specific divisor to be (2/r)_4=+1.")
    print("(c) the global quartic character of 2 carries NO information about")
    print("    which r | Phi_{4p}(2) can be 3-Higgs beyond the one-way")
    print("    per-divisor mod-16 test already established.")
    print("    => DIRECTIVE-14 LINE CLOSED-no-constraint.")
    sys.exit(0 if allmatch else 1)

if __name__ == "__main__":
    main()
