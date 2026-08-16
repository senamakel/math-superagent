# The Cramér–Gallagher model of the primes applied to the fold's second moment

```approach
idea: >
  Compute the fold's second moment E[S(n)²] = Σ_{d,d'} E[(−1)^{T(n,d) ⊕ T(n,d')}]
  in the CRAMÉR–GALLAGHER random-prime model (not the F₂-uniform "fair model"
  the run has used, which knows no number theory), where index-distance-2^g
  pairs are transferred to value-distance ≈ 2^g log x at the mean gap scale and
  the correlations are given by the Hardy–Littlewood singular series / short-
  interval prime-counting moments. Prove the model's second moment is O(n)
  (matching the measured |S| ≈ 3.5√n), giving a CONDITIONAL averaged-SUPPLY
  theorem — the first conditional result in this run — and isolating the
  unconditional gap as one named statement strictly weaker than positive mod-4
  switch density.

mechanism: >
  T(n,d) ⊕ T(n,d') is the parity of the switch indicator h over the symmetric
  difference M_d △ M_{d'}; exponentiating, (−1)^{T⊕T'} = Π_{j ∈ M_d △ M_{d'}}
  s_j s_{j+1}, a product of adjacent-pair signs of s = χ(q_j). Under the
  Cramér–Gallagher model, the primes' residues at specified index positions are
  governed by the value-domain k-tuples singular series at value gaps ~ (index
  gap)·log x: the model predicts Σ_j χ(q_j) χ(q_{j+2^g}) through the pair
  correlation of χ at value distance ≈ 2^g log x. The fold's second moment sums
  these over the dyadic coefficients of M_d △ M_{d'}; the geometry already
  proved (meet-semilattice, F_n(z)=O(n) for iid input) is the archimedean part,
  and the novel content is that the non-archimedean singular-series factors
  cancel the same way at second order, so E[S²] = O(n) in the model for a
  purely combinatorial reason about the pattern set. Named engines: the
  Cramér model, Gallagher's moments of the number of primes in short intervals,
  the Hardy–Littlewood singular series (and its short-range form). The
  unconditional gap then reads: "the real primes match Cramér–Gallagher at
  second order for the submask correlations the fold reads" — a variance
  statement over many structured patterns, strictly weaker than the first-
  moment adjacent switch density.

status: refuted

first-step: >
  (symbolic_math + tool_builder, exact arithmetic)
  (1) VERIFY the index↔value transfer: for the real primes up to x = 40000,
      print the value-gap distribution of index-distance-2^g pairs (g = 0..4)
      and confirm it concentrates at ≈ 2^g log x with sublinear relative
      spread. (2) WRITE the finite singular-series formula for
      E[(−1)^{T(n,d) ⊕ T(n,d')}] as a sum over residue patterns
      (−1)^{#switches} · S(pattern) and symbolically derive S for low-popcount
      pairs (d,d'). (3) MACHINE-SUM the formula for all (d,d') at n ≤ 64 and
      confirm it is O(n), not n² — the falsifier is any stratum contributing
      Θ(n²). (4) CALIBRATE: cross-check the model's g=0 adjacent-switch mean
      against the known measured switch density before trusting any higher
      scale. FALSIFIER: if the singular-series sum does not cancel at second
      order (some stratum is Θ(n²)), the model does not predict averaged-SUPPLY
      and the route dies with the reason recorded.

killed-by: >
  The named engines are real (the route is correctly grounded in the literature's
  machinery), but two defects — one structural, one of scope — make the intended
  conditional conclusion unreachable. The result is a computation IN a model,
  not even a conditional SUPPLY.
  (1) THE CRAMÉR MODEL IS UNBIASED MOD 4 AND CANNOT REPRODUCE THE VERY INPUT
  (SWITCH DENSITY) THE FOLD'S SECOND MOMENT IS DOMINATED BY. Cramér's random-prime
  model, and its Gallagher/Hardy–Littlewood singular-series refinement at the
  level of residues, assigns the four ordered mod-4 pairs (1,1),(1,3),(3,1),(3,3)
  equal weight (≈1/4 each) — there is no mod-4 pair bias in the model. But the
  g=0 stratum of the fold's SECOND moment, and the measured mean of the fold,
  are carried by the mod-4 SWITCH density, which is exactly what LOS
  (lemke_oliver_soundararajan_bias) shows is NON-uniform: measured switch pairs
  (1,3),(3,1) ≈ 57.5% vs equal ≈ 42.5% over x=10^3..10^6 (claim
  abgs-mod4-nonuniform-measured), and which ABGS §9 says is
  L-function-inaccessible (abgs-p1-wide-open). So the Cramér–Gallagher model
  does not predict even the FIRST moment of the fold correctly: it is
  equidistributed while the primes are switch-biased. A model that cannot match
  the mean of S(n) cannot be trusted for its second moment — the singular-series
  resummation the route relies on for E[S²]=O(n) is applied to pair frequencies
  the model has systematically wrong. First-step (4) "calibrate the g=0
  adjacent-switch mean" was designed to catch exactly this and would fire.
  (2) THE VALUE-DISTANCE TRANSFER HYPOTHESIS IS NOT ESTABLISHED. The route
  assumes index-separation-2^g pairs transfer to VALUE-distance ≈ 2^g log x at
  the mean-gap scale. This is the Cramér prediction for the MEAN gap; the
  SUBMASK pair-correlation the fold reads is a statement about the joint
  distribution of residues at that separation, and short-interval
  prime-counting moments (Gallagher 1976) only give the Poisson-type mean-count
  law when the interval is of logarithmic length — they do NOT determine the
  χ(q_j)χ(q_{j+2^g}) pair correlation at second order without a Hardy–Littlewood
  k-tuple input that is itself conjectural. So the "singular-series factors
  cancel at second order" claim is a heuristic inside a model, priced only by a
  finite n≤64 sum, not a theorem of the model either.
  (3) EVEN IF THE MODEL GAVE E[S²]=O(n), THE CONCLUSION IS A STATEMENT ABOUT A
  RANDOM MODEL, NOT THE PRIMES. "The real primes match Cramér–Gallagher at
  second order" is exactly the unconditional gap, and it is not an input the
  model computation supplies — it is the finite-prefix/transfer statement that
  every route lacks. A conditional theorem about the Cramér model is, at best,
  evidence (like the white-noise measurements), not a conditional SUPPLY: it
  neither proves "real primes have E[S²]=O(n)" nor isolates a named unconditional
  statement strictly weaker than switch density — it conflates "true in the
  model" with "the primes match the model", and the latter (= finite-transfer)
  is the open gate, not a bonus.

  Net: the route computes a statistic of Cramér's model that the model gets the
  input wrong for (switch density), transfers to value-distance on an unproved
  hypothesis, and then reads "true in the model" as progress on the primes —
  the last being precisely the deterministic-to-random transfer no source
  supplies. Refuted on evidence: the mod-4 unbiasedness of the classical model
  is documented (LOS's whole point is that the real primes deviate from the
  model), and the transfer is the known parity barrier, not a named tool.

precedent: >
  The engines are real and precisely stated:
  - Cramér (1936): primes as independent Bernoulli(1/log n); the classical model.
  - Gallagher, "On the distribution of primes in short intervals", Mathematika 23
    (1976) 4–9, DOI 10.1112/S0025579300016442: for h ~ λ log N, the average
    number of primes in (n,n+h] is Poisson/mean-λ, and this follows from a
    quantitative Hardy–Littlewood k-tuple conjecture via the singular series
    S(D)=∏_p (1−ν_p(D)/p)(1−1/p)^{−k}.
  - Pintz, "On the singular series in the prime k-tuple conjecture",
    arXiv:1004.1084: SH(H)→1 averaged over k-subsets (Gallagher-type), refining
    the mean behaviour of the singular series.
  - Montgomery–Soundararajan framework (as in the ANTS 2025 paper
    "D⊂[1,h]... Hardy-Littlewood conjectures imply Poisson behavior in intervals
    of logarithmic length", DOI 10.2140/ant.2025.19-4): variance ~ H log(N/H)
    beyond the short regime.
  - The mod-4 pair bias that the model cannot reproduce: Lemke Oliver &
    Soundararajan, PNAS 113 (2016), DOI 10.1073/pnas.1605366113; in-workspace
    claims los-switch-preferred-mod4, abgs-mod4-nonuniform-measured,
    abgs-p1-wide-open.
  - Distinct from the adopted in-workspace fair model (claim
    fair-model-exact-binomial) and from `function-field-fqt-model` (grounded):
    those model h on the cube / irreducibles; this is the classical integer
    Cramér model. But its UNbiasedness mod 4 is the documented defect (LOS).
  Verification caveat: none of the route's computations (value-gap transfer,
  singular-series sum, n≤64 calibration) was run on this pass (no execution
  tool); the refutation rests on the literature facts about the model being
  mod-4 unbiased and the parity-barrier transfer being open, which are sourced
  above.
```

