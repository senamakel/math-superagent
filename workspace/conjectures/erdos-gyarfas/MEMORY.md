# MEMORY — what this run establishes about Erdős–Gyárfás

Each row: the belief, its evidence class (proved / verified-numerically /
conjectured / asserted-by-source), and what would falsify it. Provenance lives
in `research/ROOT.md`, `research/CLAIMS.md`, and the source digests.

## Minimal counterexample structure

| Belief | Class | Evidence | Falsified by |
| --- | --- | --- | --- |
| A minimal counterexample G splits into an independent set V1 of degree-≥4 vertices and a nonempty V2 of degree-3 vertices (degree dichotomy). | proved | Markström §4 edge-minimality: no edge between two ≥3-degree vertices, else G−{u,v} is a smaller counterexample. | A δ≥3 power-of-two-free graph G minimal in order,size with an edge between two degree-≥3 vertices. |
| Every regular minimal counterexample is cubic. | proved | Immediate from the dichotomy. | A regular δ≥3 power-of-two-free minimal graph with degree 4+. |
| Every vertex of a minimal counterexample is adjacent to a degree-3 vertex (cubic vertices dominate). | proved | Carr arXiv:2605.22844, abstract. | A minimal counterexample with a vertex all of whose neighbours have degree ≥4. |
| At least 4/7 of the vertices of any minimal counterexample have degree exactly 3. | proved | Carr, abstract. | A minimal counterexample with fewer than 4/7 of vertices degree-3. |
| Every proper subgraph H ⊊ G of a minimal counterexample has δ(H) ≤ 2. | proved | Carr Lemma 0.1: else H is a smaller counterexample. | A proper δ≥3 power-of-two-free subgraph of a counterexample. |

## Restricted classes already settled (sourced, not this run's)

| Belief | Class | Evidence | Falsify |
| --- | --- | --- | --- |
| 3-connected cubic planar graphs satisfy the conjecture. | proved | Heckman–Krakovski, EJC 20(2)#P7 2013 (discharging, partly computer). | a 3-connected cubic planar graph with no power-of-two cycle. |
| P13-free δ≥3 graphs satisfy the conjecture (and P12-free ⇒ has a C4 or C8). | proved, computer-assisted | Hegde–Sandeep–Shashank arXiv:2410.22842 (subsumes P8-free Gao–Shan, P10-free Hu–Shen). | a P13-free δ≥3 graph with no power-of-two cycle. |
| Diameter-2 δ≥3 graphs have a C4 or C8. | proved | Carr arXiv:2508.19302. | a diameter-2 δ≥3 graph with neither. |
| K1,m-free graphs with δ≥m+1 or Δ≥2m−1; planar claw-free. | proved | Shauger 1998; Daniel–Shauger 2001. | a counterexample in-class. |

## Computational verification (oracle)

| Belief | Class | Evidence | Falsify |
| --- | --- | --- | --- |
| The cycle oracle (all-simple-cycles enumeration) is correct. | verified-numerically | K4 {3,4}, K3,3 {4,6}, cube {4,6,8}, Petersen {5,6,8,9}; two independent implementations (oracle DFS + nx.simple_cycles) agree on all four, and on the Markström graph. | a graph for which the two routes disagree. |
| No counterexample on n≤15 (general) / no cubic counterexample on n≤29 (cubic); consolidated as ≥17/≥30. | asserted-by-source, machine-corroborated at low end | Royle makeg n≤15; Markström minibaum n≤29 cubic. This run re-verified no cubic graph on n≤16 avoids both C4 and C8. | a machine-checked counterexample below the bound. |
| The Markström graph (planar cubic 24-vtx) has no C4, no C8, but a C16; spectrum {3,5,6,7,9..24}. | verified-numerically, this run | graph6 Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D = HoG 51419; TWO independent routes (oracle DFS + nx brute), byte-for-byte identical across tool_builder and librarian. Integrality/cubic/planar/3-conn all checked. | a re-check finding a C4 or C8. Curiously absent: neither route sees length 4 or 8. |

## Run-owned findings (this run's contributions)

| Finding | Class | Evidence | Falsify / status |
| --- | --- | --- | --- |
| Base step of K4 → triangle expansion yields the triangular prism, cycle set {3,4,5,6} (a C4 present). | verified-numerically | `code/eg/k4_expansion_base.py`. | re-check on a different expansion bijection (none differ up to iso). |
| *Open:* the naive K4-triangle-expansion heuristic "a C4 once created is never destroyed" is FALSE (expanding a vertex on a C4 changes that cycle's length). | proved (reasoning) | expanding a vertex v on a 4-cycle v-a-b-c-v replaces v; the walk around the triangle changes by ±1/±2, so the C4 need not survive. | a concrete family where every C4-endpoints avoid later expansions — plausible in planar cubic graphs, which is exactly what the census (agent-run-12) probes. |
| *Open:* does any member of the K4-triangle-expansion family at n=24 avoid C4 and C8 (i.e. is Markström's construction remark literal)? | conjectured (to be tested) | census agent-run-12 running. | census result. |

## Failed / closed directions (each with its obstruction)

- **Cycle-basis-only length check.** A cycle basis spans the cycle space but its
  *lengths* can miss non-basic cycles. Oracle must enumerate all simple cycles.
  (`code/lib/cycle_oracle.py` docstring.)
- **Exhaustive full-size search is out of scope.** The stated bounds (n→31 or
  more) defeat enumeration; only small-instance brute force is the oracle, never
  the method. (Method policy.)
- **Naive "C4/C8 never destroyed" pruning** would incorrectly prune the very
  family that may produce the C4-free planar member — closed by the base-step
  counterexample above.

## Open gaps

- The mixed (V1 ≠ ∅) case past n=15 has no peer-reviewed bound; a run like the
  SMS "to n≤31" claim is unvetted.
- Whether the naive K4-triangle-expansion family contains a C4/C8-free member
  at n=24 (agent-run-12).
- Exact provenance of the "17/30" consolidated figures (chain Royle-15 →
  Markström-29 → "17/30" is source-anchored; a single paper stating "17" is not
  identified).
