# Library holdings — Erdős–Gyárfás conjecture

Maintained by the librarian. Full texts (unedited) in `sources/`, digests in
`summaries/`. This note records what the library holds, what it establishes at
source level, and what could not be obtained and why. Build log under
`notes/library-report.md`.

## Added this cycle (librarian)

- `sources/lyngsie-merker-cycle-lengths-modulo-k-cubic.full.md` +
  `summaries/lyngsie-merker-cycle-lengths-modulo-k-cubic.md` — **Lyngsie &
  Merker, "Cycle lengths modulo k in large 3-connected cubic graphs",
  Advances in Combinatorics (2021), doi:10.19086/aic.18971, arXiv:1904.05076v2 —
  FULL TEXT now held** (104 KB, open-access arXiv PDF; previously only a
  citation side-file). Theorem 1.1: for every odd k there is N(k) such that
  every 3-connected cubic graph of order ≥ N(k) contains a cycle of length m
  modulo k for every m. Best possible — false for 2-connected cubic (family when
  m,k divisible by 3, k≥12) and false for 3-connected min-degree-3. Closes the
  adjacent congruence-mod-k angle; realises lengths in a residue class, never a
  prescribed power of two, so it anchors (not settles) the obstruction. Claim
  `lm-modd-k-cubic` filed.

- `sources/liu-ma-cycle-lengths-minimum-degree.full.md` +
  `summaries/liu-ma-cycle-lengths-minimum-degree.md` — **Liu & Ma, "Cycle
  lengths and minimum degree of graphs", arXiv:1508.07912 (JCTB 134:36–75,
  2019) — FULL TEXT now held** (110 KB, arXiv experimental HTML; previously
  abstract-only). The *minimum-degree* interval machinery paper `problem.md`
  names as a lead. Theorems 1.1–1.13 (consecutive even/odd cycle lengths at
  δ≥k+1, modulo-k results settling Thomassen for even k, chromatic-number
  bounds) all produce blocks of consecutive or residue-termed cycle lengths,
  none a prescribed power of two. At δ=3 (k=2) gives only a 2-cycle pair
  differing by 2 (Bondy–Vince), not 8/16/32. **Primary-text confirmation of the
  obstruction**: interval results cannot settle E–G at δ≥3; the run must
  produce a cycle at a prescribed length. Claim `lm-min-degree-interval-results`
  filed in CLAIMS.md.

## Added this cycle (librarian)

- `sources/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.full.md` + `summaries/erdos-faudree-gyarfas-schelp-cycles-degree3-critical.md` — **Erdős–Faudree–Gyárfás–Schelp, Ars Combin. 25B (1988) 195–201 — FULL TEXT** (Rényi archive PDF: renyi.hu/~p_erdos/1988-06.pdf). The **foundational paper defining degree-3-critical graphs** (n vertices, 2n-2 edges, no proper subgraph of min degree 3). Proves: min degree 3, C3 & C4 (n≥5), longest cycle Ω(log n) (Thm 5), high-girth constructions (Thm 4), and the EFGS Conjecture (all cycles ≤ k, k→∞) — disproved by NPS. Previously the library held only retellings. Closes a long-standing gap.
- `sources/rautenbach-leaf-to-leaf-paths-trees.full.md` + `summaries/rautenbach-leaf-to-leaf-paths-trees.md` — **Rautenbach–Scherer–Werner, arXiv:2507.10351v2 (2025), 1–3 trees**. Proves $lp(T) \ge \mathrm{rad}(s) - \log_2(\mathrm{rad}(s))$ for a tree $T$ with no degree-2 vertex and degree sequence $s$ (Conjecture 2 target $lp \ge \mathrm{rad}(s)-O(1)$ left open). Answers a question from Di Braccio et al.; part of the degree-3-critical / 1–3 tree literature the near-cubic spine rests on. Full text downloaded (arXiv HTML).
- `sources/narins-szabo-degree3-critical-short-cycles.full.md` + `summaries/narins-szabo-degree3-critical-short-cycles.md` — **Narins–Pokrovskiy–Szabó, Combinatorica 37 (2017) 495–519 / arXiv:1408.5289 — FULL TEXT HELD** (arXiv HTML, 71 KB; Springer DOI paywalled). Primary source of the 1–3 tree construction: disproves EFGS conjecture that degree-3-critical graphs have all cycles 3..C(n) (Thm 1.2: an infinite family with no 23-cycle); Thm 1.3 (even 1–3 trees: leaf-leaf lengths 0,2,...,18 forced, an infinite family missing length 20); Thm 1.4 (non-induced degree-3-critical ⇒ pancyclic); the G(T) construction and Lemma 2.1 cycle↔leaf-leaf-path dictionary. Closes the open request.

