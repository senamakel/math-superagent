# Montgomery, "Cycles and expansion in graphs" (2026 survey)

**Source:** Richard Montgomery, "Cycles and expansion in graphs", EMS Magazine / Jahresbericht survey article, 2026. URL: https://ems.press/content/serial-article-files/52107. Full text on disk: `research/sources/montgomery-cycles-expansion-survey.full.md`.

## What the source establishes

A survey of three cycle problems advanced by expansion techniques. For this
run the relevant section is the second: cycle lengths in dense graphs, which
is the modern treatment of the dense-regime attacks on the Erdős–Gyárfás
conjecture.

- **Theorem 2.1.** There is some $d > 0$ such that every graph with average
  degree at least $d$ has a cycle whose length is a power of 2. This is the
  Liu–Montgomery theorem (the survey states it without attribution in this
  section; the companion digest attributes the power-2 result to Liu–
  Montgomery 2020). It resolves the *dense* version: for large but bounded
  average degree ($\delta$ replaced by average degree $\ge d_0$), a 2-power
  cycle is forced.
- **Conjecture 2.2.** The Erdős–Gyárfás conjecture itself: every graph with
  minimum degree at least 3 has a 2-power cycle — stated as still open.
- **Theorem 2.3.** Every graph $G$ with average degree $d$ satisfies (a bound
  on sums of reciprocals of cycle lengths — the statement is cut in the
  digest; the exact inequality is in the full text).
- **Theorem 2.4.** Every graph with chromatic number at least $k$ satisfies
  $\sum_{\ell \in \mathcal{C}_{odd}(G)} 1/\ell \ge (\tfrac12 - o(1))\log k$
  (odd cycle lengths have reciprocal sum at least half log chromatic number).
- **Conjecture 1.1 (Erdős–Gallai)** and **Theorem 1.2**: every $n$-vertex
  graph decomposes into $O(n \log^* n)$ cycles and edges — the log-star
  machinery that underlies the Sudakov–Verstraëte iterated-logarithm bound.

## Why it matters for this problem

The survey is the modern statement of the dense-regime result chain
(Verstraëte 2005 → Sudakov–Verstraëte 2008 → Liu–Montgomery 2020):
average-degree-$\ge d_0$ forces a 2-power cycle, but the minimal-degree
conjecture ($\delta \ge 3$) remains open. It frames the obstruction exactly as
the run's problem.md does: degree conditions force intervals/arithmetic
progressions of cycle lengths, and the density threshold must overwhelm the
gaps between powers of two. Theorem 2.1's significance: Erdős's own later
belief that the conjecture fails for every minimum degree ≥ 3 is *false* in
the dense regime — there is a uniform $d_0$ that works for *all* graphs.

## Claims

```claim
id: EG-dense-average-degree-pow2-survey
statement: There is a constant d0 such that every finite simple graph with average degree at least d0 contains a cycle whose length is a power of 2 (Theorem 2.1 of Montgomery's 2026 survey; the theorem is due to Liu–Montgomery 2020).
hypotheses: finite simple graph, average degree ≥ d0 (d0 large, absolute, unspecified in the survey)
holds-here: no for the EG conjecture — average degree ≥ d0 is a denser hypothesis than δ≥3, so the theorem does not resolve the conjecture; yes as a true theorem about the dense regime
status: proved (in Liu–Montgomery; survey restates it)
bearing: fixes the dense-regime state of the art: the obstruction to the full conjecture is exactly the sparse/min-degree-3 regime
anchor: research/summaries/montgomery-cycles-expansion-survey.md
```

```claim
id: EG-odd-cycle-reciprocal-sum
statement: Every graph with chromatic number at least k has odd cycle lengths whose reciprocal sum is at least (1/2 − o(1)) log k (Montgomery survey Theorem 2.4).
hypotheses: chromatic number ≥ k
holds-here: no — chromatic number is not a hypothesis of the EG conjecture; adjacent machinery only
status: proved
bearing: shows how far the "many cycle lengths" machinery goes: reciprocal sums, intervals, progressions — none of it hits a prescribed sparse length
anchor: research/summaries/montgomery-cycles-expansion-survey.md
```