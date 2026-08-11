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
- **S(n) = ceil(G(n)), G(n)=Σ_{k≤n} k·g(k)** (all conditions of the Simplicity
  Rule hold up to n=10^5: every single number g(k) is a canonical Number, i.e.
  max(One-options) < min(Zero-options) for all k≤10^5 — zero violations).
  Reproduces every known value: S(1..5)=1,2,8,9,17 (matches the real-game brute
  oracle), S(10)=64, S(2)=2, S(5)=17 (the statement's worked examples).
- **Final answer: S(10^5) = 15800662276.** G(10^5)=517756101446417/32768 =
  15800662275.58646…, floor 15800662275, ceil 15800662276. Confirmed by three
  independent implementations (solve_dyadic.py, verify_dyadic.py, inline
  Fraction sweep) giving the identical exact rational and identical S.
- The brute-force real-game oracle reaches only n≤5 (S=1,2,8,9,17); n=6 is
  unreachable (≈1.5e9 states at 500s, still climbing). So the dyadic-CGT rule
  is the only structural route, and it reproduces every reachable oracle value.
- **Dyadic CGT solution COMPUTED and CROSS-CHECKED (this run)**: g(k) = simplest
  dyadic strictly between max(Left=1-deletions) and min(Right=0-deletions),
  g(0)=0.  Every k in 1..100000 is a Number (max(Left) < min(Right); no
  violation found).  G(n)=Σ k·g(k) exact Fractions, S(n)=ceil(G(n)).
  Verified S_ceil(1,2,3,4,5,10)=1,2,8,9,17,64 — ALL match the real-game oracle
  values on disk.  G(100000)=517756101446417/32768, so
  **S(100000) = ceil(G(100000)) = 15800662276**.  Cross-checked by an
  independent birthday-scan implementation (reproduces G(1..12)) and by exact
  integer arithmetic on the final fraction (floor 15800662275, remainder
  19217, so ceil = 15800662276).  Script: /workspace/solution.py; answer in
  /workspace/dyadic_answer.txt.
- **simplest-between validated (this run)**: toolkit
  code/toolkits/simplest_dyadic.py simplest_between(a,b) (a,b Fraction or None
  for ±inf) returns the simplest (minimal-birthday) dyadic strictly between;
  validated against an independent birthday oracle
  (code/test_simplest_dyadic.py, 166 intervals, 0 mismatches) and the four
  required cases (0,1)->1/2, (1,2)->3/2, (1/2,2)->1, (-1,1)->0.  Hand-checked
  g(1..8)=1,1/2,2,1/4,3/2,1,3,1/8 reproduced exactly by solution.py.
- **Real-game oracle values on disk (source of cross-check)**: S(1)=1, S(2)=2,
  S(3)=8, S(4)=9, S(5)=17 (code/brute.py), S(10)=64 (given).  These all equal
  ceil(G(n)) under the dyadic model.
- **Real-game oracle confirmed live (this task)**: re-ran code/brute.py (budgeted
  real-game minimax) and code/fastbrute.py (budget-removed optimizer) and
  confirmed S(1..5)=1,2,8,9,17; statement S(2)=2,S(5)=17 and hand-known
  S(1)=1,S(3)=8 all match; n=1..3 double-checked against an explicit
  independent game search. n=6 NOT reached within ~5 min (budget sweep hit
  >1.5M memo states through budget=18 still inf, then 290s timeout) ⇒ S(6)>18
  is all that is established; n=6+ are infeasible for the exact minimax. Oracle
  table: /workspace/oracle_S.txt.
- **S_ceil(n)=ceil(G(n)) table n=1..20** (from solution.py, exact Fractions):
  n:   1   2   3   4   5   6   7   8   9  10
  S:   1   2   8   9  17  23  44  45  56  64
   n:  11  12  13  14  15  16  17  18  19  20
  S:  91  97 123 151 211 212 231 243 285 293
  Matches real oracle at 1,2,3,4,5,10.
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
- **Standing caveat**: the dyadic Number model is a structural hypothesis
  (each single number is a canonical dyadic Number via the Simplicity Rule).
  It is strongly corroborated: S_ceil(n)=ceil(G(n)) matches the real-game
  oracle for ALL available real values (S(1..5) from brute.py and S(10)=64
  given), and every k in 1..100000 is a Number.  But the real-game oracle
  itself does not reach S(6)..S(9) or S(100000) independently (the stated bound
  defeats enumeration), so the equality of ceil(G(n)) with the true S(n) beyond
  n=10 rests on the model.  If the model holds, S(100000)=15800662276.
- The old single-aggregate (A,B) counting surrogate is REFUTED (see below);
  the surviving exact rule is the dyadic one above, not (A,B) totals.
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
- **S(6) real-game oracle NOT obtained (run this session).** RealSolver(6)
  (fastbrute.py, budget-removed minimax) was run under `timeout 500` with a
  progress probe (code/tmp/real6.py, probe6.py). Both timed out: after 500s it
  had memoized ~1.49e9 distinct (state,turn) values and was still ascending
  (n_states 1.48e9, One=7.55e8/Zero=7.32e8 at 499.8s), so it does not converge
  in reasonable time — the real-game position space is explosive at n=6. The
  dyadic theory predicts S_theory=ceil(G(6))=ceil(22.5)=23 (g(1..6)=
  1,1/2,2,1/4,3/2,1, so G(6)=sum k*g(k)=45/2; computed exactly by
  code/tmp/dyadic6.py using toolkits/simplest_dyadic). But there is NO oracle
  S(6) to compare against — "matched the dyadic value" is UNVERIFIED, not a
  yes. Consistent with code/out/oracle_S.txt: n=6 never reached, only S(1..5)=
  1,2,8,9,17 established. This confirms brute-force real-game minimax cannot
  reach S(6); a structural method is needed.

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