## Added this cycle (librarian) — prior

- `sources/degree-3-critical-leaf-to-leaf-cycles.combinatorica.full.md` + `summaries/degree-3-critical-leaf-to-leaf-cycles.combinatorica.md` — **"Leaf-to-leaf paths and cycles in degree-critical graphs", Combinatorica (2026), doi:10.1007/s00493-026-00205-2**. Degree-3-critical graphs (2n−2 edges, no proper induced subgraph with δ≥3) are the exact structural class of the minimal-counterexample spine. Theorem 1: every n-vertex degree-3-critical graph has Ω(log n) distinct cycle lengths. Theorems 2–5: 1–3 trees can have as few as O(N^0.91) distinct leaf-to-leaf path lengths < N, and Ω(log n) cycle lengths is tight up to a constant. Directly relevant: claims feed the near-cubic structural thread. Note: Ω(log n) distinct cycle lengths does NOT force a power of two — sparse spectra are possible in the extremal class (Theorems 3–5), echoing Bensmail.
- `sources/cui-lo-tight-gaps-cycle-spectrum.full.md` + `summaries/cui-lo-tight-gaps-cycle-spectrum.md` — **Cui & Lo, "Tight gaps in the cycle spectrum of 3-connected planar graphs", arXiv:2009.02503 (2020)**. New primary source on the obstruction: fully characterizes which intervals [a,b] can be *gaps* (no cycle length in the interval) in the cycle spectrum of 3-connected (cubic) planar graphs. f₃(5)=10, f₃(7)=15, f₃(9)=20, f₃(k)=2k+3 for k=6,8,≥10; f(k)=2k+3 for k≥5 (general planar), resolving Merker's conjecture f(k)≤2k+c with c=3. Gap [k,2k+2] is achievable in cubic planar (Zamfirescu). Confirms the exact obstruction problem.md names: interval results give intervals of length only ~k, far short of the 2^k gap between powers of two — so a power of two must be caught at a prescribed length, which is why Heckman–Krakovski's discharging (not an interval argument) settles 3-connected cubic planar. Cites the classic Erdős 1997 problem paper. Note: download captured the arXiv abstract page; the detailed propositions in the summary came from read_sources triage of the same page.

## The canonical statement tier

| Source | File | What it fixes |
| --- | --- | --- |
| Wikipedia, Erdős–Gyárfás conjecture | `sources/wikipedia-erdos-gyarfas-conjecture.full.md` | Statement, prize ($100 proof / $50 counterexample), Royle–Markström 17 / cubic 30 bounds, four 24-vertex cubic no-C4-C8 graphs (one planar), 3-connected cubic planar case, open for bipartite cubic |
| erdosproblems.com/64 (Bloom) | `summaries/erdosproblems-64-power-of-two.md` | Canonical statement with k≥2, Erdős–Gyárfás's own (now disproved) negative belief, Liu–Montgomery result, infinite-graph trivial counterexample, Lean formalisation link |
| West, Open Problems (2powcyc) | `summaries/west-openp-2powcyc.md` | External standard reference; exact hypotheses of Shauger and Daniel–Shauger results; Yair Caro's weaker power variant |
| Formal Conjectures Lean statement (DeepMind) | `summaries/formal-conjectures-64-lean.md` | Existing Lean 4 formalisation of the conjecture (with a `sorry`) — reference for the Lean work |

