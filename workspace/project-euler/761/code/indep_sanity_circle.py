#!/usr/bin/env python3
"""Coarse sanity check of the circle geometry in indep_game_encoding.py.

Hand-analysis prediction: with stage point S at distance r=1/v at angle
delta from the runner start, the max of runner-dist / swim-dist over
shore points Q(theta) is:
  - delta=pi : max_theta theta/sqrt(1+r^2+2r cos theta) = pi/(1-r)
    (attained at theta=pi), fixed point v = pi+1 ~ 4.14159.
  - delta=0  : max_theta theta/sqrt(1+r^2-2r cos theta) = pi/(1+r)
    fixed point v = pi-1 ~ 2.14159.
So the script's staging model (straight dash from a radially opposite
stage point) tops out at pi+1 and CANNOT reproduce the circle oracle
4.60333885 of the real two-phase (arc-staging + tangent chord) game.
This check duplicates the model with an independent, smaller-grid
implementation before the full run is made.
"""
import math
import numpy as np


def g_circle(v, delta, n_grid=4000):
    P = 2.0 * math.pi
    r = 1.0 / v
    S = (r * math.cos(delta), r * math.sin(delta))
    s = np.linspace(0.0, P, n_grid, endpoint=False)
    best = 0.0
    argmax = 0.0
    for i in range(n_grid):
        ss = s[i]
        qx = math.cos(ss)
        qy = math.sin(ss)
        d_r = min(ss, P - ss)
        d_s = math.hypot(qx - S[0], qy - S[1])
        rat = d_r / d_s
        if rat > best:
            best = rat
            argmax = ss
    return best, argmax


def bisect(delta, iters=30, n_grid=4000):
    lo, hi = 1.0, 30.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        gm, _ = g_circle(mid, delta, n_grid)
        if gm > mid:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


if __name__ == "__main__":
    for delta, lbl in [(0.0, "delta=0  (toward runner start)"),
                       (math.pi, "delta=pi (opposite runner)")]:
        V = bisect(delta)
        pred = math.pi + 1 if delta > 0 else math.pi - 1
        print(f"{lbl}: bisected V = {V:.6f}   hand-prediction = {pred:.6f}")
    print("circle oracle = 4.60333885  |  pi+1 =", round(math.pi + 1, 6))