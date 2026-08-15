"""Brute-force the {2,4}-gap class (R-carved-gap24 / R-gaps-24).

Claim to attack: for A_0 = (2,3,x_1,x_2,...) with x_1-3 = 2 and every
subsequent gap in {2,4}, the leading entry A_k(0) = 1 for all k, i.e.
A_k(1) in {0,2} for all k (the leading 1 never dies).

The gap signature after the first is a binary string over {2,4}.  For a
prefix of length L we get a row of width L+1; the triangle can be computed
to any depth d < len.  We exhaustively search all gap strings over a window
and ask whether the leading 1 ever dies within the computed triangle.

This is a bounded verification over the class (a small, exhaustive search),
not a proof.
"""
import sys

def triangle(A, depth):
    """Return list of rows, each a list. depth = number of rows after A0."""
    rows = [list(A)]
    cur = list(A)
    for _ in range(depth):
        nxt = [abs(cur[i]-cur[i+1]) for i in range(len(cur)-1)]
        rows.append(nxt)
        cur = nxt
    return rows

def leading_survives(A, depth):
    rows = triangle(A, depth)
    for k in range(1, depth+1):
        if rows[k][0] != 1:
            return False, k, rows
    return True, None, rows

def search(gap_values, max_len, depth, first_fail_only):
    """gap_values: list like [2,4]; generate all strings of length up to max_len.
    depth: triangle depth. Report any leading failure."""
    from itertools import product
    found = 0
    first_death_dict = {}
    for L in range(1, max_len+1):
        for tail in product(gap_values, repeat=L-1):
            # gaps: g1 = x1-3 = 2 (given), then g2..gL in {2,4}
            gaps = (2,) + tail
            # A0: 2,3, then x1=5, x2=x1+g2, ...
            x = [2,3]
            cur = 5
            for g in gaps[1:]:
                cur += g
                x.append(cur)
            A = x
            ok, k, rows = leading_survives(A, depth)
            if not ok:
                found += 1
                first_death_dict[k] = first_death_dict.get(k,0)+1
                if found <= 3:
                    print(f"FAILURE: A0={A} gaps={gaps} died at row k={k}")
                    print("  rows:", [r[:8] for r in rows[:min(k+2, len(rows))]])
    print(f"searched all gap strings length 1..{max_len} over {gap_values}, depth {depth}")
    print(f"failures: {found}")
    print("deaths by row index:", dict(sorted(first_death_dict.items())))

if __name__ == "__main__":
    # default: gaps in {2,4}, window length up to 14, depth 12
    max_len = int(sys.argv[1]) if len(sys.argv)>1 else 14
    depth   = int(sys.argv[2]) if len(sys.argv)>2 else 12
    search([2,4], max_len, depth, first_fail_only=True)
