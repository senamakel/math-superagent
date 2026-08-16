# Floor-convention robustness of the nu2/n dip

## Question

Does the pointwise dip `nu2(53)/53 = 0.3585` (below the 0.42 claimed by
stored rung `R-finite-verified`) survive the choice of fold floor convention?

## Result (exact, n = 2..4000)

| convention | min nu2/n in [50,4000] | at n | # points < 0.42 |
|---|---|---|---|
| d in [2, n-1] (canonical) | 0.3585 | 53 | 10 |
| d in [3, n-1] | 0.3585 | 53 | 11 |
| d in [2, n-2] | 0.3396 | 53 | 11 |

The dip is robust. In every convention the global minimum is at `n=53` and
there are 10-11 points in `[50,4000]` with `nu2/n < 0.42`.

## Conclusion

The `R-finite-verified` statement — "nu2/n >= 0.42 for all 50 <= n <= 4000"
for the real prime string — is **false** under every floor convention tested.
The `0.42` figure traces to the problem.md table that `research/BACKWARD.md`
flagged as ungrounded prose.

This does **not** refute SUPPLY: the mean `nu2/n` over `[50,4000]` is `0.4986`,
so a smaller constant (e.g. `c = 0.33`) holds pointwise, and the averaged/
density-1 form is far stronger numerically. It simply invalidates the specific
pointwise constant `0.42` over that range.

## Evidence

Exact integer computation, DP cross-checked against brute-force submask
enumeration (PASSED at n in {2,3,5,8,13,21,34,55,64,89,100,128}).

**Independent corroboration.** `code/out/averaged_mean_capture.txt` (a
separate program, `averaged/mean_capture.py`) reports `prime nu2/n over
n=50..100: min=0.3396`, explicitly noting the literature `[0.42,0.52]` band is
not met in that range. This is a second, independent route to the same
refutation of the pointwise 0.42 floor — not merely a re-check of my DP.
