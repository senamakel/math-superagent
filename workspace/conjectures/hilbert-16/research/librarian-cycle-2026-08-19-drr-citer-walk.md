# Librarian cycle — DRR 1994 citer walk and ledger negative (2026-08-19)

## What this cycle established

The two open requests (`complete-current-ledger-cb3d`,
`dumortier-roussarie-rousseau-9c4f`) ask for a complete current open/closed
ledger of the 121 DRR graphics. The DRR 1994 JDE paper itself (JDE 110(1),
86–133, DOI 10.1006/jdeq.1994.1061) is paywalled everywhere (ScienceDirect 403
for both the article and the "cyclicity of graphics" survey
S0362546X97001752); its abstract is now held at MaRDI-record level.

## What was added

1. **MaRDI full record for DRR 1994** — `research/sources/drr-1994-jde-mardi-record.full.md`
   (URL `https://portal.mardi4nfdi.de/wiki/Publication:1329269`). Carries the
   complete 96-item citer list with MaRDI publication ids, MSC classes
   (34C05/34C23/34C25), zbMATH DE 4107805, OpenAlex W2054609165, last edited
   12 April 2026. This is now the run's best proxy for "who cited DRR 1994",
   since the citation graph API is rate-limited.
2. **MaRDI record for Roussarie 1998 book** — `research/sources/roussarie-1998-book-mardi-record.full.md`
   (Publication:371910, Modern Birkhäuser Classics, DOI 10.1007/978-3-0348-0718-0,
   Progress in Math vol 164). Bibliographic anchor for the standard reference on
   the reduction; the book itself is not freely available.
3. **Six citer records resolved** (all MaRDI publication pages, all pre-2015):
   - Publication:935124 — "Cyclicity of several planar graphics and ensembles
     through three singular points without generic conditions", 31 Jul 2008.
   - Publication:1272307 — "Cyclicity of planar polycycles and ensembles with
     codimension 3 degeneration through a saddle-node and two hyperbolic
     saddles", 21 Dec 1998.
   - Publication:5955940 — "Cyclicity of elementary polycycles and ensembles
     with codimension 3 degeneration", 18 Feb 2002.
   - Publication:5931370 — "Ergodicity of limit cycles in quadratic systems",
     3 Feb 2002.
   - Qualitative theory of two-dimensional polynomial dynamical systems (survey
     chapter), 13 Feb 2001.
   - Publication:2514027 — "Cyclicity of a fake saddle inside the quadratic
     vector fields", 30 Jan 2015, JDE, DOI 10.1016/j.jde.2014.09.024 — this is
     the DMRT 2015 fake-saddle paper, already held as postprint
     (`demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md`).

## Negative finding for the ledger requests

**The MaRDI 96-citer list of DRR 1994 contains no post-2015 closure of any open
row.** Every citer that looks like a closure ("Cyclicity of ... graphics ...",
"Cyclicity of ... polycycles ...") resolves to 1998–2008 work of the Chinese
school or to already-held papers. Combined with the prior cycle's finding (no
consolidated post-2020 ledger; Lu arXiv:2607.13785 unrefereed sole claim on
H^3_14), the standing picture is unchanged and *strengthened*:

- ≥89/121 fully closed by 2015 (88 RSZ + I^1_14 RR);
- (I^1_6b), (H^3_13), (DI_2b) boundary-sets-only (RR 2015 Thm 1.1);
- (H^3_14) open, Lu 2026 preprint the sole claim;
- ≥11 degenerate graphics open (Shan 2013);
- no post-2015 closure located anywhere in the citer record as of the MaRDI
  page's last edit (12 Apr 2026).

This does NOT close the requests — the MaRDI citer list is not an exhaustive
ledger (e.g. it may not list every citing paper) — but it is a bounded,
sourced negative for "the run's open-row inventory is missing a known closure".

## Falsifier still open

A single post-2015 paper closing (I^1_6b), (H^3_13), (DI_2b), (H^3_14), or any
of the 11 degenerate graphics, or a consolidated ledger with a different open
count, would refute the standing picture. The citation-graph API was
rate-limited this entire cycle; when it recovers, walk RR 2015
(arXiv:1506.07104) and RSZ 2015 (arXiv:1502.00689) citations directly.

## Memory

`remember_memory` was not attempted this cycle (Cognee down per CONTEXT.md and
recall returned empty). Durable record = this note + the six source files.
