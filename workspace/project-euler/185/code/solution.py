#!/usr/bin/env python3
"""Efficient solver for Project Euler 185 (Number Mind).

Method (no enumeration of the 10^L answer space):

Recursive backtracking assigns one digit s[p] per position p (0..L-1).  For
each guess i we keep an accumulated match count

    acc[i] = #{ p already assigned : s[p] == guess[i][p] }.

A partial assignment is pruned as soon as, for some guess i,

    (a) acc[i] > c_i            -- too many matches already, or
    (b) acc[i] + (unassigned positions) < c_i
                                -- even if every remaining position matched,
                                   we could no longer reach c_i.

The next position is chosen with the most-constrained-variable heuristic: the
unassigned position admitting the fewest digits that keep every guess
feasible.  Digits at a chosen position are tried in static increasing value
order (0..9).  The cost therefore scales with the constraint structure, not
with 10^L.

Because (a)/(b) are necessary conditions and at the final position (no
unassigned positions left) they collapse to acc[i] == c_i for every i, any
complete assignment the search reaches is a genuine solution; a final exact
check is still made for safety.
"""

import sys

sys.setrecursionlimit(100000)


def solve(L, constraints):
    """Return (solution_string, nodes_visited) or (None, nodes_visited).

    constraints: iterable of (guess_string, c_i), each guess of length L.
    """
    guesses = [g for g, _ in constraints]
    cs = [c for _, c in constraints]
    G = len(guesses)
    guess_digits = [[int(ch) for ch in g] for g in guesses]

    assigned = [None] * L
    acc = [0] * G
    nodes = 0

    def feasible(pos, d, U_after):
        """Can digit d be placed at pos without violating any guess?

        U_after = number of positions still unassigned AFTER placing here.
        """
        for i in range(G):
            na = acc[i] + (1 if guess_digits[i][pos] == d else 0)
            if na > cs[i] or na + U_after < cs[i]:
                return False
        return True

    def search(n_assigned):
        nonlocal nodes
        nodes += 1
        if n_assigned == L:
            for i in range(G):
                if acc[i] != cs[i]:
                    return None
            return "".join(assigned)

        U_after = (L - n_assigned) - 1

        # Most-constrained-variable: pick the position with the fewest
        # currently feasible digits.
        best_pos = None
        best_digits = None
        best_cnt = None
        for p in range(L):
            if assigned[p] is not None:
                continue
            digs = [d for d in range(10) if feasible(p, d, U_after)]
            if not digs:
                return None  # dead end: some position has no feasible digit
            if best_cnt is None or len(digs) < best_cnt:
                best_cnt = len(digs)
                best_pos = p
                best_digits = digs
                if best_cnt == 1:
                    break  # cannot do better than a single feasible digit

        # Static value ordering: try digits in increasing order (0..9).
        for d in best_digits:
            assigned[best_pos] = str(d)
            for i in range(G):
                if guess_digits[i][best_pos] == d:
                    acc[i] += 1
            res = search(n_assigned + 1)
            if res is not None:
                return res
            for i in range(G):
                if guess_digits[i][best_pos] == d:
                    acc[i] -= 1
            assigned[best_pos] = None
        return None

    return search(0), nodes


# ---------------------------------------------------------------------------
# L=5 example from the problem statement
# ---------------------------------------------------------------------------
L5 = 5
constraints5 = [
    ("90342", 2),
    ("70794", 0),
    ("39458", 2),
    ("34109", 1),
    ("51545", 2),
    ("12531", 1),
]

# ---------------------------------------------------------------------------
# L=16 main instance
# ---------------------------------------------------------------------------
L16 = 16
constraints16 = [
    ("5616185650518293", 2),
    ("3847439647293047", 1),
    ("5855462940810587", 3),
    ("9742855507068353", 3),
    ("4296849643607543", 3),
    ("3174248439465858", 1),
    ("4513559094146117", 2),
    ("7890971548908067", 3),
    ("8157356344118483", 1),
    ("2615250744386899", 2),
    ("8690095851526254", 3),
    ("6375711915077050", 1),
    ("6913859173121360", 1),
    ("6442889055042768", 2),
    ("2321386104303845", 0),
    ("2326509471271448", 2),
    ("5251583379644322", 2),
    ("1748270476758276", 3),
    ("4895722652190306", 1),
    ("3041631117224635", 3),
    ("1841236454324589", 3),
    ("2659862637316867", 2),
]


def verify_solution(sol, L, constraints):
    """Check sol against every (guess, c_i) constraint independently."""
    for g, c in constraints:
        hit = sum(1 for j in range(L) if sol[j] == g[j])
        if hit != c:
            return False, (g, c, hit)
    return True, None


def main():
    print("=" * 60)
    print("L=5 example")
    print("=" * 60)
    sol5, nodes5 = solve(L5, constraints5)
    ok5, bad5 = verify_solution(sol5, L5, constraints5)
    print(f"solver result     : {sol5}")
    print(f"nodes visited     : {nodes5}")
    print(f"independent verify: {'OK' if ok5 else 'FAILED: ' + str(bad5)}")
    brute_answer = "39542"
    if sol5 == brute_answer:
        print("AGREES with brute-force oracle (unique answer 39542).")
    else:
        print(f"MISMATCH: solver={sol5}, brute={brute_answer}")
        sys.exit(1)

    print()
    print("=" * 60)
    print("L=16 main instance")
    print("=" * 60)
    import time
    t0 = time.time()
    sol16, nodes16 = solve(L16, constraints16)
    dt = time.time() - t0
    ok16, bad16 = verify_solution(sol16, L16, constraints16)
    print(f"length L            : {L16}")
    print(f"number of guesses   : {len(constraints16)}")
    print(f"solver result (secret): {sol16}")
    print(f"nodes visited       : {nodes16}")
    print(f"runtime             : {dt:.6f} s")
    print(f"independent verify  : {'OK' if ok16 else 'FAILED: ' + str(bad16)}")
    if not ok16:
        sys.exit(1)


if __name__ == "__main__":
    main()
