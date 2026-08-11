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
