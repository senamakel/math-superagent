> Note — replaces the abstract-only digest. Full text: [[carr-real.full]] (arXiv:2605.22844v1, A. Carr, 13 May 2026, 4 pp).

## What the source establishes

Set-up: a **minimal counterexample** to Erdős–Gyárfás = finite simple graph $G$ with $\delta(G)\ge 3$, no power-of-two cycle, chosen of minimum order then minimum size. All claims below are **proved** in the paper (short, elementary arguments).

- **Lemma 0.1.** Every proper subgraph $H\subsetneq G$ has $\delta(H)\le 2$. Proof: if $H$ had $\delta\ge 3$ it would be a smaller counterexample; its power-of-two cycle would embed in $G$, contradiction. (Hypothesis: $G$ minimal counterexample. Holds here trivially — this run studies exactly such $G$.)
- **Cor 0.1(1). Cubic vertices dominate.** Every vertex of $G$ is adjacent to a degree-3 vertex. Proof: $G-v$ is a proper subgraph, so $\delta(G-v)\le 2$; the only vertex of $G-v$ that can drop to degree $\le2$ by removing $v$ is a degree-3 neighbour of $v$.
- **Cor 0.1(2). Independent set.** The vertices of degree $\ge4$ form an independent set. Proof: deleting edge $uv$ of two $\ge4$-degree vertices leaves $\delta(G-uv)\ge3$, contradicting Lemma 0.1.
- **Cor 0.2.** Every *regular* minimal counterexample is cubic (3-regular), since all degrees $\ge3$ would violate 0.1(2).
- **Thm 0.1.** At least $4/7$ of the vertices have degree exactly 3. Proof: counting edges $e(V_3,V_{\ge4})\ge 4|V_{\ge4}|$ and $\le 3|V_3|$, so $4|V_{\ge4}|\le3|V_3|$, i.e. $|V|\le\frac74|V_3|$.

Carr credits the independent-set/dichotomy observation to Markström (§4 of companion note). Intro also records Carr's own **diameter-2 result**: every graph with $\mathrm{diam}(G)=2$, $\delta\ge3$ contains a $C_4$ or $C_8$ (arXiv:2508.19302, to appear BICA 109).

## Implication for this run

These are the strongest known *unconditional* structural constraints on a would-be minimal counterexample. Together they say: $G$ is crowded with cubic vertices ($\ge4/7$), cubic vertices form a dominating set, $\ge4$-degree vertices are independent (so each such vertex talks only to cubic ones), and every proper subgraph degenerates ($\delta\le2$). Any construction or SAT/SMS search for a counterexample must satisfy all five; a candidate violating one is refuted. The edge-count proof of Thm 0.1 is directly reusable as a SAT propagator.

## Verification-bound note from intro

Carr states (citing the computational literature) any cubic counterexample needs $\ge30$ vertices, and that smallest power-of-two cycles can first appear at length 16.

## Not settled

Nothing about $n\ge18$ general or $n\ge30$ cubic structure beyond the above. The paper gives no method — it is purely structural.

```claim
id: EG-cubic-dominates
statement: Every vertex of a minimal counterexample G is adjacent to a vertex of degree exactly 3.
hypotheses: G is a minimal counterexample (min order, min size, δ≥3, no power-of-two cycle).
holds-here: yes
status: proved (Carr Cor 0.1(1), from Lemma 0.1)
bearing: cubic vertices form a dominating set; constraints any search must satisfy
anchor: research/summaries/carr-real.md
```

```claim
id: EG-predominantly-cubic
statement: At least 4/7 of the vertices of a minimal counterexample have degree exactly 3.
hypotheses: G minimal counterexample.
holds-here: yes
status: proved (Carr Thm 0.1)
bearing: edge-count lower bound (4|V≥4|≤3|V3|), directly reusable as a SAT/Degree propagator
anchor: research/summaries/carr-real.md
```
