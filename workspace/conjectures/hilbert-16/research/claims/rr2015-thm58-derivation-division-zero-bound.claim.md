# RR 2015 Theorem 5.8: derivation–division zero bound, exact hypotheses

```claim
id: rr2015-thm58-derivation-division-zero-bound
statement: RR 2015 Theorem 5.8 (derivation–division zero theorem): Let V(r,ρ,λ) = Σ_{i=1}^l Aᵢ(λ)·Mᵢ·(1 + gᵢ(r,ρ,λ)) on 𝒜×ℬ∩{r>0,ρ>0}, where (1) Mᵢ = r^{aᵢ}ρ^{bᵢ}ω^{cᵢ} are general monomials WITHOUT Ω-factor (aᵢ,bᵢ,cᵢ smooth in λ); (2) gᵢ are C^k-functions on monomials with k ≥ l, of order o(1) in the sense gᵢ(0,0,λ₀) = 0 (Notation 5.2); (3) Aᵢ(λ) are continuous; (4) pairwise non-resonance aⱼ⁰−aᵢ⁰−bⱼ⁰+bᵢ⁰ ≠ 0 for i≠j. Then on a sufficiently small neighborhood 𝒜×ℬ of (0,0,λ₀): either V has at most l−1 isolated zeros counted with multiplicity on each curve l_ν = {rρ=ν} ⊂ 𝒜, or V is identically zero. Proof: divide by M₁(1+g₁), apply L_𝒳 (𝒳 = r∂ᵣ−ρ∂_ρ; Lemmas 5.3, 5.7), repeat l−1 times, then Rolle backwards on the connected leaves l_ν.
hypotheses: quadratic systems as the ambient family in the applications; the four displayed hypotheses of the theorem (Ω-free general monomials; C^k on monomials with k≥l; gᵢ = o(1) pointwise at λ₀; Aᵢ continuous; pairwise non-resonance). The conclusion is local in λ₀ (neighborhood depends on λ₀). There is NO center-ideal hypothesis and NO uniformity-over-box conclusion in the theorem itself; the identically-zero case is not excluded by the theorem.
holds-here: yes
status: asserted
evidence: verified against held full text — research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md lines 1007–1190 (Def 5.1, Def 5.4, Notation 5.2, Lemmas 5.3/5.7, Thm 5.8, Remark 5.9) and duplicate rousseau-shan-zhu-center-graphics-2015.full.md lines 1123–1180, plus the application note at line 499 ("either V has at most two small zeros, or V is identically zero, in which case we have a center").
falsifier: (a) a non-boundary H^3_13 stratum whose displacement expansion contains an Ω-factor monomial not absorbable into the o(1) remainder — Theorem 5.8 then does not apply as stated; (b) an identically-zero displacement with a claimed finite zero bound — any bound skipping the exclusion clause is vacuous; (c) a formalisation from the held text taking ℬᵢ = {Aᵢ ≥ Aⱼ} literally (signed) — the proof's "identically zero" alternative requires the magnitude form |Aᵢ| ≥ |Aⱼ|.
sources: https://arxiv.org/abs/1506.07104 ; https://doi.org/10.1090/mosc/248
anchors: research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md lines 1007-1190 (App. II), lines 253-274 (Thm 2.3 second-type Dulac maps), lines 627-676 (Thm 1.2 proof, eq. 3.33-3.37, Ω handled by O_P(M_C)·O(ν) absorption into coefficients, never by an Ω-extension of Thm 5.8), line 465 (center ideal I_C = ⟨ε₀,ε₁,μ̄₃⟩)
note: The run's goal h16-2-h13-3-finite-cyclicity-h13-derivation-division-uniform-zero-bound and h16-2-h13-3-finite-cyclicity-h13-generalized-displacement-expansion rest on this theorem. Missing hypotheses the run must carry beyond the source: uniformity over a compact box (finite-cover corollary, needs expansion validity on the cover), the identically-zero exclusion (= center condition in applications), Ω-free expansions on every non-boundary stratum (or an extended theorem), k ≥ l with the for-all-k convention. The phrase "center-ideal/derivation-division" fuses the application layer (coefficients in the center ideal) with the theorem layer (which only needs Aᵢ continuous). Lean gap: code/lean/Lib/RCenterIdealZeroDivision.lean's zero_division hypothesis is vacuously satisfied by V′≡0 (0 ∈ the ideal, |0| ≤ C·|remainder_bound|) with an infinite zero set; the identically-zero exclusion must be added to its antecedent. Full audit: research/findings/rr2015-thm58-derivation-division-hypotheses-audit.md
answers:
```

## Why this claim block exists

The run's backward chain for H^3_13 finite cyclicity consumes "RR Thm 5.8
(generalized-monomial form)" as its zero-count engine, but no claim block with
the theorem's exact hypotheses was on disk. This block pins the exact statement
(Ω-free monomials, pointwise o(1), continuous coefficients, non-resonance,
local-in-λ₀ conclusion, identically-zero alternative) so the conditional
"center-ideal/derivation-division zero bound" is not over-claimed.
