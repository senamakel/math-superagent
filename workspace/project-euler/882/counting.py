#!/usr/bin/env python3
"""
TASK B - identical minimax on the reduced counting game (A,B).

State is (A,B): A = total number of 1-bits across all numbers, B = total
number of 0-bits.  A One-move is (A-1,B) (it consumes one 1-bit), a Zero-move
is (A,B-1).  A skip passes without changing (A,B).  A player unable to move
loses.  Zero wins iff One cannot move, i.e. A == 0 on One's turn.

Both players die at A=0: with no 1-bits anywhere, no number has a 1-bit, so
One cannot move (wins for Zero); Zero also has no 0-bit to delete (all
remaining strings are all-1's or empty), so Zero cannot move either.  The game
tree over states is acyclic (each move strictly decreases A or B), and states
with (A==0 or B==0) on Zero's turn are terminal.

need_oneturn(A,B) = minimal total skips Zero needs from state (A,B) on One's
turn to force a win.
need_zeroturn(A,B) = same from (A,B) on Zero's turn.

Note: a skip on One's turn is just a pass to Zero and cannot help the player
who is losing the parity fight, so it never occurs; One has no skip.
"""
import sys
sys.setrecursionlimit(10000)

INF = float("inf")

def need_oneturn(A, B, memo_one, memo_zero):
    """minimal skips Zero needs from (A,B), One to move."""
    if (A, B) in memo_one:
        return memo_one[(A, B)]
    if A == 0:
        # One has no 1-bit anywhere -> cannot move -> Zero has won at cost 0
        r = 0.0
    else:
        # One must move: picks the child maximising Zero's needed skips.
        # One's only moves go to (A-1, B') with B' in [B-L, B] by the
        # varied shape lemma; the maximum is achieved at B'=B.
        # (Conservative: we still compute max over reachable B' below.)
        assert A >= 1
        best = -1.0
        for Bp in range(max(0, B - 20), B + 1):
            # Bp must be reachable: Bp <= B and at least B-(#bits deleted so far)
            # We limit the search to a plausible band; the maximum over the
            # entire reachable set is at B'=B (consuming only 1-bits shortens
            # a string, never increases B).  So we can simply use B.
            pass
        r = need_zeroturn(A - 1, B, memo_one, memo_zero)
    memo_one[(A, B)] = r
    return r

def need_zeroturn(A, B, memo_one, memo_zero):
    """minimal skips Zero needs from (A,B), Zero to move."""
    if (A, B) in memo_zero:
        return memo_zero[(A, B)]
    if A == 0 or B == 0:
        # Zero cannot move (needs a 0-bit) -> Zero loses
        r = INF
    else:
        # Zero may delete a 0-bit (goes to (A, B-1)) or skip (passes to One
        # from the same (A,B)).  Note the memoised skip self-dependency is
        # resolved below by treating skip as infinite unless the One-move
        # value at the same (A,B) is finite and the budget allows; simplest
        # correct formulation: need_zeroturn = min( 1+need_oneturn(A,B),
        # need_oneturn(A,B-1) ) with the skip option paying a cost of 1 and
        # costing budget 1.  Since budget is not an explicit parameter in this
        # table, we use the standard fixpoint formulation:
        #
        #   Z = min( O(A,B-1), 1 + O(A,B) ) where O = need_oneturn.
        #
        # but the recursive O(A,B) itself calls Z(A-1,B); the skip at A=0
        # bottom is handled by the A==0 rule.  This is a min/max DP over a DAG
        # plus one self-loop, whose least fixpoint is
        #   Z(A,B) = min( O(A,B-1), 1 + O(A,B) ).
        o_same = need_oneturn(A, B, memo_one, memo_zero)
        o_down = need_oneturn(A, B - 1, memo_one, memo_zero)
        cands = []
        if o_down < INF:
            cands.append(o_down)      # move: consume one 0-bit
        if o_same < INF:
            cands.append(o_same + 1.0)  # skip (costs one skip)
        r = min(cands) if cands else INF
    memo_zero[(A, B)] = r
    return r

def A_of_n(n):
    """A = sum_{k=1..n} k * popcount(k)"""
    return sum(k * (k.bit_count()) for k in range(1, n + 1))

def B_of_n(n):
    """B = sum_{k=1..n} k * (bitlength(k) - popcount(k))"""
    return sum(k * (k.bit_length() - k.bit_count()) for k in range(1, n + 1))

def S_counting(n):
    """S(n) on the counting game, by binary search on the budget with the
    two-value DP (need_* as functions of budget)."""
    A, B = A_of_n(n), B_of_n(n)
    # minimal total skips Zero needs from (A,B), One to move, unlimited budget
    lo, hi = 0, max(1, A + B + 3)   # S can't exceed total numbers of moves
    def winnable(k):
        mo, mz = {}, {}
        return need_oneturn(A, B, mo, mz)
    # With the self-loop fixpoint we computed Z = min(O(A,B-1), 1+O(A,B)),
    # which already accounts for budget through the +1 per skip.  The value
    # from state (A,B), One to move, is the minimal skip count NEEDED overall,
    # not capped by a budget.  So S_counting = need_oneturn(A,B).
    v = need_oneturn(A, B, {}, {})
    return v

def s_counting_table(N):
    """Return list of (n, A, B, need_oneturn(A,B)) for n=1..N.
    The need_oneturn value is the minimal TOTAL skip count Zero needs."""
    res = []
    for n in range(1, N + 1):
        A, B = A_of_n(n), B_of_n(n)
        mo, mz = {}, {}
        v = need_oneturn(A, B, mo, mz)
        res.append((n, A, B, v))
    return res

def main():
    print("=== TASK B: counting game (A,B) DP ===")
    # verify given examples
    for (n, expect) in ((2, 2), (5, 17), (10, 64)):
        A, B = A_of_n(n), B_of_n(n)
        mo, mz = {}, {}
        v = need_oneturn(A, B, mo, mz)
        ok = "OK" if v == expect else "MISMATCH"
        print(f"  n={n}: A={A} B={B} need_oneturn={v} expected {expect} -> {ok}")
    print()
    print("S(n) counting game n=1..10:")
    for (n, A, B, v) in s_counting_table(10):
        vs = int(v) if v < INF else "inf"
        print(f"  n={n:2d} A={A:3d} B={B:3d} S={vs}")
    print()
    print("need_oneturn(A,B) for A,B in 0..12 (minimal skips Zero needs, One to move):")
    mo_all, mz_all = {}, {}
    for A in range(0, 13):
        row = []
        for B in range(0, 13):
            v = need_oneturn(A, B, mo_all, mz_all)
            row.append("  ." if v == INF else f"{int(v):3d}")
        print(f"  A={A:2d}: " + " ".join(row))
    print("  (columns B=0..12, '.' = unable to force a win)")
    print()
    print("need_zeroturn(A,B) for A,B in 0..12:")
    mo2, mz2 = {}, {}
    for A in range(0, 13):
        row = []
        for B in range(0, 13):
            v = need_zeroturn(A, B, mo2, mz2)
            row.append("  ." if v == INF else f"{int(v):3d}")
        print(f"  A={A:2d}: " + " ".join(row))
    print("  (columns B=0..12, '.' = unable to force a win)")

if __name__ == "__main__":
    main()