# Bad-prime-minors criterion verified for n=5 (rank-over-F_p route), with independent semantic route on small primes

Follows the n=4 verification (research/notes/badprimes-criterion-n4-n20.md).
Two independent routes, both exit 0.

Route 1 (criterion): for every one of the 625 tuples T in {1..5}^4 and every
prime p in {primes < 1000} ∪ {3541, 8009} (170 primes), the exact rank of the
195×120 integer matrix M_T over F_p was computed (modular Gaussian
elimination, `lib.badprimes.rank_mod_p`). By Thm 3.1 of arXiv:2411.13967,
p is bad for degree 5 iff p | J_T for some T, and p | J_T iff
rank_{F_p}(M_T) < 120. The rank drops occur exactly for the published list
{2,3,7,11,131,193,599,3541,8009} (Castryck et al. 2012 Thm 4); every listed
prime has a witnessing tuple, every other prime < 1000 has full rank 120 on
all 625 tuples. The SNF route to J_T was measured infeasible at n=5 (one
195×120 SNF exceeded a 90 s cap, code/out/commands.log); the rank route needs
only the drop, never J_T itself.

Route 2 (semantics): for p in {2,3,5,7,11,13} the literal definition was
checked by exhaustive enumeration of all p^5 monic degree-5 polynomials over
F_p through the canonical oracle (lib.casas_alvero.is_ca_hasse /
is_pure_power). A counterexample exists iff p ∈ {2,3,7,11}, matching the
published bad list on these primes and matching Route 1 on 2,3,7,11 bad and
5,13 good. 552,551 polynomials total, 28 workers, 85.4 s.

The two routes measure the same object by different means: the criterion's
rank drop is the algebraic certificate that the bad-prime variety over F_p is
nonempty; the enumeration counts the actual counterexample polynomials on the
primes where the count is feasible. The large bad primes (131, 193, 599,
3541, 8009) are out of enumeration reach (e.g. 131^5 ~ 3.9e10) and are
certified by Route 1 only.

## Claims

```claim
id: badprimes-n5-minor-criterion-verified
status: checked — reproduced by code/badprimes_criterion/verify_badprimes_n5.py:
  all 625 tuples T in {1,2,3,4,5}^4, 170 primes (all primes < 1000 plus
  3541, 8009), 106250 exact rank computations over F_p via
  lib.badprimes.rank_mod_p (28 workers, 386.9 s). Rank drops (rank < 120)
  occur exactly at the 9 published primes, each with witnesses: p=2 (500
  witnesses, min rank 114), p=3 (480, 114), p=7 (180, 118), p=11 (80, 114),
  p=131 (60, 118), p=193 (60, 118), p=599 (180, 118), p=3541 (180, 118),
  p=8009 (120, 119). All 161 primes < 1000 outside the list have full rank
  120 on every tuple. Spot check rank_{3547}(M_(1,2,3,4)) = 120. Capture:
  code/out/badprimes_n5.captured.txt, exit 0.
holds-here: yes
statement: For degree n=5, the rank-over-F_p form of the Schaub-Spivakovsky
  minor criterion certifies exactly the published bad-prime list
  {2,3,7,11,131,193,599,3541,8009} (Castryck et al. 2012 Thm 4): every
  listed prime has rank_{F_p}(M_T) < 120 for some tuple T, and no prime
  below 1000 outside the list has a rank drop on any of the 625 tuples.
hypotheses: degree 5; the minor criterion (Thm 3.1 of arXiv:2411.13967) is
  unconditional; the rank-drop equivalence p | J_T <=> rank_{F_p}(M_T) < C
  is exact
evidence: verified-computationally — exact integer arithmetic (modular
  Gaussian elimination over F_p, no floating point); rank<->J_T equivalence
  itself validated at n=4 by two independent exact routes (SNF lcm and rank)
program: code/badprimes_criterion/verify_badprimes_n5.py
capture: code/out/badprimes_n5.captured.txt
anchor: research/sources/castryck2012_degree12_html.full.md (Thm 4, lines
  ~147-149); research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md (Thm 3.1)
falsifies: a listed prime with full rank 120 on every tuple, or a prime
  outside the list with a rank drop, computed by the same exact method
```

```claim
id: badprimes-n5-semantic-smallprimes
status: checked — reproduced by code/badprimes_criterion/semantic_n5_smallprimes.py:
  exhaustive enumeration of all p^5 monic degree-5 polynomials over F_p for
  p in {2,3,5,7,11,13} (552,551 polynomials, 28 workers, 85.4 s), each
  decided by the canonical oracle lib.casas_alvero.is_ca_hasse /
  is_pure_power (exact over GF(p)). Counterexample exists iff p in
  {2,3,7,11}: counts {2:2, 3:12, 5:0, 7:42, 11:110, 13:0}. Witnesses:
  x^5+x over F_2 (H_1=x^4+1, H_2=H_3=0, H_4=x, f=x(x+1)^4 not a pure
  power — hand-verified by explicit Hasse derivative computation),
  x^5+x^4+x^3 over F_3, and one each over F_7, F_11. Capture:
  code/out/badprimes_n5_semantic.captured.txt, exit 0.
holds-here: yes
statement: By the literal definition (Castryck et al. 2012 Def 1, Hasse
  formulation), p is a bad prime for degree 5 iff a counterexample exists
  over F_p. On the primes {2,3,5,7,11,13} this holds exactly at
  {2,3,7,11}, agreeing with the published degree-5 bad-prime list and with
  the rank-over-F_p criterion route (2,3,7,11 bad; 5,13 good).
hypotheses: degree 5; the published lists use the Hasse-derivative
  formulation (established in research/notes/ordinary-vs-hasse-badprimes.md)
evidence: verified-computationally — exact oracle decisions over GF(p), no
  floating point; the p=2 witness additionally hand-verified by explicit
  Hasse derivative computation
program: code/badprimes_criterion/semantic_n5_smallprimes.py
capture: code/out/badprimes_n5_semantic.captured.txt
anchor: research/sources/castryck2012_degree12_html.full.md (Def 1, Thm 4)
falsifies: a prime in {2,3,5,7,11,13} whose counterexample-count zero/nonzero
  contradicts p in {2,3,7,11}, computed by the same exact method
```

