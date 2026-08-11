"""Structural analysis of the PE763 growth rule for the research role.

Growth rule (d dimensions): start with {origin}. In one step replace one
monomial/point p by its d forward-neighbor children (p+e_i, i=1..d),
provided all d children slots are empty in the current set; parent removed.
Count DISTINCT reachable sets after N steps.

We verify:
 A) reverse-merge characterization: a set is reachable from {origin} iff
    there is a sequence of "forward merges" (replace the d children of a
    common parent by the parent, valid when parent currently absent)
    reducing it to the singleton {origin}.
 B) compute D(N) in d=2 (the 2D analog, likely in OEIS) and d=3, by BFS.
"""
from functools import lru_cache


def children(p, d):
    return tuple(sorted(list(p[:i]) + [p[i] + 1] + list(p[i + 1:]) for i in range(d)))


def one_step(level, d):
    """All distinct sets reachable in one division from any set in `level`."""
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p, d)
            if all(c not in Sset for c in ch):
                ns = (Sset - {p}) | set(ch)
                nxt.add(tuple(sorted(ns)))
    return nxt


def D_bfs(N, d):
    """D(0..N) by exact BFS on frozensets."""
    level = {((0,) * d,)}  # singleton at origin
    out = [1]
    for n in range(1, N + 1):
        level = one_step(level, d)
        out.append(len(level))
    return out


def reverse_merge_reducible(S, d, memo):
    """Can set S (as frozenset) be reduced to the singleton {origin} by
    forward merges?  A forward merge of cube p needs its d children all in
    S and p not in S; replaces the children by p."""
    key = frozenset(S)
    if key in memo:
        return memo[key]
    if key == frozenset([(0,) * d]):
        memo[key] = True
        return True
    Sset = set(S)
    # a merge adds a parent that is currently absent
    # candidate parents: any p=(x1,..,xd)>=0 with p not in S whose children all in S
    for p in _forbidden(Sset, d):
        ch = children(p, d)
        if all(c in Sset for c in ch):
            ns = (Sset - set(ch)) | {p}
            if reverse_merge_reducible(ns, d, memo):
                memo[key] = True
                return True
    memo[key] = False
    return False


def _forbidden(Sset, d):
    """Set of points with each child a plausible future parent: p not in S,
    but to merge we need children in S.  We just need candidate parents p
    whose children are in S.  Since children of p have sum one more than p,
    enumerate points one level below the occupied levels."""
    lv = set()
    for pt in Sset:
        # p can be at most one less than an occupied point in some coord
        pass
    # simpler: try parents obtained by decrementing one coordinate of an occupied child
    cands = set()
    for c_pt in Sset:
        for i in range(d):
            if c_pt[i] > 0:
                pnew = list(c_pt)
                pnew[i] -= 1
                cands.add(tuple(pnew))
    # also include all points p not in S within bounding box (cheap for small cases)
    xs = [pt[i] for pt in Sset for i in []]  # placeholder
    return cands


if __name__ == "__main__":
    print("== 2D analog D(N), N=0..14 ==")
    d2 = D_bfs(14, 2)
    print(d2)

    print("\n== 3D D(N), N=0..10 (cheap) ==")
    d3 = D_bfs(10, 3)
    print(d3)
