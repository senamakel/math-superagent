#!/usr/bin/env python3
"""Diagnostic: run L=5 and probe L=16 node counts with a budget."""
import sys
sys.setrecursionlimit(1000000)

L5 = 5
constraints5 = [
    ("90342", 2), ("70794", 0), ("39458", 2), ("34109", 1),
    ("51545", 2), ("12531", 1),
]

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


def solve_with_budget(L, constraints, budget):
    guesses = [g for g, _ in constraints]
    cs = [c for _, c in constraints]
    G = len(guesses)
    gd = [[int(ch) for ch in g] for g in guesses]
    assigned = [None] * L
    acc = [0] * G
    nodes = 0
    found = [None]

    def feasible(pos, d, U_after):
        for i in range(G):
            na = acc[i] + (1 if gd[i][pos] == d else 0)
            if na > cs[i] or na + U_after < cs[i]:
                return False
        return True

    def search(n):
        nonlocal nodes
        nodes += 1
        if nodes > budget:
            return
        if found[0] is not None:
            return
        if n == L:
            if all(acc[i] == cs[i] for i in range(G)):
                found[0] = "".join(assigned)
            return
        U_after = (L - n) - 1
        best = None
        best_d = None
        for p in range(L):
            if assigned[p] is not None:
                continue
            digs = [d for d in range(10) if feasible(p, d, U_after)]
            if not digs:
                return
            if best is None or len(digs) < best[1]:
                best = (p, len(digs))
                best_d = digs
                if len(digs) == 1:
                    break
        p = best[0]
        for d in best_d:
            if found[0] is not None:
                return
            assigned[p] = str(d)
            for i in range(G):
                if gd[i][p] == d:
                    acc[i] += 1
            search(n + 1)
            for i in range(G):
                if gd[i][p] == d:
                    acc[i] -= 1
            assigned[p] = None

    search(0)
    return found[0], nodes


def main():
    for what, L, c in (("L5", L5, constraints5), ("L16", L16, constraints16)):
        import time
        budget = 1000000000 if what == "L5" else 500000000
        t0 = time.time()
        sol, nodes = solve_with_budget(L, c, budget)
        dt = time.time() - t0
        print(f"{what}: sol={sol} nodes={nodes} time={dt:.2f}s")


if __name__ == "__main__":
    main()