## Primary research papers

| Source | File | Establishes |
| --- | --- | --- |
| Markström 2004, Extremal graphs for some problems on cycles | `sources/markstrom-extremal-graphs-cycles.full.md` | Verification of cubic graphs ≤28 vertices for C4,C8,C16; four 24-vertex cubic without C4,C8 (contain C16, one planar); minimal-counterexample degree structure (independent set of deg≥4 + nonempty deg-3 set); Royle's <16-vertex general search |
| Carr 2026, arXiv:2605.22844 — **FULL PROOF NOW HELD** | `sources/carr-predominantly-cubic.full.md` (abstract), **`sources/carr-predominantly-cubic-fulltext.html.full.md`** (full proof, previously abstract-only) | Minimal counterexample is predominantly cubic: every vertex adjacent to a deg-3 vertex, deg≥4 vertices independent, ≥4/7 of vertices have degree 3, regular counterexample is cubic. **The 2/3 improvement (|V3| ≥ 2|V≥4|+1) is verified this cycle against this full proof** — see `notes/verify-2-3-degree-fraction.md`.
| Gao–Shan 2021, arXiv:2109.01277 | `sources/gao-shan-p8-free.full.md` | P8-free graphs with δ≥3 contain a C4 or C8 |
| Hu–Shen 2023, arXiv:2308.05675 | `sources/hu-shen-p10-free.full.md` | P10-free graphs with δ≥3 contain a C4 or C8 |
| Hegde–Sandeep–Shashank 2024, arXiv:2410.22842 | `sources/hegde-etal-p13-free.full.md` | P13-free (and P12-free) with δ≥3 contain a 2-power cycle / C4-C8, computer-assisted |
| Carr 2025/26, arXiv:2508.19302 — FULL PROOF | `sources/carr-diameter2-c4-c8.full.md` (24 KB), summary `summaries/carr-diameter2-c4-c8.md` | Diameter-2 graphs with δ≥3 contain a C4 or C8 (Theorem 1.1, full two-case proof held); confirms E–G for the diameter-2 class; accepted at BICA |
| Pirzada–Shah–Baskoro 2022, EJGTA 10(1) 337–344 | `sources/pirzada-2power-unicyclic-cubic.full.md` (label MISLEADING — actually a capture of the 2026 issue TOC, not the article), proper full text at **`sources/pirzada-2power-unicyclic-proof.full.md`** (full proof from the PDF), listing page `sources/pirzada-2power-unicyclic-fulltext.full.md`, summaries `summaries/pirzada-2power-unicyclic-proof.md` + `summaries/pirzada-2power-unicyclic-fulltext.md` | **Construction now held in full**: infinite family of 2-power unicyclic cubic graphs G_i (|G1|=94 only C32, |G2|=222 only C64, |G3|=478 only C128), each with a single 2-power cycle of a prescribed length. **The paper's own Conclusion over-claims to rule out all counterexamples — that step is circular and NOT established; cite only the construction.** Claim `pirzada-2power-unicyclic` |
| Salehi-Nowbandegani–Esfandiari–Haghighi–Bibak 2011/2014, claw-free | `sources/salehi-etal-clawfree.full.md`, **`sources/nehb14-clawfree-3-2k.full.md`** (full proof) | Claw-free partial results: **Thm 1 (δ≥3 claw-free ⟹ cycle of length 2^k or 3·2^k) and Thm 9 (cubic claw-free counterexample ≥ 114 vertices)** — full proof text now held; Hobbs's question; cubic claw-free studied |
| Heckman–Krakovski 2013, cubic planar — FULL PROOF | `sources/heckman-krakovski-cubic-planar-proof.full.md` (114 KB) | 3-connected cubic planar graphs contain 2^m-cycle with 2≤m≤7; discharging method, computer-assisted parts; corollary: bounded-local-search detection |
| Liu–Montgomery 2020, arXiv:2010.15802 | `sources/liu-montgomery-odd-cycle-and-powers-of-two.full.md` | Large average degree forces a 2-power cycle; strong interval result in even cycle lengths |
| Sudakov–Verstraëte 2008, arXiv:0707.2117 | `sources/sudakov-verstraete-sparse.full.md` | No-2-power-cycle graphs have average degree ≤ e^{O(log* n)} |
| Ghaffari–Mostaghim 2018, Cayley graphs | `sources/ghaffari-mostaghim-cayley.full.md` | E–G holds for Cayley graphs on quaternion/dihedral/semidihedral/order-p^3 groups |
| Gao–Huo–Liu–Ma 2019, arXiv:1904.08126 | `sources/gao-huo-liu-ma-unified.full.md` | Adjacent theory: tight min-degree conditions forcing long APs of cycle lengths (mod k, consecutive) |

