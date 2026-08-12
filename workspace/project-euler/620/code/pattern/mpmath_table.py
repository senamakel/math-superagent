"""Lift seqgen's float counts to an mpmath-verified table c<=38.

For every tuple, bisect each integer level of n_p with mpmath (binary search
on d to 40 digits), requiring the root to be strictly interior and both
planet positions non-degenerate (y_p,y_q > 1e-7).  This is the ground truth
the float generator is checked against.  Emits only rows where the float
and mpmath counts disagree, plus a final agreement summary, and writes the
full mpmath table to code/out/mpmath_table.txt.
"""
from mpmath import mp, mpf, pi, atan2, sqrt
import os

mp.dps = 40
OUT = "/workspace/code/out/mpmath_table.txt"


def g_mp(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)

    def geom(t, d):
        rho = mpf(t) / (2 * pi)
        a = R - rho
        b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        y2 = a * a - x * x
        if y2 <= 0:
            return None
        return a, b, x, sqrt(y2)

    def n_t(t, d):
        g = geom(t, d)
        if g is None:
            return None
        a, b, x, y = g
        beta = atan2(y, x)
        gamma = atan2(y, x - d)
        return ((c - t) * beta + (s + t) * gamma) / pi

    # bounds (mpmath-exact)
    lowers, uppers = [], []
    for t in (p, q):
        rho = mpf(t) / (2 * pi)
        a, b = R - rho, r + rho
        lowers.append(abs(a - b))
        uppers.append(a + b)
    DL = max(lowers)
    DU = min(uppers + [R - r - 1])
    if DL >= DU:
        return 0, (DL, DU)
    eps = (DU - DL) / mpf(10 ** 6)
    lo0, hi0 = DL + eps, DU - eps
    nlo = n_t(p, lo0)
    nhi = n_t(p, hi0)
    if nlo is None or nhi is None or nlo > nhi:
        return 0, (DL, DU)
    kmin = int(mp.ceil(nlo))
    kmax = int(mp.floor(nhi))
    cnt = 0
    for k in range(kmin, kmax + 1):
        a, b = lo0, hi0
        fa = n_t(p, a) - k
        fb = n_t(p, b) - k
        if fa * fb > 0:
            continue
        for _ in range(250):
            m = (a + b) / 2
            fm = n_t(p, m) - k
            if fa * fm <= 0:
                b, fb = m, fm
            else:
                a, fa = m, fm
        d = (a + b) / 2
        yp = geom(p, d)[3]
        yq = geom(q, d)[3]
        if d > DL and d < DU and yp > mpf('1e-7') and yq > mpf('1e-7'):
            cnt += 1
    return cnt, (DL, DU)


def main():
    rows = []
    for c in range(16, 39):
        for s in range(5, c - 10):
            for p in range(5, (c - s - 1) // 2 + 1):
                q = c - s - p
                g, _ = g_mp(c, s, p, q)
                rows.append((c, s, p, q, g))
    with open(OUT, "w") as f:
        for r_ in rows:
            f.write("%d %d %d %d %d\n" % r_)
    print("wrote %d rows to %s" % (len(rows), OUT))

    # compare to seqgen rows (float) from its output file
    seq = {}
    sg = "/workspace/code/out/seqgen.txt"
    if os.path.exists(sg):
        for line in open(sg):
            parts = line.split()
            if len(parts) == 5 and parts[0].isdigit():
                c, s, p, q, g = map(int, parts)
                seq[(c, s, p, q)] = g
    disagree = []
    for c, s, p, q, g in rows:
        if (c, s, p, q) in seq and seq[(c, s, p, q)] != g:
            disagree.append((c, s, p, q, seq[(c, s, p, q)], g))
    print("disagreements float-vs-mpmath: %d" % len(disagree))
    for d_ in disagree:
        print("  c,s,p,q=%s seqgen=%d mpmath=%d" % (d_[:4], d_[4], d_[5]))


if __name__ == "__main__":
    main()