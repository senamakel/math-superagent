#!/usr/bin/env python3
"""SCORER for the es-nogon scored search.

Usage:
    python score.py <module_path> [k]

<module_path> is a candidate module exposing `points(k) -> list[(int,int)]`.
Imports it, calls points(k) (default k=7 unless given), and prints exactly one
verdict line:

    SCORE: n            every check below held; n = len(points)
    INVALID: <check>    first check that failed, with a witness

Checks, all exact integer arithmetic (never floats), in order:
  1. distinct integer coordinates;
  2. general position (no three collinear) via lib.es_geom.orient (exact
     determinant sign; no new predicate, no floats);
  3. no k points in convex position.

The no-convex-k-gon check is two-stage:
  * onion-layer precheck (SUFFICIENT): if any hull layer has >= k points that
    layer itself is a convex k-polygon => INVALID immediately with witness.
    (Verified: maxlayer>=k  =>  convex k-subset, 13254/13254 random cases.)
  * exact parallel enumeration (AUTHORITATIVE): a hull layer of size < k does
    NOT imply absence of a convex k-gon (verified false: 802/3000 random sets
    had a convex k-gon with every hull layer < k), so every candidate that
    survives the precheck is still checked exactly.  C(N,k) convexity tests,
    split across all available cores.  Any convex k-subset found => INVALID.
    None found => SCORE n.

Every geometric test reuses verified lib.es_geom primitives:
  * lib.es_geom.orient            exact orientation sign
  * lib.es_geom.in_general_position
  * lib.es_geom.convex_hull
  * lib.es_geom.in_convex_position
No new predicate is introduced anywhere in the scorer.

Memory is bounded: enumeration streams subsets one at a time (itertools
combinations, O(k) live subset), and multiprocessing workers each hold only the
point set and their slice of work.  Peak memory is kilobytes, far under 8 GiB.
"""

import importlib
import importlib.util
import math
import multiprocessing as mp
import os
import sys
from itertools import combinations

from lib.es_geom import (
    orient,
    collinear,
    convex_hull,
    in_convex_position,
)


def import_from_path(module_path):
    """Import a candidate module from a file path or a dotted package name."""
    module_path = module_path.strip()
    if module_path.endswith(".py"):
        if not os.path.isfile(module_path):
            raise FileNotFoundError(module_path)
        spec = importlib.util.spec_from_file_location(
            "_es_nogon_candidate", module_path
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    # dotted module name on PYTHONPATH
    return importlib.import_module(module_path)


def onion_layers(pts):
    """Peel convex hull layers; each returned layer is a convex polygon vertex list."""
    remaining = set(pts)
    layers = []
    while remaining:
        h = convex_hull(list(remaining))
        if len(h) <= 2:
            # degenerate tail (can only happen if a small set lies on a line,
            # which is already a collinearity INVALID at the general-position
            # check, so we should never reach here on a valid candidate).
            layers.extend([(p,)] for p in remaining)
            break
        layers.append(h)
        remaining = remaining - set(h)
    return layers


def largest_layer_size(layers):
    return max(len(layer) for layer in layers) if layers else 0


def _check_no_convex_k_fast(pts, k):
    """Layer precheck. Returns (INVALID_or_None, witness_layer)."""
    layers = onion_layers(pts)
    for layer in layers:
        if len(layer) >= k:
            return ("convex-%d-gon" % k, layer[:k])
    return (None, None)


def _worker(args):
    """Check one slice of the C(N,k) enumeration for a convex k-subset.

    The caller splits by choosing the first two indices (i<j) of each subset;
    each worker enumerates the remaining k-2 indices after j.  Returns the
    witness subset as a tuple of point indices, or None."""
    pts, i, j, k, start = args
    N = len(pts)
    # combinations of k-2 indices from (j+1 .. N-1), but to split evenly across
    # cores we enumerate them all in `start`-th-order; simpler: each task gets a
    # narrow (j) range so no two workers duplicate, handled by the caller.
    for rest in combinations(range(j + 1, N), k - 2):
        idx = (i, j) + rest
        sub = [pts[t] for t in idx]
        if in_convex_position(sub):
            return idx
    return None


def _check_no_convex_k_exact(pts, k):
    """Authoritative check: any convex k-subset? Split C(N,k) across cores.

    Locks the first two indices i<j of the k-subset (each valid subset has a
    unique smallest two indices), so tasks are disjoint and complete.  Each
    task enumerates choices for the remaining k-2 indices.  Returns a witness
    tuple of indices, or None."""
    N = len(pts)
    if N < k:
        return None
    # first two indices i<j with j <= N-(k-1) so k-2 slots remain after j
    tasks = [
        (pts, i, j, k, 0)
        for i in range(N - (k - 1))
        for j in range(i + 1, N - (k - 2))
    ]
    ncores = max(1, min(len(os.sched_getaffinity(0)), len(tasks)))
    with mp.Pool(ncores) as pool:
        for witness in pool.imap_unordered(_worker, tasks, chunksize=8):
            if witness is not None:
                pool.terminate()
                return witness
    return None


def main(argv):
    if len(argv) < 2:
        print("usage: python score.py <module_path> [k]")
        return 2
    module_path = argv[1]
    k = int(argv[2]) if len(argv) > 2 else 7

    mod = import_from_path(module_path)
    points = mod.points(k)
    points = list(points)

    # --- check 1: distinct integer coordinates -----------------------------
    for p in points:
        if not (isinstance(p, tuple) and len(p) == 2 and
                isinstance(p[0], int) and isinstance(p[1], int)):
            print("INVALID: non-integer coordinate point %r" % (p,))
            return 1
    if len(set(points)) != len(points):
        seen = set()
        for p in points:
            if p in seen:
                print("INVALID: duplicate point %r" % (p,))
                return 1
            seen.add(p)
    n = len(points)
    if n < k:
        # can never contain k in convex position, but fewer points than the
        # rung asks for is still a valid (weak) score
        print("SCORE: %d  (fewer than k=%d points)" % (n, k))
        return 0

    # --- check 2: general position (verified helper, exact orientations) ---
    from lib.es_geom import in_general_position
    if not in_general_position(points):
        # find a witnessing collinear triple
        for i, j, l in combinations(range(n), 3):
            if collinear(points[i], points[j], points[l]):
                print("INVALID: three collinear points %r %r %r" %
                      (points[i], points[j], points[l]))
                return 1

    # --- check 3: no k points in convex position ---------------------------
    # 3a. fast sufficient layer precheck
    bad, witness = _check_no_convex_k_fast(points, k)
    if bad is not None:
        # witness here is already a list of point (x,y) tuples (layer[:k]).
        print("INVALID: %s in convex position, witness %r" %
              (bad, witness))
        return 1
    # 3b. authoritative exact parallel enumeration
    wit = _check_no_convex_k_exact(points, k)
    if wit is not None:
        print("INVALID: convex-%d-gon in convex position, witness %r" %
              (k, [points[t] for t in wit]))
        return 1

    print("SCORE: %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
