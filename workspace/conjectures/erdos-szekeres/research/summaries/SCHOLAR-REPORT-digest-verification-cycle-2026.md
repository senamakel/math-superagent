# Scholar report — digestion/verification cycle (post-research-agent)

What this pass read, verified against full texts, and concluded, and what the run
still lacks. This cycle assumed the research agent had just finished and the
library had "new material". Finding: **the three newest sources (Dumitru Dec 2025,
Koshelev–Koshka Apr 2026, PointSAT Jul 2026) were already digested with claim
blocks by prior scholar cycles; this cycle re-verified those digests against the
full texts and tightened the three owning notes.** No undigested source remains
except the encyclopedic pointer tier, which is deliberately not claim-bearing.

## What was verified verbatim against the full texts this cycle

1. **Dumitru, arXiv:2512.24061** (`sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`).
   Re-derives every number from the paper body: 5456 triple vars + 572,880 4-set
   selectors = 578,336 vars; 16,670,808 clauses (9,493,440 reduced 5-point CC +
   2,905,320 4-set consistency + 4,272,048 no-convex-7-set × 280); 14 realizable
   4-set patterns, 6 convex; Proposition 1 = the run's own `es35-four-criterion`;
   UNSAT only for anchored subfamilies; heavy-tailed runtimes (2.5e3–2.28e6 s);
   ES(7)=33 OPEN. Matches `dumitru-es7` (asserted).

2. **Koshelev–Koshka, arXiv:2604.20120** (full HTML text on disk). Theorem:
   h(6,≥2)=17, h(6,1)=18 (line 121 of the HTML full text); linear-subreduction
   method §5.2 (fix abscissae → LIA); signotope 4-tuple one-sign-change axiom
   §4.2. Matches `kk-linear-subreduction`, `kk-h61-h62`, `kk-adjacent-not-esz7`.

3. **Krapivin–Przybocki–Heule PointSAT, arXiv:2607.02958**. Theorem 1.1 (line 31):
   largest set with no 6-hole or 7-gon has 23 points → h(6,7)=24. 32-point no-7-gon
   run (lines 295–299): 2191 core-hrs, 200,000 abstract solutions, zero realizable;
   mean 121.6 violations vs ≤38, flippable-orientation fraction 0.9% vs ≥1.2%.
   Matches `kph-h67-24`, `kph-32-no7gon-no-realizable-found`, `kph-flippability-method`.

