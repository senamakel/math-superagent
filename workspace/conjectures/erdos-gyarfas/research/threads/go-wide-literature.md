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

- `research/sources/wikipedia-erdos-gyarfas.full.md` — the Wikipedia article, with
  references and external links
- `research/summaries/markstrom-graph-mathworld.md` — already here; MathWorld on
  the Markström graph
- `research/sources/ucsd-erdos-problems-64.md` — the Erdős Problems page #64 (via
  Wayback Machine; the live page is down)
- `research/sources/bibliotekanauki-30148697.full.md` — Salehi, Esfandiari,
  Shirdareh, Bibak: "On the Erdős–Gyárfás conjecture in claw-free graphs"
  (Theorems 1–9, cubic claw-free bound ≥114 vertices)

## Cited but not on disk — must download or mark unverified

From Wikipedia's references (not in this library):

| Source | What it establishes | 
|--------|---------------------|
| Daniel & Shauger 2001 | EG holds for planar claw-free graphs |
| Shauger 1998 | EG holds for K1,m-free graphs with degree constraints |
| Sudakov & Verstraëte 2008 | EG holds for graphs with avg degree in iterated log of n (arXiv:0707.2117) |
| Verstraëte 2005 | set S of lengths, |S|=O(n^0.99), every graph avg deg ≥10 has a cycle with length in S |
| Salehi Nowbandegani & Esfandiari 2011 | bipartite counterexample ≥30 vertices (14th Workshop, Szklarska Poręba) |

From Wikipedia's external links (not in this library):

| Link | What it is |
|------|-------------|
| Exoo, "Graphs Without Cycles of Specified Lengths" | Catalog of graphs avoiding specified cycle lengths |
| West, "Erdős Gyárfás Conjecture on 2-power Cycle Lengths" | Open Problems page |

From Markström's own PDF link (Wikipedia cites it, not in library):
| Link | What it is |
|------|-------------|
| `abel.math.umu.se/~klasm/Uppsatser/cycex.pdf` | Markström 2004 full paper |

## Go-wide targets

These are the categories the directive says to cover:

### Surveys
- Any survey paper or section that summarizes the conjecture's status, beyond
  the introduction paragraphs in individual papers.
- The Wikipedia article (now on disk) has a references section; chase its
  review-style references.

### Failed methods
- Approaches that were tried and documented as failing: why did they fail, and
  what obstruction stopped them?
- The Hegde et al. paper states that P_k-free backtracking cannot reach the full
  conjecture — is there more in the literature?

### Adjacent problems
- Cycle spectra: what is known about which cycle lengths must appear in graphs
  of given minimum degree?
- Girth vs. degree: the Moore bound and its consequences for cycle existence.
- Ramsey-type cycle results: what does Ramsey theory say about unavoidable cycle
  lengths?
- Unavoidable cycle-length sets (Verstraëte, Sudakov—Verstraëte): the wider
  theory.

### Computational attacks
- All computational attempts beyond Royle–Markström and ArjunBalaji79.
- What SAT/SMS/CEGAR methods have been applied? Did any fail at specific bounds?
- The SMS landscape: BreakID, Glasgow Subgraph Solver, other tools.

### Counterexample constructions
- Exoo's constructions (G78, G420) are here. What else?
- The Markström 24-graphs — any higher-order analogs?
- Any construction that systematically avoids cycles of lengths 4, 8, 16, …?

## Next actions

1. Download the five Wikipedia-cited papers (Daniel–Shauger 2001, Shauger 1998,
   Sudakov–Verstraëte 2008, Verstraëte 2005, Nowbandegani–Esfandiari 2011) and
   the two external-link pages (Exoo catalog, West open-problems).
2. Download the Markström full PDF from `abel.math.umu.se`.
3. Have the scholar produce summaries.
4. For each of the go-wide categories, identify the 2–3 most-cited papers and
   download them.
5. Update ROOT.md and CLAIMS.md with what is found.

## Status

- [x] Canonical four downloaded (Wikipedia, MathWorld, UCSD #64, bibliotekanauki 30148697)
- [ ] Wikipedia references (5 papers) downloaded
- [ ] Wikipedia external links (2 pages) downloaded
- [ ] Markström full PDF downloaded
- [ ] Surveys identified and downloaded
- [ ] Failed methods documented
- [ ] Adjacent problems covered
- [ ] Computational attack landscape mapped
- [ ] Counterexample constructions catalogued