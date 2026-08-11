<!-- source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture | converted from HTML -->

# Erdős–Gyárfás conjecture — statement, prizes, and the computational verification bound

Secondary source (Wikipedia), useful chiefly for the **computational verification bound** and prize framing. The conjecture is stated as: every graph with minimum degree 3 contains a simple cycle whose length is a power of two. Made 1995; Erdős offered $100 for a proof, $50 for a counterexample.

## The computational verification bound (the quantity Phase 3 of TASKS.md must anchor)

- **Any counterexample has at least 17 vertices** (computer searches of Gordon Royle and Klas Markström).
- **Any cubic counterexample has at least 30 vertices**.
- Markström's searches found **four graphs on 24 vertices** in which the only power-of-2 cycles have length 16. **One of these four is planar**.
- Nonetheless the conjecture is now **known true for 3-connected cubic planar graphs** (Heckman & Krakovski 2013) — so the planar 24-vertex near-counterexample is not 3-connected.
- The conjecture remains open for bipartite graphs (statement cut off — re-open full text if needed).

```claim
id: eg-counterexample-bound
statement: Any counterexample to EG has at least 17 vertices, and any cubic counterexample has at least 30 vertices.
hypotheses: a graph with min degree >= 3 and no 2-power cycle (counterexample); cubic variant
holds-here: yes
status: verified-computationally (Royle, Markström), per secondary source
bearing: sets the lower bound the oracle must reproduce; exhaustive enumeration below ~17-30 vertices is settled, so Phase 3's count only extends past this
anchor: research/L0.0/wikipedia-erdos-gyarfas.full.md
```

```claim
id: eg-markstrom-24
statement: Markström's exhaustive search found four min-degree-3 graphs on 24 vertices whose only 2-power cycle has length 16; one of the four is planar.
hypotheses: 24 vertices, min degree >= 3
holds-here: yes
status: verified-computationally (exhaustive search), per secondary source
bearing: these are the closest known to counterexamples; each still has a 2-power cycle (16). The planar one shows planarity alone is not enough — consistent with 3-connectedness being needed for the Heckman–Krakovski theorem
anchor: research/L0.0/wikipedia-erdos-gyarfas.full.md
```
