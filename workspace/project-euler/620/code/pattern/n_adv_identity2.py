"""F1 with the correct domain constraint c == s+p+q (as in PE620)."""
import mpmath as mp
mp.mp.dps = 60


def radii(c, s, t):
    pi = mp.pi
    return (c - t) / (2 * pi), (s + t) / (2 * pi)


def angles(c, s, t, d):
    a, b = radii(c, s, t)
    x = (a * a - b * b + d * d) / (2 * d)
    y = mp.sqrt(mp.fabs(a * a - x * x))
    return mp.atan2(y, x), mp.atan2(y, x - d), x, y


def n_t(c, s, t, d):
    beta, mu, _, _ = angles(c, s, t, d)
    return ((c - t) * beta + (s + t) * mu) / mp.pi


def adv_interval(c, s, p, q):
    pi = mp.pi
    a_p, b_p = radii(c, s, p)
    a_q, b_q = radii(c, s, q)
    R = c / (2 * pi); r = s / (2 * pi)
    lo = max(abs(a_p - b_p), abs(a_q - b_q))
    hi = min(a_p + b_p, a_q + b_q, R - r - 1)
    return lo, hi


def test():
    tot = inbad = outbad_tot = outbad = worst = 0
    ntuples = 0
    for c in range(16, 80):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                q = c - s - p          # enforce c == s+p+q
                if q <= p:
                    continue
                ntuples += 1
                lo, hi = adv_interval(c, s, p, q)
                if lo >= hi:
                    continue
                a_p, b_p = radii(c, s, p)
                for k in range(7):
                    frac = mp.mpf(k) / 6
                    d = lo * (1 - frac) + hi * frac  # strictly interior
                    bp, mp_, xp, _ = angles(c, s, p, d)
                    res = abs(n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s))
                    inband = (xp > 0) and (xp < d)
                    tot += 1
                    worst = max(worst, res)
                    if inband:
                        if res > mp.mpf('1e-30'):
                            inbad += 1
                    else:
                        outbad_tot += 1
                        if res > mp.mpf('1e-30'):
                            outbad += 1
    print("tuples (c==s+p+q) tested: %d" % ntuples)
    print("interior points tested: %d" % tot)
    print("  in-band points: identity-bad = %d" % inbad)
    print("  out-of-band points: %d total, identity-bad = %d"
          % (outbad_tot, outbad))
    print("  worst |residual| anywhere: %s" % mp.nstr(worst, 5))


if __name__ == "__main__":
    test()