```claim
id: minors-criterion-feasibility-boundary
status: checked — reproduced by code/n5/feasibility_boundary.py (capture
  code/out/feasibility_boundary.captured.txt, exit 0) plus the re-run of
  code/badprimes_criterion/verify_badprimes_n5.py this attempt (384.1 s,
  ALL CHECKS PASSED). Parameters computed exactly; C,D cross-checked against
  lib.badprimes.lex_monomials. Cost model O(D*C^2) per-rank calibrated on the
  measured n=5 wall (0.1012 core-s/rank).
holds-here: yes
statement: The Schaub-Spivakovsky bad-prime-minors criterion has a hard
  computational wall at n=6: n<=4 is fully feasible by SNF (n=4: 19x15, 64
  tuples, lcm J_T=1575 -> bad primes {3,5,7}); n=5 is SNF-infeasible (one
  195x120 SNF > 90 s cap) but rank-over-F_p feasible (C=120, D=195); n=6 is
  rank-infeasible (C=1365, D=2751, ~185 core-s per rank, full n=6 sweep ~2.2e5
  core-hours); n=7,8 neither a fortiori. Consequence: the minor criterion
  cannot be used to test goodness of primes at n=20 (C = binomial(190,18) ~
  1e20, far past the n=6 wall); at n=20 only the SUFFICIENT binomial criterion
  p | C(20,i) - 1 is usable and it certifies bad (18 primes) but never good.
evidence: verified-computationally for n<=5 (exact rank over F_p); n=6,7,8 are
  magnitude extrapolations of the measured O(D*C^2) per-rank cost, labelled as
  such, not new verifications
program: code/n5/feasibility_boundary.py, code/badprimes_criterion/verify_badprimes_n5.py
capture: code/out/feasibility_boundary.captured.txt, code/out/badprimes_n5.captured.txt
anchor: research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md (Thm 3.1)
falsifies: an exact n=6 rank computation that finishes in reasonable time, or a
  smaller-wall n=6 measurement contradicting C=1365/D=2751
```

```claim
id: binomial-criterion-calibration
status: checked — reproduced by code/n5/binomial_calibration.py (capture
  code/out/binomial_calibration.captured.txt, exit 0, ALL CHECKS PASSED).
  Exact integer arithmetic via lib.badprimes.criterion_bad_primes (sympy
  binomial + factorint); true bad lists sourced from Castryck-Laterveer-
  Ounaies 2012 Thm 4 (n=5) and Sec 1.7 (n=3, n=4).
holds-here: yes
statement: The sufficient binomial bad-prime criterion (Schaub-Spivakovsky
  2023 Cor 8, arXiv:2307.05997: p bad for degree d if p | C(d,i) - 1 for some
  i in 1..d-1) is sufficient but never exhaustive. Against the true bad
  lists: n=3 certifies {2} of {2} (ratio 1.0); n=4 certifies {3,5} of
  {3,5,7} (missing {7}, ratio 2/3); n=5 certifies {2,3} of the 9 true bad
  primes, missing {7,11,131,193,599,3541,8009} (ratio 2/9 = 22%). Negative
  control: the first 10 good primes at each degree divide no C(n,i)-1 (30
  checks, the criterion never falsely condemns a good prime).
hypotheses: the binomial criterion (Cor 8) is a sufficient condition for a
  prime to be bad; the degree-3,4,5 true bad lists are as published
  (Castryck 2012 Thm 4 / Sec 1.7)
evidence: verified-computationally — exact integer arithmetic, no floating
  point; the criterion routine is the same one the n=20 frontier imports
program: code/n5/binomial_calibration.py
capture: code/out/binomial_calibration.captured.txt
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Cor 8);
  research/sources/castryck2012_degree12_html.full.md (Thm 4, Sec 1.7)
falsifies: a degree where the binomial criterion falsely condemns a known
  good prime, or an n=3,4,5 binomial-certified set differing from {2}/{3,5}/
  {2,3}, computed with the same exact method
```

## What this settles

The task `badprimes-n5-rank-mod-p` (TASKS.md): the n=5 bad-prime list is now
verified by two independent exact routes, and the boundary between the two is
recorded — enumeration (semantics) is feasible to p = 13 at degree 5; beyond
that only the criterion (rank route) remains feasible, which is exactly why
the criterion exists. The n=20 frontier program (certified_bad_frontier_n20.py)
is untouched: the binomial criterion there is sufficient only, and the full
minor criterion at n=20 is infeasible (C = binomial(190,18) ~ 10^20), so no
claim about degree 20 changes.
