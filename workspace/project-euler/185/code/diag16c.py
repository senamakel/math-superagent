#!/usr/bin/env python3
"""Probe: strong forward-checking bound av[i] (available future matches per
guess) replaces the loose (b) bound U_after. Test node counts on L16."""
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


def run(node_cap):
    guesses = [g for g, _ in constraints16]
    cs = [c for _, c in constraints16]
    G = len(guesses)
    gd = [[int(ch) for ch in g] for g in guesses]
    assigned = [None] * L16
    acc = [0] * G
    nodes = 0
    found = [None]
    t0 = time.time()

    def feasible(pos, d, acc_now):
        # check incremental placement against all guesses
        for i in range(G):
            na = acc_now[i] + (1 if gd[i][pos] == d else 0)
            if na > cs[i]:
                return False
        return True

    def search(n, acc_now, unassigned_list):
        nonlocal nodes
        nodes += 1
        if found[0] is not None or nodes > node_cap:
            return
        if n == L16:
            if all(acc_now[i] == cs[i] for i in range(G)):
                found[0] = "".join(assigned)
            return
        u = len(unassigned_list)
        # compute per-position feasible sets
        feas_sets = {}
        for p in unassigned_list:
            fs = [d for d in range(10) if feasible(p, d, acc_now)]
            if not fs:
                return
            feas_sets[p] = fs
        # strong lower-bound: av[i] = # unassigned positions that can still
        # match guess i (feasible set contains the guess's digit).
        for i in range(G):
            av = 0
            for p in unassigned_list:
                if gd[i][p] in feas_sets[p]:
                    av += 1
            if acc_now[i] + av < cs[i]:
                return
        # MCV
        best_p = None; best_d = None; best_len = None
        for p in unassigned_list:
            fs = feas_sets[p]
            if best_len is None or len(fs) < best_len:
                best_len = len(fs); best_p = p; best_d = fs
                if best_len == 1:
                    break
        for d in best_d:
            if found[0] is not None:
                return
            assigned[best_p] = str(d)
            new_acc = acc_now[:]
            for i in range(G):
                if gd[i][best_p] == d:
                    new_acc[i] += 1
            new_unassigned = [p for p in unassigned_list if p != best_p]
            search(n + 1, new_acc, new_unassigned)
            assigned[best_p] = None

    init_un = list(range(L16))
    search(0, acc, init_un)
    dt = time.time() - t0
    print(f"[strong-av] sol={found[0]} nodes={nodes} time={dt:.2f}s "
          f"rate={nodes/dt:.0f}/s", flush=True)


print("=== L16 strong-av pruning, cap 50M ===", flush=True)
run(50_000_000)
