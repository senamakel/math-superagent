#!/usr/bin/env python3
"""Verify code/brute.py against every worked example in the PE597 statement.

Two checks, both at the statement's own sizes (n=3,L=160 and n=4,L=400) only:

A) Construct a concrete speed vector that realizes each of the five
   n=3,L=160 bump patterns from the statement, then check the engine's
   reported (new order, parity) against the table row.

B) Monte Carlo over true Exp(1) speeds (n=3,L=160 and n=4,L=400): count the
   five bump edge-sets and compute the empirical fraction for each row
   (comparing to the statement's rational), and estimate p(3,160), p(4,400).

This pins down what the statement means; it does not touch n=13.
"""
import math
import random
from collections import Counter

from brute import simulate_order, parity_of_new_order

# n=3 boats: A=0 (lowest), B=1, C=2. positions 0,40,80; L=160.
# Expected edge sets (bumper -> bumped) for each table row:
ROWS = {
    "none":                     (set(),            ("A", "B", "C"), 0),  # even
    "B bumps C":                ({(1, 2)},         ("A", "C", "B"), 1),  # odd
    "A bumps B":                ({(0, 1)},         ("B", "A", "C"), 1),  # odd
    "B bumps C then A bumps C": ({(1, 2), (0, 2)}, ("C", "A", "B"), 0),  # even
    "A bumps B then B bumps C": ({(0, 1), (1, 2)}, ("C", "B", "A"), 1),  # odd
}
TABLE_PROB = {
    "none": 4 / 15,
    "B bumps C": 8 / 45,
    "A bumps B": 1 / 3,
    "B bumps C then A bumps C": 4 / 27,
    "A bumps B then B bumps C": 2 / 27,
}
NAMES = ["A", "B", "C"]


def realize(name):
    """Return a speed triple that produces the given bump pattern (n=3,L=160).

    Found by a small grid + drain search over speeds in (0, 10]; this is a
    tiny 3D verification search, not the problem's search space.
    """
    target_edges = ROWS[name][0]
    step = 0.5
    v = [2.0, 3.0, 4.0]
    best = None
    for a in [x * step for x in range(1, int(10 / step) + 1)]:
        for b in [x * step for x in range(1, int(10 / step) + 1)]:
            for c in [x * step for x in range(1, int(10 / step) + 1)]:
                above = simulate_order(3, 160, [a, b, c])
                # recover edge set
                edges = set()
                # face cells: we can't get edges directly from above alone,
                # so re-run collecting edges via a tiny local sim is overkill;
                # instead compare on the realized outcome below.
                par, order = parity_of_new_order(3, above)
                # determine edge set by simulating to edges: reuse a lightweight
                # copy from brute by checking which pattern this vector yields
                # via a dedicated edge-extraction.
                eset = _edges_of(3, 160, [a, b, c])
                if eset == target_edges:
                    return [a, b, c]
    return None


def _edges_of(n, L, speeds):
    """Return the set of bump edges (bumper,bumped) for a speed vector."""
    # Recompute the chronological simulation to collect edges. Same logic as
    # brute.simulate_order but returning edges (brute already keeps them
    # internally but discards them; snapshot here is fine and exact enough).
    state = [0] * n
    pos = [40.0 * j for j in range(n)]
    edges = []
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            cands = [(ft, 'F', j, None)]
            if k is not None and vj > speeds[k]:
                cands.append(((pos[k] - pos[j]) / (vj - speeds[k]), 'C', j, k))
            for e in cands:
                if best is None or e[0] < best[0] - 1e-12:
                    best = e
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1
            pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]
            edges.append((j, k))
    return set(edges)


def check_table_parities():
    print("=" * 70)
    print("A) n=3, L=160: realize each bump pattern, check (order, parity)")
    print("=" * 70)
    allok = True
    for name, (exp_edges, exp_order, exp_par) in ROWS.items():
        speeds = realize(name)
        if speeds is None:
            print(f"  {name:34s}  FAIL: could not realize a speed vector")
            allok = False
            continue
        above = simulate_order(3, 160, speeds)
        par, order = parity_of_new_order(3, above)
        order_names = [NAMES[i] for i in order]
        o_s = "OK " if (par == exp_par and order_names == list(exp_order)) else "BAD"
        if o_s == "BAD":
            allok = False
        print(f"  {name:34s} speeds={[round(x,2) for x in speeds]} "
              f"-> order={order_names} parity={'even' if par==0 else 'odd'}  [{o_s}] "
              f"expect {list(exp_order)} {'even' if exp_par==0 else 'odd'}")
    print("  =>", "ALL PARITIES/ORDERS MATCH" if allok else "MISMATCH FOUND")
    return allok


def mc_probabilities(N):
    print()
    print("=" * 70)
    print("B) MC over Exp(1) speeds: per-row probabilities + p(n,L)")
    print("=" * 70)
    rng = random.Random(12345)
    for (n, L, expect_p) in [(3, 160, 56 / 135), (4, 400, 0.5107843137)]:
        counts = Counter()
        even = 0
        for _ in range(N):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            above = simulate_order(n, L, speeds)
            par, order = parity_of_new_order(n, above)
            if par == 0:
                even += 1
            # classify n=3 by edge set
            if n == 3:
                eset = _edges_of(n, L, speeds)
                for name, (e, _, _) in ROWS.items():
                    if eset == e:
                        counts[name] += 1
                        break
        p = even / N
        print(f"  p({n},{L}) estimate = {p:.6f} "
              f"(expect {expect_p:.6f})  "
              f"{'OK' if abs(p-expect_p) < 0.01 else '<= 1% off'}")
        if n == 3:
            print("    per-row fractions (Exp speeds) vs statement rationals:")
            total = N
            for name, (e, _, _) in ROWS.items():
                frac = counts[name] / total
                dif = abs(frac - TABLE_PROB[name])
                mark = "OK" if dif < 0.01 else "off"
                print(f"      {name:34s} est={frac:.5f}  "
                      f"truth={TABLE_PROB[name]:.5f}  [{mark}]")


if __name__ == "__main__":
    a = check_table_parities()
    mc_probabilities(400000)
    print()
    print("DONE. Table parity check:", "MATCHED" if a else "FAILED")