## Computational verification (the oracle anchor)

| Source | File | Bound established |
| --- | --- | --- |
| Royle & Markström (computer search) | via Wikipedia/Markström | any counterexample ≥ 17 vertices; any cubic counterexample ≥ 30 vertices |
| Salehi Nowbandegani & Esfandiari 2011 | via Wikipedia | bipartite cubic counterexample, if any, ≥ 30 vertices |
| Balaji SMS 2026, v1 (Zenodo 20782739) | `summaries/sms-verification-30-vertices.md` | every δ≥3 graph on ≤30 vertices has a C4/C8/C16; general counterexample ≥ 31 |
| Balaji SMS 2026, v2 (Zenodo 20782738) | `summaries/sms-verification-31-vertices.md` | every δ≥3 graph on ≤31 vertices has a C4/C8/C16; general counterexample ≥ 32; hardest orders each ~2 CPU-hours; robust to CEGAR, encodings, nauty check |

## Bensmail's q-power construction (now held in full text)

**Result (Bensmail 2016, Discuss. Math. Graph Theory 37(1):211–220, doi:10.7151/dmgt.1926):**
- For every q ≥ 3, there exist arbitrarily large cubic graphs with **no** q-power cycle.
- For q = 2 (the Erdős–Gyárfás case), there exist arbitrarily large cubic graphs whose all 2-power cycles have length **4 only**, or **8 only**.

The full construction is now held at `research/sources/bensmail-q-power-construction.full.md`
(bibliotekanauki mirror of the DMGT PDF — see the next section). This section
keeps the historical caution: the arXiv ID 1508.05567 resolves to a *different,
unrelated* paper (dual-based network-connectivity approximations, not q-power
cycles), and the earlier download `bensmail-q-power-cycles-cubic.full.md` is
mislabeled — **do not cite it** as Bensmail's q-power paper. Use
`bensmail-q-power-construction.full.md`, which is the genuine full text.

## Bensmail's construction — full text now held

`research/sources/bensmail-q-power-construction.full.md` holds Bensmail's
written proof (bibliotekanauki PDF of *Discuss. Math. Graph Theory*
37(1):211–220, doi:10.7151/dmgt.1926). Confirms and upgrades the claim:
- q ≥ 6: arbitrarily large **planar cubic** graphs with no q-power cycle (Thm 9).
- q = 5, 4, 3: the same (Thms 14, 18, 22).
- q = 2: arbitrarily large cubic graphs whose only 2-power cycles all have
  length 4, or all length 8.
Construction: start from an internally cubic tree, attach edge-gadgets to the
leaves to raise every degree to 3 while controlling all possible cycle lengths.
(This closes the longest-open request in `notes/requests.md`.)

## Couch–Daniel–Wright 2021 — Caro's weakening held

