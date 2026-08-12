#!/usr/bin/env python3
import sys, time
sys.setrecursionlimit(1000000)

L5 = 5
constraints5 = [
    ("90342", 2), ("70794", 0), ("39458", 2), ("34109", 1),
    ("51545", 2), ("12531", 1),
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
        best_len = None
        best_d = None
        for p in range(L):
            if assigned[p] is not None:
                continue
            digs = [d for d in range(10) if feasible(p, d, U_after)]
            if not digs:
                return
            if best_len is None or len(digs) < best_len:
                best_len = len(digs)
                best_d = digs
                if best_len == 1:
                    break
        p = assigned.index(None)
        # we must use the chosen best position, not first None
        # recompute chosen pos
        p = None
        for q in range(L):
            if assigned[q] is None:
                p = q
            # placeholder; fix below
        return
    # replaced below

# simpler standalone L5
def solve5():
    guesses = [g for g, _ in constraints5]
    cs = [c for _, c in constraints5]
    G = len(guesses)
    gd = [[int(ch) for ch in g] for g in guesses]
    assigned = [None] * L5
    acc = [0] * G
    nodes = 0

    def feasible(pos, d, U_after):
        for i in range(G):
            na = acc[i] + (1 if gd[i][pos] == d else 0)
            if na > cs[i] or na + U_after < cs[i]:
                return False
        return True

    def search(n):
        nonlocal nodes
        nodes += 1
        if n == L5:
            return "".join(assigned) if all(acc[i]==cs[i] for i in range(G)) else None
        U_after = (L5 - n) - 1
        best_p = None; best_len = None; best_d = None
        for p in range(L5):
            if assigned[p] is not None:
                continue
            digs = [d for d in range(10) if feasible(p, d, U_after)]
            if not digs:
                return None
            if best_len is None or len(digs) < best_len:
                best_len = len(digs); best_p = p; best_d = digs
                if best_len == 1:
                    break
        for d in best_d:
            assigned[best_p] = str(d)
            for i in range(G):
                if gd[i][best_p] == d:
                    acc[i] += 1
            r = search(n+1)
            if r is not None:
                return r
            for i in range(G):
                if gd[i][best_p] == d:
                    acc[i] -= 1
            assigned[best_p] = None
        return None

    t0=time.time()
    sol = search(0)
    dt=time.time()-t0
    print(f"L5 method-A (plain): sol={sol} nodes={nodes} time={dt:.3f}s", flush=True)

solve5()
