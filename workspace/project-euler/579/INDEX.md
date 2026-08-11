# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace-wide method and evidence rules (restate the problem, run the small-case oracle first, exact integer arithmetic, no answer-space search, cite sourced claims). |
| `README.md` | Short overview of the problem workspace and its file-map conventions. |
| `config.toml` | Runtime configuration: solver settings (exact arithmetic, cite sources, forbid exponential time/space) and the artifact file paths. |
| `goal.md` | The objective (PE 579) restated, the oracle values, and the 6 completion criteria. All 6 criteria DONE; final answer S(5000) mod 10^9 = 3,805,524 recorded. |
| `memory.md` | Working memory: established results (oracle values, frame method, power-sum), growth data, failed approaches, open questions. |
| `problem.html` | The PE 579 problem statement, converted from the source page. |
| `problem.url` | Source URL (`https://projecteuler.net/minimal=579`), single line. |
| `prompts/` | Role-specific guidance files for each agent (see `prompts/INDEX.md`). |
| `reflections/` | Archived attempt verdicts; written by the solution loop itself (see `reflections/INDEX.md`). |
| `research/` | Externally sourced material: source summaries, full texts, and the run's verification scripts against them (see `research/INDEX.md`). |
| `scratchpad.md` | Temporary calculations not yet promoted to `memory.md`. Currently empty. |
| `tasks.md` | Task checklist. All items DONE, including the final one: full `solution.py` verified and S(5000) mod 10^9 computed (3805524) and checked by an independent route. |
| `toolkit.md` | Documents every `toolkit.py` function (signature, returns, what verified it); kept in step with `toolkit.py`. |
| `toolkits/` | One-function-per-file helper library (currently empty; see `toolkits/INDEX.md`). The working helpers live in root `toolkit.py` instead. |
