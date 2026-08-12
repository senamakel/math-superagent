# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and evidence rules all agents follow: compute before prose, exact arithmetic, no exponential search, brute force as oracle only, source citations for theorems. |
| `CONTEXT.md` | Working state / task guidance context for the run. |
| `GOAL.md` | Current objective and observable completion criteria for the run. Presently a stub for the solver to fill in; the goal is solving Project Euler 185 (unique 16-digit secret sequence). |
| `MEMORY.md` | Durable run memory: problem restatement, established results, failed approaches, open questions. Stub template at present; belongs to the solver loop. |
| `README.md` | Entry-point orientation to the workspace: how the directory is organised, where to start (AGENTS.md, prompts/), and where outputs land (code/out/). |
| `SCRATCHPAD.md` | Provisional working notes not yet established enough for MEMORY.md. Currently holds one pattern_finder note: PE 185 is a constraint-satisfaction problem with no integer sequence to analyze, so pattern-matching should wait until a solver produces output. |
| `TASKS.md` | Task checklist tracking progress toward the goal. Stub template at present. |
| `problem.md` | Official Project Euler 185 (Number Mind) statement, converted from projecteuler.net/minimal=185. The canonical statement this run solves. |
