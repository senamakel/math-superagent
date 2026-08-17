# Librarian report — library completeness audit (this cycle)

## Conclusion in one line

The reference library already meets the phase-1 exit test and every standing
REQUEST row is answered by a primary full text on disk. This cycle's work was an
audit, two attempted acquisitions (one confirmed unobtainable), and a durable
record of the disposition — **not** a new swath of downloads, because nothing
on-topic and primary was missing.

## What the library holds (canonical tier, all with URLs inside the files)

`research/sources/*.full.md` (full texts, never edited), digests in
`research/summaries/*.md`, claims in the claims ledger, index in
`research/LIBRARY_LEDGER.md`.

### Primary sources held in full
- **Erdős–Szekeres 1935**, *A combinatorial problem in geometry*, Compositio Math. 2:463–470.
  Finiteness, cups-and-caps f(k,l)=C(k+l-4,k-2)+1, ES(n)≤C(2n-4,n-2)+1.
  `erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md`
  (numdam PDF).
- **Erdős–Szekeres 1960/61**, *On some extremum problems in elementary geometry*,
  Ann. Univ. Sci. Budapest. 3-4:53–62 — the **lower-bound construction** 2^{n-2}
  points with no convex n-gon. `erdos-szekeres-1961-...-renyi.pdf.full.md`
  (renyi.hu/~p_erdos/1960-09.pdf); concrete statement in
  `summaries/erdos-szekeres-1961-construction-concrete.md`. **Answers request
  `full-text-faithful-b96b`.**
- **Szekeres–Peters 2006**, *Computer solution to the 17-point ES problem*, ANZIAM J.
  48(2):151–164 — computes ES(6)=17, signature functions, ~1500 CPU-hours,
  three independent implementations. `peters-szekeres-17-point-esz-ANZIAM-2006.full.md`
  (Cambridge PDF).
- **Suk 2017**, *On the ES convex polygon problem*, JAMS 30:1047–1053 —
  ES(n) ≤ 2^{n+6n^{2/3}log n}. `suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md`.
- **Holmsen–Mojarrad–Pach–Tardos**, *Two extensions of the ES problem*,
  arXiv:1710.11415 — 2^{n+O(√(n log n))}. `holmsen-mojarrad-pach-tardos-...-full.md`.
- **Baek–Balko 2025**, *The ES Conjecture Revisited*, SoCG — ES_split(k)=2^{k-2}+1,
  decomposable classes. `baek-balko - ... SoCG 2025 correct.full.md`.
- **Chung–Graham 1998**, **Kleitman–Pachter 1998**, **Tóth–Valtr 1998/2005**,
  **Norin–Yuditsky 2016**, **Vlachos 2015**, **Mojarrad–Vlachos 2015** — the
  binomial-form upper-bound chain and its improvements.
- **Morris–Soltan 2000** survey, BAMS — canonical survey (§2 manuals the
  cups/caps, §3 the lower construction, §5 the extensions).
- **Balko–Valtr, A SAT attack on the ES conjecture** (ENDM 49 (2015) 425–431) —
  refutes the strengthened Peters–Szekeres conjecture (cES(7)>32, cES(8)>64);
  verifies the ES-equivalent ETV Conjecture 3.1 over pseudolinear colorings;
  the orientation-variable SAT encoding. `balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md`
  (eurocomb2015.w.uib.no PDF). **Answers requests `balko-valtr-attack-baa4` and
  `open-access-full-1e6e`.**
