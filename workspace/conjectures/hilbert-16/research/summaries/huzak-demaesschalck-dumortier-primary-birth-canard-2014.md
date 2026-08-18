# Huzak–De Maesschalck–Dumortier, *Primary birth of canard cycles in slow-fast codimension 3 elliptic bifurcations*, CPAA 13(6) (2014) 2641–2673

<!-- source: https://documentserver.uhasselt.be/bitstream/1942/17161/1/pdfs.pdf ; DOI 10.3934/cpaa.2014.13.2641 -->

Full published PDF held: [[huzak-demaesschalck-dumortier-primary-birth-canard-2014.full]]

**What this is.** The open-access companion to the (paywalled) Huzak–De
Maesschalck–Dumortier 2013 JDE paper on slow-fast codimension-3 saddle and
elliptic bifurcations. It studies the **birth of canard cycles** — limit cycles
at the interface between small-amplitude cycles and canard cycles — in a
codimension-3 slow-fast elliptic bifurcation, using a **primary blow-up**
(desingularizing the codim-3 singularity) combined with a **secondary blow-up**
(dissolving the slow-fast structure).

## Established

- **Theorem 4.1**: The transition maps H± across the turning point,
  `(U,R,τ) ↦ (−ϵ²h±(U,R,τ), UR)`, are C^∞ and have C^k-extensions to D_k;
  h± strictly positive. (Presence of hyperbolic saddles weakens the smoothness:
  C^k for all k, possibly ϵ_k → 0 as k → ∞.)
- **Theorem 4.3** (cyclicity of the limit periodic set Γ at B₂ = B̄₂):
  - (a) −2 < B̄₂ < 2, B̄₂ ≠ 0: cyclicity exactly 1 (hyperbolic attracting if B̄₂>0, repelling if B̄₂<0);
  - (b) B̄₂ = ±2: cyclicity exactly 1 (attracting at +2, repelling at −2);
  - (c) 2 < |B̄₂| ≤ B₀₂: cyclicity 0.
- **Theorem 4.4**: if H̄(0,λ) ≠ 0 for all λ ∈ Λ, cyclicity of Γ at B₂ = 0 is bounded by 2.
- **Method** (the instrument): zeros of δ = h⁺ − h⁻ on the hyperbolas
  {UR = r} correspond to limit cycles Hausdorff-close to Γ; the Lie-derivative
  L_Y (Y = U∂_U − R∂_R) trick reduces the zero count (which naively involves
  exponentials) to a tractable equation, and Rolle's theorem bounds zeros of δ
  by zeros of L_Y δ. This is the displacement-function machinery of the run's
  `slow-divergence-integral-ect` / `dulac-cochain-stokes-consistency` approaches.

## Verified against the full text

The claim block matches the paper: the family (5) in Liénard plane, the primary
blow-up (3) and secondary blow-up, the limit periodic set Γ = {critical curve
`{ȳ−½x̄²=0}`} ∪ {regular arc A}, the sections Σ¹₀, Σ²₀, the C^k transition
maps, the exponential Dulac form (46) `x̄ = ... − exp(−1/ϵ² (∫ A(...)/R' dR' + ϵ²L))`,
the Lie-derivative equation (63)–(64), the slow divergence integral (78), the
ST-system derivation–division bound in §5.4 (Lemma 5.15: `−2√2 + f₁(R)` and
`−π/2 + f₂(R)`). No gap found between the claim and the source.

## For this problem

This is the slow–fast/canard instrument (problem.md's slow–fast test regime).
Its primary/secondary blow-up + Lie-derivative zero-counting pattern is the
model for treating limit cycles at the interface of small-amplitude and canard
cycles at degenerate singularities — the same interface the open DRR graphics'
second-type Dulac maps present. It does not close any DRR graphic.

## Boundary

- The 2013 JDE paper [8] (saddle AND elliptic bifurcations; the small-amplitude
  cycles) is the paywalled half of the pair; this 2014 paper is the elliptic
  canard-birth half and uses [8]'s results.
- Not a DRR-graphic closure; a methodology/cyclicity instrument.
- Claim block: `h16-hdd2014-canard-birth-slowfast-codim3` in `research/claims/`.
