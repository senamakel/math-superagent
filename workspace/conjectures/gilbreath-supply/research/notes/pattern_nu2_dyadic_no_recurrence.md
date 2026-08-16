# nu2(2^k) subsequence: no recurrence, not polynomial, OEIS miss

From `code/out/excess_E2_30000.txt` (exact) via nu2(2^k) = (2^k − 2 − S(2^k))/2:

    nu2(2^k) for k = 2..15:  [2, 2, 12, 13, 27, 66, 136, 243, 502, 1003, 2010, 4184, 8338]

## Sequence tools (exact over the terms supplied)

- `find_linear_recurrence`, max_order 6: **no constant-coefficient linear
  recurrence** fits all 13 terms.
- `analyze_sequence`: differences never become constant within 12 levels → not a
  low-degree polynomial.
- `oeis_lookup` on nu2(n) n=2..25 `[1,1,2,1,2,1,2,7,4,5,3,5,3,11,7,7,13,10,10,8,
  11,11,13,10]`: **miss** — sequence not catalogued.

## Consequence

No closed form to look up; any regularity in nu2 must come from the problem
itself (the fold + prime gap-parity input), not from a known catalogued family.
This is consistent with the fold-generic-√n picture: the pointwise values behave
like a random walk's increments, and a random walk has no polynomial/low-order
recurrence in its positions at dyadic times either.

Recorded so nobody searches again.
