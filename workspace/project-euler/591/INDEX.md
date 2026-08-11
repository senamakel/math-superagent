# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and evidence rules; read before any work. Defines the oracle-driven, no-enumeration method policy and the housekeeping conventions for indexes, research/, toolkits/, goal.md, tasks.md, memory.md, scratchpad.md. |
| `README.md` | Library-level README explaining how a problem workspace is organised (start at AGENTS.md, use prompts/ for role guidance, define completion in goal.md, etc.). |
| `GOAL.md` | The objective: PE591, sum of abs(I_d(BQA_d(pi,10^13))) over non-square d less than 100. States the 4 worked examples (the test oracle) and the completion criteria. |
| `MEMORY.md` | Durable working memory: problem restatement, verified worked examples, established results (Cabanillas method, all-90-d validation, d=2 oracle), failed approaches, and the current CORRECTED both-sign final answer S=526007984625966 (records the b-may-be-negative correction and the now-obsolete positive-only S=498809825393729). |
| `problem.md` | The PE591 problem statement (converted to HTML); the 4 worked example values and the question about I_d. |
| `SCRATCHPAD.md` | Scratch area for draft findings being validated; durable results promoted to memory.md and research/notes/. |
| `solution.md` | The PE591 derivation: reduction of BQA to the inhomogeneous problem min over b in [0,L] of the distance of b*alpha-beta to nearest integer (both signs of b via beta=frac(pi) and 1-beta), the governing Cabanillas Prop 9/10 candidate method, the algorithm, verification, and S=526007984625966. |
| `TASKS.md` | Task checklist for the run: brute-force example reproduction, record probes, semiconvergent hypothesis, deriving the method, computing and verifying S. |
| `verify_run_report.md` | Verbatim output and independent re-sum verification of the PE591 oracle run (brute.py, solution_bothsides.py, results_full_bothsides.txt) confirming S = 526007984625966. |
