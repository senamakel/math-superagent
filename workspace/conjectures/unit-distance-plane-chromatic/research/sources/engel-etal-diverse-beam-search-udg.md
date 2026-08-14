# Diverse beam search for densest planar unit-distance graphs — Engel, Hammond-Lee, Su, Varga, Zsámboki

**Source:** doi.org/10.1080/10586458.2025.2507956 (Experimental Mathematics,
published 2025-06-13); code and 60M+ graph database at
codeberg.org/zsamboki/dbs-udg
**Authors:** Peter Engel, Owen Hammond-Lee, Yiheng Su, Dániel Varga, Pál
Zsámboki (Cornell / Georgia Tech / UW-Madison / Alfréd Rényi Institute / ELTE)
**Full text:** NOT on disk — download_document network-blocked; content from
server-side read_sources passes over the DOI landing text and abstracts.

## What this establishes — the computational census machinery

- **Method:** a diverse backtracking beam search with a visitation-count
  penalty (promotes diversity), forward/backward steps that incrementally
  build dense unit-distance graphs, and pruning. This is a search *over dense
  graph constructions*, not over random point sets — directly the "search over
  constructions" discipline GOAL.md demands.
- **Reproduction:** the algorithm reproduces, up to isomorphism, every known
  maximally dense planar unit-distance graph for n ≤ 15 (where u(n) is known),
  and for 15 < n ≤ 30 reproduces all previously published densest graphs.
- **Extension:** generates dense candidates through n ≤ 100; the growth rate
  u(n)/n stays comparable beyond n = 30 (=: the literature's evidence about
  the density slope, not a proof).
- **Structure:** many dense UDGs arise as **Minkowski sums of smaller UDGs,
  including non-disjoint sums** — a structural observation matching problem.md's
  claim that Minkowski sums are the standard accumulation engine. The paper
  quantifies this: **~44.2% incidence of Minkowski-sum structure among the
  densest known UDGs**, with canonical examples: the optimal 9-vertex UDG from
  two unit triangles (the Hamming graph H(2,3) — a Cartesian product /
  disjoint Minkowski sum), and larger graphs as sums of e.g. a unit triangle
  and a 6-wheel. The search uses generator-based expansion, triangle
  completion, and parallelogram completion as its edge-structure moves —
  machinery the run's own construction engine can adopt.
- **Database:** over 60 million UDGs at codeberg.org/zsamboki/dbs-udg; the
  paper includes pseudocode and a section on Minkowski sums.

## Why it matters here

Two deliverables in GOAL.md are served directly: (1) the **census** deliverable
— "the chromatic numbers actually attained by the unit-distance graphs the run
can construct, with the maximum reached, the size at which the search became
infeasible, and why" — this paper is the state of the art for the *density*
census, and the run's own census should be stated against it; (2) the
**construction engine** — the observation that dense graphs are Minkowski sums
(including non-disjoint ones) sharpens the class of constructions the run's
engine should sweep. The run must NOT reuse their 60M-graph database as
answer-tier material (the densest graphs are the answer to the Erdős unit
distance problem, u(n)); what is usable is the method and the structural
observation.

```claim
id: dbs-udg-census-machinery
statement: A diverse beam search with a visitation metric, searching over dense planar unit-distance graph constructions, reproduces every maximally dense unit-distance graph up to isomorphism for n <= 15 (where u(n) is known) and every previously published densest graph for 15 < n <= 30; it generates dense candidates through n <= 100, with u(n)/n growth comparable beyond n = 30. A 60M+ graph database accompanies the paper.
hypotheses: planar unit-distance graphs; u(n) = max unit distances among n points; beam search is a heuristic, not a complete enumeration - candidates for n > 15 are not certified optimal.
holds-here: yes as census context and method; the run's own census must be stated against this, and its own chromatic-number sweep is a different (not yet published) census.
status: sourced (Experimental Mathematics 2025, DOI 10.1080/10586458.2025.2507956, via read_sources; full text not on disk)
bearing: sets the density-census state of the art the run reports against; the visitation/beam method is a candidate engine for the run's own construction search.
anchor: research/sources/engel-etal-diverse-beam-search-udg.md
```

```claim
id: dbs-udg-minkowski-structure
statement: Many dense unit-distance graphs are Minkowski sums of smaller unit-distance graphs, including sums of non-disjoint summands; Minkowski summation is a structural pattern among dense instances.
hypotheses: planar unit-distance graphs, empirical pattern observed across the enumerated census, not a theorem.
holds-here: yes - supports problem.md's claim that Minkowski sums are the main accumulation engine, and widens it to non-disjoint summands.
status: sourced (Engel et al. 2025, via read_sources; observed, not proved)
bearing: the construction engine should sweep Minkowski sums of algebraic point sets including non-disjoint summands and rotated variants.
anchor: research/sources/engel-etal-diverse-beam-search-udg.md
```

## Note on download

Full text and the codeberg database are network-blocked in this run. Status:
**sourced via read_sources; full text not on disk**.