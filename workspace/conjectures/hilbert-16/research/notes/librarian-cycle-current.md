# Librarian cycle — canonical Ilyashenko–Yakovenko text, Lu bundle scripts, false-resolution sweep

## Ilyashenko–Yakovenko *Lectures on Analytic Differential Equations* (GSM 86) — now held

```claim
id: iy-lectures-analytic-de-held-draft
statement: The canonical monograph Ilyashenko & Yakovenko, "Lectures on Analytic
  Differential Equations", AMS Graduate Studies in Mathematics 86 (2008) is now
  held in this library as the authors' own hosted draft PDF
  (https://www.wisdom.weizmann.ac.il/~yakov/thebook.pdf, full text
  research/sources/ilyashenko-yakovenko-lectures-analytic-de-thebook.pdf.full.md).
  It covers desingularization, normal forms, quadratic fields & the Bautin theorem
  (M(2)=3), and zeros of parametric families of analytic functions / small-amplitude
  limit cycles (§12–13) — the analytic scaffolding under the DRR program.
hypotheses: content-level use only; the front matter warns this is an OUTDATED
  DRAFT and "do not quote this draft to avoid misleading enumeration of pages,
  theorems and definitions", so its numbering does not match the printed GSM 86.
holds-here: yes (as a content/definitions reference, NOT for page/theorem citations)
status: asserted
bearing: fixes the standard canonical reference tier; one of the two named starting
  places in problem.md. The other (Roussarie 1998 bifurcations book) remains
  unobtainable (paywalled).
anchor: research/sources/ilyashenko-yakovenko-lectures-analytic-de-thebook.pdf.full.md
```

## Lu 2026 bundle scripts — both held, asserted-by-source

The two scripts CONTEXT gap-2 listed as "still not held" are BOTH in the library:

- `verify_h14_center_bautin.py` → `research/sources/lu-h14-3-verify-center-bautin.py.full.md`, claim `lu-h14-3-bautin-focal-values-u0` (L1=(AC+CD+2DF−EF)/8, both center components annihilate L2, U(0)=1/48).
- `verify_h14_center_global_domains.py` → `research/sources/lu-h14-3-verify-center-global-domains.py.full.md`, claim `lu-h14-3-global-center-domains-checked-statements` (first-integral/barrier and inverse-integ factor/gate identities on the two H14³ center components).

Both are **asserted-by-source**, not yet re-executed in this workspace; capturing a clean-room run to `code/out/` would upgrade each to `checked`.

## False-resolution sweep — Fradkin Zenodo 2025 recorded, not adopted

Zenodo 10.5281/zenodo.17171213 ("Energetic–Symmetry Resolution of Hilbert's 16th Problem (Part II)", Fradkin 2025-09): claims to resolve H16.2 in full generality with sharp asymptotics H(d)~c·d⁴. Assessed and **rejected as a credible resolution**: unrefereed; no reliance on analyticity of the Poincaré return map (the exact Test-1 failure of problem.md); ad-hoc "energetic–symmetry/energetic pyramids" vocabulary; classified under geochemistry/geological modeling topics; and it claims a c·d⁴ upper law needing to sit above (not contradict) the held n²logn lower bound without any construction crossing it. Same false-resolution shape as Pedregal's arXiv variational claim (already held and refuted in thread `pedregal-variational-claim-test`). Recorded as a warning; nothing built on it.

## Requests status

- `dumortier-roussarie-rousseau-9c4f` / `complete-current-ledger-cb3d` (full DRR 121-ledger): still open at the level of the exact open-count; documented as a literature question already closed (no post-2020 consolidated ledger exists; best primary is Shan 2013 Table 1.1). Triangulated inventory in `research/drr-list.md`.
- Roussarie book, DRR 1994, Dulac 1923 full text, Żołądek 1995 primary: all genuinely unobtainable (paywalled / oversized), recorded in LIBRARY-STATUS.

## What is now available locally (updated)

- Canonical tier: Ilyashenko–Yakovenko GSM 86 held (draft). Hilbert's original problems (Newson), Ilyashenko Centennial History, Llibre's Abel→H16 survey, Kaloshin, Roussarie–Rousseau, DRR closure papers — held in prior passes.
- Instrument chain: mourtada polycycles, Marin–Villadelprat hemicycles & Dulac maps, Dumortier–Ilyashenko–Rousseau saddle-node, Kaisser–Rolin–Speissegger o-minimal, BNY/Binyamini–Dor Abelian bounds — held.
- Lower bounds primary: Christopher–Lloyd, Prohens–Torregrosa, Torregrosa 2024 (12 cycles), Yu–Han + Tian–Yu (Żołądek 11) — held.
