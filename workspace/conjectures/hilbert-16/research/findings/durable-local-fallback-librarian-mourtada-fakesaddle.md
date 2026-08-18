# Durable local fallback — librarian cycle (Mourtada PDF + fake-saddle caveat)

Cognee was unavailable when durable storage was attempted (memory server health
check did not answer within 8 seconds; both `remember_memory` calls refused).
The following source-backed findings are recorded in the workspace instead and
must be stored to Cognee once the service recovers.

## 1. Mourtada Théorème 0 conclusion recovered from the arXiv PDF

- Full text: `research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md`
  (219709 B, 6399 lines, indexed), source URL https://arxiv.org/pdf/0912.1560v1.
- Théorème 0, complete (lines 50–62): for an analytic q-parameter unfolding
  X_ν of a real monodromic hyperbolic polycycle X_0 (eigenvalue ratio −1 at
  each singularity, "for simplicity"), there exist integers N and L and
  neighborhoods Γ_k ⊂ U ⊂ U_0, V ⊂ (ℝ^q,0) such that (i) for all ν ∈ V the
  number of limit cycles of X_ν in U is ≤ N, and (ii) the multiplicity of each
  is ≤ L.
- This closes the truncation gap in `research/findings/mourtada-theoreme-0-truncation.md`.
- Finding: `research/findings/mourtada-theoreme-0-recovered-from-pdf.md`.
- Claim updated: `mourtada-2009-no-accumulation-hyperbolic-polycycles` in
  `research/claims/mourtada-2009-qrh-chi-finite.md`.

## 2. Fake-saddle / DRR degree-2 programme caveat verified verbatim

- DMRT 2015 (JDE 258(2):588–620, held postprint) lines 70–76: the fake-saddle
  singularity "has in fact no contribution in the degree-2 programme outlined
  by Dumortier, Roussarie and Rousseau: in that programme, homogeneous vector
  fields could be avoided using rescalings."
- Consequence: fake-saddle cyclicity (DMRT ≥2; Marín 2026 uniform expansion)
  does NOT close any DRR 121-graphic row. The thread
  `fake-saddle-transition-maps`'s DRR-closure direction is closed; the uniform
  expansion remains a division-in-flat-class template only.
- Finding: `research/findings/fake-saddle-drr-programme-caveat-verified.md`.
- Thread updated: `research/threads/fake-saddle-transition-maps.md`.

## Retry Cognee only after service recovery.
