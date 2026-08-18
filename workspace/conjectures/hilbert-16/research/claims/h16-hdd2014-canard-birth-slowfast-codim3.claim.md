# Claim — Huzak–De Maesschalck–Dumortier 2014, primary birth of canard cycles in slow-fast codim-3 elliptic bifurcations

```claim
id: h16-hdd2014-canard-birth-slowfast-codim3
statement: For the slow-fast codimension-3 elliptic bifurcation family X̄_{ϵ,b,λ}: ẋ = y, ẏ = −xy + ϵ̄(b₀ + b₁x + b₂x² − x³ + x⁴H̄(x,λ) + y²G(x,y,λ)), studied via a primary blow-up (desingularizing the codim-3 singularity) and a secondary blow-up (dissolving the slow-fast structure), the cyclicity of the limit periodic set Γ at B₂ = B̄₂ is: (a) exactly 1 when −2 < B̄₂ < 2, B̄₂ ≠ 0 (hyperbolic attracting if B̄₂>0, repelling if B̄₂<0); (b) exactly 1 when B̄₂ = ±2 (attracting at +2, repelling at −2); (c) 0 when 2 < |B̄₂| ≤ B₀₂. Method: transition maps H± : (U,R,τ) ↦ (−ϵ²h±(U,R,τ), UR) across the turning point are C^∞ with C^k-extensions (Theorem 4.1); limit cycles correspond to zeros of δ = h⁺−h⁻ on the hyperbolas {UR = r}; the Lie-derivative L_Y trick (Y = U∂_U − R∂_R) with Rolle's theorem bounds the zeros (used in [2], Dumortier–Roussarie birth-of-canard-cycles). Theorem 4.4: if H̄(0,λ) ≠ 0 for all λ ∈ Λ, cyclicity of Γ at B₂ = 0 is bounded by 2.
hypotheses: slow-fast family with codimension-3 elliptic singularity, ϵ̄ singular parameter, 3 unfolding parameters; H̄(0,λ) ≠ 0 for each λ ∈ Λ (away from the degenerate center-type case B₀=B₂=0); B₂ ∈ [−B₀₂, B₀₂]; r = UR > 0 small; ϵ ∼ 0.
holds-here: yes — this is the canard-birth / slow-fast instrument (companion to the referenced 2013 JDE paper [8], which is paywalled but whose results this paper uses and states). It supplies the primary/secondary blow-up + Lie-derivative zero-counting pattern for limit cycles at the interface between small-amplitude and canard cycles at codim-3 slow-fast singularities — the slow–fast test regime of problem.md and the instrument class the run's slow-divergence-integral-ect approach needs. It does not close any DRR graphic.
status: proved
evidence-class: proved (peer-reviewed CPAA 13(6) 2641–2673 (2014); published PDF held)
falsifier: A counterexample with >1 limit cycle for some B₂ ∈ (−2,2)\{0}, or a failed independent re-check of the transition-map C^k-extension / cyclicity-1 bound.
answers: none
follows-from: none (parent paper HDD 2013 JDE is record-only on disk; DR 2009 birth-of-canards paper not held in full)
contradicts: none
anchors: research/sources/huzak-demaesschalck-dumortier-primary-birth-canard-2014.full.md
url: https://documentserver.uhasselt.be/bitstream/1942/17161/1/pdfs.pdf ; DOI 10.3934/cpaa.2014.13.2641
```

## Notes

- This is the published companion to Huzak–De Maesschalck–Dumortier, "Limit
  cycles in slow-fast codimension 3 saddle and elliptic bifurcations", JDE 255
  (2013) 4012–4051 (DOI 10.1016/j.jde.2013.07.057), which is paywalled/restricted
  at the UHasselt repository; this 2014 paper states and uses [8]'s results
  (Theorem 2.4 etc.) and is the open-access member of the pair.
- The transition map H±, the Lie-derivative L_Y trick, and the δ = h⁺−h⁻
  zero-counting on {UR = r} are exactly the displacement-function machinery the
  run's approach `slow-divergence-integral-ect` and `dulac-cochain-stokes-consistency`
  build on. The cyclicity-1 theorem (Thm 4.3) is a clean kernel-checkable-type
  statement.
