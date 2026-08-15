#!/usr/bin/env python3
"""Directly measure, for a set of principled FAMILIES (constructions, not
candidate-set searches), the two defining properties of the upper construction:
   |S| == 2^{n-1}+1        (the size the lower bound is stated for)
   D(S) <= ceil(sqrt(n))   (max internal degree target)

Every family is a closed-form rule F(n) -> subset of {0,1}^n; we neither
enumerate subsets nor search the answer space.  We measure |S| and the full
internal degree distribution exactly (lib.qcube counters + an independent
pure-python counter as cross-check).

Families:
  parity           even total weight (independent; only for orientation)
  parity_plus_one  even class + one fixed odd vertex (known D = n, bad -- check)
  bpp_prefix       "block-prefix-parity": every block-prefix cumulative weight even
  grid_bpp         k x k grid, row-prefix parity zero (n = k^2)
  flat_window      every block weight in [lo,hi] (flat/saturation family)
  single_heavy     at most one block weight >= heavy (saturation)
  product          S = S_a x {0,1}^b product-style recursive screen
This is construction + verification: we report what each family gives at
n=6..10, in particular whether it meets size AND D targets.
"""
import sys, math
from collections import Counter
from lib.qcube import max_internal_degree, internal_degree_distribution


def ceil_sqrt(n):
    r = 1
    while r * r < n:
        r += 1
    return r


def blocks(n, nb):
    sizes = [n // nb + (1 if i < n % nb else 0) for i in range(nb)]
    coords = list(range(n))
    out, at = [], 0
    for s in sizes:
        out.append(coords[at:at + s]); at += s
    return out


def weight(x):
    return bin(x).count('1')


def z(blocks_, x):
    return [sum(1 for c in b if (x >> c) & 1) for b in blocks_]


def fam_parity(n):
    return {x for x in range(1 << n) if weight(x) % 2 == 0}


def fam_parity_plus_one(n):
    S = fam_parity(n)
    # remove one even vertex, add a high-degree odd one? no: keep even class size 2^{n-1}
    # and add a single odd vertex -> size 2^{n-1}+1
    odd = next(x for x in range(1 << n) if weight(x) % 2 == 1)
    S.add(odd)
    return S


def fam_bpp(n, b):
    """Blocks of size b; S = {x : cumulative weight of each prefix of blocks even}."""
    if n % b != 0:
        return None
    nblk = n // b
    bks = blocks(n, nblk)
    S = set()
    for x in range(1 << n):
        w = z(bks, x)
        cum = 0
        ok = True
        for wi in w:
            cum += wi
            if cum % 2 != 0:
                ok = False; break
        if ok:
            S.add(x)
    return S


def fam_grid_bpp(n):
    """n = k^2 grid, row-prefix parity zero (rows are the k blocks of size k)."""
    k = int(math.isqrt(n))
    if k * k != n:
        return None
    S = set()
    bks = blocks(n, k)
    for x in range(1 << n):
        w = z(bks, x)
        cum = 0
        ok = True
        for wi in w:
            cum += wi
            if cum % 2 != 0:
                ok = False; break
        if ok:
            S.add(x)
    return S


def fam_flat_window(n, nb, lo, hi):
    bks = blocks(n, nb)
    S = set()
    for x in range(1 << n):
        w = z(bks, x)
        if all(lo <= wi <= hi for wi in w):
            S.add(x)
    return S


def fam_single_heavy(n, nb, heavy):
    bks = blocks(n, nb)
    S = set()
    for x in range(1 << n):
        w = z(bks, x)
        if sum(1 for wi in w if wi >= heavy) <= 1:
            S.add(x)
    return S


def measure(n, S, label):
    if S is None:
        return None
    size = len(S)
    target = (1 << (n - 1)) + 1
    maxdeg = max_internal_degree(n, S) if size else None
    dist = internal_degree_distribution(n, S) if size else {}
    # independent cross-check
    Sset = set(S)
    ck = Counter()
    for v in S:
        d = sum(1 for k in range(n) if (v ^ (1 << k)) in Sset)
        ck[d] += 1
    if size:
        assert max(ck) == maxdeg and dict(ck) == dict(dist), "cross-check failed"
    return dict(label=label, size=size, target=target, maxdeg=maxdeg, dist=dist,
                size_ok=(size == target))


def report_line(r, bound, hits):
    s = f"  {r['label']:<26} |S|={r['size']:<5} target={r['target']} size_ok={r['size_ok']}"
    s += f"  D={r['maxdeg']} (<= {bound}: {'YES' if r['maxdeg'] is not None and r['maxdeg']<=bound else 'no'})"
    if r.get('dist'):
        s += f"  dist={dict(sorted(r['dist'].items()))}"
    if r['size_ok'] and r['maxdeg'] is not None and r['maxdeg'] <= bound:
        s += "   *** HIT ***"
        hits.append(r['label'])
    return s


def main():
    ns = [int(x) for x in sys.argv[1:]] or [6, 7, 8, 9, 10]
    print("ceil(sqrt n):", {n: ceil_sqrt(n) for n in ns})
    print()
    allhits = {n: [] for n in ns}
    for n in ns:
        bound = ceil_sqrt(n)
        print(f"===== n={n}  ceil(sqrt)={bound}  target |S|={ (1<<(n-1))+1 } =====")
        hits = allhits[n]
        families = [
            ("parity", fam_parity(n)),
            ("parity+one(known bad)", fam_parity_plus_one(n)),
        ]
        for b in (2, 3):
            families.append((f"bpp_prefix(b={b})", fam_bpp(n, b)))
        families.append(("grid_bpp(k^2)", fam_grid_bpp(n)))
        for nb in (2, 3):
            for (lo, hi) in ((0, 1), (1, 2), (0, 2), (1, 3)):
                families.append((f"flat[{lo},{hi}] nb={nb}", fam_flat_window(n, nb, lo, hi)))
        for nb in (2, 3):
            families.append((f"single_heavy2 nb={nb}", fam_single_heavy(n, nb, 2)))
            families.append((f"single_heavy3 nb={nb}", fam_single_heavy(n, nb, 3)))
        for (lab, S) in families:
            r = measure(n, S, lab)
            if r is None:
                print(f"  {lab:<26} n/a")
                continue
            print(report_line(r, bound, hits))
        print()
    print("======= SUMMARY: which families hit |S| and D targets =======")
    for n in ns:
        print(f"  n={n}: HIT -> {allhits[n]}")
    print("DONE")


if __name__ == "__main__":
    main()
