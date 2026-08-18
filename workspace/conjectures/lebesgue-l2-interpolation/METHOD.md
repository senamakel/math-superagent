Solve by approximation theory and exact rational computation. The objective is a
rational function of the nodes — `sum_k l_k(x)^2` is a degree-`2n-2` polynomial
and its integral over `[-1,1]` is exact — so every value in this run should be
a rational number or a certified interval, never a quadrature estimate.

The oracle for this problem is an exact evaluator of `I` for a given node vector
together with an exact solver for the critical-point system `dI/dx_k = 0`, via
Groebner bases or resultants for small `n` and certified global optimisation
past that. The deliverable of the oracle is a table: for each `n`, the exact
`min I`, its minimiser, and `n*(2 - min I)` — the column the conjecture is a
statement about.

Reformulate before optimising: `I` is the trace of the Gram matrix of the
Lagrange basis in `L^2([-1,1])`, and `integral l_k` is the interpolatory
quadrature weight. Linear algebra on that matrix is more likely to produce a
lower bound than any pointwise estimate, because the open half of this problem
is a lower bound over *all* node systems and no single test function reaches it.

Use symbolic_math (sympy, PARI, Singular) for the polynomial systems and the
exact integration, coder for the optimisation and the table, pattern_finder on
the sequence of exact minimisers. Szabados' disproof of Erdős's own first guess
is the standing falsifier: any lemma implying the Legendre-integral nodes are
optimal is refuted at `n = 4`.
