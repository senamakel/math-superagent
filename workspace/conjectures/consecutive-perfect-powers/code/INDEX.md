# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive exact-integer oracle for x^p - y^q = 1. solutions(N) returns every (x,p,y,q) with x^p,y^q<=N and x^p-y^q=1 by enumerating the set of perfect powers and checking consecutive values. Pure int arithmetic (no floats/logs/math.pow). Verified correct by (a) matching the worked example (3,2,2,3) for every N in {9,100,1000,1e4,1e5,1e6}, and (b) agreeing with an independent direct pairwise enumerator for N in {9,100,1000}. Intended to underpin every claimed lemma with an exact small-case check. |
| `verify_foundations.py` | Exact-integer oracle/verification foundation: perfect_powers_upto(N), solutions(N) (=={(3,2,2,3)} up to 10^8), exp2_xq_solutions, exp2_yp_solutions, prime_reduction_cases (identity check), double_wieferich_stats. Established correct: solutions(N) matches pre-existing scholar oracle brute output; exp2 cases = oracle on x-side/y-side exponent parity; double-Wieferich conditioning validated against (83,4871); output in code/out/verify_foundations.captured.txt. |
