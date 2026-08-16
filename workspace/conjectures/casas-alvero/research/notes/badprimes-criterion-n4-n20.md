# Bad-prime-minors criterion verified for n=4; certified-bad frontier for n=20

Computation record: `code/out/badprimes_criterion_n4_n20.md` (notes on the
sympy sequential-subs bug and the SNF-minor identity).

## Claims

```claim
id: badprimes-n4-minor-criterion-verified
status: checked — reproduced by code/badprimes_criterion/verify_badprimes_n4.py:
  all 64 tuples T in {1,2,3,4}^3, J_T = gcd of all 15x15 minors of the 19x15
  matrix M_T computed exactly as |product of the 15 Smith-normal-form invariant
  factors|, lcm = 1575 = 3^2 * 5^2 * 7; prime divisors {3,5,7} confirmed by a
  second route (rank_{F_p}(M_T) < 15 exactly for p in {3,5,7}, every tuple,
  every prime <= 101). Capture: code/out/badprimes_n4.captured.txt, exit 0.
holds-here: yes
statement: For degree n=4, the prime divisors of lcm_{T in {1,2,3,4}^3} J_T
  are exactly {3, 5, 7}, matching the known bad primes of degree 4 (Castryck
  et al. 2012 Thm 3-4 / de Jong-Draisma). The sufficient binomial criterion
  p | C(4,i)-1 gives {3,5}, a strict subset of the true bad primes.
hypotheses: degree 4; the minor criterion (Thm 3.1 of arXiv:2411.13967) is
  unconditional
evidence: verified-computationally — exact integer arithmetic, two
  independent routes agree, matches the published bad-prime list
program: code/badprimes_criterion/verify_badprimes_n4.py
capture: code/out/badprimes_n4.captured.txt
anchor: research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md (Thm 3.1)
falsifies: a prime other than {3,5,7} dividing lcm J_T, or {3,5,7} failing
  to divide it, computed with the same exact method
```

```claim
id: badprimes-n20-certified-frontier
status: checked — reproduced by code/badprimes_criterion/certified_bad_frontier_n20.py:
  exact sympy factorint of C(20,i)-1 for i=1..19 (all values <= 184755),
  independently reproduced by pure-Python trial division; each of the 20
  frontier candidates asserted to divide no C(20,i)-1. Capture:
  code/out/badprimes_n20_frontier.captured.txt, exit 0.
holds-here: yes
statement: The degree-20 certified-bad primes by the sufficient binomial
  criterion p | C(20,i)-1 (arXiv:2307.05997 Cor 8) are the 18 primes
  {2,3,5,7,11,13,17,19,37,67,89,103,109,113,173,419,1223,15269}. The
  frontier — 20 smallest primes NOT certified (candidate good primes) — is
  {23,29,31,41,43,47,53,59,61,71,73,79,83,97,101,107,127,131,137,139}; the
  candidates < 100 are {23,29,31,41,43,47,53,59,61,71,73,79,83,97}.
hypotheses: the binomial criterion is SUFFICIENT (Cor 8 of arXiv:2307.05997),
  so a non-certified prime is a candidate good prime, NOT a proven good prime
  (calibration at n=4: criterion captures {3,5} of {3,5,7})
evidence: verified-computationally — exact integer arithmetic, two
  independent factorization routes agree
program: code/badprimes_criterion/certified_bad_frontier_n20.py
capture: code/out/badprimes_n20_frontier.captured.txt
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Cor 8)
falsifies: a certified prime that does not divide any C(20,i)-1, or a
  non-certified prime below 139 that divides one (computed exactly)
```

The full minor criterion for n=20 is infeasible: C = binomial(190,18) ~ 10^20
columns would make the gcd-of-minors computation astronomical. The binomial
criterion is the exact, cheap, certified subset.
