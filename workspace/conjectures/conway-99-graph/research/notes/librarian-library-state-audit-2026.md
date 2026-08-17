# Librarian library-state audit (this pass) — integrity verified, one report fix

Per the run's standing rule the library is CLOSED: no acquisition except against
a NEW gap a live phase-4 argument names. This pass therefore audited integrity
and consistency rather than downloading. Findings, all checked this session:

## 1. Source inventory (research/sources/, 51 files)

All full texts carry their URL on line 1 as `<!-- source: <URL> | converted from ... -->`
(verified by grep across the directory). The authoritative primary/reference
tier for the Conway 99-graph problem, all local:

| File | URL | What it fixes |
|---|---|---|
| `wikipedia-conway-99-graph.full.md` | https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem | encyclopedic statement; open status; locally 7K2 |
| `wikipedia-berlekamp-vanlint-seidel-graph.full.md` | https://en.wikipedia.org/wiki/Berlekamp%E2%80%93van_Lint%E2%80%93Seidel_graph | the (243,22,1,2) control |
| `brouwer-srg-table-{1-50,51-100,101-150}.full.md` | https://aeb.win.tue.nl/graphs/srg/srgtab*.html | canonical SRG tables; 99 row `?` open |
| `brouwer-neumaier-1988-combinatorica.full.md` | https://ir.cwi.nl/pub/1721/1721D.pdf | primary μ=2 / girth-5 PLS paper; 99 open |
| `makhnev-1988-lambda1-russian-fulltext.full.md` | https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=rus&paperid=4220&what=fullt | primary Makhnev 1988, full Russian; n3=0 conditional |
| `makhnev-symmetric-graphs-automorphisms-lecture.full.md` | https://www.math.uni-bielefeld.de/~baumeist/sommerschule/makhnev.pdf | Wilbrink order-11; Makhnev–Minakova fixed-point dichotomy |
| `behbahani-2009-phd-thesis-pdf.full.md` | https://spectrum.library.concordia.ca/id/eprint/976720/1/NR63369.pdf | orbit-matrix method; primes {2,3}; order-3 fixed-point-free |
| `crnkovic-maksimovic-full-pdf.full.md` | https://cdm.ucalgary.ca/article/download/62323/54015 | no Z6/S3/Z9/E9; |G|=2^a 3^b |
| `automorph-putative-conway-99-graph.full.md` | https://alco.centre-mersenne.org/articles/10.5802/alco.418/ | Cesarz–Woldar published; computer-free |
| `cesarz-woldar-automorph-conway99.full.md` | https://arxiv.org/pdf/2308.02978 | Cesarz–Woldar arXiv version |
| `van-lint-perfect-codes-survey-1975.full.md` | https://projecteuclid.org/journals/rocky-mountain-journal-of-mathematics/volume-5/issue-2/A-survey-of-perfect-codes/10.1216/rmj-1975-5-2-199.pdf | five-member list; BvLS construction |
| `reimbayev-hexagon-bound-body.full.md` | https://arxiv.org/html/2409.10620v1 | hexagon bound; n3 pivot |
| `reimbayev-subgraphs-order-six-body.full.md` | https://arxiv.org/html/2508.03377v2 | order-6 subgraph counts |
| `reimbayev-hamiltonian-order7-srg-l1-mu2.full.md` | https://arxiv.org/html/2511.06572v1 | order-7 Hamiltonian subgraphs (added; verified this pass) |
| `shpectorov-zhao-srg85-full.full.md` | https://arxiv.org/pdf/2504.02449 | srg(85,14,3,2) nonexistence; k=14, μ=2 precedent |
| `wilbrink-brouwer-57141-does-not-exist.full.md` | https://ir.cwi.nl/pub/6822/6822D.pdf | srg(57,14,1,4) nonexistence |
| plus assmus 2-rank STS, brouwer–ihringer–kantor 4-vertex, kaski–khatirinejad–östergård, greaves–koolen–park Delsarte, pech highly-regular, reichard 7-vertex, forced-structure-reduction (2026 CAISc preprint), lou–murin, bondarenko–radchenko, mohammadian diamond-free, östergård–soicher, keramatipour, zehavi–oliveira, milosevic star-complement, koolen–cae–yang survey | | |

## 2. Every claim-block anchor resolves to a file on disk

grep across research/notes for `sources/<name>` found no absent target:
- `behbahani-2009-phd-thesis-pdf`, `crnkovic-maksimovic-full-pdf`,
  `automorph-putative-conway-99-graph`, `cesarz-woldar-automorph-conway99` —
  all present.
- `assmus-2ranks-sts-fulltext.full.md` — present (an older note's alternate
  name `assmus-2ranks-steiner-triple-systems` resolves to the same file; not a gap).
- The two newest summaries (`reimbayev-hamiltonian-order7-srg-l1-mu2`,
  `vanlint-brouwer-srg-partial-geometries-1984`) point at files both present on
  disk.

## 3. Requests state confirmed

- `published-mechanism-ruling-5cf8` — answered (claim `srg33-mechanism-answers-request`,
  note bagchi-mu2-dichotomy-resolution.md): srg(33,8,1,2) dies on integrality; spectral ⇒ dead end for 99.
- `exact-list-prime-051a` — answered (claim `automorphism-orders-consolidated`,
  note automorphism-orders-consolidated.md + wilbrink-order11-makhnev.md):
  excluded orders, by whom, computer-assisted status — full table in the note.
- The rendered derived/REQUESTS.md still lists both; the closing `answers:` rows
  are in the answering notes, so the next derive closes them. Both are resumption
  artifacts, not live gaps. Do NOT re-open.

## 4. Reserved acquisition remains settled constructively

`serve-supersimple-22242-existence` is dropped: super-simple 2-(22,4,2) EXISTS
(CP-SAT OPTIMAL 167.35s, 77-block certificate, independently verified; claim
`super-simple-22242-exists`, checked). The Gronau–Mullin spectrum row is
answered by construction; no citation needed.

## 5. Report fix this pass

`research/LIBRARY-REPORT.md` previously omitted the most misleadingly-named
file in the library: `research/sources/index.full.md` (Springer paywalled
landing page of Brouwer–Neumaier 1988, DOI 10.1007/BF02122552 — NOT an index;
the real full text is `brouwer-neumaier-1988-combinatorica.full.md`). Added a
flagged row to the corrected-sources table, plus rows flagging the three
Pech landing-page/ar5iv duplicates (real text: `pech-highly-regular-fulltext.full.md`)
and confirming the two known wrong downloads (`bagchi-mu2-correct`,
`crnkovic-maksimovic-composite-order-srg`) carry in-file correction headers.
The summaries index (`research/summaries/index.md`) already flags all of these
under "Not useful / wrong downloads".

## State

The local reference set for the Conway 99-graph problem is complete and
internally consistent: primary full texts in research/sources/ (51 files, URL
in every header), one bounded summary per source in research/summaries/ (with
index), established claims in research/notes/ with `answers:` closing both
resumption requests. Library remains CLOSED to new acquisition.