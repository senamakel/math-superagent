# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and evidence rules; read before any work. Defines the oracle-driven, no-enumeration method policy and the housekeeping conventions for indexes, research/, toolkits/, goal.md, tasks.md, memory.md, scratchpad.md. |
| `README.md` | Library-level README explaining how a problem workspace is organised (start at AGENTS.md, use prompts/ for role guidance, define completion in goal.md, etc.). |
| `brute.py` | Naive BQA brute force: for d, x, n scans all b in [-n,n] and takes the nearest a to minimise abs(a+b*sqrt(d)-x). Reproduces worked examples 1-3. Float arithmetic; not scalable. |
| `brute_n7.py` | Independent brute force at n=10^7 (mpmath dps=40): scans all b in [-floor(n/sqrt(d)),floor(n/sqrt(d))] for the 16 chosen d, sets a=nint(pi-b*sqrt(d)) clamped to [-n,n], and minimises the resulting error. Writes results_brute_n7.txt and prints a comparison against the n=1e13 solver file (expected to differ). Not scalable. |
| `brute_n7_run.log` | Captured stdout of the brute_n7.py run: per-d (d, b, a, absolute-a, err) rows plus a comparison against results_full_bothsides.txt whose per-d MISMATCHes are expected (brute at n=1e7, solver file at n=1e13). |
| `check_rel.py` | Investigated whether abs(I_d) equals round(sqrt(d)*b_d). Hypothesis **disproved** (see memory.md); kept as a record of a failed approach. |
| `compute_I.py` | Computes I_d and b_d for all non-square d in [2,99] at n=10^4 by scanning b in [0,n]. Small-scale data generation; also prints the abs(I_d) sequence. |
| `config.toml` | Run configuration for the mathematical-research workspace: solver preferences (exact arithmetic, forbid exponential time/space) and artifact file names. |
| `goal.md` | The objective: PE591, sum of abs(I_d(BQA_d(pi,10^13))) over non-square d less than 100. States the 4 worked examples (the test oracle) and the completion criteria. |
| `memory.md` | Durable working memory: problem restatement, verified worked examples, established results (Cabanillas method, all-90-d validation, d=2 oracle), failed approaches, and the current CORRECTED both-sign final answer S=526007984625966 (records the b-may-be-negative correction and the now-obsolete positive-only S=498809825393729). |
| `probe_records.py` | Task 2 probe: scans b in [0,2e6] for several d, collects record-holding b's of the distance of b*sqrt(d)-pi to nearest integer, and checks whether each is a semiconvergent denominator of sqrt(d). |
| `probe_semi.py` | Explores which candidate irrational (pi/sqrt2, pi*sqrt2, 2pi*sqrt2, pi, 2pi) the d=2 record b's match as semiconvergent or convergent denominators. |
| `probe_structure.py` | Fast float scan: whether d=2 record b's match convergent denominators of pi/sqrt2, pi*sqrt2, etc. Probe; superseded by the Cabanillas candidate-set method. |
| `problem.html` | The PE591 problem statement (converted to HTML); the 4 worked example values and the question about I_d. |
| `problem.url` | The Project Euler URL for problem 591 (https://projecteuler.net/minimal=591). |
| `results_brute_n7.txt` | Per-d output of brute_n7.py at n=1e7 for the 16 chosen d: rows (d, b, a, absolute-a, err). Independent brute-force reference for the mid-scale check. |
| `results_full.txt` | Output of solution.py (positive-b-only) for PE591 at n=1e13: rows d, b, a, abs(a), and S=sum(abs(a))=498809825393729. **Candidate result, superseded by results_full_bothsides.txt (the problem allows b of either sign).** |
| `results_full_bothsides.txt` | Output of solution_bothsides.py (both signs of b) for PE591 at n=1e13: rows d, b, a, abs(a), and S=526007984625966. Corrected answer consistent with the problem statement (b sign is free); supersedes results_full.txt. Current authoritative result file. |
| `results_solver_n7.txt` | Row data (d, b, a, absolute-a) of solution_bothsides.solve_d_both at n=1e7 for the 16 d. Apples-to-apples independent-check values matching brute_n7 at n=1e7 (not the n=1e13 numbers). |
| `scratchpad.md` | Scratch area for draft findings being validated; durable results promoted to memory.md and research/notes/. |
| `solution.md` | The PE591 derivation: reduction of BQA to the inhomogeneous problem min over b in [0,L] of the distance of b*alpha-beta to nearest integer (both signs of b via beta=frac(pi) and 1-beta), the governing Cabanillas Prop 9/10 candidate method, the algorithm, verification, and S=526007984625966. |
| `solution.py` | PE591 solver that considers only positive b (b in [0,L]): Cabanillas (arXiv:1904.01874) Prop 9/10 candidate-set method, a_d = nint(pi - b_d*sqrt(d)). Writes results_full.txt. **One-sided; superseded by solution_bothsides.py.** |
| `solution_bothsides.py` | Corrected PE591 solver considering BOTH signs of b (matching the problem, where b's sign is free): runs the Cabanillas candidate method for beta={pi} (b positive) and 1-beta (b negative), takes the global min, a = nint(pi - b*sqrt(d)). Reproduces worked examples 1-4; writes results_full_bothsides.txt. Current authoritative solver. |
| `struct_probe.py` | Probe verifying the d=2 given oracle b,a satisfy the BQA relation and scanning small-scale record b's for d=2; early structural investigation. |
| `tasks.md` | Task checklist for the run: brute-force example reproduction, record probes, semiconvergent hypothesis, deriving the method, computing and verifying S. |
| `verify_cabanillas.py` | Standalone small-scale verification of Cabanillas Prop 9/10 candidate structure for a few alpha,beta pairs against brute force. Superseded as a toolkit by toolkits/ostrowski_verify.py and toolkits/verify_cabanillas_exact.py. |
| `verify_n7_rerun.py` | Independent re-run check: calls solution_bothsides.solve_d_both(d, 10**7) for the 16 d in results_brute_n7.txt and compares (b,a) exactly against brute-force results at the same n=10^7. Corrects the apples-to-apples comparison that brute_n7.py's built-in report misses (its internal comparison is against the n=1e13 file, which is expected to differ). All 16 d PASS. |
| `verify_run_report.md` | Verbatim output and independent re-sum verification of the PE591 oracle run (brute.py, solution_bothsides.py, results_full_bothsides.txt) confirming S = 526007984625966. |
