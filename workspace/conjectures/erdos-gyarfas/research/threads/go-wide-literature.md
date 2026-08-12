# Go-wide literature — surveys, failed methods, adjacent problems, and constructions

Opened by directive: the library's 23 sources are concentrated on one method
(structural minimal-counterexample / Carr-Markström). Cover what is missing.

## Why

The run has deep coverage of the Carr-Markström structural approach but almost
nothing on:
- **Surveys** — what surveys exist of the conjecture or cycle-length problems?
- **Failed methods** — which approaches have been tried and rejected, and why?
- **Adjacent problems** — cycle spectra, girth-vs-degree, Ramsey-type cycle
  results, unavoidable cycle-length sets.
- **Computational attacks** — the full landscape of SAT/SMS/CEGAR/enumeration
  attempts beyond the two that are already here (Royle-Markström and
  ArjunBalaji79).
- **Counterexample constructions** — Exoo's G78/G420 are here; what else has
  been built? What near-misses (like the Markström 24-graphs) exist for higher
  powers of two?

## Canonical reference tier — landed

These were downloaded on directive and are now on disk:

- `research/sources/wikipedia-erdos-gyarfas.full.md` — the Wikipedia article, with references and external links
- `research/summaries/markstrom-graph-mathworld.md` — already here; MathWorld on the Markström graph
- `research/sources/ucsd-erdos-problems-64.md` — the Erdős Problems page #64 (via Wayback Machine; live page is down)
- `research/sources/bibliotekanauki-30148697.full.md` — Salehi, Esfandiari, Shirdareh, Bibak: "On the Erdős–Gyárfás conjecture in claw-free graphs" (Theorems 1–9, cubic claw-free bound ≥114 vertices)

## Wikipedia-cited papers — partially landed

- `research/sources/sudakov-verstraete-2008.full.md` — Sudakov & Verstraëte 2008 (arXiv:0707.2117) — downloaded
- `research/sources/verstraete-2005.md` — Verstraëte 2005 (doi:10.1002/jgt.20072) — downloaded
- `research/sources/daniel-shauger-2001.full.md` — **Google Scholar search results, NOT the actual paper** — paper still missing
- `research/sources/shauger-1998.full.md` — **Google Scholar search results, NOT the actual paper** — paper still missing

## Wikipedia-cited papers — not yet attempted

- Nowbandegani & Esfandiari 2011 (14th Workshop, Szklarska Poręba — bipartite counterexample ≥30 vertices)

## Wikipedia external links — both unreachable

- Exoo catalog (`cs.indstate.edu/ge/CYCLES`) — 404, not in Wayback Machine
- West open-problems (`math.uiuc.edu/~west/openp/2powcyc.html`) — connection failed

## Markström full PDF — already in library

Deduped against `research/summaries/markstrom-extremal-graphs.md`; §4 content already digested.

## Status

- [x] Canonical four downloaded (Wikipedia, MathWorld, UCSD #64, bibliotekanauki 30148697)
- [x] Sudakov–Verstraëte 2008 downloaded
- [x] Verstraëte 2005 downloaded
- [ ] Daniel–Shauger 2001 — only Google Scholar results; actual paper needed
- [ ] Shauger 1998 — only Google Scholar results; actual paper needed
- [ ] Nowbandegani–Esfandiari 2011 — not yet attempted
- [ ] Exoo catalog — unreachable (404, no Wayback copy)
- [ ] West open-problems — unreachable (connection failed)
- [ ] Surveys identified and downloaded
- [ ] Failed methods documented
- [ ] Adjacent problems covered
- [ ] Computational attack landscape mapped
- [ ] Counterexample constructions catalogued