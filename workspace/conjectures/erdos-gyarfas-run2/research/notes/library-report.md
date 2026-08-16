# Erdős–Gyárfás reference library — build report

Date of build: this run. Library of primary treatments of the Erdős–Gyárfás
conjecture, its restricted-class proofs, its computational verification, and
the surrounding cycle-length machinery. All full texts are under
`research/sources/`, their structural digests under `research/summaries/`, and
everything is indexed so `search_documents` reaches it.

## Phase-1 exit: `research/ROOT.md` written

The phase-1 exit test (GOAL.md deliverable 1 / phase-1 stop condition) is met:
`research/ROOT.md` now synthesises the full library into (1) the obstruction
(interval/congruence machinery cannot hit a prescribed power of two; the only
δ ≥ 3 2-power-specific handles are the restricted-class structural proofs and
the counterexample-shape structure), (2) the structure of a minimal
counterexample (predominantly cubic, > 4/7 and derived > 2/3 of vertices degree
3, degree-≥4 set independent & dominated, induced-degree-3-critical with 2n−2
edges), (3) nine settled restricted classes with exact hypotheses, (4) the
current verification bound (Markström ≥ 17 / cubic ≥ 30; Balaji SMS ≥ 31
asserted-by-source; Markström 24-vertex and Exoo 78/540 near-misses), and (5)
a statement of the run's own standing and oracle-verified rungs. This is the
stop condition for phase 1: the library no longer grows except against a stated
gap in `notes/requests.md`.

## Canonical reference tier (statement, notation, history, names)

| Source | Full text | Digest | What it fixes |
| --- | --- | --- | --- |
| Wikipedia, "Erdős–Gyárfás conjecture" | `wikipedia-erdos-gyarfas-conjecture.full.md` | `summaries/wikipedia-erdos-gyarfas-conjecture.md` | The statement, the $100/$50 prizes, Royle & Markström's 17/30-vertex bounds, the list of settled classes, the bibliography of every primary source. |
| Erdős Problems #64 (T. Bloom) | `erdosproblems-64-power-of-two.full.md` | `summaries/erdosproblems-64-power-of-two.md` | The conjecture as Erdős's problem, the exact Liu–Montgomery resolution of the stronger "every fixed degree-3 graph avoids powers of 2"? claim, the infinite-tree falsity, the formalised-statement pointer (Lean). URL: https://www.erdosproblems.com/64 |
| The Formal Conjectures Lean statement | `formal-conjectures-64-lean.md` | `summaries/formal-conjectures-64-lean.md` | A machine-readable statement of the conjecture in Lean 4 (`answer(sorry) ↔ ...`), ready to build on for the formalisation deliverable. |
| West's Open Problems page | `west-openp-2powcyc.md` | `summaries/west-openp-2powcyc.md` | The exact hypotheses of Shauger's $K_{1,m}$-free result and Daniel–Shauger's planar claw-free result, plus Yair Caro's weaker variant. URL: https://dwest.web.illinois.edu/openp/2powcyc.html |

## Restricted classes settled

| Source | Class | Result | Full text |
| --- | --- | --- | --- |
| Heckman & Krakovski 2013 | 3-connected cubic planar | Contains a $2^m$-cycle with $2 \le m \le 7$; discharging method. Full proof downloaded. | `heckman-krakovski-cubic-planar-proof.full.md` (114 KB) |
| Gao & Shan 2022 | $P_8$-free | Contains a 4- or 8-cycle. | `gao-shan-p8-free.full.md` |
| Hu & Shen 2024 | $P_{10}$-free | Contains a 4- or 8-cycle. | `hu-shen-p10-free.full.md` |
| Hegde, Sandeep, Shashank 2024 | $P_{13}$-free | True; the $P_{13}$-free bound via computer search. | `hegde-etal-p13-free.full.md` |
| Salehi Nowbandegani et al. 2013 | claw-free (cubic claw-free) | Partial: Hobbs' question for claw-free graphs, esp. cubic claw-free. | `salehi-etal-clawfree.full.md` |
| Ghaffari & Mostaghim 2017 | Cayley graphs on quaternion, dihedral, semidihedral, order-$p^3$ groups | True. | `ghaffari-mostaghim-cayley.full.md` |
| Carr 2026 | Minimal counterexample | Predominantly cubic: high-degree vertices form an independent set, cubic vertices dominate, ≥ 4/7 of vertices cubic. | `carr-predominantly-cubic.full.md` |
| Daniel & Shauger 2001 | planar claw-free | True (cited in West & Wikipedia; primary is a conference proceedings not fetched). |
| Shauger 1998 | $K_{1,m}$-free with $\delta \ge m+1$ or $\Delta \ge 2m-1$ | True (cited in West). |

