# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `PARALLEL.md` | _(undescribed)_ |
| `binom_multiplicity.py` | Exact inversion oracle for Singmaster: canonical_reps(a,n_max), multiplicity(a,n_max), nontrivial_reps(a,n_max). Counts both mirrors and the trivial pair. Verified: 3003->8, the six N=6 witnesses ->6, j=2 Pell member (61218182743304701891431482520)->6, all cross-checked against the direct brute oracle code/brute.py. |
| `matveev.py` | Matveev 2000 (Izv. Math. 62:4, 723-772) explicit lower bounds for homogeneous rational linear forms in logarithms, specialized to K=Q (D=1, rho=1, C3=n). Provides: binomial_reduction_identity() (symbolic check 6C(x,2)-6C(y,3) == 3x(x-1)-y(y-1)(y-2)), two_sided_products(x,y) (P=3x(x-1), Q=y(y-1)(y-2) + factorizations), linear_form(factP,factQ) (nonzero b_j = v_p(P)-v_p(Q), Lambda = sum b_j ln p_j, exact 0 iff P==Q), kummer_subset_verification(primes) (Kummer condition (1.5) for distinct primes: [Q(sqrt p_j):Q]=2^n, polynomial + small-n subset oracle), matveev_constants(primes,bs,theta,E) (Thm 2.2 constants C1,C2 (2.4), Omega, omega (2.5), C0' (2.15), B (2.14), exponent (2.16); also Thm 2.3(ii) theta=1/(2-2/(n e^{n+1}))). Correctness: independent transcription code/matveev_verify_paper_formula.py agrees to relerr 0 in all 8 constants for n=3,4 forms both theta regimes; hand-check of a=120/n=3 values; captures in code/out/matveev_2_3_constant.captured.txt and code/out/matveev_paper_formula_verify.captured.txt. |
| `parallel.py` | _(undescribed)_ |
