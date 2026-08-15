#!/usr/bin/env python3
"""Rebuild and directly verify an explicit UPPER construction:
an S subset of {0,1}^n with |S| = 2^{n-1}+1 and D(S) <= ceil(sqrt(n)).

This is the missing upper leg of f(n) = Theta(sqrt n).  We do NOT search over
candidate vertex-sets; we fix a parametric *family* (a construction) and
measure, directly and exactly, its size and its max internal degree for each n.
The family that meets the target |S| = 2^{n-1}+1 and D(S) <= ceil(sqrt n) at
n = 6..10 is the construction; anything else is reported as how far it fell.

Families implemented (all F: n and args -> set of ints 0..2^n-1):

  A  "block-prefix-parity zero": blocks of size b; S = {x : for every prefix
     the parity of the total weight is zero}).  This is the task's "simplest
     candidate".  (Given |S| must be ~ half, only the last-parity reading has
     the right size; we measure that reading too.)
  B  "flat block window": partition into blocks, keep vertices whose block
     weight-vector lies in a product of windows  [lo,hi] (per-block).
  C  "single-heavy-block": at most one block has weight >= 2 (others <= 1).
  D  "two-block product": split coordinates into two chunks, S = S1 (x) X ...
     along the recursive/product idea of the statement.

Every degree is measured with lib.qcube's exact integer counter (a second,
independent pure-python counter is used as a cross-check).
"""
import sys, math
from collections import Counter
from lib.qcube import max_internal_degree, internal_degree_distribution


def ceil_sqrt(n):
    r = 1
    while r * r < n:
        r += 1
    return r


