"""Precise F1 test on the ADMISSIBLE interval, tracking the 0<x<d band."""
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


def test_adv():
    npts = bad_iden = bad_band = band_ok = tot = 0
    worst = 0
    out_of_band_iden_bad = 0
    in_band_tot = 0
    in_band_bad = 0
    for c in range(16, 61):
        for s in range(5, c - 10):
            for p in range(5, c - s - 5):
                for q in range(p + 1, c - s - p + 1):
                    lo, hi = adv_interval(c, s, p, q)
                    if lo >= hi:
                        continue
                    a_p, b_p = radii(c, s, p)
                    for k in range(5):
                        frac = mp.mpf(k) / 4
                        d = lo * (1 - frac) + hi * frac
                        bp, mp_, xp, yp = angles(c, s, p, d)
                        res = abs(n_t(c, s, p, d) + n_t(c, s, q, d) - (c + s))
                        inband = (xp > 0) and (xp < d)
                        tot += 1
                        worst = max(worst, res)
                        if inband:
                            in_band_tot += 1
                            if res > mp.mpf('1e-30'):
                                in_band_bad += 1
                        else:
                            bad_band += 1
                            if res > mp.mpf('1e-30'):
                                out_of_band_iden_bad += 1
    print("admissible-interval points tested: %d" % tot)
    print("  in-band (0<xp<d): %d of which identity-bad: %d" % (in_band_tot, in_band_bad))
    print("  out-of-band:      %d of which identity-bad: %d" % (bad_band, out_of_band_iden_bad))
    print("  worst |residual| anywhere: %s" % mp.nstr(worst, 5))


if __name__ == "__main__":
    test_adv()
