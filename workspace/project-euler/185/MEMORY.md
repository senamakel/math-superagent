# Working memory

## Problem

Project Euler 185 (Number Mind): find the unique N-digit secret s where for
each guess i, the number of positions j with g_i[j]==s[j] equals count[i].
Example (N=5) answer: 39542. Full instance N=16, M=22.

## Established results

- The problem is exact-match constraint satisfaction: each guess imposes
  exactly count[i] matching positions.
- (Not yet established by execution — pending brute.py and solution.py outputs.)
- Classical governing structure: this is a small constraint-satisfaction
  problem over a 16-digit sequence with 22 per-guess "exact Hamming count"
  constraints. Because each constraint is a count (not a position), the
  search space 10^16 can be cut by the two-sided pruning bounds:
    matches_so_far(i) <= count[i]
    matches_so_far(i) + positions_remaining >= count[i]
  applying to every guess at every partial assignment. Unlike Mastermind, the
  secret is a fixed string, so the standard technique is exact-cover-style
  backtracking (each guess fixed, positions chosen), not the `secret`-space
  enumeration Mastermind solvers use.

## Failed approaches

- (none yet)

## Open questions

- Whether 10^16 full enumeration (brute.py) on N=16 is feasible — it is not;
  brute.py is only the small-N oracle. The full-size answer must come from
  solution.py's pruning.
