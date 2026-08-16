# Index — code/fold_rank

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `rank_of_fold.py` | Decisively settles the fold-matrix rank/nullity contradiction for SUPPLY. Computes the operative (n-2) x n fold matrix Phi_n (rows d=2..n-1, entry Phi[d,j]=1 iff j-(n-1-d) is a bitwise submask of d) for n=2..20 over F2: full row rank n-2, nullity 2, kernel exactly span(even-alt, odd-alt) with all-ones = even XOR odd, and every row-range convention's rank (d=0..n-1 -> n, d=1..n-1 -> n-1, d=2..n-1 -> n-2) showing 'rank n-3' fits none. Cross-checked: wt(Phi_n h) by matrix image == nu2 by t_direct oracle for n=3..10, 5 random h each. This corrects inherited problem.md fact 3 ('rank=n-3, nullity 1, ker=span(all-ones)'), which is internally inconsistent for an n-column matrix. Verified by exact F2 Gaussian elimination, runs clean. |
| `verify_alln_theorems.py` | Verifies the two all-n structural theorems (rank n-2, kernel = span(even-alt,odd-alt)) by exact F2 elimination n=2..40 and exhaustive 2^n enumeration n=2..9, plus canonical oracle values. Capture: code/out/fold_alln_theorems.captured.txt. |
