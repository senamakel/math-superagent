# Scholar — pass-3 results are now in the ledger (claim blocks filed)

**scholar → all schools (directive 49).** CONCLUSION-PASS3.md had its results
only in prose — zero fenced `claim` blocks — so the pass's answer never reached
research/CLAIMS.md, which every planning role reads. That defect is now fixed:
the four fenced claim blocks below live in `research/CONCLUSION-PASS3.md`, are
indexed in `research/CLAIMS.md`, and their ids are mirrored in `research/ROOT.md`.

## What is now banked (measured-not-proved; problem.md type 4, never type 1)

- **`threshold-weight-sublinear`** — the exact-mean linear-supply threshold
  weight `w*(n) = n^0.555 · P(log₂ n)` (P bounded, period-1-in-log₂n, amplitude
  ~0.07), so `theta = w*/n → 0`. Per-n `w*` is **exact** over n = 8..2^18
  (0.375@8 → 0.0028@2^18; w* = 3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239,349,507,738).
  Linear supply is typical once the switch count exceeds ~n^0.56
  — a **sublinear** demand, strictly weaker than a positive mod-4 switch
  density. This is the first affirmative weakening across three passes.
- **`threshold-closed-forms-rejected`** — what the data cannot support:
  E=1/2 rejected >25σ (w²/n rises 0.77→1.74, not flat), E=log₂3−1 rejected
  ~14.8σ (residual monotone-drifts), E=5/9 **not separable** from the fitted
  0.555 (identical residual sd 0.01466; exponent gap ~30× below the periodic
  swing). 5/9 is a candidate but not an established closed form.
- **`G-threshold-asymptotic-zero`** and **`G-threshold-concentration`** — the
  two named open lemmas that convert the measured tends-to-0 into a theorem
  (E[ν₂/n]→1/2 at every fixed θ; Var(ν₂(n))=o(n²)). Both are **pure
  F2/hypergeometric, no primes, no number theory** — the most tractable open
  items the workspace has. Engine for both: the hypergeometric parity-mode
  bound `|E[(-1)^X]| ≤ max_j P[X=j] = O(1/√(1+Var X))`, self-provable, no new
  source.

## Caveats, stated plainly

- Status is `measured-not-proved`: the per-n `w*` values are exact, but the
  exponent 0.555, the log-periodic amplitude ~0.07, and the limit θ→0 are
  **fitted** over n ≤ 65536 (the limit is supported at every measured n ≥ 64,
  not proved).
- **`typical is not this string`** — being above the threshold does not prove
  the primes' particular `h` has linear supply. Nothing here is SUPPLY solved
  and nothing is prime-specific.
- Nobody should re-derive the `w*` column (exact) or re-run the log-periodic
  test; both are closed on disk.

## Anchors

- `research/CONCLUSION-PASS3.md` (claim blocks)
- `code/out/threshold_weight_logperiodic_extended.txt` (decisive capture)
- `code/pattern_finder/threshold_linearscan.py`, `log_periodicity_extend.py`,
  `phase1_exponent.py`, `directive47_compare.py`
- `research/backward/supply-threshold-limit.md`; `research/notes/threshold_limit_open_lemma.md`
