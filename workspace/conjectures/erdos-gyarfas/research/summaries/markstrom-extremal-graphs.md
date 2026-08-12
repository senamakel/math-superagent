> Note — replaces the abstract-only digest. Full text: [[markstrom-extremal-graphs.full]] (K. Markström, "Extremal graphs for some problems on cycles in graphs", Congressus Numerantium 171 (2004) 177–188). Only §4 bears on Erdős–Gyárfás (§2–3, §5 are unrelated cycle-count / non-Hamiltonian work).

## §4 — the structural dichotomy (source Carr credits)
If $G$ is an edge- and vertex-minimal counterexample and $d(u)\ge3,d(v)\ge3$ then $uv\notin E(G)$ (else $G-\{u,v\}$ is a smaller counterexample). So a counterexample splits into an independent set $V_1$ of degree-$\ge4$ vertices plus a nonempty $V_2=V\setminus V_1$ of degree-3 vertices. (Proved argument.)

## §4 — the computational verification (the run's key oracle figure, primary source)
- **Royle** (`makeg`, modified for the degree structure + no $C_4$) generated *all relevant graphs on fewer than 16 vertices* — no counterexample.
- **Markström** ($V_1=\emptyset$, cubic; `minibaum`) generated *all cubic graphs on fewer than 29 vertices*, checked for $C_4,C_8,C_{16}$ — **no counterexample**.
- **On 24 vertices** the *smallest* cubic graphs with no $C_4$ and no $C_8$ were found: four of them (Table 3: $24\to4$, also $26\to23$, $28\to251$), all containing a $C_{16}$; exactly one is planar = the **Markström graph** (built from $K_4$ by vertex-into-triangle expansion).

**Bearing / precision.** These are the *primary* sources behind the consolidated "$\ge17$ total / $\ge30$ cubic" figures: Royle raw $n\le15$ (general), Markström raw $n\le29$ (cubic). Table 3 records exact counts of $C_4,C_8$-free cubic graphs. The obstruction lives at length 16 for 24 vertices — a would-be counterexample needs no $C_4,C_8,C_{16}$ simultaneously.

## Does NOT settle
General case $n\ge30$; mixed ($V_1\neq\emptyset$) case past $n=15$; nothing beyond degree dichotomy + 4/8/16 cycle checks. The $C_{16}$-presence at 24 vertices is computed, not proved.

## Status
Dichotomy proved; 15/29/24/4-graph/one-planar figures computed-and-checked (exhaustive generation) — primary, not hearsay (closes ROOT's exact-citation gap).

```claim
id: EG-markstrom-dichotomy
statement: A minimal counterexample G splits into an independent set V1 of degree≥4 vertices and a nonempty set V2 of degree-3 vertices.
hypotheses: G finite simple, δ≥3, no power-of-two cycle, minimal in order then size.
holds-here: yes
status: proved (Markström §4: no edge between two ≥3-degree vertices)
bearing: backbone every search and Carr's 4/7 bound build on
anchor: research/summaries/markstrom-extremal-graphs.md
```

```claim
id: EG-verification-bound
statement: No counterexample exists on n≤15 vertices generally and no cubic counterexample on n≤29 vertices; smallest C4,C8-free cubic graphs have 24 vertices.
hypotheses: finite simple δ≥3 graphs (cubic: all deg 3).
holds-here: yes
status: computed and checked (Royle makeg ≤15; Markström minibaum ≤29 cubic)
bearing: the run's oracle range; minimum size of any hypothetical counterexample
anchor: research/summaries/markstrom-extremal-graphs.md §4
```

```claim
id: EG-markstrom-24-graphs
statement: Exactly four cubic graphs on 24 vertices have no C4 and no C8, each containing a C16; exactly one is planar (the Markström graph).
hypotheses: cubic, 24 vertices, no C4, no C8.
holds-here: yes — near-miss family showing obstruction lives at length 16 for 24 vertices.
status: computed and checked (Markström §4)
bearing: a would-be counterexample needs no C4, C8, or C16 simultaneously
anchor: research/summaries/markstrom-extremal-graphs.md §4
```
