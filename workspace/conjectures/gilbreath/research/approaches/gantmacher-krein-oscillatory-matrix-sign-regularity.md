# gantmacher-krein-oscillatory-matrix-sign-regularity

```approach
idea: Prove A_k(1) ∈ {0,2} by bounding the sign changes in the signed
forward-difference sequence Δ_k via the variation-diminishing property of
totally positive (oscillatory) matrices — a classical theorem of
Gantmacher–Krein (1950) and Schoenberg (1930).

mechanism: The signed k-th forward difference Δ_k(i) = Σ_{j=0}^k (−1)^{k−j} ·
binom(k,j) · A_0(i+j) satisfies A_k(i) = |Δ_k(i)| WHEN the signs of
Δ_k(i) and Δ_{k−1}(i) agree in the right way (specifically, when no sign
change forces the min branch). The matrix M_{k,j} = (−1)^{k−j} · binom(k,j)
is a totally positive kernel: it is sign-regular, and Gantmacher–Krein's
"variation-diminishing theorem" says that the number of sign changes in the
transformed sequence Δ_k is at most the number of sign changes in the
original sequence A_0 (restricted to the relevant window).

Now the obstruction to A_k(i) = |Δ_k(i)| is exactly at points where Δ_k
changes sign — because there the min-branch correction in |a−b| = a+b −
2·min(a,b) activates with a nontrivial carry. If the sign-change count of
Δ_k can be bounded independently of k (using that the prime gaps, while
irregular, have a "coherence length" beyond which variations are smoothed),
then the correction −2·min is confined to a bounded zone. In particular, if
the sign-change count at position 1 is zero for all k (i.e., Δ_k(1) never
changes sign), then A_k(1) = |Δ_k(1)| is a pure linear binomial transform of
the gaps, and the conjecture reduces to: does a specific signed binomial sum
of prime gaps stay in {0,2}?

More precisely, the variation-diminishing theorem gives:
    S^−(Δ_k) ≤ S^−(A_0) = bounded,
where S^− counts sign changes (with zeros handled by a standard convention).
This means Δ_k has at most S^−(A_0) sign-change blocks, independent of k.
Within each block the sign is constant, so the absolute-value operation
on that block is just (±) the signed value — no min correction. The min
correction only occurs at block boundaries, and there are at most S^−(A_0)
of them. For position 1, the correction at each boundary is an even integer
(the min of two even numbers), and the total correction at position 1 after
k steps is a sum of at most S^−(A_0) such boundary terms, each damped by
binomial coefficients from the Pascal convolution.

The program: prove that for a sequence starting (2 followed by odds) whose
initial halved-gap row has bounded sign variation, the cumulative boundary
correction at position 1 never pushes A_k(1) past 2. The engine is the
Gantmacher–Krein oscillation theorem, which is a standard tool in
approximation theory, splines, and the moment problem — never applied to
Gilbreath.

Why this is genuinely different: it does not track blocks, intruders,
erosion, or regeneration. It replaces the nonlinear |a−b| with its
linear signed cousin + a boundary correction whose count is controlled by
a classical matrix-property theorem. It attacks the valency of the min
branch directly, using the sign-regularity of the Pascal matrix. No other
approach on disk uses oscillation theory.

named mathematics: Gantmacher–Krein oscillation theorem, totally positive
matrices, variation-diminishing property, Schoenberg's spline theory,
sign-regular kernels, Chebyshev systems, the Descartes rule of signs
(generalised).

status: refuted
killed-by: >
  Refuted on three independent grounds. (1) The load-bearing matrix is NOT
  sign-regular, so the Gantmacher–Krein / Schoenberg variation-diminishing
  theorem does not apply to it. The candidate asserts M_{k,j} = (−1)^{k−j}
  binom(k,j) is "totally positive: sign-regular". Hand-check (script
  code/out/check_three_candidates.py written this cycle, NOT executed — no
  execution tool): the 2×2 minor of rows {1,2}, cols {0,1} is
  (−1)(−2) − (1)(1) = +1, while rows {1,2}, cols {0,2} is (−1)(1) − (0)(1)
  = −1. Same minor order, opposite signs ⇒ the matrix is NOT sign-regular of
  order 2. The modern sharp form of the VD theorem (Choudhury–Yadav 2024:
  A has the VD property S^+(Ax) ≤ S^−(x) for all x iff A is strictly
  sign-regular) therefore cannot be invoked.

  (2) The claimed bound fails on the primes at k=2 regardless of which
  matrix theorem is being (mis)applied. A_0 = (2,3,5,7,11,13,17,19,23,29)
  is strictly increasing, so S^−(A_0) = 0. The signed second forward
  difference is D_2 = (1,0,2,−2,2,−2,2,2), which has 4 sign changes after
  deleting zeros. So S^−(Δ_k) ≤ S^−(A_0) is false at k=2: 4 ≰ 0.

  (3) The mechanism depends on A_k(i) = |Δ_k(i)| "when the signs agree",
  and that identity is already refuted on the actual rows: first violation
  at (k=3, i=2) — INSIDE the leading {0,2} block — and at position 1 from
  k=4 on (claim fwd-diff-identity-refuted, evidence checked). This is the
  same mechanism as the already-refuted sign-coherence-forward-differences
  approach; oscillation theory is a new name for the same dead
  linearization. The run's runcount-lemma-refuted bearing already recorded
  that the Schoenberg/Pólya-frequency/total-positivity variation-diminishing
  theory is LINEAR-operator theory and does not transfer to the nonlinear
  absolute-difference map — this candidate crosses exactly that line.
precedent: >
  - https://doi.org/10.1090/proc/17026 (Choudhury–Yadav 2024: VD ⟺ SSR —
    the precise theorem whose hypothesis (sign-regularity) fails here)
  - https://link.springer.com/article/10.1007/BF02806392 (Karlin 1965:
    oscillation of eigenvectors of strictly TP matrices — the classical
    theory is real, but for STP/oscillation matrices, not this one)
  - https://doi.org/10.1090/s0025-5718-1993-1182247-7 (Odlyzko 1993 — the
    actual literature on this triangle; uses the mod-4 linearization, not VD)
  - https://arxiv.org/abs/2607.08712 (CHT 2026 — the only known structural
    obstructions to decay: long 0-blocks / long shallow {0,d}-blocks)
  - claims: fwd-diff-identity-refuted, runcount-lemma-refuted,
    mod4-pascal-invariant
holding-claims: fwd-diff-identity-refuted, runcount-lemma-refuted
falsifies: >
  That the alternating Pascal matrix (−1)^{k−j} C(k,j) is sign-regular, or
  that S^−(Δ_k) ≤ S^−(A_0) holds for the primes, or that A_k = |Δ_k| holds
  anywhere inside the block. Each is false; the first two are elementary
  hand checks, the third is the stored machine-checked claim
  fwd-diff-identity-refuted.
buy: >
  Nothing for Gilbreath. The named theory is real and deep (Gantmacher–Krein
  1950; Schoenberg 1930; Karlin; the modern VD characterisations) but its
  hypotheses are sign-regular LINEAR operators, and the Gilbreath operator is
  neither sign-regular nor linear. Any linearization must survive the
  (k=3, i=2) cell inside the {0,2} block, which the identity this candidate
  leans on does not.

first-step (superseded by the refutation): >
  The proposed first step — verifying S^−(Δ_k) non-increasing on real rows —
  is already answered in the negative at k=2 by hand computation (ground (2)
  above); the whole approach is dead at that step.

speculative: The min-branch valency is genuinely the hard part of the
conjecture (it is the regeneration step), but sign-regular linear theory
cannot control it because the operator is nonlinear. A surviving route would
need a NONLINEAR variation-diminishing statement, of which no source exists.
```

