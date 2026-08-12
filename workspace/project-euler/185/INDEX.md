# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and evidence rules all agents follow: compute before prose, exact arithmetic, no exponential search, brute force as oracle only, source citations for theorems. |
| `CONTEXT.md` | Working state / task guidance context for the run. |
| `GOAL.md` | Current objective and completion criteria: solve Project Euler 185 (unique 16-digit secret sequence). Holds the full problem statement, the L=5 worked-example oracle (answer 39542), the L=16 guesses, and the four completion criteria (brute.py, solution.py, solution2.py, final verification). |
| `MEMORY.md` | Durable run memory: problem restatement, the governing constraint-satisfaction approach (backtracking with pruning, ILP reformulation), and open questions/failed approaches. Belongs to the solver loop. |
| `README.md` | Entry-point orientation to the workspace: how the directory is organised, where to start (AGENTS.md, prompts/), and where outputs land (code/out/). |
| `SCRATCHPAD.md` | Provisional working notes not yet established enough for MEMORY.md. Pattern-finder notes conclude neither the PE 185 constraint data (counts, columns, row/column sums) nor the L=16 secret's digits carry exploitable integer-sequence structure (no recurrences, no polynomials, no OEIS entry); a tool_builder note records the MILP route (solution2.py) that produced and verified the L=16 secret 4640261571849533, and code/lib/pe185secret.py derives its sequences. |
| `TASKS.md` | Task checklist tracking progress toward the goal. Stub template at present. |
| `problem.md` | Official Project Euler 185 (Number Mind) statement, converted from projecteuler.net/minimal=185. The canonical statement this run solves. |
