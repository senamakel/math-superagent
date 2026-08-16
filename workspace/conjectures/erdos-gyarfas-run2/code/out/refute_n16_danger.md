# Refuter: corroborating the n≤16 rung against its sharpest danger case

Refuter's own computation (this run, not a source). See `code/refute/refute_report.md`
for the full reduction reasoning and file map.

```claim
id: refute-heawood-petersen-8cycle
statement: The Heawood graph (smallest cubic girth-6 graph, n=14, the (3,6)-cage) contains a simple 8-cycle 0-L0-1-L5-6-L3-4-L4-0 (points 0,1,6,4; lines L0,L5,L3,L4 of the Fano incidence L_i={i,i+1,i+3}); and the Petersen graph (n=10, girth 5) contains an 8-cycle, the latter confirmed independently by find_counterexample returning "proved" against the pinned graph.
hypotheses: Heawood/Petersen as constructed in code/refute/heawood_n16.py
holds-here: yes
status: checked
bearing: These are the two sharpest danger cages for the asserted-settled rung R-delta3-n16-three-targets (every delta>=3 graph on <=16 vertices has a 4/8/16-cycle): girth>=5 kills C4, n<=16 kills C16, so the rung for a girth>=5 graph hinges wholly on the 8-cycle. Both cages contain an 8-cycle, so the Heawood/Petersen cases do not refute the rung. The n<=16 lane survives this attack.
anchor: code/refute/refute_report.md
```

## What the searches returned (verbatim, not upgraded)

- `find_counterexample` on pinned-Heawood 8-cycle: **undecided**.
- `find_counterexample` on n=12 and n=16 delta>=3 counterexample model searches:
  **undecided** (solver cannot decide 12–16-vertex graph existence in budget).
- `find_counterexample` on pinned-Petersen 8-cycle: **proved** (from the axioms
  written: symmetric, irreflexive, exact Petersen edge set; conjecture: an
  8-cycle exists). This corroborates the oracle's Petersen verdict by a second,
  independent mechanism.

## The honest bottom line

Neither rung is refuted, and neither is independently re-derived here:

- The two rungs are marked "settled" in `research/WEAKENED.md` on the strength
  of Balaji's 2026 preprint (`balaji-sms-32`: every delta>=3 graph on <=31
  vertices has a C4/C8/C16). That source is flagged in the run's own claims
  ledger as **asserted, preprint under review, no formal proof certificate**,
  and the run's oracle has not reproduced even its n<=16 baseline (task
  `verify-2conn-class-oracle` is open; prior output `g_heart_verify_n8.out` is
  corrupt).
- So "settled" is stronger than the machine evidence the run currently holds.
- The single genuinely open danger that would refute the n≤16 rung: a
  **non-regular** min-degree-3 graph of girth 6 on 15 or 16 vertices with no
  8-cycle and no 16-cycle. Balaji's search covered it; this run has not
  independently decided it.
