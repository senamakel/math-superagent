# SUPPLY via an input strictly weaker than switch density (the fold does work)

Reduction of the goal to three lemmas. This is the **positive** branch of the
central hypothesis under test (GOAL.md): that the fold `Φ` forces a linear lower
bound on `ν₂` from an arithmetic input on the prime gap-parity string that is
strictly weaker than positive mod-4 switch density. Rival of
`switch-equivalence.md`; at most one of the two can be discharged.

```skeleton
goal: (SUPPLY) There is c > 0 with ν₂(n) = wt(Φ_n h) ≥ c·n for all sufficiently
  large n, established from an arithmetic input C(h) on the prime gap-parity
  string h that is strictly weaker than positive mod-4 switch density.
implies: Linearisation (problem.md, imported) gives ν₂(n) = wt(Φ_n h). By
  lucas-submask-odd, wt(Φ_n h) = |{ d ∈ [0,n) : T(d)=1 }| where T(d) = ⨁_{i⊆d} h(i)
  is the submask-XOR vector — the image coordinate the fold Φ reads at depth d.
  Lemma G-weak-input-submask-density supplies a condition C(h), stated only in the
  coordinates T(d), with C(h) ⇒ |{d<n : T(d)=1}| ≥ c·n for all n ≥ N₀.
  Lemma G-weak-input-primes-satisfy-C establishes that the real prime gap-parity
  string h satisfies C(h). Chaining the two gives ν₂(n) ≥ c·n for all n ≥ N₀,
  which is SUPPLY. Lemma G-weak-input-strictness exhibits a string h* with switch
  density 0 that satisfies C(h*), so by the first lemma ν₂(h*) ≥ c·n while the
  frequency form sees nothing: this proves C is strictly weaker than positive
  switch density, i.e. the fold contributes work the switch-density reduction
  discards. Without G-weak-input-strictness the skeleton would only re-derive the
  known (dead-end) reduction.
status: sketched
rests-on: lucas-submask-odd, C-fold-generic-expectation,
  lucas-mixing-iff-fold-randomization
```

```gap
id: G-weak-input-submask-density
lemma: There exists a condition C(h), stated entirely in the submask-XOR
  coordinates T(d) = ⨁_{i⊆d} h(i) that Lucas makes Φ_n read, such that C(h)
  implies |{ d < n : T(d) = 1 }| ≥ c·n for all sufficiently large n, and C is not
  implied by any of the five closed-door hypotheses (weight, no-constant-runs,
  aperiodicity, anti-dyadicity, periodicity).
status: open
next: Enumerate which submask-XOR patterns force a positive density of odd depths
  from the Lucas row structure. Concrete first move for tool_builder + sat_solver:
  build Φ_n over F₂ for n = 8..64, and search over candidate conditions
  C(h) = "all coordinates T(d), d in a chosen family S ⊆ {0..n−1}, are nonzero",
  finding the minimal such S for which the image {T : T = Φ_n h, T|_S fixed} still
  has weight ≥ c·n. Run the three negative controls through every candidate
  (all-ones, Thue–Morse, balanced anti-dyadic strings) and confirm they violate C
  — a candidate any one of them satisfies is a closed door reopened. This is rung
  R-submask-sufficiency of research/weakened/supply.md. The sourced claim
  lucas-mixing-iff-fold-randomization supplies the candidate (Lucas mixing) and its
  sharpness at density-one times but NOT the finite-prefix pointwise weight bound;
  that transfer is exactly what this gap must provide.
```

```gap
id: G-weak-input-primes-satisfy-C
lemma: The real prime gap-parity string h[j] = ((q_{j+1}−q_j)/2) mod 2 satisfies
  the condition C(h) of G-weak-input-submask-density. Equivalently: there is a
  provable arithmetic input on h — a bounded-autocorrelation bound, a
  second-moment/variance bound, a Walsh-coefficient bound, or an input along
  binary-submask sets — that implies C(h), and this input is unconditional (or at
  worst conditional on Shiu 2000, held abstract in problem.md).
status: open
next: This gap is the arithmetic heart and its next move can run today,
  independent of which C is eventually fixed. tool_builder: compute the empirical
  Walsh coefficients and lagged autocorrelations of the prime gap-parity string h
  for n up to 10^6, and for each candidate input named in GOAL.md priority 2 record
  the measured value and the threshold C(h) would demand. Then lean_prover:
  formalise the implication "named arithmetic input ⇒ C(h)" once G-weak-input-submask-density
  fixes C, with #print axioms and no sorryAx. If the only input that implies C is
  positive switch density itself, the honest output is the rival skeleton
  switch-equivalence.md (GOAL priority 3), not a claim of the weak-input route.
```

```gap
id: G-weak-input-strictness
lemma: There is a binary string h* with switch density 0 (the density of its
  1-coordinates is 0; h is the indicator of gaps ≡ 2 mod 4, so this says
  mod-4-switch pairs have density 0) that satisfies C(h*). By
  G-weak-input-submask-density this gives ν₂(h*) ≥ c·n while the frequency form
  sees nothing — the fold has a linear-weight image on a sparse input, which is
  the positive resolution of the hypothesis under test.
status: open
next: sat_solver / tool_builder: for n = 8..64, encode "∃ h ∈ F₂^n with wt(h) ≤ δn
  and wt(Φ_n h) ≥ εn" as a CP-SAT/SAT instance over a grid of (δ, ε) with δ→0, and
  report SAT witnesses or UNSAT thresholds. If a sparse witness exists at every
  reachable n, that is G-weak-input-strictness; if instead the maximum fold weight
  over k-sparse inputs is sublinear in n uniformly in k/n, that is exactly the
  rival gap G-eq-sparse-fold-is-sublinear and this skeleton dies with the reason
  recorded. The two directions are the same finite computation, so this gap and
  the rival's gap share one first move.
```