## Speculation, marked

The Cramér–Gallagher model and the singular series are real and named; that the
INDEX-distance constraint transfers cleanly to value-distance at the mean gap
scale is a hypothesis to be checked (first-step (1)) — it can fail in the
tails. That the singular-series factors cancel to give E[S²] = O(n) is the
central speculation, priced by first-step (3). The result, if it holds, is
conditional (on HL/Gallagher short-range behaviour), and it is reported as
conditional, not as SUPPLY. — The grounding pass found, in addition, that the
model is mod-4 UNbiased and so cannot reproduce the switch-density input that
dominates the fold's mean, which is why the route is refuted rather than
promoted to a live conditional theorem.

## Distinctness check

- Not the F₂-uniform fair model (fair-model-exact-binomial, established): that
  model draws h uniformly on the cube and knows no prime arithmetic. This is
  the number-theoretic Cramér–Gallagher model.
  — True, but the model's mod-4 unbiasedness means it ALSO fails to know the
  prime pair arithmetic that dominates the fold.
- Not `function-field-fqt-model` (grounded: models primes by irreducibles in
  F₂[t]). This is the classical integer model with singular series.
- Not `prime-race-variance-large-sieve` (refuted: unconditional value-domain
  BDH). This is a conditional model computation, used to isolate the exact
  unconditional gap rather than to prove it.
  — It names the gaps correctly but does not isolate them: "the real primes
  match Cramér–Gallagher" IS the gap, and the model computation does not
  establish it.
