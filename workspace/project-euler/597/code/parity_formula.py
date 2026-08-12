#!/usr/bin/env python3
"""PE 597 Torpids — three jobs in one script.

JOB 1 — NEW parity reformulation (verify).
   Claim:  parity of the final order == (number of comparable
   ancestor/descendant pairs in the bump forest) mod 2.
   The bump forest is the parent-array of bump edges (parent[j]=k when boat j
   bumped k); every vertex has out-degree <= 1 (a boat bumps at most once and
   then becomes OUT), so the bump edges form a forest and "ancestor of" is a
   tree relation. Every bump chain i->...->j is exactly an ancestor-descendant
   pair in that forest, and the parity is (# such pairs with i<j) mod 2; since
   an ancestor always has a lower starting index (edges strictly increase),
   all ancestor-descendant pairs are i<j, so the forest chain-pair count mod 2
   must equal the parity. We check:
     (a) the full n=3,L=160 five-row table (each realised row's forest parity
         must equal the stated parity), and
     (b) parity-formula MC at the two anchors p(3,160)=56/135 and
         p(4,400)=521/1020, comparing forest parity cell-by-cell against
         brute.outcome_parity on every trial (0 mismatches expected).

JOB 2 — EXACT rational p(5,1800).
   The arrangement has d=n-1=4, 85 hyperplanes, ~13,750 cells. We report
   precisely why the existing machinery cannot do it and time the parts:
     * Polytope.volume() implements only d in {2,3} -> NotImplementedError,
       so no 4D volume is available at all;
     * the recursive vertex-re-slicing enumeration is too slow (>570 s for the
       full n=5 cell enumeration, timed out under the tool budget).
   We also time enumerate_cells(5,1800) up to a cap to give a concrete figure.

JOB 3 — High-precision MC for p(13,1800) via the parity formula.
   Parity = forest ancestor-descendant pair count mod 2 (cheaper than the
   full reachability/order construction). Pooled across many processes to
   >= 100M samples; report estimate and binomial SE. Independent bit of the
   estimate from job-1 anchors.

All numbers exact where available (the parity formula itself only yields 0/1,
so job 3's report is the binomial p estimate with SE; anchors are exact
rationals 56/135 and 521/1020).
"""
import random
import sys
import os
import time
import math
import multiprocessing as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))

from brute import outcome_parity, simulate_order, parity_of_new_order


# ---------------------------------------------------------------------------
# Bump forest + parity-formula parity
# ---------------------------------------------------------------------------
def bump_forest(n, L, speeds):
    """Return parent array: parent[j]=k if boat j bumped boat k, else None.
    Same chronological dynamics as brute.simulate_order. A boat bumps at most
    once, so out-degree <= 1 and the edges form a forest."""
    state = [0] * n
    pos = [40.0 * j for j in range(n)]
    parent = [None] * n
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
            if k is not None:
                vk = speeds[k]
                if vj > vk:
                    cands.append(((pos[k] - pos[j]) / (vj - vk), 'C', j, k))
            for c in cands:
                if c[0] == float('inf'):
                    continue
                if best is None or c[0] < best[0] - 1e-15:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1
            pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]
            parent[j] = k
    return parent


def forest_chain_parity(n, parent):
    """(Number of proper ancestor-descendant pairs in the forest) mod 2.
    Ancestor-descendant comparator uses graph reachability (chains may be
    length > 1, e.g. A bumps B then B bumps C: A is ancestor of C)."""
    children = [[] for _ in range(n)]
    for j in range(n):
        if parent[j] is not None:
            children[parent[j]].append(j)
    total = 0
    for a in range(n):
        stack = list(children[a])
        while stack:
            d = stack.pop()
            total += 1
            stack.extend(children[d])
    return total % 2


def parity_from_formula(n, L, speeds):
    """Parity predicted by the bump-forest reformulation."""
    return forest_chain_parity(n, bump_forest(n, L, speeds))


