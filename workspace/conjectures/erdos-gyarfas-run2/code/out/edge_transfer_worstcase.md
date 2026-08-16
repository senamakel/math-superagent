# Edge-transfer worst case: chord-deletion induction up to n = 8

## What was checked

On the committed 2-connected δ≥3 class (generated only via
`lib.biconnected_gen_hash`, **no ad-hoc regeneration**), for every graph, every
deletable chord e = ab (i.e. G−e 2-connected and δ(G−e) ≥ 2, the Lemma-A chords)
was tested for the **good** property:

> C(G−e) contains a power of two (4, 8, 16, …)  **OR**  G−e has a simple a–b
> path of length 2^k − 1 (3, 7, 15, …).

A graph with no good deletable chord is the **worst case**: the single
chord-deletion step (research/approaches/edge-deletion-2adic-transfer.md) cannot
close on it, which is exactly the place the induction stops.

## Result: no worst case exists up to n = 8

| n | δ≥3 2-connected graphs | worst cases |
|---|---|---|
| 3 | 0 | – |
| 4 | 1 | 0 |
| 5 | 3 | 0 |
| 6 | 19 | 0 |
| 7 | 149 | 0 |
| 8 | 2581 | 0 |
| **total** | **2753** | **0** |

**The smallest n where a worst case exists does not occur in the range 3–8.**
Every one of the 2753 graphs has at least one good deletable chord.

## Why this is expected, and the independent check

Structural fact used and cross-checked: if G has a power-of-two cycle of length
2^k, then **every** deletable chord of G is good — a 2^k-cycle either avoids e
(it then lies in G−e), or passes through e (cycle minus e is an a–b path in G−e
of length 2^k − 1). So a bad graph is exactly a graph with **no** power-of-two
cycle at all.

By the Moore bound, a cubic/delta≥3 graph needs ≥ 10 vertices (the Petersen
graph, the smallest girth-5 3-regular graph) to reach girth 5. Every δ≥3 graph
on ≤ 8 vertices therefore has girth ≤ 4 and hence a 4-cycle — a power of two.
That makes every graph trivially good.

Independent numerical confirmation of this route: girth measured directly
(BFS shortest cycle) over the whole class —

| n | max girth over δ≥3 graphs |
|---|---|
| 4, 5 | 3 |
| 6, 7, 8 | 4 |

Max girth is ≤ 4 throughout, so every graph contains a 4-cycle. The per-chord
scan and the girth route agree with **zero mismatches** (the script also checks
that per-chord "good" status never disagrees with "G has a power-of-two cycle").

## What this means

The two load-bearing lemmas of the adopted approach hold throughout the verified
range:

- **Lemma A** (every 2-connected δ≥3 graph has a deletable chord with G−e
  2-connected and δ(G−e)≥2): PASS on all 2753 graphs.
- **Lemma B** (C(G) = C(G−e) ∪ {|P|+1 : P an a–b path in G−e}): PASS — it is
  tautological for every edge (a cycle of G either avoids e or is an a–b path
  plus e), and was mechanically confirmed by the oracle on every graph's chosen
  chord.

And the induction's first rung closes everywhere: **no graph up to n=8 is the
worst case.** The earliest candidate for the genuinely hard content must live at
n ≥ 10 (girth-5 graphs without a power-of-two cycle, above the Moore-bound
floor), consistent with the known standing obstruction (ROOT §1) and the Balaji
verification bound.

## Command

```
python code/out/verify_edge_deletion_lemmas.py      # ~39s, both lemmas PASS
python code/out/edge_transfer_worstcase.py          # ~40s, 0 worst cases, n<=8
```

Both run the committed generator; neither regenerates the class ad hoc.