`research/sources/couch-daniel-wright-cubic-integer-power.full.md` (Australas.
J. Combin. 79 (2021) 100-105). Addresses Caro's variant — every δ≥3 graph has a
cycle of length a^k for some a≥2, k≥2. Proves (verified against full text):
- **Theorem 1**: graph with a cycle D (each vertex deg 3, each in exactly one
  triangle, D meets each triangle in ≤1 edge, D length ≠ 10) contains a cycle of
  length a^k. Uses Paz's density lemma (a perfect power in [2n,3n] except n=5).
- **Corollary 1**: every claw-free δ≥3 graph has such a cycle.
- **Corollary 2**: claw-free δ≥2, Δ=3, ≤2 vertices of degree 2 → such a cycle.
- **Theorem 2**: min degree 3 and the set of centers of induced claws is
  independent → such a cycle.
- **Theorem 3**: every almost claw-free graph with min degree 3 has such a cycle.
Cites Shauger 2002 (Congr. Numer. 159:119–126): *claw-free cubic graphs of low
genus have a cycle of length a power of two* — an additional E-G settled class.
A strictly weaker target than power-of-two, useful as a rung on the weakened
ladder.

## Computational catalogue — Exoo & Markström's no-fixed-cycle graphs

- `research/sources/exoo-cubic-no-4-8-16` (as summary; page is small):
  catalogue of trivalent graphs avoiding specified cycle lengths. **The
  smallest cubic graph Exoo knows with no {4,8,16} cycles has 78 vertices; the
  smallest with no {4,8,16,32} cycles has 540 vertices.** These are "smallest
  known", not proven exhaustive (Markström's complete search reaches only
  N≤52 for no-{4,8,16} cubic graphs).
- `research/sources/markstrom-cubic-avoiding-cycles` (as summary): exhaustive
  search for 3-connected cubic graphs avoiding given cycle lengths (minibaum
  generator). Complete for no-{4,8,16} up to N≤52 (none); also searches
  no-{4,6,8,10,12}.
These extend the near-counterexample landscape dramatically past the 32-vertex
verification bound: a 540-vertex cubic graph avoiding {4,8,16,32} survives as a
potential counterexample pending whether it contains a ≥64 2-power cycle.

## Computational verification — new 2026 results

- **Balaji (SMS), general δ≥3:** `research/sources/balaji-sms-github.full.md`
  and summaries `sms-verification-31-vertices.md`. SAT-Modulo-Symmetries with
  Glasgow subgraph solver verifies every δ≥3 graph on ≤31 vertices has a
  C4/C8/C16; any general counterexample ≥ 32 vertices (frontier 17→32).
  Independent CEGAR-SAT agrees for n≤19; exact nauty check at n=10. Code
  archived at GitHub `ArjunBalaji79/erdos-gyarfas-min-degree-3`. 2026 preprint,
  under review at Experimental Mathematics (not journal-certified; no formal
  proof certificate).
- **Balaji, cubic bipartite:** `research/sources/balaji-bipartite-60-vertex.full.md`
  (arXiv:2608.02675). Certified exhaustive computation: every simple cubic
  bipartite graph on ≤58 vertices has a C4/C8/C16; any cubic bipartite
  counterexample ≥ 60 vertices (frontier 30→60). Method: Levi-graph encoding of
  a v3-configuration, two rooted extensions, restricted-growth search, checked
  by two independent C16 oracles + static witness certificate. This is the
  *independently certified* bound for the explicitly open bipartite cubic
  class.

## Could not be obtained and why

- **Verstraëte 2016, "Extremal problems for cycles in graphs" (survey, Recent
  Trends in Combinatorics, doi:10.1007/978-3-319-24298-9_4)** — chapter body
  paywalled at Springer; only the abstract + full bibliography captured
  (400 refs → FRONTIER). Abstract and bibliography held in
  `sources/verstraete-extremal-problems-cycles-survey.full.md`; the chapter's
  body must not be cited for any theorem.
