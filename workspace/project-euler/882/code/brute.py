#!/usr/bin/env python3
"""
TASK A - naive minimax on the REAL game (no reduction).

Game: multiset of nonnegative ints, whose turn, skips used so far, remaining
skip budget.  One removes a 1-bit from a number's binary string; Zero removes a
0-bit.  Resulting string with leading zeros dropped; empty string -> 0.  A move
on the number 0 is impossible.  A player who cannot move loses.  Zero wins iff
One cannot move on One's turn.  Only Zero may skip (turn -> One, skip+1).

need(state, turn, used, budget) = minimal total skips (from 0 used, counting
the skips actually taken) that Zero needs in the subtree from this state to
force a win, under the rule that Zero may use at most 'budget' skips total;
inf if Zero cannot force a win within that budget.

  One's turn: if no move, Zero has already won -> 0.
               else need = max over One's moves of need(child, Zero, used, budget)
                    (One minimises Zero's chance; pick the move maximising need).
  Zero's turn: if no move, Zero loses -> inf.
               need = min( min over Zero's moves need(child, One, used, budget),
                           budget-used >= 1 ? 1 + need(same, One, used+1, budget) : inf )

S(n) = min budget k such that need(initial_with_budget_k, One, 0, k) is finite.
"""
from functools import lru_cache
from itertools import product
import sys

INF = float("inf")

def bin_deletions(x):
    """All distinct values obtainable by deleting one bit of bin(x).

    Leading zeros of the resulting string are dropped; if the string becomes
    empty the value is 0.  Returns a list of distinct nonnegative ints.
    Does NOT include x itself (a deletion always changes the string, and the
    deletion of the only 1-bit of a power of two gives a string of zeros that
    drops to 0).
    """
    if x == 0:
        return []
    s = bin(x)[2:]          # canonical binary string without leading zeros
    out = []
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == "":
            out.append(0)
        else:
            out.append(int(t, 2))
    # dedupe (deleting equal bits from different positions gives same value)
    return sorted(set(out))

def one_deletions(x):
    """Values obtained by deleting a '1' bit (so impossible for x with no 1-bit)."""
    if x == 0:
        return []
    s = bin(x)[2:]
    out = []
    for i, ch in enumerate(s):
        if ch == "1":
            t = s[:i] + s[i+1:]
            out.append(0 if t == "" else int(t, 2))
    return sorted(set(out))

def zero_deletions(x):
    """Values obtained by deleting a '0' bit (so impossible for x with no 0-bit)."""
    if x == 0:
        return []
    s = bin(x)[2:]
    out = []
    for i, ch in enumerate(s):
        if ch == "0":
            t = s[:i] + s[i+1:]
            out.append(0 if t == "" else int(t, 2))
    return sorted(set(out))

def initial_multiset(n):
    """k copies of k for k=1..n"""
    ms = []
    for k in range(1, n + 1):
        ms += [k] * k
    return tuple(sorted(ms))

def moves(state, who):
    """All successor states (multiset tuples) for player 'who' in {'One','Zero'}."""
    out = set()
    for i, x in enumerate(state):
        if who == "One":
            cand = one_deletions(x)
        else:
            cand = zero_deletions(x)
        for y in cand:
            lst = list(state)
            lst[i] = y
            out.add(tuple(sorted(lst)))
    return sorted(out)

class Solver:
    """Memoized minimax with skip budget."""

    def __init__(self):
        self.memo = {}
        self.stats = {"states": 0, "one_states": 0, "zero_states": 0}

    def need(self, state, turn, used, budget):
        """minimal skips Zero still needs from this state (used already), given
        total budget; INF if Zero cannot force a win within budget."""
        key = (state, turn, used, budget)
        v = self.memo.get(key)
        if v is not None:
            return v
        self.stats["states"] += 1
        if turn == "One":
            mvs = moves(state, "One")
            if not mvs:
                v = 0.0            # Zero has already won: One cannot move
            else:
                v = max(self.need(m, "Zero", used, budget) for m in mvs)
        else:  # Zero
            mvs = moves(state, "Zero")
            opts = []
            for m in mvs:
                r = self.need(m, "One", used, budget)
                if r < INF:      # only finite options can be best
                    opts.append(r)
            if used < budget:    # skip available
                r = self.need(state, "One", used + 1, budget)
                if r < INF:
                    opts.append(r + 1.0)
            v = min(opts) if opts else INF
        self.memo[key] = v
        return v

