# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `report_rank_powers.md` | Summary of cited facts (Lehmer/factorial-rank identity, ord=lcm of cycle lengths, Σ rank = n!(n!+1)/2) plus the derived reduction Q(n)=Σ_{H cyclic} φ( |
| `verify_facts.py` | Brute-force oracle for the rank/powers problem: Lehmer `rank0`/`r1`, `apply_power`, `order`, `Q(n)` literal, plus checks Σ rank = n!(n!+1)/2 and rank(2,1,3)=3, Q(2)=5, Q(3)=88. Written but NOT run in its original environment; its n=2,3 checks were reproduced by hand (see the report). Use to validate solution.py once a code executor exists. |
