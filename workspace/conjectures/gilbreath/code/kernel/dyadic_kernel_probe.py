#!/usr/bin/env python3
"""DPC-kernel-classification feasibility probe (Directive 57 DPC-kernel-classification).

Question: is min wt(Phi_n h)/m over balanced, anti-dyadic h bounded away from 0
as m grows, or does it decay?  This is the falsifier for the quantitative converse
of the dyadic collapse: "the only h with sublinear fold weight are those close to
a 2^k-periodic string."

Conventions (locked against code/gap_analysis/linearization_verify.py,
code/refute/kernel_characterize.py, code/refute/universal_transfer_matrix.py):

  * n = m + 2;  the F2 transfer matrix Phi_n has
        rows  k = 2..n-2   (tail cells of the right diagonal)
        cols  j = 2..n-1   (row-1 halved gap bits, m = n-2 of them)
        entry (k,j) = [ C(k-1, j-(n-k)) mod 2 ]  if j in [n-k, n-1] else 0.
  * nu2 = wt(Phi_n h) = number of tail rows whose Pascal-window XOR of h = 1.
    This is the SAME matrix convention the DPC-kernel-classification lemma is
    stated in (kernel = span(all-ones): h = 111.., consecutive odds, gives 0).
    Cross-checked against the DIRECT triangle maximal-{0,2}-suffix count of 2s
    of diag(n) on random small h (60 cases, 0 mismatches) and all-ones h (0/0).
  * h[j] = (A_1[j]//2) mod 2, j in [2,n-1]; h=1 -> gap 2 (==2 mod 4), h=0 ->
    gap 4.  (The task's "first gap g_1=2 from 2->3" is loose for the primes;
    what Phi_n sees is the row-1 window [2,n-1], i.e. the odd gaps, which are
    2/4 here — exactly the 2-then-odd input and the mod-4 switch bit.)

Probe (per m in {4,6,..,18}, exact integers, all 2^m strings vectorized):
  * survivors =
      (i)  BALANCED: 0.2*m <= wt(h) <= 0.8*m  (both bits present),
      (ii) ANTI-DYADIC:  distance(h, nearest 2^k-periodic string) >= 0.2*m
           for k = 0..4.  (A 2^k-periodic string on length m repeats a block of
           length 2^k; distance via the optimal majority-per-residue assignment.)
  * min ratio = min_{survivors} wt(Phi_n h)/m.
  * report minimizer h (bit string + run-length encoding), its nearest-period
    distance profile, and whether min ratio trends to 0 or stays bounded away.

Complexity: scan is linear in the number of strings (2^m dot products via the
numpy Phi-h matrix), O(m^2 * 2^m) total time for the whole m-range; anti-dyadic
distances are O(m) per string per k via the majority-residue identity.
"""
import numpy as np
from math import comb

MAX_K = 4
MIN_FRAC = 0.2
MODES = [4, 6, 8, 10, 12, 14, 16, 18]


def build_phi_matrix(m):
    """Phi_n as numpy (m-1) x m F2 matrix: rows k=2..n-2, cols j=2..n-1.
    nonzero entries (k,j) = [C(k-1, j-(n-k)) mod 2] for j in [n-k, n-1]."""
    n = m + 2
    rows = []
    colmap = {j: j - 2 for j in range(2, n)}   # h index for col j
    for k in range(2, n - 1):                  # tail rows
        r = np.zeros(m, dtype=np.int64)
        for j in range(n - k, n):
            if j in colmap:
                r[colmap[j]] = comb(k - 1, j - (n - k)) % 2
        rows.append(r)
    return np.array(rows, dtype=np.int64), n


def fold_wt(Phi, H):
    """H: (N,m) int rows of h vectors. Returns (N,) wt(Phi h) via XOR (mod-2 sums)."""
    acc = Phi @ H.T                          # (n-3, N) integer dot products
    return (acc % 2).sum(axis=0)             # count of rows with XOR 1


def periodic_masks(m):
    """For k=0..MAX_K with 2^k <= m/2 (the period block must repeat at least
    TWICE on length m to genuinely constrain — a period >= m  admits every
    string, so those k are degenerate and are dropped), the masks of positions
    grouped by residue mod 2^k: per k a list (one per residue class) of
    index lists."""
    ps = []
    for k in range(MAX_K + 1):
        P = 1 << k
        if P > m // 2:                       # block does not repeat twice
            break
        classes = []
        for r in range(P):
            idx = [j for j in range(m) if j % P == r]
            classes.append(idx)
        ps.append(classes)
    return ps


def anti_dyadic_distance_masks(H, per_classes):
    """For each row of H, min over k of the min Hamming distance to any
    2^k-periodic string.  Optimal distance to period P string = for the string
    giving each residue class the majority bit of that class:
       dist = sum over residues r of (# in that class) - (max(count0,count1)).
    Returns (N,) distances and (N, len(per_classes)) per-k distances."""
    N, m = H.shape
    dist_per_k = np.zeros((N, len(per_classes)), dtype=np.int64)
    for k, classes in enumerate(per_classes):
        P = 1 << k
        d = np.zeros(N, dtype=np.int64)
        for cls in classes:
            col = H[:, cls]                       # (N, len(cls))
            cnt1 = col.sum(axis=1)
            cnt0 = len(cls) - cnt1
            d += len(cls) - np.maximum(cnt0, cnt1)
        dist_per_k[:, k] = d
    best = dist_per_k.min(axis=1)
    return best, dist_per_k


