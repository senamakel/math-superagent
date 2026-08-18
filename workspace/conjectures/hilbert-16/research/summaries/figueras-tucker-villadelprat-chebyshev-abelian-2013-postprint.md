# Figueras–Tucker–Villadelprat, *Computer-assisted techniques for the verification of the Chebyshev property of Abelian integrals*, JDE 254 (2013) 2647–3663

<!-- source: https://ddd.uab.cat/record/150616 ; postprint https://ddd.uab.cat/pub/artpub/2013/gsduab_3450/FigTucVil2012.pdf ; DOI 10.1016/j.jde.2013.01.036 -->

Full postprint held: [[figueras-tucker-villadelprat-chebyshev-abelian-2013-postprint.full]]

**What this is.** The certified-verification instrument for the run's sharp-Abelian
approach. It develops computer-assisted (interval-arithmetic, CAP) techniques to
verify the extended complete Chebyshev (ECT) property of Abelian integrals, and
applies them to prove the Dumortier–Roussarie conjecture on the cyclicity of
slow-fast Hopf points (birth of canard cycles) for q ≤ 2.

## Established

- **Theorem 1.1** (from Grau–Mañosas–Villadelprat [13, Thm B]): for
  `H = A(x) + B(x)y^{2m}` analytic with a local minimum at the origin, ovals
  `γ_h ⊂ {H = h}`, `h ∈ (0,h0)`, involution `σ` with `A(x)=A(σ(x))`, and
  Abelian integrals `I_i(h) = ∫_{γ_h} f_i(x) y^{2s-1} dx`, if the σ-balanced
  functions `ℓ_i := B_σ(f_i/(A'B^{(2s-1)/(2m)}))` form a CT-system on `(0,xr)`
  and `s > m(n−2)`, then `(I_0,…,I_{n−1})` is an ECT-system on `(0,h0)`.
- **Theorem A**: `(J̄_0, J̄_1, J̄_2)` with `J̄_i(h)=∫_{γ_h} y^{2i-1}dx` over
  `γ_h ⊂ {A(x)+B(x)y²=h}`, `A(x)=½−e^{−2x}(x+½)`, `B(x)=e^{−2x}`, is an
  ECT-system on `[0,½)`. This is the non-polynomial (transcendental) setting
  where the resultant/Sturm route of the polynomial case is unavailable; the
  Wronskian nonvanishing of `(ℓ_0,ℓ_1,ℓ_2)` is certified by interval arithmetic
  (Lemma 4.9) plus analytic estimates (Lemmas 4.5–4.7, Fujiwara bound Lemma 4.8).
  The computations for Lemma 4.10 took ~6.5 h on a 2.8 GHz desktop.
- Consequence: via Dumortier–Roussarie [7, Thms 1.5, 1.8] the cyclicity of a
  slow-fast Hopf point of codimension 1–2 (smooth and analytic systems) is
  explicitly bounded. This is the slow–fast/canard regime of problem.md.

## Verified against the full text

The claim block matches the paper: Theorem A, the ECT criterion (Theorem 1.1),
the σ-balance/ℓ_i construction, the three-interval split
`I1∪I2∪I3 = (xℓ, xℓ+ε1) ∪ [xℓ+ε1, −ε2] ∪ (−ε2, 0)`, the CAP/MPFI
interval-arithmetic Wronskian enclosures, and the Corollary 3.5 endpoint
analyticity (division-derivation algorithm). No gap found between the claim and
the source.

## For this problem

This is the ECT-certification instrument the run's approaches
(`slow-divergence-integral-ect`, `abelian-picard-fuchs-argument-principle-sharp-count`)
name. It shows how a Wronskian nonvanishing check that is algebraic in the
polynomial case becomes an interval-arithmetic certification in the
transcendental case — the exact pattern needed for the second-type Dulac /
slow-divergence endpoint maps of the open DRR graphics, where the functions are
not algebraic. It does not by itself close any DRR graphic.

## Boundary

- Theorem A proves the DR conjecture only for n = 0,1,2 (q ≤ 2), not all n.
- The computer-assisted part is rigorous (interval arithmetic with CAP) but is
  a proof the run has not re-verified independently.
- Claim block: `h16-ftv2013-chebyshev-abelian-ca` in `research/claims/`.
