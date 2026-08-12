# Working memory

## Problem

Project Euler 185 "Number Mind": find a secret digit-string of length L such
that each of the given guesses has exactly c_i of its digits in the correct
position. See GOAL.md for full statement, symbols, and the L=5 test oracle
(answer 39542 unique).

## Governing theory / approach

The problem is a constraint satisfaction problem over 16 positions, each with a
10-digit domain, and 22 exact-count constraints. Standard exact methods:

- Recursive backtracking assigning one digit per position, pruning with the
  feasibility bound: for each guess i, if `fixed_matches_i > c_i` or
  `fixed_matches_i + remaining_positions < c_i`, the partial assignment is
  dead. This is fast here because counts are tight (several are 0,1,2,3).
- Reformulation as an integer linear program: binary variable x[p][d] (1 if
  secret[p]=d), constraints sum_d x[p][d]=1 for each p, and for each guess i:
  sum over positions p where guess digit is d_p of x[p][d_p] == c_i. Solve by
  branch-and-bound (scipy.optimize.milp) — an independent route.

The ILP/backtracking cost does not scale with 10^L; it scales with the
constraint structure, so it is not "searching the answer space" at the bound.

## Established results

(pending runs)

## Failed approaches

(none yet)

## Open questions

(none yet)
