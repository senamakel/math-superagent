# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive obviously-correct exhaustive oracle for f(n)=min over S of size 2^{n-1}+1 of max internal degree on Q_n. Functions: internal_degree_distribution(n,S) -> {deg:count}, max_internal_degree(n,S), f_exact(n) by exhaustive subset enumeration (n<=4 only), even_weight_set(n). Verified: matches statement's worked example (even-weight set size 2^{n-1}, D=0); f(1)=1,f(2)=2 hand-checked; f(3)=2,f(4)=2 exhaustive. This is the oracle the fast/solver methods are checked against. |
| `f_exact_spectral_check.py` | Independent exact checker for f(n) with a Huang spectral cross-check. Brute-forces all size-(2^{n-1}+1) subsets for n=1..4 (exhaustive, exact ints), reporting f(n) and one achieving set with full degree profiles; builds the signed adjacency A_n (A_n^2 = n·I, spectrum ±sqrt(n)) and for every admissible S checks λ_max(A_n[S,S]) between sqrt(n) and D(S); reproduces the even-weight-set worked example (independent, |
| `spectral_verify.py` | Mechanical verification of Huang's spectral chain: exact A_n^2==n*I + support (n=1..8, sympy), spectrum +-sqrt(n) (n=2..10), interlacing lambda_max(B[A_n[S,S]]) >= sqrt(n) for random |
| `verify_huang_signing.py` | Directly computes Huang's recursive signed adjacency matrix for Q_n (n up to 9) and checks A_n^2 = n I, {0,±1} entries on cube edges, and eigenvalues ±sqrt(n). Establishes the construction's correctness numerically. |
