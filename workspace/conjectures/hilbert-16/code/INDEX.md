# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle: exact count of limit cycles for radially symmetric polynomial fields (displacement function sign = roots of A(u), u=r²). Reproduces all worked examples: cubic→1 (r=1), linear centre→0, linear expanding focus→0, two-cycle A=(1−u)(2−u)→2, semi-stable A=(1−u)²(2−u)→1 (u=1 double root excluded). Non-radial fields refused honestly. Exact rational arithmetic, Sturm counts; avoids float/integration/sampling. Runs as `python code/brute.py`. |
| `sk_ceil_structure.py` | Exact-arithmetic verifier for the ceil(S_k) sequence: fractional-part periodicity mod 3 (k>=2), delta period 3, order-6 minimal annihilator check over k=2..199, sympy order-5/order-6 elimination; input: none, prints claims A-E. |
| `sk_crosscheck.py` | _(undescribed)_ |
| `sk_integerity.py` | Verifies by exact arithmetic (k=1..400) that S_k is integer iff 3 |
| `sk_recurrence.py` | _(undescribed)_ |
| `sk_sequence.py` | Computes exact S_k = 4^{k-1}(k-13/6)+(2k-1)/3 (Christopher-Lloyd/Li lower bound on H(2k-1)) and the guaranteed-count sequence. |
| `sk_solve_recurrence.py` | Solves and verifies constant-coefficient order-4 recurrences for S_k ((E-4)^2(E-1)^2) and S_{3j} ((E-64)^2(E-1)^2) by exact Gaussian elimination. |
| `sk_structure.py` | _(undescribed)_ |
| `sk_subseq_recurrence.py` | _(undescribed)_ |
