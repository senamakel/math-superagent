> Summary — replaces the digest. Full text: [[gao-shan-P8-free-html.full]] (Y. Gao, S. Shan, "Erdős-Gyárfás Conjecture for $P_8$-free graphs", arXiv:2109.01277v1, 3 Sep 2021; published Graphs and Combinatorics 38(6):168, 2022).

## What the source establishes

**Theorem 1.1.** Every P5-free graph with minimum degree at least 3 contains a 4-cycle.

**Theorem 1.2.** Every P8-free graph with minimum degree at least 3 contains a 4-cycle or an 8-cycle. (This proves the EG conjecture for P8-free graphs.)

**Lemma 3.1** (proved in Nowbandegani–Esfandiari–Shirdareh–Bibak [6], restated here): *Let G be a graph with δ(G) ≥ 3. If G does not contain C4 as a subgraph, then G has an induced cycle Ck for some k ≥ 5.* This is a reusable, general structural fact: a C4-free δ≥3 graph always has an induced cycle of length ≥ 5.

**Proof technique of Theorem 1.2.** Assume G is connected, P8-free, δ≥3, and contains neither C4 nor C8. By Lemma 3.1 there is a shortest induced cycle C of length k with 5 ≤ k ≤ 7 (k=8 excluded since C8 is forbidden as a subgraph anyway; k≥8 would give an induced P8). The three claims (3.2: no two consecutive vertices of a 5-cycle share a common neighbor; 3.3: k≥6; 3.4: k=7) then force a chain of neighbors, each time excluding a C4 or C8 and producing an induced P8, a contradiction. The argument works purely by forbidden C4/C8 + induced P8, i.e. it is a "shortest induced cycle + neighbor structure" technique.

## Implication for this run

- **Lemma 3.1** is the natural starting point for any "induced cycle in a C4-free δ≥3 graph" argument, and is already in the literature (Nowbandegani et al., DMGT 34 (2014) 635–640).
- The Gao–Shan Claims 3.2–3.4 are **specific to P8-free graphs** and do not transfer to the general setting of a minimal counterexample (which is not known to be P8-free).
- The paper uses a minimum cut-set argument (Claim 2.1, proving κ(G)≥2) **inside the P5-free proof** — this is a 2-connectivity result but only for that restricted class, and does not state anything about EG minimal counterexamples.

```claim
id: EG-C4-free-induced-cycle
statement: Every graph with δ≥3 and no C4 as a subgraph contains an induced cycle Ck for some k≥5 (chordless cycle of length at least 5).
hypotheses: finite simple graph, δ(G)≥3, no C4 subgraph.
holds-here: yes — a C4-free minimal counterexample would be such a graph.
status: proved (Nowbandegani–Esfandiari–Shirdareh–Bibak, DMGT 34 (2014) 635–640; restated as Lemma 3.1 in Gao–Shan arXiv:2109.01277).
bearing: any "no C4" structural argument about a minimal counterexample starts from a shortest induced cycle Ck, k≥5; the neighborhoods of its vertices are then heavily constrained by C4/C8/C16-freeness.
anchor: research/summaries/gao-shan-P8-free-html.md
```