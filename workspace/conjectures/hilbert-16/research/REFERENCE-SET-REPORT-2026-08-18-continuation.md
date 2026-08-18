# Librarian reference set — completion report

**Run:** 2026-08-18 (continuation). **Problem:** Hilbert's 16th problem,
Part II — `H(n) < ∞` (uniformity for planar polynomial vector fields), with the
displacement-function / Bautin-ideal / DRR-graphics frame from `problem.md` and
`GOAL.md`.

The library was already mature when this cycle began (ROOT.md phase-1 criterion
met, ~170 sources held). This cycle closed the two remaining precisely-scoped
librarian gaps and re-confirmed the standing unfillable ones.

---

## What is now available locally (this cycle's additions)

### 1. Mourtada 2009 — arXiv PDF v1, full text (NEW, closes a recorded gap)

- **Source URL:** https://arxiv.org/pdf/0912.1560v1
- **Held at:** `research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md`
  (219709 B, 6399 lines, 40085 words; indexed and searchable)
- **Summary:** `research/summaries/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.md`
- **What it settles:** the ar5iv HTML conversion truncated **Théorème 0's
  conclusion**; the PDF recovers it completely (lines 50–62): for an analytic
  q-parameter unfolding X_ν of a real monodromic hyperbolic polycycle X_0,
  there exist integers **N and L** and neighborhoods Γ_k ⊂ U ⊂ U_0, V ⊂ (ℝ^q,0)
  such that (i) the number of limit cycles of X_ν in U is ≤ N for all ν ∈ V,
  and (ii) the multiplicity of each is ≤ L. This is the analytic uniformity
  input behind Lu 2607.13785's QRH application (thread `lu-h14-3-verification`).
- **Finding:** `research/findings/mourtada-theoreme-0-recovered-from-pdf.md`;
  claim `mourtada-2009-no-accumulation-hyperbolic-polycycles` updated (truncation
  caveat removed, PDF anchor added); CONTEXT.md established-ledger line updated.

### 2. Fake-saddle / DRR degree-2 programme caveat — verified verbatim

- **Source:** De Maesschalck–Rebollo-Perdomo–Torregrosa 2015, JDE 258(2):588–620
  (held UAB postprint, `research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md`,
  lines 70–76).
- **What it settles:** the thread `fake-saddle-transition-maps`'s blocking
  question — *does fake-saddle cyclicity close a DRR graphic?* — is answered
  **no** by DMRT's own text: the fake saddle "has in fact no contribution in
  the degree-2 programme outlined by Dumortier, Roussarie and Rousseau: in that
  programme, homogeneous vector fields could be avoided using rescalings."
  The DRR-closure direction of the thread is closed; the Marín 2026 uniform
  expansion remains a division-in-flat-class template only.
- **Finding:** `research/findings/fake-saddle-drr-programme-caveat-verified.md`;
  thread file updated.

### 3. Both findings stored in Cognee (memory recovered mid-cycle)

Fallback file kept at `research/findings/durable-local-fallback-librarian-mourtada-fakesaddle.md`.

---

## Standing state of the reference library (unchanged, re-confirmed)

- **~170 full-text sources** in `research/sources/`, each with a digest in
  `research/summaries/` and the source URL in its header — covering every axis
  the goal names: Dulac/Écalle–Ilyashenko finiteness and the Yeung gap-challenge,
  the DRR 121-graphics programme (RSZ 2015, Roussarie–Rousseau 2015, Shan 2013
  thesis, DGR 2002, DRR companions at abstract level), nilpotent/degenerate
  graphics (Zhu–Rousseau, Roussarie–Rousseau 2008, Marín–Villadelprat
  hemicycles), Bautin ideal / Lyapunov quantities (Bautin 1952, Villanueva–
  Tucker), Abelian integrals (BNY, Binyamini–Dor, Gavrilov, Grau–Mañosas–
  Villadelprat, Figueras–Tucker–Villadelprat), Liénard/canards (DPR, Huzak,
  De Maesschalck–Dumortier), o-minimality (Kaiser–Rolin–Speissegger),
  lower bounds (Christopher–Lloyd, Gasull–Santana, monomial variant), and the
  disputed Pedregal variational claim.
- **Canonical tier:** Encyclopedia of Mathematics, MathWorld, Scholarpedia,
  Ilyashenko 2002 Centennial History (Bull. AMS), Hilbert 1900 original
  problems, Ilyashenko–Yakovenko Lectures — all held.
- **DRR status ledger** (the two open requests): re-confirmed unfillable from a
  single open source — no consolidated post-2020 graphic-by-graphic ledger
  exists. Honest triangulated picture: ≥89/121 fully closed by 2015;
  (I¹₆b),(H³₁₃),(DI₂b) boundary-sets-only; (H³₁₄) open with Lu 2026 unrefereed
  claim; ≥11 degenerate graphics open (DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a,
  DI2b, DH3, DH4, DH5). DRR 1994 raw catalogue (JDE 110:86–133) remains
  paywalled — its content is substantively reproduced by the held full texts.

## Not obtained (genuine, re-confirmed this cycle)

- DRR 1994 raw 121-graphic catalogue (paywalled).
- DRR 1994 Nonlinearity 7(3):1001 and DRR 1996 Nonlinearity 9(5):1209 full
  texts (bot-captcha/paywall; abstracts held).
- Roussarie 1998 book; Planar Dynamical Systems (De Gruyter) — classic
  paywalled monographs; their specific results are held in the primary papers.

## Evidence discipline

Everything added this cycle is `asserted-by-source`, quoted from held primary
full texts with line anchors. No theorem, computation, or Lean formalisation
was produced in this librarian cycle; nothing here claims H(n) < ∞ or H(2) = 4.
