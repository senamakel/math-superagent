Attempt 2 verified status

- `python code/brute.py` outputs `psi(3)= 20302` and `psi(10) mod M= 10699667`, reproducing both statement examples.
- `python code/refute/run_fib_block_state_counterexample.py` reports the smallest local summary collision: `010` and `101` share `(2, 11, 101)`, but appending `0` gives `(3, 11, 101)` versus `(3, 21, 201)`.
- `code/lean/G4BlockStateNonClosure.lean` was checked with no sorry and no axioms; theorem `k2_summary_nonclosure` is kernel-verified.
- No fixed-dimensional joint intercept/block-collapse theorem or honest value of Psi(10^18) was established.