```claim
id: gantmacher-krein-sign-regularity-refuted
statement: The Gantmacher–Krein / Schoenberg variation-diminishing route to
  Gilbreath fails at its load-bearing premise: the alternating Pascal matrix
  M_{k,j} = (−1)^{k−j} binom(k,j) is NOT sign-regular of order 2 (2×2 minors
  of both signs exist: rows {1,2}/cols {0,1} give +1, rows {1,2}/cols {0,2}
  give −1 — hand check), and the claimed bound S^−(Δ_k) ≤ S^−(A_0) fails on
  the primes at k=2 (S^−(A_0) = 0 since the primes strictly increase; the
  signed second difference D_2 = (1,0,2,−2,2,−2,2,2) has 4 sign changes).
  The identity A_k = |Δ_k| the mechanism needs is refuted at (k=3,i=2)
  inside the block (claim fwd-diff-identity-refuted).
hypotheses: signed forward differences of the primes; the alternating-sign
  Pascal matrix as the linearization kernel.
holds-here: yes (the refutation applies to the exact object the approach
  proposes to analyse)
status: refuted (elementary hand checks + stored machine-checked claim
  fwd-diff-identity-refuted; script code/out/check_three_candidates.py
  written but not executed this cycle)
bearing: closes the oscillation-theory line: TP/VD machinery does not reach
  the nonlinear absolute-difference map; do not re-propose
  variation-diminishing control of the min-branch.
anchor: research/approaches/gantmacher-krein-oscillatory-matrix-sign-regularity.md
```
