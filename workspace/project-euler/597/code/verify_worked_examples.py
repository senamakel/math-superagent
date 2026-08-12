#!/usr/bin/env python3
"""verify_worked_examples.py -- reproduce every PE 597 worked example exactly.

Engines used, all existing workspace code:
  * brute.py            naive chronological race simulator (reference oracle)
  * exact_race.py       the same dynamics with exact Fraction arithmetic
  * cell_exact.py       exact arrangement-cell integration (rational p(n,L))
  * toolkits/arr_enum.py + arr_polytope.py   (cell machinery behind the above)

Checks performed, exact rationals throughout:

  A) The five n=3, L=160 table rows. For each row an exact Fraction speed
     triple is constructed that realises the row's bump edge-set; the race is
     replayed with exact_race.simulate_order_exact and brute.simulate_order;
     the realised edge set, new order, and parity must match the table.

  B) The row probabilities. The n=3,L=160 outcome arrangement (32 open cells)
     is enumerated; every cell's interior is evaluated by the exact race and
     classified by its COMPLETE new order (not just parity). Cell areas are
     summed per order and scaled by the Dirichlet density (n-1)! = 2. The five
     new orders must receive exactly 4/15, 8/45, 1/3, 4/27, 2/27 and the
     sixth permutation (B,C,A) exactly 0 -- the rows partition the probability
     space and sum to 1. The even orders sum to 56/135.

  C) The given p values, exactly: p(3,160)=56/135, p(4,400)=521/1020
     (== given 0.5107843137 to 10 dp), and the two requested extra exact
     values from the same exact solver: p(3,1800)=2237/5742,
     p(4,1800)=166802/317985.

Writes a timestamped report to code/out/verification_run.txt and prints the
same content to stdout.

Usage: python3 verify_worked_examples.py
"""
import datetime
import math
import os
import sys

from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))

from brute import simulate_order, parity_of_new_order
from exact_race import simulate_order_exact
from cell_exact import p_exact
from arr_enum import enumerate_cells, leaf_interior

NAMES = ["A", "B", "C"]
NEW_ORDER_LABEL = {0: "even", 1: "odd"}

# Rows from the statement, n=3, L=160. speeds are exact Fractions chosen so the
# chronological bump edge-set is exactly the row's (checked below, exactly).
ROWS = [
    #  name                             speed (A,B,C)   bumps (edges)      new order    parity
    ("none",                            (F(1, 2), F(1), F(2)),     set(),          ("A", "B", "C"), "even"),
    ("B bumps C",                       (F(3, 10), F(2), F(1)),    {(1, 2)},       ("A", "C", "B"), "odd"),
    ("A bumps B",                       (F(2), F(1), F(3, 2)),     {(0, 1)},       ("B", "A", "C"), "odd"),
    ("B bumps C then A bumps C",        (F(3, 2), F(2), F(1, 2)),  {(1, 2), (0, 2)}, ("C", "A", "B"), "even"),
    ("A bumps B then B bumps C",        (F(3), F(8, 5), F(1)),     {(0, 1), (1, 2)}, ("C", "B", "A"), "odd"),
]

ROW_PROB = {
    ("A", "B", "C"): F(4, 15),
    ("A", "C", "B"): F(8, 45),
    ("B", "A", "C"): F(1, 3),
    ("C", "A", "B"): F(4, 27),
    ("C", "B", "A"): F(2, 27),
}


def realized_edges_exact(n, L, speeds):
    """Replay the race exactly and return the set of bump edges."""
    state = [0] * n
    pos = [F(40) * j for j in range(n)]
    edges = []
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]
            ft = F(L - pos[j]) / vj
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            cands = [(ft, "F", j, None)]
            if k is not None and vj > speeds[k]:
                cands.append(((pos[k] - pos[j]) / (vj - speeds[k]), "C", j, k))
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
            edges.append((j, k))
    return set(edges)


def order_names_of(order):
    return tuple(NAMES[i] for i in order)


