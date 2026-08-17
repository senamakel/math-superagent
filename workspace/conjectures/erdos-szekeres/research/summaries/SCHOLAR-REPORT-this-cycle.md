# Scholar report — this cycle's read of the reference library

Frame: the research agent finished and the library has "new material". I read the
library ledger, the canon of summaries, the claims/threads/requests ledgers, and
the current CONTEXT/tasks against the goal (ES(n)=2^{n-2}+1, upper bound open).

## Verdict up front

**Everything genuinely new is already digested.** The librarian's frontier
acquisitions this cycle and last — Horton 1983 (primary), Dumitru arXiv:2512.24061,
Koshelev–Koshka arXiv:2604.20120, PointSAT arXiv:2607.02958, Baek–Balko SoCG 2025
full PDF, Baek ETV, Balko–Valtr ENDM 2015 full text — were all read against their
full texts and given claim blocks by prior scholar cycles. No placeholder or
undigested substantive source remains. The encyclopedic tier is catalogued context
only. My contribution this cycle is confirmation + one persisted status check +
recording that the durable-finding promotion to Cognee is blocked.

## What each genuinely-new source establishes (confirmed verbatim against full texts)

- **Horton 1983** (`sources/horton-1983-...pdf.full.md`): S_k={(i,d(i))}, d(i)=Σ a_j c^{j-1},
  c=2^k+1, has no *empty* convex 7-gon → g(n) nonexistent for n≥7; g(5)=10 (Harborth),
  g(6) open. Claims `horton-no-empty-7gon`, `horton-s-k-construction` (proved by source
  argument). **Empty-side analogue of the ES 1961 construction; kept OUT of Established** per
  GOAL's adjacent-problem drift guard. Machine check `code/out/horton_verify.py` still
  NOT executed (coder-owned) — claims are `proved-by-source`, not yet `checked`.
- **Dumitru arXiv:2512.24061** (live ES(7) frontier): 578,336 vars / 16,670,808 clauses;
  UNSAT only for anchored convex-layer subfamilies; ES(7)=33 OPEN. `dumitru-es7` (asserted).
- **Koshelev–Koshka arXiv:2604.20120**: h(6,≥2)=17, h(6,1)=18; linear subreduction
  (§5.2: fix abscissae → LIA) is the run's SMT-realizability route. Adjacent, not ES(7).
- **PointSAT arXiv:2607.02958**: h(6,7)=24; 32-point no-7-gon run: 200,000 abstract
  solutions, zero realizable (evidence, not proof). Adjacent.
- **Baek–Balko SoCG 2025**: split k-gon threshold 2^{n-2}+1 PROVED (Lemma 10/11);
  decomposable-set Theorem 8 is **asserted-by-source** ("proof omitted"; JCTA 2026 =
  the one genuine acquisition gap). Matches durable memory; not a contradiction.
- **Balko–Valtr ENDM 2015**: refutes the strengthened Peters–Szekeres conjecture
  (cES(7)>32, cES(8)>64) but ALL counterexamples are NON-pseudolinear, so they never
  touch the geometric ES conjecture; verifies the ES-equivalent Conjecture 3.1 over
  pseudolinear colorings at a=4,u=k=7 (N=16) and a=4,u=k=8 (N=22). Answers requests
  `balko-valtr-attack-baa4`, `open-access-full-1e6e`.

## Sources that do NOT help (and why)

- **Encyclopedic tier** (Wikipedia, MathWorld, erdosproblems, OEIS): no mathematics the
  primaries do not establish more reliably; pointers and drift-guards only. OEIS A000051
  (2^n+1) IS the conjecture, catalogued not proven.
- **MIS-DOWNLOAD stubs** (7 files): wrong physics papers fetched from guessed arXiv IDs;
  each flagged DO NOT CITE with a redirect to its genuine sibling.
- **Adjacent-problem sources** (empty hexagon h(6)=30, higher-dim SAT, k-convex,
  big-line-big-convex cfhmsv, Horton empty-side, PointSAT h(6,7), Koshelev–Koshka
  h-values): `holds-here: no` or drift-guarded. None bears on ES(n)=2^{n-2}+1.
- **Cardinal–Santos, Hoffmann–Merckx, SLMath/Goodman–Pollack** allowable-sequence
  material: framework/vocabulary for the (now-closed) allowable-sequence thread, not tools
  for the exact constant.

## Contradictions

None between any primary full text, its digest/claim block, and recalled memory. The one
label slip (MV16-chain "TV 1998 +1") was inside a summary (fixed) and never in a claim
block. `lib.es_geom.longest_cap` DP bug does not invalidate any claim (load-bearing claims
use is_cup/is_cap + hull oracle, not whole-set longest_cap).

## Persisted status discrepancy (this cycle)

The two `horton-*` claim blocks are recorded in the digest note
`research/summaries/horton-1983-sets-with-no-empty-convex-7-gons.pdf.md` and in durable
memory, but they do NOT render in `derived/CLAIMS.md` (a `read_ledger query: "horton"`
returns nothing; the ledger holds 109 entries). This looks like a re-derivation/extraction
state quirk for these blocks, not a missing source — same class as the three answered
REQUEST rows that still render open. Owners holding the claims ledger should confirm the
`horton-*` blocks extract into `derived/CLAIMS.md`.

## Durable findings — Cognee promotion BLOCKED (server down)

`remember_memory` failed 20× this run (health check not answering; would accept and drop).
Per the workspace convention, the verified source-backed findings intended for durable
memory are preserved **on disk** here for a later pass with a healthy server to store
verbatim. They are D1–D7 of the prior readback cycle plus this cycle's confirmation; the
full text is in `research/summaries/SCHOLAR-REPORT-readback-digestion-cycle.md` and above.

## What the run still lacks (unchanged; run-side, not library)

- ES(7)=33: open; every attack (SMQH, PointSAT, Dumitru, Koshelev–Koshka) stops at
  evidence; the abstract signotope analogue (`baek-balko-signotope-analogue-open`) is the
  well-posed SAT-arm target after the encoder reproduces ES(5)=9 / ES(6)=17.
- The gsplit Phase-2 provenance re-capture (task `gsplit-enumeration-recheck`, steer 11).
- The Horton machine check (`code/out/horton_verify.py` → `horton_verify.captured.txt`).
- Cognee promotion of the durable findings F1–F7 / D1–D7 once the memory server recovers.
