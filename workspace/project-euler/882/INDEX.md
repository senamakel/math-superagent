# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and housekeeping rules for every agent. |
| `CONTEXT.md` | Records what the reference library now establishes beyond its prior state: O(log n) computation of A(n),B(n) via OEIS A000788/A059015 for the (A,B) counting game at n=10^5. |
| `GOAL.md` | The objective and completion criteria: build and validate TASK A (real-game brute) and TASK B (counting-game (A,B) DP). |
| `MEMORY.md` | Working memory: problem restatement, given values, established results (to fill), failed approaches, open questions. |
| `README.md` | Standard project boilerplate: how to use AGENTS.md, prompts/, goal/tasks/scratchpad/memory. |
| `SCRATCHPAD.md` | Scratchpad for provisional calculations not yet ready for memory.md. |
| `TASKS.md` | Task checklist (single placeholder task row). |
| `brute.py` | Root copy of TASK A: naive minimax over the REAL bit-deletion game, mirrors code/brute.py. Kept at root because GOAL.md names /workspace/brute.py; the canonical program is code/brute.py. |
| `dyadic_answer.txt` | Two-line output of the Euler 882 solution: (1) every k in 1..100000 is a Number (no violating k), (2) S(100000) = ceil(G(100000)) = 15800662276. |
| `dyadic_clean.py` | Clean compact version of the dyadic g(k) computation with Number-ness check: prints g(k) for k=1..30 and S=ceil(G(n)) vs real oracle. Byte-identical file also at code/dyadic_clean.py. |
| `gstudy.py` | Scratch analysis of the single-number dyadic CGT value g(k) structure: checks g(2k) vs g(k)/2 for divergences and prints g around powers of 2, using the same one/zero-deletion + Simplicity-Rule engine as gtable.py/dyadic_clean.py. Exploratory; stdout only, no saved output. |
| `gtable.py` | Computes the single-number dyadic CGT value g(k) via the Simplicity Rule (one/zero-deletion options) up to a chosen bound (argv default 60), prints k and g(k) tab-separated, and S(n)=ceil(G(n)) for the board. Part of the dyadic-value scratch line of work (dyadic.py/dyadic_clean.py/gstudy.py); exploratory, stdout only, no saved output. |
| `indep_check.py` | Independent verification of PE882: g(k) by direct recursive surreal-value evaluation with its own from-scratch birthday-scan simplest-dyadic-between, exact-sum G(100000), S=ceil. Cross-checks solution.py/verify_dyadic.py. |
| `oracle_S.txt` | Root stray duplicate of code/out/oracle_S.txt (byte-identical): the real-game minimax S(n)=1,2,8,9,17 for n=1..5. Canonical copy lives in code/out/oracle_S.txt; read that one. |
| `problem.md` | The problem statement: partisan bit-deletion game, definition of S(n), given values S(2)=2, S(5)=17, S(10)=64, ask for S(10^5). |
| `scratchpad_run.md` | Scratch log note ("run existing programs, executed inline, see transcript") from an earlier scratch run; no durable claims. |
| `solution.md` | Write-up of the dyadic-CGT solution to Project Euler 882: governing theory (Simplicity Rule / canonical Numbers), reduction S(n)=ceil(G(n)), exact result, and verification routes. |
| `solution.py` | The solution implementation: forward dyadic sweep of g(k) (simplest dyadic between max(Left)/min(Right)) for k=1..100000, checks every k is a Number, prints S(n)=ceil(G(n)) for n=1..20, computes G(100000) exactly and writes the final answer to dyadic_answer.txt. |
| `solve_dyadic.py` | Full-size solver attempt: computes S(N)=ceil(G(N)) with G(N)=sum_{k<=N} k*g(k), g(k) the dyadic CGT value of the single-number bit game via the Simplicity Rule, by direct O(N log N) iteration so N=1e5 is cheap (argv default 100000; default ~how long depends on g(k) birthday scan). Prints G(N), S(N), and the S(n) sequence for n=1..30. Root stray: a program that belongs in code/ (canonical home would be code/solve_dyadic.py); no out/ capture of its run was found. Whether S(N)=ceil(G(N)) for the dyadic-CGT model is correct for the real game is open — the real-game oracle confirms only S(1..5); note it is a scratch attempt, not yet verified against brute at the values that matter. |
| `verify_dyadic.py` | Independent verification of G(N)=sum k*g(k) via a separate code path (explicit one_deletions/zero_deletions expansion at each k), printing exact numerator/denominator and S(N)=ceil(G(N)). Cross-checks solve_dyadic.py by a second route. |
