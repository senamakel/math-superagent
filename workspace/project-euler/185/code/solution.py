#!/usr/bin/env python3
"""Project Euler 185 (Number Mind) — backtracking with arc-consistent pruning.

Not enumeration: we assign one position at a time and, for every guess i with
required count[i], maintain

    m_i = number of already-assigned positions that match guess i
    r   = number of positions not yet assigned

and require, for every i, the two feasibility bounds

    (a) m_i <= count[i]           (we cannot already have exceeded the target)
    (b) m_i + r >= count[i]       (enough unassigned positions remain to still
                                   reach the target)

At each step we try every digit 0..9 for the current position and prune any
digit that, once assigned, violates either bound for some guess. This makes
most of the 10^N search space unreachable; we recurse only into digits that
survive. The brute-force oracle (code/brute.py) is used on the N=5 example as
a correctness check; the 16-digit instance is far beyond enumeration.

Exact integer arithmetic throughout (counts are plain ints).
"""


def parse_guesses(text):
    """Parse the statement block into a list of (string, count)."""
    guesses = []
    for raw_line in text.strip().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if ";" in line:
            s, c = line.split(";", 1)
        else:
            raise ValueError(f"Cannot parse line: {line!r}")
        s = s.strip()
        c = int(c.strip())
        if not s.isdigit():
            raise ValueError(f"Guess is not a digit string: {s!r}")
        guesses.append((s, c))
    return guesses


def solve(guesses):
    """Return sorted list of all secret strings satisfying every constraint.

    Uses backtracking over positions with the two arc-consistency bounds
    described above. Returns every complete consistent sequence.
    """
    length = len(guesses[0][0])
    assert all(len(g) == length for g, _ in guesses)
    n = len(guesses)

    results = []
    assignment = [None] * length  # digits chosen so far

    def backtrack(pos, m):
        """pos: next position to fill; m[i]: matches accumulated per guess."""
        if pos == length:
            # all positions filled; every bound is tight by construction, but
            # double check each guess reached exactly its target
            if all(m[i] == guesses[i][1] for i in range(n)):
                results.append("".join(assignment))
            return

        r = length - pos  # unassigned positions including this one
        for d in "0123456789":
            ok = True
            new_m = m[:]
            for i in range(n):
                g, c = guesses[i]
                if g[pos] == d:
                    new_m[i] += 1
                # bound (a): cannot already exceed target
                if new_m[i] > c:
                    ok = False
                    break
                # bound (b): matches so far plus all remaining positions
                # (including current, so r after this assignment = r-1) must
                # still be able to reach the target.
                remaining_after = r - 1
                if new_m[i] + remaining_after < c:
                    ok = False
                    break
            if ok:
                assignment[pos] = d
                backtrack(pos + 1, new_m)
                assignment[pos] = None

    backtrack(0, [0] * n)
    return results


EXAMPLE = """
90342 ;2
70794 ;0
39458 ;2
34109 ;1
51545 ;2
12531 ;1
"""

FULL = """
5616185650518293 ;2
3847439647293047 ;1
5855462940810587 ;3
9742855507068353 ;3
4296849643607543 ;3
3174248439465858 ;1
4513559094146117 ;2
7890971548908067 ;3
8157356344118483 ;1
2615250744386899 ;2
8690095851526254 ;3
6375711915077050 ;1
6913859173121360 ;1
6442889055042768 ;2
2321386104303845 ;0
2326509471271448 ;2
5251583379644322 ;2
1748270476758276 ;3
4895722652190306 ;1
3041631117224635 ;3
1841236454324589 ;3
2659862637316867 ;2
"""


if __name__ == "__main__":
    eg = parse_guesses(EXAMPLE)
    eg_sols = solve(eg)
    print("N=5 example solutions:", eg_sols)
    print("Expected 39542 present:", "39542" in eg_sols)
    print("Number of N=5 solutions:", len(eg_sols))
    print()

    full = parse_guesses(FULL)
    print("Solving full 16-digit, 22-guess instance...")
    full_sols = solve(full)
    print("Number of 16-digit solutions:", len(full_sols))
    for s in full_sols:
        print("FULL ANSWER:", s)