- **Verstraëte 2005, "Unavoidable cycle lengths in graphs"** (JGT 49:151–167, doi:10.1002/jgt.20072) — full text paywalled at Wiley (cookie/login wall; download returned only the abstract). Abstract sourced: "there is a zero-density set S with |S∩{1,...,n}| = O(n^0.99) such that every graph of average degree ≥ 10 contains a cycle whose length is in S." Held in `summaries/verstraete-unavoidable-cycle-lengths.md`.
- **Daniel–Shauger 2001** (planar claw-free) and **Shauger 1998** (K_{1,m}-free) — conference proceedings, no open full text. Exact hypotheses sourced from West's page: "K_{1,m}-free with minimum degree ≥ m+1 OR maximum degree ≥ 2m−1".
- **Original Erdős problem papers** (Er93, Er95) — paywalled (ScienceDirect); but the Erdős–Gyárfás original negative belief is preserved verbatim in the held NEHB14 full text (`sources/nehb14-clawfree-3-2k.full.md`), and erdosproblems.com/64 quotes the relevant passages.
- **(Clarification) Bensmail 2016** — full text IS now held at `sources/bensmail-q-power-construction.full.md`; the earlier download `bensmail-q-power-cycles-cubic.full.md` is mislabeled and is NOT Bensmail. arXiv 1508.05567 is NOT Bensmail either.

## Added this cycle (librarian) — NEW

- `sources/exoo-three-graphs-G420-no-4-8-16.full.md` + `summaries/exoo-three-graphs-G420-no-4-8-16.md` — **Exoo, "Three Graphs and the Erdős–Gyárfás Conjecture", arXiv:1403.5636 (2014)**. New primary source: **G420**, a 3-connected cubic **planar** graph derived from the Buckyball with **no 4-, 8-, or 16-cycle** — shows Heckman–Krakovski's uniform m≤7 cannot be lowered to m≤4 even inside the 3-connected cubic planar class; plus the apparent smallest-known cubic graphs with no 2^m-cycle for m≤4 (Petersen-derived) and m≤5 (Tutte–Coxeter-derived). Directly confirms the short-2-power obstruction and refutes any "forces a C4/C8" claim.

- `summaries/gebendorfer-proof-of-erdos-gyarfas.abstract.md` — **Gebendorfer 2026 Zenodo preprint (doi:10.5281/zenodo.18232846) claiming a full proof** of the conjecture. Full text NOT obtained (Zenodo 410 on fetch); abstract captured. Its central dichotomy "every δ≥3 graph is forced to contain a C4 or C8" is **contradicted** by held Markström 24-vertex (no C4/C8), Exoo 78/540-vertex, and Exoo G420. Treat the conjecture as still open; do not cite this preprint as a proof.

## Added this cycle (librarian) — prior

- `sources/ucsd-erdosproblems-69-power-of-two-cycles.full.md` + `summaries/ucsd-erdosproblems-69-power-of-two-cycles.md` — the **UCSD Erdős problems collection page #69** ("The Erdös–Gyárfás conjecture", mathweb.ucsd.edu/~erdosproblems). The graphs-problem-collection twin of the already-held erdosproblems.com/64 forum/statement page. Fixes the **classic five-entry bibliography with exact venues/pages**: Shauger 1998 (K_{1,m}-free, Congr. Numerantium 171:61–65), Daniel–Shauger 2001 (planar claw-free, Proc. 32nd SE Conf. 153:129–139), Markström 2004 (Congr. Numerantium 171:179–192), Sudakov–Verstraëte 2008 (Combinatorica 28:357–372), Verstraëte 2005 (JGT 49:151–167). Prize on this page is **$100 proof / $50 counterexample** (matches West's page, not the $1000 on /64). All five cited works already held as summaries; this adds exact bibliographic detail. Note: direct `download_document` of the URL failed at the network layer; the verbatim content was captured via `read_sources`, so the `.full.md` is a captured copy, not a native download.

## Added this cycle (librarian)

