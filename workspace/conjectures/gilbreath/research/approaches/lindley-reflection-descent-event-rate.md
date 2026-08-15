```approach
idea: Read the intruder's descent x_s = |x_{s−1} − 2ε_s|, ε_s ∈ {0,1}, as a reflected random walk (Lindley/Skorokhod reflection) absorbed at the set {0,2}, and the (2,4)-event as its absorption (hitting) event. Then the regeneration rate is an absorption rate for a reflection driven by the Rule-90 edge-bit sequence, and the fluctuation theory of reflected walks (Spitzer–Baxter, Wiener–Hopf factorization, Kesten's criterion) gives the sharp drift condition separating persistent regeneration from eventual stall.

mechanism: In halved units the intruder obeys y_s = |y_{s−1} − ε_s| with ε_s ∈ {0,1}: it decreases by ε_s while y ≥ 2 and bounces in {0,1} once below 2, absorbing exactly when y ∈ {0,1} (intruder ∈ {0,2}). The (2,4)-event is "absorbed at y = 1 (intruder 4) at a step with ε = 1 (edge 2)". So the event rate equals the rate at which this reflected walk, driven by the edge-bit stream, is absorbed at height 1. The already-proved descent lemma (`lemma54-re-derived-proof`) is the absorption biconditional for this walk: y_L ∈ {0,1} ⟺ y_0 ≤ 2·#{ε=1} + 2. The open regeneration problem is the hitting-time lower bound, which is a queueing/reflected-walk question rather than a number-theoretic one. The named tools are the Lindley recursion (y' = max-form/absolute-form reflection), Skorokhod's reflection problem, the Spitzer–Baxter identity for the hitting-time generating function, and Kesten's criterion for positive recurrence of reflected walks — giving an exact drift condition (mean edge-bit density vs reflection at {0,1}) that the edge-bit stream must satisfy for events to keep arriving. This is a third, queueing-theoretic setting, distinct from the subadditive-renewal and ruin-theory proposals (which work on the block length b_k and the surplus via Kingman / Foster–Lyapunov): this works on the intruder descent sequence itself and the (2,4)-event as absorption, with the reflection at {0,2} — not the block boundary — as the reflected object.

status: refuted
killed-by: The reflection representation itself is a correct re-reading — it
  passes the Scholze gate of reproducing the proved descent biconditional and
  the drain law — but the load-bearing transfer to a hitting-time lower bound
  is not supplied by any named theorem for this object, on three independent
  grounds.
  (1) THE FLUCTUATION THEOREMS' HYPOTHESES FAIL. Spitzer's identity,
  Spitzer–Baxter / Wiener–Hopf factorization, and Kesten's criterion give
  sharp, exact statements for reflected walks (Lindley/queueing processes)
  under IID — at most jointly stationary/exchangeable — increments: Spitzer's
  identity expresses the joint transform of the reflected position and running
  maximum in terms of the increment walk's fluctuation structure; Kesten's
  criterion settles positive recurrence under a negative-drift-with-moments
  condition. Here the increments ε_s of the halved descent
  x_s = |x_{s−1} − ε_s| ARE THE DETERMINISTIC RULE-90 EDGE-BIT STREAM — a
  driven, non-random sequence (the terminal entry of the eroding block,
  `edge-interior-invertibility-sharpened`: e_d = XOR_{j≤d} [C(d,j) mod 2] h_{…},
  a unitriangular deterministic map of the block bits, with no two-tap
  independence). No Spitzer/Wiener–Hopf/Kesten theorem converts an arbitrary
  deterministic increment stream into a hitting-time lower bound; the whole
  body is about stochastic reflected walks with a law.
  (2) THE DRIFT CONDITION RESTATES THE CONJECTURE. The exact regeneration
  criterion (edge 2, intruder 4) and the recharge identity
  `step-law-theorem-proved` are already proved and reduce GC to "the (2,4)-
  event arrival rate keeps Σ(j_i+1) ≥ k−2". Reading the (2,4)-event as
  "absorption of the reflected walk at height 1" is a relabel, not a
  reduction: the "drift condition" the proposal needs the edge-bit stream to
  satisfy (mean edge-bit density vs reflection at {0,1}) IS ex hypothesi the
  unproved regeneration content itself. The descent biconditional the
  representation reproduces is `lemma54-re-derived-proof` (proved,
  kernel-checked core `lemma54-descent-lean-formalised`, and the Lean is now
  sorry-free) — so the reflection reading re-derives a proved fact and then
  must conjure a probability law for the edge bits that the deterministic
  primes do not provide.
  (3) EPPSTEIN KILLS THE CLASS-LEVEL FORM. For any unbounded monotone
  f(n) ≥ 2 Eppstein 2011 builds a 2-then-odds sequence with gaps ≤ f(n) whose
  right edge escapes to non-1 infinitely often — a reflected-walk/intruder
  path that "stalls" (fails to absorb at height 1) infinitely often. So no
  per-event drift/hitting-time lower bound holds on the whole 2-then-odds
  class; the primes can only differ by non-concentration, which no fluctuation
  theorem supplies.
  This is precisely the ruin-theory refutation
  (`ruin-theory-foster-lyapunov-surplus`, refuted: "drift/supermartingale
  certificate is a statement about probabilistic ruin, which this is not — no
  probability measure, no i.i.d. claim law…; the required drift hypothesis is
  RESTATED, not reduced"). Candidate 3 reframes the same open content in
  reflected-walk vocabulary over the intruder descent instead of the surplus;
  the wall is identical. What survives (and is worth keeping) is the valid
  reflection/Lindley READING as an organisational language and the fact that
  the (2,4)-event is genuinely an absorption event of a {0,1}-reflected walk —
  but it supplies no new theorem and no source applies Spitzer/Wiener–Hopf/
  Kesten to the Gilbreath problem (none found).
precedent: >
  Sourced (fluctuation theory of reflected walks, all real and standard here):
  Lindley recursion / queueing reflected walk; Spitzer's identity (Janssen–van
  Leeuwaarden, Oper. Res. Lett. 2017, doi:10.1016/j.orl.2017.12.003);
  Peigné–Woess recurrence of 2D Lindley processes (Ann. Appl. Prob. 2021,
  doi:10.1214/20-aap1654); Reed, "On the generalized drift Skorokhod problem
  in one dimension" (J. Appl. Prob. 2018); "A multiplicative version of the
  Lindley recursion" (Queueing Systems 2021). These are statements about
  reflected walks WITH a probability law; none applies to a deterministic
  driven increment stream, and none touches the Gilbreath problem.
  Internal claims: lemma54-re-derived-proof (absorption biconditional),
  lemma54-descent-lean-formalised (kernel-checked halved core),
  step-law-theorem-proved (step law, drain law, recharge identity, (2,4)-event
  criterion), edge-interior-invertibility-sharpened (unitriangular deterministic
  edge map — the increments are NOT independent).
  Sibling refuted approach: ruin-theory-foster-lyapunov-surplus (identical
  probabilistic-machinery-lacks-a-measure / drift-restates-conjecture /
  Eppstein refutation); renewal-process-edge-flip-hitting-time (grounded,
  distinct: works on the (0,4)-edge stall, not the intruder descent).
  No source was found applying Lindley/reflected-walk/fluctuation theory to
  the Gilbreath or iterated-absolute-difference problem.
buy: The reflection representation is the right vocabulary for the already-
  proved descent/drain facts — worth keeping as shorthand, not as a route. It
  re-derives `lemma54-re-derived-proof` (absorption biconditional = absorption
  at {0,1} of a {0,1}-reflected walk) and the drain law (= reflection at
  {0,1}), so it passes the Scholze gate for reproduction but adds no new
  theorem. The open event-rate question remains what it already was, in
  different words: an unproved hitting-time/arrival bound for a deterministic
  driven stream, which no fluctuation theorem closes. Retire it as a route to
  the event-rate; the honest partial result for regeneration stays the
  conditional form "IF the (2,4)-arrival drift holds on the prime stream THEN
  b_k never hits 0", whose hypothesis is the open content (restated, not
  reduced) — exactly as `ruin-theory-foster-lyapunov-surplus` concluded.
first-step: Formulate the exact Lindley/reflection representation of the intruder descent and of the (2,4)-event as absorption at height 1; verify it reproduces `lemma54-re-derived-proof`'s biconditional and the drain law y' = y − 2·[x=2] on the real prime diagonals (zero violations); then derive the hitting-time generating function for the reflected walk driven by an i.i.d. unbiased edge bit as the random-analogue baseline, and read off the drift condition that would need to hold for the real edge-bit stream.
```

## Established vs speculation

- **Established:** the descent/absorption biconditional (`lemma54-re-derived-proof`, kernel-checked halved core `lemma54-descent-lean-formalised`) and the drain law are proved; the (2,4)-event is the only growth mechanism (step law / recharge identity).
- **Speculation:** the transfer from "the edge-bit stream satisfies a drift condition" to "events keep arriving" is the content of Kesten/Spitzer theory applied to a DRIVEN (non-i.i.d.) reflection; the load-bearing step is whether the edge-bit stream's structure (Rule-90 readout of the block, `edge-interior-invertibility-sharpened`) yields a usable drift lower bound — this is the open content, not settled.

## Scholze gate

The reformulation must reproduce `lemma54-re-derived-proof` (absorption biconditional) and the drain law as a reflection hitting-time statement; those are the two held results the queueing setting must see natively. If the reflection reading cannot even re-derive the biconditional, it is not yet worth having.

## Falsifier

Smallest input that breaks the dictionary: an intruder descent sequence for which the "absorbed at height 1 with ε=1" condition does not coincide with the (2,4)-event as defined by the step law (edge 2, intruder 4). The first-step verification is exactly this check against the real prime diagonals; any mismatch refutes the representation.
