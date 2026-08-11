# Fold: order of a random permutation (the n!/ord weights)

The `n!/ord(π)` weight in brute2 is governed by the distribution of ord(π). Law: log ord(π) is asymptotically normal, mean (log 2)n/2, variance (log 3)n/3 (Erdős–Turán); but the *average* order µ_n is dominated by rare high-order permutations, log µ_n = C√(n/log n)·(1+o(1)), C≈2.99047 (Goh–Schmutz; refined by Stong with explicit error). This bounds how large n!/ord(π) can be and maps the order literature.

- [[stong_average_order_permutation]] (Stong, EJC 5 R41, 1998): log µ_n = C√(n/log n) + O(√n loglog n / log n). L0 `stong_average_order_permutation.full.md` (+ `.pdf.full.md` stub).

<!-- brief -->
Established: order-of-random-permutation law (Erdős–Turán normal for log ord; µ_n ~ exp(C√(n/log n))). Relevant to the n!/ord(π) weights in the period-mean, not directly to A_n,B_n.
