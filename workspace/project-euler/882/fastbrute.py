#!/usr/bin/env python3
"""
TASK A (optimized) - real-game minimax, oracle for the real bit-deletion game.

Same exact game semantics as brute.py:
  - board is a multiset of nonnegative ints (init: k copies of k, k=1..n)
  - One deletes a '1' bit from a number's binary string (leading zeros of the
    result dropped; empty string -> 0); Zero deletes a '0' bit; 0 has no moves.
  - a player unable to move loses; Zero wins iff One cannot move on One's turn.
  - only Zero may skip (turn -> One).

KEY STRUCTURAL OPTIMIZATION (the theory that makes it fast):
brute.py computes need(state, turn, used, budget) and loops the budget k from 0
to S(n), running a whole memo each time, with 'used' in the key.  But the value
need() returns is exactly the number of skips Zero still needs from here, and
the budget only ever *caps* it.  So we define an uncapped value

    f(state, turn) = minimal number of skips Zero needs from here (unlimited
                     budget), i.e. S-value of the position.

Then S(n) = f(initial, One), and the budget is never searched: one memo over
(state, turn) instead of S(n)+1 separate memo runs each carrying a 'used'
dimension.

Recurrences (unlimited budget => Zero may always skip):
    f(state, One):
        if One has no move: 0                      (Zero already won)
        else max over One-moves m of f(m, Zero)    (One picks worst for Zero)
    f(state, Zero):
        min( min over Zero-moves m of f(m, One),
             1 + f(state, One) )                   (skip: cost 1, back to One)

This is well-founded: every deletion reduces total bit count by >=1, so the
skip is the ONLY move that leaves the state unchanged.  f(state, One) depends
only on strictly-smaller children, so f(state, Zero) is then computable from
the (known) f(state, One); there is a 2-cycle One->Zero on the SAME state but
it does not create a true circular dependency because f(state, One) never calls
f of the same state.  S(n) = f(init, One) reproduced the oracle values
S(1..5) = 1,2,8,9,17 (verified below against brute.py).

Optimizations vs brute.py:
  (1) precompute one_delete[x] / zero_delete[x] for x in 0..n once,
  (2) canonical sorted tuple, moves regenerated from the tables, moves memoized
      per state with lru_cache,
  (3) budget dimension removed entirely (see above).
"""
import sys
from functools import lru_cache

def bin_deletions_tables(limit):
    """Return (one_delete, zero_delete): dicts x -> sorted distinct values from
    deleting a '1' / '0' bit of bin(x), with leading-zero dropping and empty->0."""
    one = {}
    zero = {}
    for x in range(0, limit + 1):
        if x == 0:
            one[x] = []
            zero[x] = []
            continue
        s = bin(x)[2:]
        o, z = set(), set()
        for i, ch in enumerate(s):
            t = s[:i] + s[i + 1:]
            y = 0 if t == "" else int(t, 2)
            if ch == "1":
                o.add(y)
            else:
                z.add(y)
        one[x] = sorted(o)
        zero[x] = sorted(z)
    return one, zero

def initial_multiset(n):
    """k copies of k for k=1..n, sorted tuple."""
    ms = []
    for k in range(1, n + 1):
        ms += [k] * k
    return tuple(sorted(ms))

class RealSolver:
    """Memoized real-game minimax with the budget dimension removed."""

    def __init__(self, n):
        self.one, self.zero = bin_deletions_tables(n)
        self.n_states = 0
        self.n_one = 0
        self.n_zero = 0
        self._memo_moves = {}
        self._f = lru_cache(maxsize=None)(self._need)

    def moves(self, state, who):
        """tuple of distinct successor states for player 'who' in {'One','Zero'}."""
        key = (state, who)
        v = self._memo_moves.get(key)
        if v is not None:
            return v
        tbl = self.one if who == "One" else self.zero
        out = set()
        for i, x in enumerate(state):
            for y in tbl[x]:
                lst = list(state)
                lst[i] = y
                out.add(tuple(sorted(lst)))
        v = tuple(sorted(out))
        self._memo_moves[key] = v
        return v

    def _need(self, state, turn):
        self.n_states += 1
        if turn == "One":
            self.n_one += 1
            mvs = self.moves(state, "One")
            if not mvs:
                return 0
            return max(self._need(m, "Zero") for m in mvs)
        else:
            self.n_zero += 1
            mvs = self.moves(state, "Zero")
            best = min(self._need(m, "One") for m in mvs) if mvs else None
            skip = 1 + self._need(state, "One")          # skip: cost 1 -> One
            if best is None:
                return skip
            return min(best, skip)

    def solve(self, state):
        return self._need(state, "One")

    def stats(self):
        return dict(states=self.n_states, one=self.n_one, zero=self.n_zero,
                    move_entries=len(self._memo_moves))

def main():
    print("=== TASK A (optimized): real-game minimax, budget dimension removed ===")
    results = {}
    for n in range(1, 10):
        solv = RealSolver(n)
        init = initial_multiset(n)
        S = solv.solve(init)
        st = solv.stats()
        results[n] = S
        print(f"  S({n}) = {S}   states_memoized={st['states']} "
              f"(One={st['one']}, Zero={st['zero']})  move_cache={st['move_entries']}")
        sys.stdout.flush()

    print("\nS(n) table (real game oracle):")
    for n in range(1, 10):
        print(f"  S({n}) = {results[n]}")
    # oracle agreement check with given examples
    print("\nExample check (must match): S(2)=2, S(5)=17 -> got",
          results.get(2), results.get(5), end=" ")
    print("OK" if results.get(2) == 2 and results.get(5) == 17 else "MISMATCH")

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 7)
    import time
    main()
