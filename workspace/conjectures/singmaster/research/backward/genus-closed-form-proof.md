```skeleton
goal: Prove (not merely check) that for distinct m,n >= 2 the geometric genus of the projective closure of C(x,m)=C(y,n) equals g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2.
implies: View the curve in P^1 x P^1, where C(x,m)=C(y,n) has bidegree (m,n) and arithmetic genus p_a = (m-1)(n-1) (G-bidegree-pa). The geometric genus is p_a - delta, where delta is the total delta invariant of all singularities including those at infinity. If G-delta-invariant holds, delta = ((m-1)(n-1) - 1 + gcd(m,n))/2, hence g = p_a - delta = ((m-1)(n-1) + 1 - gcd(m,n))/2, which is identically equal to ((m-1)n - (m-2) - gcd(m,n))/2 (genus-symmetric-form-and-delta-prediction). Integrality of the RHS is already proved (genus-closed-form-integrality), so the expression is a valid integer genus. Bilu-Tichy Prop 4.1 (2g-2 = sum_gamma (mn - Omega(gamma)) - mn - gcd(m,n)) is an independent route to the same formula once the Omega(gamma) are computed.
status: live
rests-on: genus-closed-form-integrality, genus-symmetric-form-and-delta-prediction, bilu-tichy-classification-primary
```

```gap
id: G-delta-invariant
lemma: The total delta invariant of the singularities of C(x,m)-C(y,n)=0 on P^1 x P^1 (distinct m,n >= 2) is delta(m,n) = ((m-1)(n-1) - 1 + gcd(m,n))/2. Equivalently g = p_a/2 = (m-1)(n-1)/2 whenever gcd(m,n)=1.
status: open
next: resolve the singularities at the common vanishing points of the two binomial polynomials (where the common falling factorial vanishes) and at infinity, then sum the delta contributions. The mechanism named in genus-symmetric-form-and-delta-prediction is the involution z -> k-1-z giving C(k-1-z,k) = (-1)^k C(z,k), a 2:1 structure that should account for the factor of 2. First concrete move for symbolic_math: run Singular on 3 representative pairs — (5,7) coprime, (4,6) gcd 2, (6,8) gcd 2 — and extract the singularity type and delta of each singular point (affine and at infinity), then match against the predicted total delta.
```

```gap
id: G-bidegree-pa
lemma: The projective closure of C(x,m)=C(y,n) in P^1 x P^1 has bidegree (m,n) and arithmetic genus p_a = (m-1)(n-1), with the diagonal m=n reducible and therefore excluded.
status: discharged
discharged-by: genus-symmetric-form-and-delta-prediction (records the bidegree-(m,n) and p_a = (m-1)(n-1) identification; elementary for the degree-m and degree-n binomial polynomials)
```
