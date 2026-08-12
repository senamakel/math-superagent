#!/usr/bin/env python3
"""pattern_finder: verify the closed form |S(e)| = (prod_{p=1 mod 4, p^a||e}
(2a+1) - 1) / 2, and show that the recorded sequence S4 = "first e with
|S(e)| = k" is exactly the closed-form minimization over multiplicative
partitions of 2k+1:

    m(k) = min over factorisations 2k+1 = prod u_j (u_j odd >= 3) of
           prod_j q_j^{(u_j-1)/2}

where q_1 < q_2 < ... are the primes = 1 mod 4 and the exponents
(u_j-1)/2 are sorted descending before assignment (rearrangement
inequality: largest exponent to smallest prime).

Inputs: the S4 row recorded in code/out/pattern_seq_output.txt:
  S4 first e with |S(e)|=k, k=1..40:
  5,25,125,65,3125,15625,325,390625,1953125,1625,-,4225,1105,-,-,40625,
  21125,-,203125,-,-,5525,-,274625,5078125,-,528125,-,-,-,27625,
  2640625,-,-,-,-,71825,6865625,-,32045   ('-' = nothing <= 1e7)

Every number below is exact integer arithmetic.
"""
from math import isqrt
from functools import lru_cache
import random

# ---------------------------------------------------------------- closed form
def nS(e):
    """|S(e)| = (prod_{p = 1 mod 4, p^a || e} (2a+1) - 1) / 2."""
    n, prod = e, 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            if p % 4 == 1:
                prod *= 2 * a + 1
        p += 1
    if n > 1 and n % 4 == 1:
        prod *= 3
    return (prod - 1) // 2


def S_by_xloop(e):
    """Direct definition: d > 0 with e^2 - d and e^2 + d both squares.
    O(e) loop; the independent oracle for the closed form."""
    out = set()
    c = e * e
    for x in range(1, isqrt(c - 1) + 1):
        y2 = 2 * c - x * x
        y = isqrt(y2)
        if y * y == y2:
            out.add(c - x * x)
    return out


def verify_closed_form():
    bad = 0
    # exhaustive small
    for e in range(1, 2001):
        if nS(e) != len(S_by_xloop(e)):
            bad += 1
            print(f"  MISMATCH e={e}: closed {nS(e)} xloop {len(S_by_xloop(e))}")
            if bad > 5:
                break
    # random large
    rng = random.Random(12345)
    for _ in range(10):
        e = rng.randint(10**5, 4 * 10**5)
        if nS(e) != len(S_by_xloop(e)):
            bad += 1
            print(f"  MISMATCH e={e}")
    print(f"[closed-form verify] exhaustive e<=2000 + 10 random e in "
          f"[1e5,4e5]: {'PASS' if bad == 0 else str(bad) + ' FAILS'}")
    return bad == 0


# --------------------------------------------------- multiplicative-partition m(k)
PRIMES_1MOD4 = []
def primes_1mod4(up_to):
    """Primes == 1 mod 4 (with 2 appended conceptually for nothing)."""
    out = []
    for x in range(5, up_to + 1):
        ok = True
        for p in range(2, isqrt(x) + 1):
            if x % p == 0:
                ok = False
                break
        if ok and x % 4 == 1:
            out.append(x)
    return out


PRIMES_1MOD4 = primes_1mod4(400)   # enough: smallest is 5, exponents <= 60


def multiplicative_partitions(N):
    """All multisets (sorted ascending, parts >= 3 odd) with product N.
    Each part u >= 3 odd is admissible as 2a+1."""
    res = []

    def rec(rem, lo, acc):
        if rem == 1:
            res.append(tuple(acc))
            return
        # parts >= lo, odd, >= 3, dividing rem (product exactly rem)
        d = lo | 1  # ensure odd
        while d <= rem:
            if d >= 3 and rem % d == 0:
                rec(rem // d, d, acc + [d])
            d += 2
    rec(N, 3, [])
    return res


def m(k):
    """Smallest e with |S(e)| = k, by multiplicative partitions of 2k+1."""
    N = 2 * k + 1
    best = None
    for parts in multiplicative_partitions(N):
        exps = sorted(((u - 1) // 2 for u in parts), reverse=True)
        e = 1
        for a, q in zip(exps, PRIMES_1MOD4):
            e *= q ** a
        if best is None or e < best:
            best = e
    return best


# ------------------------------------------------------------- recorded S4 row
S4_RECORDED = [5, 25, 125, 65, 3125, 15625, 325, 390625, 1953125, 1625, None,
               4225, 1105, None, None, 40625, 21125, None, 203125, None, None,
               5525, None, 274625, 5078125, None, 528125, None, None, None,
               27625, 2640625, None, None, None, None, 71825, 6865625, None,
               32045]

def main():
    ok = verify_closed_form()

    print("\n[m(k) = minimal e with |S(e)| = k, exact closed form]")
    print("k : m(k)              |S(m(k))|  recorded-S4(<=1e7)  match")
    match_all = True
    for k in range(1, 41):
        mk = m(k)
        ns = nS(mk)
        rec = S4_RECORDED[k - 1]
        if rec is None:
            status = "gap>1e7" if mk > 10**7 else "RECORDED-GAP-BUT-FOUND<1e7 !!"
        else:
            status = "match" if mk == rec else f"DISAGREE recorded {rec}"
        if status.startswith("D") or (rec is not None and mk != rec) or \
           (rec is None and not mk > 10**7):
            match_all = False
        print(f"{k:2d} : {mk:>12d}   {ns:>7d}   {str(rec):>16s}  {status}")
    print(f"\n[m(k) consistent with recorded S4 over k=1..40: "
          f"{'YES' if match_all else 'NO'}]")

    # smallest e with |S(e)| >= t, by scanning m(k):
    print("\n[smallest e with |S(e)| >= t (from m(k), exact)]")
    for t in (3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 40):
        best = min((m(k), k) for k in range(1, 81) if m(k) != 0)
        # recompute: minimum over k >= t
        cand = [(m(k), k) for k in range(1, 81) if nS(m(k)) >= t]
        e_min, k_min = min(cand)
        print(f"  t={t:2d}: e={e_min:>12d} (|S|={k_min} at k={k_min})")

    # extension: m(41..60) for the record
    print("\n[m(41..60) extension (exact prediction, unverified by scan)]")
    print("  " + ", ".join(str(m(k)) for k in range(41, 61)))
    return 0 if ok and match_all else 1


if __name__ == "__main__":
    raise SystemExit(main())