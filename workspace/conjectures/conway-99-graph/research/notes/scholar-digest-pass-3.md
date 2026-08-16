# Scholar digest pass 3 — verify the newest sources, close computed-result gaps

This pass (third scholar pass) verified the two newest load-bearing sources
against their full texts, confirmed the primary-source chain for the n3 pivot,
and closed the two biggest gaps in the ledger: computed results that existed on
disk but had no claim blocks, so never reached CLAIMS.md or the run's durable
memory.

## Added this pass (computed results promoted to the ledger)

1. **`n3-99-forced-at-least-3`** (`code/out/n3-screening-claims.md`).
   Combining the order-6 integrality residue (n3 ≡ 0 mod 3) with the
   sourced+re-derived Makhnev conditional (n3 ≥ 1 at (99,14,1,2)), a putative
   99-graph must have **n3 ≥ 3, n3 ≡ 0 (mod 3)**. The admissible set at
   (99,14) is exactly the 1387 multiples of 3 in [0, 4158],
   cap = v·k·(k−2)/4 = 4158 (4158 admissible, 4159 not — sharp). This is a
   **sharpening** of the recorded n3≥1, and a CONSTRAINT, not a nonexistence
   proof (the n3≥3 case remains open). Recorded as entailed by
   `order6-n3-not-forced` + `makhnev99-shorter-proof-integrality`.

2. **`pentagon-count-closed-form-verified`** (`code/out/pentagon-count-verified.md`).
   The induced-C5 count closed form p5 = n·k·(k−2)·(k−4)/5 is now **checked**
   on both controls (rook = 0, BvLS = 384,912), promoted from asserted. At 99
   it forces exactly 33,264 induced pentagons — a hard isomorph-rejection
   target, but parameter-determined and surviving unchanged on the controls, so
   a dead end as a nonexistence lever.

Both were stored to durable memory (Cognee writes landed; recall returns 404 per
prior passes, an infra limitation not a content loss).

## Verified against full texts this pass

- **Shpectorov–Zhao (85,14,3,2) template** — Theorem 1.1 "There is no srg(85,14,3,2)"
  and the 478-segment enumeration confirmed verbatim at lines 50, 72, 447, 1289
  of the full text. The closest successful local-enumeration precedent for 99
  (same k=14, μ=2, λ=3; the 99 local graph 7K2 gives a smaller analogue space).
- **Makhnev 1988 condition (*)** — verified verbatim in the Russian full text
  (lines 51-52, 55-62): (*) = "any pair of triangles joined by at least two
  edges is joined by exactly three edges" = this run's **n3 = 0**; Thm 1 (μ≤3 or
  (27,10,1,5)); Thm 2 "no srg(99,14,1,2) or srg(115,18,1,3) satisfying (*)".
  Lines 182-232 confirm the forced Λ₀ = srg(33,12,1,6) subgraph under (*) at
  (99,14,1,2). This validates the whole n3≥1/≥3 chain.
- **Phillips 2026 Thm 4.5** — the three graphs whose triangle graph is strongly
  regular, and the s=−k/2 or k=6 criterion, confirmed at lines 1956-1975/1622.
  The triangle-graph-not-SRG constraint is shared by 99 and 243 (both fail the
  criterion), so it is a constraint, not a rule-out.

## Contradictions checked

- The Bagchi "μ=2 ⇒ grid or k≥48" apparent contradiction of BvLS's existence is
  **already resolved** in the ledger (`bagchi-bvls-contradiction-resolved`) and
  closed — the second branch k<(λ+1)(λ+2)=6 is not met by 22 or 14. No new
  contradiction found this pass.
- No source in the library contradicts the n3 pivot: Makhnev (n3=0 ⇒ no 99),
  Reimbayev (hexagon count, order-6 counts in n3), and the measured n3=0 on both
  controls are mutually consistent and cross-checked.

## Sources that do not help (unchanged, confirmed)

- `makhnev-2013-local-subgraphs-srg-99` (paywalled, body absent — useful only as
  a marker).
- `brouwer-haemers-srg-chapter` (paywalled preview).
- `zehavi-oliveira` (solvable variant, not the problem).
- `keramatipour-sat` (no boundary value; confirms enumeration is wrong method).
- `bagchi-mu2-correct` (wrong download — Gichev Lie algebra paper; the correct
  Bagchi content is in the dichotomy-resolution note).

## What the run still lacks

- Whether n3 ≥ 3 (or the whole n3≥1 case) is even consistent with a global
  closure at 99 — the seed extends locally to every radius (solution.md §6), so
  the obstruction, if any, is global.
- Whether Aut is trivial, and the exact orbit structure of the small candidate
  groups (a hypothetical Z₂ or Z₇).
- A k=14-specific argument in the 84/140/5 outer partial Steiner triple system,
  or a 22-coclique → 2-(22,K,2) design contradiction (the coclique bound 22 is
  the cleanest parameter-specific number; not refuted on arrival by the controls
  with bounds 3 and 45).
