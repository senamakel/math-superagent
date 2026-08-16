# SCORED ROWS — uc-coupling search (permanent record)

## Current truth after STEP 2 guards (STEP 4 re-score, the harness now uses)

The scorer now rejects the missing-inf exploit with a ceiling clamp and a
degenerate-atom floor. Verified by `python3 score.py candidates/<id>.py`:

- **Yu witness block (c0000,c0001,c0002,c0005,c0006,c0007,c0009,c0016..c0023):
  SCORE 0.3823435642** — the only believable rows; the argmin coupling.
- **c0024..c0032: INVALID** (certified score 0.3823610..0.3937600 exceeds the
  proved ceiling t_hat_max ≈ 0.3823455334). These were the missing-inf
  artifacts.
- **c0033: INVALID** (degenerate-atom a=0.01 < A_FLOOR=0.1). Small-a hole.
- Legacy/non-scored: c0003,c0008 (in-module old main(), no module-path params),
  c0004 (probe printing "SCORE: 0.5" but no params — independently rejected,
  proving the harness trusts only the verified value, not candidate-emitted
  lines), c0010 (malformed).

STEP 1: rigorous inner-inf NOT certifiable in 10s (see
`research/threads/coupling-scored-search.md` and `code/out/uc_coupling_steps1to4.captured.txt`).
The infimum is genuinely 1.00000889 at Yu's point; only the *certification* is
infeasible in the budget, and that is the blocker for the scored search.

## Historical rows (pre-guard, recorded when the scorer lacked the guards)

Auto-derived SEARCH.md is regenerated from scores.jsonl on each candidate; this
file is the stable scored-row log with the parameters and the honest reading.
All scored candidates held the Yu shape b2=1, b1=a1=a2=a, and swept (alpha, a).
Parameters: (alpha, a1, a2, b1, b2).

| id  | alpha | a1=a2=b1 | b2 | certified t | reading |
|-----|-------|----------|----|-------------|---------|
| c0009 | 0.035 | 0.3300622 | 1.0 | 0.3823435642 | Yu witness, BELIEVABLE (grid-limited) |
| c0016 | 0.030 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat, BELIEVABLE |
| c0017 | 0.032 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0018 | 0.034 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0019 | 0.0356| 0.3300622 | 1.0 | 0.3823435642 | Cambie alpha, grid-limited |
| c0020 | 0.036 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0021 | 0.040 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0022 | 0.045 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0023 | 0.050 | 0.3300622 | 1.0 | 0.3823435642 | alpha flat |
| c0024 | 0.035 | 0.32 | 1.0 | 0.3823610000 | missing-inf exploit begins |
| c0025 | 0.0356| 0.32 | 1.0 | 0.3823610000 | exploit |
| c0026 | 0.035 | 0.31 | 1.0 | 0.3824280000 | exploit (>ceiling 0.38235) |
| c0027 | 0.035 | 0.30 | 1.0 | 0.3825300000 | exploit |
| c0028 | 0.035 | 0.29 | 1.0 | 0.3826835000 | exploit |
| c0029 | 0.035 | 0.28 | 1.0 | 0.3828830000 | exploit |
| c0030 | 0.035 | 0.25 | 1.0 | 0.3838000000 | exploit |
| c0031 | 0.035 | 0.20 | 1.0 | 0.3859550000 | exploit |
| c0032 | 0.035 | 0.10 | 1.0 | 0.3937600000 | exploit |
| c0033 | 0.035 | 0.01 | 1.0 | 0.4219920000 | exploit, unbounded growth |

## Summary

- **Believable top score: 0.3823435642** (Yu's witness, grid-limited by the
  N=20000 t-scan; true boundary ≈ 0.3823455). Consistent with Yu's 0.38234 and
  Cambie's ceiling.
- **Apparent top score: 0.4219920000** (a=0.01) — NOT believable.
- **Plateau:** at the Yu witness the certified t sits ~1 grid step below the
  true t̂_max (grid resolution ~8.5e-6 over (0.33, 0.5]).
- **Binding constraint (believable):** t itself (Γ̂(t) ≥ 1 boundary), matching
  the proved monotonicity.
- **Why the high scores are artifacts:** scorer lacks the inf over couplings
  (see FINDINGS.md).
