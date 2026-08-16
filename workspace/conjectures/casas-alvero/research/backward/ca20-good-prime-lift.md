# CA in degree 20 via one good prime (reduction mod p + lift)

The smallest open degree is 20. This skeleton reduces CA_20,0 to a single
remaining task — exhibit one "good" prime — by chaining the reduction-mod-p
lift (already in the library) with the bad-prime/minors criterion (already in
the library). Everything except the good-prime search is discharged; the open
gap is the degree-20 conjecture in its sharpest finite form.

```skeleton
goal: CA_20,0 — over any field K of characteristic 0, every monic f ∈ K[x] of
  degree 20 that shares a non-constant factor with each of its first 19 Hasse
  derivatives H_1(f),…,H_19(f) is (x−a)^20. (The smallest open degree,
  smallest-open-degree.)
implies: >
  The load-bearing direction is the reduction-mod-p lift (G-lift): for any
  prime p, if no CA-polynomial of degree 20 exists over F̄_p (that is, CA_20,p
  holds), then CA_20,0 holds — the k=0 case of the Graf-von-Bothmer lift
  "no degree-d CA-polys over F̄_p ⟹ CA in degree d p^k for all k≥0, over
  char 0 and char p" (gvb-lift; equivalently the p-adic form
  pdic-valuation-method with n′=20 < p, so any p ≥ 23). The contrapositive is
  unconditional: a char-0 counterexample f has Res(f,H_i(f))=0 for each i,
  which reduces mod p to a char-p counterexample for every p; so absence in
  char p for one p forces absence in char 0.
  (G-minors-test) gives the exact test for "p good": p is a bad prime for 20
  iff p | J_T for some T ∈ {1,…,20}^{19}, where J_T is the gcd of all C×C
  minors of the explicit integer matrix M_T (bad-prime-minors-criterion,
  Schaub–Spivakovsky Thm 3.1, unconditional as a test). Hence p is good iff
  rank_{F_p}(M_T) = C for every T, with C = binom(190,18) ≈ 1.0×10^20.
  (G-upper-bound) — conditional on CA_20,0 — bounds every bad prime for 20 by
  C!·∏_{i=1}^{19} binom(i+18,18)·binom(d−i+18,18) with d = (20²−3·20+4)/2 = 172,
  so the good-prime search is in principle a finite filter.
  Therefore the single remaining content is (G-good-prime): exhibit one good
  prime p ≥ 23 for n = 20. Chaining (G-minors-test) then (G-lift):
  rank_{F_p}(M_T) = C for all T ⟹ CA_20,p ⟹ CA_20,0.
  (G-minors-boundary) names why the direct minors route cannot deliver
  (G-good-prime): the minors criterion tops out at n = 5 (n = 6
  rank-infeasible, minors-criterion-feasibility-boundary), and at n = 20 the
  search space is |T| = 20^19 ≈ 5.2×10^24 tuples × a C ≈ 10^20-rank test, so
  (G-good-prime) must beat that wall by scenario-type reduction or a finite
  certificate over a single F_p.
  Char-p break (the test every argument must pass): this decomposition is a
  mod-p method by construction, so char p is the working space rather than a
  pathology. The step that must break in char p is named exactly: J_T ≢ 0 mod
  p fails precisely at the bad primes p | J_T, which is where the char-p
  counterexamples x^{p+1}−x^p live. A candidate for (G-good-prime) that also
  works in every characteristic would prove CA_{20,p} for all p, hence (by the
  lift) no char-p counterexamples at all — refuted by charp-false — so any
  proposed (G-good-prime) argument must name the prime p where it is
  char-0-honest.
status: live
rests-on: gvb-lift (k=0 reduction-mod-p lift), pdic-valuation-method,
  bad-prime-minors-criterion, bad-prime-upper-bound,
  minors-criterion-feasibility-boundary, smallest-open-degree, charp-false
```

```gap
id: G-lift
lemma: For any prime p, CA_20,p (no degree-20 Casas–Alvero polynomial over
  F̄_p that is not a pure power) implies CA_20,0. This is the k=0 case of the
  Graf-von-Bothmer–Labs–Schicho–van de Woestijne lift: no degree-d CA-polys
  over F̄_p ⟹ CA in degree d p^k for all k ≥ 0 (char 0 and char p); and the
  p-adic form of Draisma–de Jong covers n = n′ p^e with n′ < p, here n′=20,
  e=0, p ≥ 23.
status: discharged
discharged-by: gvb-lift (peer-reviewed, Graf-von-Bothmer et al. 2007, quoted as
  Castryck Thm 3); pdic-valuation-method
```

```gap
id: G-minors-test
lemma: For n = 20, a prime p is bad iff p | J_T for some T ∈ {1,…,20}^{19},
  where J_T is the gcd of all C×C minors of the integer matrix M_T
  (C = binom(190,18)); equivalently p is good iff rank_{F_p}(M_T) = C for all
  T. This is the unconditional Schaub–Spivakovsky criterion (Thm 3.1) applied
  at n = 20.
status: discharged
discharged-by: bad-prime-minors-criterion
```

```gap
id: G-upper-bound
lemma: Conditional on CA_20,0, every bad prime p for 20 satisfies
  p < C! · ∏_{i=1}^{19} binom(i+18,18) binom(d−i+18,18), d = 172,
  C = binom(190,18), so the set of bad primes (equivalently the good-prime
  search) is finite and explicitly bounded.
status: discharged
discharged-by: bad-prime-upper-bound
```

```gap
id: G-minors-boundary
lemma: The direct minors/rank criterion is computationally infeasible at n = 20:
  it is SNF-feasible only to n ≤ 4, rank-over-F_p-feasible only to n = 5, and
  rank-infeasible already at n = 6 (C=1365, ~2.2e5 core-hours for the full
  sweep); at n = 20 the sweep is |T| = 20^19 tuples × a binom(190,18)-rank
  test. Hence G-good-prime must use a method that beats this wall.
status: discharged
discharged-by: minors-criterion-feasibility-boundary
```

```gap
id: G-good-prime
lemma: There exists a good prime for n = 20 — that is, some prime p ≥ 23 with
  CA_20,p (equivalently rank_{F_p}(M_T) = C for all T ∈ {1,…,20}^{19},
  equivalently p ∤ J_T for all T). By G-lift this single prime settles
  CA_20,0. This is the whole remaining content of the degree-20 problem.
status: open
next: Attack the smallest candidate-good prime p = 23 (the first prime not
  certified bad by the binomial criterion, badprimes-n20-certified-frontier).
  Concretely, a tool_builder/coder can: (i) re-derive the lift direction k=0 —
  for a random monic degree-20 f over ℚ with gcd(f,H_i(f)) ≠ 1, confirm
  Res(f,H_i(f)) ≡ 0 mod 23 for each i, so a char-0 counterexample forces a
  char-23 one; (ii) encode "∃ degree-20 f over F̄_23, not a pure power, with
  Res(f,H_i(f))=0 ∀i" by the scenario/rank formulation and run the elimination
  (Gröbner/resultant over F_23, or a SAT/SMT encoding of rank_{F_23}(M_T) < C
  for some T) on the first root-coincidence scenario, building on
  massri-degree20-no-3-recycled (three-recycled-roots already ruled out).
  This is the Castryck et al. n=12 template (scenario reduction + Gröbner in
  char p) carried to n = 20 at the first candidate prime, recording the wall
  clock and degree reached if it does not terminate.
```
