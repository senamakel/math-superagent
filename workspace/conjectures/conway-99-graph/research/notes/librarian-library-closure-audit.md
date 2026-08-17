# Librarian — library closure audit, this cycle

Per directive 18/19 the library is CLOSED: no further source acquisition except
against a NEW gap a live phase-4 argument names. This cycle audited completeness
rather than acquiring. Findings:

## Both rendered open requests are answered on disk (stale render)

`derived/REQUESTS.md` still shows two rows, but each carries its `answers:`
marker in the answering note, so the next derive closes them:

- `exact-list-prime-051a` (which prime orders excluded as automorphisms, by
  whom, computer-assisted?) — answered by
  `research/notes/automorphism-orders-consolidated.md`, claim block
  `automorphism-orders-consolidated` with `answers: exact-list-prime-051a`.
  Primary anchors on disk: `cesarz-woldar-automorph-conway99.full.md`,
  `crnkovic-maksimovic-full-pdf.full.md`, `behbahani-2009-phd-thesis-pdf.full.md`.
- `published-mechanism-ruling-5cf8` (mechanism ruling out srg(33,8,1,2)?) —
  answered by `research/notes/bagchi-mu2-dichotomy-resolution.md`, claim block
  `srg33-mechanism-answers-request` with `answers: published-mechanism-ruling-5cf8`.
  Mechanism = eigenvalue-multiplicity integrality (spectral; cannot transfer to
  v=99, so the 33 precedent is a dead end).

## Reserved acquisition dropped by construction

`serve-supersimple-22242-existence` (super-simple 2-(22,4,2) existence verdict)
was dropped: construction beat citation — CP-SAT OPTIMAL in 167.35s,
77-block certificate `code/out/coclique_lift_clean_design.txt`, independently
verified, claim `super-simple-22242-exists`. No source needed.

## Frontier anchor checked: no missing primary source

The most-cited row of the frontier (cited by 9 of the library's own sources) is
Behbahani–Lam–Östergård 2012, "On triple systems and strongly regular graphs"
(JCTA 119, DOI 10.1016/j.jcta.2012.03.013). Its full text is paywalled
(ScienceDirect). Audit result:

- Not currently relied on as evidence: nothing in CONTEXT.md/ROOT.md/claims
  assigns it a result; the one note that names it
  (`research/notes/triangle-geometry-4vertex-enumeration.md`) anchors its
  actual two-family content to the in-library full text
  Brouwer–Ihringer–Kantor "Strongly regular graphs satisfying the 4-vertex
  condition" §3.4, which pins the classification exactly (Higman: STS block
  graph with 4-vertex condition is PG(m,2) or v ∈ {9,13,25}; BIK eliminates
  13, 25, leaving AG(2,3); all rank-3; none has the (99,14,1,2) spectrum).
- The 99 triangle geometry is a *partial* STS, which escapes that genuine-STS
  classification regardless.
- Hence no live phase-4 argument is blocked on acquiring BLÖ 2012. Its exact
  content is already covered by an on-disk primary source. Recorded as a
  known-paywalled secondary anchor, not a gap.

## Earlier gaps verified closed

- Makhnev 1988 "Strongly regular graphs with λ=1" full text: closed — primary
  Russian full text at `research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`
  (mathnet.ru paperid=4220), read; Thm 1/2 and the n3≥1 conditional sourced.

## State

48 full-text sources in `research/sources/`, each carrying its URL in the
`<!-- source: ... -->` header; 49th (brouwer-srg-table binary) also present.
Summaries in `research/summaries/`. Nothing in the notes cites a source absent
from disk. Library is genuinely closed for this phase.
