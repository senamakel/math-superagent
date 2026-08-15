# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `fmax.py` | Exact f(n) oracle for the hypercube: exhaustive decision_oracle(n,d) (n<=4) and ILP decision_ilp(n,d) via scipy.optimize.milp (HiGHS). decision_ilp linearises "D(S)<=d" with binaries x_v, sum x=2^{n-1}+1, and per-vertex neighbour-sum + M*x_v <= d+M (M=n). f_milp/f_exact find the smallest feasible d. Validated: decision_ilp agrees with decision_oracle on all (n,d) with n=1..4 (13 cases); f-exact values confirmed f(1..4)=(1,2,2,2). |
| `huang.py` | Signed adjacency matrices A_n of the hypercube (Huang): huang_matrix(n) returns exact sympy Integer Matrix with A_n^2=n*I; huang_matrix_np(n) returns numpy float array. Verified A_n^2==n*I, zero diagonal, support==edges(Q_n) for n=1..8; spectrum +-sqrt(n) mult 2^{n-1} each (exact n<=7, numeric n<=10). |
| `qcube.py` | Hypercube combinatorial helpers: popcount, is_edge(u,v) (differ in exactly one bit), internal_degree_distribution(n,S) -> {degree:count}, max_internal_degree(n,S). Exact integer; agrees with code/brute.py oracle on n<=4. |
