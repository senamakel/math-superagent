# The native-world spectral-gap (Parseval) form of the finite transfer — proposed in the converging pass, refuted

```approach
idea: >
  The three external engines (Matomäki–Radziwill, Green–Tao/Gowers U²,
  Furstenberg rigidity) all fail because they are value-domain / Walsh-basis /
  two-map tools while the fold Φ = 1+σ (Rule 90) lives in F₂ over the dyadic
  odometer. The synthesis: compute the missing FINITE transfer in the native
  world by Parseval. Since Φ = 1+σ is the dyadic difference operator, its
  complex Fourier multiplier is (1+e^{2πiω}), whose zero set should be exactly
  the ×2-invariant characters, giving a spectral-gap identity
  wt(Φ_n h) = Σ_ω |1+e^{2πiω}|²·|ĥ(ω)|² that separates the four-element kernel
  ker Φ_n = {0ⁿ, 1ⁿ, (01)*, (10)*} and turns "input ε-far from the kernel" into
  a quantitative weight bound — the finite transfer every ergodic route lacked.

mechanism: >
  Fourier (Plancherel/Parseval) on the cyclic group: for an F₂-linear fold, the
  image weight is an energy of a multiplier. The single-fold identity is
  textbook: with f = 1−2h ∈ {±1}, wt(h⊕σh) = N − ‖(1+σ)f‖²/4, where
  ‖(1+σ)f‖² = Σ_ω |1+e^{2πiω}|² |f̂(ω)|². If this iterated to Φ_n = (1+σ)^n
  with multiplier (1+e^{2πiω})^n, SUPPLY would reduce to the spectral mass of
  the prime switch sign h away from the alternating (ω=1/2) mode — a classical
  arithmetic statement strictly weaker than switch density.

status: refuted

killed-by: >
  Three independent defects, either alone fatal (verified by the research pass;
  see research/notes/spectral_gap_finite_transfer_novelty.md). (1) WEIGHT ≠
  ENERGY without the ±1 embedding, and even with it the single-fold identity is
  the ONLY one that works: for n ≥ 2 the complex multiplier (1+e^{2πiω})^n
  represents ℂ-arithmetic 1+1=2, which cannot see the F₂ collapse 1+1=0 that
  makes Φ_n = (1+σ)^n = Σ_{j⊆n} σ^j (Lucas) what it is. Over ℂ the DC mode is
  not annihilated; over F₂ it is (ker Φ_n kills the constant mode too). So the
  multiplier does not iterate. (2) ZERO SET WRONG: |1+e^{2πiω}|=0 only at ω=1/2
  (alternating), but the PROVED kernel ker Φ_n = span(even-alt, odd-alt) is
  2-dimensional, killing BOTH the alternating and the constant mode; the
  asserted four-element kernel correspondence is false in the complex basis.
  (3) The genuinely correct n-fold object is NOT a linear multiplier but a
  HIGHER-ORDER product: (−1)^{(Φ_n h)_i} = ∏_{j⊆n} f_{i+j} (a submask-box
  Gowers inner product of the switch sign f), whose spectral home is the
  Gowers box norm — which is exactly the world the gowers-u2 candidate was
  refuted for (Walsh vs zeta/ANF basis mismatch), and which at degree 1
  (g=0) is the parity barrier. The synthesis is "the same chisel in new
  clothing": the one surviving seed (the single-fold identity) is textbook and
  does not transfer to the n-fold fold.
precedent:
  - "In-workspace proved facts used against it: fold-rank-is-n-2-nullity-2-
    alternating (ker Φ_n = span(even-alt, odd-alt), nullity 2);
    supply-fold-submask-zeta-involution (the fold cell is the F₂ zeta/ANF
    transform, not a Walsh character); fair-model-exact-binomial (uniform input
    has linear weight)."
  - "Research pass of this convergence (spectral_gap_finite_transfer_novelty):
    Pivato–Yassawi Thm 7.1 and Takei's Rule-90 rigidity are measure-level
    Cesàro/weak-* statements with no finite L² Parseval identity, no complex
    multiplier, no zero set, no weight of a fixed string. No external source
    names a 'spectral-gap finite transfer'; the composite is new as a label but
    unsound as stated."
first-step: >
  (none — refuted) If revisited at all, the only live fragment is the exact
  n-fold identity wt(Φ_n h) = (n − Σ_i ∏_{j⊆n} f_{i+j})/2 with f = (−1)^h the
  switch sign, which is the definition in ±1 form, already priced on disk as
  the arithmetic heart E[S(n)²]=O(n) of the adopted
  downset-row-code-distance-closed-form route. It is not a new mechanism.
```

## Disposition of the converging pass

All three candidates from the proposing pass (matomaki-radziwill-index-autocorrelation,
gowers-u2-nilsequence-uniformity, furstenberg-measure-rigidity-disjointness) are
**refuted**, and this fourth synthesis candidate is **refuted** too. The single
structural lesson they jointly establish: every external engine fails by the
same world-mismatch — value-domain vs prime-index, Walsh vs zeta/ANF basis,
two-map vs one-map, and now complex-Fourier vs F₂ — so the fold's native home is
*exclusively* the F₂ zeta/ANF basis plus the prime index. The surviving route is
the pre-adopted `downset-row-code-distance-closed-form`, whose geometry side
(F_n(z) = O(n)) is closed and whose arithmetic heart is the single second-moment
statement E[S(n)²] = O(n) for the prime switch sign.
