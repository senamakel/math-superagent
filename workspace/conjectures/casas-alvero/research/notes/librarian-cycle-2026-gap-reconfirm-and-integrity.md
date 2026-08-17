# Librarian cycle — gap re-confirmation and library-integrity audit (no new fetches possible)

Cycle focus: verify the library is still current and complete against the
2026-08 record, re-attempt the two documented fetch-blocked items through
every untried route, and audit URL provenance across the full-text corpus.
Conclusion: **nothing fetchable is missing; the two blocked items remain
blocked at the network layer after fresh attempts; every held source carries
its source URL.**

## 1. The 2026 arXiv sweep — all results held or documented background

Fresh `exa_search` restricted to 2026-06-01 onward (category research paper)
returns only already-held works (Ghosh 2501.09272, Schaub–Spivakovsky
s40687-024-00444-z / 2411.13967, Ghosh 2402.18717, Castryck 1208.5404,
Graf-von-Bothmer math/0605090). The held fresh arXiv query dump
(`research/sources/arxiv_search_casasalvero_fresh.full.md`, dated
2026-08-17, 23 results) likewise lists only held items; the remaining hits
are polars/quasi-ordinary-singularities background explicitly out of scope
per GOAL.md (2411.10853, 2410.21250, 2410.11732, 1907.03249, 1704.01428,
1602.01143) or C*-algebraic generalisation (2206.09197, degree 2 only —
GOAL.md's out-of-scope clause; recorded in the sweep file, not fetched).
No new settled degree, no new disproof, no new refereed partial result.
`citation_graph` on 2501.09272 adds 0 connected works (held 0-citation
record, `research/summaries/citations_w4406548163.md`).

Status re-confirmed: CA open; smallest open degree 20 (Castryck 2012,
Schaub–Spivakovsky 2024/25); Ghosh 2501.09272 v2 (21 Mar 2026, "Major
revisions") remains an unverified preprint — no journal publication, no
independent validation, no retraction through the 2026-08 record.

## 2. The two fetch-blocked items — re-attempted through every route, still blocked

**de Frutos Marín 2015, "Un problema sobre números combinatorios"** (JTN2015,
Valladolid). The exact PDF URL
`http://singacom.uva.es/JTN2015/contribuciones/ordinarias/frutos.pdf` is
correct (confirmed by the JTN2015 program page `trabajos.html` via search),
but `download_document` fails at the network layer on both http and https —
same failure class as every prior attempt on `uvadoc.uva.es` /
`hdl.handle.net`. `https://web.archive.org/web/2020/...` returns **503
Service Unavailable** (wayback rate-limit, not proof of absence). The uva.es
host block is network-wide from this environment. Held content remains the
quoted abstract (claim `badprimes-lists-corroborated-by-defrutosmarin2015`),
whose lists the run has independently verified exactly.

**Chávez Martínez 2018, "La Conjetura de Casas-Alvero para un número fijo de
raíces"** (UCrea, Univ. Cantabria, handle 10902/15246). Re-attempted
`hdl.handle.net/10902/15246` and `repositorio.unican.es/xmlui/handle/10902/15246`
— both fail at the network layer. `web.archive.org/web/2023/...` also 503
(rate-limit). Abstract held (`research/summaries/chavez-martinez2018.md` via
grep; see notes/chavez-martinez2018-degree20-lead.md): degree-20 restricted
result, 4/5/6 distinct roots, 302/627 partitions — the strongest
degree-20 restricted class known; still abstract-only, not citable as a
full text.

Both remain **fetch-limited, not unknown**: claim-level coverage is in the
library, and a future run with working outbound access to uva.es / unican.es
(or to an unthrottled wayback) should grab the two PDFs.

## 3. Díaz-Toca–Gonzalez-Vega — A3L-2005 variant confirmed already documented

The A3L 2005 publication ("On a Conjecture About Univariate Polynomials and
Their Roots", Passau, pp. 83–90) surfaced by search is the alternative venue
of the same d≤7 Maple verification; it is already recorded in the held
`research/sources/diaz-toca-gonzalez-vega-2006.full.md` (NOT OBTAINED block,
lines 1-5) and in `research/notes/casas-alvero-status.md:453`. No open PDF
exists at researchr, the Gröbner-Bases Bibliography, or MaRDI (all
metadata-only; checked via read_sources). The verification-bound claim it
would support is doubly corroborated by held primaries (Draisma–de Jong;
Castryck et al. 2012). Not a gap.

## 4. URL-provenance audit — every held full text carries its source URL

`grep "^<!-- source:"` across `research/sources/` returns 60 files, every
one with the URL recorded on line 1 (arXiv PDF/HTML variants, HAL,
doi.org, EMS, AMS, CWI, Cambridge, Rose-Hulman via wayback, uva.es, etc.).
The three non-`source:` files are the `openalex_*` API records and
`tmp-castryck-homepage` (which carry their URLs in the body). No held file
lacks provenance.

## Verdict

The library meets the phase-1 exit test (status / minimal-counterexample
structure / verification bound / restricted classes all sourced) and the
2026-08 sweep changes nothing. Frontier top rows are all held or
documented-blocked. No open request can be settled by a download from this
environment. **Next cycles are mathematics, not gathering** — the open tasks
(uresultant-n6-multmap-closedform, uresultant-n5-multmap,
redirect-refuter-to-rootdiff, defer-inventor-pending-output) are the work.