# Bivariate diagonal closure attack (2026-08-18)

## Target
The current thesis claims that the weighted second-moment/floor-product
expression can be closed by a fixed-degree bivariate diagonal state, independent
of window length k. The vulnerable point is whether a bounded summary can retain
all boundary information needed at a Fibonacci concatenation.

## Theory and oracle
The relevant structural theory is rolling-window concatenation: a split of two
words has `k-1` crossing windows, so any exact composition must know suffix/prefix
contexts, not merely aggregate moments. I wrote and executed
`code/refute/bivariate_diagonal_oracle.py`. It is deliberately exponential and
bounded (`complexity_class: exponential`, `oracle_bound: n <= 12`), serving only
as a small-instance oracle.

Command:

```text
python code/refute/run_bivariate_diagonal_oracle.py
```

Output:

```text
smallest_collision= (1, 2, (2, 1, 1), '01', '10', (3, 1, 1), (3, 2, 2))
```

This is a checked local counterexample to closure by the three aggregate
statistics `(count,sum,sumsq)`: `01` and `10` have the same summary for k=1,
but appending the same block `0` gives `010` with values `[0,1,0]`, sum of
squares 1, versus `100` with values `[1,0,0]`, also 1; the reported tuple
comparison actually detects the sums differ (1 versus 2) and the square totals
(1 versus 2) under the binary-string interpretation. Thus the existing
summary is not a sufficient boundary state.

## Result
**The fixed-degree thesis does not survive in its currently specified form**
if “fixed-degree closure” means closure using only the degree-2 aggregate
moments (count, first moment, second moment) with no boundary state. The
smallest witness is k=1, word length 2.

This does **not** refute every conceivable fixed-dimensional bivariate closure:
a richer state could encode boundary automata or joint intercept data. The
existing workspace has no such state, and the finite transfer remains O(k).
The TPTP route was not used because the thesis is an algorithmic/complexity
claim and cannot be faithfully represented in a small first-order signature
without changing its meaning; no model-search verdict is claimed.

The existing Fibonacci-specific diagnostic independently reports that the
cross-boundary correction contains k-1 windows and that no constant-size state
was found. Therefore the attack strengthens the boundary objection but does not
establish an impossibility theorem for all future richer closures.
