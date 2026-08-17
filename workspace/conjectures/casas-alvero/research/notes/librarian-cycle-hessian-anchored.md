# Librarian cycle 2026 — integrity repair, origin-paper OA status, fresh-sweep confirmation

## 1. Library-integrity repair: the Hilbert-covariants mislabel is RESOLVED

See `research/notes/abdesselam-chipalkatti-mislabel.md` (rewritten this cycle).
The correct paper (arXiv:**1203.4761**, Canad. J. Math. 66(1) 2014 3–30) was
held all along under the correct id; the two wrong-content files are now marked
DO-NOT-CITE; the earlier note's "correct id is 1010.2667" was itself wrong.
Hessian-iff-perfect-power is now anchored to the held full text (Prop 3.2,
line 822). The hessian-covariant approach remains refuted on its unproved
bridge, so this was a completeness/anchoring repair, not a change of direction.

## 2. Origin paper "Higher order polar germs": OpenAlex confirms bronze OA, but PDF routes all blocked

- OpenAlex record `W2003962780` (held: `research/sources/openalex_W2003962780.full.md`)
  confirms: **Eduardo Casas-Alvero, "Higher Order Polar Germs", J. Algebra
  240(1) (2001) 326–337, DOI 10.1006/jabr.2000.8727, is_open_access=true
  (oa_status=**bronze**), with a ScienceDirect PDF URL and an OpenAlex content
  URL.**
- **Both PDF routes failed from this environment**: OpenAlex content
  (`https://content.openalex.org/works/W2003962780.pdf`) → HTTP 401
  Unauthorized; ScienceDirect
  (`https://www.sciencedirect.com/science/article/pii/S0021869300987271/pdf`)
  → HTTP 403 Forbidden. No arXiv version exists (the paper is not on arXiv).
- **Standing**: the full text of the origin paper remains un-held, but the
  earlier "unobtainable" conclusion is now sharpened to "obtainable-in-
  principle (bronze OA), blocked at the network layer from this host". A later
  run with working publisher/OpenAlex access should retry. The conjecture's
  statement/motivation/status remain fully covered by the held secondary tier
  (the origin reference is quoted by every held paper's history section), so
  nothing load-bearing is missing.
- The OpenAlex grobid-XML URL (`https://content.openalex.org/works/W2003962780.grobid-xml`)
  is the same 401-blocked content server; noted for a later run.

## 3. Fresh arXiv sweep (2026-08-17) confirms coverage — nothing new to hold

- Re-ran the arXiv API query (`all:"Casas-Alvero"`, 40 results, sorted by
  date desc): `research/sources/arxiv_search_casasalvero_fresh.full.md`.
- Every hit is already held or accounted for: Ghosh 2501.09272 (v2, held),
  Schaub–Spivakovsky 2411.13967 + 2307.05997 + 2312.08742 (held), Massri
  1806.09561 (held), Castryck 1208.5404 (held), Laterveer–Ounaïes 1204.0450
  (held), Graf-von-Bothmer math/0605090 (held), withdrawn claims (Battiston
  1511.04932, Dobrowolski 1705.01704, Fernández-de-las-Heras 1306.5656, held),
  Krishma C*-algebraic 2206.09197 (recorded as off-path), and the polar/
  singularity items (2410.11732, 1602.01143, 1907.03249, 2411.10853,
  1704.01428, 2410.21250) which are the out-of-scope origin-motivation
  literature.
- **No new primary treatment of CA from 2023–2026 is absent.** The library
  stands complete for the run's agenda.

## 4. Citation graph of Castryck 2012 (arXiv:1208.5404)

Cited by only Dobrowolski 2017 (already held, withdrawn). No new lead.

## 5. OpenAlex metadata files in the library

Four `openalex_W*.full.md` metadata records exist in `research/sources/`
(queries from an earlier cycle): W2003962780 (origin paper, above),
W1579326781 (Yakubovich 2013, arXiv:1308.5320 — already held in full),
W1558046128 (Qing Liu book review, off-path), W2062454016 (Barwise–Eklof
"Lefschetz's principle", J. Algebra 1969 — off-path). None is load-bearing
beyond the origin-paper OA status; recorded so they are not re-fetched.

## Status of the problem through 2026-08

Unchanged: CA is open; the only complete-proof candidate is Ghosh 2501.09272
(v2 Mar 2026), unverified preprint; every refereed 2024-25 source treats CA as
open; smallest open degree 20. No new degree, no new counterexample, no
retraction.