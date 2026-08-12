#!/usr/bin/env python3
"""Test value-orderings for finding the L=16 solution fast (first solution).
We only need to FIND it; exhaustive proof is only required for L=5 (brute
checks that anyway)."""
import sys, time
sys.setrecursionlimit(1000000)

L16 = 16
constraints16 = [
    ("5616185650518293", 2), ("3847439647293047", 1),
    ("5855462940810587", 3), ("9742855507068353", 3),
    ("4296849643607543", 3), ("3174248439465858", 1),
    ("4513559094146117", 2), ("7890971548908067", 3),
    ("8157356344118483", 1), ("2615250744386899", 2),
    ("8690095851526254", 3), ("6375711915077050", 1),
    ("6913859173121360", 1), ("6442889055042768", 2),
    ("2321386104303845", 0), ("2326509471271448", 2),
    ("5251583379644322", 2), ("1748270476758276", 3),
    ("4895722652190306", 1), ("3041631117224635", 3),
    ("1841236454324589", 3), ("2659862637316867", 2),
]


def run(order_name, order_fn, node_cap):
    guesses = [g for g, _ in constraints16]
    cs = [c for _, c in constraints16]
    G = len(guesses)
    gd = [[int(ch) for ch in g] for g in guesses]
    assigned = [None] * L16
    acc = [0] * G
    nodes = 0
    found = [None]
    t0 = time.time()

    def feasible(pos, d, U_after):
        for i in range(G):
            na = acc[i] + (1 if gd[i][pos] == d else 0)
            if na > cs[i] or na + U_after < cs[i]:
                return False
        return True

    def search(n):
        nonlocal nodes
        nodes += 1
        if found[0] is not None or nodes > node_cap:
            return
        if n == L16:
            if all(acc[i] == cs[i] for i in range(G)):
                found[0] = "".join(assigned)
            return
        U_after = (L16 - n) - 1
        best_p = None; best_len = None; best_feas = None
        for p in range(L16):
            if assigned[p] is not None:
                continue
            digs = [d for d in range(10) if feasible(p, d, U_after)]
            if not digs:
                return
            if best_len is None or len(digs) < best_len:
                best_len = len(digs); best_p = p; best_feas = digs
                if best_len == 1:
                    break
        # order digits by order_fn(p, acc)
        ordered = order_fn(best_p, best_feas)
        for d in ordered:
            if found[0] is not None:
                return
            assigned[best_p] = str(d)
            for i in range(G):
                if gd[i][best_p] == d:
                    acc[i] += 1
            search(n + 1)
            for i in range(G):
                if gd[i][best_p] == d:
                    acc[i] -= 1
            assigned[best_p] = None

    search(0)
    dt = time.time() - t0
    print(f"[{order_name}] sol={found[0]} nodes={nodes} time={dt:.2f}s "
          f"rate={nodes/dt:.0f}/s", flush=True)


def dig_popular(p, feas, G, gd):
    # order feasible digits by how many guesses they'd match at p (desc)
    cnt = {}
    for d in feas:
        cnt[d] = sum(1 for i in range(G) if gd[i][p] == d)
    return sorted(feas, key=lambda d: -cnt[d])


def dig_needs(p, feas, G, gd, acc, cs):
    # prefer digit that resolves guesses still needing matches
    def score(d):
        s = 0
        for i in range(G):
            if gd[i][p] == d:
                r = cs[i] - acc[i]
                if r > 0:
                    s += 2
                elif r == 0:
                    s -= 1
        return s
    return sorted(feas, key=lambda d: -score(d))


def dig_asc(p, feas):
    return sorted(feas)


run("asc", lambda p, f: dig_asc(p, f), 200_000_000)
