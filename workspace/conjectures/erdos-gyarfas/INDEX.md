# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace-wide working instructions: the method policy (compute before writing prose, brute force only on small instances as oracle, never search the answer space, attack your own method, state complexity before running, distinguish proof from numerical evidence), the evidence rules (every number from a program, every theorem from a source), where things live, and the housekeeping rules for generated files, GOAL/SCRATCHPAD/MEMORY, and code/. Static guidance for every agent; describes the tree and the rules, not mathematics. |
| `CONTEXT.md` | _(undescribed)_ |
| `GOAL.md` | The run's objective: attack the Erdős–Gyárfás conjecture (every finite simple graph with min degree >=3 has a 2-power cycle). States the committed method (structural graph theory on a minimal counterexample, with computation/SAT/Lean serving the argument), and the completion criteria: research/ROOT.md, MEMORY.md of established structural facts, at least one new stated-and-attacked statement, a Lean formalisation, and an honest final report. |
| `MEMORY.md` | _(undescribed)_ |
| `README.md` | Welcome note for the workspace: how to start (AGENTS.md, prompts/, GOAL.md, TASKS.md, SCRATCHPAD.md, MEMORY.md) and the reproducibility rule. Static boilerplate. |
| `SCRATCHPAD.md` | Temporary calculations and observations. Current note: pattern-finder check found no computed integer sequences on disk yet. |
| `TASKS.md` | _(undescribed)_ |
| `problem.md` | The problem statement: the Erdős–Gyárfás conjecture and exactly what it does and does not say (minimum degree, not average/connectivity; k>=2 so lengths 4,8,16,...; any cycle, not necessarily induced; finite and simple). States the obstruction any approach must beat (powers of two are sparse, interval results need b>=2a) and lists the literature leads to verify. Working document for the run's targets. |
