# Librarian cycle — library re-verified complete; nothing further to add

**Date:** this cycle. **Role:** librarian. **Cognee:** down (6 memory-store
failures); this note is the workspace copy, as the Poonen gap note records the
same failure mode.

## What this cycle did

- Read `GOAL.md` and `research/ROOT.md` — phase-1 bar is met (minimal
  counterexample: `|F| ≥ 4·13 − 1 = 51`, `n ≥ 13`; verification: `n ≤ 12`
  Vučković–Živković 2017 computer-assisted, `|F| ≤ 50`; settled classes:
  lattice, graph-formulation, small-sets, large-families lines, each tied to a
  primary source on disk).
- Read `derived/REQUESTS.md` (ledger): one open row
  `exact-current-published-c8b8`. Verified by grep that **11 notes carry
  `answers: exact-current-published-c8b8`**
  (`research/notes/librarian-cycle-2026c-…`, `librarian-published-record-reconfirmed-2026`,
  `librarian-record-still-stable-2026`, summaries of AHS/Cambie/Das-Wu/Liu/
  published-status/current). The rendering is stale, not the gap: the request
  is answered. Do not re-ask.
- Read the frontier's top rows and grepped the sources tree:
  - Knill math/9409215 → `knill-graph-generated-1994.full.md` (on disk; cited by
    20+ files incl. AHS, Gilmer, Bruhn–Charbit–Schaudt–Telle, Das–Wu).
  - Balla–Bollobás–Eccles JCTA 2013 (doi 10.1016/j.jcta.2012.10.005) → on disk
    (cited in cambie, colbert-order-2026); **full text present as
    `balla-bollobas-eccles-union-closed-2012.full.md`**.
  - Reimer 2003 (10.1017/S0963548302005230) → `reimer-average-set-size-2003.trial.full.md`.
  - Czédli–Maróti–Schmidt Order 2009 (10.1007/s11083-008-9105-5) → on disk
    (czedli-publist + the 2009 full text `czedli-maroti-schmidt-scope-averaging-2009.full.md`).
  - Morris EJC 2004 (10.1016/j.ejc.2004.07.012) → `morris-fc-families-2007.full.md`.
  - Gowers polymath → `polymath-frankl-union-closed.full.md`; Wikipedia → on disk.
  - Lower-ranked rows (Extremal UC set families, Lozin–Zamaraev Horn, Pulaj MCOM,
    asymptotic AMS 2021, random bipartite graphs, Samotij entropy survey) are
    either on disk or cite-within-noise from files already held. No open lead.
- Read the two prior librarian audits
  (`librarian-reference-set-report.md`, `librarian-frontier-audit-2026.md`):
  both confirm the library is complete, the record stable (Yu ≈0.38234
  published; AHS (3−√5)/2 peer-reviewed EJC 2024 doi:10.37236/12232; Cambie
  ≈0.3823455 and Liu ≈0.38271 preprints), and 2025–2026 freshness searches
  surfaced nothing new.

## The one recorded unfillable gap (not re-attempted)

- **Poonen 1992, "Union-closed families", JCTA 59:253–268** — full text not
  obtainable: author's own site does not host it, ScienceDirect paywalled,
  no arXiv, ar5iv 404. Content represented by Poonen's own errata + survey
  restatement + Morris/Marić restatements. Gap note:
  `research/notes/poonen-1992-gap-reconfirmed.md`, falsifier stated (a free
  full text surfacing). Do not re-attempt.

## Conclusion

Phase 1 (library) is **finished**; the operator directive `stop-adding-sources`
is in force and this cycle found no source that would change a number. The
frontier is pinned and reproduced. Nothing further for the librarian to fetch:
active fronts (abundance-profile, Lean restate of the two false Ellis–Gilmer
goals, odd-filter minmax, g(n,m) envelope Lean) are computational/formalisation
tasks owned by other roles and fully supported by the library on disk.

## Durable-store note

Cognee was down when this was recorded; store this cycle's finding durably once
the memory server recovers (the earlier `librarian cycle` record did not
persist).