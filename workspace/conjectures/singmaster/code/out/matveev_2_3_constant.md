# Matveev 2000 Thm 2.2/2.3(ii) explicit constants for the (2,3) curve — computed

```claim
id: matveev-2-3-constants-computed
statement: For the (2,3) triangular=tetrahedral curve C(x,2)=C(y,3), i.e.
  3x(x-1)=y(y-1)(y-2), the exact-solution linear form Lambda = ln P - ln Q
  attached to the two-sided product equality has ALL coefficients zero
  (n_nonzero=0), so Matveev's Theorem 2.2 does not apply to it -- an exact
  equality of prime factorizations is identically zero as a linear form in
  logs.  For nonzero DELTA forms ln(P_a) - ln(Q_b) between DIFFERENT
  solutions (a != b), Theorem 2.2 (K=Q real: D = D_K/kappa = 1, rho =
  rank_R{ln p_j} = 1, C3 = n/rho = n, A_j = h(p_j) = ln p_j) gives the
  explicit lower bound ln|Lambda| > -112*2^n*C2*C0'*D^2*omega*ln(2eB); the
  constants C1, C2, Omega, omega, C0', B were computed exactly here.
hypotheses: K=Q; alpha_j = distinct primes p_j (so A_j = h(p_j) = ln p_j,
  satisfying (2.13) and Theorem 2.3(ii) with A_j = ln alpha_j); Kummer
  condition [Q(sqrt(p_1),...,sqrt(p_n)):Q] = 2^n holds automatically for
  distinct primes and was verified exactly (all nonempty subset products
  non-squares); Lambda != 0 (nonzero forms only); conditions (2.9)-(2.11)
  with C0=1.23*C0', W0=ln(2eB) verified to ALL PASS.
holds-here: yes
status: checked
bearing: the theorem is effective (computed explicit constants) but is a
  per-form bound: for the exact solutions of the (2,3) curve the linear form
  is identically zero, so the machinery constrains near-misses/inequalities
  (e.g. |ln a - ln b| for distinct collision values), not the exact
  triangular=tetrahedral equalities themselves.  PDF correction vs older
  summary: Theorem 2.3(ii) uses theta = 1/(2 - 2/(n e^{n+1})) (~= 0.5008 for
  n=4, > 0.5 as the paper states), NOT (1/2)(1 - 1/(n e^{n+1})) which would
  be < 0.5.  The task's parameter line "C3 = rho = n" is a typo for
  C3 = n/rho = n with rho = 1.
anchor: code/out/matveev_2_3_constant.captured.txt
```