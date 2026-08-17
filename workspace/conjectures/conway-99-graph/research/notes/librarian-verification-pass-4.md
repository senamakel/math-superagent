# Librarian verification pass — attempt 4

State: the Conway 99-graph reference library is COMPLETE and phase 1 is CLOSED.

## What was verified this cycle (no new acquisition required)

The library on disk under `research/` already holds 48 full texts (`sources/`),
one summary per source (`summaries/`), and ~60 notes (`notes/`). Phase 1 was
declared closed in `ROOT.md`. The librarian's only job this cycle was to confirm
the canonical reference tier and the claims it supports, against the rule that
"anything cited must be in the library".

### Canonical encyclopedia/statement tier — confirmed present and real

| Source | File | URL (in file) | Verified |
|---|---|---|---|
| Wikipedia, Conway's 99-graph problem | `sources/wikipedia-conway-99-graph.full.md` | en.wikipedia.org/wiki/Conway%27s_99-graph_problem | Yes — open status, locally 7K2, five-member list, references (Biggs, Wilbrink, Makhnev–Minakova, Behbahani–Lam) |
| Wikipedia, Berlekamp–van Lint–Seidel graph | `sources/wikipedia-berlekamp-vanlint-seidel-graph.full.md` | en.wikipedia.org/wiki/Berlekamp%E2%80%93van_Lint%E2%80%93Seidel_graph | Yes — (243,22,1,2), 2673 edges, Golay-code origin, Berlekamp–van Lint–Seidel 1973 reference |
| Conway's Five $1000 Problems | `summaries/conway-five-1000-problems.md` | oeis.org/A248380/a248380.pdf | Yes — Problem 2 verbatim; prize origin 2017 update |
| Brouwer's SRG tables | `sources/brouwer-srg-table-{1-50,51-100,101-150}.full.md` | aeb.win.tue.nl/graphs/srg/… | Yes — row `? 99 14 1 2 \| 3 54 \| -4 44` open |

### Primary structural sources — confirmed real (content, not landing pages)

- **Makhnev 1988, "Strongly regular graphs with λ=1"** — Russian full text in
  `sources/makhnev-1988-lambda1-russian-fulltext.full.md` (URL mathnet.ru
  paperid=4220). Grep confirms ТЕОРЕМА 1 and ТЕОРЕМА 2 are present, condition
  (*) is stated, and the proof of Thm 2 (Lemmas 6–9, the 33-point closure) is
  in the body. This is the source of the n₃=0 ⇒ nonexistence conditional.
- **Brouwer–Neumaier 1988, Combinatorica 8:57–61** — full text in
  `sources/brouwer-neumaier-1988-combinatorica.full.md` (ir.cwi.nl/pub/1721 PDF).
  Its table row 243 22 1 4 −5 132 110 confirms the BvLS graph; the μ=2
  dichotomy and 99's `?` status are recorded. (The `index.full.md` under
  sources/ is a duplicate Springer landing page of this paper — flagged, not a
  real independent source.)
- **van Lint 1975, perfect codes survey** — five-member list and explicit BvLS
  construction in `sources/van-lint-perfect-codes-survey-1975.full.md`.
- **Automorphism corpus** — Behbahani 2009 PhD thesis (full PDF), Behbahani–Lam
  2011, Cesarz–Woldar 2025 (published + arXiv), Crnković–Maksimović 2020
  (full PDF §7), Makhnev–Minakova via Makhnev's lecture. All on disk and cited
  by the consolidated automorphism claim.

## Request ledger — both resumption gaps CLOSED

`read_ledger requests` still renders both rows, but the closure mechanism has
fired: each note carries `answers:<id>`.

- `exact-list-prime-051a` — answered by claim `automorphism-orders-consolidated`
  (excluded orders + authors + computer-assistance status) at
  `notes/automorphism-orders-consolidated.md` line "answers: exact-list-prime-051a".
- `published-mechanism-ruling-5cf8` — answered by claim
  `srg33-mechanism-answers-request` (mechanism = eigenvalue-multiplicity
  integrality, spectral, cannot transfer to 99) at
  `notes/bagchi-mu2-dichotomy-resolution.md`.

These are resumption artifacts; the directed instruction is not to re-open them.

## The one authorized late acquisition — NOT needed

Task `serve-supersimple-22242-existence` (fetch the super-simple 2-(22,4,2)
existence verdict for v=22 from the Gronau–Mullin spectrum) was DROPPED by the
director for good reason: the construction beat the citation. An explicit
77-block certificate of a super-simple 2-(22,4,2) design was produced by CP-SAT
(OPTIMAL 167.35s) at `code/out/coclique_lift_clean_design.txt` and independently
verified. A source is not needed for a fact the run has already constructed and
checked. Do NOT re-open this.

## No new acquisition made

Per the closure directive, no further source acquisition is warranted. The
library is not exhausted — no finite library ever is — but it passes ROOT.md's
phase-1 test (minimal-counterexample structure stated, verification bound
stated, three restricted classes settled with hypotheses), and further gathering
is to happen only against a stated gap in `requests`. There are none open.

## Known mis-downloads / do-not-use (from `summaries/index.md`)

- `sources/bagchi-mu2-correct.full.md` — a WRONG paper (a Lie-algebra preprint,
  arXiv math/0512558). The correct Bagchi content is resolved in
  `notes/bagchi-mu2-dichotomy-resolution.md`. Never cite the file for graph theory.
- `sources/index.full.md` — duplicate Springer landing page of Brouwer–Neumaier
  1988. Real content is in `brouwer-neumaier-1988-combinatorica.full.md`.
- `sources/makhnev-1988-lambda1.full.md` — paywalled landing page; real content
  is in the Russian full-text file.
- `sources/cesarz-woldar-automorph-conway99.full.md` — arXiv landing page
  (duplicate of the published `automorph-putative-conway-99-graph.full.md`).

## Could not obtain (recorded, do not re-attempt without a new reason)

Cameron 1975 Partial Quadrangles (paywalled, content fully carried by
in-library secondary sources); Behbahani–Lam–Östergård 2012 (JCTA paywalled,
abstract captured); Behbahani–Lam 2011 / Makhnev–Minakova 2004 / Bagchi 2006
journal full texts (each filled by a primary or summary in-hand).

## Statement of the library's value to the run

Every load-bearing claim the run makes today traces to a source on this disk:
the five-member family and the two existing controls (9, 243); the open status
of (99,14,1,2); the automorphism bounds (|G| | 2·3³·7·11; primes {2,3}; no
Z6/S3/Z9/E9; small-or-trivial); the μ=2 dichotomy NOT biting at 99; Makhnev's
n₃=0 conditional. That is the canonical reference tier plus the named primary
sources, which is what "anything cited must be in the library" requires.
