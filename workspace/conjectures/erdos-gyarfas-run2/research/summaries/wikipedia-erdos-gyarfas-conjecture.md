# Wikipedia — Erdős–Gyárfás conjecture

Source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture. Full text held; [[wikipedia-erdos-gyarfas-conjecture.full]].

## What it records

- Statement (1995), $100 proof / $50 counterexample.
- Computer-search bounds: any counterexample **≥ 17 vertices** (Royle and
  Markström); any **cubic** counterexample **≥ 30 vertices** (Markström).
- Markström's four 24-vertex graphs in which the only power-of-two cycles
  have length 16; one of the four is planar.
- 3-connected cubic planar case is settled (Heckman–Krakovski 2013).
- **The conjecture remains open for bipartite cubic graphs** (a distinct
  restricted class; relevant to gap in requests.md on whether bipartite cubic
  is open).

## For this problem

Wikipedia's 17/30 wording vs Markström's primary "<16 all checked"/"<29
cubic all checked": the "≥17" and "≥30" headers count "at least n vertices"
while the primary searches checked fewer. Both are now superseded upward by
Balaji's 32. The "open for bipartite cubic" line is the one open restricted
class flagged for verification (requests.md).

```claim
id: wp-bounds
statement: Computer search (Royle, Markström) gives any counterexample ≥ 17 vertices and any cubic counterexample ≥ 30 vertices; superseded by Balaji's 32.
hypotheses: finite simple δ ≥ 3 (resp. cubic)
holds-here: yes (historical; superseded)
status: sourced (Wikipedia)
bearing: the oracle anchor chain; "≥32" is the current best
anchor: research/sources/wikipedia-erdos-gyarfas-conjecture.full.md
```

```claim
id: wp-bipartite-cubic-open
statement: The conjecture remains open for bipartite cubic graphs.
hypotheses: bipartite cubic
holds-here: candidate restricted class for attack; status needs primary confirmation (see requests)
status: asserted (Wikipedia)
bearing: a natural target class for a structural attack (cubic + bipartite)
anchor: research/sources/wikipedia-erdos-gyarfas-conjecture.full.md
```
