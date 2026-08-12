#!/usr/bin/env python3
"""Verify code/brute.py against every worked example in the PE597 statement.

The statement's worked examples are:

  (i)  the five n=3, L=160 rows, each giving (bumps -> new order -> parity),
       and the even-row total p(3,160) = 56/135;
  (ii) the given value p(4,400) = 0.5107843137 (10 dp).

The naive oracle (brute.py) is a deterministic simulator: given a concrete
speed vector it replays the race chronologically and reports the new order and
its parity. It cannot integrate the Exp(1) probability measure, so:

  A) For each of the five rows we hand-construct a speed triple whose
     chronological bump-edge set is exactly the row's, feed it to brute, and
     check that brute reports the table's new order and parity.
  B) We MC brute over true Exp(1) speeds at the two given sizes to confirm
     p(3,160) ~ 56/135 and p(4,400) ~ 0.5107843137.

This only touches the statement's own sizes (n=3,L=160 and n=4,L=400).
"""
import random

from brute import simulate_order, parity_of_new_order, outcome_parity

NAMES = ["A", "B", "C"]  # A=0 lowest/downstream, C=2 highest/upstream

# Hand-constructed (v_A, v_B, v_C) realising each table row's bump-edge set.
# Each was chosen so its catch/finish chronology matches the verbal scenario.
ROWS = [
    #  name                        speeds      expected edges         order      parity
    ("none",                       (0.5, 1.0, 2.0),  set(),           ("A","B","C"), "even"),
    ("B bumps C",                  (0.3, 2.0, 1.0),  {(1, 2)},        ("A","C","B"), "odd"),
    ("A bumps B",                  (2.0, 1.0, 1.5),  {(0, 1)},        ("B","A","C"), "odd"),
    ("B bumps C then A bumps C",   (1.5, 2.0, 0.5),  {(1, 2), (0, 2)},("C","A","B"), "even"),
    ("A bumps B then B bumps C",   (3.0, 1.6, 1.0),  {(0, 1), (1, 2)},("C","B","A"), "odd"),
]

def realized_edges(n, L, speeds):
    """Replay and collect the set of chronological bump edges (bumper,bumped)."""
    state = [0] * n; pos = [40.0 * j for j in range(n)]; edges = []
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]; ft = (L - pos[j]) / vj
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk; break
            cands = [(ft, 'F', j, None)]
            if k is not None and vj > speeds[k]:
                cands.append(((pos[k] - pos[j]) / (vj - speeds[k]), 'C', j, k))
            for c in cands:
                if c[0] == float('inf'):
                    continue
                if best is None or c[0] < best[0] - 1e-12:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1; pos[j] = L
        else:
            state[j] = 2; pos[j] = pos[k]; edges.append((j, k))
    return set(edges)


def check_table_rows():
    print("=" * 72)
    print("A) n=3, L=160: for each row, realise its bump edge-set and check")
    print("   brute reports the table's (new order, parity).")
    print("=" * 72)
    allok = True
    for (name, speeds, exp_edges, exp_order, exp_par) in ROWS:
        n, L = 3, 160
        got_edges = realized_edges(n, L, list(speeds))
        if got_edges != exp_edges:
            print(f"  {name:28s}  FAIL: realised edges {got_edges} != {exp_edges}")
            allok = False
            continue
        above = simulate_order(n, L, list(speeds))
        par, order = parity_of_new_order(n, above)
        order_names = tuple(NAMES[i] for i in order)
        par_name = "even" if par == 0 else "odd"
        ok = (order_names == tuple(exp_order)) and (par_name == exp_par)
        if not ok:
            allok = False
        print(f"  {name:28s} edges={sorted(got_edges)} "
              f"order={order_names} parity={par_name} "
              f"expect order={exp_order} parity={exp_par}  "
              f"[{'OK' if ok else 'MISMATCH'}]")
    print("  =>", "ALL 5 ROWS MATCH" if allok else "MISMATCH FOUND")
    return allok


def mc_anchors(N):
    print()
    print("=" * 72)
    print("B) MC brute over true Exp(1) speeds at the two given sizes.")
    print("=" * 72)
    ok = True
    rng = random.Random(20240517)
    for (n, L, target) in [(3, 160, 56 / 135), (4, 400, 0.5107843137)]:
        even = 0
        for _ in range(N):
            v = [rng.expovariate(1.0) for _ in range(n)]
            if outcome_parity(n, L, v) == 0:
                even += 1
        p = even / N
        se = (p * (1 - p) / N) ** 0.5
        good = abs(p - target) < 5 * se  # >5 sigma would call the engine into question
        if not good:
            ok = False
        print(f"  p({n},{L}) MC = {p:.6f} +/- {se:.6f}   "
              f"(target {target:.7f})   [{'OK' if good else 'OFF'}]")
    print("  =>", "BOTH ANCHORS WITHIN 5 SE" if ok else "ANCHOR OFF")
    return ok


if __name__ == "__main__":
    a = check_table_rows()
    b = mc_anchors(400000)
    print()
    print("DONE. Table rows:", "MATCHED" if a else "FAILED",
          "| Anchors:", "MATCHED" if b else "FAILED")