## The surrounding cycle-length machinery (where the obstruction lives)

| Source | Result | Relevance | Full text |
| --- | --- | --- | --- |
| Sudakov & Verstraëte 2008 | Avg-degree bound $e^{O(\log^* n)}$ for a graph on $n$ vertices with no 2-power cycle. | The strongest "sparse side" bound: how dense a graph must be to force a 2-power cycle. | `sudakov-verstraete-sparse.full.md` |
| Liu & Montgomery 2020 | High average degree forces all even cycle lengths in $[(\log \ell)^8, \ell]$; in particular a power of 2. Solves Erdős's stronger claim. | Disproves the "every fixed degree avoids powers of 2" conjecture; shows interval results DO eventually reach a power of 2. | `liu-montgomery-odd-cycle-and-powers-of-two.full.md` |
| Verstraëte 2005 | There is a zero-density set $S$, $|S\cap[1,n]|=O(n^{0.99})$, with every graph of avg degree ≥ 10 containing a cycle with length in $S$. | The unavoidable-cycle-length framework. Full text paywalled; abstract sourced. | — |
| Gao, Huo, Liu, Ma 2021 | Unified proof: cycles of all lengths mod $k$, consecutive-length cycles, etc. via arithmetic-progression path lemmas. | The standard interval/congruence machinery the obstruction says is insufficient. | `gao-huo-liu-ma-unified.full.md` |
| Markström 2004 | Extremal graphs from exhaustive search; the 24-vertex cubic planar graph with no 4-/8-cycle (but with a 16-cycle). | Source of the computational bound and the near-counterexamples. | `markstrom-extremal-graphs-cycles.full.md` |
| Balaji (SMS) 2026 | SAT-Modulo-Symmetries verification: no min-degree-3 counterexample on ≤ 30 vertices; every such graph has a 4-, 8-, or 16-cycle. | The newest verification bound (31), from Zenodo preprint. | `sms-verification-30-vertices.md` |

## The computational verification bounds (oracle anchor)

- Any counterexample has **≥ 17 vertices** (Royle, Markström). Source: Wikipedia;
  primary = Royle's searches reported in Markström.
- Any **cubic** counterexample has **≥ 30 vertices** (Markström 2004). Source:
  Wikipedia, Markström's paper.
- Bipartite cubic counterexample, if any, ≥ 30 vertices (Salehi Nowbandegani &
  Esfandiari 2011). Source: Wikipedia.
- SMS (Balaji 2026): every min-degree-3 graph on **≤ 30 vertices** has a 4-, 8-,
  or 16-cycle, so any counterexample has **≥ 31 vertices** (general and cubic).
  Source: Zenodo preprint `sms-verification-30-vertices.md`.
- Markström's 24-vertex cubic planar graph: no 4- or 8-cycles, has a 16-cycle —
  a near-miss that does not disprove the conjecture. Source: Wikipedia, Heckman
  & Krakovski.

## The obstruction, as the sources fix it

The literature's interval and congruence results (Gao–Huo–Liu–Ma; the
unavoidable-cycle set frameworks) deliver cycles at *some* length in a range or
residue class. The powers of two are sparse — the gap doubles each step — so an
interval result needs length exceeding $2^k$ to be forced to contain one. The
two genuinely "2-power-specific" positive results are:
1. Sudakov–Verstraëte: *average degree* `e^{O(log* n)}` forces a 2-power cycle
   (sparse-class, avg degree, not min degree 3);
