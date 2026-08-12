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

- **L=5 (oracle):** brute-force (code/brute.py) enumerates all 10^5 strings and
  finds exactly one satisfying the 6 (guess, c_i) constraints: **39542**.
- **L=16 secret (MILP route, code/solution2.py via scipy.optimize.milp):**
  **4640261571849533**. Feasibility ILP with binary x[p][d], position and
  guess-count equalities; branch-and-bound (HiGHS). All 22 counts verified
  exactly (`sum_p [secret[p]==guess[p]] == c_i` for every guess). Uniqueness
  confirmed: re-solving with a "no-good" cut forbidding this assignment is
  infeasible. Solve wall-time ~0.16 s. Full run log:
  code/out/solution2_run.log.
- **Independent-route cross-check status:** the backtracking solver
  (code/solution.py) reproduced L=5 (39542), but its L=16 run had not produced
  output within a 550 s window at this snapshot. The MILP L=16 answer
  4640261571849533 stands on its own verification (all 22 counts + uniqueness);
  it is the well-known PE185 answer.

## Failed approaches

- (none; the MILP model built correctly. One bug encountered: the initial
  reconstruction emitted the *value* x[p*10+d] (always 1) instead of the digit
  d, printing "11111"; fixed by emitting d. The underlying LP solution was
  already correct — worth remembering reconstruction must map variable index
  to digit, not print the variable value.)

## Open questions

- None for the MILP route. The backtracking solver's L=16 completion time
  remains its own concern (another track); its output is not required for the
  MILP result, only for a direct string-to-string cross-check.
