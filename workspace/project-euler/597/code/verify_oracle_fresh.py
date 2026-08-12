#!/usr/bin/env python3
"""Fresh verification of the PE597 oracle for this run.

Exact anchors required by the completion criteria:
  (1) the full 5-row n=3, L=160 worked-example table (bumps/new order/parity),
      with the five row probabilities summing to 1;
  (2) p(3,160) = 56/135 exactly;
  (3) p(4,400) = 521/1020 = 0.5107843137... exactly.

Engines (all existing workspace code):
  * brute.py        naive chronological race simulator -> reference oracle
                    (deterministic: given a speed vector it returns the parity)
  * brute.outcome_parity drives the MC sanity estimate of the two anchors
  * cell_exact.p_exact   exact arrangement-cell rational integration
  * arrangement_pn.build_lines / compute_pn  second, independent enumerator

This file is a fresh verification driver; it does not introduce a new method.
"""
import math, os, sys, random, time
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))

from brute import simulate_order, parity_of_new_order, outcome_parity
from exact_race import simulate_order_exact
from cell_exact import p_exact

NAMES = ["A", "B", "C"]

# Five rows of the n=3, L=160 statement table. speeds are exact Fractions that
# realise the chronological bump edge-set exactly (verified in Part A).
ROWS = [
    ("none",                         (F(1, 2), F(1), F(2)),    set(),         ("A", "B", "C"), "even"),
    ("B bumps C",                    (F(3, 10), F(2), F(1)),   {(1, 2)},      ("A", "C", "B"), "odd"),
    ("A bumps B",                    (F(2), F(1), F(3, 2)),    {(0, 1)},      ("B", "A", "C"), "odd"),
    ("B bumps C then A bumps C",     (F(3, 2), F(2), F(1, 2)), {(1, 2), (0, 2)}, ("C", "A", "B"), "even"),
    ("A bumps B then B bumps C",     (F(3), F(8, 5), F(1)),    {(0, 1), (1, 2)}, ("C", "B", "A"), "odd"),
]
ROW_PROB = {
    "ABC": F(4, 15),
    "ACB": F(8, 45),
    "BAC": F(1, 3),
    "CAB": F(4, 27),
    "CBA": F(2, 27),
}


def realized_edges_exact(n, L, speeds):
    """Replay the race with exact rationals; return the chronological bump edge set."""
    L = F(L)
    state = [0] * n
    pos = [F(40) * j for j in range(n)]
    edges = set()
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = F(speeds[j])
            ft = F(L - pos[j]) / vj
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            cands = [(ft, "F", j, None)]
            if k is not None and vj > F(speeds[k]):
                cands.append(((F(pos[k]) - pos[j]) / (vj - F(speeds[k])), "C", j, k))
            for c in cands:
                if best is None or c[0] < best[0]:
                    best = c
        t, kind, j, k = best
        if kind == "F":
            state[j] = 1
            pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]
            edges.add((j, k))
    return edges


def names(order):
    return "".join(NAMES[i] for i in order)


def part_a():
    """Five rows through brute.py (float) and exact_race.py (rational)."""
    print("=" * 72)
    print("A) The five n=3, L=160 rows  (brute.py replay; exact edges/order/parity)")
    print("=" * 72)
    ok_all = True
    for name, speeds, exp_edges, exp_order, exp_par in ROWS:
        n, L = 3, 160
        got_edges = realized_edges_exact(n, L, list(speeds))
        above = simulate_order_exact(n, L, list(speeds))
        par, order = parity_of_new_order(n, above)
        # float engine must agree
        above_f = simulate_order(n, L, [float(x) for x in speeds])
        par_f, order_f = parity_of_new_order(n, above_f)
        ok = (got_edges == exp_edges and names(order) == exp_order
              and ("even" if par == 0 else "odd") == exp_par
              and names(order_f) == exp_order and par_f == par)
        ok_all &= ok
        print(f"  {name:28s} edges={sorted(got_edges)!s:16s} "
              f"new={names(order):5s} parity={'even' if par==0 else 'odd':4s}  "
              f"[{'OK' if ok else 'MISMATCH'}]")
    print(f"  => {'ALL 5 ROWS MATCH' if ok_all else 'MISMATCH'}")
    # Row probabilities from the n=3,L=160 arrangement: exact, sum to 1
    print("=" * 72)
    print("A2) Row probabilities exactly (n=3, L=160 arrangement cells), sum == 1")
    print("=" * 72)
    leaves, planes = enumerate_cells_import(3, 160)
    per_order = {}
    for poly, _ in leaves:
        pt = leaf_interior_import(poly)
        if pt is None:
            continue
        s = sum(F(x) for x in pt)
        speeds = [F(x) for x in pt] + [F(1) - s]
        above = simulate_order_exact(3, 160, speeds)
        par, order = parity_of_new_order(3, above)
        key = names(order)
        per_order[key] = per_order.get(key, F(0)) + poly.volume()
    dens = math.factorial(2)
    total = F(0)
    allok2 = True
    for key in sorted(ROW_PROB, key=lambda k: ["ABC", "ACB", "BAC", "CAB", "CBA"].index(k)):
        prob = dens * per_order.get(key, F(0))
        total += prob
        ok = (prob == ROW_PROB[key])
        allok2 &= ok
        print(f"  {key}: p = {prob} = {float(prob):.9f}  (table {ROW_PROB[key]})  "
              f"[{'OK' if ok else 'MISMATCH'}]")
    # sixth permutation should be zero
    sixth = dens * per_order.get("BCA", F(0))
    print(f"  BCA (no table row): p = {sixth}  [{'OK zero' if sixth == 0 else 'NONZERO?!'}]")
    allok2 &= (sixth == 0)
    print(f"  sum of the five row probabilities = {total}  "
          f"[{'OK, = 1' if total == 1 else 'NOT 1'}]")
    allok2 &= (total == 1)
    even = ROW_PROB["ABC"] + ROW_PROB["CAB"]
    print(f"  P(even) = 4/15 + 4/27 = {even}  [{'OK, = 56/135' if even == F(56,135) else 'FAIL'}]")
    print(f"  => {'ALL ROW PROBABILITIES EXACT, SUM = 1' if allok2 else 'B FAILED'}")
    return ok_all and allok2