2. Liu–Montgomery: huge average degree forces all even lengths up to $\ell$,
   hence a 2-power.
Neither applies at uniform `min degree 3`, which is exactly the gap this run
must attack.

## Gaps / what could not be obtained

- **Verstraëte 2005 "Unavoidable cycle lengths in graphs"** — full text is
  paywalled at Wiley (cookie/login wall; download returned only the abstract).
  The abstract and the exact $O(n^{0.99})$ statement are sourced from
  semanticscholar/exa. Not downloaded as full text.
- **Daniel & Shauger 2001** (planar claw-free) and **Shauger 1998**
  ($K_{1,m}$-free) — conference proceedings, no open full text found. The
  *statements* are sourced from West's page and Wikipedia; the proofs are not in
  the library.
- **Original Erdős problem papers** (Er93, Er95, etc.) — cited but not fetched;
  the Erdős Problems #64 page quotes the relevant passages.

## Librarian cycle log — this cycle's additions

The library was already at the gap-driven steady state: every canonical reference and
all settled restricted classes were held, and the open rows in `notes/requests.md` are
either paywalled-and-unreachable or flagged "do not re-fetch." One genuine gap was
closed this cycle:

- **Pirzada–Shah–Baskoro 2022 full proof — CLOSED.** Previously the library held only
  a landing page for "On 2-power unicyclic cubic graphs" (EJGTA 10(1):337–344,
  doi:10.5614/ejgta.2022.10.1.24) with the construction "not held" and the abstract
  flagged as over-claiming. The full PDF text is now held at
  `research/sources/pirzada-2power-unicyclic-proof.full.md` (from the download URL
  https://ejgta.org/index.php/ejgta/article/download/1312/pdf_224). Verified against
  the full text: Theorem 2.1 constructs 2-power unicyclic cubic graphs G_i
  (|G1|=94 only C32, |G2|=222 only C64, |G3|=478 only C128, builder |G_i|=|G_{i-1}|+2^{i+4}),
  each with a single prescribed power-of-two cycle length. **The paper's Conclusion
  over-claims to rule out all counterexamples, but that final step is circular
  (it invokes the conjecture as an observation) and is NOT established.** Claim
  `pirzada-2power-unicyclic` filed; holdings note corrected.
- Also noted: `research/sources/pirzada-2power-unicyclic-cubic.full.md` is a
  **mislabeled pre-existing capture** of the EJGTA Vol 14 No 1 (2026) table of
  contents, not the 2022 article — do not use it as the article text. The proper full
  text is `pirzada-2power-unicyclic-proof.full.md`.

**Remaining gaps unchanged** (all marked do-not-re-fetch or confirmed unreachable):
Gebendorfer 2026 full text (HTTP 410), Shauger/Daniel–Shauger proceedings proofs
(statement-only), original Erdős 1997 problem paper (paywalled), and the body of
Verstraëte's 2016 survey (paywalled; bibliography held). Further fetching happens only
against a new stated gap in `notes/requests.md`.

## Librarian cycle log — this cycle's additions (prior)



Surveyed the whole library. It was already comprehensive (27 full texts + ~40
summaries covering statement tier, primary papers, surveys, verification
bounds, counterexample constructions, adjacent cycle-length machinery). Closed
the one remaining gap in the canonical statement tier:

- **Added `sources/ucsd-erdosproblems-69-power-of-two-cycles.full.md`** +
  `summaries/ucsd-erdosproblems-69-power-of-two-cycles.md`: the **UCSD Erdős
  problems collection page #69** ("The Erdös–Gyárfás conjecture",
  mathweb.ucsd.edu/~erdosproblems), twin of the held /64 page. Captured verbatim
  via `read_sources` because the direct `download_document` of that URL failed
  at the network layer (recorded as captured copy, not native download). Adds
  the classic five-entry bibliography with exact venues/pages (Shauger 1998
  Congr. Numer. 171:61–65; Daniel–Shauger 2001 Proc. 32nd SE Conf. 153:129–139;
  Markström 2004 Congr. Numer. 171:179–192; Sudakov–Verstraëte 2008 Combinatorica
  28:357–372; Verstraëte 2005 JGT 49:151–167) and the older $100/$50 prize.
  Claim `ucsd-69-statement` filed; re-derives CLAIMS.md.

