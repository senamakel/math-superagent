# Index — code/matveev

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_matveev_23.py` | Executed obstruction check: the prime-factor log-ratio route of research/approaches/matveev-explicit-2-3.md is vacuous on C(x,2)=C(y,3) (Lambda identically zero at every solution; Matveev Thm 2.2 needs Lambda!=0). Computes real Matveev constants for the nonzero difference forms C(x,2)=C(y,3)+d (d in {-2,-1,1,3}), giving explicit y-bounds with log10 y max ~ 2.9e10 .. 3.4e27 — an effective-but-astronomically-large constant, i.e. the effective-vs-usable gap made concrete. Oracle over y<=10^6 recovers exactly the Avanesov/SDW complete solution set. Correctness: exact integer arithmetic, Kummer condition verified exactly, n>=2 hypothesis of Thm 2.2 checked against the held source; EXIT_CODE=0, ALL CHECKS PASSED (code/out/check_matveev_23.captured.txt). |
