# Bondy & Vince, "Cycles in a graph whose lengths differ by one or two", J. Graph Theory 27 (1998) 11–15

[[research/sources/bondy-vince-cycles-lengths-differ-one-two.full.md]] · source URL: https://people.clas.ufl.edu/avince/files/Cycles.pdf

## What it establishes

This is the canonical adjacent result on the *distribution* of cycle lengths in min-degree-3 graphs — the machinery the Erdős–Gyárfás conjecture sits inside. It does not prove EG (powers of two are sparse, differences of 1 or 2 are dense), but it is the strongest structural statement about how close cycle lengths must be under δ≥3, and it is what settles Erdős problem #64.

**Question answered** (attributed to Erdős and colleagues): in a simple graph where every vertex has degree at least three, must there exist two cycles whose lengths differ by one or two?

**Theorem 1.** With the exception of K1 and K2, every simple graph having at most two vertices of degree less than three contains two cycles whose lengths differ by one or two.
- Best possible: each of C3, P3, K2,3 has three vertices of degree <3 but no two cycles differing by 1 or 2.
- With twelve exceptions, every simple graph with at most three vertices of degree <3 contains two such cycles; the seven extra exceptions come from attaching a pendant edge to degree-two vertices of C3, P3, K2,3.

**Theorem 2.** Every nonbipartite 3-connected graph has two cycles whose lengths differ by one.

**Conjecture** (Bondy–Vince). For any nonnegative integer k, with finitely many exceptions, every simple graph having at most k vertices of degree less than three has two cycles whose lengths differ by one or two. *(This was later confirmed by Gao–Ma, "On a conjecture of Bondy and Vince".)*

## Why it matters for this problem

- The bond between δ≥3 and *dense* cycle-length sets is strong: cycles of consecutive/near-consecutive lengths are forced. EG asks for a cycle *at a prescribed sparse length* (power of two), which is why the interval-producing machinery cannot be the whole answer — but Bondy–Vince is the reference for what δ≥3 already gives for free.
- Lemma 1 (2-connected graph, induced cycle bridge with many internal vertices) and Lemma 2 (nonbipartite 2-connected, bridge structure of induced odd cycle) are constructive tools that any attempt on a minimal counterexample — which is 2-connected-ish and non-bipartite-ish — can reuse.
- Relevance to the run's cut-vertex / 2-connectivity direction: these bridge lemmas operate on exactly the lobe/separator structure the run is analysing.

**Claim block** (fenced for CLAIMS.md):

```claim
id: EG-BondyVince-two-cycles
statement: Every simple graph with at most two vertices of degree less than three (except K1 and K2) contains two cycles whose lengths differ by one or two. Every nonbipartite 3-connected graph has two cycles whose lengths differ by one.
hypotheses: G simple; at most 2 vertices of degree <3 (for Thm 1); nonbipartite 3-connected (for Thm 2).
holds-here: Thm 1 applies to a minimal counterexample G (δ(G)≥3, so zero vertices of degree <3): G contains two cycles of consecutive-or-adjacent lengths. This does NOT imply a power-of-two cycle, so it is adjacent machinery, not the answer.
status: proved (source)
bearing: establishes the dense-lower-bound side of the cycle-spectrum picture; the reference for what δ≥3 forces toward (not at) prescribed sparse lengths.
anchor: research/summaries/bondy-vince-cycles-lengths-differ-one-two.md
```
