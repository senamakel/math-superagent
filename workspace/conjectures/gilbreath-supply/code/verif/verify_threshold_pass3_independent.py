#!/usr/bin/env python3
"""TOTALLY independent second-route verification of the numerical claims in
code/out/linear_supply_threshold_pass3.txt.

Routes used (deliberately different code from both lib.threshold_exponent and
lib.krawtchouk_sphere):

  (1) exact-mean P_d(w) = P(XOR of a fixed k-set is odd over weight-w strings)
      computed by TWO independent closed forms (both exact integer arithmetic):
        (a) direct hypergeometric odd sum   sum_{r odd} C(k,r) C(n-k,w-r)
        (b) generating-function coefficient (C(n,w) - c_w)/(2 C(n,w)),
            c_w = [z^w](1-z)^k (1+z)^{n-k}  =  sum_j (-1)^j C(k,j) C(n-k,w-j)
      These are provably equal (even+odd=C(n,w), even-odd=c_w), but coded
      separately so agreement is a genuine check.
      mean_n(w) = (1/n) sum_{p} N_p P_{k_p}(w), N_p = #{d in [2,n-1]: pc(d)=p}.
      The expensive literal product-polynomial build of (1-z)^k(1+z)^{n-k}
      is used only as a third route on a few small (n,k,w) sanity points.

  (2) least-squares slope of log2(w) vs log2(n) over n>=128, n>=256, n>=512,
      n>=2048 (regression with intercept b = sxy/sxx).

  (3) relative spread of w/n^a over n=128..4096 for a in {0.50,0.55,0.7925},
      relative spread = (max-min)/(mean).

No capture file is written; numbers are printed only.
"""

import math
from math import comb

# ------------------------- exact P_d(w) routes -----------------------------


def P_oddsum(n, k, w):
    """sum_{r odd} C(k,r) C(n-k,w-r)  /  C(n,w)  (direct hypergeometric)."""
    lo = max(0, w - (n - k))
    hi = min(k, w)
    s = 0
    for r in range(lo, hi + 1):
        if r & 1:
            s += comb(k, r) * comb(n - k, w - r)
    return s / comb(n, w)


def P_genfunc(n, k, w):
    """(C(n,w) - c_w) / (2 C(n,w)), c_w = sum_j (-1)^j C(k,j) C(n-k,w-j)."""
    lo = max(0, w - (n - k))
    hi = min(k, w)
    c = 0
    for j in range(lo, hi + 1):
        term = comb(k, j) * comb(n - k, w - j)
        c += -term if (j & 1) else term
    C = comb(n, w)
    return (C - c) / (2 * C)


def P_product(n, k, w):
    """Literal build of (1-z)^k (1+z)^{n-k} & read coefficient (slow, sanity
    only)."""
    poly = [1]
    for _ in range(k):
        new = [0] * (len(poly) + 1)
        for i, v in enumerate(poly):
            new[i] += v
            new[i + 1] -= v
        poly = new
    for _ in range(n - k):
        new = [0] * (len(poly) + 1)
        for i, v in enumerate(poly):
            new[i] += v
            new[i + 1] += v
        poly = new
    C = comb(n, w)
    return (C - poly[w]) / (2 * C)


def popcount_distribution(n):
    c = {}
    for d in range(2, n):
        p = bin(d).count("1")
        c[p] = c.get(p, 0) + 1
    return c


def mean_weight(n, w, Np, route):
    tot = 0.0
    for p, cnt in Np.items():
        k = 1 << p
        if route == "odd":
            tot += cnt * P_oddsum(n, k, w)
        elif route == "gf":
            tot += cnt * P_genfunc(n, k, w)
        else:
            tot += cnt * P_product(n, k, w)
    return tot / n


def find_first_w(n, Np, thr=0.40, route="gf"):
    for w in range(1, n):
        if mean_weight(n, w, Np, route) >= thr:
            return w
    return None


def linfit_loglog(points, base):
    xs = [math.log(float(n), base) for n, _ in points]
    ys = [math.log(float(w), base) for _, w in points]
    k = len(points)
    if k < 2:
        return float('nan'), float('nan')
    mx = sum(xs) / k
    my = sum(ys) / k
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    sse = sum((y - my - b * (x - mx)) ** 2 for x, y in zip(xs, ys))
    se = math.sqrt(sse / sxx / (k - 2)) if k > 2 else float('nan')
    return b, se