def run_length_encoding(bits):
    if not bits:
        return []
    out = []
    cur = bits[0]
    cnt = 1
    for b in bits[1:]:
        if b == cur:
            cnt += 1
        else:
            out.append((cur, cnt))
            cur, cnt = b, 1
    out.append((cur, cnt))
    return out


def near_short_period(bits, dist_per_k):
    """Report the k achieving the min distance and what fraction that is of m.
    Also total complement distance to all-residue groups bookkeeping."""
    kmin = int(dist_per_k.argmin())
    dmin = int(dist_per_k.min())
    return kmin, dmin


def main():
    import sys
    print("=" * 82)
    print("DPC-kernel-classification feasibility probe: min wt(Phi_n h)/m")
    print("over BALANCED + ANTI-DYADIC h in {0,1}^m, m = %s" % MODES)
    print("conventions: Phi_n rows k=2..n-2 cols j=2..n-1; "
          "nu2 = wt(Phi_n h) [kernel=all-ones]")
    print("balanced: wt(h) in [0.2m, 0.8m];  anti-dyadic: >=0.2m Hamming "
          "from every 2^k-periodic string, k<=%d" % MAX_K)
    print("-" * 82)
    hdr = "%-4s %-8s %-10s %-30s %-30s" % (
        "m", "min/m", "surv/tot", "minimizer h", "dist-per-k (/m)")
    print(hdr)
    print("-" * 82)

    ratios = []
    trend_note = ""
    for m in MODES:
        Phi, n = build_phi_matrix(m)
        N = 1 << m
        # all h rows
        idx = np.arange(N)
        H = ((idx[:, None] >> np.arange(m)[None, ::-1]) & 1).astype(np.int64)
        # H column c (0..m-1) = bit (m-1-c) -> h[0] is the most significant.
        # For reporting we want h[j], j=2..n-1 in j order; revert here:
        Hr = H[:, ::-1].copy()

        wt = Hr.sum(axis=1)
        bal = (wt >= MIN_FRAC * m) & (wt <= (1 - MIN_FRAC) * m)

        per_classes = periodic_masks(m)
        anti, dist_per_k = anti_dyadic_distance_masks(Hr, per_classes)
        anti_ok = anti >= MIN_FRAC * m

        surv = bal & anti_ok
        nsurv = int(surv.sum())

        if nsurv == 0:
            print("%-4d %-8s %-10s %-28s %-14s %s" % (
                m, "NO SURV", "0/%d" % N, "—", "—", "skip"))
            continue

        wts = fold_wt(Phi, Hr)
        s_wts = wts[surv]
        s_idx = np.nonzero(surv)[0]
        pos = s_idx[s_wts.argmin()]
        min_ratio = s_wts.min() / m
        ratios.append((m, min_ratio))
        hmax = list(Hr[pos])
        hstr = "".join(map(str, hmax))
        rl = run_length_encoding(hmax)
        rlstr = "".join("%d^%d " % (b, c) for b, c in rl)
        kmin, dmin = near_short_period(hmax, dist_per_k[pos])
        dpro = "/".join("%.2f" % (dist_per_k[pos][kk] / m)
                        for kk in range(len(dist_per_k[pos])))
        print("%-4d %-8.4f %-10s %-30s %-30s" % (
            m, min_ratio, "%d/%d" % (nsurv, N), hstr, dpro))
        if m >= MODES[-1]:
            trend_note = ("  minimizer h=%s rle=[%s]  nearest-period k=%d "
                          "dist=%d/%d (%.3f); per-k dists /m = [%s]"
                          % (hstr, rlstr, kmin, dmin, m, dmin / m,
                             ", ".join("%d" % dist_per_k[pos][kk]
                                       for kk in range(len(dist_per_k[pos])))))
            print("  " + trend_note)

    print("-" * 82)
    print("RATIO TABLE (m -> min wt(Phi h)/m):")
    for m, r in ratios:
        print("  m=%4d  min ratio = %.4f" % (m, r))
    print("-" * 82)

    # verdict: decay vs bounded-away
    if len(ratios) >= 2:
        first = ratios[0][1]
        last = ratios[-1][1]
        # linear regression slop on last half
        ys = [r for _, r in ratios]
        xs = [m for m, _ in ratios]
        if len(ys) >= 2:
            A = np.vstack([np.array(xs, float), np.ones(len(xs))]).T
            coef = np.linalg.lstsq(A, np.array(ys, float), rcond=None)[0]
            slope = coef[0]
        else:
            slope = 0.0
        print("first ratio (m=%d) = %.4f ; last (m=%d) = %.4f ; slope = %.5f"
              % (ratios[0][0], first, ratios[-1][0], last, slope))
        if last > 0.25 and slope > -0.001:
            print("DECISIVE VERDICT: min ratio STAYS BOUNDED AWAY FROM 0 "
                  "(>= %.4f over m<=%d)"
                  % (min(r for _, r in ratios), MODES[-1]))
            print("  -> DPC-kernel-classification numerically ANCHORED: "
                  "balanced & anti-dyadic h never have sublinear fold weight "
                  "at these scales.")
        elif last < 0.15:
            print("DECISIVE VERDICT: min ratio DECAYS toward 0 as m grows "
                  "(%d -> %.4f)" % (ratios[0][0], last))
            print("  -> DPC-kernel-classification FALSE as stated: there are "
                  "balanced anti-dyadic h with small fold weight.")
        else:
            print("DECISIVE VERDICT: INCONCLUSIVE (last=%.4f, slope=%.5f) — "
                  "needs a larger m or a re-stated lemma." % (last, slope))
    print("EXIT_CODE line follows (set by the shell).")
    print("PROBE DONE")


if __name__ == "__main__":
    main()
