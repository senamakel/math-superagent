# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive exact oracle for PE 597: chronological race simulation + parity of the new order derived from bump chains. Exposes `simulate_order`, `parity_of_new_order`, `outcome_parity`. Reproduces all five rows of the n=3,L=160 table. NOTE: `simulate_order` still has the multi-bump overwrite bug; the corrected engine is `simulate_order_nobug.py`. |
| `bump_study.py` | Monte Carlo structural study (small n, L=160): for each sample records parity, bump multiset, finishes, chain-pair count; verifies `parity == (#chain pairs) mod 2` on every sample and histograms bump-pattern types split by parity. MC driver, not a solver. |
| `check_counterexample.py` | Sanity/oracle check: validates the counterexample pair ce1/ce2 (n=3) give opposite parities with float and exact agreement, and prints uniform-grid even-count ratios for M in (8,16,32). Grid converges to 0.5, not 56/135 — a sampling-measure artifact (uniform grid ≠ Exp(1)), not a parity bug. |
| `exact_race.py` | Exact-rational race dynamics mirroring `brute` on Fractions (`simulate_order_exact`, `outcome_parity_exact`); tuple-vs-Fraction comparison bug fixed so it runs. Like `brute`, carries the multi-bump overwrite limitation. |
| `examine_multibump.py` | Diagnostic demonstrating the multi-bump overwrite bug in `brute.simulate_order`: `bumped_by[k]` keeps only the last bumper, silently losing earlier bump edges that the new-order reachability needs. Not a solver; a bug demonstration. |
| `high_precision_mc.py` | High-precision parallel Monte Carlo for p(n,L) using the verified `brute.py` engine. Each worker runs its own RNG seed and chunk; results pooled with binomial-mean SE. Usage: `python3 high_precision_mc.py n L total_samples` (one process per (n,L)). MC estimator, not exact. |
| `monte_carlo.py` | Plain Monte Carlo oracle: draws iid Exp(1) speeds and counts even-parity outcomes via `brute.outcome_parity`, printing an estimate of p(n,L). Fallback exact-tie-break note; plain N-event MC. |
| `out/trace.jsonl` | _(undescribed)_ |
| `scratch_verify_invexp.py` | RETIRED / superseded. One-off retired MC scratch verifying an inverse-exponential claim; the claim is now sourced in `research/inverse_exponential_finish_times_wikipedia.md`. Kept as a record only. |
| `simulate_order_nobug.py` | Corrected race engine fixing `brute`'s multi-bump overwrite: records every bump edge and computes placed-below sets by graph reachability. Same API as `brute.simulate_order` / `parity_of_new_order`. This is the reference-correct engine. |
| `verify_hypothesis.py` | MC verifier of both statement examples plus the structural test "final parity depends only on the w-order" — which it refutes (buckets hold both parities). |
