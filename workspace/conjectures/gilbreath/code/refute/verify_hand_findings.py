#!/usr/bin/env python3
"""Verify three hand-math findings by exact computation.

F1. R-carved-gap24 (all gaps after the first in {2,4}) is SETTLED by the
    corner argument: for any such sequence, A_2 is the {0,2} corner
    (positions 1.. all in {0,2}), so the leading 1 persists forever.
    Check: exhaustively over ALL gap strings in {2,4} up to a length, the
    leading 1 never dies.  This is an oracle on the small class, plus the
    structural check that every A_2 row is the corner.

F2. The UNCONDITIONAL all-zero-block unreachability sub-claim is FALSE:
    the 2-then-odds g_1=2 sequence A_0 = (2,3,5,7,9,15) has row 2 =
    (1,0,0,4,...), an all-zero leading {0,2} block of length 2 with
    intruder 4.  (The intruder-4-everywhere hypothesis is load-bearing.)

F3. Same sequence dies: A_0=(2,3,5,7,9,15) reaches leading entry != 1
    (a genuine death in the g_1=2 2-then-odds class with one gap 6).
"""
from itertools import product


def build(gaps):
    x = 3
    row0 = [2, 3]
    for g in gaps:
        x += g
        row0.append(x)
    return row0


def rows(A):
    out = [list(A)]
    cur = list(A)
    while len(cur) > 1:
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        out.append(cur)
    return out


def blocklen(row):
    b = 0
    for v in row[1:]:
        if v in (0, 2):
            b += 1
        else:
            break
    return b


def is_corner(row):
    # row = (1, x, y, ...) with every x,y,... in {0,2}
    return row[0] == 1 and all(v in (0, 2) for v in row[1:])


def main():
    # ---- F1: {2,4} class never dies; every A_2 is the corner ----
    noticorner = 0
    deaths = 0
    total = 0
    for L in range(1, 13):            # total even gaps after the first 2
        for rest in product([2, 4], repeat=L - 1):
            gaps = (2,) + rest
            total += 1
            R = rows(build(list(gaps)))
            if not is_corner(R[2]):
                noticorner += 1
            # death check: leading entry of every row after A_0 must be 1
            died = any(r[0] != 1 for r in R[1:])
            if died:
                deaths += 1
    print(f"[F1] {{2,4}}-class (g_1=2): {total} sequences, "
          f"A_2-not-corner: {noticorner}, deaths: {deaths}")

    # ---- F2: all-zero block reachable, A_0=(2,3,5,7,9,15) ----
    A = [2, 3, 5, 7, 9, 15]
    R = rows(A)
    print(f"\n[F2] A_0 = {A}")
    for k, r in enumerate(R):
        b = blocklen(r)
        print(f"   A_{k} = {r}  blocklen(b)={b}")
    # row 2 check: (1, 0, 0, 4, ...)
    print("   row 2 all-zero block len 2 with intruder 4?",
          R[2][:2] == [1, 0] and len(R[2]) > 2 and R[2][2] == 4)

    # ---- F3: death in g_1=2 class with one 6 gap ----
    deathrow = None
    for k in range(1, len(R)):
        if R[k][0] != 1:
            deathrow = k
            break
    print(f"\n[F3] first death row for (2,3,5,7,9,15): {deathrow}  "
          f"(leading entry {R[deathrow][0] if deathrow else None})")


main()
