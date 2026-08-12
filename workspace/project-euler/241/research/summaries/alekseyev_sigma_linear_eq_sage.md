# Alekseyev sigma_linear_eq.sage — the runnable solver for aσ(n)=bn+c

**Source:** `https://raw.githubusercontent.com/maxale/multiplicative_functions/main/sigma_linear_eq.sage`
— `[[alekseyev_sigma_linear_eq_sage.full]]`.

## What it is

The SageMath implementation of Alekseyev's paper (arXiv:2601.17832), function
`res_solve_sigma_abc(a, b, c, U)` — solves aσ(n)=bn+c for all n ≤ U. Uses the RES
(recursively enumerated set) framework, prime-wheel pruning, shortcuts, and the
`reduce_abc` configuration reduction (cancels gcd of coefficients; handles g=gcd(a′,c′)
forced factors; recognises a′=b′=c′ infinite series).

The `sigma_over_n_bound.sage` dependency uses the Robin bound σ(n)/n ≤ n/φ(n) to prune.
Implements Theorem 3.2's wheel and §3.1 shortcuts; optional constraints: squarefree,
even_only, coprime_to, omega/bigomega bounds, fixed tau(n), and `refs` to OEIS core
equations.

## What it means for PE 241

This is a *runnable, complete* reference solver for the exact general equation family
the run's DFS is the specialised c=0 instance of. It is **not** run in this environment
(no shell), and it would solve 2σ(n)=(2k+1)n (a=2, b=odd, c=0) directly. It corroborates
(1) that the DFS parameters the run uses are implementable and complete, and (2) the
method's cost in the visited-tree not the bound. It does not provide the 22 values or sum
itself. If the run's own DFS cannot be executed, this is the alternative complete route —
but it needs SageMath, also absent. Keep as the canonical code reference; not load-bearing.

No separate claim — covered by `alekseyev-tree-search-complete`. Do not re-read for the
solver.
