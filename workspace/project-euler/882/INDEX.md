# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace method and housekeeping rules for every agent. |
| `README.md` | Standard project boilerplate: how to use AGENTS.md, prompts/, goal/tasks/scratchpad/memory. |
| `brute.py` | TASK A: naive minimax on the REAL game (multiset state, whose turn, skip budget). Prints S(n) for n=1..8 and verifies n=1..3 against an explicit move-search. |
| `compare.py` | Cross-check: real-game S(n) (brute.py, n=1..8) vs counting-game S(n) (counting.py) for n=1..8; prints match/mismatch per row. |
| `config.toml` | Workspace/tooling config: kind "mathematical-research", solver flags (exact arithmetic, forbid exponential, etc.), artifact file names. |
| `context.md` | Records what the reference library now establishes beyond its prior state: O(log n) computation of A(n),B(n) via OEIS A000788/A059015 for the (A,B) counting game at n=10^5. |
| `counting.py` | TASK B: the same minimax DP on the reduced counting game (A,B) where A=total 1-bits, B=total 0-bits; One-move (A-1,B), Zero-move (A,B-1), skip passes. Verifies S(2)=2, S(5)=17, S(10)=64; prints S(n) n=1..10 and the need_oneturn/need_zeroturn grids for A,B in 0..12. |
| `goal.md` | The objective and completion criteria: build and validate TASK A (real-game brute) and TASK B (counting-game (A,B) DP). |
| `memory.md` | Working memory: problem restatement, given values, established results (to fill), failed approaches, open questions. |
| `problem.html` | The problem statement: partisan bit-deletion game, definition of S(n), given values S(2)=2, S(5)=17, S(10)=64, ask for S(10^5). |
| `problem.url` | Source URL: https://projecteuler.net/minimal=882 — Project Euler 882, from which problem.html was converted. |
| `scratchpad.md` | Scratchpad for provisional calculations not yet ready for memory.md. |
| `scratchpad_td.py` | Provisional numeric verification of Trollope-Delange identities: S(2n)=2S(n)+n, S(n+p(n)) and S(n+2p(n)) recurrences, S(2^e)=e·2^(e-1), formula 35 reconstruction, and the ones/zeros total-bits cross-check. Scratch; superseded if tool_builder runs it and confirms. |
| `tasks.md` | Task checklist (single placeholder task row). |
