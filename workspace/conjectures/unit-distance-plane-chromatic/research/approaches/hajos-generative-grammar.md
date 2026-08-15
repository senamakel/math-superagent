# Hajós construction as a generative grammar for 5-critical unit-distance graphs

```approach
idea: Replace the continuum search over point sets with a discrete generative
  grammar: by the Hajós construction theorem every k-critical graph is obtained
  from K_k by repeated Hajós joins (and vertex identifications), so every
  5-chromatic unit-distance graph contains a 5-critical subgraph that is a leaf
  of the Hajós tree rooted at K_5. The search becomes "walk the Hajós tree,
  and at each node ask the geometric-realizability oracle whether that abstract
  graph embeds as a unit-distance graph."
mechanism: This is a change of representation from *point sets* to *abstract
  graphs with a build certificate*. The Hajós theorem (Hajós 1961; every graph
  of chromatic number >= k contains a k-critical subgraph obtainable from K_k by
  Hajós joins and identifications) is a theorem about abstract graphs, so the
  generative side is pure finite combinatorics; the geometry is pushed entirely
  into a single well-defined query — is a given abstract graph a unit-distance
  graph in R^2? That query is a rank-2 rigidity/realizability question solvable
  by exact algebraic (Groebner/cad) means, exactly the arithmetic the run
  already owns. The known dead-end to beat — "Minkowski sums and spindling
  accumulate rigidity but do not force the pair" — is a *particular* family of
  build operations; Hajós is the *complete* grammar for chromatic-critical
  graphs, so it is the natural superset in which a 5-critical UDG, if it exists,
  is guaranteed to appear.
status: refuted
precedent:
  - Hajós 1961, "Über eine Konstruktion nicht n-färbbarer Graphen" — every
    k-chromatic graph contains a k-constructible subgraph (merge + vertex id).
    Statement correct; lib claim `k-critical-minimum-degree`
    (research/sources/colour-critical-hajos-construction.md) records it.
  - Urquhart 1976: every k-chromatic graph is t-constructible for all 3<=t<=k
    (Ore merge). Reachable, but see killed-by.
  - Jensen–Royle 1999 (J. Graph Theory 30:37), https://doi.org/10.1002/(sici)1097-0118(199901)30:1
    — NOT every k-critical graph (k>=4) is constructible through a sequence of
    k-critical graphs; the final construction step may break criticality. So the
    "walk the Hajós tree keeping criticality" framing is false in general.
  - "Products of unit distance graphs" (Discrete Math 2009),
    https://www.sciencedirect.com/science/article/pii/S0012365X09005949 — the
    join operation does NOT preserve unit-distance realizability (most wheels,
    being joins K_1+..., are not UD in the plane; only W_7 is). The Hajós merge
    is a join-like operation, so the merge step does not keep graphs UD.
  - Wikipedia "Hajós construction": the construction does not guarantee
    preserving unit-distance realizability — the UDP is a separate geometric
    constraint not inherited by these graph operations.
  - Schaefer, "Realizability of graphs and linkages"
    (https://ovid.cs.depaul.edu/documents/realizability.pdf): unit-distance
    graph realizability (even all-unit-edge length) is ∃R-complete (Mnëv
    universality). So the "per-node realizability oracle" is not a well-defined
    cheap query; it is as hard as the original continuum problem.
killed-by: unit-distance-realizability-is-ER-complete + hajos-merge-not-UDP-preserving
```

## Literature verdict

The **named mathematics is correct and is already half of the record**: the
Moser spindle — the 4-critical calibration object — *is itself* one Hajós merge
of two copies of K4 (the Wikipedia treatment makes this explicit: "the result
of applying the Hajós construction [to two K4's] is the Moser spindle"). So the
4-critical generative step is genuinely realized in the run's own construction.

But the approach's two load-bearing operational claims fail on evidence:

1. **The Hajós merge does not preserve unit-distance realizability.** The
   discrete-graph theory is about abstract graphs; the merge (delete two edges,
   identify two vertices, add a new edge) has no reason to keep all edges at
   length 1 in a common embedding. The join operation is shown in "Products of
   unit distance graphs" (Discrete Math 2009) *not* to preserve the UDP, and the
   Hajós merge is join-like. So walking the tree and pruning by realizability
   prunes essentially everything — the realized leaves are the rare survivors,
   exactly the graphs the ordinary construction engine already finds.

2. **The per-node oracle is ∃R-complete, not a "well-defined" cheap query.**
   Schaefer shows unit-distance realizability of an abstract graph is
   ∃R-complete (Mnëv universality — these systems can encode arbitrary
   semi-algebraic conditions and require transcendental/non-rational
   coordinates). This is *harder*, not easier, than the original point-set
   search. The proposal's premise — "the geometry is pushed entirely into one
   well-defined query" — is the whole difficulty in disguise.

3. **Jensen–Royle 1999** show the "complete superset while staying critical"
   framing is false: for k >= 4 there are k-critical graphs not constructible
   through a sequence of k-critical graphs.

**What it would still buy:** the Moser-spindle reconstruction (a merge of two
K4's) confirms the run's calibration object is a genuine Hajós leaf — a useful
cross-check, already available. But as a *search* the grammar replaces one hard
problem (find a 5-chromatic point set) with a harder one (∃R-complete
realizability at every node of a tree whose operations do not preserve the
property). Closed as refuted; the constructive engine (Minkowski sums,
spindling) remains the only route that keeps coordinates exact through the
operations.
