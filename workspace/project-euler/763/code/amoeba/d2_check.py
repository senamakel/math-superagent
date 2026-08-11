"""Frozenset oracle for the 2D amoeba, to validate the bitmask BFS.

One step: an amoeba at (x,y) divides into two at (x+1,y) and (x,y+1) provided
both are empty; parent disappears.  Returns D2(N) for N=0..max_n by exact
frozenset BFS.  Simple and obviously faithful; used only as the small-N oracle.
"""

import sys

from lib.amoeba2d import next_level_bits2_compact


def frozenset_next(level):
    nxt = set()
    for cells in level:
        for (x, y) in cells:
            na = (x + 1, y)
            nb = (x, y + 1)
            if na in cells or nb in cells:
                continue
            child = set(cells)
            child.discard((x, y))
            child.add(na)
            child.add(nb)
            nxt.add(frozenset(child))
    return nxt


def oracle(max_n):
    level = {frozenset({(0, 0)})}
    results = [1]
    for n in range(1, max_n + 1):
        level = frozenset_next(level)
        results.append(len(level))
    return results


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    res = oracle(max_n)

    # cross-check the compact bitmask against the frozenset oracle
    bl = {1}
    W = 1
    bit = [1]
    ok = True
    for n in range(1, max_n + 1):
        bl = next_level_bits2_compact(bl, W)
        W += 1
        bit.append(len(bl))
        if bit[n] != res[n]:
            ok = False
            print(f"MISMATCH at N={n}: fs={res[n]} bits={bit[n]}")
    print("frozenset D2:", res)
    print("bitmask   D2:", bit)
    print("bitmask matches frozenset oracle for N=0..{0}: {1}".format(max_n, ok))


if __name__ == "__main__":
    main()
