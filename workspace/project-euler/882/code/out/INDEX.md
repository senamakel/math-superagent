# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_time.txt` | Failed timing capture: /usr/bin/time not found in the environment. No timing data; harmless record of the environment's lack of GNU time. |
| `brute_examples.txt` | Record of which worked examples from problem 882 the real-game oracle reproduced: S(2)=2 and S(5)=17 matched, S(10) unreachable by enumeration (timed out). |
| `brute_out.txt` | TASK A output: real-game naive minimax S(n) for n=1..5 plus explicit-move verification for n=2,3; files real-game values S(2)=2, S(3)=8, S(4)=9, S(5)=17. |
| `counting_proper.txt` | Output of counting_proper.py: exact O(A,B) tables to N=2000 and S_counting(n)=max(0,A(n)-B(n)) for n=1..30 vs real-game oracle. Records the refuted single-aggregate (A,B) surrogate. |
| `fastbrute_out.txt` | TASK A (optimized) output: real-game minimax with the budget dimension removed; S(n) for n=1..3 and memo/state counts, same S values as brute.py. |
| `fastbrute_realtime.txt` | Another capture of fastbrute.py (TASK A optimized) output, byte-identical to fastbrute_out.txt/fastbrute_run.txt/my_fastbrute.txt — same run, another capture name. Read fastbrute_out.txt: S(1)=1, S(2)=2, S(3)=8 with memo/state counts. |
| `fastbrute_run.txt` | Output of fastbrute.py (TASK A optimized, budget dimension removed): S(n)=1,2,8 for n=1..3 with memo/state counts; same S values as brute.py. NOTE: byte-identical duplicate of fastbrute_out.txt (same run, two captures); read fastbrute_out.txt. |
| `my_fastbrute.txt` | Third capture of fastbrute.py output (TASK A optimized), byte-identical to fastbrute_out.txt/fastbrute_run.txt — same run, another capture name. Read fastbrute_out.txt. |
brute_out.txt. |
| `my_fastbrute.txt` | Third capture of fastbrute.py output (TASK A optimized), byte-identical to fastbrute_out.txt/fastbrute_run.txt — same run, another capture name. Read fastbrute_out.txt. |
