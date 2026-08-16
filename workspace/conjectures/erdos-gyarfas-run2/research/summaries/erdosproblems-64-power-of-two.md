# Erdős Problem #64 (Bloom) — canonical status record

Source: https://www.erdosproblems.com/64 (T. Bloom). Full text held in this
summary; [[erdosproblems-64-power-of-two]].

## What it records

- Open problem (falsifiable: could be disproved by a finite counterexample),
  $1000 prize per this page's header (Bloom lists $1000; Erdős's original
  $100/$50 as cited in Wikipedia/Markström).
- **Erdős and Gyárfás's own belief was negative:** they conjectured the
  answer is negative, and in fact for every r there is a δ ≥ r graph with no
  2-power cycle (k ≥ 2).
- **That belief is disproved** by Liu & Montgomery [LiMo20]: an absolute
  minimum-/average-degree threshold forces a 2-power cycle.
- **Infinite graph falsity:** an infinite tree with minimum degree 3 has no
  2-power cycle. So finiteness is essential (conjecture is for finite graphs).
- Confirmed for various families (comment by Alfaiz lists them).
- Formalised statement link to google-deepmind/formal-conjectures 64.lean.

## For this problem

Confirms the statement (k ≥ 2), the finiteness hypothesis, the falsity for
infinite graphs, and the historical framing. The "Erdős–Gyárfás believed
false" fact is historically important but mathematically mooted by
Liu–Montgomery; it does not change the δ ≥ 3 question.

```claim
id: erdosproblems-statement
statement: The conjecture (finite simple, δ ≥ 3, some 2^k-cycle with k ≥ 2) is open; false for infinite graphs; Erdős–Gyárfás's negative belief is refuted by Liu–Montgomery.
hypotheses: finite simple δ ≥ 3
holds-here: yes
status: sourced (Bloom's editorial status; belief-refutation sourced to LiMo20)
bearing: fixes the exact statement, finiteness hypothesis, and open status
anchor: research/sources/wikipedia-erdos-gyarfas-conjecture.full.md
```
