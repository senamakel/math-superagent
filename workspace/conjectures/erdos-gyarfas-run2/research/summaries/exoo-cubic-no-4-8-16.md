# Exoo — Graphs without cycles of specified lengths (near-miss data)

Source: G. Exoo, "Graphs Without Cycles of Specified Lengths",
http://isu.indstate.edu/ge/COMBIN/CYCLES/index.html. Full text held;
[[exoo-cubic-no-4-8-16]].

## The data (catalogue-level; these are constructed examples, not exhaustive unless stated)

Trivalent (=cubic) graphs avoiding various cycle-length sets, motivated by the
Erdős–Gyárfás conjecture:

- A smallest trivalent graph with no 4, 6, or 10-cycles.
- A trivalent graph of order 32 with no 4, 8, or 32-cycles.
- A smallest trivalent graph with no 4 or 8-cycles (3 others exist) — these
  are Markström's 24-vertex near-misses.
- The (unique) smallest trivalent graph with no 4 or 6-cycles.
- A smallest trivalent graph with no 4, 6, or 8-cycles.
- **The smallest graph Exoo knows with no 4, 8, or 16-cycles has 78 vertices.**
- **The smallest with no 4, 8, 16, or 32-cycles has 540 vertices.**

## What it implies here

Cubic graphs that avoid the short powers {4,8,16} (resp. {4,8,16,32}) are
*very* rare and appear only at large size (78, 540). This is sharp near-miss
data: a δ≥3 graph can avoid 4, 8, and 16 simultaneously only if it has ≥ 78
vertices (and to also avoid 32, ≥ 540). It directly extends the sense in which
the Balaji 32-vertex verification is near-optimal: avoiding the three smallest
2-powers pushes the order to 78. These are the extreme "delay the 2-power
lengths" examples a minimal counterexample would resemble.

```claim
id: exoo-short-2power-avoidance
statement: There exist cubic graphs avoiding C4,C8,C16 on 78 vertices and avoiding C4,C8,C16,C32 on 540 vertices; these are the smallest Exoo knows of.
hypotheses: cubic (trivalent), avoiding the stated cycle lengths
holds-here: yes — near-miss data for where a counterexample's short 2-powers must live
status: catalogued (constructed examples, not claimed exhaustive)
bearing: a counterexample would have to avoid 4,8,16 (n ≥ 78) and 32 (n ≥ 540); bounds the reach of any 'short 2-power' forcing argument
anchor: research/sources/exoo-cubic-no-4-8-16.full.md
contradicts: none (consistent with a large counterexample being possible at n ≥ 32)
```
