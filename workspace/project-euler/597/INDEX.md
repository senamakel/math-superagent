# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method and evidence rules for the whole run: restate the problem, test small cases, prefer theory over enumeration, keep sourced facts separate from deductions, keep files described. |
| `README.md` | Folder-layout note pointing newcomers to AGENTS.md, `prompts/`, and the goal/tasks/scratchpad/memory working files. |
| `brute.py` | Naive exact oracle for PE 597: chronological race simulation + parity of the new order derived from bump chains. Exposes `simulate_order`, `parity_of_new_order`, `outcome_parity`. Reproduces all five rows of the n=3,L=160 table (comparator bug already fixed). |
| `check_counterexample.py` | Sanity/oracle check: validates the counterexample pair ce1/ce2 (n=3) give opposite parities with float and exact agreement, and prints uniform-grid even-count ratios for M in (8,16,32). Grid converges to 0.5, not 56/135 — a sampling-measure artifact (uniform grid ≠ Exp(1)), not a parity bug. |
| `config.toml` | Solver configuration: prefer exact arithmetic, verify with code, forbid exponential time/space, and names of the goal/memory/scratchpad/solution artifact files. |
| `exact_race.py` | Exact-rational race dynamics mirroring `brute` on Fractions (`simulate_order_exact`, `outcome_parity_exact`); Latent tuple-vs-Fraction comparison bug fixed so it runs. |
| `goal.md` | Restated PE 597 goal with the full setup (every symbol defined), the n=3,L=160 worked probability table, the given p(4,400), the target p(13,1800), and the completion criteria. |
| `memory.md` | Working memory: established results (brute now reproduces the table; comparator bug fixed), failed approaches (the w-order-only hypothesis, refuted), and the open question of the exact method. |
| `monte_carlo.py` | Monte Carlo importance-sampling integration oracle over Exp(1) speeds; calls `brute.outcome_parity`. (A separate, simpler route than a hand integration.) |
| `problem.html` | The downloaded PE 597 statement (Torpids) — the source document this run is solving. |
| `problem.url` | URL of the PE 597 statement (projecteuler.net/minimal=597). |
| `race_spec.md` | Exact chronological race-dynamics specification for implementation: event simulation, bump/OUT/FINISH treatment, and the bump-chain parity definition. Reference contract for any race solver. |
| `scratchpad.md` | Provisional work: the diagnosis of the parity-comparator bug, its fix, and the corrected MC run output. |
| `tasks.md` | Task checklist: done items (verify sample, fix comparator, MC re-check) and the open task to solve p(13,1800) exactly. |
| `verify_hypothesis.py` | MC verifier of both statement examples plus the structural test "final parity depends only on the w-order" — which it refutes (buckets hold both parities). |
 |
