# Tasks

- [x] Reproduce the statement's oracle with brute force (`code/brute.py`):
      f(n,1) table n=0..12, f(22,2)=6, first solutions 0, 1, 199981.
- [x] Build the efficient evaluator (place-value, `code/lib/digits.py`) and
      verify against the oracle.
- [x] Write and run `code/verify.py`, the independent second route
      (two MSD digit-DP evaluators, no place-value peeling; own jump iterator).
- [x] Compute the grand total Σ s(d) for d=1..9: **21295121502550**,
      verified three ways (both new evaluators + primary f_place_value),
      against the naive oracle to 300000, and against the earlier primary
      run's per-digit solution files on disk (all identical).
