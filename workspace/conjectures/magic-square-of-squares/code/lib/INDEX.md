# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `mss.py` | Exact-integer core for the 3x3 magic square of squares: is_perfect_square/sqrt_or_none, grid_from_params(c,u,v), params_from_grid (completeness map), lines_of/line_sums/magic_sum, failure_of and is_magic_square_of_squares (ground-truth verifier), count_squares, the 8x9 line-incidence matrix and Fraction rank/RREF nullspace helpers, two_square_splits, and the two literature near-misses built directly from the printed grids (sallows_ls1_grid, bremner_magic_grid). Verified by code/check_near_misses.py: parametrisation identity and completeness on ~720k exact grids, both 7-square grids' line sums and square counts, incidence rank 7 / affine dimension 3 over Q (sympy cross-check). |
