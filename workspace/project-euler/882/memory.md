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
- What is the closed-form/structure for S(n)? (Not yet computed.)

## Failed approaches
(none yet)
