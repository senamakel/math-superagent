# Scholar report — readback of the reference library against the goal, tasks, and beliefs

What this pass read, verified, and concluded, and what the run still lacks.

## Frame

The research agent finished and the library had "new material". I read the full
`research/LIBRARY_LEDGER.md`, the canon of summaries, the approach adjudications, and
the live claims/threads/requests ledgers against this investigation's goal (ES(n)=2^{n-2}+1,
upper bound open), its current tasks (gsplit provenance re-capture; es-nogon scored search),
and its established beliefs (CONTEXT.md, durable memory). The verdict below: **everything
genuinely new is already digested with claim blocks by prior scholar cycles; the contribution
this pass can make is (a) confirming the digest layer is complete and internally consistent,
(b) resolving one status discrepancy, and (c) filing the durable findings prior cycles left
"awaiting Cognee" — here, on disk, because the memory server is down.**

## Sources new in the last few cycles — all already digested, with claim blocks

- **Dumitru arXiv:2512.24061** (Dec 2025) — the live ES(7) frontier. Digest + claim
  `dumitru-es7` (asserted): 578,336 vars / 16,670,808 clauses; UNSAT only for anchored
  convex-layer subfamilies; ES(7)=33 OPEN. Owner note: `summaries/dumitru-notes-on-33-point-esz-arxiv2512.24061.md`.
- **Koshelev–Koshka arXiv:2604.20120** (Apr 2026) — claims `kk-linear-subreduction`,
  `kk-h61-h62` (h(6,≥2)=17, h(6,1)=18), `kk-adjacent-not-esz7`. Full HTML on disk.
- **PointSAT arXiv:2607.02958** (Jul 2026) — claims `kph-h67-24`, `kph-32-no7gon-no-realizable-found`,
  `kph-flippability-method`. 32-point no-7-gon: 200,000 abstract solutions, zero realizable
  (evidence, not proof).
- **Baek–Balko SoCG 2025** full PDF — claims `baek-balko-split` (proved: Lemma 10/11),
  `baek-balko-decomposable` (asserted: "proof of Theorem 8 omitted"), `baek-balko-weak7-fails`,
  `baek-balko-signotope-analogue-open`, `baek-balko-blowup-new-constructions`.
- **Baek ETV arXiv:2206.04260** — `baek-ETV-n4n` (P(n,4,n), first new ETV case since 1935),
  `etv-alpha-statistic-injective`, `baek-interweaved-laced-cups`, `etv-equivalent-to-es`.
- **Horton 1983** primary — `horton-no-empty-7gon`, `horton-s-k-construction` (empty-side
  analogue; held in context, out of Established).
- **ETV Ramsey-remainder** (Valtr B 93-01 abstract) — `etv-rr-definition`,
  `etv-rr-es-conditional`, `etv-rr-offdiagonal` (asserted, abstract-level; full text paywalled).

## Approach adjudications (research specialist's newest deliverable) — all recorded

The three newest candidate lines were taken to the literature and closed on evidence, each
with `status` + `killed-by` in `research/approaches/<slug>.md` and in the approaches ledger:

