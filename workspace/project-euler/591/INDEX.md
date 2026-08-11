# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and evidence rules; read before any work. Defines the oracle-driven, no-enumeration method policy and the housekeeping conventions for indexes, research/, toolkits/, goal.md, tasks.md, memory.md, scratchpad.md. |
| `README.md` | Library-level README explaining how a problem workspace is organised (start at AGENTS.md, use prompts/ for role guidance, define completion in goal.md, etc.). |
| `brute.py` | Naive BQA brute force: for d, x, n scans all b in [-n,n] and takes the nearest a to minimise abs(a+b*sqrt(d)-x). Reproduces worked examples 1-3. Float arithmetic; not scalable. |
| `check_rel.py` | Investigated whether abs(I_d) equals round(sqrt(d)*b_d). Hypothesis **disproved** (see memory.md); kept as a record of a failed approach. |
| `compute_I.py` | Computes I_d and b_d for all non-square d in [2,99] at n=10^4 by scanning b in [0,n]. Small-scale data generation; also prints the abs(I_d) sequence. |
| `config.toml` | Run configuration for the mathematical-research workspace: solver preferences (exact arithmetic, forbid exponential time/space) and artifact file names. |
| `goal.md` | The objective: PE591, sum of abs(I_d(BQA_d(pi,10^13))) over non-square d less than 100. States the 4 worked examples (the test oracle) and the completion criteria. |
| `memory.md` | Durable working memory: problem restatement, verified worked examples, established results (Cabanillas method, all-90-d validation, d=2 oracle), failed approaches, and the final S=498809825393729. |
| `probe_records.py` | Task 2 probe: scans b in [0,2e6] for several d, collects record-holding b's of the distance of b*sqrt(d)-pi to nearest integer, and checks whether each is a semiconvergent denominator of sqrt(d). |
| `probe_semi.py` | Explores which candidate irrational (pi/sqrt2, pi*sqrt2, 2pi*sqrt2, pi, 2pi) the d=2 record b's match as semiconvergent or convergent denominators. |
| `probe_structure.py` | Fast float scan: whether d=2 record b's match convergent denominators of pi/sqrt2, pi*sqrt2, etc. Probe; superseded by the Cabanillas candidate-set method. |
| `problem.html` | The PE591 problem statement (converted to HTML); the 4 worked example values and the question about I_d. |
| `problem.url` | The Project Euler URL for problem 591 (https://projecteuler.net/minimal=591). |
| `results_full.txt` | Output of solution.py for PE591 at n=1e13: one line per non-square d in [2,99] giving d, b, a, abs(a), and the final line S=sum(abs(a))=498809825393729. This is the reported answer. |
| `scratchpad.md` | Scratch area for draft findings being validated; durable results promoted to memory.md and research/notes/. |
| `solution.py` | PE591 scalable solver: for each non-square d in [2,99] at n=1e13, finds b_d = argmin of the distance of b*sqrt(d)-pi to nearest integer over b in [0,L] using the Cabanillas (arXiv:1904.01874) Prop 9/10 candidate-set method (O(log L)), then a_d = nint(pi - b_d*sqrt(d)). Reproduces all 4 worked examples; writes results_full.txt. Authoritative answer source. |
| `struct_probe.py` | Probe verifying the d=2 given oracle b,a satisfy the BQA relation and scanning small-scale record b's for d=2; early structural investigation. |
| `tasks.md` | Task checklist for the run: brute-force example reproduction, record probes, semiconvergent hypothesis, deriving the method, computing and verifying S. |
| `verify_cabanillas.py` | Standalone small-scale verification of Cabanillas Prop 9/10 candidate structure for a few alpha,beta pairs against brute force. Superseded as a toolkit by toolkits/ostrowski_verify.py and toolkits/verify_cabanillas_exact.py. |
