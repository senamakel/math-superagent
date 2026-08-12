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

- [x] FRONTIER.md top-tier downloads (worked; Litmaps/Modal/OEIS refs are tool/sequence pages, not sources)
- [x] Erdos-problems #64 / #751 source download (`research/sources/erdosproblems-64-source.md`; the UCSD PowerOfTwoCycles original statement was already on disk via Wayback, read)
- [x] Bondy–Vince located and downloaded (`research/sources/bondy-vince-cycles-lengths-differ-one-two.full.md` + summary) — Thm 1: every graph with ≤2 vertices of degree <3 (except K1,K2) has two cycles differing by 1 or 2; Thm 2: nonbipartite 3-connected has two differing by 1
- [ ] Erdős–Faudree–Rousseau–Schelp (1999) — located (Discrete Math 200:55-60, lower bound c·k·g/8 on # cycle lengths); Memphis PDF returned 403, no full text on disk; secondary sources hold the statement
- [x] q-power construction landscape — Bensmail 2017 downloaded (`research/sources/bensmail-q-power-cycles-cubic.full.md`): arbitrarily large planar cubic graphs with no q-power cycle for every q≥3; for q=2 only length-4-only or 8-only constructions exist
- [x] Pirzada–Shah–Baskoro 2022 downloaded (`research/sources/pirzada-shah-baskoro-2-power-unicyclic-cubic.full.md`): infinite family of cubic graphs with exactly one 2-power cycle
- [x] Ghaffari–Mostaghim 2018 Cayley downloaded (preview; `research/sources/ghaffari-mostaghim-cayley-erdos-gyarfas.full.md`): EG holds for Cayley on generalized quaternion/dihedral/semidihedral/p^3 groups
- [x] Hu–Shen P10-free downloaded (`research/sources/hu-shen-P10-free-erdos-gyarfas.full.md`): every P10-free graph with δ≥3 has a C4 or C8
- [x] Markström original computational notes — already on disk (`research/sources/markstrom-extremal-graphs.full.md`); confirmed while cross-checking
- [x] Royle original computational notes — already on disk (`research/sources/royle-2n-conjecture.md`): UWA archive of the 2^n conjecture page — n≤15 check with makeg (min deg 3, no edge between two degree->3 vertices, no C4, then check C8), the "at most one vertex of degree two" relaxation, and the three-copies-joined-to-a-central-vertex 1-connected construction; counts table n=9..15
- [ ] Gould's cycle survey — not located as an open PDF; the adjacent-theory gap is instead covered by Bondy–Vince + Gao–Huo–Liu–Ma unified + Liu–Ma cycle-lengths-min-degree (all on disk) + Marczyk 2008 survey (Disc. Math. 454) identified, not downloaded
- [x] Girth/degree extremal literature — EFRS 1999 statement captured; Sudakov–Verstraëte 2008 (on disk) proves Erdős's |C(G)|=Ω(d^⌊(g-1)/2⌋) conjecture
- [ ] Daniel–Shauger 2001 actual paper — only search results on disk, not the paper (conference proceedings, no free PDF found)
- [ ] Shauger 1998 actual paper — only search results on disk
- [x] Nowbandegani–Esfandiari claw-free — already on disk (`research/sources/nowbandegani-clawfree.full.md`)
- [ ] Verstraëte 2005 — only summary on disk (`research/summaries/verstraete-2005.md`); full JGT paper paywalled
- [ ] Exoo catalog retried (Wayback) — not retried this cycle
- [ ] West open-problems retried (Wayback) — not retried this cycle

## What this cycle added (librarian run)

Full primary texts now on disk for six new sources covering the adjacent
machinery (Bondy–Vince), the original statement context (Erdős problems #751),
the counterexample-construction landscape (Bensmail q-power, Pirzada 2-power
unicyclic), and two more settled restricted classes (Cayley graphs, P10-free).
All summarized with claim blocks; CLAIMS.md and THREADS.md re-derived.
Remaining thinnest spots for a later cycle: EFRS 1999 full text (403-blocked),
Daniel–Shauger 2001 and Shauger 1998 (conference proceedings, no free PDF),
Verstraëte 2005 full text (paywalled), and a dedicated EG survey (Shah–
Purohit–Gulzar 2017 "A survey and strengthening..." identified but not
downloaded).

## What this cycle added (librarian run 2)

- **Ghasemi–Varmazyar 2021** (Matematički Vesnik 73(1) 37–42, open-access PDF)
  now on disk: settles the conjecture for **connected Cayley graphs on groups of
  order 2p² and 4p** (p odd prime), all via explicit 4-/8-/16-cycles. Also the
  **primary Erdős–Gyárfás founding quote** ("we are convinced now that this is
  false... but we never found a counterexample even for r=3") quoted verbatim.
  `research/sources/ghasemi-varmazyar-erdos-gyarfas-cayley-2p2.full.md` +
  summary. This closes the Phase-1 "original statement in a primary source"
  priority.
- **Potočnik–Vidali 2022** (Discrete Math 345:112734, arXiv:2005.01635, open
  HTML) now on disk: complete **classification of cubic vertex-transitive graphs
  of girth 6** (except the Desargues graph: toroidal hexagonal skeletons /
  hyperbolic triangulation truncations / dihedral-scheme truncations). The
  structural census behind the cubic-bipartite and cubic-vertex-transitive
  restrictions of the conjecture, and behind Gebendorfer's girth-6 paper.
  `research/sources/potocnik-vidali-cubic-vertex-transitive-girth6-html.full.md`
  + summary.
- **EFRS 1999 full text confirmed on disk** (the thread had it as 403-blocked;
  reopened with Wayback: `research/sources/efrs-cycle-lengths-degree-girth.full.md`
  has the full theorems/proofs). Thread item ticked.
- **Royle 2^n primary note confirmed on disk** (`research/sources/royle-2n-conjecture.md`).
  Thread item ticked.

## What this cycle added (librarian run 3)

- **Narins–Pokrovskiy–Szabó 2017** (Combinatorica 37, 495–519; full text
  `research/sources/narins-pokrovskiy-szabo-degree3-critical-pdf.full.md`): degree
  3-critical graphs (the class containing a minimal EG counterexample) do NOT force all
  short cycles — infinite families with no C23 exist; every such graph with n≥6 has a
  C6; refutes the EFRS 1988 short-cycle conjecture. **Warning: no "degree-3-critical ⇒
  many cycle lengths" argument can prove EG; the power-of-two must come from a specific
  structural fact.** Nuances the EFRS 1988 "induced" reading (verbatim discussion in the
  paper).
- **Couch–Daniel–Wright 2021** (Australas. J. Combin. 79, 100–105, full text on disk):
  Caro's integer-power question settled for claw-free δ≥3, for graphs whose induced-claw
  centers are independent, and almost claw-free δ≥3 — strictly weaker than the
  power-of-two conjecture for claw-free graphs, which stays open. Also cites Shauger 2002
  "Claw-free cubic graphs of low genus...", Congr. Numer. 159 (a primary source still not
  in the library).
- **West's open-problems page** re-located to `dwest.web.illinois.edu/openp/2powcyc.html`
  and fetched: verbatim statement of the Shauger 1998 class (K1,m-free, δ≥m+1 or Δ≥2m−1)
  and Daniel–Shauger 2001 (planar claw-free) — this settles the *statement* halves of the
  two REQUESTS rows (full proceedings text still unobtainable).
- **Markström cubicavoid catalog** (`abel.math.umu.se/~klasm/Data/cubicavoid.html`,
  live): NO 3-connected cubic graph on n≤52 avoids C4,C8,C16 — the strongest verified
  exhaustion for that class. Claim `EG-markstrom-3conn-cubic-n52`.
- **Exoo live CYCLES catalog** (`isu.indstate.edu/ge/COMBIN/CYCLES/index.html`, live) and
  **full Exoo paper** (arXiv:1403.5636 PDF now on disk): f(2)=10, f(3)=24, f(4)∈[54,78],
  f(5)≤450 (2014) but **smallest known no-C4/C8/C16/C32 is 540** (newer catalog). G420 is a
  3-connected cubic planar 420-vertex graph with NO C4/C8/C16, showing Heckman–Krakovski's
  m≤4 suggestion is false. **Reconciled the 450-vs-540 discrepancy**: 450 is Exoo 2014's
  construction bound; 540 is the newer "smallest known" in the live catalog. CONTEXT.md's
  "f(5)≤450" is the 2014 construction; the honest current figure is "smallest known 540".
- **Sudakov–Verstraëte "Cycles in sparse graphs II"** (arXiv:1010.5309, full text on
  disk): independence-ratio regime, prime-length and sparse-sequence cycles forced; the
  sequence condition log σ_r ≤ σ_{r−1} explicitly excludes powers of two (their growth
  gap) — a boundary marker for the run's central obstruction.
- Shah–Purohit–Gulzar 2017 survey: MaRDI/zbMATH record captured (theorem on n−2 degree-3 +
  2 degree-2 vertices and distance n/2+1 → a cubic graph with no C_{2^n}); no open PDF.

### Still NOT on disk (genuine gaps)
- **Gebendorfer girth-12 paper** ("...Cubic Vertex-Transitive Graphs of Girth
  Twelve Without Sixteen-Cycles...", 2026): no open copy — ResearchGate 403,
  no arXiv. Only title/existence recorded. NOT an established result.
- **Gebendorfer girth-6 paper** ("Power-of-Two Cycles in Cubic Bipartite
  Vertex-Transitive Graphs of Girth Six"): title only on the author's Scholar
  profile; no SSRN/arXiv open text found this cycle. Same caveat.
- **Shauger 1998 / Daniel–Shauger 2001**: remain Google-Scholar search stubs,
  not the papers (conference proceedings, no free PDF). The two claw-free /
  K1,m-free settled classes still rest on citation, unverified primary text.
- **Shah–Purohit–Gulzar 2017 survey**: MaRDI/zbMATH only, no PDF located.