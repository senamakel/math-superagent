# Working memory

## Problem
Partisan bit-deletion game. Start with k copies of k, k=1..n. One deletes a
1-bit from a number's binary string (leading zeros dropped; empty -> 0). Zero
deletes a 0-bit. A player unable to move loses. Zero wins iff One cannot move
on One's turn. Only Zero may skip (turn passes to One, skip count +1). S(n) =
minimal total skip budget so Zero has a forced win.

Given: S(2)=2, S(5)=17, S(10)=64. Need S(10^5) ultimately; this task first
builds and validates the two DP programs (real-game brute up to n=8, counting
game up to n=10).

## Established results
- brute.py (real game, memoized minimax): S(1..6) = 1,2,8,9,17,23. Explicit
  minimax agrees on n=1,2,3 (S=1,2,8). n=7,n=8 NOT reachable: naive minimax
  state space explodes (n=6 already 1.57M memoized states) and the process is
  killed (timeout/OOM). brute.py cannot finish n=1..8 as task A expects.
- counting.py currently BROKEN: prints S=inf for every n and every (A,B) grid
  cell ('.'), so it fails S(2)=2, S(5)=17, S(10)=64 and crashes compare.py
  (OverflowError: cannot convert float infinity to integer). Suspect: the
  (A,B) reduction mapping is wrong too (n=2 prints A=3 B=2 but 2 copies of 2
  = {10,10} => A=2,B=2), and the DP base-condition/move logic never finds a
  finite forced win. Needs fixing before compare.py can run.
- compare.py cannot run until counting.py returns finite S values.

## Failed approaches
(none yet)

## Current progress
Ran all three programs (brute.py, counting.py, compare.py) — see memory.md.

Open questions
- Why does brute.py fail to finish n=7,8 (naive minimax too slow/memory)?
  Task A's goal of S(1..8) is not met by the existing brute.py.
- counting.py is broken (all inf); need to find the bug (move reductions and
  DP recurrence) before compare.py can run or S(10^5) can be computed.
