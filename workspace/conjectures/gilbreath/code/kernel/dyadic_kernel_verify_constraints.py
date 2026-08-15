#!/usr/bin/env python3
"""Verify the probe's minimizers genuinely satisfy BOTH constraints imposed on
survivors: (i) balanced and (ii) anti-dyadic (>=0.2*m from every genuine
2^k-periodic string, block must repeat twice).  A minimizer that fails a
constraint would not be a valid survivor, so this confirms/however the
counterexamples are legitimate."""
import numpy as np


def periodic_masks(m):
    ps = []
    for k in range(5):
        P = 1 << k
        if P > m // 2:
            break
        classes = [[j for j in range(m) if j % P == r] for r in range(P)]
        ps.append(classes)
    return ps


def dists_to_periodic(h, m, per):
    out = []
    for classes in per:
        d = 0
        for cls in classes:
            cnt1 = sum(h[j] for j in cls)
            cnt0 = len(cls) - cnt1
            d += len(cls) - max(cnt0, cnt1)
        out.append(d)
    return out


def main():
    cases = {
        6: [1, 1, 0, 0, 0, 0],
        8: [1, 1, 0, 0, 0, 0, 0, 0],
        10: [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        12: [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        14: [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        16: [1] * 4 + [0] * 12,
        18: [0, 0, 1, 1, 1, 1] + [0] * 12,
    }
    print("%-4s %-28s %-9s %-10s %-22s %s" % (
        "m", "h", "wt/m", "bal?", "min anti-dist/m", "is-survivor"))
    ok_all = True
    for m, h in sorted(cases.items()):
        wt = sum(h)
        bal = 0.2 * m <= wt <= 0.8 * m
        per = periodic_masks(m)
        ds = dists_to_periodic(h, m, per)
        amin = min(ds)
        is_surv = bal and amin >= 0.2 * m
        ok_all &= is_surv
        print("%-4d %-28s %-9.3f %-10s %-22s %s" % (
            m, "".join(map(str, h)), wt / m, bal,
            "%.2f (%s)" % (amin / m, "/".join(str(d) for d in ds)),
            "YES" if is_surv else "NO"))
    print("ALL ARE GENUINE SURVIVORS:", ok_all)


if __name__ == "__main__":
    main()
