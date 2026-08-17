# CA via the weighted-torus structure of the resultant scheme

This skeleton uses the run's strongest freshly-proved content — each Hasse
resultant `R_i = Res_x(f, H_i f)` is weighted-homogeneous of weight `n(n−i)`
for all `n` — to collapse the Casas–Alvero conjecture to a single
0-dimensionality statement about an explicit ideal. The reduction is genuinely
new (it is not the `J_T ≠ 0` determinant form of the other skeleton, though it
lands on the same open content), and its char-0-only step is locatable: the
weighted homogeneity is char-free, but the nonzero-ness of the integer
resultants, and hence the survival of the order, is a char-0 fact.

```skeleton
goal: Casas–Alvero (CA): over any char-0 field K, every monic f of degree n sharing a factor with each of its first n−1 Hasse derivatives is (x−a)^n.
implies: Traceless slice A=Q[a_2..a_n], w(a_j)=j, R_i=Res_x(f,H_i f), I=(R_1..R_{n−1}). Two discharged lemmas: (G-resultant-scheme) CA ⟺ sqrt(I)=m_0 ⟺ V(I)={0} (char-free); (G-weighted-order) each R_i is weighted-homogeneous of weight n(n−i) and nonzero over Q (Theorem A char-free, Lemma B char-0), so I is T-homogeneous and V(I) is T-invariant with the torus's only fixed point = origin. Single open lemma (G-torial-zero-dim): dim A/I=0 for all n. Inference: finite T-invariant V(I) is a union of T-orbits; a non-fixed point has an infinite G_m-orbit, impossible in a finite set, so V(I)={0}, hence CA_n. Universal over n gives full CA. So CA ⟺ ∀n dim A/I=0 — same content as J_T≠0 but with the handle that the sought exponent is governed by the known weights n(n−i) rather than total degree. Char-0 break (admissibility): reduction is char-free; in char p it reads CA_{n,p} ⟺ dim A_p/I_p=0; the content-degeneracy of integer resultants (e.g. R_{n−1}=(−1)^n n^n a_n vanishes mod p when p|n) makes this premise fail at bad primes, which is exactly the bad-prime phenomenon.
killed-by: 
rests-on: ord0-resultant-weighted-order-proved-all-n (Theorem A + Lemma B), resultant-reformulation (CA ⟺ V(I)={0}, char-free), charp-false, minors-criterion-feasibility-boundary
status: live
```

```gap
id: G-torial-zero-dim
lemma: For every n ≥ 1, the ideal I = (R_1,…,R_{n−1}) ⊂ A = ℚ[a_2,…,a_n], where
  R_i = Res_x(f, H_i f) with f = x^n + Σ_{j=2}^n a_j x^{n−j} (monic traceless),
  satisfies dim A/I = 0 — equivalently V(R_1,…,R_{n−1}) is finite, equivalently
  some power of each a_j lies in I, equivalently m_0^M ⊂ I for some M,
  equivalently CA. Given the two discharged lemmas above this is exactly the
  Casas–Alvero conjecture in degree n, stated as a 0-dimensionality of an
  explicit ideal whose generators have known weighted degrees n(n−1),…,n.
  The structure this skeleton adds: because the generators are weighted-
  homogeneous with known weights, the sought exponent is governed by the
  weights — if V(I) is finite then weighted homogeneity alone forces V(I) = {0}
  (torus fixed space), so the single task is finiteness.
status: open
next: keep pushing the quotient-dimension / coordinate-nilpotency computation
  already begun (n=4,5,6,8 give vdim = n^(n−2) and explicit nilpotent
  exponents a_2^19, a_3^13, a_4^10, a_5^1 ∈ I at n=5) and seek the *weighted*
  law: from ord_0(R_i) = n(n−i), predict the nilpotency exponent e_j of a_j in
  A/I (conjecturally e_j should sit near the weighted-homogeneous bound
  n(n−1−j) or the Macaulay d = (n²−3n+4)/2, whichever is sharper), verify it
  exactly for n=4,5,6,7,8 with Singular (dp/grevlex-weighted order — sympy's
  grevlex is known incomplete at n≥5 per CONTEXT.md) and record whether the
  exponent follows a uniform formula in n,j. A theorem_prover move: formalise
  "dim A/I = 0 ⟹ (weighted-homogeneity ⟹ V(I)={0})" once, so a proof of
  finiteness for a given n immediately jaws CA_n. First concrete move today:
  for n=6 compute the nilpotency exponents of a_2,…,a_6 in A/I and check them
  against n(n−1−j) and against d = (n²−3n+4)/2; if e_j = n(n−1−j) holds
  uniformly in the computed range it is the weighted law to prove by induction
  on n, which is the strongest first instalment of G-torial-zero-dim.
```

```gap
id: G-resultant-scheme
lemma: f = x^n + Σ_{j=2}^n a_j x^{n−j} (monic, traceless, a shared root of
  H_{n−1} translated to 0) is a Casas–Alvero polynomial iff (a_2,…,a_n) lies in
  V(R_1,…,R_{n−1}) ⊂ ℚ^{n−1}; and CA_n,0 over any char-0 field K is equivalent
  to √I = (a_2,…,a_n), i.e. V(I) = {0}. Truth depends only on char K, not on K
  (faithfully flat extension).
status: discharged
discharged-by: resultant-reformulation (Schaub–Spivakovsky bad-primes §1),
  verified via ca-variety-results / lu-2017 / the run's oracle
next: none — already in the library as a resolved claim
```

```gap
id: G-weighted-order
lemma: In the traceless slice, each R_i = Res_x(f, H_i f) is exactly
  weighted-homogeneous of weight n(n−i) under w(a_j) = j (Theorem A, char-free,
  Sylvester determinant monomial weights), and R_i is nonzero over ℚ (Lemma B,
  root-form product in the integral domain ℚ[β_1,…,β_{n−1}]/(Σβ)). Hence
  ord_0(R_i) = n(n−i) exactly for all n ≥ 3, i ∈ {1,…,n−1}; and I is
  T-homogeneous so V(I) is T-invariant with T-fixed space = {0}. This is the
  char-0 premise: over F_p the integer resultants can collapse by content (e.g.
  R_{n−1} = (−1)^n n^n a_n vanishes identically when p|n), which is exactly the
  bad-prime phenomenon.
status: discharged
discharged-by: ord0-resultant-weighted-order-proved-all-n (Theorem A + Lemma B,
  proved; exact checks n=3..8 in code/out/verify_*.captured.txt)
next: none — proved for all n in research/notes/weighted-order-theorem.md
```
