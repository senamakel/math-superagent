"""Structural analysis of the PE763 growth rule for the research role.

Growth rule (d dimensions): start with {origin}. In one step replace one
point p by its d forward-neighbor children (p+e_i, i=1..d), provided all d
child slots are empty in the current set; parent removed.  Count DISTINCT
reachable sets after N steps.

We verify the reverse-merge characterization (each reachable set can be
reduced to the singleton by repeatedly replacing the d children of a common
parent with the parent, valid when the parent is absent), and compute D(N)
in d=2 and d=3 by exact BFS.
"""


def children(p, d):
    return [tuple(p[i] + (1 if i == j else 0) for i in range(d)) for j in range(d)]


def one_step(level, d):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p, d)
            if all(c not in Sset for c in ch):
                ns = (Sset - {p}) | set(ch)
                nxt.add(frozenset(ns))
    return nxt


def D_bfs(N, d):
    level = {frozenset([(0,) * d])}
    out = [1]
    for n in range(1, N + 1):
        level = one_step(level, d)
        out.append(len(level))
    return out


def reverse_merge_reducible(S, d, memo):
    """Can set S be reduced to the singleton {origin} by repeated forward
    merges?  A merge of cube p is legal when p is absent and its d children
    are all present; it replaces the children by p."""
    key = frozenset(S)
    if key in memo:
        return memo[key]
    if key == frozenset([(0,) * d]):
        memo[key] = True
        return True
    Sset = set(S)
    for p in all_parent_candidates(Sset, d):
        if p in Sset:
            continue
        ch = children(p, d)
        if all(c in Sset for c in ch):
            ns = (Sset - set(ch)) | {p}
            if reverse_merge_reducible(ns, d, memo):
                memo[key] = True
                return True
    memo[key] = False
    return False


def all_parent_candidates(Sset, d):
    """Parents p whose children are all in S.  p is one unit smaller than
    each child in one coordinate, so p's coords are <= some child's.  We
    enumerate p in the bounding box of S and filter below."""
    cands = set()
    xs = [[pt[i] for pt in Sset] for i in range(d)]
    maxes = [max(c) for c in xs]
    from itertools import product
    for box in product(*[range(m + 1) for m in maxes]):
        ch = children(box, d)
        if all(c in Sset for c in ch):
            cands.add(box)
    return cands


if __name__ == "__main__":
    import sys
    print("== d=2 D(N), N=0..14 ==")
    print(D_bfs(14, 2))
    print("\n== d=3 D(N), N=0..12 ==")
    print(D_bfs(12, 3))

    print("\n-- reverse-merge vs forward reachability check (d=2, N<=6) --")
    for N in range(2, 7):
        fwd = D_bfs(N, 2)
        # actually verify on the frontier sets at depth N
        level = {frozenset([(0,) * 2])}
        for _ in range(N):
            level = one_step(level, 2)
        memo = {}
        bad = [S for S in level if not reverse_merge_reducible(S, 2, memo)]
        print(f"N={N}: frontier={len(level)}, reverse-merge failures={len(bad)}")
