# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method policy for the whole run: how to reason (compute before prose), evidence rules (every number from a run, every theorem cited), housekeeping conventions |
| `README.md` | Overview of the workspace and its entry points (AGENTS.md, prompts/, goal.md, tasks.md, scratchpad.md, memory.md) |
| `CONTEXT.md` | Shared-context brief written by the research team and read by every role: what the reference library under research/ means for this problem (established results usable as known, contradictions, and the open gaps). Kept short so each new attempt can act on it without opening the sources. Complements research/INDEX.md, which only says what each file is. |
| `GOAL.md` | Objective: compute Q(10^6) mod (10^9+7); statement, worked examples (Q(2)=5, Q(3)=88, Q(6)=133103808, Q(10) about 468421536), completion criteria, current status |
| `MEMORY.md` | Working memory: problem restatement, verified Q(n) table (n=2..8) with both methods' timings, established results, failed approaches (none), open questions (the n=10^6 method) |
| `problem.md` | The problem statement (source of the run): defines Q(n), rank, pi^i; gives worked examples; asks for Q(10^6) mod (10^9+7) |
| `SCRATCHPAD.md` | Provisional work: the task, method-1 cost model, method-2 justification, power-semantics check, verified results table |
| `TASKS.md` | Task list with checkboxes: recording objective, reading the statement, writing brute.py/brute2.py, verifying n=2..6/7/8, and the (pending) efficient method |
