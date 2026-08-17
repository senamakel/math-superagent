# Librarian audit — attempt 4 (directive-39 reopen)

Status of the reference library at this cycle. **No new acquisition was needed.**
The library is closed (directive 18/21) with 48 sources on disk under
`research/sources/`, and every item the workflow demanded is verified held.

## 1. Canonical reference tier — held

The encyclopedic and problem-collection entries that fix the statement, the
standard notation, the history, and the names of everyone who has worked on it:

- Wikipedia Conway 99-graph (`wikipedia-conway-99-graph.full.md`)
- Wikipedia Berlekamp–van Lint–Seidel graph (`wikipedia-berlekamp-vanlint-seidel-graph.full.md`)
- Brouwer's SRG tables: 1-50, 51-100, 101-150 (`brouwer-srg-table-*.full.md`)
- van Lint 1975 perfect codes survey (`van-lint-perfect-codes-survey-1975.full.md`)
  — confirms (243,22,1,2) = BvLS from the perfect ternary Golay code, and the
  five-member family.

## 2. The automorphism literature — held, full bodies where available

- Makhnev–Minakova 2004 (character theory) — via Cesarz–Woldar / Behbahani
- Cesarz–Woldar 2025 *On the automorphism group of a putative Conway 99-graph*
  (`cesarz-woldar-automorph-conway99-body.full.md` — FULL PROOF BODY)
- Crnković–Maksimović 2020 (`crnkovic-maksimovic-full-pdf.full.md`)
- Behbahani 2009 PhD thesis (`behbahani-2009-phd-thesis-pdf.full.md` — full text)
- Behbahani–Lam 2011 (`behbahani-lam-2011-srg-nontrivial-automorphisms.full.md`)
- Makhnev lecture on symmetric graphs / automorphisms
  (`makhnev-symmetric-graphs-automorphisms-lecture.full.md`)
- Lou–Murin 2014 ON THE SRG OF PARAMETERS (99,14,1,2)
  (`lou-murin-srg991412-2014.full.md` — orders 11/13/14 exclusion proofs)

## 3. The two rendered-open REQUESTS rows are answered on disk

Both rows in `derived/REQUESTS.md` still render as open, but each carries its
closing claim block with an `answers: <id>` line on disk. This is a derive lag,
**not a genuine gap**:

- `exact-list-prime-051a` — answered by `research/notes/automorphism-orders-consolidated.md`
  (claim `automorphism-orders-consolidated`, `answers: exact-list-prime-051a`).
  Consolidated table: |G| | 2·3³·7·11 (MM04, computer-free); prime divisors of
  |G| ⊆ {2,3} (Behbahani–Lam 2011, computer-assisted orbit matrices); no
  Z6/S3/Z9/E9 (CM 2020, computer-assisted); no order-14, 13, 11; 7|G| ⇒ Z₇ and
  2|G| ⇒ |G| | 6 (Cesarz–Woldar 2025, computer-free in published form; the arXiv
  Frob(21) elimination is computer-assisted — flagged).
- `published-mechanism-ruling-5cf8` — answered by
  `research/notes/bagchi-mu2-dichotomy-resolution.md` (claim
  `srg33-mechanism-answers-request`, `answers: published-mechanism-ruling-5cf8`).
  srg(33,8,1,2) is ruled out by **eigenvalue-multiplicity integrality** (spectral),
  which cannot transfer to 99 — so the nearest precedent is a dead end.

## 4. The two open tasks are computational gates, not acquisition gaps

- `gate-clique-complex-homology` (directive 39 FIRST) — **already answered on
  disk** by `research/notes/clique-complex-homology-gate-refuted.md` carrying
  `answers: gate-clique-complex-homology`: dim H1(Cl(rook(3)))=4 and
  dim H1(Cl(BvLS))=1540, both non-zero, so the Cioaba–Mim classification keyed to
  the Neumaier smallest-eigenvalue list gives no 99-vs-243 separation; refuted on
  arrival. The Cioaba–Mim source itself is held (`cioaba-mim-clique-homology-srg-html.full.md`).
- `incidence-budget-ledger-controls` (directive 39 SECOND) — no answering
  artifact yet; the ledger methodology must pass rook(3)/bvls controls through
  lib.n3patch. This is a computation, not an acquisition.

## 5. Conclusion

Nothing further to gather. The run has 48 sources covering the encyclopedic
tier, the automorphism programme, the failed methods and why, the adjacent
problems, the computational attacks (SAT, orbit matrix, clique homology), and
the control constructions. Any future source fetch must be against a NEW stated
gap in REQUESTS.md; none exists at this cycle.
