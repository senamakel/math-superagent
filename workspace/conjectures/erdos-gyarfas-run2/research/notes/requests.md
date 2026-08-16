# Research requests — gaps this run is missing and what would settle each

Each row is a gap stated precisely enough to be a research request. The
`falsifies` column says what a source would have to settle, which is a better
query than a topic. Work the open rows before new guessing.

## Open

- **Balaji SMS full-PDF / proof certificate** (VERIFIED unobtainable this cycle,
  do not re-fetch the dead URL). The run's verification anchor (≤31 vertices,
  any counterexample ≥ 32) is held only as landing-page + GitHub README
  (`summaries/balaji-sms-github.md`, `sms-verification-31-vertices.md`). The
  Zenodo file URL `records/20782738/files/erdosgyarfassms.pdf?download=1`
  returns HTTP 404 (renamed `EGC_CVTG6...`/`egc paper v6 corrected.pdf` are the
  *Gebendorfer* files, not Balaji's). No arXiv number exists. The workspace
  effect is unchanged: the 32-vertex bound is asserted-by-source with no formal
  certificate on disk, and the run's own oracle should reproduce a subset
  (n≤16 baseline or n≤19 CEGAR agreement) before trusting numbers past it. Do
  not re-fetch the dead URL.

- **Gebendorfer 2026 full proof text** (NEW, unobtainable). `A Proof of the
  Erdős–Gyárfás Conjecture`, Zenodo doi:10.5281/zenodo.18232846 (2026-01-13).
  Direct record/file fetch returns HTTP 410 Gone; only the abstract is held at
  `summaries/gebendorfer-proof-of-erdos-gyarfas.abstract.md`. If the full text
  ever becomes downloadable, verify whether its girth≥5 ⇒ 8-cycle step evades
  the held refutations (Markström 24-vertex cubic no-C4-C8; Exoo 78/540 and
  G420 no-{4,8,16}). Do not re-fetch until it is confirmed reachable; the
  abstract's central dichotomy contradicts all three held constructions.

- **Shauger's original K1,m-free and planar-claw-free results** (unchanged).
  Conference proceedings (Congr. Numer.) have no open full text found; only the
  *statements* are sourced (West's page, Wikipedia, Heckman–Krakovski, and now
  the Alfaiz list on erdosproblems.com #64). Exact hypotheses now doubly
  confirmed: "K1,m-free graphs of min degree ≥ m+1 or max degree ≥ 2m−1 contain
  a 2-power cycle" and "planar claw-free graphs contain a 2-power cycle". Still
  no full proof text obtainable. (This cycle: re-searched; both Shauger 1998 and
  Daniel–Shauger 2001 remain full-text-unobtainable, statement-only. Do not
  re-fetch.)

- **Original Erdős 1997 problem paper "Some old and new problems in various
  branches of combinatorics" (Discrete Math 165/166:227–231)** — confirmed
  paywalled at ScienceDirect (doi:10.1016/S0012-365X(96)00173-2). No open PDF
  found on Rényi archive or elsewhere; the statement of the E–G conjecture as
  Erdős first published it is preserved in the held encyclopedic pages
  (erdosproblems.com/64, UCSD #69, Wikipedia) and the NEHB14 full text quotes the
  original negative belief verbatim. Do not re-fetch.

- **Independence of the Balaji general SAT bound** (partly closed). As before.

- **Exoo, "Graphs Without Cycles of Specified Lengths"** (partly closed). As
  before. The concrete graph6 data subpages (N4610, N4832, G24a, G24b, N46,
  N468) were downloaded this cycle and are **image-only** (automorphism group,
  similar-vertices-by-colour); they add nothing beyond the already-held index
  page `sources/exoo-cubic-no-4-8-16.full.md`, which fixes the 78-vertex
  no-{4,8,16} and 540-vertex no-{4,8,16,32} constructions and the 32-vertex
  no-{4,8,32} graph.

- **The 2/3 degree-fraction claim — VERIFIED by deduction** (CLOSED this cycle).
  The jul059 forum proof
  (research/summaries/erdosproblems-64-discussion.md, claim ce-2-3-degree-fraction)
  improving Carr's 4/7 to >2/3 is now verified step by step against the held
  Carr full proof (now at `sources/carr-predominantly-cubic-fulltext.html.full.md`,
  previously abstract-only). Every step rests on Carr's held lemmas: V≥4
  independent ⟹ e ≥ 4|V≥4|; Cor 0.1(1) (every vertex adjacent to a deg-3 vertex)
  applied to V3 vertices gives each V3 vertex ≤ 2 V≥4 neighbours (the new step vs
  Carr's 3), so e ≤ 2|V3|; equality excluded by H-construction. Status `derived`,
  NOT formally/Lean-checked and source is a forum post — but the mathematics is
  confirmed. Verification in `notes/verify-2-3-degree-fraction.md`. Remaining
  caveat: no independent/formal check, and the near-cubic thread may still
  combine it with the oracle. Do not re-verify from scratch; read the note.

## Closed (answered from the library)

- **Liu–Ma "Cycle lengths and minimum degree of graphs" full text — CLOSED**
  (NEW). arXiv:1508.07912 (JCTB 134 (2019) 36–75) is now held in full text at
  `sources/liu-ma-cycle-lengths-minimum-degree.full.md` (was abstract-only).
  Confirms from primary text that the minimum-degree interval machinery
  (Thms 1.1–1.13: ⌊k/2⌋ consecutive even cycle lengths at δ≥k+1, modulo-k
  results, chromatic bounds) produces only blocks of consecutive/residue-
  termed lengths, never a prescribed power of two — at δ=3 (k=2) exactly
  Bondy–Vince. Primary-source closure of the interval-obstruction gap.

- **Original EFGS 1988 paper — CLOSED** (NEW). The foundational
  Erdős–Faudree–Gyárfás–Schelp paper "Cycles in graphs without proper subgraphs
  of minimum degree 3" (Ars Combin. 25B:195–201) is now held in full text from
  the Rényi archive (`sources/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.full.md`).
  Establishes the degree-3-critical class baseline (min degree 3, C3/C4, longest
  cycle Ω(log n), high-girth constructions) and the EFGS Conjecture (all cycles
  ≤ k, k→∞) that NPS later refuted.

- **Narins–Pokrovskiy–Szabó full text — CLOSED** (NEW). Springer DOI is
  paywalled, but the arXiv version (1408.5289, arXiv HTML) is now held in full
  at `sources/narins-szabo-degree3-critical-short-cycles.full.md` (71 KB).
  Establishes Theorem 1.2 (degree-3-critical graphs with no 23-cycle, disproving
  EFGS Conjecture 1.1), Thm 1.3 (even 1–3 trees: leaf-leaf lengths 0,2,...,18
  forced, none of length 20 in an infinite family), Thm 1.4 (non-induced
  degree-3-critical ⇒ pancyclic), the G(T) construction, and Lemma 2.1
  (cycle↔leaf-leaf-path dictionary). This is the primary source the near-cubic
  thread's 1–3-tree material builds on.

- **Whether bipartite cubic graphs (30-vertex bound) can be improved — CLOSED**
  at ≥60 vertices. (unchanged)

- **Bensmail 2016 — CLOSED.** (unchanged)

- **Carr diameter-2 — CLOSED.** (unchanged)

- **Exoo data subpages — CLOSED** (NEW). N4610/N4832/G24a/G24b/N46/N468
  downloaded, all image-only; the substantive catalogue was already held. No
  further change to what was known from `exoo-cubic-no-4-8-16.full.md`.

- **A recent-survey restatement of the obstruction — CLOSED** (NEW).
  Montgomery's EMS Magazine 138 (2025) survey (full text now held)
  confirms Liu–Montgomery Thm 2.1: an absolute constant d>0 such that every
  graph with average degree ≥ d has a 2-power cycle, via a long interval of even
  cycle lengths that catches a power of two; and restates the E–G conjecture as
  open with a needed constant far below d.

- **Minimal-unavoidability frame — CLOSED** (NEW). Madaras–Tamášová, Opuscula
  Math. 38 (2018) 859–878 (full text now held): introduces minimal unavoidable
  cycle sets, proves several in plane graphs ({3,4,11}, {3,4,6,8}, {3,4,8,9},
  {3,4,7,9}, {3,5,6,7}), and leaves whether {2^k} is minimal-unavoidable in
  min-degree-3 graphs open.

- **Bondy–Vince 1998 primary text — CLOSED** (NEW). The interval result problem.md
  names as a lead is now held in full text
  (`sources/bondy-vince-cycles-differ-1-2.full.md`): Theorem 1 (≤2 vertices deg<3
  ⟹ two cycles differing by 1 or 2) and Theorem 2 (nonbipartite 3-connected ⟹
  difference 1), plus the exact statement of the Erdős–Gyárfás conjecture as it
  appears there. Confirms the obstruction from primary text.

- **The 3·2^k weakening in claw-free graphs — CLOSED as sourced statement*** (NEW).
  NEHB14 (arXiv:1109.5398v3, full text now held in
  `sources/nehb14-clawfree-3-2k.full.md`): every claw-free δ≥3 graph has a cycle
  of length 2^k or 3·2^k (Theorem 1); cubic claw-free counterexample ≥ 114
  vertices (Theorem 9). Verified against the full text this cycle; the
  Erdős–Gyárfás original negative belief is quoted verbatim.