def rel_spread(vals):
    m = sum(vals) / len(vals)
    return (max(vals) - min(vals)) / m


def main():
    DATA = [  # (n, w) exact-mean first_w from linear_supply_threshold_pass3.txt
        (8, 3), (10, 3), (12, 3), (14, 4), (16, 3),
        (32, 5), (64, 7), (128, 11), (256, 16), (512, 24),
        (1024, 35), (2048, 52), (4096, 77),
    ]

    print("=" * 74)
    print("PASS-3 EXACT-MEAN THRESHOLD -- INDEPENDENT SECOND-ROUTE CHECK")
    print("=" * 74)

    # ---- tiny cross-check: three independent P_d routes agree ----
    print("\nSTAKE sanity -- P_d(w) via odd-sum vs genfunc vs literal product:")
    for n, k, w in [(8, 2, 3), (8, 4, 3), (10, 2, 2), (12, 8, 4), (16, 4, 5),
                    (20, 2, 4), (64, 2, 7), (64, 8, 7)]:
        a = P_oddsum(n, k, w)
        b = P_genfunc(n, k, w)
        c = P_product(n, k, w)
        ok = abs(a - b) < 1e-12 and abs(a - c) < 1e-12
        print("  (n=%3d k=%2d w=%2d) odd=%.6f gf=%.6f prod=%.6f %s"
              % (n, k, w, a, b, c, "OK" if ok else "MISMATCH"))

    # ---- PART A: independently recompute first_w ----
    print("\nPART A -- independently recomputed first_w (mean>=0.40):")
    all_rows = []
    for n, wfile in DATA:
        Np = popcount_distribution(n)
        # odd route first, then recheck the crossing with genfunc
        w_odd = find_first_w(n, Np, thr=0.40, route="odd")
        w_gf = find_first_w(n, Np, thr=0.40, route="gf")
        all_rows.append((n, w_odd))
        tag = "OK" if (w_odd == wfile and w_gf == wfile) else "MISMATCH"
        print("  n=%5d  file_w=%3d  mine(odd)=%3d  mine(gf)=%3d  %s"
              % (n, wfile, w_odd, w_gf, tag))

    # ---- PART B: exact check at n=64, w=7 ----
    print("\nPART B -- exact check at n=64, w=7 (claimed mean ~0.4124):")
    n, w = 64, 7
    Np = popcount_distribution(n)
    m_gf = mean_weight(n, w, Np, "gf")
    m_odd = mean_weight(n, w, Np, "odd")
    print("  E[nu2/n] via genfunc = %.6f" % m_gf)
    print("  E[nu2/n] via odd-sum = %.6f" % m_odd)
    print("  |mean - 0.4124| = %.6f ; routes agree: %s"
          % (abs(m_gf - 0.4124), abs(m_gf - m_odd) < 1e-12))
    print("  N_p(n=64):", dict(Np))

    # ---- PART C: least-squares slope log2(w) vs log2(n) ----
    print("\nPART C -- least-squares slope of log2(w) vs log2(n):")
    for lo in [128, 256, 512]:
        pts = [(nn, ww) for nn, ww in all_rows if lo <= nn <= 4096]
        b, se = linfit_loglog(pts, 2)
        print("  n>=%4d : a = %.4f  (se=%.4f, %d pts)" % (lo, b, se, len(pts)))
    pts = [(nn, ww) for nn, ww in all_rows if 2048 <= nn <= 4096]
    b, se = linfit_loglog(pts, 2)
    print("  n>=2048: a = %.4f  (se=%.4f, %d pts)" % (b, se, len(pts)))

    # ---- PART D: relative spread of w/n^a ----
    print("\nPART D -- relative spread of w/n^a over n=128..4096:")
    tail = [(nn, ww) for nn, ww in all_rows if 128 <= nn <= 4096]
    for a in [0.50, 0.55, 0.7925]:
        vals = [ww / (nn ** a) for nn, ww in tail]
        print("  a=%.4f : %s" % (a, ["%.3f" % v for v in vals]))
        print("           rel spread = %.4f" % rel_spread(vals))
    print("\n  smallest rel spread wins (near-constant best exponent).")

    # exact mean values at the crossing for transparency
    print("\nExact crossing means:")
    for n, ww in all_rows:
        Np = popcount_distribution(n)
        print("  n=%5d w=%3d  E[nu2/n]=%.6f" % (n, ww, mean_weight(n, ww, Np, "gf")))


if __name__ == "__main__":
    main()
