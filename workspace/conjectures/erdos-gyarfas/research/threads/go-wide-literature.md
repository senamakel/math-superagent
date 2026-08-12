# Go-wide literature — surveys, failed methods, adjacent problems, and constructions

```thread
question: What do the surveys, failed methods, adjacent cycle-length theory, computational-attack landscape beyond Royle–Markström/ArjunBalaji79, and counterexample constructions say about the Erdős–Gyárfás conjecture?
status: open; directive-ordered internet research pass — FRONTIER.md has 326 unvisited URLs, the library is 28 sources concentrated on one structural thread, and the CEGAR non-convergence at n=10 shows the SAT line needs structural facts it does not yet have
rests-on: FRONTIER.md (326 ranked candidates from within-library citations), EG-go-wide-literature-gaps (missing surveys, missing original computational notes, missing adjacent theory)
blocked-by: nothing — the directive explicitly orders this pass now
next: download from the top of FRONTIER.md (cited-by ≥2, anything not already on disk as a full source); fetch Erdos-problems #64 source; then widen to Bondy–Vince, Erdős–Faudree–Rousseau–Schelp, Sudakov–Verstraëte forward citations, Markström/Royle original notes, Gould's cycle survey, girth/degree extremal literature; fill Daniel–Shauger 2001, Shauger 1998, Nowbandegani–Esfandiari 2011 gaps; retry Exoo/West via Wayback
```

## Why

The run has deep coverage of the Carr-Markström structural approach and the
SAT/CEGAR computational thread but almost nothing on:
- **Surveys** — what surveys exist of the conjecture or cycle-length problems?
- **Failed methods** — which approaches have been tried and rejected, and why?
- **Adjacent problems** — cycle spectra, girth-vs-degree, Ramsey-type cycle
  results, unavoidable cycle-length sets.
- **Computational attacks** — the full landscape of SAT/SMS/CEGAR/enumeration
  attempts beyond the two that are already here (Royle-Markström and
  ArjunBalaji79).
- **Counterexample constructions** — Exoo's G78/G420 are here; what else has
  been built?

## Priorities from directive (2025-07-14)

These are ordered. The directive says to work the top of FRONTIER.md first,
then widen deliberately.

### 1. FRONTIER.md top tier — download now

From the frontier table (ranked by citation count within the library):

- `download_document` on every URL in the top two tiers (cited-by ≥2) that
  is not already on disk as a full source
- The Erdos-problems entry #64: the summary exists
  (`research/summaries/ucsd-erdos-problems-64.md`) but the source download
  does not — fetch it now
- Litmaps (cited-by 7) is a tool link, not a source — skip
- OEIS cross-references (cited-by 3, 17 entries) are sequence pages — useful
  but low priority vs surveys; download only when a specific sequence is
  needed for a claim
- Avery Carr author search (cited-by 2) — already in library; only download if
  a new Carr preprint has appeared since the last fetch
- Modal (cited-by 2) — tool link, skip

### 2. Widen — surveys and adjacent theory

The directive names these specifically:

- **Cycle spectra of graphs with given minimum degree** — the general theory
  the conjecture sits inside. What is known about the set of cycle lengths in
  a graph with δ≥k?
- **Bondy–Vince** on cycle lengths — a classical result about the number of
  distinct cycle lengths in a graph with minimum degree constraints
- **Erdős–Faudree–Rousseau–Schelp** on cycle lengths — the foundational paper
  on how many distinct cycle lengths a graph of given order/degree must have
- **Sudakov–Verstraëte 2008** — already downloaded; now get what cites it
  (Google Scholar forward citations, Semantic Scholar "cited by")
- **Markström's original computational notes** — the actual writeup of the
  n<29 cubic search, not just the extremal-graphs paper digest
- **Royle's original computational notes** — the n<16 general search; the
  run has a summary (`research/summaries/royle-2n-conjecture.md`) but no
  primary source
- **Gould's cycle survey** — "Cycles and Paths in Graphs" or equivalent; the
  standard survey reference on cycle-length problems
- **Girth/degree extremal literature** — what is the smallest graph with δ≥3
  and girth g? What is known about unavoidable cycle lengths at given girth?

### 3. Wikipedia-cited papers — fill the gaps

- **Daniel–Shauger 2001**: on disk as Google Scholar search results only
  (NOT the actual paper)
- **Shauger 1998**: same — search results, not the paper
- **Nowbandegani–Esfandiari 2011**: not yet attempted
- **Verstraëte 2005**: downloaded (`research/sources/verstraete-2005.md`) —
  check it is the full paper, not a stub

### 4. External links — retry or replace

- Exoo catalog (`cs.indstate.edu/ge/CYCLES`) — 404; try Wayback Machine
  explicitly, and try Exoo's personal page / arXiv page as fallback
- West open-problems (`math.uiuc.edu/~west/openp/2powcyc.html`) — connection
  failed; try again, try Wayback, try West's current page at a different host

## Method

Every download lands in `research/sources/` with the URL in the file header.
After each batch, the scholar writes summaries to `research/summaries/` and
the librarian updates `research/FRONTIER.md` (which rewrites itself on each
download). A downloaded source that is only search results must be marked as
such and re-attempted.

## Status

- [ ] FRONTIER.md top-tier downloads
- [ ] Erdos-problems #64 source download
- [ ] Bondy–Vince located and downloaded
- [ ] Erdős–Faudree–Rousseau–Schelp located and downloaded
- [ ] Sudakov–Verstraëte forward citations mapped
- [ ] Markström original computational notes downloaded
- [ ] Royle original computational notes downloaded
- [ ] Gould's cycle survey located and downloaded
- [ ] Girth/degree extremal literature surveyed
- [ ] Daniel–Shauger 2001 actual paper downloaded
- [ ] Shauger 1998 actual paper downloaded
- [ ] Nowbandegani–Esfandiari 2011 downloaded
- [ ] Verstraëte 2005 verified as full paper
- [ ] Exoo catalog retried (Wayback)
- [ ] West open-problems retried (Wayback)