- **Heule–Scheucher 2024** (empty hexagon h(6)=30), **Subercaseaux et al. 2024**
  (Lean formalisation), **Scheucher** (higher-dim SAT), **Aichholzer et al. 2002**
  (order-type database ≤11), **Duque–Fabila-Monroy–Hidalgo-Toscano** (small-integer
  realization of the ES construction), **Károlyi–Tóth 2012** (forbidden-order-type
  restricted class), **Pór–Valtr 2002** (partitioned ES), **Bárány–Valtr**
  (positive-fraction ES), **Damásdi–Dong–Scheucher–Zeng 2024** (saturation),
  **Dumitru 2025** (ES(7) SAT, still open), **Koshelev–Koshka**, **PointSAT
  (Krapivin et al.)**, **SMQH (Subercaseaux et al. automated symmetries)**,
  **Dumitrescu**, **Horton 1983** (empty convex 7-gons, adjacent), **Felsner–Weil
  2001 + Bergold–Felsner–Scheucher** (signotopes/pseudoline arrangements),
  **Dobbins–Holmsen–Hubard**, **Moshkovitz–Shapira**, **Fox–Pach–Sudakov–Suk 2012**,
  **Goaoc–Welzl** (random order types), plus the **Lean/Mathlib** formalisation
  records and **Wikipedia/MathWorld** encyclopedic tiers.

## Everything-cited-is-in-the-library check (this audit's core)

Every claim in the claims ledger carries an `anchor:` pointing at a file on disk;
the grep for every `anchor` resolved to a real file. The MIS-DOWNLOAD quarantine
files each have a `correct` sibling. No claim is stranded on recall.

## Requests — all answered by full texts on disk

The three rows in `derived/REQUESTS.md` (`balko-valtr-attack-baa4`,
`open-access-full-1e6e`, `full-text-faithful-b96b`) carry `answers:` claim blocks
in the held summaries but still **render open** in the derived file. That is a
re-derivation-state artifact, not a library gap — the primary content backing
each is held. A future run should not re-open them; if it needs REQUESTS.md to
agree, the claims ledger entries with `answers:` are authoritative.

## Attempted this cycle, plus the definitive record of two not-held items

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder"** (EJC 17(6):519–532, DOI
  10.1006/eujc.1996.0045) — the canonical primary of the ETV enumeration
  conjecture N(a,u,k)=ΣC(k-2,i-2) equivalent to ES. **Confirmed unobtainable in
  open access**: ScienceDirect 403; SZTAKI repository holds metadata only; the
  FU-Berlin `tr-b-93-01` is a different 1993 single-author Valtr precursor, not
  this paper. Its content is faithfully restated in the held Baek (arXiv:2206.04260,
  Thm 1.5, proves P(n,4,n)) and Balko–Valtr. Recorded as documented-but-not-held;
  do not re-search. (Stored in Cognee.)
- **Bonnice 1974** (AMM) and **Kalbfleisch–Kalbfleisch–Stanton 1970** — the
  primary ES(5)=9 proofs are paywalled; the full proof outline is in the held
  Morris–Soltan survey (Theorem 2.7/2.8 classification of 9-point no-pentagon
  sets). Documented-but-not-held, sufficient fidelity second-hand.
- **Pach–Solymosi k-convex chapter** (DOI 10.1007/978-3-030-25005-8_4) — held
  only as a MIS-DOWNLOAD stub; it is a drift-guarded adjacent problem, and the
  IWOCA-2019 version of the same content is held. Not worth a Springer paywall.

## Where the library stands against the run's needs

- **ROOT.md** meets GOAL.md criterion 1: every upper bound with its error term
  and source, the lower-bound construction written concretely, ES(3..6) with the
  method that settled each (Peters–Szekeres n=6 computation with its encoding and
  ~1500 CPU-hour cost), and multiple restricted classes / partial results
  (Tóth–Valtr class, decomposable/split Baek–Balko, forbidden-order-type
  Károlyi–Tóth, saturation Damásdi et al., 9-point no-pentagon classification).
- **Oracle foundation**: the 4-point criterion primary, the exact-arithmetic
  checklist, and the ES construction primary are all held.
- **Lean/formalisation arm**: Mathlib `erdos_szekeres` confirmed to be the
  monotone-subsequence theorem (name collision, NOT the convex-polygon ES), so
  the planar statement must be written from scratch; the LeanPool CapCup.lean
  and Subercaseaux ITP are held as models.
- **SAT arm**: Balko–Valtr, Scheucher, Dumitru, SMQH, PointSAT, Koshelev–Koshka
  all held — the full modern landscape of orientation-variable encoders.

Net: the library is complete at the fidelity this run requires; further
acquisition happens only against a new stated gap in `research/REQUESTS.md`.
