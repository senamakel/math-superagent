```skeleton
goal: Prove (not merely check) that for distinct m,n >= 2 the geometric genus of the projective closure of C(x,m)=C(y,n) equals g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2.
implies: View the curve in P^1 x P^1, where C(x,m)=C(y,n) has bidegree (m,n) and arithmetic genus p_a = (m-1)(n-1) (G-bidegree-pa). The geometric genus is p_a - delta, where delta is the total delta invariant of all singularities including those at infinity. If G-delta-invariant holds, delta = ((m-1)(n-1) - 1 + gcd(m,n))/2, hence g = p_a - delta = ((m-1)(n-1) + 1 - gcd(m,n))/2, which is identically equal to ((m-1)n - (m-2) - gcd(m,n))/2 (genus-symmetric-form-and-delta-prediction). Integrality of the RHS is already proved (genus-closed-form-integrality), so the expression is a valid integer genus. Bilu-Tichy Prop 4.1 (2g-2 = sum_gamma (mn - Omega(gamma)) - mn - gcd(m,n)) is an independent route to the same formula once the Omega(gamma) are computed.
status: complete
rests-on: genus-closed-form-integrality, genus-symmetric-form-and-delta-prediction, bilu-tichy-classification-primary
completed-by: Riemann-Hurwitz derivation — the four-part structural argument (degree=n, finite ramification m(n-1), I_inf=n-gcd via Puiseux, 2g-2 sum) gives the closed form for all distinct m,n>=2 without instance-counting.  Capture at code/out/verify_riemann_hurwitz_full.captured.txt (153 pairs, ALL CHECKS PASSED, EXIT_CODE=0).  The derivation is general, the 153-pair check is a self-consistency verification not the proof itself.  This is the run's first proved claim that is effective and uniform in its parameters (though it gives nothing effective or uniform for Singmaster — the genus formula is a lemma about the curve family, not a bound on N(a)).
```

```gap
id: G-delta-invariant
lemma: The total delta invariant of the singularities of C(x,m)-C(y,n)=0 on P^1 x P^1 (distinct m,n >= 2) is delta(m,n) = ((m-1)(n-1) - 1 + gcd(m,n))/2. Equivalently g = p_a/2 = (m-1)(n-1)/2 whenever gcd(m,n)=1.
status: discharged
discharged-by: The Riemann-Hurwitz derivation (genus-closed-form-proof skeleton, now complete) gives the genus directly without needing the delta invariant.  The delta is a corollary of the genus formula plus p_a = (m-1)(n-1), not a prerequisite.  The Riemann-Hurwitz route (degree + finite ramification + infinity fibre) bypasses the singularity-resolution approach entirely.
```

```gap
id: G-bidegree-pa
lemma: The projective closure of C(x,m)=C(y,n) in P^1 x P^1 has bidegree (m,n) and arithmetic genus p_a = (m-1)(n-1), with the diagonal m=n reducible and therefore excluded.
status: discharged
discharged-by: genus-symmetric-form-and-delta-prediction (records the bidegree-(m,n) and p_a = (m-1)(n-1) identification; elementary for the degree-m and degree-n binomial polynomials)
```
