# Bad-prime-minors criterion verified for n=4; certified-bad frontier for n=20

Canonical claim blocks live in `research/notes/badprimes-criterion-n4-n20.md`.

## Computation record

### TASK 1 — n=4, exact verification of Thm 3.1 (arXiv:2411.13967)

Program `code/badprimes_criterion/verify_badprimes_n4.py` (capture
`code/out/badprimes_n4.captured.txt`, exit 0, ALL CHECKS PASSED).

- parameters: n=4, d=4, C=15, D=19 (matches the source's values)
- all 64 tuples T in {1,2,3,4}^3; M_T is 19×15; J_T = gcd of all 15×15
  minors, computed exactly as |product of the 15 Smith-normal-form invariant
  factors|
- lcm over all T of J_T = **1575 = 3²·5²·7**
- prime divisors of lcm J_T = **exactly {3,5,7}**, matching the known bad
  primes of degree 4 (Castryck et al. 2012 Thm 3-4 / de Jong-Draisma)
- second independent route: rank_{F_p}(M_T) < 15 iff p ∈ {3,5,7}, checked
  for every tuple and every prime ≤ 101 — agrees exactly
- sufficient binomial criterion p | C(4,i)-1 (i=1..3): {3,5}, a strict
  subset of {3,5,7} (it misses 7)
- sanity: a generic random 19×15 matrix has J = 1; J_{(1,1,1)} = 1 also
  confirmed by brute-force enumeration of all 3876 minors

### TASK 2 — n=20 certified-bad frontier

Program `code/badprimes_criterion/certified_bad_frontier_n20.py` (capture
`code/out/badprimes_n20_frontier.captured.txt`, exit 0, ALL CHECKS PASSED).

- certified-bad primes p | C(20,i)-1 (1≤i≤19), exact factorint of values
  ≤ 184755: the **18 primes**
  {2,3,5,7,11,13,17,19,37,67,89,103,109,113,173,419,1223,15269}
- independently reproduced by pure-Python trial division — identical
- 20 smallest primes NOT certified (candidate good primes):
  {23,29,31,41,43,47,53,59,61,71,73,79,83,97,101,107,127,131,137,139}
- candidates < 100: {23,29,31,41,43,47,53,59,61,71,73,79,83,97}
- guard: each candidate asserted to divide no C(20,i)-1
- caveat: the binomial criterion is SUFFICIENT only (n=4 calibration shows
  it misses 7), so non-certified primes are candidate-good, not proven-good

## Notes on correctness

- The one real bug found: sympy's `expr.subs(dict)` is SEQUENTIAL, not
  simultaneous, which corrupted the linear substitutions x_i → x_i − x_j
  (Phi_j). Fixed with fresh-dummy simultaneous substitution
  (`_simultaneous_subs` in lib/badprimes.py), verified by hand:
  Φ₂(σ₁) = x₁ − 3x₂ + x₃, and the Lemma 3.3 multiplicity fact (coeff of
  x_j^i in G_{T,i} is C(i+n−2,n−2) up to sign) now holds.
- The SNF-minor identity (gcd of all C×C minors = |product of invariant
  factors|) verified against brute-force minor enumeration on 9 small random
  matrices (all match).
- Generic random 19×15 matrices give J = 1 (sanity control).
