# Proof skeleton: the conditional supply step, split into concentration + suffix length

This file does **not** restate the Granville reduction (already discharged in
`route-b-supply-consolidated.md`) and does **not** re-open any of the three
coordinate forms of the supply gap. It decomposes the one lemma the run's own
stated deliverable rests on — *"Hardy–Littlewood / Lemke Oliver–Soundararajan
two-point mod-4 correlation ⟹ ν₂(q_n) ≥ n^β (β > 0.52)"* — into two lemmas of
different type and different difficulty:

- **CT-concentration** — a combinatorial concentration statement about the
  weight of a fixed F₂ (Rule-90/Pascal) fold of a near-white bit string. This
  is the half that actually uses HL/LOS, and it is attackable today by a
  theorem_prover (McDiarmid/bounded-difference) or verified on a random
  analogue by a tool_builder.
- **CT-suffix-length** — a statement that the maximal `{0,2}` suffix of the
  right diagonal is long enough for the fold to have cells to count. This is
  the number-theoretic half, and the important observation is that its
  threshold is **sublinear** (`n^β`, β > 0.52), because the demand side
  `g*_n ≤ n^{0.52}` is sublinear — not the linear `ν₂ ≥ c·n` the run has been
  quoting as "the" target. The measured suffix is *linear* (ν₂/n ≈ 0.45–0.52,
  hence suffix length ≥ that), so CT-suffix-length has enormous slack at the
  threshold that actually matters.

Honesty up front: this split does **not** close the supply side. It moves the
open content from "one monolithic ν₂ statement" to "one combinatorial lemma +
one sublinear-suffix-length statement", and it names the precise place where a
too-quick concentration argument would smuggle in success (see CT-suffix-length's
`next`).

Conventions (matching the run): δ(q_n) = (δ_0,…,δ_{n−1}), δ_k = A_k(n−k), is
the right diagonal through q_n; the **maximal {0,2} suffix** of δ(q_n) is the
trailing run of entries in {0,2} (excluding the final δ_{n−1} = 1), of length
L_n; ν₂(q_n) is the number of 2s in that suffix; h[j] = ((p_{j+2} − p_{j+1})/2)
mod 2 ∈ {0,1} is the halved-gap parity bit over the ancestor window.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1 —
as a CONDITIONAL theorem under the Hardy–Littlewood / Lemke Oliver–Soundararajan
two-point consecutive-prime mod-4 correlation hypothesis.
implies: |
  (0) EQUIVALENCE [discharged]  A_k(0)=1 ∀k ⟺ A_k(1)∈{0,2} ∀k
      (gilbreath-reduces-to-second-in-02; gilbreath-second-entry-equivalence, Lean IFF).

  (1) LINEARIZATION [discharged]  On the maximal {0,2} suffix (rows of the right
      diagonal whose halved values are {0,1}), each halved entry equals the
      XOR/Rule-90 fold of h over the fixed ancestor window, so
      ν₂(q_n) = wt(Φ_n h) where Φ_n is the explicit Pascal-mod-2 fold:
      rule90-interior-xor (proved) gives the binom(d,·) window law per cell, the
      ancestor-window union is the fixed interval [2,n−1] (verified in the
      nu2_vs_gap_parity session; promotion to a claim block is housekeeping, not a
      gap), and transfer-matrix-kernel-allones (checked) pins
      Φ_n[k][j] = C(k−1, j−(n−k)) mod 2. PRECISION: Φ_n must be restricted to the
      suffix rows, i.e. its row set is the maximal {0,2} suffix, not the full
      slice k=2..n−2 unless the full slice is {0,2}-valued — see CT-suffix-length.

  (2) CONCENTRATION [CT-concentration, OPEN]  Under HL/LOS (h asymptotically
      unbiased, bounded pair correlations — los-2016-consecutive-pair-mod4-bias;
      measured near-white in switch-bit-two-point-autocorrelation-near-white):
      ν₂(q_n) ≥ L_n/2 − C·√(n log n) for all large n.

  (3) SUFFIX LENGTH [CT-suffix-length, OPEN]  L_n ≥ n^β for some β > 0.52
      (any sublinear power above 0.52 suffices; L_n ≥ n^{0.526} with coefficient 1
      is the concrete choice).

  (4) BUDGET [discharged from (2)+(3)]  The runway needs 2ν₂ + 2 ≥ g*_n, i.e.
      ν₂ ≥ g*_n/2 − 1. With g*_n ≤ n^{0.52} it suffices that ν₂ ≥ (1/2)n^{0.52} − 1.
      (2)+(3) give ν₂ ≥ L_n/2 − C√(n log n) ≥ (1/2)n^β − C√(n log n)
      ≥ (1/2)n^{0.52} − 1 for all large n, because β > 0.52 forces
      (1/2)(n^β − n^{0.52}) ≫ C√(n log n). NOTE the coefficient 1/2: the
      demand is g*_n/2, NOT g*_n, so the threshold is ν₂ ≥ (1/2)n^{0.52}, not
      ν₂ ≥ n^{0.526} — the run's other skeletons state the supply with
      coefficient 1 and are therefore needlessly strong by a factor 2.

  (5) RUNWAY + DEMAND [discharged]  2ν₂(q_{n−1}) + 2 ≥ n^{0.52} ≥ g*_n ⟹
      q_1..q_n succeeds (lemma54-re-derived-proof, proved on the even domain;
      lemma54-descent-lean-formalised-even; lemma54-composition-lean-formalised;
      demand g*_n ≤ n^{0.52} from gap-bounds-cannot-force-block-growth / BHP 2001 /
      li2023-short-interval-052; the exponent choice α ∈ {0.52, 0.525} is
      immaterial once (4) holds — li2023-not-bottleneck).
      Strong induction on n from the verified base (verification-record-2026).

  COMBINE: (2)+(3) give the supply bound (4); (5) turns "q_1..q_{n−1} successful"
  into "q_1..q_n successful"; induction gives every finite prefix successful; (0)
  gives A_k(0)=1 for all k. Hence HL/LOS two-point correlation ⟹ Gilbreath's
  conjecture, conditional on the two lemmas below.

