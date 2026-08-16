# Bruhn & Schaudt, "The union-closed sets conjecture almost holds for almost all random bipartite graphs" (arXiv:1302.7141)

**Full text:** [[bruhn-schaudt-random-bipartite-2013.full]] · **Source:** https://arxiv.org/abs/1302.7141 (DOI 10.48550/arXiv.1302.7141; published EJC 2013, doi 10.1016/j.ejc.2013.07.010 per FRONTIER)

Works entirely in the **graph formulation** (Bruhn–Charbit–Schaudt–Telle): in every bipartite graph with at least one edge, each of the two colour classes contains a vertex belonging to at most half of the maximal stable (independent) sets. A vertex in at most half is "rare".

## Main theorem

For every fixed edge-probability `p ∈ (0,1)` and every `δ > 0`, almost every random bipartite graph `G(n,p)` satisfies the union-closed sets conjecture **up to δ**: each colour class has a vertex that lies in at most `(1/2 + δ)` of the maximal stable sets of `G`.

So UC "almost holds for almost all" random bipartite graphs — a probabilistic/average-case statement, not a proof of the conjecture class.

```claim
id: random-bipartite-almost-holds
statement: For every fixed p∈(0,1) and δ>0, almost every random bipartite graph has, in each colour class, a vertex lying in at most (1/2+δ) of its maximal stable sets (i.e. it satisfies the graph form of the union-closed conjecture up to δ).
hypotheses: G = G(n,p) random bipartite graph, fixed p, n→∞; graph formulation of UC.
holds-here: true
status: proved (probabilistic; the exact/limiting statement is asymptotic with δ-slack, not the conjectured exactly-half bound)
bearing: random bipartite graphs are a "settled" class only in this up-to-δ average-case sense. It confirms UC is not violated in the typical/random regime, so a counterexample must be a highly structured non-random object — supports the minimal-counterexample structural programme.
anchor: research/sources/bruhn-schaudt-random-bipartite-2013.full.md
```

## Why it matters for this run

- Fills a frontier lead (the paper is cited several times in the library's own FRONTIER but was absent from `sources/`).
- Complements the settled *deterministic* graph classes (chordal bipartite, subcubic bipartite, bipartite series-parallel, bipartitioned circular interval — Bruhn–Charbit–Schaudt–Telle): random bipartite graphs hold only up to δ / almost surely.
- The up-to-δ formulation is the standard way the graph side escapes needing rarity exactly — neighbourhood of the false claim "a random bipartite graph satisfies UC exactly."
