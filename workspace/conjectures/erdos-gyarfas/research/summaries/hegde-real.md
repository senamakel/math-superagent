> Note — replaces the abstract-only digest. Full text: [[hegde-real.full]] (arXiv:2410.22842v2, Hegde, Sandeep & Shashank, 11 Feb 2025, 6 pp). Code: github.com/rbsandeep/Erdos-Gyarfas (C++, parallel Cilk variants).

## What the source establishes

**Computer-assisted proofs** (backtracking `explore` algorithm, Fig. 1; code released). The algorithm builds graphs vertex-by-vertex, only ever forbidding cycles of length a power of two, and returns True (⇒ no $P_k$-free counterexample extends) or False (⇒ a $P_k$-free counterexample exists). Lemma 1 + Cor 1 justify correctness: if $G^*$ is a minimal $P_k$-free counterexample then `explore(G,k)` returns False for any prefix $G$; so running `explore` on the path $P_{k}$ and getting True proves no $P_k$-free counterexample exists.

**Theorem 0.1.** Every $P_{13}$-free graph with $\delta(G)\ge3$ contains a cycle of length a power of two. (Conjecture holds for the class.) Proved by running `explore` for $k=3..13$, all returning True; $k=13$ took 11h56m (C++ serial) / 17m17s (Cilk).

**Theorem 0.2 (sharper).** Every $P_{12}$-free graph with $\delta\ge3$ contains a $C_4$ or a $C_8$. (Only lengths 4 and 8 forbidden.) This improves Hu–Shen's $P_{10}$-free ⇒ $C_4$ or $C_8$ (Discrete Math 2024) and Gao–Shan's $P_8$-free (Graphs Comb 2022).

**Verification-bound confirmation.** Intro asserts: counterexample needs $\ge17$ vertices, **cubic** counterexample needs $\ge30$ vertices [ref 10 Markström], **bipartite** counterexample needs $\ge30$ vertices [ref 11 Nowbandegani–Esfandiari]. Also: Liu–Montgomery proved every graph with average degree $\ge C$ (large constant) has a power-of-two cycle — this *disproved Erdős's own later belief* the conjecture fails for every min-degree $\ge3$.

**Appendix correctness checks** (position them as *evidence the code is right*, not proof): matches Hu–Shen $P_{10}$ result; manual check of $k=3..5$; unit tests; and reproduced all four 24-vertex cubic graphs with no $C_4/-C_8$ but a $C_{16}$, confirming the unique planar one as the Markström graph and its $P_{17}$ induced subgraph / $P_{18}$-free status.

## Relevance / limits for this run

This is one of the two strong restricted-class proofs (with 3-conn cubic planar). The $P_{12}$-free ⇒ $C_4$ or $C_8$ is the *sharper* structural statement the run could try to reproduce or beat. **Not useful as a general method**: the authors explicitly note the technique cannot extend to $H$-free graphs where $H$ contains a cycle (infinite min-deg-3 tree is $H$-free with no power-of-two cycle), and Massey-clique substitution shows it fails for non-path trees — so the approach is tied to $P_k$-free and does not touch the full conjecture. Leave open: whether `explore` resolves $P_k$ for $k\ge14$.

```claim
id: EG-P13-free
statement: Every P13-free graph with δ≥3 contains a cycle of length a power of two.
hypotheses: G finite simple, δ(G)≥3, G P13-free (no induced P13).
holds-here: yes (a class the run treats as partial proof)
status: proved, computer-assisted (Hegde–Sandeep–Shashank Thm 0.1)
bearing: done class; subsumes P8, P10 results
anchor: research/summaries/hegde-real.md
```

```claim
id: EG-P12-free-C4C8
statement: Every P12-free graph with δ≥3 contains a C4 or a C8.
hypotheses: G finite simple, δ≥3, P12-free.
holds-here: yes
status: proved, computer-assisted (Thm 0.2)
bearing: sharper forced-cycle statement than P13; a good test target for the oracle/SAT
anchor: research/summaries/hegde-real.md
```

```claim
id: EG-bipartite-30
statement: Any bipartite counterexample to the conjecture has at least 30 vertices.
hypotheses: G bipartite, δ≥3, no power-of-two cycle.
holds-here: yes
status: cited (Nowbandegani & Esfandiari 2011), not in this library's full text
bearing: one more restricted verification bound; anchor for SAT check
anchor: research/summaries/hegde-real.md
```
