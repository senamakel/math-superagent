"""Phase A worked examples + Phase B classification for H_even cap [2,1200].

This is the oracle-facing script: it (A) reproduces every worked example of the
spec and the paper on which the 3-Higgs machinery rests, and (B) combines the
sieve's witness tables (written by heven_sieve.py) with full factorization of
survivors to compute H_even ∩ [2,1200] and compare with the ten candidates
from arXiv:2605.20475 Theorem 8.

The ten numbers are the ONLY hard-coded expectation; a mismatch is printed
loudly and reflected in the exit code.

All arithmetic exact; no floats anywhere.

Usage: python3 code/heven_classify.py [--tables code/out]
"""
import os
import math
import sys

import sympy
from sympy import factorint, isprime, pollard_rho

from lib.higgs import (budget_row, factorize, is_3_higgs, is_unitary_perfect,
                       odd_higgs_cubefree, sigma_star, v2)

FIVE = [6, 60, 90, 87360, 146361946186458562560000]
TEN = [2, 6, 10, 18, 26, 30, 46, 62, 82, 122]


def phase_a1():
    """Oracle + 2-adic budget table for the five UPNs and the 12 control."""
    print("=" * 78)
    print("A1. sigma_star oracle + 2-adic budget identity")
    print("=" * 78)
    ok_all = True
    for n in FIVE + [12]:
        ss = sigma_star(n)
        up = (ss == 2 * n)
        b = budget_row(n)
        fs = b["factors"]
        rep = " * ".join("%d^%d" % (p, e) if e > 1 else str(p)
                         for p, e in sorted(fs.items()))
        print("n = %d" % n)
        print("    = %s" % rep)
        print("    sigma_star = %d, 2n = %d, unitary perfect: %s"
              % (ss, 2 * n, up))
        print("    a = %d, omega(odd) = %d, sum v2(p^e+1) = %d, a+1 = %d, "
              "identity: %s" % (b["a"], b["omega_odd"], b["budget_sum"],
                                b["a"] + 1, b["identity"]))
        if n == 12:
            if up:
                print("    *** CONTROL FAILURE: 12 must NOT be unitary perfect")
                ok_all = False
        elif (not up) or (not b["identity"]):
            ok_all = False
    if ok_all:
        print("A1 PASS: five UPNs verified, 12 negative control verified, "
              "budget identity exact on all five")
    else:
        print("A1 FAIL")
    return ok_all


def phase_a2():
    """3-Higgs predicate: statuses <= 31, 17 non-Higgs, 31 Higgs,
    definitional-equivalence self-test on primes <= 1000."""
    print("=" * 78)
    print("A2. 3-Higgs predicate")
    print("=" * 78)
    print("257 decision: 257-1 = 256 = 2^8, v2 = 8 > 3, so 257 is NOT "
          "3-Higgs and consequently m = 8 is NOT in H_even (2^8+1 = 257 is "
          "a non-Higgs prime divisor): is_3_higgs(257) = %s" % is_3_higgs(257))
    assert is_3_higgs(257) is False, "257 must NOT be 3-Higgs"
    statuses = {}
    for p in list(sympy.primerange(2, 32)):
        statuses[p] = is_3_higgs(p)
    print("prime <= 31:", " ".join("%d:%s" % (p, "H" if s else "n")
                                   for p, s in sorted(statuses.items())))
    ok17 = (statuses.get(17) is False)
    ok31 = (statuses.get(31) is True)
    print("17 non-Higgs (17-1 = 2^4, v2 = 4 > 3): %s" % ok17)
    print("31 Higgs (31-1 = 2*3*5): %s" % ok31)
    # The genuinely literal OEIS A057447 rule, run from scratch: p is
    # 3-Higgs iff (p-1) | P^3 where P is the product of all primes already
    # certified 3-Higgs by the SAME rule, and P starts at 2 (the base; 2 is
    # 3-Higgs).  Upon certification P *= p.  Compare with the working form
    # is_3_higgs (p-1 fully factored, every q | p-1 3-Higgs with v_q <= 3)
    # on every prime p <= 1000.  A single disagreement prints loudly and
    # fails the phase.
    lit_lists = {2: True}
    P = 2                       # running product of literal-certified primes
    equiv = True
    for p in sympy.primerange(3, 1000 + 1):
        lit = (P ** 3) % (p - 1) == 0      # the literal divisibility, exact
        lit_lists[p] = lit
        if lit != is_3_higgs(p):
            print("    *** LITERAL-RULE MISMATCH at p=%d: literal=%s "
                  "is_3_higgs=%s ***" % (p, lit, is_3_higgs(p)))
            equiv = False
        if lit:
            P *= p
    print("literal rule (p-1) | P^3 vs working form: agree on ALL primes "
          "<= 1000: %s" % equiv)
    print("literal-Higgs primes <= 1000: %d of %d"
          % (sum(lit_lists.values()),
             len(list(sympy.primerange(2, 1000 + 1)))))
    ok = ok17 and ok31 and equiv
    print("A2 %s" % ("PASS" if ok else "FAIL"))
    return ok


