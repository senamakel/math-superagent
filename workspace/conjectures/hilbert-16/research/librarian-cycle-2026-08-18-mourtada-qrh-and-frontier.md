# Librarian cycle — 2026-08-18 (continuation): Mourtada QRH source, Dulac record, frontier resolution

## Scope
Library is mature (ROOT.md phase-1 criterion met). This cycle worked the run's
active verification thread (`lu-h14-3-verification`) and the frontier's top
rows, rather than broadening.

## Newly held sources
1. **Mourtada 2009, "Action de dérivations irréductibles sur les algèbres
   quasi-régulières d'Hilbert"** — arXiv:0912.1560 (94 pp, French):
   - `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert.full.md` (abstract page)
   - `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md` (full text, 362644 B, 85 sections)
   - **Why it matters:** Lu arXiv:2607.13785 (the H14³ closure the run is
     verifying) cites Mourtada [3] as the QRH theorem behind its Thm 36
     (all-hyperbolic QRH theorem). Previously cited without the source being
     readable; now held in full.
2. **Dulac 1923, "Sur les cycles limites"** — Numdam record only:
   `research/sources/dulac-1923-sur-les-cycles-limites-numdam.full.md` (DOI
   10.24033/bsmf.1031). The 144-page body is too large for the downloader
   (fetch refused); the record fixes the citation anchor. The analysis of
   Dulac's error is carried by held Ilyashenko 2002 / Ilyashenko 2016 / Yeung 2024.

## What the Mourtada source establishes (asserted-by-source)
- **Théorème IVC1:** QRH^{k,.} algebras are locally χ-finie for irreducible
  Hilbert derivations χ: finite degree of the integral projection on fibers,
  Noetherian/locally-Noetherian differential ideals, and the double inclusion
  (θ^n)π_χ*(J) ⊂ I_{χ,f} ⊂ π_χ*(J).
- Reduced singularities of χ after desingularisation: χ_ℓ = ρ∂/∂ρ − Σ s_j u_j ∂/∂u_j.
- **Théorème 0 / application:** no accumulation of limit cycles on hyperbolic
  polycycles in compact analytic families on S², including polycycles that are
  accumulations of cycles. **Caveat:** Théorème 0's numerical conclusion
  (integers N, L) is truncated in the ar5iv HTML conversion — recorded in
  `research/findings/mourtada-theoreme-0-truncation.md`; the PDF is the
  authoritative copy if those numbers are ever needed.
- Claims filed: `mourtada-2009-qrh-chi-finite`, `mourtada-2009-no-accumulation-hyperbolic-polycycles`
  in `research/claims/mourtada-2009-qrh-chi-finite.md`.

## DRR catalogue: re-confirmed unfillable from open sources
- ScienceDirect 403 on the 1997 survey (S0362546X97001752); no open PDF of DRR
  1994 (JDE 110:86-133) in a fresh search. Third librarian pass confirms the
  earlier conclusion. Requests `dumortier-roussarie-rousseau-9c4f` and
  `complete-current-ledger-cb3d` stay open. The honest ledger stands:
  ≥89/121 fully closed by 2015 (88 RSZ + I¹₁₄ RR), (I¹₆b),(H³₁₃),(DI₂b)
  boundary-only, (H³₁₄) claimed by Lu 2026 (verification open), ≥11 degenerate
  open per Shan 2013.

## Frontier resolution
Resolved four untitled high-count rows via citation_graph — all already held:
- W135561972 = Roussarie 1988 "A note on finite cyclicity property and Hilbert's 16th problem" (record-level, cited throughout held sources)
- W1566141765 = Novikov–Yakovenko 1999 hyperelliptic tangential Hilbert (held full)
- W1980673640 = Gavrilov 1998 Petrov modules (held full via Gavrilov 1999)
- Françoise 1996 successive derivatives (record-level, cited in BNY 2008)
No new downloadable gap from the frontier's top rows; the remaining top rows
(Écalle 1992 book, Andronov–Leontovich–Gordon–Maier, Arnol'd et al.
Singularities of Differentiable Maps, Ilyashenko 1991 monograph) are classic
paywalled monographs with records held.

## Lu citation-spine completeness
Lu's 7 references: DRR94 (paywalled record), Dumortier–Ilyashenko–Rousseau 2002
(held), Mourtada 2009 (NOW HELD), Roussarie–Rousseau 2015 (held), Marín–
Villadelprat 2025 (held), Krantz–Parks 2002 (standard text, record-level),
Hervé 1963 (standard text, cited in IY book). The only unavailable primary item
in Lu's spine is DRR94 itself, already tracked as the run's top request.

## Memory
Stored in Cognee: Mourtada 2009 QRH χ-finiteness + no-accumulation + the
truncation caveat (note 3429898854370069147).

## Boundaries
No new theorem, computation, or Lean formalisation was produced in this
librarian-only cycle. All claims are asserted-by-source. The requests ledger is
unchanged except that the Mourtada truncation is now a precisely-scoped open gap
(anchored in the finding file and the claim block).
