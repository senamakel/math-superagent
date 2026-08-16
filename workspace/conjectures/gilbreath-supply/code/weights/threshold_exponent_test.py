#!/usr/bin/env python3
"""Hypothesis test on the exact-mean linear-supply threshold weight.

Steering directive (operator): fit log2(w*) vs log2(n) with an error bar over
the large-n rows, and separately test
    (B) w = c*sqrt(n)          -- if w/sqrt(n) is flat, exponent is exactly 1/2
    (C) w = c*sqrt(n)*log(n)
    (D) w = c*n^(log_4 3)
and say which the data prefers and by how much. Do not declare a closed form
the data cannot separate.

The threshold weights are EXACT (theta_mean from lib.krawtchouk_sphere, the
verified grouped-by-popcount closed form, cross-checked against the literal
brute s_sos oracle digit-for-digit). We extend the exact column to large n --
the cost per (n,w) is O(log n * w) integer ops, trivial -- so the exponent is
fitted over a far longer tail than the prior captures.

All per-n theta values are exact. The exponent and the closed-form comparison
are numerical fits, labelled measurement-not-proof.
"""
from math import log2, sqrt, log
import numpy as np

from lib.krawtchouk_sphere import theta_mean


def compute_column(nmax_k):
    """Exact (n, w*) pairs at n = 2^k .. 2^nm_k and the +1 neighbours."""
    rows = []
    for k in range(6, nmax_k + 1):      # 2^6 = 64 .. 2^nm_k
        n = 1 << k
        w, mean = theta_mean(n)
        rows.append((n, w, mean))
        n1 = n + 1
        w1, mean1 = theta_mean(n1)
        rows.append((n1, w1, mean1))
    return rows


def ols_fit(xs, ys):
    """log-log OLS: ys = a + b*xs. Returns (b, se_b, a, r2)."""
    x = np.array(xs, float)
    y = np.array(ys, float)
    b, a = np.polyfit(x, y, 1)
    yhat = a + b * x
    resid = y - yhat
    n = len(x)
    s2 = resid @ resid / (n - 2)
    xbar = x.mean()
    se_b = sqrt(s2 / ((x - xbar) @ (x - xbar)))
    ss_tot = ((y - y.mean()) ** 2).sum()
    r2 = 1.0 - (resid @ resid) / ss_tot
    return b, se_b, a, r2


def rel_spread(vals):
    """Relative residual std of vals about their mean (for w/sqrt(n) etc)."""
    v = np.array(vals, float)
    return np.std(v) / np.mean(v)


def main():
    nmax_k = 18                      # n up to 2^18 = 262144 (cost ~4x per doubling)
    rows = compute_column(nmax_k)
    # use only exact powers of two for the clean geometric column
    pw = [(n, w) for (n, w, _) in rows if n & (n - 1) == 0]
    # and also keep the +1 row for robustness checks
    pw_plus = [(n, w) for (n, w, _) in rows]

    out = []
    add = out.append
    add("=" * 78)
    add("HYPOTHESIS TEST on exact-mean threshold weight w*(n)")
    add("sequence : weight-w binary strings over F2^n (threshold is "
        "min w with mean nu2/n >= 0.40)")
    add("oracle   : lib.krawtchouk_sphere.theta_mean (exact, grouped-by-popcount,"
        " verified vs literal s_sos brute)")
    add("range    : n = 64 .. 2^%d (exact integer arithmetic)" % nmax_k)
    add("=" * 78)
    add("")
    add("EXACT COLUMN (powers of two):")
    add("   %7s %6s %10s %12s %12s %12s" % ("n", "w*", "w/n", "w/sqrt(n)",
                                            "w/sqrt(n)*1/log n*2", "w/n^log43"))
    B = []; C = []; D = []
    for n, w in pw:
        s = w / sqrt(n)
        c = w / (sqrt(n) * log(n)) * 2e0
        d = w / (n ** (log2(3) - 1))     # n^log_4 3 = n^(log4 3) = n^(0.792)
        B.append(s); C.append(c); D.append(d)
        add("   %7d %6d %10.5f %12.5f %12.5f %12.5f" % (n, w, w / n, s, c, d))
    add("")

    # --- log-log power-law fit ---
    pw_n = [(n, w) for (n, w) in pw if n >= 128]   # drop early transients
    add("=" * 78)
    add("MODEL A: log2(w*) = a + E*log2(n)   (power law w ~ n^E), n>=128")
    add("=" * 78)
    xs = [log2(n) for n, _ in pw_n]
    ys = [log2(w) for _, w in pw_n]
    E, seE, a, r2 = ols_fit(xs, ys)
    add("  E = %.5f  +/-  %.5f   (95%% CI ~ [%.5f, %.5f])" % (
        E, seE, E - 1.96 * seE, E + 1.96 * seE))
    add("  intercept a = %.4f,  R^2 = %.6f,  n_points = %d" % (a, r2, len(pw_n)))
    add("  |E - 0.5000| = %.4f (sqrt law)" % abs(E - 0.5))
    add("  |E - log4(3)=0.7925| = %.4f" % abs(E - (log2(3) - 1)))
    add("  |E - 0.5568 (pass3 fit, n<=32768)| = %.4f" % abs(E - 0.55678))
    add("")
    # local per-doubling slopes
    add("  per-doubling slope d(log2 w)/d(log2 n):")
    last = None
    for n, w in pw:
        if last is not None:
            n0, w0 = last
            sl = (log2(w) - log2(w0)) / (log2(n) - log2(n0))
            add("    n=%7d -> %7d:  slope=%.4f" % (n0, n, sl))
        last = (n, w)
    add("")

    # --- closed-form candidate tests ---
    add("=" * 78)
    add("MODEL B/C/D: candidate closed forms on the EXACT column")
    add("rel-spread = std/mean of w / (candidate normalising factor); flat==>fit")
    add("=" * 78)
    # B: w = c sqrt(n)
    add("  B) w = c*sqrt(n):           w/sqrt(n) rel-spread = %.4f"
        % rel_spread(B))
    # C: w = c sqrt(n) log(n)
    add("  C) w = c*sqrt(n)*log(n):    w/(sqrt(n)log n) rel-spread = %.4f"
        % rel_spread(C))
    # D: w = c n^(log_4 3)
    add("  D) w = c*n^(log_4 3)=n^0.792:w/n^0.792 rel-spread = %.4f"
        % rel_spread(D))
    # tail-only spreads (last 6 powers of two)
    Bt = [w / sqrt(n) for n, w in pw[-6:]]
    Ct = [w / (sqrt(n) * log(n)) for n, w in pw[-6:]]
    Dt = [w / (n ** (log2(3) - 1)) for n, w in pw[-6:]]
    add("  tail-only (last 6 powers):  B %.4f   C %.4f   D %.4f"
        % (rel_spread(Bt), rel_spread(Ct), rel_spread(Dt)))
    add("")
    add("  NOTE: D uses exponent 0.7925 (n^log_4 3); pass3 already ruled it out")
    add("  (spread 0.83). Included for completeness against the directive.")
    add("")
    add("VERDICT: labelled inference, not a proof. state which candidate the")
    add("data can separate and by how much.")
    text = "\n".join(out)
    print(text)


if __name__ == "__main__":
    main()