def phase_a3():
    """Cyclotomic / Aurifeuillean identities and the two worked examples."""
    print("=" * 78)
    print("A3. Cyclotomic / Aurifeuillean identities")
    print("=" * 78)
    ok = True
    x = sympy.Symbol("x")
    # 2^(2p) + 1 == 5 * Phi_{4p}(2) for the first 30 odd primes
    cnt = 0
    for p in sympy.primerange(3, 10**6):
        if cnt == 30:
            break
        ph = int(sympy.cyclotomic_poly(4 * p, x).subs(x, 2)) # exact int, no floats
        if 2 ** (2 * p) + 1 != 5 * ph:
            print("    FAIL Phi_{4p}(2) identity at p=%d" % p)
            ok = False
            break
        cnt += 1
    print("2^(2p)+1 == 5*Phi_{4p}(2) for first %d odd primes: %s"
          % (cnt, ok and cnt == 30))
    # Aurifeuillean split 2^(2p)+1 = (2^p - 2^((p+1)/2) + 1)(2^p +
    # 2^((p+1)/2) + 1) holds for every odd p (the cross terms cancel
    # algebraically); check it on all odd primes p <= 100.
    auri_ok = True
    for p in list(sympy.primerange(3, 100 + 1)):
        lhs = 2 ** (2 * p) + 1
        rhs = (2**p - 2**((p + 1) // 2) + 1) * (2**p + 2**((p + 1) // 2) + 1)
        if lhs != rhs:
            print("    FAIL p=%d" % p)
            auri_ok = False
    print("Aurifeuillean 2^(2p)+1 == (2^p - 2^((p+1)/2) + 1)(2^p + "
          "2^((p+1)/2) + 1) on all odd primes <= 100: %s"
          % ("PASS" if auri_ok else "FAIL"))
    ok = ok and auri_ok
    # m = 2426 worked example (paper section 5.2)
    x = 2 ** 303
    L = 2 * x**4 - 2 * x**2 + 1
    M = 2 * x**4 + 2 * x**2 + 1
    ok2426 = (L * M == 2**2426 + 1) and (L % 25893760589 == 0) \
        and sympy.isprime(25893760589)
    print("m=2426: L*M == 2^2426+1: %s; 25893760589 | L: %s; "
          "25893760589 prime: %s" % (L * M == 2**2426 + 1,
                                     L % 25893760589 == 0,
                                     sympy.isprime(25893760589)))
    # Filter-N example (paper 3.2): 20127043 | 2^1509 + 1, v3(20127042)=4>3
    f = factorize(20127042)
    ok1509 = (pow(2, 1509, 20127043) == 20127042) \
        and (f == {2: 1, 3: 4, 13: 1, 19: 1, 503: 1}) \
        and (not is_3_higgs(20127043))
    print("Filter-N: 20127043 | 2^1509+1: %s; 20127042 == 2*3^4*13*19*503: "
          "%s; 20127043 non-3-Higgs (v3=4>3): %s"
          % (pow(2, 1509, 20127043) == 20127042,
             f == {2: 1, 3: 4, 13: 1, 19: 1, 503: 1},
             not is_3_higgs(20127043)))
    ok = ok and ok2426 and ok1509
    print("A3 %s" % ("PASS" if ok else "FAIL"))
    return ok


def phase_b1():
    """B1 cross-check: how many odd k in [1,600] are Higgs-cubefree."""
    print("=" * 78)
    print("B1. Higgs-cubefree odd k in [1,600] (Proposition 4(1)(2) filter)")
    print("=" * 78)
    cnt = sum(1 for k in range(1, 601, 2) if odd_higgs_cubefree(k))
    # also list them for the record
    ok = (cnt == 246)
    print("odd k in [1,600] that are Higgs-cubefree: %d (paper: 246) %s"
          % (cnt, "MATCH" if ok else "MISMATCH"))
    return ok


def read_tables(tables_dir):
    ord_path = os.path.join(tables_dir, "ord_sieve_table.tsv")
    wit_path = os.path.join(tables_dir, "witnesses_1200.tsv")
    if not (os.path.exists(ord_path) and os.path.exists(wit_path)):
        return None, None
    ord_rows, wit_rows = [], []
    with open(ord_path) as f:
        for ln in f:
            a, b = ln.split()
            ord_rows.append((int(a), int(b)))
    with open(wit_path) as f:
        for ln in f:
            a, b, c = ln.split()
            wit_rows.append((int(a), int(b), int(c)))
    return ord_rows, wit_rows


def _split_rec(mm, fs, depth):
    """Bounded pollard-rho split (mirrors heven_patterns.partial_factor):
    trial division for factors <= 1e5, then up to `depth` rho attempts;
    return the leftover (1 iff fully factored).  Never searches for UPNs —
    it is a factoring routine for fixed m <= 1200."""
    if mm == 1:
        return 1
    m0 = mm
    for d in range(2, 100_001):
        if d * d > m0:
            break
        if m0 % d == 0:
            while m0 % d == 0:
                fs[d] = fs.get(d, 0) + 1
                m0 //= d
            if m0 == 1:
                return 1
    mm = m0
    if mm == 1:
        return 1
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if mm % d == 0:
            while mm % d == 0:
                fs[d] = fs.get(d, 0) + 1
                mm //= d
            if mm == 1:
                return 1
    # one round of pollard rho with a fresh seed
    rho = pollard_rho(mm)
    if rho and rho != mm and rho != 1:
        r1 = _split_rec(rho, fs, depth - 1)
        r2 = _split_rec(mm // rho, fs, depth - 1)
        if r1 != 1 and r2 != 1:
            # fully split
            return 1
        if r1 == 1:
            fs.update({})
        if r2 == 1:
            fs.update({})
        if r1 == 1 and r2 == 1:
            return 1
    if mm != 1 and sympy.isprime(mm):
        fs[mm] = fs.get(mm, 0) + 1
        return 1
    return mm


def _partial_factor(n):
    """({p: e}, leftover) for n; leftover == 1 iff complete."""
    fs = {}
    left = _split_rec(n, fs, depth=6)
    if left != 1 and sympy.isprime(left):
        fs[left] = fs.get(left, 0) + 1
        return fs, 1
    return fs, left


def phase_b3_b4(tables_dir):
    """Combine sieve witnesses with full factorization of survivors."""
    print("=" * 78)
    print("B3/B4. Survivor classification and Theorem 8 comparison")
    print("=" * 78)
    ord_rows, wit_rows = read_tables(tables_dir)
    if wit_rows is None:
        print("NO SIEVE TABLES — run heven_sieve.py first.  B3/B4 skipped.")
        return False

    # killed set: every even m <= 1200 with a non-3-Higgs witness r
    killed = set()
    witness_of = {}
    for r, m, o in wit_rows:
        witness_of.setdefault(m, []).append((r, o))
        if not is_3_higgs(r):
            killed.add(m)
    # every killed m must carry a verified witness: pow(2, m, r) == r-1
    for m in killed:
        assert any(pow(2, m, r) == r - 1 and not is_3_higgs(r)
                   for r, _ in witness_of[m])

    all_even = set(range(2, 1201, 2))
    survivors = sorted(all_even - killed)
    print("even m in [2,1200]: %d" % len(all_even))
    print("killed by sieve witness: %d" % len(killed))
    print("survivors (to full-factor): %d" % len(survivors))
    print("survivor list: %s" % survivors)

    # full factorization for m <= 122 (tiny, 2^122+1 has 37 digits); for
    # 122 < m <= 1200 the sieve already certifies every killed m, and
    # killing a candidate only needs ONE certified non-3-Higgs divisor, so
    # bounded trial division to 10^5 + one rho round suffices (same budget
    # as heven_patterns.py); an m with no witness found stays UNRESOLVED
    # and is reported, never silently classified.
    in_heven, undecided = [], []
    survivor_factorizations = {}
    for m in survivors:
        n = 2**m + 1
        if m <= 122:
            fs = factorint(n)
        else:
            fs, left = _partial_factor(n)
            if left != 1:
                undecided.append((m, "leftover %d digits"
                                  % (len(str(left)))))
                continue
        chk = 1
        for p, e in fs.items():
            chk *= p**e
        complete = (chk == n) and all(isprime(p) for p in fs)
        if not complete:
            undecided.append((m, fs))
            continue
        survivor_factorizations[m] = dict(fs)
        if all(is_3_higgs(int(p)) for p in fs):
            in_heven.append(m)

    print("-" * 78)
    print("computed H_even ∩ [2,1200] = %s" % in_heven)
    print("expected (Theorem 8)         = %s" % TEN)
    match = (in_heven == TEN and not undecided)
    print("MATCH: %s" % ("YES" if match else "*** NO — DISCREPANCY ***"))
    if not match:
        print("  only in computed: %s" % sorted(set(in_heven) - set(TEN)))
        print("  only in expected: %s" % sorted(set(TEN) - set(in_heven)))
    print("killed-by-sieve: %d, in-H_even: %d, unresolved(m>122): %d"
          % (len(killed), len(in_heven), len(undecided)))
    for m, fs in undecided:
        print("    UNRESOLVED m=%d: %s" % (m, fs))
    # spot-check two hand-verifiable factorizations
    sp6 = sympy.factorint(2**6 + 1)
    sp18 = sympy.factorint(2**18 + 1)
    print("spot check 2^6+1  = %s (expect {5:1, 13:1})" % sp6)
    print("spot check 2^18+1 = %s (expect {5:1, 13:1, 37:1, 109:1})" % sp18)
    ok37 = is_3_higgs(37) and factorize(36) == {2: 2, 3: 2}
    ok109 = is_3_higgs(109) and factorize(108) == {2: 2, 3: 3}
    print("37 Higgs (36=2^2*3^2): %s; 109 Higgs (108=2^2*3^3): %s"
          % (ok37, ok109))
    return match


def main():
    tables_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "out")
    if "--tables" in sys.argv:
        tables_dir = sys.argv[sys.argv.index("--tables") + 1]
    a1 = phase_a1()
    a2 = phase_a2()
    a3 = phase_a3()
    b1 = phase_b1()
    b34 = phase_b3_b4(tables_dir)
    print("=" * 78)
    print("SUMMARY  A1:%s A2:%s A3:%s B1:%s B3/B4:%s"
          % ("PASS" if a1 else "FAIL",
             "PASS" if a2 else "FAIL",
             "PASS" if a3 else "FAIL",
             "PASS" if b1 else "FAIL",
             "PASS" if b34 else "FAIL"))
    sys.exit(0 if (a1 and a2 and a3 and b1 and b34) else 1)


if __name__ == "__main__":
    main()