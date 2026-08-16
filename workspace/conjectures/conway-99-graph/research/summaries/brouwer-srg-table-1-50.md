# Brouwer's parameters of strongly regular graphs — table 1 ≤ v ≤ 50 (canonical reference)

<!-- source: https://aeb.win.tue.nl/graphs/srg/srgtab1-50.html -->
<!-- full text: research/sources/brouwer-srg-table-1-50.full.md -->

## The rook's-graph row (the (9,4,1,2) positive control)

```
! | 9 | 4 | 1 | 2 | 1 4 | -2 4 | Paley(9); 3^2; 2-graph*
```
- status **`!` = exists**, spectrum **1⁴, −2⁴** (k=4, so 1⁴·(−2)⁴; wait the
  entries are r^f, s^g = 1^4, −2^4 — the two non-k eigenvalues each with
  multiplicity 4). This matches the run's oracle: rook(3)=Paley(9)=the 3×3
  lattice graph is srg(9,4,1,2). The comment "3^2" notes it is a 3×3 grid
  (lattice), and "Paley(9)" / "2-graph*" the Seidel-2-graph framing.

This is the first positive control for every nonexistence argument (GOAL.md):
any argument against (99,14,1,2) must fail on this graph.

## Neighbouring λ=1 context in the table
- `! | 15 | 6 | 1 | 3 | 1 9 | -3 5 | O(5,2)... GQ(2,2)` — a λ=1, μ=3 srg.
- `! | 27 | 10 | 1 | 5 | 1 20 | -5 6 | O-(6,2) polar graph; GQ(2,4)` — λ=1,
  μ=5, exists; this is the (27,10,1,5) graph that appears in Makhnev 1988
  Theorem 1 as the exceptional non-μ≤3 member of a λ=1 SRG satisfying (*).
- Both confirm λ=1 μ≠2 members exist, so the λ=1 family is not empty of
  higher-μ structures; only μ=2 makes 99 hard.

## What it does not contain
The table stops at v≤50, so (99,14,1,2) itself is in the 51–100 table (see
research/summaries/brouwer-srg-table-51-100.md, row `? | 99 | 14 | 1 | 2 | 3 54 | -4 44`).

## Implication
The canonical citation for the rook's-graph positive control and its spectrum,
and for the existence of the λ=1 members (15,6,1,3), (27,10,1,5) that frame
the family.

```claim
id: brouwer-table-rook9-exists
statement: Brouwer's table marks srg(9,4,1,2) (Paley(9), the 3x3 rook's/lattice
  graph) with status '!' (exists), spectrum 1^4,-2^4. Also records the
  existing lambda=1 members (15,6,1,3) and (27,10,1,5) [the latter = Makhnev
  1988 Thm 1's exceptional case].
hypotheses: none — canonical reference table.
holds-here: yes — the first positive control.
status: catalogued (Brouwer's web table; rook(3) existence independently
  oracle-verified as srg(9,4,1,2)).
bearing: the citation for the (9,4,1,2) positive control; confirms the lambda=1
  family has existing higher-mu members.
anchor: research/sources/brouwer-srg-table-1-50.full.md
contradicts: none; confirms c4.
```

[[brouwer-srg-table-1-50.full]]