# ---------------------------------------------------------------------------
# JOB 1a: the five-row n=3,L=160 table
# ---------------------------------------------------------------------------
# speed triples realising each row (from verify_brute_examples)
ROWS = [
    ("none",                     (0.5, 1.0, 2.0), set(),           ('A', 'B', 'C'), "even"),
    ("B bumps C",                (0.3, 2.0, 1.0), {(1, 2)},        ('A', 'C', 'B'), "odd"),
    ("A bumps B",                (2.0, 1.0, 1.5), {(0, 1)},        ('B', 'A', 'C'), "odd"),
    ("B bumps C then A bumps C", (1.5, 2.0, 0.5), {(1, 2), (0, 2)},('C', 'A', 'B'), "even"),
    ("A bumps B then B bumps C", (3.0, 1.6, 1.0), {(0, 1), (1, 2)},('C', 'B', 'A'), "odd"),
]
NAMES = ['A', 'B', 'C']


def check_table():
    print("=" * 74)
    print("JOB 1a) n=3,L=160 five-row table via bump-forest parity")
    print("=" * 74)
    allok = True
    for (name, speeds, exp_edges, exp_order, exp_par) in ROWS:
        n, L = 3, 160
        parent = bump_forest(n, L, list(speeds))
        edges = set((j, parent[j]) for j in range(n) if parent[j] is not None)
        fp = forest_chain_parity(n, parent)
        # also compare with brute outcome_parity and order
        above = simulate_order(n, L, list(speeds))
        par, order = parity_of_new_order(n, above)
        order_names = tuple(NAMES[i] for i in order)
        par_name = "even" if fp == 0 else "odd"
        ok = (edges == exp_edges) and (order_names == tuple(exp_order)) \
             and (par_name == exp_par) and (fp == par)
        if not ok:
            allok = False
        print(f"  {name:30s} edges={sorted(edges)} forest_par={fp} "
              f"order={order_names} parity={par_name}  "
              f"expect {exp_par}  [{'OK' if ok else 'MISMATCH'}]")
    print("  =>", "ALL 5 ROWS MATCH" if allok else "MISMATCH")
    return allok


# ---------------------------------------------------------------------------
# JOB 1b + shared MC engine
# ---------------------------------------------------------------------------
def _mc_worker(job):
    n, L, total, seed = job
    rng = random.Random(seed)
    even = 0
    for _ in range(total):
        v = [rng.expovariate(1.0) for _ in range(n)]
        parent = bump_forest(n, L, v)
        fp = forest_chain_parity(n, parent)
        even += (1 - fp)
    return even


def mc_parity_formula(n, L, N, nprocs=None, seed0=12345):
    """Pooled MC estimate of p(n,L) using ONLY the bump-forest parity formula.
    Each trial recomputes the forest from Exp(1) speeds and counts it even iff
    forest chain-pair parity is 0."""
    if nprocs is None:
        nprocs = mp.cpu_count()
    chunk = 200000
    nchunks = (N + chunk - 1) // chunk
    nprocs = min(nprocs, nchunks)
    jobs = [(n, L, min(chunk, N - i * chunk), seed0 + i) for i in range(nchunks)]
    t0 = time.time()
    with mp.Pool(nprocs) as pool:
        evens = pool.map(_mc_worker, jobs)
    total = sum(min(chunk, N - i * chunk) for i in range(nchunks))
    even = sum(evens)
    p = even / total
    se = math.sqrt(p * (1 - p) / total)
    dt = time.time() - t0
    return p, se, even, total, dt


def job1(N=200000):
    ok = check_table()
    print()
    print("=" * 74)
    print("JOB 1b) parity-formula MC vs brute.outcome_parity + anchors")
    print("=" * 74)
    # cell-by-cell mismatch check (parity formula vs brute oracle)
    rng = random.Random(7)
    mism = 0
    M = 400000
    t0 = time.time()
    for _ in range(M):
        v = [rng.expovariate(1.0) for _ in range(3)]
        fp = parity_from_formula(3, 160, v)
        bp = outcome_parity(3, 160, v)
        mism += (fp != bp)
    print(f"  n=3,L=160: parity-formula vs brute.outcome_parity over {M} "
          f"trials: mismatches={mism} ({time.time()-t0:.1f}s)")
    for (n, L, target) in [(3, 160, 56 / 135), (4, 400, 521 / 1020)]:
        p, se, even, total, dt = mc_parity_formula(n, L, N)
        good = abs(p - target) < 5 * se
        print(f"  p({n},{L}) via parity formula = {p:.6f} +/- {se:.6f} "
              f"({total} samples, {dt:.1f}s)  target={target:.7f}  "
              f"[{'OK' if good else 'OFF'}]")
    # n=3 exact 56/135 via formula with larger N and compare to exact
    p, se, even, total, dt = mc_parity_formula(3, 160, 4000000)
    print(f"  [n=3,L=160 big run] parity-formula = {p:.6f} +/- {se:.6f} "
          f"({total} samples), exact 56/135={56/135:.6f} "
          f"(diff {abs(p-56/135)*135:.3f}/135)")
    return ok


