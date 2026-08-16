"""WITNESS HUNT for COLLAPSE, n=2..20, fully vectorized with numpy.

Primary fiber: C_K(h) = pair-correlation counts N_ab(k) for k=1..K.
S(n,h)^2 computed once for all h from fold-row masks (parity of popcount of
mask&h), then s2's constancy within equal-key fibers checked by lexicographic
sort of the key matrix.

Monotonicity used: 'no witness at K' is upward closed (C_{K+1} refines C_K), so
K* = smallest K with no witness; witnesses exist exactly for K < K*.

Secondary literal fiber (interval inner products, length<=K) is degenerate
(K=1 recovers h), reported separately.

Output: code/out/witness_hunt_n20.txt
"""
import sys, os
import numpy as np
from lib.collapse import downset


def build(n):
    N = 1 << n
    bits = np.empty((N, n), dtype=np.uint8)
    hh = np.arange(N, dtype=np.uint64)
    for i in range(n):
        bits[:, i] = (hh >> i) & 1
    # S(n,h) for all h
    tot = np.zeros(N, dtype=np.int64)
    for d in range(2, n):
        mask = 0
        for pos in downset(d, n):
            mask |= 1 << pos
        # parity of popcount(mask & h): precompute per-h popcount of mask&h
        t = np.array([((h & mask).bit_count() & 1) for h in range(N)], dtype=np.int64)
        tot -= 2 * t
    s2 = (tot + (n - 2)).astype(np.int64) ** 2
    return bits, s2


def witness_exists(bits, s2, n, K, N):
    """True iff two strings with equal C_K have different S^2 (primary fiber)."""
    key = np.empty((N, 4 * K), dtype=np.int64)
    for k in range(1, K + 1):
        a = bits[:, :-k].astype(np.int64)
        b = bits[:, k:].astype(np.int64)
        c00 = (1 - a) * (1 - b)
        c01 = (1 - a) * b
        c10 = a * (1 - b)
        c11 = a * b
        col = (k - 1) * 4
        key[:, col] = c00.sum(axis=1)
        key[:, col + 1] = c01.sum(axis=1)
        key[:, col + 2] = c10.sum(axis=1)
        key[:, col + 3] = c11.sum(axis=1)
    # lexicographic sort by all key columns (last column most significant -> sort reversed cyclic)
    order = np.lexsort([key[:, c] for c in range(key.shape[1] - 1, -1, -1)])
    kk = key[order]
    ss = s2[order]
    # a witness exists iff within a group of equal keys the s2 values differ
    rowkey = (np.zeros(N, dtype=bool))
    # mark boundaries of key changes
    neq = np.ones(N, dtype=bool)
    if N > 1:
        neq[1:] = (kk[1:] != kk[:-1]).any(axis=1)
    # group id via cumsum of neq
    gid = np.cumsum(neq) - 1
    # per group: check min and max s2 equal
    # use np.minimum.at / maximum.at
    gmin = np.full(gid.max() + 1, np.iinfo(np.int64).max)
    gmax = np.full(gid.max() + 1, np.iinfo(np.int64).min)
    np.minimum.at(gmin, gid, ss)
    np.maximum.at(gmax, gid, ss)
    return bool((gmin != gmax).any())


def witness_exists_interval(bits, n, K, N):
    """Literal interval-inner-product fiber; returns True if a witness exists."""
    keys = np.empty((N, 0), dtype=np.int8)
    # build per-row key incrementally; store as set for simplicity on small N
    lookup = set()
    for h in range(N):
        row = bits[h]
        key = []
        for l in range(n):
            acc = 0
            for r in range(l, min(n, l + K)):
                acc ^= int(row[r])
                key.append(acc)
        lookup.add(tuple(key))
    return len(lookup) < N


def main():
    out_lines = []
    for n in range(2, 21):
        N = 1 << n
        bits, s2 = build(n)
        maxK = n - 1
        Kstar = None
        for K in range(1, maxK + 1):
            if not witness_exists(bits, s2, n, K, N):
                Kstar = K
                break
        wit = {}
        for K in {1, 2, 3, n - 1}:
            if 1 <= K <= maxK:
                wit[K] = witness_exists(bits, s2, n, K, N)
        # secondary: minimal K with no witness under interval fiber
        ik = None
        for K in range(1, maxK + 1):
            if not witness_exists_interval(bits, n, K, N):
                ik = K
                break
        line = (f"n={n:2d} K*(primary)={Kstar} "
                f"witness@K=1:{wit.get(1)} K=2:{wit.get(2)} K=3:{wit.get(3)} "
                f"K=n-1:{wit.get(n - 1)} | interval-K*={ik}")
        out_lines.append(line)
    ys = [t for t in []]
    # fit growth: parse K* from out_lines
    vals = []
    for ln in out_lines:
        m = ln.split("K*(primary)=")[1].split(" ")[0]
        vals.append(None if m == "None" else int(m))
    nlist = list(range(2, 21))
    out_lines.append("")
    pts = [(nlist[i], vals[i]) for i in range(len(vals)) if vals[i] is not None]
    out_lines.append("K*(primary) vs n: " + " ".join(f"n={n}:{v}" for n, v in pts))
    if len(pts) >= 2:
        ratios = [pts[i + 1][1] / pts[i][1] for i in range(len(pts) - 1) if pts[i][1]]
        out_lines.append("successive ratios: " + " ".join(f"{r:.3f}" for r in ratios))
    txt = "\n".join(out_lines) + "\n"
    with open("code/out/.wit.tmp", "w") as f:
        f.write(txt)
    os.replace("code/out/.wit.tmp", "code/out/witness_hunt_n20.txt")
    sys.stdout.write(txt)


if __name__ == "__main__":
    main()
