# Liu–Montgomery 2020 — solution to Erdős–Hajnal odd cycle problem, and the average-degree power-of-2 result

Source: Hong Liu, Richard Montgomery, "A solution to Erdős and Hajnal's odd cycle problem", arXiv:2010.15802 ([https://arxiv.org/abs/2010.15802](https://arxiv.org/abs/2010.15802)), submitted Oct 2020, accepted version Sep 2022, 42 pages. Full text: `research/sources/liu-montgomery-odd-cycle-power2.full.md`.

## What the source establishes

Three theorems.

1. **Erdős–Hajnal odd cycle problem** (posed 1981). For a graph $G$ of chromatic number $k$, let $\mathcal C_{\rm odd}(G)$ be the set of odd cycle lengths. Then
   $$\sum_{\ell \in \mathcal C_{\rm odd}(G)} \frac{1}{\ell} \ge \Big(\frac12 - o_k(1)\Big)\log k .$$
   This is asymptotically optimal.

2. **Erdős's 1984 question — average degree forces a power-of-2 cycle.** Erdős asked whether there is some $d$ such that every graph with chromatic number at least $d$ (or even merely average degree at least $d$) contains a cycle of length a power of 2. Liu–Montgomery prove that **an average-degree condition is sufficient**: there is a constant $d_0$ such that every graph with average degree at least $d_0$ contains a cycle of length a power of 2. The methods apply to a wide range of length sequences beyond the powers of 2.

3. **Thomassen's 1984 subdivision conjecture.** For every $k$ there is some $d$ such that every graph of average degree at least $d$ contains a subdivision of $K_k$ in which every edge is subdivided the same number of times.

## Why it matters for Erdős–Gyárfás

The Erdős–Gyárfás conjecture is about **minimum degree ≥ 3 bounded**. The average-degree power-of-2 result (2) shows the conjecture is true for **very large minimum/average degree** — it disproved Erdős's own later belief that the conjecture fails for every minimum degree ≥ 3 (see also ROOT.md note on the "dense regime") — but it says nothing about the degree-3 threshold that the conjecture actually concerns. $d_0$ here is a large (unspecified) constant, and the result collapses exactly where $\delta = 3$ is fixed.

The method (expansion, Komlós–Szemerédi, finding long intervals of cycle lengths then selecting the right parity/structure) is precisely the *interval* machinery that the obstruction paragraph in `problem.md` warns cannot work at fixed $\delta = 3$: it produces a cycle of a length lying in some range, and the range needed to force a power of two grows faster than $\delta=3$ buys. So this result marks the boundary of what the dense/expansion approach can reach, and why the degree-3 problem is hard.

```claim
id: EG-dense-average-degree-pow2
statement: There is a (large, unspecified) constant d0 such that every finite simple graph with average degree at least d0 contains a cycle whose length is a power of 2. (Erdős 1984 question, solved by Liu–Montgomery 2020, arXiv:2010.15802.)
hypotheses: finite simple graph, average degree >= d0 (average, not minimum)
holds-here: yes as stated (a true theorem); but its threshold is a huge constant and it says nothing about the fixed-delta-3 class the conjecture concerns — the conjecture is the limit as the degree threshold is lowered to 3.
status: proved (in the source; not independently reproduced here)
bearing: marks the upper boundary of the dense/expansion approach; confirms the conjecture for very large degree, disproving Erdős's later pessimism, but does not touch minimum degree 3.
anchor: research/summaries/liu-montgomery-odd-cycle-power2.md
```

```claim
id: EG-dense-regime-constraint
statement: The cycle chosen in the Liu–Montgomery power-of-2 argument lies at a length in some long interval of achievable cycle lengths; forcing a power-of-2 cycle by an interval argument needs the interval to outweigh the gaps between powers of two, which scales with the largest power below it.
hypotheses: none (structural observation about the method)
holds-here: yes — this is exactly why fixed minimum degree 3 is hard (see problem.md obstruction paragraph)
status: sourced observation, not a theorem
bearing: explains why power-of-2 results need large degree; an approach that ends in "all lengths in [a,b]" makes progress only if b > 2a.
anchor: research/summaries/liu-montgomery-odd-cycle-power2.md
```
