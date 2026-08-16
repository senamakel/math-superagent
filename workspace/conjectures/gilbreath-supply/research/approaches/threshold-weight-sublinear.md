```approach
idea: The minimum weight w*(n) at which linear supply becomes typical is sublinear — w*(n) ~ n^0.555 · P(log₂ n), with P a bounded period-1 log-periodic factor of amplitude ~0.07 — so the threshold ratio θ = w*/n → 0. The arithmetic demand this encodes is a sublinear switch count, strictly weaker than positive mod-4 switch density (type 4, never type 1).
mechanism: For strings of weight w, the exact mean of ν₂ over the Krawtchouk route is (1/C(n,w)) Σ_d K_w(2^popcount(d); n), computable exactly per n over n=8..262144; w*(n) is where this mean crosses 0.40·n. A sublinear threshold means typical linear supply requires only ~n^0.555 switches, not Θ(n).
status: grounded
precedent: >
  Hwang–Janson–Tsai, Periodic minimum in the count of binomial coefficients not
  divisible by a prime, arXiv:2408.06817 (2024), Theorem 2.2: every Pascal-mod-p
  counting function has the log-periodic form F_p(n) = n^ρ·P(log_p n) with P a
  continuous 1-periodic function (p=2: OEIS A006046, ρ=log₂(3/2)=0.58496).
  GROUNDS THE FORM (bounded period-1 P(log₂n)) as a theorem for the Paskal-mod-2
  family; does NOT transfer the exponent log₂3−1 (or any constant) to w*(n),
  which is a derived crossing of the fold's sphere-mean — the measured
  E = 0.55678 ± 0.002 stays FITTED, not closed-form. In-workspace: claim
  sphere-mean-krawtchouk-exact (proved), claim hjt-p2-log-periodic-representation-proved,
  notes log_periodic_pascal_mod2_engine.md, grounding_threshold_lemmas_krawtchouk.md.
first-step: Extend the exact-mean computation beyond n=262144 to sharpen the log-periodic factor P, and reduce the θ = w*/n → 0 statement to the pure-F₂ open problem G-threshold-asymptotic-zero (now grounded: HKS Krawtchouk decay).
```

