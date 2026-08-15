#!/usr/bin/env python3
"""Diagnostic: run the corrected sweep logic inline (no file modification),
streaming per-row timing, to find the cost driver. Imports the same lib."""
import math, time, sys
import sympy as sp
from lib.torus_minsep import (corrected_separation_graph,
                              row_kernel_generators)
from lib.satcolor import is_k_colorable

Lv = sp.Rational(2, 5)


def sweep_rows(D):
    rows = []
    for p in range(1, D):
        for q in range(-D, D + 1):
            if math.gcd(p, q, D) == 1:
                rows.append((p, q))
    return rows


for Dv in [7, 13]:
    rows = sweep_rows(Dv)
    print(f"=== D={Dv}: {len(rows)} rows ===", flush=True)
    t_graph = 0.0
    t_sat = 0.0
    n_sat6 = 0
    dense = 0
    kc = 0
    for (p, q) in rows:
        g1, g2 = row_kernel_generators(p, q, Dv)
        t0 = time.time()
        n, edges, reps = corrected_separation_graph(g1, g2, Dv, Lv)
        t_graph += time.time() - t0
        t0 = time.time()
        sat6, w6 = is_k_colorable(edges, 6, n)
        t_sat += time.time() - t0
        if sat6:
            n_sat6 += 1
        if len(edges) == Dv * (Dv - 1) // 2:
            dense += 1
        if (Dv, p, q) == (7, 3, -1):
            kc = (n, len(edges))
        print(f"  D={Dv} row=({p},{q}): {len(edges)} edges, 6col={sat6} "
              f"[graph {time.time()-t0+ (0)}]", flush=True)
    print(f"  D={Dv}: graph={t_graph:.2f}s sat={t_sat:.2f}s "
          f"6col rows={n_sat6} dense rows={dense}")
    if Dv == 7:
        print(f"  canonical row (3,-1): n,edges={kc}", flush=True)
