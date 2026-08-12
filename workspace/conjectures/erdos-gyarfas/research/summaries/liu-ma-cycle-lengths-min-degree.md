# Liu–Ma 2015 — cycle lengths and minimum degree of graphs

Source: Chun-Hung Liu, Jie Ma, "Cycle lengths and minimum degree of graphs", arXiv:1508.07912 ([https://arxiv.org/abs/1508.07912](https://arxiv.org/abs/1508.07912)). Full text: `research/sources/liu-ma-cycle-lengths-min-degree.full.md`.

## What the source establishes

Let $G$ have minimum degree at least $k+1$.

- If $G$ is **bipartite**, then there are $k$ cycles in $G$ whose lengths form an arithmetic progression with common difference 2.
- For general $G$: there are $\lfloor k/2\rfloor$ cycles with **consecutive even lengths**, and $k-3$ cycles whose lengths form an arithmetic progression with common difference 1 or 2.
- If $G$ is **2-connected and non-bipartite**: $\lfloor k/2\rfloor$ cycles with consecutive odd lengths.

It also confirms **Thomassen's two 1983 conjectures on cycle lengths modulo a fixed integer $k$** when $k$ is even:
- (1) every graph with minimum degree at least $k+1$ contains cycles of all even lengths modulo $k$;
- (2) every 2-connected non-bipartite graph with minimum degree at least $k+1$ contains cycles of all lengths modulo $k$.
Both best possible.

## Why it matters for Erdős–Gyárfás

This is the core of the "adjacent cycle-length machinery" the run's method statement points at. It guarantees **many** cycle lengths (progressions, consecutive even lengths, all lengths modulo $k$) from large minimum degree. But every conclusion is a *set of lengths* — an arithmetic progression or a congruence class — and none forces a *specific* sparse length like a power of two. At $\delta = k+1$, for an interval/progression of lengths to contain a power of two one needs the progression to span the gap between consecutive powers of two; these results do not deliver that at the low degree 3. So they tell us a $\delta\ge3$ graph has *some* concentration of cycle lengths, but not a prescribed power of two — exactly the structural gap the conjecture sits in.

These results hold at all $\delta = k+1 \ge 3$, so in principle they apply to $\delta = 3$ ($k = 2$): a $\delta \ge 3$ graph has $\lfloor 2/2\rfloor = 1$ consecutive even length (trivial) and $k-3 = -1$ progressions (vacuous); the non-bipartite 2-connected case gives $1$ consecutive odd length. So the general theory gives essentially nothing at the degree-3 threshold aside from parity-concentration facts. This is a precise statement of why the conjecture is hard: the machine that produces many cycle lengths produces many only when degree is large.

```claim
id: EG-cycle-lengths-many-from-degree
statement: A graph with minimum degree at least k+1 contains: k cycles in arithmetic progression of common difference 2 if bipartite; floor(k/2) cycles with consecutive even lengths and k-3 cycles in an AP of difference 1 or 2 in general; and (if 2-connected non-bipartite) floor(k/2) cycles with consecutive odd lengths. Also, for even k, all even lengths modulo k for delta>=k+1, and all lengths modulo k if 2-connected non-bipartite.
hypotheses: finite simple graph, minimum degree >= k+1 (k even for the modulo results), connectivity/non-bipartiteness as stated
holds-here: yes as stated — but these are set-of-lengths guarantees; at k=2 (delta=3) they collapse to near-trivial parity facts and force no specific length such as a power of two.
status: proved (in source, not independently reproduced here)
bearing: maps the boundary of the many-cycle-lengths machinery; shows the degree-3 case gives almost no length-concentration, which is the structural void the EG conjecture occupies.
anchor: research/summaries/liu-ma-cycle-lengths-min-degree.md
```
