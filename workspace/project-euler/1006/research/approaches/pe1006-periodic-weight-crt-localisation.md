# Multiplicative-order localisation of decimal weights

```approach
slug: pe1006-periodic-weight-crt-localisation
idea: Reduce Ψ(k) modulo M componentwise modulo each prime-power factor q of M by CRT, exploiting that gcd(10,M)=1 makes the decimal weights 10^j periodic with period ord_q(10). The observed mod-100 simplification Ψ(k) ≡ 1+⌊k/φ²⌋ (mod 100) is the first rung of this periodicity.
status: narrowed
survives: the elementary periodicity of 10^j modulo each prime-power factor of M
revive-when: factor M completely and derive a joint finite state whose dimension is bounded independently of k, including the Sturmian boundary/intercept data
precedent: https://doi.org/10.1007/s00209-021-02834-3; https://doi.org/10.1016/j.tcs.2018.01.033; claim: universal-euclidean-geometric-floor-sum; claim: governing-sturmian
killed-by: (as a primary route) periodicity of the coefficient sequence alone does not make Ψ(k) finite-state: the factor set and its pair correlations still depend on k through the irrational Sturmian rotation. The existing floor-sum/Euclidean claim handles those floor moments; periodic coefficients shorten coefficient bookkeeping but do not remove the intercept/boundary state. No source proves the claimed k-independent collapse modulo the odd-prime factors.
```

## Literature assessment

This is best called **CRT localisation plus multiplicative-order periodicity** (finite-ring periodic weighting), not a Sturmian collapse theorem. If q is a prime power coprime to 10 and L=ord_q(10), then 10^{j+L}=10^j mod q; CRT decomposes congruences modulo coprime prime powers. These are elementary facts whose hypotheses hold whenever gcd(10,q)=1.

They do apply to the decimal weights in PE1006, but periodicity of the coefficients does not make Ψ(k) finite-state: the factor set and its pair correlations still depend on k through the Sturmian rotation. The observed mod-100 simplification is a checked instance of coefficient periodicity, not evidence for the full claim. Hence **narrowed**: the elementary first rung is valid and could shorten coefficient bookkeeping inside the adopted bivariate/Euclidean monoid, but it is not a standalone O(log k) route.

## What it would buy

After a complete factorisation M=∏q and a proof that the Sturmian state also closes modulo each q, one could evaluate each component with a fixed state and CRT-combine. At present it only reduces repeated powers of 10.