status: sketched
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, rule90-interior-xor, transfer-matrix-kernel-allones, lemma54-re-derived-proof, lemma54-descent-lean-formalised-even, lemma54-composition-lean-formalised, gap-bounds-cannot-force-block-growth, li2023-short-interval-052, li2023-not-bottleneck, verification-record-2026, los-2016-consecutive-pair-mod4-bias, switch-bit-two-point-autocorrelation-near-white, abgs-2011-s9-mod4-switch-limit-open
killed-by: (none — new decomposition of the conditional supply step; its two gaps are the named-open content split into a combinatorial half and a number-theoretic half, and are NOT disguised as provable)
```

```gap
id: CT-concentration
lemma: |
  Under the Hardy–Littlewood / Lemke Oliver–Soundararajan two-point mod-4
  correlation hypothesis, the halved-gap parity bit string h[j] = ((p_{j+2}−p_{j+1})/2)
  mod 2 over the ancestor window is asymptotically unbiased with bounded pair
  correlations, and the maximal-{0,2}-suffix cells of the right diagonal are a
  fixed F₂-linear (Rule-90/Pascal) fold Φ of h. Then, conditional on the suffix
  location (i.e. given the row set S_n of length L_n), the number of 2s in the
  suffix satisfies
      ν₂(q_n) = wt(Φ_{S_n} h) ≥ L_n/2 − C·√(n log n)
  for an absolute C and all sufficiently large n.
