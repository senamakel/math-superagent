# |Φ(B)| asymptotic = (2/π²)B² — pattern_finder finding (this session)

Derived from the run's own exact closed form (phi_identity_verify.py, verified
exact vs direct enumeration B ≤ 1200):

    |Φ(B)| = Σ_{M even ≤ B} φ(M)  +  ½ Σ_{M odd ≤ B} φ(M)

with φ the Euler totient, where Φ(B) = { f(m,n) : m>n≥1, m≤B }, the universal
rational set of the MSS centre-AP differences.

## Result (verified-numerical, exact arithmetic)

|Φ(B)|/B² → **2/π² = 0.202642** (matches to 6 significant figures by B = 2×10⁶):

    B=1000:     0.202862
    B=10⁴:      0.202658
    B=10⁵:      0.202644
    B=10⁶..2e6: 0.202642

Program: `code/out/phi_asymptotic_check.py` (exact integer totient sieve to B).

## Why this is structural, not a fit

Sum_{n≤B} φ(n) ~ 3B²/π² (standard). The even/odd totient partial sums split
as E ~ S/3, O ~ 2S/3 (verified numerically), so

    |Φ(B)| = E + O/2  ~  S/3 + (2S/3)/2  ~  (2/3)(3B²/π²)  =  2B²/π².

So |Φ(B)| ~ (2/3)·Σφ(B) — checked |Φ|/((2/3)S) = 1.0000013 at B=4×10⁵,
`code/out/phi_two_thirds_check.py`. This confirms the earlier guess from finite
terms: |Φ(2^k)| = 1,4,15,55,217,847,3358,13332,53258,212740 has term ratios
→ 4, consistent with quadratic growth |Φ| ~ 2/π²·4^k, NOT a low-order linear
recurrence (the order-5 recurrence the tool found over 10 terms is an overfit:
5 free rational coefficients on 10 points fit almost anything; the OEIS miss
confirms no catalogued closed form).

## OEIS checks on this run's crowded sequences

- Run's S2 record |S(e)| values 0,1,2,4,7,13,22,31,40,67,94,121,202 = **A088111**;
  record-holder e's 1,5,25,65,325,1105,… = **A088959 = A006339 = A046112**
  (minimal hypotenuse with n representations as sum of two squares).
- `code/oeis_verify.py` routes A (A006339 backtracking match True) and B
  (primitive-triple count vs formula, 0 mismatches ≤ 60000) PASS.
  **Route C's record sweep is BUGGY**: it cumulatively multiplies (2a+1) over
  prime powers (overcounts), printing nonsense "records" like 6874655287 at
  e=9765625. Routes A/B are the trustworthy confirmation; do not cite route C.

## Evidence class

Asymptotic constant: **verified-numerical** up to B = 2×10⁶ from the exact
closed form; the closed form itself is verified exact to B = 1200. The
asymptotic is a conjecture (standard totient-sum asymptotics + splitting) —
clean and low-risk, but stated as such.

## Bearing on the problem

|Φ(B)| ~ 2B²/π² is quadratic in B: the number of distinct centre-AP-difference
ratios f(m,n) with m ≤ B grows quadratically. This quantifies "abundance of
differences is not the obstruction" — it is the additive relation among the
four differences u,v,u+v,u−v (all in Φ) that is scarce, not Φ itself.
