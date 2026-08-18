# Mourtada 2009: quasi-régulières d'Hilbert algebras are χ-finite — source now held

```claim
id: mourtada-2009-qrh-chi-finite
statement: Mourtada (arXiv:0912.1560, 94pp, Amstex) proves: for an irreducible derivation χ acting on a Hilbert quasi-regular algebra QRH^{k,.} of germs at 0 of real-analytic functions on a semi-algebraic open set (U,0), the algebra is locally χ-finite — the degree of the integral projection π_χ restricted to fibers of elements of QRH is finite, and the differential ideals I_{χ,f} are Noetherian or locally Noetherian — and satisfies locally the double inclusion (θ^n)π_χ*(J_{χ,f,γ}) ⊂ I_{χ,f} ⊂ π_χ*(J_{χ,f,γ}) relating the differential ideal of f to the saturation of its transverse ideal, where θ = ∏ x_j generates the ideal of the boundary B_k = {∏ x_j = 0} and n is the multiplicity m_χ(f), linked to an algebraic multiplicity ma_χ(f).
hypotheses: χ an irreducible (Hilbert) derivation realized on U ⊂ (ℝ^{+*})^k × ℝ^q, with Sing(χ) ⊂ (B_k, 0), B_k invariant under the flow of χ; QRH^{k,.} quasi-analytic in the x-coordinates (QRH ∩ ∩_n M_x^n = {0}) with elementary Ecalle–Khovanskii asymptotic structure; U semi-algebraic open; the germ f ∈ QRH^{k,.}. Theorem 0 additionally assumes X_ν an analytic q-parameter unfolding of X_0, a real monodromic hyperbolic polycycle Γ_k with k singularities (eigenvalue ratio −1 at each singularity, stated "uniquement pour simplifier la présentation").
holds-here: yes — Lu arXiv:2607.13785 cites Mourtada [3] as the QRH theorem source, applied "only to an analytic all-hyperbolic word after its sections, connectors, Hilbert derivation, integral fibers, and closing germ have been realized on one common positive-corner neighborhood" (Lu §1). This held source is that citation.
status: asserted-by-source (French text, held in full; not independently formalised)
falsifier: a correction to Mourtada 2009 weakening χ-finiteness of QRH to non-Noetherian differential ideals, or a demonstration that the double inclusion's algebraic multiplicity bound fails for the all-hyperbolic words Lu constructs; either would break Lu's QRH theorem application.
sources: https://arxiv.org/abs/0912.1560 ; https://ar5iv.labs.arxiv.org/html/0912.1560
anchors: research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md lines 20-33 (Théorème 0), 570-579 (Théorème principal II1), 1170-1237 (Théorème principal IIIA1), 1262-1267 (Théorème principal IIIB1), 1898-2013 (Théorème IVC1)
```

```claim
id: mourtada-2009-no-accumulation-hyperbolic-polycycles
statement: Application of the QRH χ-finiteness theorems: inside compact analytic families of vector fields on the 2-sphere S², there is no accumulation of limit cycles on hyperbolic polycycles — including the case of a polycycle that is itself an accumulation of cycles. Theorem 0: for an analytic q-parameter unfolding X_ν of a real monodromic hyperbolic polycycle X_0, there exist integers N and L and neighborhoods Γ_k ⊂ U ⊂ U_0 and V ⊂ (ℝ^q, 0) such that (i) for all ν ∈ V, the number of limit cycles of X_ν in U is bounded by N, and (ii) the multiplicity of each such limit cycle is bounded by L.
hypotheses: analytic family on S²; hyperbolic monodromic polycycle; q parameters finite. Theorem 0 restricts the eigenvalue ratio at each singularity to −1 "for simplicity of presentation".
holds-here: yes — this is the analytic input class Lu's QRH theorem (Lu 2607.13785 Theorem 36) applies to all-hyperbolic words in the H14^3 hemicycle analysis.
status: asserted-by-source; the exact numerical content of Theorem 0's conclusion was truncated in the ar5iv HTML conversion and is NOW RECOVERED from the arXiv PDF v1 (see anchors) — the statement (i)+(ii) above is complete.
formalisation: code/lean/Lib/Mourtada2009.lean — the theorem stated as Cited axiom `mourtada_theoreme_0` + wrapper `mourtada_theoreme_0_uniform_bound`, self-contained (single-file kernel: IsLimitCycle/LimitCycleSet inlined from Statement.lean). UNCOMPILED as of the scholar pass — no lean_check verdict filed; status stays `asserted` until a passing verdict exists. The `MultiplicityOf` predicate is a True placeholder pending the displacement formalism, so even a passing compile would make the count bound exact and the multiplicity bound a scaffold.
falsifier: a compact analytic family on S² with a hyperbolic polycycle accumulating limit cycles (which would contradict Dulac finiteness as strengthened by Mourtada's uniformity); or a demonstration that Lu's all-hyperbolic words fail Mourtada's realized-connectors hypotheses.
sources: https://arxiv.org/abs/0912.1560 ; https://arxiv.org/pdf/0912.1560v1 ; https://ar5iv.labs.arxiv.org/html/0912.1560
anchors: research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md lines 50-62 (Théorème 0 complete, PDF conversion); research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md lines 20-33 (Théorème 0, truncated), 1898-2013 (Théorème IVC1)
```

## Why this matters to the run

The `lu-h14-3-verification` thread verifies Lu's claim of **local uniform finite
cyclicity of the H14³ semihyperbolic hemicycle**. Lu's Part III "QRH theorem"
(Theorem 36, "All-hyperbolic QRH theorem") rests on Mourtada's QRH machinery,
which the library previously did **not** hold — Lu's [3] was cited without its
source being readable. Now the source is in the library:

- **QRH^{k,.} locally χ-finite + double inclusion** (Théorème IVC1) is the
  analytic backbone.
- The reduced singularities of χ after desingularisation take the explicit form
  χ_ℓ = ρ ∂/∂ρ − Σ_{j=1}^ℓ s_j u_j ∂/∂u_j (ℓ = 0..k−1), which is the exact
  algebraic model Lu's "compact analytic words" must match.
- Theorem 0's uniformity (integers N, L over neighborhoods U × V) is the shape
  of the uniform bound Lu assembles — but the held conversion truncates its
  conclusion, so if Lu's proof ever needs Mourtada's actual N, L the PDF must
  be fetched and read (ar5iv conversion is lossy on displayed equations).

## Availability record

- Abstract page: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert.full.md` (6361 B).
- Full text: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md` (362644 B, 85 sections, 2506 lines).
- Both carry the source URL in the document header. The ar5iv conversion drops
  parts of displayed equations (Théorème 0's conclusion), so the arXiv PDF is
  the authoritative copy if exact statement content is needed.