def part_a(lines):
    """Five rows through brute + exact race: edges, order, parity."""
    lines.append("=" * 78)
    lines.append("A) The five n=3, L=160 rows -- brute.py + exact_race.py")
    lines.append("   (exact Fraction replay; edges, new order, parity)")
    lines.append("=" * 78)
    allok = True
    for name, speeds, exp_edges, exp_order, exp_par in ROWS:
        n, L = 3, 160
        got_edges = realized_edges_exact(n, L, list(speeds))
        above = simulate_order_exact(n, L, list(speeds))
        par, order = parity_of_new_order(n, above)
        order_names = order_names_of(order)
        par_name = NEW_ORDER_LABEL[par]
        # float engine must agree with the exact one on this vector
        above_f = simulate_order(n, L, [float(x) for x in speeds])
        par_f, order_f = parity_of_new_order(n, above_f)
        ok = (got_edges == exp_edges
              and order_names == exp_order
              and par_name == exp_par
              and order_names_of(order_f) == exp_order
              and NEW_ORDER_LABEL[par_f] == exp_par)
        allok = allok and ok
        lines.append(f"  row '{name}':")
        lines.append(f"    speeds (exact)          = ({speeds[0]}, {speeds[1]}, {speeds[2]})")
        lines.append(f"    realised bump edges     = {sorted(got_edges)}  (table: {sorted(exp_edges)})")
        lines.append(f"    new order (exact)       = {order_names} (table: {exp_order})")
        lines.append(f"    parity (exact/float)    = {par_name} / {NEW_ORDER_LABEL[par_f]} (table: {exp_par})")
        lines.append(f"    => {'OK' if ok else 'MISMATCH'}")
    lines.append(f"  => {'ALL 5 ROWS MATCH' if allok else 'MISMATCH FOUND'}")
    return allok


def part_b(lines):
    """Row probabilities exactly from the arrangement cells at n=3, L=160."""
    lines.append("")
    lines.append("=" * 78)
    lines.append("B) Row probabilities exactly from the n=3, L=160 arrangement")
    lines.append("   (32 open cells; each classified by its COMPLETE new order)")
    lines.append("=" * 78)
    n, L = 3, 160
    leaves, planes = enumerate_cells(n, L)
    per_order_vol = {}
    per_order_count = {}
    even_vol = F(0)
    even_count = 0
    for poly, _svec in leaves:
        pt = leaf_interior(poly)
        if pt is None:
            continue
        s = sum(F(x) for x in pt)
        speeds = [F(x) for x in pt] + [F(1) - s]
        above = simulate_order_exact(n, L, speeds)
        par, order = parity_of_new_order(n, above)
        key = order_names_of(order)
        per_order_vol[key] = per_order_vol.get(key, F(0)) + poly.volume()
        per_order_count[key] = per_order_count.get(key, 0) + 1
        if par == 0:
            even_vol += poly.volume()
            even_count += 1
    dens = math.factorial(n - 1)  # Dirichlet density factor (n-1)!
    allok = True
    total = F(0)
    key_order = ["ABC", "ACB", "BAC", "CAB", "CBA", "BCA"]
    for key in sorted(per_order_vol,
                      key=lambda k: key_order.index("".join(k))):
        prob = dens * per_order_vol[key]
        total += prob
        row_prob = ROW_PROB.get(key, None)
        if row_prob is None:
            ok = (prob == 0)
            allok = allok and ok
            lines.append(f"  new order {key}:  p = {prob}  (table has no row for it)  "
                         f"[{'OK, zero as required (rows partition the space)' if ok else 'NONZERO?!'}]")
            continue
        ok = (prob == row_prob)
        allok = allok and ok
        lines.append(f"  new order {key}:  p = {prob} = {float(prob):.9f}  "
                     f"(table {row_prob})  cells={per_order_count[key]}  "
                     f"[{'OK' if ok else 'MISMATCH'}]")
    even_p = dens * even_vol
    sum_ok = (total == 1)
    even_ok = (even_p == F(56, 135))
    for key, rp in ROW_PROB.items():
        if dens * per_order_vol.get(key, F(0)) != rp:
            sum_ok = False
    lines.append(f"  sum of the five row probabilities               = {total}  "
                 f"[{'OK, = 1' if sum_ok else 'NOT 1'}]")
    lines.append(f"  P(even) = 4/15 + 4/27                          = {even_p}  "
                 f"[{'OK, = 56/135' if even_ok else 'NOT 56/135'}]")
    lines.append(f"  cells: {len(leaves)} total, {even_count} even  (planes: {len(planes)})")
    ok = allok and sum_ok and even_ok
    lines.append(f"  => {'ALL 5 ROW PROBABILITIES EXACT, SUM = 1, EVEN = 56/135' if ok else 'B FAILED'}")
    return ok


