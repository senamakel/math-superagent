# Elder–Lafrenière–McNicholas–Striker–Welch, "Homomesies on permutations" (arXiv:2206.13409)

Source: https://arxiv.org/abs/2206.13409 (abs page). Journal: Mathematics of Computation 93 (2024) 921–976, DOI 10.1090/mcom/3866. Full text not captured (arXiv abs page carries abstract only); the PDF is at https://arxiv.org/pdf/2206.13409.

## What the paper establishes

128 instances of the **homomesy** phenomenon: a statistic X on S_n is homomesic under a map φ if the average of X is the **same on every φ-orbit**. Maps surveyed: **Lehmer-code rotation** (a cyclic shift of the Lehmer/factoradic digits), reverse, complement, Foata bijection, Kreweras complement. Statistics include inversions, descents, permutation-pattern counts.

Key structural fact for permutation orbits:
- **Lehmer-code rotation map**: every orbit has the same size, **lcm(1,2,...,n)** (Theorem 4.8), and many inversion-linked statistics (45 in FindStat) are homomesic under it (Theorem 4.7). Homomesy ⇒ the orbit average equals the global average.

## Why it matters for this run

Our open core is summing the Levi/Lehmer rank over the cyclic subgroup {π^i} — an average of a permutation statistic over the orbits of a power action. Homomesy is exactly the phenomenon that would make such an orbit-average equal the global average, collapsing the whole sum. Two caveats keep it a route, not the solution:
1. The map here is **Lehmer-code rotation**, not the permutation-power map π → π^k / cyclic group {π^i}; those are different actions on S_n.
2. homomesy of **rank** (a heavy factoradic-weighted sum) is not among the listed homomesic statistics; only individual inversion-related statistics are shown homomesic under rotation.

So this note supplies the **conceptual framework and test** (is our rank-sum homomesic under some natural map?) rather than a formula. It is a sibling of [[cambie_yan_html]] (averages of statistics over powers) and the L2 fold [[../../L2/rank_lehmer]] (Lehmer/factoradic machinery) — none of which covers the cyclic subgroup {π^i} directly.