def S_real(n, budget_cap=None):
    """S(n) for the real game: minimal total budget so Zero forces a win.
    budget_cap=None: binary-search / grow budget until win possible.
    Returns (S, last_debug) or None if not winnable within cap."""
    init = initial_multiset(n)
    start = 1
    if budget_cap is not None:
        lo, hi = 0, budget_cap
        # find minimal k in [0,hi] with finite need
        solv = None
        if hi < 0:
            return None
        # linear scan is fine and simplest, robust: budget small
        for k in range(0, hi + 1):
            s = Solver()
            v = s.need(init, "One", 0, k)
            if v < INF:
                solv = k
                break
        return solv
    # grow exponentially
    k = 0
    while True:
        s = Solver()
        v = s.need(init, "One", 0, k)
        if v < INF:
            return k, s
        k += 1
        if k > 200:   # safety
            return None, s

# ---------------------------------------------------------------- explicit
def explicit_moves(state, who):
    """Explicit, independent implementation of the move generator for
    verification: enumerate all strings and re-parse.  Same semantics, written
    separately from one_deletions/zero_deletions."""
    out = set()
    for i, x in enumerate(state):
        if x == 0:
            continue
        s = bin(x)[2:]
        for j in range(len(s)):
            if (who == "One" and s[j] != "1") or (who == "Zero" and s[j] != "0"):
                continue
            t = s[:j] + s[j+1:]
            y = 0 if t == "" else int(t, 2)
            lst = list(state)
            lst[i] = y
            out.add(tuple(sorted(lst)))
    return out

def explicit_need(state, turn, used, budget, memo=None):
    """Fully explicit minimax over the real-bit game (no reduction),
    recursion with a fresh memo each budget.  Returns minimal skips Zero needs
    given total budget, INF if cannot force a win within budget."""
    if memo is None:
        memo = {}
    key = (state, turn, used, budget)
    if key in memo:
        return memo[key]
    if turn == "One":
        mvs = explicit_moves(state, "One")
        if not mvs:
            v = 0.0
        else:
            v = max(explicit_need(m, "Zero", used, budget, memo) for m in mvs)
    else:
        mvs = explicit_moves(state, "Zero")
        opts = []
        for m in mvs:
            r = explicit_need(m, "One", used, budget, memo)
            if r < INF:
                opts.append(r)
        if used < budget:
            r = explicit_need(state, "One", used + 1, budget, memo)
            if r < INF:
                opts.append(r + 1.0)
        v = min(opts) if opts else INF
    memo[key] = v
    return v

def S_explicit(n, cap):
    for k in range(0, cap + 1):
        v = explicit_need(initial_multiset(n), "One", 0, k)
        if v < INF:
            return k
    return None

def main():
    # 1) verify the example from the statement: n=2, S(2)=2
    print("=== TASK A: real-game minimax ===")
    print("explicit-move check n=2: S(2) =", S_explicit(2, 4))
    # sanity: explicit and memo solver agree on n=1,2,3
    for n in (1, 2, 3):
        se = S_explicit(n, 20)
        sm = S_real(n)[0]
        print(f"verify n={n}: explicit S={se}, memo S={sm}, match={se==sm}")
    print()
    print("S(n) real game (memoized minimax), n=1..8:")
    worst = 0
    for n in range(1, 9):
        k, s = S_real(n)
        worst = max(worst, s.stats["states"])
        print(f"  S({n}) = {k}   states_memoized={s.stats['states']}")
    print(f"(largest memoized-state count over n=1..8: {worst})")

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()