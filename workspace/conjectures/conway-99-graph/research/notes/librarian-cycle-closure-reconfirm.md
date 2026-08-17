# Librarian — closure reconfirmation, this cycle

Per directive 18/19 the library is CLOSED; this cycle re-ran the closure audit
against the current on-disk state. Nothing new was downloaded. Verdict:
NOTHING FURTHER.

## 1. Request rows are answered on disk (stale renders only)

`derived/REQUESTS.md` and the requests ledger still render two rows, but both
carry their closing `answers:` field in the answering notes, so the next derive
closes them:

- `exact-list-prime-051a` — answered by claim `automorphism-orders-consolidated`
  (`answers: exact-list-prime-051a`) in
  `research/notes/automorphism-orders-consolidated.md`; also claimed by
  `wilbrink-order11-makhnev.md`. p ∈ {5,7} excluded (Behbahani–Lam 2011, orbit
  matrix), p = 11 excluded (Wilbrink 1984 / Makhnev–Minakova 2004), possible
  primes {2,3}, no Z6/S3/Z9/E9 (Crnković–Maksimović 2020), 2||G| ⇒ |G||6,
  7||G| ⇒ G≅Z7 (Cesarz–Woldar 2025).
- `published-mechanism-ruling-5cf8` — answered by claim
  `srg33-mechanism-answers-request` (`answers: published-mechanism-ruling-5cf8`)
  in `research/notes/bagchi-mu2-dichotomy-resolution.md`: srg(33,8,1,2) is
  ruled out by eigenvalue-multiplicity integrality (spectral; does not transfer
  to 99). Confirmed current.
- `super-simple-22242-existence` (the one reserved acquisition) — task dropped:
  construction beat citation (CP-SAT OPTIMAL 167.35s, 77-block certificate
  `code/out/coclique_lift_clean_design.txt`, claim `super-simple-22242-exists`,
  note `research/notes/coclique-lift-supersimple-exists.md`).

## 2. On-disk integrity re-verified

- 50 files in `research/sources/`, 49 real documents + `index.full.md`
  (documented duplicate Springer landing page of Brouwer–Neumaier 1988; the
  full text is `brouwer-neumaier-1988-combinatorica.full.md`, from the CWI
  repository PDF). No duplicate of actual content.
- 45 of 50 carry `<!-- source: https://... -->` URL headers verified by grep;
  the 5 without are the recorded paywalled/landing-page stubs
  (`bagchi-mu2-correct`, `behbahani-2009-phd-thesis`, `behbahani-lam-2011-*`,
  `crnkovic-maksimovic-composite-order-srg`, `makhnev-1988-lambda1`) — each is
  documented as a correction/identity record in LIBRARY-REPORT.md, with the
  real content held elsewhere on disk.
- 70+ summaries in `research/summaries/` with `index.md` catalogue.
- grep across threads finds no acquisition/gap/missing-source demand; no
  blocked task waits on a source.

## 3. Frontier top rows still non-blocking

Behbahani–Lam–Östergård 2012 (JCTA 119, paywalled) — the frontier's most-cited
row — remains covered by content in the in-library Brouwer–Ihringer–Kantor full
text; the 99 geometry is a *partial* STS, escaping that genuine-STS
classification. Cesarz–Woldar proof body remains absent (landing pages only),
flagged once already in `audit-fixed-set-lemma-automorphism-sources.md` as
"no evidence, not guaranteed" — non-blocking, independently sourced verdicts.

State: library genuinely closed for this phase; no source acquisition is
warranted until a live phase-4 argument names a NEW missing source.