def enumerate_cells_import(n, L):
    from arr_enum import enumerate_cells
    return enumerate_cells(n, L)


def leaf_interior_import(poly):
    from arr_enum import leaf_interior
    return leaf_interior(poly)


def part_b_mc(seed=12345, n_mc=2000000):
    """Small MC sanity of both anchors via brute.outcome_parity (Exp(1) draws)."""
    print("=" * 72)
    print(f"B) MC sanity (N={n_mc}) of p(3,160) and p(4,400) via brute.outcome_parity")
    print("=" * 72)
    rng = random.Random(seed)
    out = {}
    for (n, L, expect) in [(3, 160, F(56, 135)), (4, 400, F(521, 1020))]:
        even = 0
        sample = n_mc
        for _ in range(sample):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            if outcome_parity(n, L, speeds) == 0:
                even += 1
        phat = even / sample
        se = math.sqrt(phat * (1 - phat) / sample)
        target = float(expect)
        in3 = abs(phat - target) <= 3 * se
        out[(n, L)] = phat
        print(f"  p({n},{L}) MC = {phat:.6f} +/- {se:.6f}   exact {float(expect):.6f}"
              f"  [within 3 SE: {'OK' if in3 else 'NO'}]")
    return out


def part_c():
    """Exact p values from cell_exact.p_exact (rational arrangement integration)."""
    print("=" * 72)
    print("C) Exact p(n,L) from cell_exact.p_exact (arrangement-cell integration)")
    print("=" * 72)
    cases = [
        (3, 160, F(56, 135), "p(3,160)"),
        (4, 400, F(521, 1020), "p(4,400)"),
    ]
    allok = True
    for n, L, expect, label in cases:
        t0 = time.time()
        p, even_vol, even_count, nleaves, dt = p_exact(n, L)
        ok = (p == expect)
        allok &= ok
        print(f"  {label:10s} n={n} L={L:<5} cells={nleaves} even={even_count}  "
              f"got {p} = {float(p):.10f}  expected {expect}  "
              f"[{'OK' if ok else 'MISMATCH'}]  ({dt:.1f}s)")
    return allok


def part_d():
    """Second independent route: arrangement_pn.py exact enumerator."""
    print("=" * 72)
    print("D) Second independent route: arrangement_pn.py (own cell machinery)")
    print("=" * 72)
    import importlib.util
    # import arrangement_pn without executing its main
    spec = importlib.util.spec_from_file_location(
        "arrangement_pn",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "arrangement_pn.py"))
    apn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(apn)
    allok = True
    for n, L, expect in [(3, 160, F(56, 135)), (4, 400, F(521, 1020))]:
        lines, events = apn.build_lines(n, L)
        p, ncells, cells = apn.compute_pn(n, L, lines)
        ok = (p == expect)
        allok &= ok
        print(f"  arrangement_pn: n={n} L={L} cells={ncells}  got {p} = {float(p):.10f}  "
              f"expected {expect}  [{'OK' if ok else 'MISMATCH'}]")
    return allok


def main():
    print("PE 597 (Torpids) -- fresh oracle verification for this run")
    print("run at: " + time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()))
    res_a = part_a()
    mc = part_b_mc()
    res_c = part_c()
    res_d = part_d()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  A) five n=3,L=160 rows (edges/order/parity) + probabilities: "
          f"{'ALL MATCH' if res_a else 'FAIL'}")
    print(f"  B) MC sanity: p(3,160)~0.4148, p(4,400)~0.5108 (see SE bands)")
    print(f"  C) cell_exact: p(3,160)=56/135, p(4,400)=521/1020: "
          f"{'ALL MATCH' if res_c else 'FAIL'}")
    print(f"  D) arrangement_pn (independent): same exact values: "
          f"{'ALL MATCH' if res_d else 'FAIL'}")
    ok = res_a and res_c and res_d
    print(f"  OVERALL: {'ALL ANCHORS REPRODUCED' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
