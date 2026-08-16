# The fold collapses exactly the ×2-invariant inputs — Furstenberg measure rigidity against the dyadic odometer

```approach
idea: >
  All five closed doors share one hidden invariant, invisible to "h is
  complicated enough": the collapse witnesses (all-ones, Thue–Morse, balanced
  anti-dyadic, 2-regular, eventually-periodic-with-power-of-two period) are all
  inputs whose empirical measure is INVARIANT under the ×2 (dyadic odometer)
  map. The fold Φ = 1+σ (Rule 90) is the difference operator of the dyadic
  group, so its kernel and low-weight image are exactly the ×2-invariant
  measures. This repositions SUPPLY in the category where the statement is
  native: measure rigidity on the 2-adic odometer. The single arithmetic input
  needed is that the prime measure is NOT ×2-invariant — a disjointness/rigidity
  statement of exactly the kind Furstenberg's ×2×3 theorem and its modern
  descendants (Rudolph–Johnson, Host, Hochman–Shmerkin) prove — and it is
  provably true for the primes at low complexity by Dirichlet equidistribution
  mod 2^k.

mechanism: >
  Change of ground: instead of bounding wt(Φ_n h) through h's complexity, ask
  which MEASURES the fold collapses. The kernel ker Φ_n = span(even-alt,
  odd-alt) (claim fold-rank-n-minus-2-binomial-proved, proved) consists of the
  parity-class-constant strings, i.e. the eigenfunctions of the ×2 map on the
  odometer; every low-weight-image witness on disk is 2-automatic, hence its
  empirical measure is ×2-invariant. So the obstruction "Φ has low-weight
  images on rich inputs" reads as: Φ collapses exactly the ×2-invariant inputs.

  The rigidity engine is named: Furstenberg's ×2×3 theorem (a Borel probability
  measure on R/Z invariant and ergodic under both ×2 and ×3 is Lebesgue),
  Rudolph–Johnson (×p, ×q rigidity), Host, and Hochman–Shmerkin (measures
  invariant under a non-lacunary multiplicative semigroup are homogeneous).
  The primes provide the non-×2 structure through DIRICHLET, not through
  unproved correlation: primes equidistribute mod 2^k for every k
  (Siegel–Walfisz), so their empirical measure on Z₂ is the odd-concentrated,
  then residue-uniform measure — NOT ×2-invariant. In fact the value-domain
  prime measure is *spread* across the dyadic odometer, which is the
  anti-collapse input.

  The priced arithmetic input is therefore a single rigidity fact: the
  prime-gap-parity measure is disjoint from the ×2 (dyadic) system, equivalently
  it has no nontrivial ×2-invariant factor. This is orthogonal to the mod-4
  switch-density mean (it constrains the measure's factor structure, not the
  one-point frequency), does not reopen the five doors (their witnesses are
  ×2-invariant by construction and are the model collapse), and is the natural
  host for a theorem because the ×2 map is exactly what Lucas' theorem makes Φ
  read.

status: refuted

precedent:
  - "Furstenberg, Disjointness in ergodic theory, minimal sets, and a problem
    in Diophantine approximation, Math. Systems Theory 1 (1967) 1–49. THEOREM:
    for p,q multiplicatively independent rationals, no infinite proper closed
    subset of [0,1) is simultaneously ×p- and ×q-invariant (the topological
    ×2×3 result). Measure rigidity (the ×2×3 CONJECTURE) is NOT proved in
    general and remains open."
  - "Rudolph, ×2 and ×3 invariant measures and entropy, Ergodic Theory Dynam.
    Systems 10 (1990) 395–406, DOI 10.1017/S0143385700005681. THEOREM (Rudolph):
    for p,q relatively prime, if μ is ×p,×q-invariant and ergodic for the
    semigroup, and some r∈<p,q> has positive entropy, then μ=λ (Lebesgue).
    Needs BOTH maps and POSITIVE entropy of the semigroup action."
  - "Johnson: extends Rudolph to multiplicatively independent p,q.
    Host, Parry: alternate entropy-based proofs."
  - "Hochman & Shmerkin, On Furstenberg's intersection conjecture,
    arXiv:1508.04145, and Shmerkin's Annals 2019 convolution result
    (DOI 10.4007/annals.2019.189.2.1): rigidity for measures invariant under
    ×p and ×q (multiplicatively independent bases)."
  - "Lindenstrauss survey, Invariant measures for multiparameter diagonalizable
    algebraic actions, DOI 10.4171/009-1/16 (2019 reissue)."
  - "On-disk: fold-rank-is-n-2-nullity-2-alternating (checked),
    fair-model-exact-binomial (PROVED: uniform h on F2^n has wt(Phi_n h) ~
    Binomial(n-2,1/2), linear with high probability), g-run-telescope-verified
    (checked), takei-rule90-mixing-limits-uniform (asserted)."
killed-by: >
  The central claim — 'the fold collapses exactly the ×2-invariant inputs; the
  collapse witnesses are ×2-invariant, and ×2-invariant ⇒ collapse' — is FALSE
  in the direction the argument needs. By the PROVED fair-model fact, the
  UNIFORM (×2-invariant, Haar) measure on the 2-adic odometer is NOT a collapse
  input: wt(Phi_n h) for h uniform is exactly Binomial(n-2,1/2) (claim
  fair-model-exact-binomial, proved from rank Phi_n=n-2), so a μ-generic ×2-
  invariant string has LINEAR fold weight with probability
  1-exp(-c n). Hence ×2-invariance does NOT force low fold weight — the
  equivalence 'collapse ⟺ ×2-invariant' fails in the WRONG direction from the
  one SUPPLY needs. (The collapse witnesses are ×2-invariant, but ×2-invariance
  is far from sufficient for collapse: the invariant measure is the paradigm
  NON-collapse input.) Second independent defect: the rigidity engines named
  (Furstenberg ×2×3, Rudolph–Johnson, Hochman–Shmerkin) ALL require TWO
  multiplicatively independent maps (×2 and ×3, or ×p and ×q with log p/log q
  irrational); here there is a SINGLE map ×2 on the dyadic odometer, and a
  single ×2-invariant measure is as unstructured as a Bernoulli shift (uniform
  in the additive/dyadic coordinates), with no rigidity at all. The measure
  rigidity that forces a measure to be Haar is exactly the statement that needs
  the second, independent direction of expansion; one map gives the candidate
  nothing to rigidity against. Third, the candidate's only real input is
  'the prime measure is not ×2-invariant' (Dirichlet equidistribution mod 2^k,
  classical), but that input is already avail-slave and — being about the ODD-
  residue structure of the value-domain prime distribution, not about the
  INDEX-domain gap-parity string h — it is not the input the fold reads, and
  its transfer to wt(Phi_n h)≥c·n (the candidate's own open-step) needs the same
  absent finite transfer that killed lucas-mixing and every ergodic route.
  Verdict: the world is real and the rigidity theorems are exactly as stated,
  but neither they (two-map requirement) nor the ×2-invariance reading of
  collapse (fair-model counterexample) supports the mechanism.
open-step: >
  The quantitative transfer from "prime measure is not ×2-invariant" to
  "wt(Φ_n h) ≥ c·n on a density-1 set". Measure rigidity gives qualitative
  disjointness of the measure from the dyadic system; SUPPLY needs a FINITE,
  quantitative bound on the fold weight of a finite prefix. This is the same
  shape of finite-prefix transfer the adopted lucas-mixing route lacks, but now
  on the rigidity side, where quantitative/effective statements exist for
  Furstenberg's theorem. The open step is to state the effective form:
  a measure δ-far from ×2-invariance has fold weight ≥ c(δ)·n. If such an
  effective rigidity theorem exists or is provable, SUPPLY follows from the
  single classical input (Dirichlet), closing GOAL priority 2 at the cheapest
  price yet.
first-step: >
  research + tool_builder in parallel. (1) research: locate the exact statement
  and any EFFECTIVE/quantitative form of Furstenberg ×2×3 / Rudolph–Johnson /
  Hochman–Shmerkin rigidity — specifically whether "μ is ε-far from ×2-invariant"
  yields a quantitative bound on the weight of Φ_n applied to a μ-generic
  string. (2) tool_builder: compute the empirical measure of the prime-gap-parity
  string h over windows of length 2^m (m ≤ 12) and measure its distance to the
  nearest ×2-invariant measure (a finite convex feasibility check); confirm the
  primes are ε-far from ×2-invariance with ε bounded away from 0, while
  all-ones, Thue–Morse and anti-dyadic witnesses have distance 0 — the negative
  control that must show collapse at distance 0. (3) If the effective rigidity
  statement is located, hand the quantitative bound to a theorem pass; if it is
  absent, the route's open step is a genuinely new effective-rigidity theorem,
  stated precisely, for another school to grind out.
```

## Distinctness and honesty

- **Not any of the five closed doors:** those were hypotheses on h's weight, runs, aperiodicity, anti-dyadicity, periodicity — all "h is complicated enough". This route's input is a *measure-rigidity* property of the prime measure (disjointness from ×2), proved at low complexity by Dirichlet, and orthogonal to every door.
- **Not** `hypergraph-cut-cheeger` (refuted): that was connectivity/isoperimetry of the fold's hypergraph. This is measure rigidity of the *input*, a different world.
- **Not** `lucas-mixing-finite-transfer` (adopted): that uses Pivato–Yassawi's CA-randomization characterization (the CA's action on measures). This uses Furstenberg-type rigidity of the measure itself against the dyadic map — a different theorem family, with the specific advantage that the arithmetic input (non-×2-invariance) is classical, not conjectural.

**Speculative half:** the effective form "ε-far from ×2-invariance ⇒ fold weight ≥ c(ε)n" is NOT in the cited sources to the run's knowledge; it is the candidate's own conjecture to be priced. This is stated, not hidden. If the effective form does not exist, the route's deliverable is its precise statement as a new effective-rigidity question — itself a result worth a school's effort.