status: open
next: |
  This is the combinatorial half and is attackable TODAY, independent of the
  suffix-location problem. Two first moves:
  (a) tool_builder (cheap, pins the constant): for i.i.d. unbiased h ∈ {0,1}^m,
      compute wt(Φ_{S} h) for the run's explicit Φ_S on a fixed row set S of
      length L, over many draws; record E[wt] = L/2 and the fluctuation
      max |wt − L/2| as a function of (L, n). Confirm it is O(√(n log n)) and
      NOT O(√(L)) — the rows of Φ_S are XOR-folds of overlapping windows, so the
      correlation structure is what determines the constant; this pins the exact
      fluctuation the deterministic HL argument must reproduce.
  (b) theorem_prover: under a stated bounded-pair-correlation hypothesis on h
      (the quantitative form LOS 2016 supplies under HL), prove the
      concentration. The row functionals are (nonlinear) indicators of XOR sums;
      since the XOR-fold of a near-white bit string is itself near-iid unbiased,
      wt(Φ_S h) is a sum of near-independent Bernoulli indicators and concentrates
      by McDiarmid / bounded-difference. Formalise the fold as an F₂-linear map
      over the window, state the correlation hypothesis as a sum-of-covariances
      bound, and carry the variance through. Report #print axioms, zero sorry.
  GUARD (adversarial): this lemma MUST be stated with the row set S_n as an
  explicit parameter. If the argument quietly sets S_n = the full slice
  k=2..n−2 (i.e. assumes the suffix is full), it has smuggled in CT-suffix-length
  — the load-bearing number-theoretic half below — and the "conditional theorem"
  collapses to a restatement. The first move (a) should therefore use an
  arbitrary fixed S, not the prime-diagonal suffix, precisely to keep the two
  lemmas separate.
```

```gap
id: CT-suffix-length
lemma: |
  For the prime right diagonal, the maximal {0,2} suffix of δ(q_n) (equivalently
  the row set S_n of the linearization) has length L_n ≥ n^β for some β > 0.52
  and all sufficiently large n. Concretely L_n ≥ n^{0.526} (coefficient 1)
  suffices, because that makes (1/2)L_n − C√(n log n) ≥ (1/2)n^{0.52} − 1. Because
  the demand is g*_n ≤ n^{0.52} (sublinear), the threshold is SUBLINEAR with
  coefficient 1 — strictly weaker than the linear ν₂ ≥ c·n the run quotes as its
  target, and strictly weaker than the linear suffix actually measured (ν₂/n ∈
  [0.45, 0.52] forces L_n ≥ 0.45 n).
status: open
next: |
  STATUS HONESTY: this is the number-theoretic half and it is the named-open
  content abgs-2011-s9-mod4-switch-limit-open, restated at a weaker threshold.
  The mod-4 switch density enters here, not in CT-concentration: a long {0,2}
  suffix is exactly "the descent stays in {0,2} for L_n steps", which is the
  budget the switches supply. Do NOT claim it is corollary-level.

  First move (tool_builder, the missing anchor — cheaper and more decisive than
  any sweep): the run has measured ν₂ (≤ L_n) but I found no claim block that
  measures L_n itself. Extract the maximal {0,2} suffix length L_n of the right
  diagonal from the exact right-diagonal computation (one length-n vector op per
  n, O(N²) time / O(N) memory — far below the 8 GiB ceiling), to n = 1e5 or 1e6,
  and report min L_n/n, min L_n/n^{0.526}, and the suffix-start row K_n. This
  decides whether L_n is linear (expected, and then the threshold n^{0.526} has
  ≫ 100× slack) or only barely superlinear (which would change the honest
  statement).

  Second move (theorem_prover): prove the equivalence "L_n ≥ n^β ⟺ the switch
  budget holds for n^{1−β} steps along the diagonal", composing Lemma 5.4's
  descent with the switch conservation identity (switch-conservation-identity).
  This turns CT-suffix-length into a clean statement about the mod-4 switch
  count at a SUBLINEAR threshold, and connects it to
  abgs-2011-s9-mod4-switch-limit-open without pretending a linear bound.

  THE DELICATE POINT (this is what the next forward attempt must not hide):
  if the only available proof of L_n ≥ n^β goes through "the budget holds, hence
  the suffix stays long, hence ν₂ is large, hence the budget holds", that is
  circular — it is the conjecture in diagonal coordinates. A non-circular proof
  must establish L_n ≥ n^β from the prime gap arrangement alone (the switch
  density), which is precisely why ABGS §9 — no limiting frequency — is the
  obstacle. The honest deliverable keeps this lemma as the hypothesis of the
  conditional theorem.
thread: research/threads/regeneration.md
```
