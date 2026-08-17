# Pattern-finder report — round 34: H1 sequence re-verified; sequence line unchanged

## What this round did

Surveyed the workspace for artifacts newer than round 33's captures
(`homology_controls_final.captured.txt`, 12:54, the latest result file). Only
prose postdates it: `derived/BLUEPRINT.md`, `derived/BACKWARD.md`,
`research/backward/n3-positive-global.md` — none carries new computed terms.

The one sequence that round 33 introduced — the clique-complex H1 family
`[4, 364, 1540, 227920, 163190944]` — was re-verified this round with the
exact tools and against its closed form.

## Re-verification (exact)

Closed form (round 33, proven for every connected λ=1 SRG via λ=1 ⇒
edge-disjoint triangles ⇒ rk(δ₂) = T):

    dim H1(Cl(G)) = 2T − v + 1 = vk/3 − v + 1

| u | v | k | H1 = vk/3 − v + 1 | checked |
|---|---|---|---|---|
| 1 | 9 | 4 | 4 | ✓ (rook(3) computed) |
| 3 | 99 | 14 | 364 | ✓ by formula |
| 4 | 243 | 22 | 1540 | ✓ (BvLS computed) |
| 10 | 6273 | 112 | 227920 | ✓ by formula |
| 31 | 494019 | 994 | 163190944 | ✓ by formula |

Tool verdicts on `[4, 364, 1540, 227920, 163190944]`:
- `analyze_sequence`: level-1 diffs [360, 1176, 226380, 162963024] — never
  constant, not a low-degree polynomial; every term ≡ 0 (mod 4); mod-2 period 1.
- `find_linear_recurrence` (order ≤ 4): none — the divisor-63 sparse-index
  signature, same as every other family sequence.
- `oeis_lookup`: **no match** — already recorded in
  `research/notes/clique-complex-h1-closed-form.md` ("do not search again");
  this round's lookup is a re-hit, not a new miss.

Derived trivial consequence (not a new sequence): β₂ = 0 identically, from
χ = v − E + T and β₂ − β₁ = χ − 1 with β₁ = 2T − v + 1:
β₂ = (χ − 1) + β₁ = (v − vk/2 + vk/6 − 1) + (vk/3 − v + 1) = 0. Parameter-
determined, holds identically at both controls, no separating power.

## Verdict

Standing verdict unchanged through 34 rounds: **every family sequence on disk is
divisor-63-governed and parameter-determined; none separates srg(99,14,1,2)
from its controls rook(3) and BvLS(243).** The only 99-specific structural
values remain the coclique bound 22 and forced n₃ ≥ 3 (Makhnev conditional) —
individual values, not extendable sequences. NOTHING FURTHER from the sequence
tools; the live front is the 84-vertex H encoder / budget ledger (open tasks,
directives 39/43), which are construction questions, not sequence questions.

## Files
- this report
- `research/notes/clique-complex-h1-closed-form.md` (claim, proof, OEIS miss)
- `code/out/pattern_finder_report33.md` (round 33)