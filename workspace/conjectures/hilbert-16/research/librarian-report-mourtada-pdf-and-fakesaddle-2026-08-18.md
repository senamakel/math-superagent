# Librarian cycle report — Mourtada Théorème 0 PDF recovery, fake-saddle DRR-caveat verification

## What this cycle did

The library was already mature (ROOT.md phase-1 criterion met; ~170 sources
held across every goal axis). This cycle worked the two live gaps that were
still open after prior passes:

1. **Mourtada Théorème 0 truncation** — a precisely-scoped open gap recorded in
   `research/findings/mourtada-theoreme-0-truncation.md`, whose stated action
   was to fetch the arXiv PDF and read Théorème 0's conclusion from it.
2. **The `fake-saddle-transition-maps` thread's blocking question** — whether
   fake-saddle cyclicity contributes to the DRR degree-2 programme, which the
   thread's own note flagged as needing a primary-source anchor.

## 1. Mourtada PDF now held — truncation gap closed

- **Fetched:** https://arxiv.org/pdf/0912.1560v1 (736579 bytes → 219709 B of
  converted Markdown, 6399 lines, 40085 words).
- **Held at:** `research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md`
  (indexed); proper summary written to
  `research/summaries/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.md`
  (replacing the auto-generated structural digest).
- **Théorème 0 complete, from the PDF (lines 50–62):** for an analytic
  q-parameter unfolding X_ν of a real monodromic hyperbolic polycycle X_0,
  there exist integers N and L and neighborhoods Γ_k ⊂ U ⊂ U_0, V ⊂ (ℝ^q,0)
  such that (i) the number of limit cycles of X_ν in U is ≤ N for all ν ∈ V,
  and (ii) the multiplicity of each is ≤ L. This is exactly the content the
  ar5iv HTML conversion dropped.
- **Updated:** claim `mourtada-2009-no-accumulation-hyperbolic-polycycles`
  (statement now complete, PDF anchor added, truncation caveat removed);
  CONTEXT.md established-ledger line; finding
  `research/findings/mourtada-theoreme-0-recovered-from-pdf.md`.
- **Why it matters:** Lu 2607.13785 cites Mourtada [3] for the QRH theorem
  behind its Theorem 36 (thread `lu-h14-3-verification`). Théorème 0's N, L
  uniformity is the shape of the uniform bound Lu assembles; the authoritative
  copy is now local.

## 2. Fake-saddle / DRR programme caveat verified verbatim

- **Question:** does the Marín 2026 uniform fake-saddle transition-map
  expansion (held) certify finite cyclicity of an open degenerate DRR graphic?
- **Answer — no, from the primary source:** De Maesschalck–Rebollo-Perdomo–
  Torregrosa 2015 (JDE 258(2):588–620, held UAB postprint), lines 70–76:
  "the study of the singularity at X0 has in fact no contribution in the
  degree-2 programme outlined by Dumortier, Roussarie and Rousseau: in that
  programme, homogeneous vector fields could be avoided using rescalings."
- **Recorded:** finding `research/findings/fake-saddle-drr-programme-caveat-verified.md`;
  thread `fake-saddle-transition-maps` updated — the DRR-closure direction is
  closed; the uniform expansion remains a division-in-flat-class template for
  the run's adopted slow-divergence/ECT route, not a DRR closure.
- **Evidence label:** asserted-by-source, quoted from the held postprint.

## 3. Standing requests — unchanged, re-confirmed

The two open requests (`complete-current-ledger-cb3d`,
`dumortier-roussarie-rousseau-9c4f`: the complete 121-graphic DRR ledger)
remain unfillable from a single open source — no post-2020 consolidated ledger
exists; the triangulated picture (≥89/121 closed by 2015, (I¹₆b),(H³₁₃),(DI₂b)
boundary-only, (H³₁₄) open with Lu 2026 claiming it, ≥11 degenerate open) is
the honest statement. DRR 1994 raw catalogue remains paywalled.

## Memory

Cognee was down (health check timed out; both `remember_memory` calls refused).
Both findings were written to the durable local fallback
`research/findings/durable-local-fallback-librarian-mourtada-fakesaddle.md`
and must be stored to Cognee on service recovery.

## Boundaries

No theorem, computation, or Lean formalisation was produced in this
librarian-only cycle. All claims are asserted-by-source. Nothing here claims
H(n) < ∞ or H(2) = 4.
