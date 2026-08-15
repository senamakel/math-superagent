# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `SCRATCH_CLEANUP.md` | Records that scratch test scripts (grounding_shifting_test, run_grounding, tmp_run*) were removed because the grounding conclusions rest on pure reasoning verified by hand at n=2, not on those scripts. |
| `brute.py` | Naive obviously-correct exhaustive oracle for f(n)=min over S of size 2^{n-1}+1 of max internal degree on Q_n. Functions: internal_degree_distribution(n,S) -> {deg:count}, max_internal_degree(n,S), f_exact(n) by exhaustive subset enumeration (n<=4 only), even_weight_set(n). Verified: matches statement's worked example (even-weight set size 2^{n-1}, D=0); f(1)=1,f(2)=2 hand-checked; f(3)=2,f(4)=2 exhaustive. This is the oracle the fast/solver methods are checked against. |
| `f_exact_spectral_check.py` | Independent exact checker for f(n) with a Huang spectral cross-check. Brute-forces all size-(2^{n-1}+1) subsets for n=1..4 (exhaustive, exact ints), reporting f(n) and one achieving set with full degree profiles; builds the signed adjacency A_n (A_n^2 = n·I, spectrum ±sqrt(n)) and for every admissible S checks λ_max(A_n[S,S]) between sqrt(n) and D(S); reproduces the even-weight-set worked example (independent, |
| `grounding_shifting_test.py` | _(undescribed)_ |
| `run_grounding.sh` | _(undescribed)_ |
| `spectral_verify.py` | Mechanical verification of Huang's spectral chain: exact A_n^2==n*I + support (n=1..8, sympy), spectrum +-sqrt(n) (n=2..10), interlacing lambda_max(B[A_n[S,S]]) >= sqrt(n) for random |
| `tmp_run.py` | _(undescribed)_ |
| `tmp_run2.py` | _(undescribed)_ |
| `tmp_run_oeis.py` | _(undescribed)_ |
| `verify_harper_edgemini.py` | Brute-force verification of Harper's 1964 cube edge-isoperimetric theorem (claim harper-optimal-assignments-1964): for each m, checks that the binary-order initial segment attains the minimum edge boundary over all subsets of Q_n, for n=1..4. Written by scholar, NOT yet run (no shell); a runner must execute it before promoting the Harper claim from asserted-by-source to checked. |
| `verify_huang_signing.py` | Directly computes Huang's recursive signed adjacency matrix for Q_n (n up to 9) and checks A_n^2 = n I, {0,±1} entries on cube edges, and eigenvalues ±sqrt(n). Establishes the construction's correctness numerically. |
| `verify_new_sources.py` | Scholar verification of the three new library sources' central claims (Liu-Zhou spectrum, Barber parity-class classification, Ellis subcube edge-isoperimetric extremality) at small n. |
