# Pattern-finder report — round 14

## What changed since round 13

Since round 13 the run produced one genuinely new unmined artifact: the
**explicit 2-(22,4,2) design** `code/out/coclique_lift_design.txt`, found by the
Q1 MILP (HiGHS, 66s) that the steering directive targets. It is the confluence
of the two 99-specific levers (coclique bound 22 + the equality-forced
2-(22,4,2) design), so it is the correct place to look for structure. I analysed
it exactly (second-route re-derivation + defect anatomy). The sequence tools
confirm the standing catalogue is genuinely exhausted; no new algebraic sequence
exists to extract. This round's value is a precise, exact account of the
super-simple defect of the one known 2-(22,4,2) design.

## Finding 1 — the Q1 design is a valid 2-(22,4,2), re-derived by a second route (CHECKED)

Re-derived from `coclique_lift_design.txt` independently of the MILP: 77
distinct 4-blocks on 22 points, every point in exactly 14 blocks, every pair
of points in exactly 2 blocks. `assert` on both histograms passes. So the
design the steering directive named exists and is exactly `2-(22,4,2)`,
`b=77, r=14, λ=2`— matching the equality-force `d_C=4, r=14, b=77` of report 12.

## Finding 2 — the super-simple defect is exactly 6 triples in 2 blocks, concentrated on point 18 (CHECKED, exact)

A super-simple completion (Q2) requires no triple lying in two blocks (no two
blocks meeting in 3 points). Exact count over all C(22,3) triples:

```
triple-occurrence histogram (count -> #triples): {1: 296, 2: 6}
  block-pair overlap histogram: {0:1149, 1:1558, 2:213, 3:6}
bad triples (in >=2 blocks, = direct mu=2 violations): 6
  (6,17,20), (2,4,18), (3,18,21), (10,15,18), (8,12,16), (14,18,20)
bad-triple point concentration: 18->4, 20->2, all other points ->1 each
```

So **point 18 is a hub: it participates in 4 of the 6 bad triples**. The 6
triples each lie in exactly 2 blocks (histogram `2:6`), so the defect is
sparse — but not a clean matching: the "movable extra" vertex is reused
(8, 16, 19 each appear as the differing vertex in 2 different bad pairs),
and the bad triples `{2,4},{3,21},{10,15},{14,20}` are exactly the
co-18-triples. Every bad triple is **isolated** (only its 2 owner blocks
contain ≥2 of its points), so the violations do not cascade through shared
block content.

**Status:** these are exact integer facts about THIS design (not about the
existence of any 99-graph, and not a claim about any other 2-(22,4,2) design).
They are computed here, not sourced. They give the concrete obstruction the
super-simple Q2 line must remove: the coupling of the movable vertices
(8,16,19) and the point-18 hub means a local per-pair repair is not trivially
independent — which is consistent with the Q2 MILP timing out rather than
finding a clean design, but a timeout is not a proof.

## Finding 3 — the sequence catalogue is confirmed exhausted (re-affirmed)

I ran `analyze_sequence` / `find_linear_recurrence` on the two remaining
unmined families and they show no structure beyond the standing catalogue:

- n3-radius survivor trajectory `[1,2,5,11,19,19,19]`: no low-degree
  polynomial, no order-≤4 constant-coefficient linear recurrence (round 8
  already said this; re-confirmed). The plateau at 19 is the radius-6 stable
  fixpoint, not a polynomial limit.
- The 2-(22,4,2) defect histogram is a finite structural fact, not a sequence.

Nothing since round 13 has added a sequence-bearing artifact. The full
catalogue stands (13 rounds): every parameter-determined family count is the
same `a=2u+1 | 63` quartic, none separates 99, and the only 99-specific
quantities remain the **coclique bound 22** and **forced n3≥3**.

## Hand-off / recommendation

The super-simple Q2 question (does a 2-(22,4,2) design with no two blocks
meeting in 3 points exist?) is exactly the steering directive's open item, and
it is a **design-existence** question — sat_solver's job, not the sequence
tools'. This round contributes the precise anatomy of the one known design's
defect (the 6 triples, the point-18 hub, the coupled movable vertices
8/16/19, and the isolation of each bad triple) so that any repair/search has a
concrete starting object. Whether a super-simple 2-(22,4,2) exists may be
settled in the design-theory literature (Gronau–Mullin carry super-simple
(v,4,2) existence spectra); I did not search it — that was already flagged as
a research gap.

## Files

- `code/out/pf_supersimple_design_structure.py` / `_summary.py` — validity re-derivation + defect histograms (exact).
- `code/out/pf_supersimple_probe.py` — bad-pair anatomy.
- `code/out/pf_point18_probe.py` — point-18 hub analysis.
- `code/out/pf_supersimple_isolation.py` — isolation + coupling of the defect.
- This report.
