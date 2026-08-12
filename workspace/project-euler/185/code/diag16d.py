#!/usr/bin/env python3
"""Strong-av probe with progress output and lower cap."""
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
    gd = [[int(ch) for g in [guesses] for ch in g] for guesses in guesses]
    gd = [[int(ch) for ch in g] for g in guesses]
    assigned = [None] * L16
    nodes = 0
    found = [None]
    t0 = time.time()
    last = [t0]

    def search(n, acc):
        nonlocal nodes
        nodes += 1
        if found[0] is not None or nodes > node_cap:
            return
        if time.time() - last[0] > 10:
            print(f"  ... nodes={nodes} depth={n} "
                  f"rate={nodes/(time.time()-t0):.0f}/s", flush=True)
            last[0] = time.time()
        if n == L16:
            if all(acc[i] == cs[i] for i in range(G)):
                found[0] = "".join(assigned)
            return
        unlist = [p for p in range(L16) if assigned[p] is None]
        # feasible sets per position
        feas = {}
        for p in unlist:
            fs = []
            for d in range(10):
                ok = True
                for i in range(G):
                    if acc[i] + (1 if gd[i][p] == d else 0) > cs[i]:
                        ok = False; break
                if ok:
                    fs.append(d)
            if not fs:
                return
            feas[p] = fs
        # strong av bound
        for i in range(G):
            av = 0
            for p in unlist:
                if gd[i][p] in feas[p]:
                    av += 1
            if acc[i] + av < cs[i]:
                return
        best_p = None; best_d = None
        for p in unlist:
            fs = feas[p]
            if best_d is None or len(fs) < len(best_d):
                best_p = p; best_d = fs
        for d in best_d:
            if found[0] is not None:
                return
            assigned[best_p] = str(d)
            na = acc[:]
            for i in range(G):
                if gd[i][best_p] == d:
                    na[i] += 1
            search(n + 1, na)
            assigned[best_p] = None

    search(0, [0]*G)
    dt = time.time() - t0
    print(f"[strong-av] sol={found[0]} nodes={nodes} time={dt:.2f}s "
          f"rate={nodes/dt:.0f}/s", flush=True)


print("=== L16 strong-av, cap 2M ===", flush=True)
run(2_000_000)
