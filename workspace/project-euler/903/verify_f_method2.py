#!/usr/bin/env python3
"""Independent verification of extend_f.py's n=10,11 rows.

Method 2 (cycle-type decomposition, no repeated composition):
For each permutation pi in S_n, count f contributions by cycle structure.
f_n(k) = sum_pi (n!/d) * #{tau in <pi> : tau(k) < tau(0)}, d = ord(pi).

Instead of enumerating tau by power iteration, use the standard fact that
pi^t moves a point x to the element t positions ahead on x's pi-cycle.
For fixed pi we need, over t = 0..d-1 (one per distinct power),
  cnt_k(pi) = #{t : (pi^t)(k) < (pi^t)(0)}.
This depends only on the cycle structure and the positions of 0 and k:
  - same cycle of length L: pi^t maps 0 and k to p0(t), pk(t) =====
    the cyclic distance between them is fixed (= distance 0->k along the
    cycle), so the comparison (pi^t)(k) < (pi^t)(0) is constant in t and
    holds for exactly L of the d values when ... (see code).
  - different cycles of lengths L0, Lk: the two images run independently
    around their cycles; count pairs (i,j) in residues where
    (a + i) vs (b + j) by relative order -- a small double sum.

Enumerate all n! permutations (same bound as extend_f), but accumulate
per-power counts by the closed formulas, not by composing powers.

This is deliberately a DIFFERENT code path from extend_f.py, so agreement
is an independent check of the n=10,11 rows in extend_f.json.
"""
import itertools
import math
import time
from collections import Counter


def cycle_decomp(perm):
    """Return list of cycles as lists of 0-based elements, pi-direction."""
    n = len(perm)
    seen = [False] * n
    cycles = []
    for s in range(n):
        if not seen[s]:
            cyc = []
            c = s
            while not seen[c]:
                seen[c] = True
                cyc.append(c)
                c = perm[c]
            cycles.append(cyc)
    return cycles


def power_positions(cyc, start, t):
    """Element reached from start after t applications of pi along cycle.
    t is taken modulo len(cyc)."""
    L = len(cyc)
    idx = cyc.index(start)
    return cyc[(idx + t) % L]


def count_for_cycles(cyc0, cyck, d):
    """# {t in 0..d-1 : image of cyck-point(t) < image of cyc0-point(t)}.
    The two points 0 and k are on given cycles (lengths L0, Lk).
    The pairing is (pos0 + t mod L0 on cyc0) vs (posk + t mod Lk on cyck),
    with t = 0..d-1.  We normalize so cyc0's point starts at index 0 of a
    fresh labeling via adding offset; the count only depends on the two
    lengths and their relative offset.
    """
    L0, Lk = len(cyc0), len(cyck)
    # walk t=0..d-1; d is a multiple of lcm(L0,Lk) if same cycle else product
    # Actually only the pattern modulo lcm(L0,Lk) matters; t real range 0..d-1
    # covers each residue class of lcm exactly d/lcm times.
    L = L0 * Lk // math.gcd(L0, Lk)
    reps = d // L
    # count within one period
    cnt = 0
    for t in range(L):
        # pick representative positions: 0 at index 0 of cyc0, k at its own index
        # but relative order is what matters; by rotation invariance we can fix
        # cyc0 to be [0,1,...,L0-1] and cyck a shifted list of 0..Lk-1.
        # We rotate so that cyc0 = [0..L0-1] in order, keep track of cyck's
        # starting value relative to 0 (offset o): element at index r of cyck
        # has value o + r mod Lk where o in 0..Lk-1 (the 'value' of cyck[0]).
        pass
    # Better: enumerate actual positions in the real cycles.
    # cyc0 and cyck are real lists; use their actual element values for
    # comparisons, and t runs over the period L.
    cnt = 0
    for t in range(L):
        a = cyc0[t % L0]           # image of 0 at time t (cyc0[0] is 0's slot)
        b = cyck[t % Lk]
        if b < a:
            cnt += 1
    return cnt * reps


def f_n_method2(n):
    nf = math.factorial(n)
    idt = list(range(n))
    f = [0] * (n - 1)
    for perm in itertools.permutations(range(n)):
        d = 1
        cycles = cycle_decomp(perm)
        for cyc in cycles:
            L = len(cyc)
            d = d * L // math.gcd(d, L)
        w = nf // d
        # locate 0 and each k
        # find cycle containing 0, rotate so 0 is at index 0
        for ci, cyc in enumerate(cycles):
            if 0 in cyc:
                c0 = ci
                break
        else:
            raise RuntimeError("0 not found")
        # rotate c0 so 0 is at position 0
        z = cycles[c0]
        zr = z[z.index(0):] + z[:z.index(0)]
        # We'll need cycle-containing-k for each k: build map
        cyc_of = {}
        pos_of = {}
        for ci, cyc in enumerate(cycles):
            for j, v in enumerate(cyc):
                cyc_of[v] = ci
                pos_of[v] = j
        L0 = len(zr)
        for k in range(1, n):
            ck = cyc_of[k]
            cyck = cycles[ck]
            Lk = len(cyck)
            if ck == c0:
                # same cycle: images are 0 at zr[t % L0], k at zr[(pos_of[k] + t) % L0]
                # comparison zr[(posk + t)%L] < zr[t%L] is constant over t
                # whether or not; count over full period d
                posk = pos_of[k]
                # t = 0..d-1, but pattern repeats with period L0; count per period
                # and multiply
                per = L0
                reps = d // per
                cntp = 0
                for t in range(per):
                    if zr[(posk + t) % per] < zr[t % per]:
                        cntp += 1
                cnt = cntp * reps
            else:
                # different cycles: t runs 0..d-1; period L = lcm(L0,Lk)
                L = L0 * Lk // math.gcd(L0, Lk)
                reps = d // L
                # rotate cyck so that its 0-slot maps home; actual values matter
                # but we can rotate cyck to start at pos_of[k]
                cyck_r = cyck[pos_of[k]:] + cyck[:pos_of[k]]
                cnt = 0
                for t in range(L):
                    a = zr[t % L0]
                    b = cyck_r[t % Lk]
                    if b < a:
                        cnt += 1
                cnt *= reps
            f[k - 1] += w * cnt
    return f


if __name__ == "__main__":
    import json
    data = json.load(open("extend_f.json"))
    print("Method-2 rows for n = 10, 11; compare to extend_f.json")
    for n in (10, 11):
        t0 = time.time()
        row = f_n_method2(n)
        dt = time.time() - t0
        expected = data[str(n)]
        ok = row == expected
        print(f"n={n}: time {dt:.2f}s  match={ok}")
        if not ok:
            print("  got     ", row)
            print("  expected", expected)