# PE622 sequence structure — C(k) ord-count and S(k) ord-sum

Computed from code/pe622 (verified k=1..60, cross-checked two ways). All
regularities below are **conjectures that hold exactly over every term
computed** — no proof that they continue.

## Verified beyond k=60 (this pattern run)

`code/pe622/mobius_extend.py` re-verified the Möbius-inversion identities
(items 1) against a DIRECT divisor-enumeration oracle for the sampled orders
k = 61,62,64,66,68,70,72,75,76,78,80,84,90,96,100,102,108,120,122
(19 orders, all with 2^k−1 having ≤200k divisors): every one agrees exactly on
both C and S. Falsification candidate would be the first k>60 that disagrees;
none found through k=122. This strengthens the k≤60 record: the identity
survives a deliberate attempt to break it outside the data that suggested it.

`code/pe622/ie_cube_extend.py` (THIS pattern run) verifies the full **general**
cube identity for ALL k = 1..130: the 2^{ω(k)}-term inclusion–exclusion over
maximal proper divisors k/p equals the Möbius-inversion C(k), S(k) exactly.
The only mismatch anywhere is k=1 (C(1)=0 vs cube=1), the documented m=1
convention. This upgrades the k=60 cube {12,20,30} from "the k=60 special
case" to "one instance of a general signed sum"
   C(k) = τ(2^k−1) + Σ_{T⊆primes(k)} (−1)^{|T|} τ(2^{k/π(T)}−1)
   S(k) = σ(2^k−1) + Σ_{T⊆primes(k)} (−1)^{|T|} σ(2^{k/π(T)}−1)
with π(T) the product of primes in T. The k=60 instance (ω=3, 8 terms:
N, 4095, 1048575, 1073741823, 15, 63, 1023, 3) is the Lean proof's signed sum.

`code/pe622/maximal_proper_divisor_check.py` establishes the structural
inclusion–exclusion reduction used at k=60 as a GENERAL lattice fact: for any
k, the order-k set equals divisors(2^k−1) minus the union over the MAXIMAL
proper divisors M of k of A_M = {m : m | 2^M−1}. Reason: if d|M then A_d ⊆ A_M
(m|2^d−1 implies m|2^M−1), and every proper divisor of k divides one of its
maximal proper divisors (the covers of k in the divisor poset); so the union
over ALL proper divisors collapses to the union over just the maximal ones.
k=60 has exactly three maximal proper divisors — {12,20,30} — giving the 2³=8
term inclusion–exclusion (N, 4095, 1048575, 1073741823, 15, 63, 1023, 3)
that the Lean proof uses. This is the reason the answer is a small signed sum
of eight σ/τ values, not an enumeration.

## Objects

- m = n−1 (odd, since n even).
- s(n) = ord_{n−1}(2) (structural reduction, rest of run).
- C(k) = #{m > 1 : ord_m(2) = k}
- S(k) = sum of those m
- Answer = sum of n with s(n)=60 = S(60) + C(60) = 3010983666182123972.

## Terms (k=1..60)

C: 0,1,1,2,1,3,1,4,2,5,3,16,1,5,5,8,1,24,1,38,9,11,3,68,6,5,4,54,7,79,1,16,11,5,13,462,3,5,13,140,3,123,7,110,54,11,7,664,2,114,29,118,7,124,59,188,13,55,3,4456

S: 0,3,7,20,31,93,127,408,584,1501,2159,8612,8191,22397,38873,111024,131071,472912,524287,1998316,2465913,5907597,8567135,38044872,34713696,89513981,155492944,462252012,539922239,2015289795,2147483647,7304491872,10359012233,22907060221,36251172705,166289949768,138055271871,366506147837,636328337401,2220407884392,2199187780271,7645338162979,8817412930559,29833833634540,42424026490296,95821831239837,140828559963839,648494278961616,567382630219904,1701423638038944,2599936977666041,7396670153818092,9008745449302367,32817383317182896,39301113940621169,131390354324274792,164708609085145081,393042225228269757,576463955735383775,3010983666182119516

## Verified structure

1. **Möbius inversion** (verified k=1..60 against direct divisor enumeration):
   C(k) = Σ_{d|k} μ(k/d)(τ(2^d−1)−1)
   S(k) = Σ_{d|k} μ(k/d)(σ(2^d−1)−1)
   Core iff (odd m, gcd(2,m)=1): ord_m(2) | k ⟺ m | 2^k−1.

2. **Prime order** k=p: C(p)=τ(2^p−1)−1, S(p)=σ(2^p−1)−1 (divisors of p are
   {1,p}, μ(p)=−1). Verified all primes p≤79.

3. **Mersenne signature**: when 2^p−1 is prime, C(p)=1 and S(p)=2^p−1.
   Verified for p = 2,3,5,7,13,17,19,31,61 (all primes p in 2..63).

4. **Inclusion-exclusion at k=60**: every proper divisor d of 60 divides one of
   {12,20,30}, so the order-60 set = divisors(2^60−1) \ (A_12 ∪ A_20 ∪ A_30)
   with A_k={m|2^k−1}. Gives C=4456, S=3010983666182119516, answer 3010983666182123972.

```claim
id: pe622-answer-order-sixty
statement: The sum of all positive even n with s(n) = 60 (Project Euler 622)
  is 3010983666182123972, where s(n) is the number of consecutive perfect
  out-shuffles needed to restore a deck of size n.
hypotheses: n positive even, s(n) = ord_{n-1}(2) (established by
  outshuffle-order-equals-ord).
holds-here: yes.
bearing: This is the final numeric answer. It is the sum over the m=n-1 with
  ord_m(2)=60, i.e. S(60)+C(60), where the legal m are exactly the divisors of
  2^60-1 not dividing 2^12-1, 2^20-1, 2^30-1 (G-ord-criterion); S(60)=
  3010983666182119516 and C(60)=4456 by the inclusion-exclusion/Möbius routes.
status: checked
anchor: code/pe622/solution.py (structural divisor enumeration) agreeing with
  code/pe622/verify_answer.py (Möbius inversion, k=1..24 and k=60), and
  code/pe622/pattern_verify.py (identity for every k=1..60); all three
  produce 3010983666182123972. Worked-example oracle s(52)=8, s(86)=8,
  sum{s(n)=8}=412 reproduced in code/pe622/oracle_check.py.
```

## Negative results

- Neither C nor S satisfies a constant-coefficient linear recurrence of order
  ≤10 (find_linear_recurrence: none over the terms given).
- Neither is a low-degree polynomial (differences do not stabilise).
- CORRECTION (this run): the earlier "both OEIS misses" note was an artifact
  of the leading term. **C(k) IS catalogued as OEIS A059499** = |{m: ord_m(2)=n}|,
  formula a(n)=Sum_{d|n} mu(n/d)*tau(2^d-1) (Alekseyev/Heinz). Verified the
  formula reproduces all 60 official terms and equals our C(k) for every k>=2;
  A059499(1)=1 counts m=1, which our C(1)=0 excludes (-1 in the formula).
  C(60)=A059499(60)=4456. The S-sequence (sum of m) is genuinely NOT in OEIS
  (lookup returns no match) — its structure must come from the Möbius form.
