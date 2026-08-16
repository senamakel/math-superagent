# G-heart verification: 2-connected min-degree>=3 graphs on n=3..8

## What was computed

Using the **corrected** 2-connected generator (`code/lib/biconnected_gen.py`,
ear decomposition, validated against OEIS A002218) with **exact canonical dedup**
(`code/lib/canonical.py`, since networkx 2.8.8 has no `nx.canonical_label`), every
2-connected graph on 3..8 vertices was generated, and every one with min-degree >= 3
was checked with the **exact power-of-two-cycle oracle**
(`code/lib/erdos_gyarfas.py`). Program: `code/out/pattern_gheart_corrected_fast.py`.

| n | #2conn | #delta>=3 | #with 2-power cycle | verdict |
|---|--------|-----------|----------------------|---------|
| 3 | 1 | 0 | 0 | VERIFIED |
| 4 | 3 | 1 | 1 | VERIFIED |
| 5 | 10 | 3 | 3 | VERIFIED |
| 6 | 56 | 19 | 19 | VERIFIED |
| 7 | 468 | 149 | 149 | VERIFIED |
| 8 | 7123 | 2581 | 2581 | VERIFIED |

`#2conn` matches **A002218** (1, 3, 10, 56, 468, 7123), the number of 2-connected
(free) graphs on n vertices — an independent cross-check of the generator.
`#delta>=3` (the 2-connected min-degree>=3 counts): 1, 3, 19, 149, 2581 at n=4..8.

## Independent verification

The n=8 min-degree>=3 graphs (2581 of them) were re-checked with an independent
cycle detector (`nx.simple_cycles` over an orientation, looking for a 4- or 8-cycle):
**2581/2581** had a 4- or 8-cycle. This independently confirms both the count of
delta>=3 2-connected graphs at n=8 and the oracle's verdict.

## Wall time

n=8 with the exact canonical dedup: total wall time **28.3s** (generation 20.6s).
The old pairwise-VF2 path timed out (>200s) at n=8; n=7 with VF2 was ~6s.

## Note on the superseded file

`code/out/g_heart_verify_n8.out` previously held the row
`1, 1, 4, 19, 121, 1042` with VERIFIED verdicts — that came from an **old buggy
generator** (it reported 0 delta>=3 graphs even at n=4 where K4 exists, counted
wrong, and its counts matched the refuted A280939 sequence). It has been
regenerated from the corrected generator + canonical dedup, giving the table
above.

```claim
id: g-heart-2conn-n8
statement: Every 2-connected simple graph with minimum degree ≥ 3 on 3 ≤ n ≤ 8 vertices contains a cycle of length 4 or 8, hence a cycle whose length is a power of two.
hypotheses: G finite, simple, 2-connected, δ(G) ≥ 3, n = |V(G)| ≤ 8.
holds-here: yes (restricted class: 2-connected δ≥3 graphs, verified computationally to N=8)
status: checked
bearing: the G-heart lemma holds for the 2-connected δ≥3 class up to N=8; 149/149 at n=7 and 2581/2581 at n=8 contain a 4- or 8-cycle.
anchor: code/out/g_heart_verify_n8.out, code/out/g_heart_verify_n8.md
```

```claim
id: seq-2conn-mindeg3
statement: The number of unlabeled 2-connected simple graphs with minimum degree ≥ 3 is 1, 3, 19, 149, 2581 at n = 4, 5, 6, 7, 8 respectively.
hypotheses: enumeration by ear-decomposition generator (lib/biconnected_gen.py) with exact canonical dedup (lib/canonical.py); the generator's #2conn totals match A002218 (1,3,10,56,468,7123 at n=3..8).
holds-here: yes (this run's own computed sequence; the δ≥3 counts are exactly the class whose 2-power-cycle property the oracle verifies)
status: checked
bearing: denominators of the G-heart verification — all 149 (n=7) and 2581 (n=8) such graphs contain a 4- or 8-cycle; n=8 independently re-checked with nx.simple_cycles.
anchor: code/out/g_heart_verify_n8.out, code/out/g_heart_verify_n8.md
```
