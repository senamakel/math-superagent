#!/usr/bin/env python3
"""Independent re-derivation of the pass-3 exact-mean weight-threshold result
for linear supply, using a code path that shares nothing with
code/scholar/threshold_exact_mean.py.

Background (SUPPLY / problem.md): for a fixed depth d in [2, n-1] the fold cell
T(n,d) = XOR over the k = 2^popcount(d) positions of row M_d.  Over all weight-w
strings, by symmetry a fixed set of k positions meets the weight-w layer
hypergeometrically: the number of weight-w strings with exactly r ones among
those k positions is C(k,r) * C(n-k, w-r).  Hence

    P_d(w) = P(XOR of those k positions is odd)
           = sum_{r odd} C(k,r) C(n-k, w-r) / C(n,w).        [DIRECT]

The scholar's stored form is the generating-function coefficient

    P_d(w) = ( C(n,w) - [z^w] (1-z)^k (1+z)^{n-k} ) / ( 2 C(n,w) ).

The two agree because sum_r (-1)^r C(k,r) C(n-k,w-r) = even - odd, and
even + odd = C(n,w), so odd = (C(n,w) - (even-odd))/2.  This script uses the
DIRECT hypergeometric odd-count as its primary route and cross-checks it
against the generating-function coefficient only as a confirmation.

mean_n(w) = average of nu2/n over all weight-w strings = (1/n) sum_d P_d(w).
Grouped by popcount p of d (k_p = 2^p, N_p = #{d in [2,n-1]: popcount(d)=p}):
    mean_n(w) = (1/n) sum_p N_p P_{k_p}(w).

The exact mean-threshold is theta_mean(n) = min{ w/n : mean_n(w) >= 0.40 }.

Exact integer / Fraction arithmetic throughout; no floats in decisions.
"""

from math import comb
from fractions import Fraction
from collections import Counter


def popcount_distribution(n):
    """N_p = #{d in [2, n-1] : popcount(d) = p}."""
    c = Counter()
    for d in range(2, n):
        c[d.bit_count()] += 1
    return c


def C(n, k):
    return comb(n, k)


def odd_count_direct(k, n, w):
    """Sum over r odd of C(k,r) C(n-k, w-r).  Exact big-int.  == #weight-w
    strings with an odd number of ones among a FIXED k-set."""
    lo = max(0, w - (n - k))
    hi = min(k, w)
    s = 0
    for r in range(lo, hi + 1):
        if r & 1:
            s += C(k, r) * C(n - k, w - r)
    return s


def coeff_genfunc(n, k, w):
    """[z^w] (1-z)^k (1+z)^{n-k} = sum_j (-1)^j C(k,j) C(n-k,w-j).  The
    generating-function coefficient used by the scholar route (kept here only
    as the CROSS-CHECK target, not the primary path)."""
    lo = max(0, w - (n - k))
    hi = min(k, w)
    c = 0
    for j in range(lo, hi + 1):
        term = C(k, j) * C(n - k, w - j)
        c += -term if (j & 1) else term
    return c


def P_direct(n, k, w):
    """P_d(w) by the direct hypergeometric odd-count."""
    total = C(n, w)
    return Fraction(odd_count_direct(k, n, w), total)


def P_scholar(n, k, w):
    """P_d(w) by the storing generating-function form (cross-check target)."""
    total = C(n, w)
    c = coeff_genfunc(n, k, w)
    return Fraction(total - c, 2 * total)


def mean_direct(n, w, Np):
    """mean_n(w) = (1/n) sum_p N_p * P_{k_p}(w), direct odd-count route."""
    total = Fraction(0)
    for p, cnt in Np:
        k = 1 << p
        total += cnt * P_direct(n, k, w)
    return total / n


def mean_scholar(n, w, Np):
    """mean_n(w) via the generating-function form (cross-check)."""
    total = Fraction(0)
    for p, cnt in Np:
        k = 1 << p
        total += cnt * P_scholar(n, k, w)
    return total / n


