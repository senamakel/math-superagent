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
- **CGT framework (sourced)**: The game is strictly partisan — One deletes only
  1-bits, Zero only 0-bits — so Sprague–Grundy/nimbers do NOT apply. Win rule
  is normal play. Source: en.wikipedia.org/wiki/Partisan_game,
  /Combinatorial_game_theory, /Normal_play_convention.
- **Disjunctive-sum reduction (sourced derivation)**: Model each number with a
  1-bits and b 0-bits as G(a,b)={G(a-1,b)|G(a,b-1)}, G(0,0)=0. Inductively
  G(a,b) = the integer (a−b) (simplest surreal between the two options). The
  board is a disjunctive sum of these, so its no-skip value is the single
  integer A−B (A = total 1-bits, B = total 0-bits). A−B>0 ⇒ One wins always
  ⇒ "Dr. Zero can never win" without skips.
- **Skip mechanism (sourced)**: One is in zugzwang (forced to consume a 1-bit
  each One turn while A>0; once A hits 0 on One's turn, One loses). The skip is
  the "passing would be best" case of zugzwang. The skip is a self-loop in the
  state graph, making the DP a fixpoint; the game is a stopper (moves strictly
  decrease A or B), so no forced tie and finite S(n). Sources:
  en.wikipedia.org/wiki/Zugzwang, /Loopy_game.
- **S(n) ≠ A−B (hand-computed, unverified-by-run)**: n=2 (A,B)=(3,2) S=2;
  n=5 (23,15) S=17; n=10 (102,83) A−B=19 but S(10)=64. A−B is the no-skip
  score; S counts skips via the (A,B) minimax DP.

## Open questions / caveats
- The counting model is a CONJECTURED surrogate for the real game: its (A,B)
  transitions (One-move (A-1,B), Zero-move (A,B-1)) differ from the real bit
  game, where deleting a leading 1 can also drop 0-bits (e.g. "100"→0). The
  given S values are reproduced, but whether real-game S(n) == counting-game
  S(n) for all n is what brute.py vs counting.py/compare.py must confirm.
- **Correct-skip-semantics surrogate is REFUTED (counting_proper.py)**: even
  with the corrected skip rule (skip always allowed, costs 1, passes the turn;
  O(0,B)=0 ⇔ Zero wins the moment One has no 1-bit on One's turn), the exact
  recurrence O(A,B)=Z(A-1,B), Z(A,B)=min(O(A,B-1) if B>=1, 1+O(A,B)) collapses
  to the closed form **O(A,B)=max(0, A−B)**. Hence S_counting(n)=max(0,A(n)−B(n))
  — for n=1..5 that gives 1,1,7,3,8 vs the real oracle 1,2,8,9,17; only n=1
  matches. So the single-aggregate (A,B) counting model is NOT a faithful
  surrogate under either skip interpretation; the real S grows far faster than
  A−B (S(5)=17 vs A−B=8), so S depends on the DISTRIBUTION of bit-strings, not
  just the totals. Output: code/out/counting_proper.txt.
- What is the closed-form/structure for S(n)? (Not yet computed.)

## KEY RESULT for Project Euler 882 (this pattern-recognition branch)

**S(n) = ceil(G(n)), G(n) = Σ_{k=1..n} k·g(k)** where g(k) is the CGT value of
the single-number bit-deletion game:
- g(0)=0; One(Left) deletes a 1-bit → option values g(j); Zero(Right) deletes a
  0-bit → option values g(j); g(k) = simplest dyadic strictly between
  max(Left) and min(Right) (Simplicity Rule for canonical Numbers). Verified
  k≤4096: always a Number (max L < min R), never a game that needs a switch.
- Board is a disjunctive sum of k copies of k → value G(n)=Σ k·g(k).
- Each Right(skip) adds −1, so Zero (Right) wins iff G(n)−m≤0 ⇒ **S(n)=ceil(G(n))**.
- Cheap at full size: G(n) direct O(n log n) iteration; no polylog needed since
  n=10^5 ⇒ S(10^5) = **15800662276** (G=517756101446417/32768≈1.5801e10).

**Verification.** Two independent code paths agree (both exact fractions):
solve_dyadic.py and verify_dyadic.py → same G, same S. Repro of all known
values: real-game brute confirms S(1..5)=1,2,8,9,17; given S(10)=64; ceil(G)
gives exactly 1,2,8,9,17,23,44,45,56,64 for n=1..10. So the dyadic rule matches
every value brute can reach and every statement example.

## Structure notes (g(k))
- g(2^p)=1/2^p; g(2^p−1)=p (Mersenne); g(2^p+1)=(2^p+1)/2^p.
- NOT g(2k)=g(k)/2 in general (first diverges k=7). S sequence has no low
  degree polynomial / plain linear recurrence (analyze_sequence). The
  computable structure is the dyadic CGT rule itself, not a closed form of S.

## Failed approaches
- **Single-aggregate (A,B) counting surrogate (both skip readings)** — refuted
  by counting_proper.py. With the corrected skip semantics the exact
  recurrence yields O(A,B)=max(0,A−B), so S_counting = max(0,A(n)−B(n)); only
  n=1 of the real oracle 1,2,8,9,17 matches (it gives 1,1,7,3,8). The real
  game's S depends on the distribution/positions of bits, not the totals A,B.
  A dead end worth recording so no later run rebuilds it.
- **Fitting S(n) to a low-order recurrence / polynomial** — no structure found,
  matching expectation: S comes from the dyadic CGT rule, and G(n)'s dyadic
  increments make S a jumpy sequence, not a clean recurrence. Don't re-derive
  S(n) independently; compute G(n)=Σ k·g(k) and take ceil.
