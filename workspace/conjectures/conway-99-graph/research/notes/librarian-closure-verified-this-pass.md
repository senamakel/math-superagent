# Librarian closure verification — this pass

Status: **no acquisition performed; closure re-verified.** Reported by the
librarian role on request, against an already-closed library.

## Why nothing was downloaded

- The workspace directive (CONTEXT.md, operational) states the library is
  CLOSED: no further source acquisition except against a NEW gap a live
  phase-4 argument is blocked on, and none is posted.
- `derived/REQUESTS.md` holds exactly two rows, both already closed with
  `answers:` claims in the library:
  - `exact-list-prime-051a` → claim `automorphism-orders-consolidated`
    (`answers: exact-list-prime-051a`, note
    `automorphism-orders-consolidated.md`); also `wilbrink-order11-sourced`.
  - `published-mechanism-ruling-5cf8` → claim `srg33-mechanism-answers-request`
    (`answers: published-mechanism-ruling-5cf8`).
- The sole reserved acquisition `serve-supersimple-22242-existence` is **dropped**
  (resolved before acquisition: super-simple 2-(22,4,2) EXISTS constructively,
  CP-SAT OPTIMAL certificate `code/out/coclique_lift_clean_design.txt`, claim
  `super-simple-22242-exists` with `answers: super-simple-22242-gap`). Nothing
  to fetch; construction beats citation.
- No open librarian task exists in the `tasks` ledger.

## What this pass verified (all on disk)

1. **URL provenance in-place for every source.** All 48 full texts under
   `research/sources/*.full.md` carry a `<!-- source: <url> -->` header (grep
   matched 48/48 substantive files; the two non-matching are correction-record
   files that themselves state the correct URL). The `LIBRARY-REPORT.md` maps
   each file to its URL, DOI, and what it establishes.
2. **One summary per source.** Every `sources/*.full.md` has a companion
   `summaries/<name>.md`; summaries index at `research/summaries/index.md`.
3. **The canonical reference tier is present**: Brouwer's SRG tables (rows 9
   `!` exists, 99 `?` open), Wikipedia encyclopedic entries for the Conway
   99-graph and the BvLS graph, van Lint 1975 (five-member family, explicit
   BvLS construction), Conway's own Five $1000 Problems.
4. **Primary full texts in hand**, including the two the run depends on most:
   - `makhnev-1988-lambda1-russian-fulltext.full.md` — the open mathnet.ru
     Russian original (paperid=4220), Thm 1/Thm 2 of the n3≥1 conditional.
   - `behbahani-2009-phd-thesis-pdf.full.md` — primary thesis, orbit-matrix
     automorphism constraints (Thm 4.14).
   - `brouwer-neumaier-1988-combinatorica.full.md` — the μ=2 / partial-linear-
     space-of-girth-5 primary structural source; own table lists (99,14,1,2) '?'.
   - `shpectorov-zhao-srg85-full.full.md` — the closest successful nonexistence-
     by-local-enumeration precedent (k=14, μ=2, λ=3).
5. **Claims trace to these sources.** `automorphism-orders-consolidated`,
   `wilbrink-order11-sourced`, `c3`/`aut-cm-2020`/`aut-cw-2025`,
   `integrality-five-members`, `srg33-does-not-exist-integrality`, `c4`,
   `brouwer-neumaier-1988-99-open`, `makhnev1988-condstar-theorems` all cite a
   held full text, not recall.

## Known paywalled sources (recorded, do not re-attempt without a new reason)

Recorded in LIBRARY-REPORT.md / its "Could not obtain" list: Cameron 1975
"Partial quadrangles" (content fully carried by in-library secondaries);
Behbahani–Lam–Östergård 2012 JCTA (abstract captured); Behbahani–Lam 2011;
Makhnev–Minakova 2004; Bagchi 2006; von der Flaass 1984 abstract. Each is filled
by an in-hand primary/summary. None blocks a live argument.

## Conclusion

The local reference set is built, closed, internally consistent, and every
fact the run treats as load-bearing traces to a held source with a URL in the
file. No librarian action is warranted until a live phase-4 argument posts a
new gap in REQUESTS.md.
