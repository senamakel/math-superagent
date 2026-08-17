#!/usr/bin/env python3
"""Independent exact re-check of the G2 slope claim at k=3, 4, 5.

Purely by-hand-to-code reproduction: computes the arc-midpoint mechanical words
for slope a = F(n-1)/F(n) (as the claim states) and for a = F(n-2)/F(n) (the
implementation's slope), and compares each against the true distinct length-k
factors of the Fibonacci word harvested from S_n.

This is the counterexample check: for the stated slope F(n-1)/F(n), the
mechanical words must NOT equal the true factor set for some k.
"""
from fractions import Fraction


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_word(n):
    a, b = '0', '01'
    for _ in range(n - 1):
        a, b = b, b + a
    return b


def true_factors(kmax):
    w = fib_word(30)
    return {k: {w[i:i+k] for i in range(len(w)-k+1)} for k in range(1, kmax+1)}


def mech_words(k, a):
    """Arc-midpoint mechanical words for slope a, k+1 arcs."""
    pts = sorted((Fraction(-m) * a) % 1 for m in range(k + 1))
    out = set()
    for i in range(k + 1):
        c1 = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + 1
        xm = (c1 + c2) / 2
        if xm >= 1:
            xm -= 1
        digs = []
        for j in range(k):
            lo = int(((xm + Fraction(j) * a).numerator) //
                     ((xm + Fraction(j) * a).denominator))
            hi = int(((xm + Fraction(j + 1) * a).numerator) //
                     ((xm + Fraction(j + 1) * a).denominator))
            digs.append(hi - lo)
        out.add(''.join(map(str, digs)))
    return out


def main():
    tf = true_factors(6)
    for k in (3, 4, 5):
        # smallest n with F(n) > k  (F(5)=5>3, F(6)=8>4, F(6)=8>5)
        n = next(n for n in range(1, 30) if fib(n) > k)
        a_bad = Fraction(fib(n-1), fib(n))     # claim's formula F(n-1)/F(n)
        a_ok = Fraction(fib(n-2), fib(n))      # implementation F(n-2)/F(n)
        w_bad = mech_words(k, a_bad)
        w_ok = mech_words(k, a_ok)
        true = tf[k]
        print(f"k={k}  n={n}  F(n)={fib(n)}")
        print(f"   stated slope F(n-1)/F(n)={a_bad}: words={sorted(w_bad)}  "
              f"== true? {w_bad == true}")
        print(f"   corr. slope F(n-2)/F(n)={a_ok}: words={sorted(w_ok)}  "
              f"== true? {w_ok == true}")
        if w_bad != true:
            print(f"   -> REFUTED for stated slope (mirror words present: "
                  f"{sorted(w_bad - true)}; missing: {sorted(true - w_bad)})")
        if w_ok != true:
            print(f"   -> MISMATCH for corrected slope: {sorted(w_ok)} vs {sorted(true)}")


if __name__ == '__main__':
    main()
