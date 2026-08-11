"""Test the conjecture C1 about the amoeba process.

Conjecture C1: a set S of cells containing the origin is reachable (via
amoeba divisions) iff S is 'origin-connected': every cell c in S with
c != origin has at least one backward-neighbour in S, i.e. at least one of
c-e1, c-e2, c-e3 (whichever have coords >= 0) is in S.

We test the *counting* version: the number of origin-connected sets of the
same size as reachable sets at generation N, compared with D(N).

Size at generation N:
  * 2D: an amoeba divides into 2, so after N divisions a config holds N+1
    cells.  The comparing size is therefore N+1 (the task text says 2N+1,
    but that is the 3D size; in 2D the correct matching size is N+1).
  * 3D: an amoeba divides into 3, so after N divisions a config holds 2N+1
    cells.

Structure fact used to make enumeration finite and exact: in any
origin-connected set of size m the max coordinate is <= m-1.  Indeed every
non-origin cell traces a strictly-coordinate-sum-decreasing backward path to
the origin using cells of S, and a sum decreasing by >=1 per step from sum s
reaches 0 in at most s <= m-1 steps, bounding every coordinate by m-1.  So
origin-connected sets of size m live in the finite box [0,m-1]^d and can be
enumerated without visiting an infinite grid.

Enumeration (not reachable-set BFS): a set S is origin-connected iff S can be
grown from {origin} by repeatedly adding a cell that already has a backward
neighbour in S.  The set of cells with a backward neighbour in S is exactly
the set of forward neighbours of S (c has backward neighbour c-e_i in S iff
c = (c-e_i)+e_i is a forward neighbour of some s in S).  So level m+1 is
obtained from level m by adding one forward neighbour.  We dedupe any set
that arises from several orders, and count distinct sets of each size.

Reachable sets in 2D come from amoeba2d.d2d (existing, verified);
in 3D from lib/amoeba D values.
"""

from amoeba2d import d2d
import sys

# ---- origin-connected enumeration ---------------------------------------


def _forward_neighbours(cell, dim):
    """Forward (+e_i) neighbours of a cell."""
    out = []
    for i in range(dim):
        out.append(tuple(c + (1 if j == i else 0) for j, c in enumerate(cell)))
    return out


def count_origin_connected(dim, sizes):
    """Count origin-connected sets of each target size (sizes: list[int]).

    Returns list aligned with `sizes`: the number of distinct origin-connected
    sets containing (0,...,0) of that size.  dim in {2,3}.
    """
    target = set(sizes)
    counts = {}
    origin = (0,) * dim
    level = {frozenset({origin})}
    size = 1
    if size in target:
        counts[size] = len(level)
    while level and size < max(sizes):
        nxt = set()
        for S in level:
            Sset = set(S)
            for cell in S:
                for nb in _forward_neighbours(cell, dim):
                    if nb not in Sset:
                        ns = Sset | {nb}
                        nxt.add(frozenset(ns))
        level = nxt
        size += 1
        print(f"  [dim={dim}] size m={size}: {len(level)} origin-connected sets", flush=True)
        if size in target:
            counts[size] = len(level)
    return [counts[s] for s in sizes]


def main():
    # ---- 2D comparison, sizes N+1 for N = 0..12 -------------------------
    Nmax2 = 12
    print(f"=== 2D (size N+1), N = 0..{Nmax2} ===", flush=True)
    print(f"{'N':>3} {'D_2D(N)':>10} {'C1_2D(N)':>10}  equal?", flush=True)
    D2 = [d2d.D_2D(n) for n in range(Nmax2 + 1)]
    sizes2 = [n + 1 for n in range(Nmax2 + 1)]
    C1_2 = count_origin_connected(2, sizes2)
    all_eq2 = True
    for n in range(Nmax2 + 1):
        eq = D2[n] == C1_2[n]
        all_eq2 &= eq
        print(f"{n:>3} {D2[n]:>10} {C1_2[n]:>10}  {eq}", flush=True)
    print(f"C1_2D list (N=0..{Nmax2}): {C1_2}", flush=True)
    print(f"C1_2D(N) == D_2D(N) for all N: {all_eq2}\n", flush=True)

    # ---- 3D comparison, sizes 2N+1 for N = 0..9 -------------------------
    if "--2d-only" not in sys.argv:
        run_3d()


def run_3d():
    Nmax3 = 9
    print(f"=== 3D (size 2N+1), N = 0..{Nmax3} ===", flush=True)
    print(f"{'N':>3} {'D(N)':>10} {'C1_3D(N)':>10}  equal?", flush=True)
    D3 = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086][: Nmax3 + 1]
    sizes3 = [2 * n + 1 for n in range(Nmax3 + 1)]
    C1_3 = count_origin_connected(3, sizes3)
    all_eq3 = True
    for n in range(Nmax3 + 1):
        eq = D3[n] == C1_3[n]
        all_eq3 &= eq
        print(f"{n:>3} {D3[n]:>10} {C1_3[n]:>10}  {eq}", flush=True)
    print(f"C1_3D list (N=0..{Nmax3}): {C1_3}", flush=True)
    print(f"C1_3D(N) == D(N) for all N: {all_eq3}", flush=True)


if __name__ == "__main__":
    main()
