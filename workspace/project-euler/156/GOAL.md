# Goal

**Problem (PE156):** Write the natural numbers 0,1,2,... consecutively in base 10.
Define `f(n,d)` = total number of occurrences of the digit `d` in all integers
written down from 0 through `n` inclusive.

Solve `f(n,d) = n` for each digit `d ∈ {1,...,9}`; let `s(d)` = the sum of all
such solution values `n` for that `d`. Per the note, if the same `n` satisfies
`f(n,d)=n` for several `d`, it is counted once for every such `d`.

**Answer required:** `Σ s(d)` for d = 1..9.

**Completion criteria / oracle (all now reproduced by `code/brute.py`):**
- f(n,1) for n = 0..12 = 0,1,1,1,1,1,1,1,1,1,2,4,5 —— reproduced.
- First solutions of f(n,1)=n are 0, 1, then 199981 —— reproduced (within 0..200000).
- f(n,1) never equals 3 —— confirmed not attained in 0..200000.
- s(1) = 22786974071 (target, reproduced only by the efficient method, not brute force).
- The brute-force size needed to reach s(1) (~2e10) is the budget-defeating
  bound; the efficient method must handle it.
