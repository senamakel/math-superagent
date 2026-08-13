#!/usr/bin/env python3
"""Scan all 8 (sigma, eta, theta) sign variants of the tangency residue on
(16,5,5,6), reusing the exact machinery of tangency_G20.py, to identify which
triple gives g=9.  The claim doc attributes 9 to (-1,-1,-1) but the saved
4-variant output (header '+ r*gamma', theta fixed +1) shows (sig,eta)=(-1,-1):
9 — these may disagree under the residue formula
Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma, so the winner must be
established empirically before the G(20) run.
"""
import sys
import time

import tangency_G20 as T


def scan_variant(c, s, p, q, sig, eta, theta):
    """Set variant globals and run the standard block; returns g set."""
    T.SIG, T.ETA, T.THETA = sig, eta, theta
    lines = []
    t0 = time.time()
    all_d = T.tuple_block(c, s, p, q, lambda s_: lines.append(s_))
    el = time.time() - t0
    return all_d, el, lines


def main():
    c, s, p, q = 16, 5, 5, 6
    print("(c,s,p,q) = (%d,%d,%d,%d); residue Q = sigma*rho*(beta-gamma)"
          " - eta*R*beta + theta*r*gamma (mod 1)" % (c, s, p, q))
    print("%3s %3s %3s : %3s   %s" % ("sig", "eta", "th", "g", "d values"))
    results = []
    for sig in (-1, 1):
        for eta in (-1, 1):
            for theta in (-1, 1):
                all_d, el, _ = scan_variant(c, s, p, q, sig, eta, theta)
                ds = sorted(float(d) for d in all_d)
                results.append((sig, eta, theta, len(all_d), ds, el))
    for (sig, eta, theta, g_, ds, el) in results:
        print("%+3d %+3d %+3d : %3d   %s   (%.1f s)"
              % (sig, eta, theta, g_,
                 " ".join("%.12f" % d for d in ds), el))
    winners = [r for r in results if r[3] == 9]
    print("")
    print("variants with g=9: %s" % [(r[0], r[1], r[2]) for r in winners])


if __name__ == "__main__":
    main()