- `convex-geometry-order-dimension` — **refuted as a reduction** (dim≥n ⟹ convex n-gon is the
  conjecture in new language; Beagley's bounds are one-sided).
- `vc-sauer-shelah-convex-family` — **refuted** on a fatal parameter mismatch (2^{n-2} is the
  Sauer–Shelah cap over a ground set of size n−2, but N=2^{n-2} is the cardinality estimated).
- `etv-grid-simplex-compression` — **refuted**: the full α-injectivity host T_{n,n} = C(2n-4,n-2)
  ≈ 4^n/√n, not 2^{n-2}; the loss is intrinsic, not a truncation artifact.
- `antimatroid-mobius-beta-bound` — **refuted**: β-invariant computes #interior exactly, never
  bounds it (identity, not inequality). Legitimate as a realization-invariant marker only.
- `convexity-complex-fvector` — **refuted**: Kruskal–Katona bounds shadow from below, never N
  from above; bound must come from anti-exchange structure = conjecture restated.
- `radon-circuit-no-radon-4set` — **refuted** (rank-3: every 4-subset is a circuit; the circuit
  hypergraph is the complete 4-uniform hypergraph, carries no convexity info).
- `halfplane-separator-depth` — **grounded** as a reformulation of the split/decomposable result.
- `same-type-tverberg-wedge-split` — **adopted** (radial-fan IS the ES construction's structure).
- `order-dimension-realization-invariant` — **adopted** (Beagley's theorem as a marker).

All closed reasons are on disk; none proposes again what was closed. **These are more valuable
kept as refutations than as routes: an abstract separator (line, wedge, order dimension, VC,
lattice) does not bound N by 2^{n-2} unless it is the conjecture restated, and every
decisive `killed-by` is a computational or literature fact, not a mood.**

## Adjudication of the apparent "Baek–Balko proved" belief — RESOLVED

The rendered `derived/CLAIMS.md` index row in this prompt showed `baek-balko-decomposable`
as `proved` and `baek-balko-split` as `proved`. Reading the claims ledger in full (108 rows):
- `baek-balko-split` has TWO rows: the ROOT.md row is the old asserted-by-source form; the
  SoCG-PDF-digest row carrying the exact formula ESsplit(a,u,k)=1+Σ C(k-2,i-2) is **proved**
  (Lemma 10/11 complete in the held text).
- `baek-balko-decomposable` is **asserted** in the ledger ("Theorem 8 ... proof omitted"; JCTA
  2026 paywalled).

So the corrected status the prior verification cycles pushed is **already on disk in the
ledger**; the `proved` rendering was the stale-summary artifact, not the operating record.
Recall check: durable memory agrees (three separate notes mark decomposable asserted-by-source).
**No contradiction with recalled memory; the earlier flag "CONTEXT.md said proved" still stands
as a CONTEXT curation item, not a library error — the library is right.**

## Contradictions

None between any primary full text, its digest/claim block, and recalled memory. The one
earlier label slip (MV16-chain "TV 1998 +1") was inside a summary, fixed in a prior cycle.
`lib.es_geom.longest_cap` DP bug does not invalidate any claim (verified: load-bearing claims
use is_cup/is_cap + hull oracle).

## Sources that do not help, and why

- **Encyclopedic tier** (Wikipedia, MathWorld, erdosproblems, OEIS): no mathematics the
  primaries do not establish more reliably; pointers/drift-guards only. OEIS A000051 (2^n+1) is
  catalogued, not a proof.
- **MIS-DOWNLOAD stubs** (7 files): wrong physics papers; each flagged DO NOT CITE with a
  redirect to its genuine sibling. Never cite.
- **Adjacent-problem sources** (empty hexagon, higher-dim SAT, k-convex, big-line-big-convex,
  Horton empty-side, PointSAT h(6,7), Koshelev–Koshka h-values): `holds-here: no` or
  drift-guarded. None bears on ES(n)=2^{n-2}+1. They are context and SAT-machinery templates.
- **Cardinal–Santos**, **Hoffmann–Merckx** (allowable-sequence realizability ∃ℝ-complete),
  **SLMath/GP allowable-sequence definition**: framework/vocabulary for the (now-closed)
  allowable-sequence thread; not tools for the exact constant.

## Durable findings — to promote to Cognee when the server recovers

The `remember_memory` server is DOWN (health check fails; 18 refused stores this run across
two cycles). Per the workspace convention (tool-permission fallback), the verified,
source-backed findings intended for durable memory are written here instead, for a later pass
with a healthy server to `remember_memory` verbatim:

- **D1 (Tóth–Valtr chain, corrected labels):** 1998 = ES(n) ≤ C(2n-5,n-2)+2 (Thm 5); 2005
  combined = C(2n-5,n-2)+1 for n≥5 (Thm 1). Binomial symmetry makes n-2/n-3 phrasings equal.
  MV16 ≈ 7/16·C(2n-4,n-2). Suk = 2^{n+6n^{2/3}log n} (n≥n0). All asymptotic; none bears on the
  exact constant. Verified against held full texts.
- **D2 (Dumitru):** verified encoding numbers (578,336 vars / 16,670,808 clauses); UNSAT only
  for anchored subfamilies; ES(7)=33 open; 4-set criterion = es35-four-criterion.
- **D3 (PointSAT):** h(6,7)=24 adjacent; 32-point no-7-gon: 200,000 abstracts, zero realizable.
- **D4 (Koshelev–Koshka):** h(6,≥2)=17, h(6,1)=18; linear subreduction (fix abscissae → LIA) is
  the run's SMT realizability route.
- **D5 (Baek–Balko):** decomposable stays asserted-by-source; split proved-in-source via
  Lemma 10/11; CONTEXT.md "proved (SoCG 2025)" line is stale.
- **D6 (Baek ETV):** P(n,4,n) proved (full proof in held text); α-statistic injectivity and
  interweaved-laced-cups proved; etv-equivalent-to-es asserted.
- **D7 (Horton):** empty-side analogue; g(n) nonexistent for n≥7; machine check (`code/out/
  horton_verify.py`) still pending execution.

To store each when the server recovers, e.g.:
```
remember_memory { text: "D1 ...", source: "scholar readback cycle; research/summaries/SCHOLAR-REPORT-readback-digestion-cycle.md" }
```

## What the run still lacks (unchanged)

- **ES(7)=33**: open. Every current attack (Dumitru, PointSAT, SMQH, Koshelev–Koshka) stops at
  evidence; the abstract signotope analogue (`baek-balko-signotope-analogue-open`) is the right
  well-posed SAT-arm target after it reproduces ES(5)=9 / ES(6)=17.
- **The queued provenance re-capture** (task `gsplit-enumeration-recheck`, steer 11): one
  command, must reproduce 4/2/0 splits at n=5/6/7 before the split counts are promoted to
  checked. This is run-side, not a library gap.
- **Horton machine check** (`code/out/horton_verify.py` → captured output).
- Three answered `requests` rows still render open in `derived/REQUESTS.md` (a re-derivation
  quirk; content is on disk with `answers:` blocks).
- **Cognee promotion of D1–D7** once the memory server recovers.
