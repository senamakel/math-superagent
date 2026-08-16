# Spacetime diagonal / Furstenberg: ν₂(n) as a diagonal of the fold array

```approach
idea: >
  Treat ν₂(n) = wt(Φ_n h) as the anti-diagonal row-sum of the 2-D fold spacetime
  A_k(i) — the Gilbreath triangle reduced mod 2. The array satisfies the EXACT
  lattice rule A_{k+1}(i) = A_k(i) + A_k(i+1) over F₂ (the F₂ reduction of
  |a−b| is a+b), so its bivariate generating function F(x,y) = Σ_{k,i} A_k(i) x^k y^i
  obeys a functional equation whose "kernel" is rational; the prime-parity string
  enters only as the boundary series B(y) = Σ_i A_0(i) y^i. The sequence ν₂(n)
  is a linear functional of the ANTI-DIAGONAL of this array, i.e. a DIAGONAL of a
  bivariate series. Named engines: Furstenberg's theorem (the diagonal of a
  rational bivariate series is algebraic) and the Flajolet–Odlyzko singularity
  growth dichotomy (an algebraic integer sequence growing o(n) on a positive-density
  set is eventually periodic). The route therefore reduces SUPPLY's contrapositive
  to: "ν₂(n) algebraic + sublinear on a density-1 set ⇒ ν₂ eventually periodic",
  which contradicts measured non-periodicity (and the primes' non-automaticity,
  Coons/Dubbe).
mechanism: >
  (1) The lattice relation A_{k+1}(i) = A_k(i) + A_k(i+1) mod 2 is EXACT and is
  the same relation that makes Φ_n = (1+σ)^d; this is the whole of the fold, and
  unlike the refuted `substitution-incidence-perron` (whose 2×2 substitution rules
  are FALSE) and the refuted `pascal-cascade-block-recursion` (block recursion on
  the slice), nothing here is conjectural — the array rule is an identity.
  (2) Anti-diagonal extraction is the standard Hadamard/diagonal operation on a
  bivariate series; the row-sum ν₂(n) = Σ_{k=2}^{n−1} A_k(n−1−k) is a further
  linear functional of the diagonal, so if F is rational/2-regular then ν₂(n) is
  an ALGEBRAIC sequence (Furstenberg). (3) The growth dichotomy for algebraic
  sequences (integer coefficients, o(n) on a set of positive upper density) forces
  an eventually-periodic branch; so a sublinear ν₂ would make the prime-driven
  fold sequence eventually periodic, which the data and the non-automaticity of
  the prime indicator rule out. (4) This is a change of ground from
  `diagonal-2regular-automaton` (refuted): that route mounted Walnut/2-regularity
  of a RUN-LENGTH transform; this route mounts the DIAGONAL-OF-RATIONAL functional
  equation and the ALGEBRAIC growth classification, which is a strictly richer
  class than 2-regular and has a clean sublinear-growth dichotomy.
status: refuted
killed-by: >
  Furstenberg's hypothesis fails: the diagonal-of-a-rational-series theorem
  needs F(x,y) RATIONAL, which over F₂ forces the boundary coefficient sequence
  to be eventually periodic; the boundary that actually produces ν₂(n)=wt(Φ_n h)
  is the non-rational prime gap-parity string h (linearisation-fold-weight), and
  h periodic would make the primes periodic (contradiction, Shiu 2000 / non-
  automaticity of primes). The rational boundary the mechanism names is the
  raw-primes-mod-2 string, which is essentially constant and gives the trivial
  (incorrect) object, not the gap-parity fold. So Furstenberg never engages;
  the route lands on the same non-automaticity wall that closed
  diagonal-2regular-automaton. The secondary growth-dichotomy step
  ("algebraic + sublinear on density-1 ⇒ eventually periodic") is not a stated
  theorem, but the rational-boundary obstruction decides independently.
precedent: >
  (verdict: refuted) — The engine is real and precisely stated: Pólya (1922, the
  first proof that the diagonal of a bivariate rational power series is
  algebraic) and Furstenberg (1967, the general theorem + converse): a univariate
  f ∈ K[[t]] is algebraic iff it is the diagonal of a bivariate rational power
  series (confirmed in Bostan–Lairez–Salvy, "Multiple binomial sums",
  J. Symbolic Comput. 2016, DOI 10.1016/j.jsc.2016.04.002, Thm 3.2; Bostan–Dumont–
  Salvy, "Algebraic diagonals and walks", JSC 2016, DOI 10.1016/j.jsc.2016.11.006;
  Y. Hu, "Coefficient extraction and Furstenberg's theorems", arXiv:1505.01379).
  These are exactly-statable, and the "diagonal ⟹ algebraic" direction is
  unconditional. But the hypothesis Furstenberg needs — RATIONALITY of F(x,y) —
  fails here, because over F₂ a rational formal power series has eventually
  periodic coefficients, and the boundary that actually produces ν₂(n)=wt(Φ_n h)
  is the non-rational prime gap-parity string h (linearisation claim
  linearisation-fold-weight). h not eventually periodic is established
  conditional on Shiu 2000 (problem.md (5)); the non-automaticity of the prime
  indicator is sourced: Hartmanis–Shank 1968, DOI 10.1145/321466.321470; Coons,
  arXiv:0810.3709; Dubbe, arXiv:2409.04314. In-workspace: the already-refuted
  diagonal-2regular-automaton approximates this route and closed on the same
  non-automaticity wall; claims linearisation-fold-weight,
  rw-not-the-submask-xor-fold; ROOT.md verification bound n=8000, pointwise
  ceiling N=40000.
first-step: >
  tool_builder, exact integer/F₂ arithmetic: (1) DERIVE the exact functional
  equation of F(x,y) from A_{k+1}(i) = A_k(i)+A_k(i+1) with boundary B(y), and
  machine-verify it against the brute submask-XOR oracle for all (k,i), n ≤ 64;
  (2) EXTRACT the anti-diagonal coefficient of ν₂(n) as a linear functional of the
  diagonal and confirm it reproduces the canonical values ν₂(53)=18, ν₂(64)=27,
  ν₂(4000)=1975; (3) STATE precisely, from Flajolet–Odlyzko or the algebraic-
  sequence literature, the theorem "algebraic + sublinear on a positive-density
  set + integer coefficients ⇒ eventually periodic", and check its hypotheses
  against what (1)+(2) produce. FALSIFIER: if the theorem as stated is wrong, or
  if the prime boundary B(y) provably cannot make F rational/2-regular (the honest
  gap — the prime-parity series is non-automatic), the route dies with the transfer
  gap recorded. Either outcome pins the boundary-rationality question, which no
  closed route has priced.
falsifies: >
  (a) the functional equation is wrong (then the array rule was misread); (b) the
  "algebraic + sublinear ⇒ eventually periodic" dichotomy is not a theorem (then
  the engine does not exist); (c) the prime boundary cannot be made rational /
  2-regular, so Furstenberg does not apply and the route only yields the
  non-automaticity wall again — recorded as the precise transfer gap.
```
