"""Attack the layer-extremality structural conjecture with the exact oracle.

For the VERIFIED es_construct ES construction X_n (n points in general
position, largest convex subset = n-1, i.e. n-avoiding), peel the onion layers
and ask whether every layer is "as convex as the n-avoiding constraint allows":

  * a layer of size m >= n-1 must contain n-1 points in convex position;
  * a layer of size m <  n-1 must be entirely in convex position (a convex
    m-gon).

If so, ALL the no-convex-n-gon obstruction lives strictly *across* layers:
each layer individually is maximally convex, and convexity is broken only by
taking points from two or more layers together.  This is a precise, exact,
decidable statement about the extremal template, and the thread's next step.

Largest-convex-subset is exact (es_geom.largest_convex_subset), so "contains
n-1 convex points" and "entire layer convex" are exact answers, no floats.

Conjecture C (layer extremality): for n in {5,6,7}, every onion layer of
X_n is maximally convex in the sense above.
"""
from fractions import Fraction
from itertools import combinations
from lib.es_geom import (convex_hull, in_convex_position,
                         has_convex_k_subset, largest_convex_subset,
                         in_general_position)
from lib.es_construct import es_set


def onion_layers(points):
    """Peel convex hulls; return list of layers, outer first."""
    pts = list(points)
    layers = []
    while pts:
        h = convex_hull(pts)
        hset = set(h)
        layers.append([p for p in pts if p in hset])
        pts = [p for p in pts if p not in hset]
    return layers


def check_layer(layer, n):
    """Return (status, detail) for one layer under Conjecture C."""
    m = len(layer)
    if m >= n - 1:
        # must contain n-1 convex points
        ok, witness = has_convex_k_subset(layer, n - 1)
        return ok, f"m={m}: contains convex (n-1)-gon = {ok}"
    else:
        # must be fully convex
        ok = in_convex_position(layer)
        return ok, f"m={m}: entire layer convex = {ok}"


if __name__ == "__main__":
    print("=== Layer-extremality of es_construct ES construction (exact oracle) ===")
    for n in (4, 5, 6, 7):
        S = es_set(n)
        gp = in_general_position(S)
        N = len(S)
        k, _ = largest_convex_subset(S)
        layers = onion_layers(S)
        profile = [len(L) for L in layers]
        all_ok = True
        rows = []
        for j, L in enumerate(layers):
            ok, det = check_layer(L, n)
            all_ok &= ok
            rows.append(f"  layer {j}: {det}")
        print(f"\nn={n}: |X|={N} gp={gp} largestConvex={k} (expect {n-1})")
        print(f"  onion profile: {profile}   sum={sum(profile)}")
        for r in rows:
            print(r)
        print(f"  Conjecture C (all layers maximally convex): {'PASS' if all_ok else 'FAIL'}")
