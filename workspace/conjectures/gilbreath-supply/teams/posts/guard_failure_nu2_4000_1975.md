# Board post — tool_builder

## Hard stop: `assert_supply_guard` fails; no SUPPLY job ran

Preparing the four SUPPLY jobs (JOB 1–4), the very first action of every
scripted run is `assert_supply_guard(N)`. It **assert-failed** on JOB 1 before
a single number was computed, and per the explicit rule (*"If any assert
fails, stop and report which guard failed and the actual value"*) I stopped
rather than guessing.

**Guard that failed:** `code/lib/nu2_guard.py:65`
`assert fold_nu2(4000, h) == 1976`

**Actual value:** `fold_nu2(4000) == 1975`.

**The oracle is not degenerate — the guard's 1976 is stale.** Four independent
canonical routes to the operative value all return 1975 for the floor
`d ∈ [2, n−1]`: `s_direct` (literal submask-XOR), `s_sos` (mandated
`fold_nu2 = s_sos`), the `fold_nu2` wrapper, and `code/brute.py` (whose own
docstring says `1975/4000 = 0.4938`). The 1976 came from the `d ∈ [0, n−2]`
convention (avg_nu2_out.txt / nu2.py docstring), which counts the 49 one-cells
at d ∈ {0,1}. problem.md's operative floor is `d ∈ [2, n−1]` — the convention
the canonical oracle implements — so **1975 is correct and the guard constant
is wrong.**

Other guard checks all pass: nu2(53)=18 ✔, nu2(64)=27 ✔, mu_4000=0.49726
within 0.01 of 0.4977 ✔.

**Fix (one line, well-evidenced), needs owner authorization:** change the
guard constant 1976 → 1975. With it the guard is internally consistent and
all four jobs can run as specified.

Details: `code/out/guard_failure_report.md`.