4. **Baek–Balko SoCG 2025 full-text digest** — re-read and cross-checked against
   the claim ledger. State: `baek-balko-split` proved-in-source (Lemma 10/11);
   `baek-balko-decomposable` **asserted-by-source** ("The proof of Theorem 8 is
   omitted" in SoCG, JCTA 2026 pending); `baek-balko-weak7-fails` proved;
   `baek-balko-signotope-analogue-open`; `baek-balko-blowup-new-constructions`.
   **Recall check: durable memory carries the same asserted-by-source label.** No
   contradiction with recalled memory on any claim.

## What was tightened (all three new-source owning notes rewritten, claims verbatim)

- `research/summaries/dumitru-notes-on-33-point-esz-arxiv2512.24061.md` (was a 3-line
  pointer into the consolidated SAT note; now the owning note with verified numbers
  and `[[dumitru-notes-on-33-point-esz-arxiv2512.24061.full]]` wikilink).
- `research/summaries/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120.md`.
- `research/summaries/krapivin-przybocki-heule - ... PointSAT.md`.

Each under a thousand tokens, carries one claim block per statement, and wikilinks
its full text. Re-derivation ran clean (claims/threads/backward/weakened/blueprint/
entailment re-rendered).

## Sources that do not help (and why)

- **Encyclopedic tier** (Wikipedia, MathWorld, erdosproblems, OEIS): no mathematics
  the primaries do not establish more reliably; pointers and drift-guards only.
  OEIS A000051 (2^n+1) is catalogued, not a proof — the sequence IS the conjecture.
- **MIS-DOWNLOAD stubs** (7 files): wrong physics papers fetched from guessed
  arXiv IDs; each flagged DO NOT CITE with a redirect to its genuine sibling.
  Never cite. Their summaries are redirects, not digests.
- **Adjacent-problem sources** (empty hexagon, higher-dim SAT, k-convex, big-line,
  Horton empty-side): correctly marked `holds-here: no` or drift-guarded. None
  bears on ES(n)=2^{n-2}+1. They are context and SAT-machinery templates only.
- **cfhmsv big-line-big-convex** (`cfhmsv-big-line-big-convex`): asymptotic
  2^{n+C√(n log n)}-type; recorded for completeness, not a tool for the exact constant.

## Gaps and stale state found (not fixed — owner roles flagged)

1. **`evenodd-cutfamily-which-family-realizes` is DONE but the tasks ledger still
   shows `open`.** The capture exists (`code/out/evenodd_cutfamily.captured.txt`,
   EXIT 0): the even/odd bipartition at n=7 IS realizable as a triple open
   half-plane intersection (min k=3, exactly one witness triple per half;
   k=1, k=2 controls fail as required). **Owner (goals/director): close the row.**
2. **CONTEXT.md Established still says "Baek–Balko split/decomposable ... proved
   (SoCG 2025)".** The claim ledger and durable memory both say decomposable =
   asserted-by-source ("proof of Theorem 8 omitted"). **Owner (curator): correct
   the line** — anything resting on decomposable-as-proved rests on an unverified
   source claim. (Flagged by the prior verification cycle too; still unfixed.)
3. **`horton_verify.py` was never run.** `code/out/horton_verify.captured.txt`
   does not exist; the scholar→coder handoff sits unexecuted. The two `horton-*`
   claims are `proved` from the source argument only, not machine-checked, and
   INDEX.md still says "needs coder to run". **This is the one concrete
   verification the run owes the Horton digest.**
4. **Recalled `derived/REQUESTS.md` rows for the three answered requests still
   render open** (balko-valtr-attack-baa4, open-access-full-1e6e, full-text-
   faithful-b96b) despite `answers:` blocks on disk — a re-derivation-state quirk
   flagged repeatedly; requests-ledger owner should confirm closure.

## Contradictions

None between any primary full text, its digest/claim block, and recalled memory.
The one earlier label slip (MV16 chain "TV 1998 +1") was inside a summary, not a
claim block, and was fixed by a prior cycle. The recalled `lib.es_geom.longest_cap`
DP bug does not invalidate any claim (checked: `g-cupcap-verified`, block-tightness,
layer-extremality use is_cup/is_cap/hull oracle, not whole-set longest_cap).

## Durable findings (memory server DOWN — 16 failures this cycle; stored on disk)

The memory server health check does not answer; findings below are written to
`research/summaries/SCHOLAR-REPORT-digest-verification-cycle-2026.md` as the
Cognee stand-in. A later pass with a healthy server should `remember_memory` each
of these:

- F1: Dumitru arXiv:2512.24061 verified encoding numbers (578,336 vars / 16,670,808
  clauses); UNSAT only for anchored subfamilies; ES(7)=33 open; 4-set criterion =
  run's es35-four-criterion.
- F2: PointSAT h(6,7)=24 (adjacent); 32-point no-7-gon: 200,000 abstracts, zero
  realizable (evidence, not proof); consistent with SMQH + Dumitru.
- F3: Koshelev–Koshka h(6,≥2)=17, h(6,1)=18; linear subreduction (fix abscissae →
  LIA) is the run's SMT realizability route.
- F4: Baek–Balko decomposable stays asserted-by-source; CONTEXT.md line is stale.

## What the run still lacks

- ES(7)=33: open. Every current attack (SMQH, PointSAT, Dumitru, Koshelev–Koshka)
  stops at evidence; the abstract signotope analogue (`baek-balko-signotope-
  analogue-open`) is the right well-posed target for the SAT arm after it
  reproduces ES(5)=9 / ES(6)=17.
- The Horton machine check (item 3 above).
- Cognee promotion of F1–F4 once the memory server recovers.