def main():
    print("sequence = weight-w binary strings over F2^n (all weights, exact mean)")
    print("oracle   = DIRECT hypergeometric odd-count (cf scholar gen-func); brute = lib.supply_fold.s_sos")
    print("range    = brute n in {6,8,10,12,14}; threshold to n=32768")
    print("=" * 78)
    print("PART 1 -- P_d(w): direct hypergeometric odd-count vs scholar gen-func")
    print("=" * 78)
    ok1 = True
    # NOTE: k = 2^popcount(d) is reachable only with k <= n-1 (d in [2,n-1]
    # has popcount(d) <= popcount(n-1), so k <= 2^floor(log2(n-1)) <= n-1).
    # All points below keep k <= n-1; a k > n case is unreachable and undefined.
    for n, w, k in [(8, 3, 2), (8, 3, 4), (10, 2, 2), (12, 4, 8), (16, 5, 4),
                    (20, 4, 2), (12, 3, 8), (14, 4, 2), (16, 3, 8), (6, 2, 4)]:
        pd = P_direct(n, k, w)
        ps = P_scholar(n, k, w)
        same = (pd == ps)
        ok1 = ok1 and same
        print(f"  (n,w,k)=({n},{w},{k}): direct={float(pd):.6f} "
              f"scholar={float(ps):.6f} match={same}")
    print(f"  PART 1 cross-check: {'PASS' if ok1 else 'FAIL'}")

    print("\n" + "=" * 78)
    print("PART 2 -- mean_n(w) formula vs literal brute enumeration (s_sos)")
    print("=" * 78)
    from itertools import combinations
    from lib.supply_fold import s_sos

    def brute_mean(n, w):
        tot = 0
        cnt = 0
        for ones in combinations(range(n), w):
            h = [0] * n
            for j in ones:
                h[j] = 1
            _, c1 = s_sos(n, h)      # c1 = #T=1 = nu2
            tot += c1
            cnt += 1
        return Fraction(tot, cnt) / n

    ok2 = True
    nw_list = [(6, 1), (6, 2), (8, 1), (8, 3), (8, 4), (10, 2), (10, 3),
               (12, 3), (12, 5), (14, 4)]
    for n, w in nw_list:
        Np = [(p, c) for p, c in sorted(popcount_distribution(n).items())]
        mdir = mean_direct(n, w, Np)
        br = brute_mean(n, w)
        same = (mdir == br)
        ok2 = ok2 and same
        print(f"  n={n} w={w}: formula={float(mdir):.6f} brute={float(br):.6f} "
              f"match={same}")
    print(f"  PART 2 cross-check: {'PASS' if ok2 else 'FAIL'}")

    print("\n" + "=" * 78)
    print("PART 3 -- exact mean-threshold theta_mean(n)=min{w/n: mean>=0.40}")
    print("=" * 78)
    # confirm the required n=8,w=3 check explicitly
    N8 = [(p, c) for p, c in sorted(popcount_distribution(8).items())]
    m83 = mean_direct(8, 3, N8)
    print(f"  n=8 w=3 mean nu2/n = {float(m83):.4f}  (expected 0.4464) "
          f"{'OK' if m83 == Fraction(25, 56) else 'MISMATCH'}")
    # (25/56 = 0.4464...)

    ns = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
    rows = []
    THR = Fraction(2, 5)
    for n in ns:
        Np = [(p, c) for p, c in sorted(popcount_distribution(n).items())]
        first = None
        for w in range(1, n):
            if mean_direct(n, w, Np) >= THR:
                first = w
                break
        rows.append((n, first))
        print(f"  n={n:>6}  first w={str(first):>5}  w/n={first / n:.6f}"
              if first is not None else f"  n={n:>6}  (none < 0.40)")

    print("\n" + "=" * 78)
    print("PART 4 -- exact per-weight mean_n(w) near the crossing (for the")
    print("          sampled-FRAC comparison)")
    print("=" * 78)
    for n in [64, 256, 1024, 4096, 16384, 32768]:
        Np = [(p, c) for p, c in sorted(popcount_distribution(n).items())]
        wcross = dict(rows)[n]
        print(f"  n={n}: crossing w={wcross} (w/n={wcross / n:.4f})")
        for w in range(max(1, wcross - 4), wcross + 5):
            print(f"      w={w:>5}  w/n={w / n:.4f}  mean={float(mean_direct(n, w, Np)):.5f}")

    print("\n" + "=" * 78)
    print("NEGATIVE CONTROL -- all-ones string (max weight n) is in the fold")
    print("kernel: nu2/n -> 0, so weight alone never forces linear supply")
    print("=" * 78)
    for n in [8, 16, 32, 64, 128, 256]:
        h = [1] * n
        _, c1 = s_sos(n, h)
        print(f"  n={n}: all-ones nu2={c1}  nu2/n={c1 / n:.4f}")

    print("\n" + "=" * 78)
    print("LOG-LOG SLOPE of theta_mean(n)=w/n vs n over the large-n tail")
    print("=" * 78)
    import math
    tail = [r for r in rows if r[1] is not None and r[0] >= 512]
    # least-squares fit of log(theta) = a + b*log(n)
    def linfit(xs, ys):
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / \
            sum((x - mx) ** 2 for x in xs)
        a = my - b * mx
        return a, b
    xs = [math.log(n) for n, w in tail]
    ys = [math.log(w / n) for n, w in tail]
    a, b = linfit(xs, ys)
    print("  tail n>=512, theta=w/n:")
    for n, w in tail:
        print(f"    n={n:>6} theta={w / n:.6f}")
    print(f"  log(theta) = {a:.4f} + ({b:.4f})*log(n)")
    print(f"  -> theta_mean(n) ~ C * n^{b:.4f}  (slope {b:.4f})")
    print(f"  slope < 0 => theta -> 0 (tends-to-zero); slope == 0 => plateau")
    print("  Behaviour on measured range:", "TENDS TO 0" if b < -0.2 else "WEAK/PLATEAU")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  PART 1 (P formula agree): {'PASS' if ok1 else 'FAIL'}")
    print(f"  PART 2 (mean vs brute):   {'PASS' if ok2 else 'FAIL'}")
    print(f"  cross-check overall:      {'PASS' if (ok1 and ok2) else 'FAIL'}")
    print("  theta_mean(n)/n column to n=32768 (exact, direct odd-count route):")
    for n, w in rows:
        print(f"    n={n:>6}  {w / n:.6f}")
    print("  This is exact, so theta_mean(n)/n is a proved value for each n;")
    print("  the LIMIT (tends-to-0 vs plateau) is inferred from the slope, data")
    print("  not a proof.")


if __name__ == "__main__":
    main()
