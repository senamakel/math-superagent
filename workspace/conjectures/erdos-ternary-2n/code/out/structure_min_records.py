import sys
from math import inf

def good_low(k, x):
    for _ in range(k):
        if x % 3 == 2:
            return False
        x //= 3
    return True

def main(kmax, K_death):
    # ---- part 1: survivor tree, strings, min non-witness survivor ----
    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    sets = [sorted(members)]
    mod_old = 2
    for k in range(2, kmax + 1):
        nxt = []
        for c in members:
            for j in (0, 1, 2):
                cand = c + j * mod_old
                if good_low(k, pow(2, cand, 3 ** k)):
                    nxt.append(cand)
        members = nxt
        sets.append(sorted(members))
        mod_old = 2 * 3 ** (k - 1)

    # every binary string starting with '1' occurs: check via digit streams
    for k in range(1, min(kmax, 12) + 1):
        streams = set()
        for c in sets[k-1]:
            r = pow(2, c, 3 ** k)
            digs = []
            for _ in range(k):
                digs.append(r % 3)
                r //= 3
            streams.add(tuple(digs))
        expect = {(1,) + t for t in __import__('itertools').product((0, 1), repeat=k-1)}
        assert streams == expect, (k, len(streams), len(expect))
    print(f"A_k classes = all binary digit-strings starting with '1', verified k=1..{min(kmax,12)}")

    # min non-witness survivor
    W = {0, 2, 8}
    print("k : |A_k| : min non-witness survivor m_k  (moduli 2*3^(k-1))")
    for k in range(1, kmax + 1):
        nw = [c for c in sets[k-1] if c not in W]
        m = min(nw) if nw else None
        print(f"{k:2d} {len(sets[k-1]):9d} {m}")
    mins = [min([c for c in sets[k-1] if c not in W] or [None]) for k in range(1, kmax+1)]
    print("m_k sequence:", mins)

    # ---- part 2: D(n) for integers n, records ----
    if K_death:
        M = min(200000, 2 * 3 ** (K_death - 1))
        best = []
        hist = {}
        for n in range(M):
            d = None
            for k in range(1, K_death + 1):
                if not good_low(k, pow(2, n, 3 ** k)):
                    d = k
                    break
            if d is None:
                d = -1  # survives all levels up to K_death (includes non-integer survivors)
            hist[d] = hist.get(d, 0) + 1
            if d >= 0 and (not best or d > best[-1][1]):
                best.append((n, d))
        print(f"D(n) histogram for n < {M}, levels 1..{K_death}:")
        for d in sorted(hist):
            print(f"  D={d:3d}: {hist[d]}")
        print("record D values (n, D):", best)

if __name__ == "__main__":
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    K_death = int(sys.argv[2]) if len(sys.argv) > 2 else 14
    main(kmax, K_death)