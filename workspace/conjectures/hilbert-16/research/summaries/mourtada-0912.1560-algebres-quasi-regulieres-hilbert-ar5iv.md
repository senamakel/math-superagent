# Mourtada 2009 — Action de dérivations irréductibles sur les algèbres quasi-régulières d'Hilbert

## Source and availability

- Abstract page: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert.full.md` (https://arxiv.org/abs/0912.1560)
- Full text: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md` (https://ar5iv.labs.arxiv.org/html/0912.1560, 362644 B, 85 sections, 2506 lines)
- 94-page Amstex preprint, Université de Bourgogne, MSC 34C07 (primary). In French.
- The ar5iv HTML drops some displayed-equation content — notably **Théorème 0's conclusion is truncated** (see `research/findings/mourtada-theoreme-0-truncation.md`). The PDF is authoritative if the exact N, L are ever needed.

## What it establishes (asserted-by-source)

**Main theorem (Théorème IVC1).** For an irreducible derivation χ (a "dérivation d'Hilbert") acting on a Hilbert quasi-regular algebra QRH^{k,.} of germs at 0 of real-analytic functions on a semi-algebraic open set (U,0), the algebra is **locally χ-finie**: the degree of the integral projection π_χ restricted to fibers of elements is finite, and the differential ideals I_{χ,f} are Noetherian or locally Noetherian. It satisfies locally the **double inclusion**
(θ^n)π_χ*(J_{χ,f,γ}) ⊂ I_{χ,f} ⊂ π_χ*(J_{χ,f,γ})
where θ = ∏ x_j generates the boundary ideal and n is the multiplicity m_χ(f), linked to an algebraic multiplicity ma_χ(f).

**Reduced normal form.** After desingularisation, the reduced singularities of χ are
χ_ℓ = ρ ∂/∂ρ − Σ_{j=1}^ℓ s_j u_j ∂/∂u_j,  ℓ = 0..k−1.
The principal orbit γ_0 = {α=0, u=0} of χ̃_{a₀} plays a key role; the integral projection π_{χ̃_{a₀}}: (ρ,α,u) ↦ (α,λ).

**Three principaux theorems.** QRH^{1,.}(ρ,.) is χ₀-finie (Thm II1); the convergent restriction QRH^{1,.}_{cvg} satisfies the double inclusion relative to χ_ℓ (Thm IIIA1); QRH^{1,.} is locally χ_ℓ-finie with the double inclusion (Thm IIIB1). The proof of IVC1 proceeds by the first blow-up (π_k, N_k) of the desingularisation of χ, with exceptional divisor D̄_k, and a recursive argument over the boundary ∂D_k (lemme de récurrence 1 and 2, Théorème IVB1/IVC1).

**Application (Théorème 0).** For X_ν an analytic q-parameter unfolding of a real monodromic hyperbolic polycycle Γ_k (k singularities; eigenvalue ratio −1 at each, stated "uniquement pour simplifier la présentation"), there exist integers N and L and neighborhoods Γ_k ⊂ U ⊂ U_0 and V ⊂ (ℝ^q, 0) such that [conclusion truncated in the HTML conversion]. The prose states: limit cycles of X_ν correspond to isolated intersections of orbits of a Hilbert derivation χ with fibers of a germ f ∈ QRH^{k,.}; property (i) is equivalent to χ-régularity of f, property (ii) follows from Noetherianity of I_{χ,f}. Hence: **no accumulation of limit cycles on hyperbolic polycycles in compact analytic families of vector fields on S²**, including polycycles that are accumulations of cycles.

## Why the run needs this

Lu (arXiv:2607.13785) cites Mourtada [3] as the QRH theorem applied "only to an analytic all-hyperbolic word after its sections, connectors, Hilbert derivation, integral fibers, and closing germ have been realized on one common positive-corner neighborhood". The `lu-h14-3-verification` thread verifies Lu's local uniform finite cyclicity of H14³. **This source is the analytic backbone of Lu's QRH theorem (Lu Thm 36), previously cited without being held.** Now: the QRH χ-finiteness + double inclusion + reduced normal form χ_ℓ are all readable here.

Claims: `mourtada-2009-qrh-chi-finite`, `mourtada-2009-no-accumulation-hyperbolic-polycycles` in `research/claims/mourtada-2009-qrh-chi-finite.md`.