def part_c(lines, cases):
    """Exact p(n,L) from the exact arrangement-cell oracle."""
    lines.append("")
    lines.append("=" * 78)
    lines.append("C) Exact p(n,L) from cell_exact.p_exact (arrangement-cell")
    lines.append("   integration, exact rational arithmetic)")
    lines.append("=" * 78)
    allok = True
    for n, L, expected, label in cases:
        p, even_vol, even_count, nleaves, dt = p_exact(n, L)
        ok = (p == expected)
        allok = allok and ok
        lines.append(f"  {label:12s} n={n} L={L:<5} cells={nleaves:<5} "
                     f"even_cells={even_count:<5}  got={p} = {float(p):.10f}  "
                     f"expected={expected}  [{'OK' if ok else 'MISMATCH'}]  ({dt:.1f}s)")
    lines.append(f"  => {'ALL 4 EXACT VALUES MATCH' if allok else 'MISMATCH FOUND'}")
    return allok


def main():
    lines = []
    lines.append("PE 597 (Torpids) -- worked-example verification run")
    lines.append("run at: " + datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S UTC"))
    lines.append("host: " + os.uname().nodename)
    lines.append("")
    lines.append("Engines: brute.py (naive float oracle), exact_race.py (exact "
                 "Fraction dynamics),")
    lines.append("         cell_exact.py + toolkits/arr_enum.py + "
                 "toolkits/arr_polytope.py (exact")
    lines.append("         arrangement-cell integration, p = (n-1)! * sum of "
                 "even-cell volumes)")
    res_a = part_a(lines)
    res_b = part_b(lines)
    cases = [
        (3, 160, F(56, 135), "p(3,160)"),
        (3, 1800, F(2237, 5742), "p(3,1800)"),
        (4, 400, F(521, 1020), "p(4,400)"),
        (4, 1800, F(166802, 317985), "p(4,1800)"),
    ]
    res_c = part_c(lines, cases)
    lines.append("")
    lines.append("=" * 78)
    lines.append("SUMMARY")
    lines.append("=" * 78)
    lines.append(f"  A) five n=3,L=160 rows (edges, order, parity): "
                 f"{'ALL MATCH' if res_a else 'FAIL'}")
    lines.append(f"  B) row probabilities 4/15, 8/45, 1/3, 4/27, 2/27 "
                 f"(sum 1, even 56/135): {'ALL MATCH' if res_b else 'FAIL'}")
    lines.append(f"  C) exact p values: p(3,160)=56/135, p(3,1800)=2237/5742, "
                 f"p(4,400)=521/1020=0.5107843137...,")
    lines.append(f"     p(4,1800)=166802/317985: {'ALL MATCH' if res_c else 'FAIL'}")
    total_ok = res_a and res_b and res_c
    lines.append(f"  OVERALL: {'ALL CHECKS PASS' if total_ok else 'FAILURE'}")
    report = "\n".join(lines) + "\n"
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out",
                            "verification_run.txt")
    with open(out_path, "w") as fh:
        fh.write(report)
    print(report)
    print(f"[report written to {out_path}]")
    return 0 if total_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())