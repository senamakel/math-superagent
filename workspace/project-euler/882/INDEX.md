# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and housekeeping rules for every agent. |
| `README.md` | Standard project boilerplate: how to use AGENTS.md, prompts/, goal/tasks/scratchpad/memory. |
| `problem.html` | The problem statement: partisan bit-deletion game, definition of S(n), given values S(2)=2, S(5)=17, S(10)=64, ask for S(10^5). |
| `problem.url` | Source URL: https://projecteuler.net/minimal=882 — Project Euler 882, from which problem.html was converted. |
| `config.toml` | Workspace/tooling config: kind "mathematical-research", solver flags (exact arithmetic, forbid exponential, etc.), artifact file names. |
| `goal.md` | The objective and completion criteria: build and validate TASK A (real-game brute) and TASK B (counting-game (A,B) DP). |
| `tasks.md` | Task checklist (single placeholder task row). |
| `memory.md` | Working memory: problem restatement, given values, established results (to fill), failed approaches, open questions. |
| `scratchpad.md` | Scratchpad for provisional calculations not yet ready for memory.md. |
| `brute.py` | TASK A: naive minimax on the REAL game (multiset state, whose turn, skip budget). Prints S(n) for n=1..8 and verifies n=1..3 against an explicit move-search. |
| `counting.py` | TASK B: the same minimax DP on the reduced counting game (A,B) where A=total 1-bits, B=total 0-bits; One-move (A-1,B), Zero-move (A,B-1), skip passes. Verifies S(2)=2, S(5)=17, S(10)=64; prints S(n) n=1..10 and the need_oneturn/need_zeroturn grids for A,B in 0..12. |
| `compare.py` | Cross-check: real-game S(n) (brute.py, n=1..8) vs counting-game S(n) (counting.py) for n=1..8; prints match/mismatch per row. |
| `prompts/` | Role-specific guidance files for each agent role (organizer, scholar, tool_builder, etc.); 10 files, indexed in `prompts/INDEX.md`. |
| `reflections/` | Archived per-attempt verdicts; written by the solution loop itself, do not hand-edit. |
| `research/` | Externally sourced material: 8 Wikipedia excerpts plus 6 full-text companions on combinatorial game theory, partisan games, surreal numbers, zugzwang, and related topics; indexed in `research/INDEX.md`. |
| `toolkits/` | Reusable one-function-per-file helpers (no function files yet). |