# ---------------------------------------------------------------------------
# JOB 3: high-precision MC for p(13,1800)
# ---------------------------------------------------------------------------
def run_job2(cap=120):
    """Report precisely why the existing machinery cannot do exact n=5.
    85 hyperplanes, d=4, ~13,750 cells; Polytope.volume() only supports
    d in {2,3}; the recursive vertex-re-slicing enumeration is too slow.
    Time enumerate_cells(5,1800) up to `cap` seconds to give a figure."""
    print()
    print("=" * 74)
    print("JOB 2) EXACT p(5,1800) via existing arrangement machinery")
    print("=" * 74)
    # (i) volume support: n=5 -> d=4
    print("  [structural] n=5 -> d=4 free coords.")
    try:
        from arr_polytope import Polytope
        d = 4
        ineqs = [[[0] * d for _ in range(d)], [1] * d]
        I = []
        for i in range(d):
            r = [0] * d
            r[i] = -1
            I.append((r, 0))
        I.append(([1] * d, 1))
        poly = Polytope(d, I)
        print(f"  d=4 simplex vertices: {len(poly.vertices())}")
        try:
            poly.volume()
            print("  volume(d=4): implemented")
        except NotImplementedError as e:
            print(f"  volume(d=4): NotImplementedError -> {e}  "
                  f"[EXACT n=5 BLOCKED: no 4D volume routine]")
    except Exception as e:
        print(f"  polytope probe error: {e}")
    # (ii) timing of the enumeration
    from arr_enum import enumerate_cells, _hyperplanes
    print(f"  hyperplanes(n=5,L=1800): {len(_hyperplanes(5, 1800))}")
    import signal

    class TO(Exception):
        pass

    def handler(sig, frame):
        raise TO("timeout")

    old = signal.signal(signal.SIGALRM, handler)
    signal.alarm(cap)
    t0 = time.time()
    try:
        leaves, planes = enumerate_cells(5, 1800)
        dt = time.time() - t0
        signal.alarm(0)
        print(f"  enumerate_cells(5,1800) finished in {dt:.1f}s, "
              f"{len(leaves)} cells")
    except TO:
        dt = time.time() - t0
        print(f"  enumerate_cells(5,1800) did NOT finish within {cap}s "
              f"(timed out at {dt:.1f}s; ~13,750 cells expected for n=5)")
    finally:
        signal.signal(signal.SIGALRM, old)
    print("  => EXACT p(5,1800) is NOT reachable with arr_enum/arr_polytope "
          "as-is: 4D volume unsupported, enumeration too slow.")


def job3(total_samples):
    print()
    print("=" * 74)
    print("JOB 3) high-precision MC p(13,1800) via bump-forest parity")
    print("=" * 74)
    p, se, even, total, dt = mc_parity_formula(13, 1800, total_samples)
    print(f"  p(13,1800) = {p:.9f} +/- {se:.9f}")
    print(f"  samples={total} even={even} p={p:.12f} SE={se:.12f} "
          f"({total/dt:.0f} samp/s, {dt:.1f}s)")
    return p, se


if __name__ == "__main__":
    job = sys.argv[1] if len(sys.argv) > 1 else "all"
    if job in ("1", "all"):
        job1()
    if job in ("2", "all"):
        run_job2()
    if job in ("3", "all"):
        N3 = int(sys.argv[2]) if len(sys.argv) > 2 else 100_000_000
        job3(N3)
