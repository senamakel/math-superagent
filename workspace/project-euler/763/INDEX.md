# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | The method policy for the whole run: restate and test small cases before full size, do not search the answer space, verify with a second route, treat every number as coming from a run program. Read first in any role. |
| `CONTEXT.md` | Shared context: what the run's reference library establishes, under a thousand tokens, writing down established results, contradictions, and gaps. Research team writes it; every role reads it. |
| `GOAL.md` | The objective for Project Euler 763 (amoeba division D(N)) with the worked examples D(2)=3, D(10)=44499, D(20)=9204559704, last nine of D(100)=780166455 as the test oracle, and observable completion criteria; target is the last nine digits of D(10000). |
| `MEMORY.md` | Working memory skeleton: sections for the exact problem, established results, failed approaches, and open questions. Solver roles fill the sections as results are proved. |
| `README.md` | Orientation for the workspace: one mathematical problem per directory, reproducible work, start with AGENTS.md then prompts/, completion in GOAL.md, work tracked in TASKS.md/SCRATCHPAD.md/MEMORY.md. |
| `SCRATCHPAD.md` | Scratchpad for temporary calculations, partial derivations, and observations not yet established enough for MEMORY.md. Currently only a section skeleton. |
| `SCRATCHPAD_pattern.md` | Pattern-finder working notes: the confirmed max-level decomposition, the refuted overfit/holonomic/OEIS searches, and the d=2==A007902 sourced identification with falsifier terms. |
| `TASKS.md` | Checklist of concrete steps toward the current goal; currently holds one unfilled step ("record the first concrete step"). |
| `brute.py` | Pure exact-BFS verification oracle for PE763 D(N): naive frozenset level-by-level BFS using lib.amoeba.forward_level, printing D(N), elapsed time and frontier size each level until a frontier cap (5e6) or time budget (500s) hits; asserts the worked examples D(2)=3, D(10)=44499; compares D(0..Nmax) to the known reference list; and gives a timing/state-count estimate of why D(20) is out of reach. Correctness: reproduces D(2)=3 and D(10)=44499 in-run (asserted), same naive semantics as code/brute.py. |
| `problem.md` | The Project Euler 763 problem statement (converted from HTML): amoeba division rule, definition of D(N), the four worked examples, and the target D(10000) last-nine-digits. |
