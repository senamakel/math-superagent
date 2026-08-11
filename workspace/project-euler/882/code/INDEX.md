# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | How to work in code/: every program lives here, all output in code/out/, one job per file, the naive program is the oracle and stays, exact arithmetic, never delete a program carrying a result. |
| `brute.py` | TASK A: naive minimax on the REAL game (multiset state, whose turn, skip budget). Prints S(n) for n=1..8 and verifies n=1..3 against an explicit move-search. |
| `compare.py` | Cross-check: real-game S(n) (brute.py, n=1..8) vs counting-game S(n) (counting.py) for n=1..8; prints match/mismatch per row. |
| `counting.py` | TASK B: the same minimax DP on the reduced counting game (A,B) where A=total 1-bits, B=total 0-bits; One-move (A-1,B), Zero-move (A,B-1), skip passes. Verifies S(2)=2, S(5)=17, S(10)=64; prints S(n) n=1..10 and the need_oneturn/need_zeroturn grids for A,B in 0..12. |
| `fastbrute.py` | TASK A (optimized): real-game minimax taking the same game semantics as brute.py but removing the skip-budget dimension — the memoized value f(state,turn) is the minimal skips Zero needs (unlimited budget), so S(n) = f(init, One) with one memo over (state,turn) instead of S(n) separate memo runs. Oracle agreement with brute.py is asserted for S(1..8). |
| `scratch_run2.py` | Scratch harness: imports counting.py's DP (up to `def main`) and prints S(n) for n=1..10 via need_oneturn with the (A,B) totals — a quick re-run of the TASK-B table outside counting.py's main. Scratch; superseded by counting.py itself. |
| `scratchpad_td.py` | Superseded scratch verification harness: the Trollope–Delange checklist it encoded was moved to research/verify_trollopedelange.md for tool_builder to execute. Kept only as a record; no numerical claims from Girgensohn (2011) were confirmed by a run. |

`out/` holds everything a program produces (see code/AGENTS.md). Contents:

| File | Purpose |
| --- | --- |
| `out/brute_out.txt` | Captured stdout from a brute.py run: real-game S(1..5) via memoized minimax, n=1..3 verified against the explicit move-search (all match). Capture is TRUNCATED — S(6..8) and the state counts beyond n=5 are not in this file; re-run brute.py for the full table. Result file, not source. |
