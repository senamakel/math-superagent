# Scholar digest report — Erdős–Gyárfás library

**Role outcome:** The library was already mature and gap-driven on disk (37
full texts, ~50 digests, populated CLAIMS/threads/approaches). The genuine gap
I closed was that **none of the durable findings had been pushed to Cognee
(`recall_memory` returned nothing, and `relate_memory`'s graph store was
empty)**. I read the load-bearing sources against their full texts, verified
the arithmetic, flagged the contradictions, and recorded the durable findings
with `remember_memory` (13 notes stored). I also corrected two summary files
that carried raw placeholder text and flagged one mislabeled source.

## What I added to durable memory (all source-backed)

1. **The obstruction** (Bondy–Vince, Liu–Ma, Gao–Huo–Liu–Ma, Cui–Lo,
   Sudakov–Verstraëte, Liu–Montgomery, Montgomery survey): interval and
   congruence cycle-length results never force a prescribed sparse power of
   two; the two results that DO force a 2-power (S–V, Liu–Montgomery) run on
   average degree ≫ 3. δ≥3 is the gap.
2. **Minimal-counterexample degree structure** (Markström, Carr full proof):
   degree-≥4 vertices independent, every vertex adjacent to a degree-3 vertex,
   ≥4/7 vertices cubic, regular CE is cubic.
3. **The 2/3 degree-fraction derivation** (from a forum post, verified against
   Carr's lemmas; status derived/unchecked).
4. **Pirzada 2-power unicyclic construction** with correct closed form
   2^{i+6}−34 and its circular conclusion flagged.
5. **Bensmail near-misses** (only 2-power cycles length 4 or 8 at arbitrary
   cubic order).
6. **Heckman–Krakovski settled class + Exoo/Markström near-miss data**
   (G420 no-{4,8,16}; 78- and 540-vertex avoidances).
7. **Verification bounds** (Royle 17, Markström cubic 29, Balaji general 32,
   Balaji certified bipartite-cubic 60).
8. **Claw-free / Caro's weakening** (2^k-or-3·2^k; 114-vertex cubic claw-free
   bound; power-of-2 claw-free still open; Caro integer-power rung).
9. **Degree-3-critical spine** (EFGS baseline Ω(log n), NPS no-23-cycle
   refutation, Combinatorica Ω(log n) distinct lengths) — with the caution
   that 3-criticality alone does not force a 2-power.
10. **Other settled classes** (P8/P10/P13-free, diameter-2, Cayley 2p²/4p).
11. **Status caveats** (Gebendorfer preprint contradictory + open, infinite
    graphs falsity, Lean sorry, prize).
12. **Adjacent frameworks** (minimal-unavoidable sets; Rautenbach Kraft
    bound).
13. **The validated oracle** (code/lib/erdos_gyarfas.py).
14. **The live thread + three proposed approaches.**

## Independent checks I performed

- **Pirzada orders (by hand against full text):** closed form |G_i| =
  2^{i+6}−34 reproduces 94, 222, 478; printed recurrence is a typo; unique
  2-power length 2^{i+4} sound.
- **Oracle** (`oracle_validation.out`): all ground truths PASS; cycle counts
  agree with an independent enumerator; edge-set keying bug found and fixed.
- **Carr full proof:** the 4/7 and degree-structure claims are proved in the
  held text (not merely abstract-asserted).

## Contradictions surfaced (the most valuable output)

- **Gebendorfer 2026** central dichotomy ("δ≥3 forces C4 or C8") is FALSE,
  contradicted by Markström 24-vertex, Exoo 78/540, Exoo G420 — all held.
- **Pirzada Conclusion** circular (invokes the conjecture). Cite construction
  only.
- **Pirzada printed recurrence** contradits its own orders (typo).

## Sources that do not help (recorded so nobody re-reads them)

- **OEIS A280939** — no connection to the problem; noted not helpful.
- **Exoo image-only subpages** (G24a/G24b/N46/N4610/N468/N4832) — image data,
  substantively the index page already held.
- **Verstraëte 2016 survey body** — paywalled, bibliography only.
- **Cayley classes** — settled but weak structural transfer.

## What the run still lacks

- **research/ROOT.md EXISTS** (created this cycle by the librarian) and meets
  GOAL criterion 1: §2 states the structure of a minimal counterexample
  (Markström independent-set structure, Carr 4/7 + verified >2/3
  strengthening, degree-3-critical frame), §4 gives the verification bound
  (Royle 17, Markström cubic 29/30, Exoo 78/540 constructions, Balaji
  general 32/bipartite-cubic 60, run's own ≤16-vertex level), and §3 lists the
  settled classes with exact hypotheses. Phase 1's exit test is met; further
  gathering is gap-driven.
- **No independent check of the 2/3 degree-fraction** (derived, not
  Lean-formalised).
- **Balaji 32-vertex bound asserted** with no certificate; the oracle should
  reproduce n≤16/n≤19 first.
- **The live SAT question** (a δ≥3, n≥32 graph with independent degree-≥4 set,
  all others degree 3, no C4/C8/C16) is the concrete next step — UNSAT would
  be a genuine structural theorem.
