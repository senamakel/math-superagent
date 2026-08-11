#!/usr/bin/env python3
"""
TASK A — naive, obviously-correct minimax over the REAL bit-deletion game
exactly as problem.md (Project Euler 882) defines it.

Game rules (from the statement):
  * The game begins with k copies of k for k = 1..n  (multiset of nonnegative
    integers, e.g. n=2 -> [1,2,2]).
  * Dr. One moves first.  On One's turn One picks a number and removes a '1'
    from its binary expansion; on Zero's turn Zero removes a '0'.  Leading
    zeros are dropped from the result; an empty string becomes 0; nobody can
    move on the number 0 (its "binary expansion" has no deletable bit, and 0
    has no moves at all).
  * The player unable to move loses.  Zero wins iff One cannot move on One's
    turn (after reaching a board of all zeros, One has no '1' bit and loses).
  * Dr. Zero is allowed to "skip the turn" — pass the turn back to One without
    moving — any number of times.  S(n) = the minimal total number of skips
    Zero must be *allowed* so that Zero has a forced win.

Model:
  state = sorted tuple of board values (canonical, order independent).
  need(state, turn, used, budget) = minimal skips Zero still needs from this
    state, having already used `used`, given it is allowed at most `budget`
    skips in total; +inf if Zero cannot force a win within that budget.

    One's turn: if One has no move, Zero has already won -> 0.
                else One picks the move that maximises what Zero needs:
                     max over One-moves m of need(m, Zero, used, budget).
    Zero's turn: Zero picks the best option:
                     min( min over Zero-moves m of need(m, One, used, budget),
                          skip if used<budget: 1 + need(state, One, used+1, budget) ).
                If Zero has no move and no skip left, Zero cannot move -> loses
                (+inf).  Crucially Zero may skip even with no move on the board
                (as in the statement's sample, Zero skips on [0,0,0]).

  S(n) = min budget k in 0.. such that need(initial, One, 0, k) is finite.
  The budget only ever *caps* Zero, so need(init,One,0,k) is monotone
  non-increasing in k and equals S(n) once k >= S(n); we find the smallest
  such k.

Correctness anchor (explicit check): a fully explicit re-implementation of the
moves (enumerate every bit position and re-parse the string, written
independently) is used for n=1,2,3 to double-check S.  The statement's given
values S(2)=2, S(5)=17 (and the n=2 sample play with 2 skips) must be
reproduced.
"""
from functools import lru_cache
import sys

INF = float("inf")


# ------------------------------------------------------------------ moves
def one_deletions(x):
    """Distinct values from deleting a single '1' bit of bin(x) (leading zeros
    dropped, empty -> 0).  Empty list if x==0 or x has no '1' bit."""
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == "1":
            t = s[:i] + s[i + 1:]
            out.add(0 if t == "" else int(t, 2))
    return sorted(out)


def zero_deletions(x):
    """Distinct values from deleting a single '0' bit of bin(x)."""
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == "0":
            t = s[:i] + s[i + 1:]
            out.add(0 if t == "" else int(t, 2))
    return sorted(out)


def initial_multiset(n):
    """k copies of k for k=1..n, as a sorted tuple."""
    ms = []
    for k in range(1, n + 1):
        ms += [k] * k
    return tuple(sorted(ms))


def moves(state, who):
    """All distinct successor states (sorted tuples) for player 'who'."""
    tbl = one_deletions if who == "One" else zero_deletions
    out = set()
    for i, x in enumerate(state):
        for y in tbl(x):
            lst = list(state)
            lst[i] = y
            out.add(tuple(sorted(lst)))
    return sorted(out)


# ------------------------------------------------------------ naive minimax
class Solver:
    """Memoized minimax with a skip budget."""

    def __init__(self):
        self.memo = {}
        self.states = 0

    def need(self, state, turn, used, budget):
        key = (state, turn, used, budget)
        if key in self.memo:
            return self.memo[key]
        self.states += 1
        if turn == "One":
            mvs = moves(state, "One")
            if not mvs:
                v = 0.0                      # Zero already won
            else:
                v = max(self.need(m, "Zero", used, budget) for m in mvs)
        else:  # Zero
            mvs = moves(state, "Zero")
            opts = [self.need(m, "One", used, budget) for m in mvs]
            opts = [r for r in opts if r < INF]
            if used < budget:                # skip: cost 1, turn -> One
                r = self.need(state, "One", used + 1, budget)
                if r < INF:
                    opts.append(r + 1.0)
            v = min(opts) if opts else INF
        self.memo[key] = v
        return v


def S_real(n):
    """Smallest budget k so Zero can force a win (naive scan)."""
    init = initial_multiset(n)
    solv = Solver()
    k = 0
    while True:
        v = solv.need(init, "One", 0, k)
        if v < INF:
            return k, solv
        k += 1
        if k > 100000:
            raise RuntimeError(f"S({n}) not found by budget {k}")


# ------------------------------------------------ explicit verify (n=1..3)
def explicit_moves(state, who):
    """Independent re-implementation: enumerate every bit position and re-parse."""
    out = set()
    for i, x in enumerate(state):
        if x == 0:
            continue
        s = bin(x)[2:]
        for j in range(len(s)):
            if (who == "One" and s[j] != "1") or (who == "Zero" and s[j] != "0"):
                continue
            t = s[:j] + s[j + 1:]
            y = 0 if t == "" else int(t, 2)
            lst = list(state)
            lst[i] = y
            out.add(tuple(sorted(lst)))
    return out


def explicit_need(state, turn, used, budget, memo=None):
    """Fully explicit minimax, fresh memo per budget (n=1..3 only)."""
    if memo is None:
        memo = {}
    key = (state, turn, used, budget)
    if key in memo:
        return memo[key]
    if turn == "One":
        mvs = explicit_moves(state, "One")
        v = 0.0 if not mvs else max(
            explicit_need(m, "Zero", used, budget, memo) for m in mvs)
    else:
        mvs = explicit_moves(state, "Zero")
        opts = [r for r in
                [explicit_need(m, "One", used, budget, memo) for m in mvs]
                if r < INF]
        if used < budget:
            r = explicit_need(state, "One", used + 1, budget, memo)
            if r < INF:
                opts.append(r + 1.0)
        v = min(opts) if opts else INF
    memo[key] = v
    return v


def S_explicit(n, cap):
    for k in range(0, cap + 1):
        if explicit_need(initial_multiset(n), "One", 0, k) < INF:
            return k
    return None


def main():
    sys.setrecursionlimit(1000000)
    print("=== brute.py: naive minimax over the REAL bit-deletion game ===")

    # (1) reproduce the statement's n=2 sample explicitly
    print(f"\n[1] Statement sample n=2: S(2) = {S_explicit(2, 6)}   (given 2)")

    # (2) explicit vs naive solver on n=1,2,3
    for n in (1, 2, 3):
        se = S_explicit(n, 60)
        sm, _ = S_real(n)
        print(f"[2] verify n={n}: explicit S={se}, naive S={sm}, match={se == sm}")

    # (3) S(1..8) from the naive solver
    print("\n[3] S(n) real game, n=1..8:")
    results = {}
    for n in range(1, 9):
        s, solv = S_real(n)
        results[n] = s
        print(f"    S({n}) = {s}   states_memoized={solv.states}")
        sys.stdout.flush()

    print("\n[4] Given examples: S(2)=2, S(5)=17 -> got",
          results.get(2), results.get(5),
          "(matched)" if results.get(2) == 2 and results.get(5) == 17
          else "(MISMATCH)")


if __name__ == "__main__":
    main()
