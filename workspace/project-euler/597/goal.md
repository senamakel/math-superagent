# Goal

Solve Project Euler 597 ("Torpids"): compute p(13, 1800) to 10 digits after the
decimal point, where p(n,L) is the probability that the new order of n rowing
boats after the race is an **even permutation** of the starting order.

## Setup (restated, every symbol defined)

- n boats, indexed j = 1..n. j=1 is the LOWEST placed / most downstream; j=n is
  the HIGHEST placed / most upstream. Starting positions (coordinate increases
  upstream, finish line upstream of all):
    p_j = 40*(j-1)
  so adjacent boats start 40 m apart, lowest boat at 0.
- Finish line is L metres upstream from the lowest boat's start (position L).
- Boat j rows upstream at steady speed v_j = -ln(X_j) m/s where X_j ~ U(0,1),
  i.i.d.  Equivalently v_j ~ Exp(1) (rate 1), i.i.d. (P(-ln X > t)=P(X<e^-t)=e^-t).
- Each boat rows until it EITHER reaches the finish line OR catches up with
  ("bumps") the next rowing boat ahead. On a bump the BUMPING boat stops and
  takes no further part (out); the bumped boat continues and may be bumped again.
  Boats that are "out" are passed freely by boats behind.
- New order rule: for boats i<j in the starting (lower→higher) sense, i is placed
  HIGHER than j in the new order iff there is a bump chain i -> ... -> j
  (directly or transitively). Pairs with no chain in either restoring direction
  keep their starting relative order. This yields a total order (ascending-place
  listing = lowest place first).
- p(n,L) = probability that this new order is an even permutation of the starting
  order.

## Worked examples (test oracle)

n=3, L=160 (positions A=0,B=40,C=80; distances to finish: A 160, B 120, C 80):

| bumps | new order | parity | prob |
|---|---|---|---|
| none | A,B,C | even | 4/15 |
| B bumps C | A,C,B | odd | 8/45 |
| A bumps B | B,A,C | odd | 1/3 |
| B bumps C then A bumps C | C,A,B | even | 4/27 |
| A bumps B then B bumps C | C,B,A | odd | 2/27 |

p(3,160) = 4/15 + 4/27 = 56/135 ≈ 0.4148148...  (sum of probs = 1)

Given: p(4,400) = 0.5107843137 (10 dp).

Target: p(13,1800) to 10 dp.

## Completion criteria
1. brute.py reproduces p(3,160)=56/135 and p(4,400)≈0.5107843137.
2. solution.py exact method agrees with brute on all reachable cases and both
   examples; matches both given example values.
3. Final n=13 answer reported with a second independent verification.
