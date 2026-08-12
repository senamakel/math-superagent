# Working memory

## Problem
Project Euler 493: 7 colours × 10 balls = 70 balls; draw 20 without
replacement; E[number of distinct colours among the drawn balls].

## Established results
- The definition is pinned: X = distinct colours among a uniformly random
  k-subset of the c·m labelled balls (balls of one colour are distinguishable
  as labelled but share a colour).
- By linearity of expectation, for a uniformly random k-subset:
  E[X] = c · (1 − C((c−1)m, k) / C(c·m, k)).
- The naive exhaustive oracle (code/brute.py) averages over every k-subset on
  small instances and matches this formula exactly on every case tried
  (c,m,k) ∈ {(1,10,5),(2,2,2),(2,3,3),(3,2,2),(3,2,3),(3,3,3),(2,10,10),
  (3,2,4)} — including C(20,10)=184756 subsets for (2,10,10).
- Real problem (7,10,20): E = 763700091/112000148 = 6.818741802... →
  6.818741802 (nine digits after the point).

## Failed approaches
(none)

## Open questions
(none for the oracle; the closed form is now pinned by exhaustive agreement.)