- `sources/nehb14-clawfree-3-2k.full.md` — **full proof text of NEHB14**
  (arXiv:1109.5398v3, "On the Erdős–Gyárfás conjecture in claw-free graphs").
  Previously abstract-only in the library; now holds Theorem 1 (claw-free δ≥3
  ⟹ 2^k or 3·2^k cycle) and Theorem 9 (cubic claw-free counterexample ≥ 114
  vertices), verified against the full text, plus the Erdős–Gyárfás original
  negative belief quoted verbatim. Summary `summaries/nehb14-clawfree-3-2k.md`,
  claim `nehb14-clawfree-3-2k`. This closes the open request for NEHB14.
- `sources/bondy-vince-cycles-differ-1-2.full.md` — **Bondy & Vince (1998), JGT 27:11–15**, primary text of the interval result problem.md names as a lead but the library previously held only secondhand. Theorems 1–2: δ≥3 (≤2 vertices deg<3) forces two cycles differing by 1 or 2; nonbipartite 3-connected forces difference 1. Confirms from primary text that interval results cannot force a sparse 2^k. Summary `summaries/bondy-vince-cycles-differ-1-2.md`, claim `bondy-vince-theorem1`.
- `sources/erdosproblems-64-discussion.full.md` — **erdosproblems.com #64 forum thread**. Carries the most complete published list of confirmed restricted classes (Alfaiz), the new **unverified** 2/3 degree-fraction claim (jul059), and flags two settled classes not previously held: Ghasemi–Varmazyar Cayley graphs of order 2p^2/4p, and the NEHB14 3·2^k weakening. Summary `summaries/erdosproblems-64-discussion.md`, claims `ce-2-3-degree-fraction`, plus the Alfaiz list.
- `sources/ghasemi-varmazyar-cayley-2p2-4p.full.md` — **Ghasemi & Varmazyar, Mat. Vesnik 282 (2022) 37–42**, new settled class: Cayley graphs of order 2p^2 (cycle of length 4/8/16) and 4p (a 4-cycle). Summary `summaries/ghasemi-varmazyar-cayley-2p2-4p.md`, claim `ghv-cayley-2p2-4p`.

## Added this cycle (librarian)

- `sources/madaras-tamasova-minimal-unavoidable-sets.full.md` (28 KB) —
  **Madaras & Tamášová, "Minimal unavoidable sets of cycles in plane graphs",
  Opuscula Math. 38 (2018) 859–878, doi:10.7494/opmath.2018.38.6.859.** New
  framework: a set S of cycles is *minimal unavoidable* in a family if every
  graph contains one and every proper subset is avoided by an infinite subfamily.
  Reframes E–G as an unavoidability (resp. minimal-unavoidability) statement on
  S={2^k:k≥2} in min-degree-≥3 graphs — whether {2^k} is minimal-unavoidable is
  open. In plane graphs (δ≥3) proves {3,4,11}, {3,4,6,8}, {3,4,8,9}, {3,4,7,9},
  {3,5,6,7} are each minimal unavoidable; note {8} in a minimal unavoidable
  plane set. Summary `summaries/madaras-tamasova-minimal-unavoidable-sets.md`,
  claim `madaras-minimal-unavoidable`.
- `sources/montgomery-cycles-and-expansion-survey.full.md` (41 KB) —
  **R. Montgomery, "Cycles and expansion in graphs", EMS Magazine 138 (2025)
  5–12, doi:10.4171/MAG/287 (open access).** Recent survey of expansion-based
  cycle results. Reports **Liu–Montgomery Thm 2.1**: an absolute constant d>0
  such that every graph with average degree ≥ d has a cycle whose length is a
  power of 2 (method works for any even k_{i+1} ≤ exp(k_i^{1/10})); mechanism is
  a long interval of even cycle lengths that catches a 2-power. States the
  Erdős–Gyárfás conjecture as Conjecture 2.2, open, likely needing a much
  smaller constant. Also Liu–Montgomery Thms 2.3/2.4 (harmonic-sum bounds).
  Summary `summaries/montgomery-cycles-and-expansion-survey.md`, claim
  `lm-large-avgdeg-forces-2power`.
