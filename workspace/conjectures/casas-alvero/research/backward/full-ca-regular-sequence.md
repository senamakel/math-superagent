# Full CA via the regular-sequence / determinant criterion

The Ghosh–Schaub–Spivakovsky reformulation reduces Casas–Alvero to a statement
about explicit integer matrices. This skeleton decomposes that reduction: which
lemmas are already in the library (Macaulay, the lift theorem), which need only
to be banked (Ghosh's equivalence), and which is the conjecture itself in
determinant form, together with the finite, computable first instalment toward
it.

```skeleton
goal: Casas–Alvero (CA). Over any field K of characteristic 0, every monic
  f ∈ K[x] with deg f = n ≥ 1 satisfying gcd(f, f^{(i)}) ≠ 1 for all
  i = 1,…,n−1 is f = (x−a)^n for some a ∈ K̄.
implies: >
  Write CA_n,0 for the conjecture in degree n over char 0, and T for the set
  {1,…,n}^{n−1} of tuples T = (j_1,…,j_{n−1}). Let G_{T,i} = Φ_{j_i}(σ_i) be the
  i-th elementary symmetric polynomial in x_1,…,x_{n−1} after the involution
  Φ_j (x_j ↦ −x_j, x_i ↦ x_i − x_j for i ≠ j); deg G_{T,i} = i.
  (G-reformulation-equivalence) gives, for each n, CA_n,0 ⟺ R_n, where
  R_n := "∀T ∈ T: (G_{T,1},…,G_{T,n−1}) is a regular sequence in
  ℚ[x_1,…,x_{n−1}]" (equivalently √(G_{T,i}) = (x_1,…,x_{n−1})).
  (G-macaulay-rank) then gives, for each n and each T, the equivalences
  "regular sequence ⟺ m^d ⊂ I_T ⟺ rank_ℚ(M_T) = C ⟺ J_T ≠ 0", where
  d = (n²−3n+4)/2, C = binom(n(n−1)/2, n−2), M_T is the integer matrix of
  multiplication into the degree-d part, and J_T = gcd of all C×C minors.
  Chaining these pointwise over T and universally over n:
  (∀n: CA_n,0) ⟺ (∀n ∀T: J_T ≠ 0 in ℤ) =: the statement of
  (G-uniform-nonvanishing). So that one lemma proves the full conjecture.
  (G-bad-prime-extension) is the finite first instalment: it validates the
  J_T criterion against the published n ≤ 7 bad-prime lists, extends them to
  new base degrees, and via the lift theorem CA_{n,p} ⇒ CA_{np^ℓ,0}
  (Graf-von-Bothmer, carried in settled-classes) converts every newly found
  good prime p for base n into newly settled degrees np^ℓ.
  Char-0 break (the test every argument must pass): the identical chain over
  F_p reads CA_{n,p} ⟺ (∀T: J_T ≢ 0 mod p), i.e. p is a bad prime for n ⟺
  p | J_T for some T (Schaub–Spivakovsky Thm 3.1). The entire char-0 content
  of the argument is therefore the single integer statement J_T ≠ 0, and the
  step that must fail in char p is exactly the non-vanishing of the integer
  J_T: the char-p counterexamples are precisely the primes p dividing some
  J_T. No char-free step survives this decomposition unlabelled.
status: live
rests-on: charp-false (CA false in char p; fixes where the argument must break),
  settled-classes (Graf-von-Bothmer lift CA_{n,p} ⇒ CA_{np^ℓ,0}),
  research/sources/schaub_spivakovsky_bad-primes_2024.full.md (Macaulay Thm 2.1,
  rank/gcd criterion Thm 3.1, Ghosh Prop 5.2 quoted as Conj 1.6/1.7)
```

```gap
id: G-reformulation-equivalence
lemma: For every n, CA_n,0 holds iff for every T ∈ {1,…,n}^{n−1} the sequence
  (G_{T,1},…,G_{T,n−1}), G_{T,i} = Φ_{j_i}(σ_i(x_1,…,x_{n−1})), is a regular
  sequence in ℚ[x_1,…,x_{n−1}]. This is the equivalence Ghosh proved
  (arXiv:2402.18717, Prop 5.2), restated as Conj 1.6/1.7 in Schaub–Spivakovsky
  (arXiv:2411.13967, §1). It holds over any field regardless of characteristic,
  so it contributes no char-0 content — that is carried entirely by J_T ≠ 0.
status: open
next: extract the statement verbatim from research/sources/ghosh2024_finiteness_full.full.md
  and schaub_spivakovsky_bad-primes_2024.full.md, write the claim block with the
  exact Φ_j definition and the Hasse-vs-formal derivative convention, then
  sympy-verify both directions at n = 3, 4 against the exact oracle (in
  particular: a char-p witness must correspond to a prime p dividing some J_T).
```

```gap
id: G-macaulay-rank
lemma: For homogeneous forms of degrees 1,…,n−1 in n−1 variables over a field,
  the following are equivalent: (i) they form a regular sequence (equivalently
  √I = (x_1,…,x_{n−1})); (ii) m^d ⊂ I with d = Σ deg − (n−2) = (n²−3n+4)/2
  (Macaulay 1916); (iii) the degree-d multiplication matrix M_T has full rank
  C = binom(n(n−1)/2, n−2); (iv) J_T := gcd of all C×C minors of M_T is nonzero.
status: discharged
discharged-by: research/sources/schaub_spivakovsky_bad-primes_2024.full.md
  (Thm 2.1, the statement of Macaulay's theorem; Thm 3.1, the rank/gcd
  criterion), classical source: Macaulay, The algebraic theory of modular
  systems, 1916.
```

```gap
id: G-bad-prime-extension
lemma: The finite computation of J_T over ℤ for n ≤ 7 reproduces the published
  bad-prime lists (validating Thm 3.1 exactly), and for the first unclassified
  base degree n = 8 (then 9, 10 as far as feasible) it determines the full set
  of bad primes — the prime divisors of some J_T, T ∈ {1,…,n}^{n−1}. Each good
  prime p found at a new base n settles every degree np^ℓ by the lift theorem,
  a new partial result. This is a bounded computation, not an enumeration of
  polynomials: the search space is the finite index set T and the matrix
  minors, and its cost grows with n but is a genuine finite filter, not the
  full answer space.
status: open
next: tool_builder/symbolic_math: build M_T over ℤ with sympy for n = 4,5,6,7
  (matrix sizes 19×15, 195×120, 2751×1365, 49259×20349), compute J_T = gcd of
  all C×C minors, factor, and check the prime divisors against the published
  bad-prime lists for n ≤ 7; then attempt n = 8 (C = 376740, D ≈ 1.07e6) one
  T at a time across 28 workers, recording the wall clock at which the gcd
  stops terminating.
```

```gap
id: G-uniform-nonvanishing
lemma: For every n ≥ 1 and every T ∈ {1,…,n}^{n−1}, the integer J_T — the gcd
  of all C×C minors of the matrix M_T built from the translated elementary
  symmetric polynomials — is nonzero. Equivalently every prime is good for
  every degree; equivalently Conj 1.7 of Schaub–Spivakovsky. By the two
  discharged lemmas this is exactly CA, so it is the whole remaining content,
  now in the form of a single explicit ℤ-valued determinant-gcd statement.
status: open
next: read the factorisations produced by G-bad-prime-extension and hunt a
  structural law for J_T (which monomials of the G_{T,i} contribute to the
  minors, how J_T behaves under n ↦ n+1 and under n ↦ np^ℓ, whether
  J_T factorises through the symmetric-group orbits on T) that would support
  an induction on n; the first theorem_prover move is to formalise
  "J_T ≠ 0 ⟹ regular sequence" for a fixed small n against the Macaulay
  statement so any later induction has a kernel-checked base.
```
