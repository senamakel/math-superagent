#!/usr/bin/env python3
"""High-precision scalar evaluation of ratio g(P,alpha)/Eh at specific atoms,
to cross-check the interval enclosure and the numeric global-minimize.  Also
checks the degenerate-atom floor effect."""
import mpmath as mp
mp.mp.dps = 60


def h(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x*mp.log(x)/mp.log(2) - (1-x)*mp.log(1-x)/mp.log(2)


def phi1(p, q):
    return sorted([max(p, q), mp.mpf("0.5"), p + q])[1]


def ratio(a1, a2, b1, b2, t, alpha):
    a = (a1 + a2)/2; b = (b1 + b2)/2
    if not (a <= t < b):
        return None
    beta = (t - a)/(b - a)
    if not (0 <= beta <= 1):
        return None
    wa = (1-beta)/2; wb = beta/2
    vals = [a1, a2, b1, b2]; wts = [wa, wa, wb, wb]
    eh = sum(wts[i]*h(vals[i]) for i in range(4))
    if eh <= 0:
        return None
    e_ind = sum(wts[i]*wts[j]*h(vals[i]+vals[j]-vals[i]*vals[j])
                for i in range(4) for j in range(4))
    e_coup = 2*wa*h(phi1(a1, a2)) + 2*wb*h(phi1(b1, b2))
    g = (1-alpha)*e_ind + alpha*e_coup
    return g/eh


def main():
    # Yu minimizer subfamily: a1=a2=b1=a, b2=1
    for t, a in [(0.380, 0.33917), (0.382, 0.330169), (0.380, 0.3300622),
                 (0.38234, 0.3300622)]:
        r = ratio(a, a, a, 1.0, t, 0.035)
        print(f"t={t} a={a} subfamily(a,a,a,1): ratio={mp.nstr(r,12)}")
    print()
    # the worst cell region (a1~0.66, a2~0.1, b~1) — is that really high?
    r = ratio(mp.mpf("0.66"), mp.mpf("0.10"), mp.mpf("0.998"), mp.mpf("0.998"),
              mp.mpf("0.380"), mp.mpf("0.035"))
    print("worst-cell-like (0.66,0.10,0.998,0.998): ratio=", mp.nstr(r,12))
    # the true inf at t=0.380 alpha 0.035 via the subfamily scan
    best = None; ba = None
    for a in [x/100000 for x in range(30000, 36000, 1)]:
        r = ratio(a, a, a, 1.0, mp.mpf("0.380"), mp.mpf("0.035"))
        if r is not None and (best is None or r < best):
            best = r; ba = a
    print(f"subfamily min at t=0.380: {mp.nstr(best,12)} at a={ba}")

    # Now the FULL 4D - the minimizer may not be subfamily. Try the b2<1 lifted
    # points that true_cross found.  0.38: atom(0.33079,0.33079,0.33079,1.0)
    r = ratio(mp.mpf("0.33079"), mp.mpf("0.33079"), mp.mpf("0.33079"),
              mp.mpf("1.0"), mp.mpf("0.380"), mp.mpf("0.035"))
    print("true_cross 0.38 atom (0.33079,..,1): ratio=", mp.nstr(r,12))


if __name__ == "__main__":
    main()
