#!/usr/bin/env python3
"""Hand-style verification of the two n=8 witness pairs, using ONLY the literal
submask-XOR definition (t_direct) - no SOS. Pins which pair witnesses which
definition of the budget (single C_K vs cumulative C_1..C_K).

Pair A (REOPENED witness): h = 00000010, h' = 00000100
   equal C_1 (2-gram hist), S^2 = 0 vs 4  -> witnesses CUMULATIVE K>=1
Pair B (find_counterexample output): h = 01110111, h' = 10111011
   equal C_4 (5-gram hist) but DIFFERENT C_1 -> witnesses SINGLE-C_4 only,
   NOT cumulative (they differ on C_1).

Both computed with the literal oracle so no transform is trusted.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos, t_direct
from itertools import product


def hist(h, L):
    n = len(h)
    cnt = {}
    for p in range(n - L + 1):
        w = 0
        for b in range(L):
            w = (w << 1) | h[p + b]
        cnt[w] = cnt.get(w, 0) + 1
    return dict(sorted(cnt.items()))


def fold_cells(n, h):
    return [t_direct(n, d, list(h)) for d in range(2, n)]


def report(n, h, hp, lab):
    S, ones = s_sos(n, list(h))
    Sp, onesp = s_sos(n, list(hp))
    cells = fold_cells(n, h)
    cellsp = fold_cells(n, hp)
    print(f"--- {lab} ---")
    print(f"h  = {''.join(map(str,h))}  cells(d=2..{n-1})={cells}  "
          f"tot={sum(cells)}  S={S}  S^2={S*S}")
    print(f"h' = {''.join(map(str,hp))}  cells(d=2..{n-1})={cellsp}  "
          f"tot={sum(cellsp)}  S={Sp}  S^2={Sp*Sp}")
    for L in range(2, n):
        same = hist(h, L) == hist(hp, L)
        print(f"  same C_{L-1} ({L}-gram hist): {same}  "
              f"{hist(h,L)}  vs  {hist(hp,L)}")
    print(f"  S^2 differ: {S*S != Sp*Sp}\n")


n = 8
# Pair A: REOPENED
hA = [0, 0, 0, 0, 0, 0, 1, 0]
hAp = [0, 0, 0, 0, 0, 1, 0, 0]
report(n, hA, hAp, "Pair A (REOPENED)")

# Pair B: find_counterexample
hB = [0, 1, 1, 1, 0, 1, 1, 1]
hBp = [1, 0, 1, 1, 1, 0, 1, 1]
report(n, hB, hBp, "Pair B (find_counterexample model)")
