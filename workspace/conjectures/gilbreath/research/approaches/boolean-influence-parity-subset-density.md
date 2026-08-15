```approach
idea: Boolean-function complexity / Walsh–Fourier attack on the supply density — ν₂(q_n) = #{d ≤ n : Σ_{j⊆d} h_j odd} is a prefix-density of a "subset-sum parity" Boolean function, and the theory of influences (KKL) plus the classical half-of-all-subsets-are-odd fact gives a new certificate route for ν₂ ≥ c·n.
mechanism: |
  The adopted identity (dyadic-linear-complexity-supply) states
  ν₂(q_n) = #{d ∈ [1,n] : ζ(h)[d] = 1}, where ζ(h)[d] = Σ_{j⊆d} h[j] (mod 2)
  is the F₂ subset-zeta (Sierpinski/Pascal fold) of the mod-4 switch bit
  h[j] = [gap_j ≡ 2 (mod 4)]. This is a SUBSET-SUM PARITY problem: ζ(h)[d] is
  the parity of the sum of h over the submasks of d.

  Classical fact (trivial by Parseval over F₂^n): for ANY nonzero 0-1 vector
  h of length n, EXACTLY HALF of all 2^n subsets have odd subset-sum —
  #{j ∈ F₂^n : ⟨h,j⟩ = 1} = 2^{n−1}. The whole difficulty of the supply bound
  is that ν₂ does not range over the full boolean lattice: it ranges over the
  CHAIN d = 1,2,…,n (n ≪ 2^n), each d using only its own submasks. So the
  supply bound is a DISCREPANCY/PREFIX statement: does the first n chain
  elements of the subset-zeta sample the "half odd" property fairly?

  The new toolbox is the Fourier analysis of Boolean functions and influence
  theory (Bourgain, Kahn–Kalai–Linial, O'Donnell, Kalai). Over ℝ (not F₂),
  the subset-zeta restricted to the chain is the function
  g(d) = (1 − Π_{i⊆d} (1−2h_i))/2  — a monotone (read-once, "upward-closed")
  Boolean function of d, whose mean over the chain [1,n] is ν₂(n)/n. The
  conjecture needs mean(g) ≥ c. Monotone functions are controlled by their
  total influence: a monotone f with no dominant Fourier coefficient has bias
  bounded away from ±1 (KKL), i.e. mean(f) is bounded away from 0 and 1.
  Concretely: ν₂(n)/n is far from 0 as soon as the prime-gap-parity string h
  has no concentration in a small number of Walsh coefficients — exactly the
  kind of two-point correlation statement the run has already reduced to
  (ABGS / Hardy–Littlewood–Lemke Oliver–Soundararajan), but now with a
  certificate in the language of influences rather than a bare frequency
  assumption.

  Why this beats the refuted neighbours: the F₂ uncertainty attempt was
  refuted because Φ_n has trivial kernel (im = whole space), so no F₂ spectral
  content; but over ℝ the Pascal/Sierpinski matrix has non-trivial spectrum
  and the bias of g is governed by REAL Walsh coefficients of h, which are
  measurable and tied to known prime-gap correlation data. The target is a
  conditional theorem with a cleaner hypothesis (bounded real Walsh
  coefficients of h) and an unconditional partial result of the form
  "if h has no large Walsh coefficient then ν₂(n) = n/2 + O(√n)" — via the
  second-moment/discrepancy argument, not via linear lower bounds on prime
  frequencies.
status: refuted
killed-by: | Fails on its own falsifier (b), which IS the run's measured ground truth. The load-bearing identity g(d) = (1 − Π_{i⊆d}(1−2h_i))/2 = #{j⊆d: Σ h_j odd} counts the ZEYA (subset-zeta) F2-parity of the mod-4 switch bit; and the run has measured that this parity count is NOT the real ν₂ (the number of cells of the right diagonal exactly 2). The fold bit zeta(h)[d] is mod-4 parity — it fires on halved values odd (2,6,10,…), NOT on cells exactly 2. Ground-truth: Thue–Morse h gives TM nu2(100)=27 but the fold count is 7, first mismatch at n=1 (claim thue-morse-sublinear-supply-witness; reconciled in dyadic-oddfactor-density-exact / thue-morse data). So the premise that the {0,2}-suffix count equals the subset-sum-parity prefix density ν₂(n)=#{d≤n: ζ(h)[d]=1} is FALSE, and the entire KKL/influence certificate — which reasons about the bias of that Boolean function g on the chain — certifies the wrong quantity: it bounds a parity count that is not A_k(1)∈{0,2}. The classical half-of-subsets-are-odd fact and KKL (Kahn–Kalai–Linial; monotone-function oracles, O'Donnell–Wimmer; Bourgain) are real and correct as stated, but they bound a full-lattice mean that the chain d=1..n does not sample uniformly, and the quantity that would make the transfer valid (the exact {0,2} count) is not expressible as such a Boolean-function bias. Independently: the run already holds the correct conditional supply statement — the real mod-4 SWITCH count (which feeds a WORKING ν₂ relation ν₂≥c·n at the measured ν₂/w∈[0.689,0.867]) reduces to the ABGS 2011 §9 two-point consecutive-prime mod-4 correlation, named-open (abgs-2011-s9-mod4-switch-limit-open). That is the honest self-consistent certificate; this Boolean-influence transcription of it does not add a route and would, if pursued, certify the parity of the wrong object.
precedent: https://doi.org/10.48550/arxiv.2404.00084 (Przybyłowski 2024, joint-influence KKL); https://doi.org/10.1137/100787325 (O'Donnell–Wimmer 2013, KKL/Kruskal–Katona/monotone bounds); https://doi.org/10.1214/ecp.v18-1961 (O'Donnell–Wimmer 2013, sharpness); <https://escholarship.org/uc/item/004616km> not needed; claims thue-morse-sublinear-supply-witness (STATED-measured: fold-parity ≠ real ν₂, first mismatch at n=1), abgs-2011-s9-mod4-switch-limit-open (the real mod-4 switch count is two-point and named-open), dyadic-oddfactor-density-exact (fold-only densities; but ground-truth ν₂ is what supply needs), dyadic-linear-complexity-supply (the adopted identity that states ν₂=#{ζ=1} — which the ground-truth measurement REFUTES as stated, real ν₂ is not the parity count).
side: supply-side / prime-gap-mod-4
named-mathematics: Fourier analysis of Boolean functions; the KKL theorem and
  influence theory (Bourgain, Kahn–Kalai–Linial); Walsh–Hadamard transform;
  the classical subset-sum parity fact; Parseval over F₂^n and over ℝ.
speculative: MEDIUM — the chain d=1..n is not a uniform sample of the boolean
  lattice, so the full-lattice "half odd" fact does not directly give ν₂; the
  honest content is to derive the prefix-discrepancy bound from a real-Walsh
  concentration hypothesis on h, which may reproduce (not beat) the existing
  ABGS/HL conditional route. That reproduction, in influence language, is
  still a distinct certificate and may yield the O(√n) unconditional-format
  bound.
falsifier: (a) a measurable counterexample where h has no large Walsh
  coefficient yet ν₂(n)/n → 0 (would refute the KKL transfer); (b) the
  identity g(d) = (1 − Π_{i⊆d}(1−2h_i))/2 failing against the oracle ν₂ (it
  must hold exactly, mod 2 parity of the product is the same bit); (c) the
  real Walsh coefficients of the prime h turn out concentrated (then the
  hypothesis is not met and the route is vacuous for primes).
first-step: |
  1. Compute the real Walsh coefficients of the prime-gap-parity string h
     over n up to a stated depth (oracle, exact), and confirm the subset-zeta
     identity ν₂(n) = #{d ≤ n : Σ_{j⊆d} h_j odd} reproduces the run's
     measured ν₂ (0 violations expected — this is the adopted identity).
  2. Compute the bias/mean of g(d) over the chain [1,n] and its Fourier
     coefficients over the chain (Dirichlet-style), and measure whether the
     largest Walsh coefficient of h is o(1) — the hypothesis check.
  3. Derive the second-moment identity Var of the prefix sum = Σ Walsh
     coefficients squared, and state the precise conditional theorem
     "no large Walsh coefficient ⟹ ν₂(n) = n/2 + O(√(n log n))".
  4. Report the hypothesis as met/unmet on the real h, and whether the
     derived bound is a theorem or a numerical fit (never "proved" without
     a proof).
```
