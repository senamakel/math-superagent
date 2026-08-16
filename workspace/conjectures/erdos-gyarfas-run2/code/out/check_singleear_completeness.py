"""Test whether the girth-6 class at level n is exactly reproduced by
single-length-1-ear + chord extension from cached level n-1 graphs.

If TRUE, then a resume that only re-processes the level-(n-1) graphs with
k=1 ears (plus chord-closure to handle same-level chord additions) is COMPLETE
— no lower-level re-processing is needed, and extending to n=16 costs only the
level-15-to-16 increment instead of a full regeneration.

Mutates nothing. Loads girth6_class_n15.json, builds the level-15 -> level-16
candidate via single ears + chord closure, and compares to the cached full
level-15 class (both forwards-completeness to 16 requires level-16 reference,
which we test empirically HERE by regressing: level-14 -> level-15 closure vs
the cached level-15 class).
"""
import json, os, sys, time
import networkx as nx
from lib.girth6_gen import girth, _add_path_ear, _add_chord

OUT = os.path.join(os.path.dirname(__file__))

def load_cache(n):
    data = json.load(open(os.path.join(OUT, f"girth6_class_n{n}.json")))
    levels = {}
    for rec in data:
        levels.setdefault(rec["n"], []).append(nx.Graph(rec["edges"]))
    return levels

def canonical(G):
    from lib.canonical import canonical_key
    return canonical_key(G)

def closure_singleear(base_level, min_girth=6, also_chords=True):
    """From graphs in base_level, produce new candidates at size+1 via k=1 ears
    (and, if also_chords, chords within base_level — but chords stay in level so
    they duplicate existing, skip for forward test). Return list of Graphs."""
    results = {}
    seen = {}
    def try_add(H):
        m = H.number_of_nodes()
        if girth(H) < min_girth:
            return
        k = canonical(H)
        if k not in seen:
            seen[k] = H
            results.setdefault(m, []).append(H)
    for G in base_level:
        verts = list(G.nodes())
        for u in verts:
            for v in verts:
                if u == v:
                    continue
                H = _add_path_ear(G, u, v, 1)
                try_add(H)
    return results

def main(n):
    # forward-from-(n-1) reproduces level n of the cached class?
    # n is the TOP level; the class up to n is in the n15-style cache. Find it.
    cache_top = 15 if os.path.exists(os.path.join(OUT, "girth6_class_n15.json")) else n
    levels = load_cache(cache_top)
    if n not in levels:
        print(f"level {n} missing from cache_to_{cache_top}; cannot test")
        return None
    base = levels[n - 1]
    closure = closure_singleear(base)
    cand = closure.get(n, [])
    ref = levels[n]
    ref_canon = {canonical(G) for G in ref}
    cand_canon = {canonical(G) for G in cand}
    print(f"level {n-1} -> level {n}: cached level-{n} class = {len(ref_canon)} graphs")
    print(f"  single-ear closure produces {len(cand_canon)} distinct level-{n} graphs")
    missing = ref_canon - cand_canon
    extra = cand_canon - ref_canon
    print(f"  MISSING from closure (in cached class, not produced): {len(missing)}")
    print(f"  EXTRA from closure (not in cached class): {len(extra)}")
    ok = not missing and not extra
    print(f"  => single-ear extension COMPLETE for level {n-1}->{n}: {ok}")
    return ok

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    main(n)
