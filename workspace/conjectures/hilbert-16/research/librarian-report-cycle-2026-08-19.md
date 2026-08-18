# Librarian cycle report — 2026-08-19 (DRR citer walk; canonical gaps filled)

## What this cycle added (all primary or record-level, none guessed)

1. **DRR 1994 full MaRDI record** — `research/sources/drr-1994-jde-mardi-record.full.md`
   (Publication:1329269, zbMATH DE 4107805, OpenAlex W2054609165). Carries the
   complete **96-item citer list** with MaRDI ids. Last edited 12 Apr 2026.
   The DRR 1994 JDE paper itself (JDE 110(1):86–133) is paywalled everywhere
   (ScienceDirect 403 on both the article and the 1997 "cyclicity of graphics"
   survey S0362546X97001752).

2. **Roussarie 1998 book record** — `research/sources/roussarie-1998-book-mardi-record.full.md`
   (Modern Birkhäuser Classics, DOI 10.1007/978-3-0348-0718-0, Progr. Math.
   164). The book itself is paywalled; the record anchors it. Standard reference
   for the finite-cyclicity reduction.

3. **Écalle 1993, "Six Lectures on Transseries, Analysable Functions and the
   Constructive Proof of Dulac's Conjecture"** — full text held at
   `research/sources/ecalle-1993-six-lectures-transseries-dulac.full.md`
   (Springer NATO ASI vol 408, DOI 10.1007/978-94-015-8238-4_3, 120 frontier
   citations). This is the **accessible content of the frontier's top item**
   (Écalle 1992 Hermann book, print-only): Écalle's own English survey of the
   resummation machinery (resurgence, compensation, acceleration; transseries
   and analysable germs) with application (C) the non-accumulation of limit
   cycles. The 1992 book itself remains print-only; bibliographically anchored
   by 20+ held sources.

4. **Andronov–Leontovich–Gordon–Maier, "Theory of Bifurcations of Dynamic
   Systems on a Plane" (1967 Russian; 1971 English NASA TT F-556)** — full OCR
   text (32358 lines) at
   `research/sources/andronov-1971-bifurcations-dynamic-systems-plane-text.full.md`
   (archive.org nasa_techdoc_19710012507 djvu.txt; title page + preface
   verified). Frontier item #2 (34 citations). The canonical classical reference:
   separatrix loop, saddle-node loop, hyperbolicity of limit cycles, structural
   stability. The record page is also held at
   `research/sources/andronov-1971-bifurcations-dynamic-systems-plane.full.md`.

5. **Three unnamed frontier entries resolved via OpenAlex API** (not guessed;
   fetched from api.openalex.org, then cross-checked against held texts):
   - W1566141765 = Novikov–Yakovenko, "Tangential Hilbert problem for
     perturbations of hyperelliptic Hamiltonian systems", Trans. AMS 1999,
     DOI 10.1090/s1079-6762-99-00061-x — **already held**
     (`novikov-yakovenko-hyperelliptic-tangential-1999`).
   - W1981047244 = **Mardešić**, "An explicit bound for the multiplicity of
     zeros of generic Abelian integrals", Nonlinearity 4(3):845–852, 1991,
     DOI 10.1088/0951-7715/4/3/011 — cited in 8 held texts; not separately
     held. **New lead.**
   - W176407471 = "On Liénard's equation", LNM, DOI 10.1007/bfb0085364 —
     bibliographically anchored (likely Lloyd or Lins–de Melo–Pugh-adjacent).
     **New lead, record-level only.**

6. **Six DRR-1994 citer records resolved to pre-2015 dates** — Publications
   935124 (2008), 1272307 (1998), 5955940 (2002), 5931370 (2002), the
   qualitative-theory survey (2001), 2514027 (DMRT fake-saddle, 30 Jan 2015,
   JDE, DOI 10.1016/j.jde.2014.09.024 — already held as postprint).

## Negative finding (recorded, strengthens the two open ledger requests)

**The MaRDI 96-citer list of DRR 1994 contains NO post-2015 closure of any open
row.** Every closure-looking citer resolves to 1998–2008 work or to
already-held papers. Standing picture unchanged and strengthened:
≥89/121 fully closed by 2015; (I^1_6b),(H^3_13),(DI_2b) boundary-sets-only;
(H^3_14) open with Lu arXiv:2607.13785 the sole (unrefereed) claim; ≥11
degenerate graphics open. Full record: `research/librarian-cycle-2026-08-19-drr-citer-walk.md`.

## Fishkin thread — status after five attempts (still open)

- Correct AMS PDF URL from OpenAlex (`/mosc/2010-71-00/...pdf`, not the guessed
  `/journals/` path) → server returned the generic journal landing page, no
  article text.
- OpenAlex content PDF (`content.openalex.org/works/W2147420023.pdf`) → HTTP 429.
- CiteSeerX mirror (doi=10.1.1.309.2425) → connection failed.
- Doklady 2009 companion (DOI 10.1134/S1064562409050251) landing page held;
  body paywalled. Its reference list confirms the Mat. Zametki companion
  (Fishkin, Mat. Zametki 85(1):110–118, 2009).
- A **guessed** Mat. Zametki DOI resolved to an unrelated network-matrix paper —
  **neutralised** with WRONG-PAPER header
  (`research/sources/fishkin-2009-mat-zametki-85-1.full.md`) and an incident
  record (`research/findings/wrong-fetch-fishkin-mat-zametki-doi-guessed-2026-08-19.md`).
  Second instance of the guessed-identifier failure; generalises the mathnet
  paperid lesson to **never guess any publisher DOI**.
- The claimed constants (10^72 / 10^77 / δ^{−33}) remain search-level recall,
  NOT verified primary text. Claim
  `fishkin-perturbed-center-qualified-bound` updated with all five attempts.

## Memory

Cognee recovered this cycle; four verified findings stored (DRR citer-walk
negative; Écalle 1993 holding; Andronov 1971 holding; wrong-fetch lesson).

## Open requests status

- `complete-current-ledger-cb3d`, `dumortier-rousseau-rousseau-9c4f`: still
  open, now with a sourced negative (no post-2015 closure in the DRR 1994 citer
  record) and an identified falsifier (any post-2015 closure paper or a
  consolidated ledger). Best next route when the citation API recovers: walk
  citations of arXiv:1506.07104 (RR 2015) and arXiv:1502.00689 (RSZ 2015)
  directly.
- Fishkin constants: open, all routes exhausted this cycle.

## Next-cycle leads (from this cycle's frontier additions)

- Mardešić 1991 (Nonlinearity 4:845–852) — the explicit generic-Abelian
  multiplicity bound; candidate for a full download.
- "On Liénard's equation" (LNM, DOI 10.1007/bfb0085364) — identify authors/year
  and decide.
- The 100+ new frontier rows added by the MaRDI and Springer downloads.
