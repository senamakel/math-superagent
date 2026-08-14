# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `fmax.py` | Exact f(n) oracle on the hypercube: decision_ilp(n,d) (binary scipy.milp/HiGHS, polynomial-size ILP) and exhaustive decision_oracle(n,d) (n<=4) as its validator; f_milp(n) and f_exact(n) return smallest feasible d. Exact integer arithmetic; the ILP/oracle agreement on n<=4 is the correctness check. |
| `huang.py` | Signed adjacency matrices A_n of the hypercube (Huang): huang_matrix(n) returns exact sympy Integer Matrix with A_n^2=n*I; huang_matrix_np(n) returns numpy float array. Verified A_n^2==n*I, zero diagonal, support==edges(Q_n) for n=1..8; spectrum +-sqrt(n) mult 2^{n-1} each (exact n<=7, numeric n<=10). |
| `qcube.py` | Hypercube combinatorial helpers: popcount, is_edge(u,v) (differ in exactly one bit), internal_degree_distribution(n,S) -> {degree:count}, max_internal_degree(n,S). Exact integer; agrees with code/brute.py oracle on n<=4. |
