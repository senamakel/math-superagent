"""Reusable routines for the 2D amoeba problem (Project Euler 763 in d=2).

Reachability: an amoeba at p=(x,y) may divide into two amoebas at the
positive-unit neighbours (x+1,y) and (x,y+1) provided those two cubes are
empty; the parent disappears.  After N divisions a config holds N+1 cubes,
each coordinate in [0,N].  D2(N) is the number of DISTINCT sets of occupied
cubes reachable after exactly N divisions.

The state space in d=2 grows far more slowly than in d=3, so exact BFS
reaches much higher N here.

Encodings supported:
  * frozenset of (x,y) tuples
  * int bitmask: bit index x*W + y, grid width W
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def G(k, m):
    """A007902 auxiliary G(k, m): counts 2D reachable configs with k pebbles
    whose extra/top structure sits at level m.  Returns 0 for k < 1.

    The recurrence below is translated from the OEIS A007902 entry (Alois P.
    Heinz).  Correctness established by reproducing OEIS A007902 a(1..33)
    exactly (incl. a(22)=13686805) and by matching the independent 2D BFS
    oracle code/amoeba2d/d2d.py on a(1..14).
    """
    if k < 1:
        return 0
    if m == 0:
        return 2 * G(k - 1, 0) + G(k, 1) + (1 if k == 2 else 0)
    if m == 1:
        return G(k - 3, 0) + 2 * G(k - 2, 1) + G(k - 1, 2) + G(k - 4, 1)
    # m >= 2
    return G(k - m - 2, m - 1) + 2 * G(k - m - 1, m) + G(k - m, m + 1)


def a(n):
    """Number of reachable 2D amoeba configs with n pebbles, OEIS A007902,
    offset 1 (a(1)=1; a(n)=G(n,0) for n>=2)."""
    return 1 if n == 1 else G(n, 0)


def next_level_fs2(level):
    """One BFS step over 2D frozenset-of-tuples configs (exact arithmetic).

    `level` is an iterable of frozensets of (x,y) cells.  Returns the set of
    all distinct configurations reachable by exactly one division: a cell p
    may divide iff both forward neighbours (x+1,y) and (x,y+1) are empty, and
    the result replaces p with those two.  Naive exponential-state oracle
    step, 2D analogue of lib/amoeba.next_level_fs; established correct by the
    2D frozenset oracle and cross-check against the bitmask in
    code/amoeba/d2_check.py.
    """
    nxt = set()
    for S in level:
        Sset = set(S)
        for (x, y) in S:
            a = (x + 1, y)
            b = (x, y + 1)
            if a not in Sset and b not in Sset:
                ns = Sset - {(x, y)} | {a, b}
                nxt.add(frozenset(ns))
    return nxt


def decode_bits2(S, W):
    """Decode an int bitmask (width W) into a frozenset of (x,y) tuples."""
    cells = set()
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, y = divmod(i, W)
        cells.add((x, y))
    return frozenset(cells)


def encode_bits2(cells, W):
    """Encode a set of (x,y) tuples into an int bitmask of width W."""
    S = 0
    for (x, y) in cells:
        S |= 1 << (x * W + y)
    return S


def next_level_bits2_compact(level, W):
    """One BFS step on a set of int-masked 2D configs encoded with grid width W.

    Returns the children encoded with grid width W+1 (coordinates grow to
    [0, W] at the next level).  A cell p divides iff both forward neighbours
    (x+1,y) and (x,y+1) are empty.
    """
    Wp = W + 1
    nxt = set()
    for S in level:
        cells = []
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, y = divmod(i, W)
            cells.append((x, y))

        def occ(x, y):
            return (S >> (x * W + y)) & 1

        for (x, y) in cells:
            a = (x + 1, y)
            b = (x, y + 1)
            free = True
            for (nx, ny) in (a, b):
                # neighbour with a coord == W is outside the parent grid
                if nx < W and ny < W and occ(nx, ny):
                    free = False
                    break
            if not free:
                continue
            child = 0
            for (cx, cy) in cells:
                if (cx, cy) == (x, y):
                    continue
                child |= 1 << (cx * Wp + cy)
            for (nx, ny) in (a, b):
                child |= 1 << (nx * Wp + ny)
            nxt.add(child)
    return nxt
