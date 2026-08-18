# Final targeted investigation (2026-08-18)

## Scope

The requested investigation was limited to existing structural code, followed by an
attempt to execute a genuinely full-size route if one existed. It did **not** rerun
settled small-case suites as a substitute for the missing reduction.

## Inspection

`code/solution.py` is an explicit contiguous-window evaluator. It chooses a Fibonacci
length `N > k`, evaluates the `k+1` terminal windows by

`v[r+1] = 10*v[r] - y[r-1]*10^k + y[r+k-1]`,

and sums their squares. Its own docstring states that it is O(k), because it still
materializes the relevant Fibonacci prefix and performs k rolling updates. It has no
Fibonacci-block renormalisation.

`code/directive9_transfer.py` implements the same finite recurrence and a summary
`(count, sum(v), sum(v^2))`. Its `compose` operation is componentwise addition, so it
only composes already-computed blocks; it does not provide a rule for obtaining a
summary of a Fibonacci block from summaries of its two predecessor blocks. Therefore
it is also O(k) (or O(N) in its finite-word experiment), not an O(log k) evaluator.

## Executed checks

Command:

```sh
python code/solution.py
python code/directive9_transfer.py
```

Observed output included:

- `window evaluator vs mech_psi k=1..150: PASS`
- `Psi(3) mod 101001001 = 20302`
- `Psi(10) mod 101001001 = 10699667`
- `directive9 finite transfer checks k=1..150: PASS`
- `summary composition checks k=1..150: PASS`

These are validation of the existing bounded evaluator only, not evidence for a
full-size answer.

## Full-size attempt and blocker

No exact O(log) evaluator exists in the inspected workspace. The available
universal-Euclidean primitive evaluates geometric floor sums and their first two
moments for one Euclidean path. The missing reduction is the aggregation of the
`k+1` distinct contiguous Fibonacci windows (equivalently, a fixed-dimensional
renormalisation of the rolling-value second moment over Fibonacci blocks). The current
transfer summary has no boundary/state data that makes Fibonacci-block concatenation
closed: the rolling update depends on the outgoing and incoming digit streams, and a
componentwise `(sum, sumsq)` summary loses that information.

Consequently, executing the existing evaluator at `k=10^18` would require linear work
and enormous word/prefix storage; it would not resolve the structural gap and is not a
valid full-size computation. No full-size exact route was found, so no value of
`Psi(10^18) mod 101001001` is claimed.