def block_partition(n, nb):
    """Partition coords [0..n) into `nb` roughly equal blocks.

    Returns list of lists of coordinate indices.  Larger blocks first.
    """
    sizes = [n // nb + (1 if i < n % nb else 0) for i in range(nb)]
    coords = list(range(n))
    blocks, at = [], 0
    for s in sizes:
        blocks.append(coords[at:at + s])
        at += s
    return blocks


def block_weights(x, blocks):
    return [sum(1 for c in blk if (x >> c) & 1) for blk in blocks]


# ---------------- families ----------------

def fam_prefix_parity(n, b):
    """Blocks of size b over n coords; S = {x : total weight even}.

    The 'block-prefix-parity is zero' candidate in its size-correct reading.
    """
    if n % b != 0:
        return None
    S = {x for x in range(1 << n) if bin(x).count('1') % 2 == 0}
    return S


def fam_flat_window(n, nb, lo, hi):
    """Keep vertices with EVERY block weight in [lo, hi] (product of windows)."""
    blocks = block_partition(n, nb)
    S = set()
    for x in range(1 << n):
        w = block_weights(x, blocks)
        if all(lo <= wi <= hi for wi in w):
            S.add(x)
    return S


def fam_single_heavy(n, nb, heavy=2):
    """S = {x : at most one block has weight >= `heavy`}."""
    blocks = block_partition(n, nb)
    S = set()
    for x in range(1 << n):
        w = block_weights(x, blocks)
        if sum(1 for wi in w if wi >= heavy) <= 1:
            S.add(x)
    return S


def fam_two_level(n, a, b, t):
    """Recursive/product: split n into chunk of size a and chunk of size b.
    Vertices: (u, v).  Keep all pairs where Hamming(u) <= t and v ranges over
    Q_b half, OR Hamming(u) > t and v ranges over the other half -- a product
    along one slice.  Parametrized by (a,b,t)."""
    NA, NB = 1 << a, 1 << b
    S = set()
    for u in range(NA):
        w = bin(u).count('1')
        half = sum(1 << j for j in range(b))  # bottom half selection not exact
        # keep v with a fixed parity per u-region
        for v in range(NB):
            vpar = bin(v).count('1') & 1
            choose = (vpar == 0) if w <= t else (vpar == 1)
            if choose:
                S.add((u << b) | v)
    return S


# ---------------- measurement ----------------

def measure(n, S, label):
    if S is None:
        print(f"  {label}: n/a (family does not apply)")
        return None
    size = len(S)
    target = (1 << (n - 1)) + 1
    if size != target:
        return {'label': label, 'n': n, 'size': size, 'target': target,
                'max_deg': None, 'ok_size': False, 'dist': None}
    maxdeg = max_internal_degree(n, S)
    dist = internal_degree_distribution(n, S)
    # independent pure-python cross-check
    Sset = set(S)
    ck = Counter()
    for v in S:
        d = sum(1 for k in range(n) if (v ^ (1 << k)) in Sset)
        ck[d] += 1
    ckmax = max(ck)
    assert ckmax == maxdeg and dict(ck) == dict(dist), "cross-check mismatch"
    return {'label': label, 'n': n, 'size': size, 'target': target,
            'max_deg': maxdeg, 'ok_size': True, 'dist': dict(dist)}


def main():
    ns = [int(x) for x in sys.argv[1:]] or [6, 7, 8, 9, 10]
    print("targets:  n -> ceil(sqrt n):",
          {n: ceil_sqrt(n) for n in ns})
    print()

    results = {n: [] for n in ns}
    for n in ns:
        bound = ceil_sqrt(n)
        print(f"=== n={n}  target |S|={ (1<<(n-1))+1 }, D-target={bound} ===")

        # A: prefix parity (parity class) -- expect D very large (failure, recorded)
        b = 1
        S = fam_prefix_parity(n, b)
        r = measure(n, S, f"A prefix-parity(b={b})")
        results[n].append(r)
        if r: print(f"  A parity : size={r['size']} D={r['max_deg']} "
                    f"hit_target={r['ok_size'] and r['max_deg']<=bound}")

        # simple family B: flat window, single block (= whole cube slice)
        # single-block window: S = {x : lo <= weight <= hi}
        for (lo, hi) in [(1, n - 1), (0, n - 1)]:
            S = fam_flat_window(n, 1, lo, hi)
            r = measure(n, S, f"B weight-window[{lo},{hi}] (1 block)")
            results[n].append(r)
            if r and r['ok_size']:
                print(f"  B window[{lo},{hi}] : size={r['size']} D={r['max_deg']} "
                      f"hit_target={r['max_deg']<=bound}")
        break_outer = False

        # family C: multi-block, single heavy block
        for nb in (2, 3, 4, 5):
            if nb > n:
                continue
            S = fam_single_heavy(n, nb, heavy=2)
            r = measure(n, S, f"C single-heavy(nb={nb})")
            results[n].append(r)
            if r and r['ok_size'] and r['max_deg'] is not None:
                print(f"  C single-heavy(nb={nb}) : size={r['size']} D={r['max_deg']} "
                      f"hit_target={r['max_deg']<=bound}")

        # family D: flat window over many blocks (empirical scan)
        for nb in (2, 3, 4, 5, 6):
            if nb > n:
                continue
            for (lo, hi) in [(0, 1), (1, 2), (0, 2), (1, 3)]:
                S = fam_flat_window(n, nb, lo, hi)
                r = measure(n, S, f"D window{lo}-{hi}(nb={nb})")
                results[n].append(r)
                if r and r['ok_size']:
                    flag = "  <== HIT" if r['max_deg'] <= bound else ""
                    print(f"  D window[{lo},{hi}] nb={nb} : size={r['size']} "
                          f"D={r['max_deg']} hit={r['max_deg']<=bound}{flag}")
        print()

    # summary of hits
    print("\n================ SUMMARY ================")
    for n in ns:
        bound = ceil_sqrt(n)
        hits = [r for r in results[n]
                if r and r['ok_size'] and r['max_deg'] is not None
                and r['max_deg'] <= bound]
        target_size = (1 << (n - 1)) + 1
        exact_hit = [r for r in results[n]
                     if r and r['size'] == target_size
                     and r['max_deg'] is not None and r['max_deg'] <= bound]
        print(f"n={n}: families with correct-size AND D<={bound}: "
              f"{[(r['label'], r['max_deg']) for r in exact_hit]}")
        if exact_hit:
            print(f"   -> achieving construction: {exact_hit[0]['label']}")
    print("\nDONE")


if __name__ == "__main__":
    main()
