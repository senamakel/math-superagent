# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive obviously-correct exhaustive oracle for f(n)=min over S of size 2^{n-1}+1 of max internal degree on Q_n. Functions: internal_degree_distribution(n,S) -> {deg:count}, max_internal_degree(n,S), f_exact(n) by exhaustive subset enumeration (n<=4 only), even_weight_set(n). Verified: matches statement's worked example (even-weight set size 2^{n-1}, D=0); f(1)=1,f(2)=2 hand-checked; f(3)=2,f(4)=2 exhaustive. This is the oracle the fast/solver methods are checked against. |
