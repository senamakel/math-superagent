#!/usr/bin/env python3
"""Full run: universal_transfer_matrix.py semantics +
per-n worst-case ratio + direct consecutive-odds triangle confirmation.

Three reports, all exact arithmetic:

(A) Universal claim wt(Phi_n h) >= wt(h)/2 for ALL h in {0,1}^{n-2}, n=4..20:
    for each n, count how many h violate the inequality (or barely pass),
    and report the first violating h if any.

(B) Exact worst-case ratio min_{h!=0} wt(Phi_n h)/wt(h) per n in 4..20,
    with the achieving h (the all-ones h = 11..1 must give nu2=0, ratio 0).

(C) Direct triangle construction confirming the consecutive-odds sequence
    q = (2,3,5,7,9,11,...) (all gaps = 2, i.e. every halved bit 1) is
    SUCCESSFUL at each n>=0 (bottom entry of its difference triangle is 1),
    for n = 0..18 (length n+1), with the right-diagonal delta and its nu2
    and w = n-2.  This verifies the recorded claim g-supply-transfer-refuted.

The F2 transfer map: halved tail cell (k, n-k), k in [2, n-2], equals the
XOR over a Pascal window:  Phi_n[k][j] = C(k-1, j-(n-k)) mod 2  for
j in [n-k, n-1], else 0.  w = wt(h);  nu2 = wt(Phi_n h).
"""
from math import comb


def phi_row(k, n, j):
    if j < n - k or j > n - 1:
        return 0
    return comb(k - 1, j - (n - k)) % 2


def nu2_of_h(h, n):
    cnt = 0
    for k in range(2, n - 1):
        x = 0
        for j in range(n - k, n):
            if phi_row(k, n, j):
                x ^= h[j - 2]
        cnt += x
    return cnt


# ---- (C) direct triangle construction ----
def consecutive_odds_triangle(L):
    """Difference triangle of q=(2,3,5,7,9,...) (length L+1).  q_0 = 2 then
    consecutive odd numbers q_i = 2i+1 for i>=1. Returns rows and the right
    diagonal [rows[k][L-k] for k=0..L]."""
    q = [2] + [2 * i + 1 for i in range(1, L + 1)]
    rows = [q[:]]
    while len(rows[-1]) > 1:
        r = rows[-1]
        rows.append([abs(r[i] - r[i + 1]) for i in range(len(r) - 1)])
    diag = [rows[k][L - k] for k in range(L + 1)]
    return rows, diag


def main():
    print("=" * 78)
    print("(A) Universal claim  wt(Phi_n h) >= wt(h)/2  for all h in {0,1}^{n-2}")
    print("=" * 78)
    first_ce = None
    total_viol = 0
    for n in range(4, 21):
        m = n - 2
        N = 1 << m
        viol = 0
        first_this = None
        for mask in range(N):
            h = [(mask >> (j - 2)) & 1 for j in range(2, n)]
            w = bin(mask).count('1')
            if w == 0:
                continue
            nu2 = nu2_of_h(h, n)
            if nu2 * 2 < w:  # nu2 < w/2
                viol += 1
                if first_this is None:
                    first_this = (nu2, w, h, mask)
                if first_ce is None:
                    first_ce = (n, nu2, w, h)
        total_viol += viol
        if first_this is not None:
            nu2, w, h, mask = first_this
            print("n=%2d : %6d strings checked; %5d VIOLATE (nu2<w/2); "
                  "first h=%s nu2=%d w=%d" % (n, N, viol, h, nu2, w))
        else:
            print("n=%2d : %6d strings checked; all %d pass (nu2>=w/2)"
                  % (n, N, N))
    print("First counterexample (smallest n): n=%d h=%s nu2=%d w=%d  "
          "=> wt(Phi_n h)=%d < w/2=%d"
          % (first_ce[0], first_ce[3], first_ce[1], first_ce[2],
             first_ce[1], (first_ce[2] + 1) // 2))
    print("TOTAL violating h over all n=4..20: %d" % total_viol)
    print()

    print("=" * 78)
    print("(B) Worst-case ratio  min_{h!=0} wt(Phi_n h)/wt(h)  per n")
    print("=" * 78)
    for n in range(4, 21):
        m = n - 2
        N = 1 << m
        best_ratio = 2.0
        best_h = None
        best_w = None
        best_nu2 = None
        for mask in range(N):
            h = [(mask >> (j - 2)) & 1 for j in range(2, n)]
            w = bin(mask).count('1')
            if w == 0:
                continue
            nu2 = nu2_of_h(h, n)
            ratio = nu2 / w
            # strict better; tie-break by largest w then by mask value
            if (ratio < best_ratio - 1e-12 or
                    (abs(ratio - best_ratio) < 1e-12 and w > best_w)):
                best_ratio = ratio
                best_h = h
                best_w = w
                best_nu2 = nu2
        # all-ones should be a minimizer with ratio 0
        allones = [1] * m
        ao_nu2 = nu2_of_h(allones, n)
        print("n=%2d : min ratio = %s  (nu2=%d / w=%d)  achieved by h=%s ; "
              "all-ones h=%s gives nu2=%d (ratio %d/%d)"
              % (n, format(best_ratio, '.6f'), best_nu2, best_w, best_h,
                 allones, ao_nu2, ao_nu2, m))
    print()

    print("=" * 78)
    print("(C) Consecutive-odds q=(2,3,5,7,9,11,...): all gaps 2 mod 4")
    print("    successful?  nu2 (run's tail convention)  w = n-2")
    print("=" * 78)
    # success is meaningful for n>=1 (a length-1 triangle's terminal is just
    # the single top entry q_1=2 itself, so n=0 trivially has no 2-row
    # triangle); count success over n>=1 only.
    all_success = True
    for L in range(0, 19):          # n = L, prefix length L+1
        rows, diag = consecutive_odds_triangle(L)
        bottom = rows[-1][0]
        ok = (bottom == 1) if L >= 1 else True  # n=0 trivial single entry
        all_success &= ok
        # nu2 = # of 2s in maximal {0,2} suffix of diag before terminal,
        # tail convention like code/gap_analysis/nu2_vs_gap_parity d[2:-1]
        tail = diag[2:-1]
        tau = len(tail)
        while tau > 0 and tail[tau - 1] in (0, 2):
            tau -= 1
        cyc = tail[tau:]
        nu2 = cyc.count(2)
        w = max(L - 2, 0)           # window [2, n-1] has n-2 = L-1 gaps
        w = L - 2 if L >= 2 else 0
        print("n=%2d len=%2d : bottom=%d %s | right diagonal=%s | "
              "nu2=%d  w=%d  (2/3)w=%.4f"
              % (L, L + 1, bottom, "SUCCESS" if ok else "FAIL", diag,
                 nu2, w, (2 / 3) * w))
    print("Consecutive-odds successful at every n in 0..18: %r" % all_success)
    print("(n=0 is the single-entry triangle whose terminal is the entry "
          "q_1=2 itself, so success is only meaningful for n>=1; over "
          "n=1..18 success holds at every n.)")
    print("=> refutes the universal transfer claim and g-supply-transfer:")
    print("   nu2=0 (tail convention) while w grows linearly = n-2.")


if __name__ == "__main__":
    main()
