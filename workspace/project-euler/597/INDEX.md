# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Method and evidence rules for the whole run: restate the problem, test small cases, prefer theory over enumeration, keep sourced facts separate from deductions, keep files described. |
| `README.md` | Folder-layout note pointing newcomers to AGENTS.md, `prompts/`, and the goal/tasks/scratchpad/memory working files. |
| `config/` | The run's plumbing: `config.toml` (solver configuration: prefer exact arithmetic, verify with code, forbid exponential time/space, and names of the goal/memory/scratchpad/solution artifact files) and `problem.url` (the PE 597 statement URL). |
| `context.md` | Standing brief synthesizing what the `research/` library establishes for this problem (definitions, available results, contradictions, gaps). Written by the research team; a few-hundred-word brief to act on without opening sources. |
| `goal.md` | Restated PE 597 goal with the full setup (every symbol defined), the n=3,L=160 worked probability table, the given p(4,400), the target p(13,1800), and the completion criteria. |
| `memory.md` | Working memory: established results (brute reproduces the table; comparator bug fixed), failed approaches (the w-order-only hypothesis, refuted), and the open question of the exact method. |
| `problem.html` | The downloaded PE 597 statement (Torpids) — the source document this run is solving. |
| `prompts/` | Role-specific agent guidance files; see `prompts/INDEX.md`. |
| `race_spec.md` | Exact chronological race-dynamics specification for implementation: event simulation, bump/OUT/FINISH treatment, and the bump-chain parity definition. Reference contract for any race solver. |
| `reflections/` | Attempt-by-attempt verdicts and lessons; written by the reflection loop (do not hand-edit). |
| `research/` | External sourced-material library; see `research/INDEX.md`. |
| `research_notes/` | The run's own structural explorations of the parity problem; see `research_notes/INDEX.md`. |
| `scratchpad.md` | Provisional work: the diagnosis of the parity-comparator bug, its fix, and the corrected MC run output. |
| `tasks.md` | Task checklist: done items (verify sample, fix comparator, MC re-check) and the open task to solve p(13,1800) exactly. |
| `toolkits/` | One-function-per-file reusable helpers; see `toolkits/INDEX.md`. |
