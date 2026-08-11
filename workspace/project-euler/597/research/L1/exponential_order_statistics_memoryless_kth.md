# Summary — Exponential order statistics and the memoryless property

Source: Timo Koski, "Order Statistics for Independent Exponential Variables",
KTH SF2955 course notes. URL:
https://www.math.kth.se/matstat/gru/sf2955/exponorderstats.pdf
Full proof: `research/L0/exponential_order_statistics_memoryless_kth.full.md`.

## Statement

For X_1..X_n iid with density f, the order statistics X_(1)<…<X_(n) have joint
density n!·∏f(y_k) on the ordered region.

Specializing to Exp(1) (Theorem 2.1): the spacings

    Y_1 = X_(1),   Y_i = X_(i) − X_(i−1)  (i=2..n)

are **independent** exponentials with rates n, n−1, …, 1 respectively
(Y_i ∈ Exp(1/(n+1−i))). Proven by the change of variables Y=AX (A triangular,
det A = 1): f factors as ∏ (n+1−i)·e^{−(n+1−i)y_i}, a product of independent
exp densities.

## Why it governs this problem

The boat speeds v_j are iid Exp(1). This structure is the exact (non-MC,
non-enumerative) integration route: after conditioning on the smallest of a set
of independent exponentials, the rest stay independent exponentials at their
original rates (memoryless). So an event-by-event (bump vs finish) chronology
decomposes into products over independent exponential rates rather than
high-dimensional integrals. Cost grows with the number of boats' structure
(n=13), not with any enumerable bound.

See also [[competing_exponential_clocks_uchicago]] (P(fires first)=λ_j/Σλ and
the product-of-rate-ratios form it yields).
