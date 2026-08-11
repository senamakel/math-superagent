# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_time.txt` | Failed timing capture: /usr/bin/time not found in the environment. No timing data; harmless record of the environment's lack of GNU time. |
| `brute_examples.txt` | Record of which worked examples from problem 882 the real-game oracle reproduced: S(2)=2 and S(5)=17 matched, S(10) unreachable by enumeration (timed out). |
| `brute_out.txt` | EMPTY (0 bytes) capture of code/brute.py output — no content survived. The real-game S values S(1..5)=1,2,8,9,17 live in brute_run.txt; read that instead. |
| `brute_realtime.txt` | EMPTY (0 bytes) capture of code/brute.py output (a second named realtime capture, alongside brute_out.txt). No content survived in either empty capture. The real-game S values S(1..5)=1,2,8,9,17 live in brute_run.txt; read that instead. Avoid re-capturing with this name. |
| `brute_realtime2.txt` | Run capture of the real-game budgeted minimax (S(n) for n=1..8 row): explicit-move check n=2 gives S(2)=2, n=1..3 explicit==memo (S=1,2,8), then S(1..5)=1,2,8,9,17 with memoized-state counts. Redundant with brute_run.txt (same values); read brute_run.txt as the canonical TASK-A oracle record. |
| `brute_run.txt` | Run capture of code/brute.py (TASK A real-game naive minimax): explicit-move verification n=1..3 all match the memoized values (S=1,2,8), then real-game S(n) for n=1..5 = 1,2,8,9,17 with per-n memoized-state counts (3,21,184,3270,83052). This reproduces the worked examples S(2)=2 and S(5)=17; it is the record of the real-game oracle values (brute_out.txt is empty — read this file instead). |
| `counting_proper.txt` | Output of counting_proper.py: exact O(A,B) tables to N=2000 and S_counting(n)=max(0,A(n)-B(n)) for n=1..30 vs real-game oracle. Records the refuted single-aggregate (A,B) surrogate. |
| `counting_run.txt` | Run capture of code/counting.py (TASK B counting-game (A,B) DP): need_oneturn/need_zeroturn grids over A,B in 0..12 all '.' (unable to force a win) and S(n)=inf for n=1..10 — MISMATCH with the expected worked examples (2,17,64). Records a failing execution of this counting DP; important negative record, read alongside code/counting.py's intended verification. |
| `fastbrute_out.txt` | TASK A (optimized) output: real-game minimax with the budget dimension removed; S(n) for n=1..3 and memo/state counts, same S values as brute.py. |
| `fastbrute_realtime.txt` | Another capture of fastbrute.py (TASK A optimized) output, byte-identical to fastbrute_out.txt/fastbrute_run.txt/my_fastbrute.txt — same run, another capture name. Read fastbrute_out.txt: S(1)=1, S(2)=2, S(3)=8 with memo/state counts. |
| `fastbrute_run.txt` | Output of fastbrute.py (TASK A optimized, budget dimension removed): S(n)=1,2,8 for n=1..3 with memo/state counts; same S values as brute.py. NOTE: byte-identical duplicate of fastbrute_out.txt (same run, two captures); read fastbrute_out.txt. |
| `my_fastbrute.txt` | Third capture of fastbrute.py output (TASK A optimized), byte-identical to fastbrute_out.txt/fastbrute_run.txt — same run, another capture name. Read fastbrute_out.txt. |
| `oracle_S.txt` | Canonical record of the REAL-game minimax oracle for Project Euler 882: S(n) = 1,2,8,9,17 for n=1..5 (n=6+ unreachable within the time budget; only S(6)>18 established). Matches statement examples S(2)=2, S(5)=17, plus S(1)=1,S(3)=8; n=1..3 verified by fully explicit independent search in code/brute.py. Produced by code/brute.py, confirmed by code/fastbrute.py for n=1..3. |
