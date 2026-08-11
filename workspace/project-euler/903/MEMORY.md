# Working memory

## THE ANSWER

**Q(10^6) mod (10^9+7) = 128553191**

Computed by code/solution103.py (modular O(n) evaluator) and cross-verified by
code/closedform_exact.py (exact Fraction/big-int).  Both exit 0 with ALL PASS.
Constituent values at n=10^6 mod p: A_n=351421860, B_n=80980398,
S(n)=695671486, H_n=881884276, n!=641102369.

## The closed forms (SEALED 18 Sep 2025 — every identity verified)

f_n(k) = A_n + (k-1) B_n, with (n >= 3; n=2 special: A_2=1, B_2=0):
  E1 = H_n
  E2 = (1/4) H_{floor(n/2)}
  E11 = n + S(n),  S(n) = sum_{a+b<=n} 1/lcm(a,b)
  A_n/(n!)^2 = 1/2 + E2/[n(n-1)] - (E11-E1)/[2 n (n-1)]
  B_n/(n!)^2 = [n - (n+1)E1 + E11 - 2 E2] / [n(n-1)(n-2)]
  Q(n) = (n!)^2 + A_n (n!-1) + (B_n/2) T(n),  T(n)=sum_{m=1}^{n-1} m(m-1)m!
S(n) evaluated mod p as sum_{d<=n/2} phi(d)/d^2 * T(n//d), T(m)=T(m-1)+2H_{m-1}/m
(1/lcm = gcd/ab, gcd = sum_{d|a,d|b} phi(d)).  Full derivation: code/closedform_derivation.md.

VERIFIED EXACTLY (code/closedform_exact.py, ALL PASS):
  (a) Campion-Loth Lemma 4.7 per-class inversion probability — direct
      enumeration vs formula, every class x every gap, n=4..7: PASS.
  (b) The three mu-moments by DIRECT orbit summation n=3..9:
      E_mu[a1]=H_n, E_mu[a2]=(1/4)H_{floor(n/2)}, E_mu[a1^2]=n+S(n): ALL PASS.
  (c) Closed-form f_n rows == out/extend_f.json n=2..11 (exact big-int);
      Q(n) via verified reduction == brute Q(2..8) and extend_f Q(9,10,11);
      Q(10) mod p == 468421536 (statement oracle): ALL PASS.

MODULAR EVALUATOR (code/solution103.py, ALL PASS): self-tests Q mod p for
n=2..11; S direct O(n^2) vs phi-method at 10^4 and 5*10^4; exact-Fraction
phi-S vs modular at 2000 and 5000; stability at 10^6 (telescoped == direct).
Independent route: exact-rational closed form == modular at n=12,13,20,30,50,100.

Closed-form values A_n/(n!)^2, B_n/(n!)^2 (n=2..11):
  n=2: 1/4, 0; n=3: 5/18, 1/36; n=4: 23/72, 0; n=5: 421/1200, -3/400;
  n=6: 83/225, -1/144; n=7: 6841/17640, -29/3528; n=8: 9413/23520, -11/1440;
  n=9: 74477/181440, -257/36288; n=10: 23743/56700, -653/100800;
  n=11: 1301911/3049200, -18947/3049200.

## Problem

Q(n) = sum over all permutations pi of {1..n} of [ sum_{i=1}^{n!} rank(pi^i) ],
where rank(pi) is the 1-based position of pi in the lexicographically sorted
list of all n! permutations (one-line notation, e.g. rank(2,1,3)=3), and pi^i is
the i-th iterate with (pi^{k+1})(j) = pi(pi^k(j)), pi^0 = identity.
Need Q(10^6) mod (10^9+7); statement gives Q(2)=5, Q(3)=88, Q(6)=133103808,
Q(10) ≡ 468421536 (mod 10^9+7).

## Established results

Verified by brute.py (literal double sum) AND brute2.py (independent period
formula), all run 18 Sep 2025 (UTC), exact integers then reduced mod p:

| n | Q(n) | Q(n) mod (10^9+7) | method1 time | method2 time |
|---|---|---|---|---|
| 2 | 5 | 5 | <0.01s | <0.01s |
| 3 | 88 | 88 | <0.01s | <0.01s |
| 4 | 4808 | 4808 | <0.01s | <0.01s |
| 5 | 597876 | 597876 | 0.00s | 0.00s |
| 6 | 133103808 | 133103808 | 0.13s | 0.00s |
| 7 | 47124948960 | 124948631 | 7.17s | 0.02s |
| 8 | 24768798220800 | 798047424 | not reached (est. 8.7 min > budget) | 0.16s |

- Oracle checks: rank(2,1,3)=3, Q(2)=5, Q(3)=88, Q(6)=133103808 — all pass.
- Cross-validation: methods exactly agree for n=2..7 (Q values identical, not
  just congruent mod p).  Note: for n≤5 Q(n) < p so mod is trivially equal.
- Structural fact behind brute2 (proved inline): pi^i is periodic with period
  d = ord(pi) = lcm of cycle lengths.  Every cycle length divides n!, hence
  d | n!, so among i = 1..n! each distinct power appears exactly n!/d times;
  sum_i rank(pi^i) = (n!/d) * sum_{tau in <pi>} rank(tau).
- Time/space: method 1 is O((n!)^2) tuple compositions + O(n!) rank dict (ran
  for n ≤ 7, 5040^2 = 25.4M steps in 7.2s); method 2 is O((n!) * avg d) + O(n!)
  (much faster, reached n=8 in 0.16s).  Both are exact-integer arithmetic.

## Failed approaches

### ccsum.py conjugacy-class engine is INVALID (18 Sep 2025, re-confirmed)
ccsum.py tried f_n(k) = sum over partitions lambda of class_size*(n!/lcm(lambda))*S(lambda,k),
reading S(lambda,k)=#{tau in <pi>: tau(k)<tau(0)} off ONE representative per cycle
type and multiplying by class size.  OUTCOME: rows match oracle-verified
out/extend_f.json ONLY at n=2; differ for every n=3..30 and aren't even arithmetic in
k (trusted rows are exactly arithmetic).  ROOT CAUSE PROVEN (test_classconst.py and a
direct S_3/S_4 count in this run): S is NOT a class function — within one cycle type
it takes several distinct values (n=4 type (1,3): S in {0,1,2}).  So a single
representative per class does not represent the class's S-values.  DEAD END for ccsum
as written; a correct engine would sum S over all representatives per class (or weight
by the intra-class S distribution), which defeats the perf advantage.  Trusted A_n/B_n
remain n=2..11 from out/extend_f.json.

## gaps.py — T(j,m) translation invariance & arithmetic form (18 Sep 2025)

T(j,m) = #{(pi,i): 0<=i<n!, (pi^i)(m) < (pi^i)(j)}, computed for n=2..9 with
the period formula T(j,m) = sum_pi (n!/ord(pi)) * #{tau in <pi>: tau(m)<tau(j)}
with exact Fractions (no literal n!-power iteration).

Verified: literal double-count oracle agrees for n=2,3 (in-script), n=4,5
(separate oracle).  Translation invariance T(j,j+k) independent of j holds for
ALL j in every n (checked exhaustively).  f_n(k)=T(1,1+k) is exactly
ARITHMETIC (constant 2nd difference = 0) for every n>=3, with values:

| n | f_n(k) = A_n + (k-1) B_n | A_n = f(1) | B_n (step) |
|---|---|---|---|
| 2 | [1] (trivial) | 1 | - |
| 3 | 10,11 | 10 | +1 |
| 4 | 184,184,184 | 184 | 0 |
| 5 | 5052,4944,4836,4728 | 5052 | -108 |
| 6 | 191232,187632,184032,180432,176832 | 191232 | -3600 |
| 7 | 9851040,9642240,9433440,9224640,9015840,8807040 | 9851040 | -208800 |
| 8 | 650626560,638208000,625789440,613370880,600952320,588533760,576115200 | 650626560 | -12418560 |
| 9 | 54052427520,53119825920,52187224320,51254622720,50322021120,49389419520,48456817920,47524216320 | 54052427520 | -932601600 |

Conjecture (structure): f_n(k) = A_n + (k-1) B_n is arithmetic in the gap k for
all n; B_n<=0 for n>=5.  Sequence A_n: 1,10,184,5052,191232,9851040,...
(no obvious closed form derived yet).

## extend_f.py — f_n(k) extended to n=11 (18 Sep 2025)

extend_f.py (period formula, 0-based, row j=0, exact ints, no mod) computes
f_n(k) = #{(pi,i): 0<=i<n!, (pi^i)(k) < (pi^i)(0)} for k=1..n-1 by enumerating
S_n with itertools.permutations(range(n)), per pi using d=ord=lcm of cycle
lengths and weight n!/d over the d distinct powers (<pi> via repeated
composition).  Literal oracle (i=0..n!-1) passed for n=2..6.  Results saved
incrementally to /workspace/extend_f.json as {n: [f(1),...,f(n-1)]}.

New rows (n=2..9 matched the gaps.py table exactly):
  n=10: [5514150297600, 5428844467200, 5343538636800, 5258232806400,
         5172926976000, 5087621145600, 5002315315200, 4917009484800,
         4831703654400]            A_10 = 5514150297600,  B_10 = -85305830400
  n=11: [680309947699200, 670409245900800, 660508544102400, 650607842304000,
         640707140505600, 630806438707200, 620905736908800, 611005035110400,
         601104333312000, 591203631513600]   A_11 = 680309947699200,
                                             B_11 = -9900701798400

2nd differences are all zero for every n=2..11 → f_n(k) is EXACTLY arithmetic
in k for all n tested.  Timings: n=8 0.16s, n=9 1.8s, n=10 21.6s, n=11 334.8s
(script's 280s gate then stopped the loop as designed).  Sequence A_n:
1, 10, 184, 5052, 191232, 9851040, 650626560, 54052427520, 5514150297600,
680309947699200.  B_n (n>=3): 1, 0, -108, -3600, -208800, -12418560,
-932601600, -85305830400, -9900701798400.

INDEPENDENT VERIFICATION: verify_f_method2.py recomputes f_n(k) by a
completely different algorithm — cycle-type decomposition (per permutation,
read the d-th power analytically off cycles, count tau(k)<tau(0) over the
distinct powers by closed-form cycle counts instead of power iteration).
Sanity-checked against the literal method for n=3..7, then run for n=10 and
n=11: rows match extend_f.json EXACTLY (mod-free integers).  n=11 again took
~319s.  So the n=10, n=11 rows are independently confirmed.

Open lead for the closed form: |B_n|/(n-1)! is an exact integer for n=6..11:
30, 290, 2464, 23130, 235080, 2728368 (and n=5 gives 4.5, not integer).
A_n/A_{n-1}: 10, 18.4, 27.4565, 37.85, 51.51, 66.05, 83.08, 102.01, 123.38 —
appears to grow ~ (n-1)(n-2)ish.  Neither has a closed form yet; that is the
next step toward Q(10^6) mod p.

## Open questions

- Efficient method for n = 10^6 (n! is astronomically beyond enumeration):
  need a structural/analytic closed form, e.g. via rank = sum of factoradic
  weights, cycle-type / conjugacy-class decomposition, and the sum over i of
  rank(pi^i).  Unresolved.
- Q(10) check against statement (468421536 mod p): RESOLVED 18 Sep 2025 — the
  verified chain Q(n)=(n!)^2+A(n!-1)+(B/2)T with A=B=f(0)/f(1)-f(0) from
  extend_f.json gives Q(10) mod p = 468421536 exactly (task12.py).  This also
  independently confirms the n=10 gap constants A_10=5514150297600,
  B_10=-85305830400.
- Extending f_n rows to n=12/13: n! enumeration (f_n_method2) walls at ~54min
  (n=12) / ~12h (n=13) — needs a conjugacy-class-summing method, not written.

## Structural finding from explore.py (n = 2..7, exact integers, 18 Sep 2025)

Definitions (0-indexed one-line permutation of {0..n-1}):
  a_j(tau) = #{ m>j : tau[m] < tau[j] }   (Lehmer coefficient)
  M_j      = sum_pi sum_{i=0}^{n!-1} a_j(pi^i)
  N(j,m)   = #{(pi,i) : 0<=i<n!, (pi^i)[m] < (pi^i)[j]}

Verified on every n=2..7:  M_j = sum_{m>j} N[j][m]  (linearity; identity is
exact, not asymptotic).

KEY PATTERN: N(j,m) depends ONLY on the gap k = m-j (translation invariance),
i.e. N(j,m) = f(k).  So M_j = sum_{k=1}^{n-1-j} f(k)  is a suffix sum of the
gap function f(k).  Hence M_j is NOT constant in j; it decreases with j.

Observed f(k) = N(j, j+k):
  n=2: f(1)=1
  n=3: f(1)=10,  f(2)=11
  n=4: f(1)=f(2)=f(3)=184
  n=5: f(1..4)=5052,4944,4836,4728  (arithmetic, step -108)
  n=6: f(1..5)=191232,187632,184032,180432,176832  (arithmetic, step -3600)
  n=7: f(1..6)=9851040,9642240,9433440,9224640,9015840,8807040 (step -208800)

M_j vectors (j=0..n-1):
  n=2: [1,0]
  n=3: [21,10,0]
  n=4: [552,368,184,0]
  n=5: [19560,14832,9996,5052,0]
  n=6: [920160,743328,562896,378864,191232,0]
  n=7: [55974240,47167200,38151360,28926720,19493280,9851040,0]

So the per-position Lehmer contributions are translation-invariant in pairwise
form, and M_j is the suffix sum of f(k).  To get Q(n) we need sum_j (n-j)! M_j
then + (n!)^2 (rank = 1 + sum_j a_j (n-j)! over powers; the +1 per power term
sums to n!·n! = (n!)^2).  Next step: derive a closed form for f(k).

CORRECT factoradic weight (verified by exact Q reconstruction for n=2..7):
  rank(tau) = 1 + sum_{j=0}^{n-2} a_j(tau) * (n-1-j)!   [weight is (n-1-j)!, NOT (n-j)!]
  Q(n) = (n!)^2 + sum_{j=0}^{n-2} (n-1-j)! * M_j
Cross-check: with M_j from explore.py and this formula, Q matches all of
Q(2..7)={5,88,4808,597876,133103808,47124948960} exactly (done 18 Sep 2025).
This is an independent second route to the M_j tables' correctness.

## Established results

### CENTRAL REDUCTION VERIFIED (verify_red.py, 18 Sep 2025) -- ALL PASS n=2..8

Using Q(n) = (n!)^2 + sum_{j=0}^{n-2} (n-1-j)! * M_j, M_j = sum_{k=1}^{n-1-j} f(k),
and f(k)=A_n+(k-1)B_n (exactly arithmetic, verified), substituting r=n-1-j:

  Q(n) = (n!)^2 + A_n * S(n) + (B_n/2) * T(n)
  S(n) = Sigma_{m=1}^{n-1} m*m!  =  n! - 1   (telescoping, verified n=3..8)
  T(n) = Sigma_{m=1}^{n-1} m*(m-1)*m!
  A_n = f[0],  B_n = f[1]-f[0]  (from extend_f.json; n=2: A=1, B term=0)

Verified EXACTLY (big ints) against Q(2..8): 5, 88, 4808, 597876, 133103808,
47124948960, 24768798220800.  All PASS.  Caveat encountered: use (B*T)//2
(B*T always even since m(m-1) is even), NOT (B//2)*T which fails at n=3.

So the whole Q(10^6) problem is now reduced to finding A_n and B_n (or
f_n(k)=A_n+(k-1)B_n).  A_n: 1,10,184,5052,191232,9851040,650626560,
54052427520,5514150297600,680309947699200.  B_n (n>=3): 1,0,-108,-3600,
-208800,-12418560,-932601600,-85305830400,-9900701798400.
