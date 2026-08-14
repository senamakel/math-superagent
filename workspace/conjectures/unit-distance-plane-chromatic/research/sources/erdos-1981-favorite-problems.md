# Erdős — On the combinatorial problems which I would most like to see solved (1981)

**Source:** doi:10.1007/bf02579174
**Author:** P. Erdős, COMBINATORICA 1 (1981)
**Full text:** not on disk; read via read_sources.

## What this establishes — the problem founder's own framing and conjecture

- Erdős states the chromatic-number-of-the-plane problem as: determine the
  minimum number of colours needed to colour every point of the plane so that
  no two points at distance exactly 1 share a colour. (This is exactly the
  problem.md statement — the canonical framing.)
- He gives the bounds **4 ≤ χ(R²) ≤ 7**: lower 4 from a unit-distance graph
  requiring four colours; upper 7 from a seven-colour tiling.
- **Erdős conjectured χ = 4** — that the plane is 4-colourable. The problem
  statement's warning ("Do not assume the answer is greater than 4; opinions
  have been offered for all four") has a named anchor: the problem's founder
  himself believed 4.

## Why it matters here

The run's bias must be balanced. A search that only ever looks for
5-chromatic unit-distance graphs cannot find the answer if the answer is 4.
Erdős's own conjecture is the strongest single datum on the "χ = 4" side, and
it should be recorded as such so the run's construction effort keeps a
proportional thread on proving 4-colourability of structured families.

```claim
id: erdos-1981-conjectures-chi4
statement: Erdős (1981) states chi(R^2,1) with bounds 4 <= chi <= 7 and conjectures chi = 4 — that the plane is 4-colourable.
hypotheses: Plain (non-measurable) chromatic number of the plane; Euclidean unit-distance graph.
holds-here: true — a named balancing datum: the problem's founder conjectured the answer is 4, so a purely 5-seeking search is biased.
status: sourced (Erdős 1981, via read_sources summary)
bearing: Keeps the lower-bound search honest: equal weight should go to proving 4-colourability of the generated family as to seeking a 5-chromatic counterexample.
anchor: research/sources/erdos-1981-favorite-problems.md
```

## Note on download

Full text blocked at network layer. Content from read_sources summary of the
paper itself. Status: **sourced via read_sources; full text not on disk.**