- Ran `citation_graph` on Bensmail (10.7151/dmgt.1926), Liu–Ma "Cycle lengths
  and minimum degree" (10.1016/j.jctb.2017.08.002), and "Well-mixing vertices"
  (10.1090/proc/16090). Connected works (unavoidable sets, q-power / 2-power
  constructions, cycle-length distribution, expanders/long-cycles) were all
  already represented in the library via the six existing `citations_*.md`
  side-files; no new primary source was needed.

- Ran `exa_search` on the thinnest angles (Shauger original, Balaji
  peer-review, high-girth): returned only works already held. No new source
  merited a download.

**Gaps remain as stated above** (paywalled Erdős originals + Verstraëte survey
body + Verstraëte 2005; conference-proceedings Shauger/Daniel–Shauger proofs
unobtainable, statements sourced secondhand). Further fetching happens only
against a new stated gap in `notes/requests.md`.

## Cycle log — Combinatorica 2026 degree-3-critical paper

- Searched every angle (Pk-free, minimal counterexample, 2025–2026 partial
  results, computational bound, Cayley, bipartite/non-planar): returned only
  sources already in the library — confirming the library is at the point where
  the literature's settled results are all held and further gathering must be
  gap-driven.
- One genuinely new primary source found and downloaded:
  `sources/degree-3-critical-leaf-to-leaf-cycles.combinatorica.full.md`
  (Combinatorica 2026, doi:10.1007/s00493-026-00205-2). Degree-3-critical
  graphs are the minimal-counterexample spine; Theorem 1 (Ω(log n) distinct
  cycle lengths) and Theorems 3–5 (sparse spectra possible, tight up to
  constant) are structural constraints on that spine, though not a proof step —
  Ω(log n) lengths do not force a power of two. Digest replaced,
  `remember_memory` stored, `library-holdings.md` updated, claim
  `dcg-degree3-critical-omn-log-n-cycle-lengths` filed.

## Cycle log — Liu–Ma minimum-degree full text

- The library already held every settled restricted class, every verification
  bound, every held counterexample construction, and the 2-power-forcing
  results (Sudakov–Verstraëte, Liu–Montgomery). One primary-source gap
  remained in the **interval machinery** section: the paper `problem.md`
  names as "Liu–Ma" — Liu & Ma, "Cycle lengths and minimum degree of graphs"
  (arXiv:1508.07912) — was held only as citation-side-file summaries
  (`citations_w2963120913.md`), never as the primary text.
- Closed it: `sources/liu-ma-cycle-lengths-minimum-degree.full.md` now holds
  the full 110 KB text (arXiv experimental HTML). Digest replaced at
  `summaries/liu-ma-cycle-lengths-minimum-degree.md`, claim
  `lm-min-degree-interval-results` filed, `remember_memory` stored,
  `library-holdings.md` and `notes/requests.md` updated.
- **What it establishes (primary text):** every Liu–Ma theorem (Thms 1.1–1.13)
  produces blocks of consecutive or residue-termed cycle lengths. At the
  run's regime δ = 3 (k = 2), Thm 1.3 gives a pair of cycles differing by 2
  (a 4- or 6-cycle) — Bondy–Vince — never an 8/16/32. This is the cleanest
  **primary-text confirmation of the obstruction problem.md names**: interval
  results cannot settle E–G at δ ≥ 3; the run must produce a cycle at a
  prescribed power of two. Nothing newly downloads unless a stated gap opens.

**Remaining unobtainable (recorded, do not re-fetch):** paywalled Erdős
originals + Verstraëte survey body + Verstraëte 2005 full text; conference-
proceedings Shauger 1998 / Daniel–Shauger 2001 proofs (statements sourced
secondhand). Gebendorfer 2026 full proof text (Zenodo 410 Gone; abstract held
and flagged as contradicting three held constructions).