- Exoo catalogue data subpages: N4610, N4832, G24a, G24b, N46, N468 now
  downloaded (`summaries/exoo-*.md`). They are **image-only** (automorphism
  group / similar-vertices-by-colour notes); the substantive content (78- and
  540-vertex no-{4,8,16} / no-{4,8,16,32} graphs, the 32-vertex no-{4,8,32}
  graph) was already in the held `exoo-cubic-no-4-8-16.full.md` index page.
- `sources/verstraete-extremal-problems-cycles-survey.full.md` (79 KB) —
  Verstraëte, "Extremal problems for cycles in graphs", Recent Trends in
  Combinatorics, Springer/IMA (2016), doi:10.1007/978-3-319-24298-9_4.
  **PARTIAL: chapter body paywalled** — only the abstract + full bibliography
  (400 refs) captured. Indexed as a lead-generator and scope-fixer; must NOT be
  cited for any theorem. Summary `summaries/verstraete-extremal-problems-cycles-survey.md`,
  claim `verstraete-survey-2016`.

## Added this cycle (librarian)

- `sources/gebendorfer-girth6-vertex-transitive.census.full.md` (41 KB) +
  `summaries/gebendorfer-girth6-vertex-transitive.census.md` — **J. J.
  Gebendorfer, "The Erdős–Gyárfás Conjecture for Cubic Vertex-Transitive
  Bipartite Graphs of Girth Six: A Complete Census Verification with
  Structural Analysis", Zenodo 18505377 (2026-02-06).** New restricted class
  settled: every cubic bipartite vertex-transitive girth-6 graph up to 1280
  vertices (all 58,438 in the Potočnik–Spiga–Verret census) contains a power-of-two
  cycle with `kmin ≤ 5`. Dyadic trichotomy: most have a 16-cycle, 2,868 have an
  8-cycle, exactly 14 have a 32-cycle but **no** 8- or 16-cycle (the PV(b)/PV(c)
  truncations). New claim `gebendorfer-cvt-g6-census`.
- `sources/gebendorfer-girth6-vertex-transitive.portvoltage.full.md` (55 KB) +
  `summaries/gebendorfer-girth6-vertex-transitive.portvoltage.md` — **companion
  paper (Zenodo 18526153, 2026-02-08 v3)**: the structural proof. A
  permutation–voltage framework (ring factor + voltage-labelled quotient)
  excludes 8- and 16-cycles via corner-cost/isoperimetric/face-shift lemmas and
  shows the 14 extremals each contain an explicit 32-cycle (mixed-hole words of
  weight 32 = identity in Aut of a regular map). New claim
  `gebendorfer-cvt-g6-extremals`. Both single-author 2026 preprints (same author
  as the unverified full-proof abstract); the census claim is a direct
  computation over an existing census, so more trustable, but not re-run here.

## The obstruction, as the sources fix it

Interval and congruence results (Gao–Huo–Liu–Ma; Verstraëte's unavoidable-set
framework) deliver cycles at *some* length in a range, not at a prescribed
power of two. The powers of two are sparse — the gap doubles each step — so an
interval result needs length exceeding 2^k to be forced to contain one. The two
2-power-specific positive results — Sudakov–Verstraëte (avg degree
e^{O(log* n)} forces a 2-power cycle) and Liu–Montgomery (huge avg degree
forces all even lengths up to ℓ, hence a 2-power) — both require *average
degree* far beyond 3. Neither applies at uniform min-degree 3, which is exactly
the gap this run must attack. Bensmail's construction is the strongest known
"near-counterexample" behaviour: arbitrarily large cubic graphs with all
2-power cycles of length 4 only or 8 only, so any structural argument must sit
alongside it.
