# Surreal numbers — why each number's value (a−b) is exact, and its limits

Source: https://en.wikipedia.org/wiki/Surreal_number ; Conway, *On Numbers and Games*, Academic Press 1976.

## What it establishes
- Surreal numbers generalize the reals (all reals plus infinite and infinitesimal objects) and form an ordered field; every game position that is a "number" compares and adds like ordinary numbers.
- The number `{L|R}` with all L<R is the simplest surreal strictly between L and R; simplest integers are the standard ones (0 simplest of all, then ±1, ±2, ...).
- Conway's construction grew out of Go endgame analysis (positions that decompose into sums whose values add), the same template that motivates the run's counting reduction.

## Why it applies here
- In the counting model each component G(a,b) = {a-b-1 | a-b+1} is a number (both options are numbers, left < right), and its simplest value between the two is the integer a−b (see disjsum note). Since adding surreal numbers = adding integers, the whole position's value is A−B. This is the precise, exact statement that "the position reduces to a single integer."

## What it does NOT settle
- Skips are not ordinary moves: they create a self-loop that is outside the short-game number framework (see loopy note). The surreal value A−B captures the no-skip outcome only; the skip budget S(n) is a different object computed by the DP. Also, the value is exact only for the counting model, which real leading-bit deletions can violate (see disjsum caveat).
