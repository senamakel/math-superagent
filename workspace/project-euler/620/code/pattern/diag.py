"""Diagnostic: for each valid d root (integer crossing of f=Qp-Qq), inspect
the residues to find which additional condition removes overcounted roots.
Goal: G(20)=205 (currently 213), i.e. 8 roots to exclude across 22 pairs.
"""
from mpmath import mp, mpf, pi, atan2, sqrt, floor, ceil

mp.dps = 60


def geometry(c, s, t, d):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(t) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    y = sqrt(y2)
    return x, y


def B_G_turns(c, s, t, d):
    g = geometry(c, s, t, d)
    if g is None:
        return None
    x, y = g
    B = atan2(y, x) / (2 * pi)
    G = atan2(y, x - d) / (2 * pi)
    return B, G


def Q_t(c, s, t, d):
    bg = B_G_turns(c, s, t, d)
    if bg is None:
        return None
    B, G = bg
    return (c - t) * B + (s + t) * G


def match_near(v, denoms):
    """distance of v mod 1 to nearest 0."""
    x = v % 1
    return min(x, 1 - x)


def bounds(c, s, p, q):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    lo, hi = [], []
    for t in (p, q):
        rho = mpf(t) / (2 * pi)
        a, b = R - rho, r + rho
        lo.append(abs(a - b))
        hi.append(a + b)
    return max(lo), min(hi + [R - r - 1])


def all_roots(c, s, p, q):
    """All integer crossings of f=Qp-Qq on (DL,DU), returned as
    (d, m, qp, qq, Bp, Gp, Bq, Gq)."""
    DL, DU = bounds(c, s, p, q)
    if DL >= DU:
        return []
    eps = (DU - DL) / 50000
    ds = [DL + eps + (DU - DL - 2 * eps) * mpf(i) / 1000 for i in range(1001)]
    f0 = f1 = None
    for d in ds:
        a = Q_t(c, s, p, d)
        b = Q_t(c, s, q, d)
        if a is None or b is None:
            continue
        if f0 is None:
            f0 = a - b
        f1 = a - b
    mmin = int(floor(f0)) + 1
    mmax = int(ceil(f1)) - 1
    roots = []
    for m in range(mmin, mmax + 1):
        lo, hi = DL, DU
        flo = f0 - m
        for _ in range(250):
            mid = (lo + hi) / 2
            a = Q_t(c, s, p, mid)
            b = Q_t(c, s, q, mid)
            if a is None or b is None:
                break
            fm = a - b - m
            if fm == 0:
                break
            if (flo < 0) != (fm < 0):
                hi = mid
            else:
                lo = mid
        d = (lo + hi) / 2
        qp = Q_t(c, s, p, d)
        qq = Q_t(c, s, q, d)
        Bp, Gp = B_G_turns(c, s, p, d)
        Bq, Gq = B_G_turns(c, s, q, d)
        roots.append((d, m, qp, qq, Bp, Gp, Bq, Gq))
    return roots


def per_pair(c, s, p, q):
    roots = all_roots(c, s, p, q)
    lines = []
    for (d, m, qp, qq, Bp, Gp, Bq, Gq) in roots:
        q4p = match_near(4 * qp, 4)
        q4q = match_near(4 * qq, 4)
        # planet self-consistency t*(B-G)
        tp = p * (Bp - Gp)
        tq = q * (Bq - Gq)
        ptp = match_near(tp, 1)
        ptq = match_near(tq, 1)
        # sun-terms and ring-terms mod 1
        sp = match_near((s + p) * Gp, 1)
        cp = match_near((c - p) * Bp, 1)
        lines.append(dict(d=float(d), m=int(m), q4p=float(q4p), q4q=float(q4q),
                          ptp=float(ptp), ptq=float(ptq), sp=float(sp),
                          cp=float(cp)))
    return roots, lines


def main():
    pairs = [(16,5,5,6)]
    pairs += [(17,5,5,7),(18,5,5,8),(19,5,5,9),(20,5,5,10),
              (18,5,6,7),(19,5,6,8),(20,5,6,9),(20,5,7,8),
              (17,6,5,6),(18,6,5,7),(19,6,5,8),(20,6,5,9),
              (19,6,6,7),(20,6,6,8),(18,7,5,6),(19,7,5,7),
              (20,7,5,8),(20,7,6,7),(19,8,5,6),(20,8,5,7),
              (20,9,5,6)]
    print("pair        g  q4p(max,min)  q4q  ptp  ptq  sp  cp")
    for (c, s, p, q) in pairs:
        roots, lines = per_pair(c, s, p, q)
        g = len(lines)
        if not lines:
            print("(%2d,%2d,%2d,%2d) g=%d" % (c, s, p, q, g))
            continue
        acc = {}
        for k in ('q4p','q4q','ptp','ptq','sp','cp'):
            vals = [abs(l[k]) for l in lines]
            acc[k] = (max(vals), min(vals))
        print("(%2d,%2d,%2d,%2d) g=%d  q4p=(%+.4f,%+.4f) q4q=(%+.4f,%+.4f) "
              "ptp=(%+.4f,%+.4f) ptq=(%+.4f,%+.4f) sp=(%+.4f) cp=(%+.4f)"
              % (c, s, p, q, g,
                 acc['q4p'][0], acc['q4p'][1], acc['q4q'][0], acc['q4q'][1],
                 acc['ptp'][0], acc['ptp'][1], acc['ptq'][0], acc['ptq'][1],
                 acc['sp'][0], acc['cp'][0]))
    print("\nDetail for (16,5,5,6):")
    for (c, s, p, q) in [(16,5,5,6)]:
        roots, lines = per_pair(c, s, p, q)
        for l in lines:
            print("  m=%+d d=%.10f q4p=%.2e q4q=%.2e ptp=%.2e ptq=%.2e "
                  "sp=%.2e cp=%.2e"
                  % (l['m'], l['d'], l['q4p'], l['q4q'], l['ptp'], l['ptq'],
                     l['sp'], l['cp']))


if __name__ == "__main__":
    main()