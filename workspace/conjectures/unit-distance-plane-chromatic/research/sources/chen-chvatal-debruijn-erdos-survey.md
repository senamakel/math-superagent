# Problems related to a de Bruijn–Erdős theorem — Chen and Chvátal 2007

**Source:** doi:10.1016/j.dam.2007.05.036, Discrete Applied Mathematics
**Authors:** Xiaomin Chen, Vašek Chvátal
**Full text:** not on disk; read via read_sources.

## What this establishes

The modern survey of the de Bruijn–Erdős compactness theorem and its variants
— the exact reduction underlying the whole finite-subgraph attack on the
chromatic number of the plane:

- **Statement context:** the de Bruijn–Erdős theorem — an infinite graph is
  k-colourable iff every finite subgraph is — lies at the root of a large
  family of compactness results in combinatorial geometry and combinatorics.
  The survey gathers the questions around it: conditions under which the
  equality between the chromatic number of an infinite graph and the supremum
  over its finite subgraphs holds, and the extremal/structural assumptions
  needed in various settings (including geometric/metric constraints).
- **Related results and tools:** Sylvester–Gallai-type configurations, metric
  betweenness (Chvátal's line of work), the finite/infinite dichotomy, and the
  roles played by Rado's selection principle and compactness (see Gottschalk
  1951, in this library).
- **Broader placement:** the compactness principle connects infinite-graph
  colorability to finite subgraphs across many areas (thresholds, Ramsey-type
  problems, hypergraphs), confirming that the de Bruijn–Erdős reduction used by
  this run is a well-understood, standard, citable input.

## Why it matters here

The run's `debruijn-erdos-compactness` claim currently carries status "proved
(classical, 1951)" with the note that the original paper's proof is not on disk.
This survey is the acknowledged modern reference for the theorem and its
hypotheses, giving the claim a second primary anchor and spelling out the
"choice principle" hypothesis (formally: Rado selection / Tychonoff for finite
spaces, per Gottschalk 1951) that the claim block records.

```claim
id: chen-chvatal-dbe-survey
statement: The de Bruijn-Erdős compactness theorem (infinite graph k-colourable iff every finite subgraph is) is the root of a surveyed family of compactness results in combinatorial geometry; its hypotheses and variants are standard and citable (Chen–Chvátal 2007 survey). The reduction chi = sup over finite subgraphs is the established route for infinite geometric graph colouring problems.
hypotheses: Infinite ordinary graph; k a nonnegative integer; a choice principle (Rado selection / Tychonoff for finite spaces).
holds-here: true — corroborates the run's load-bearing compactness claim with a modern survey-level primary source.
status: sourced (survey; theorem classical 1951, restated and surveyed here)
bearing: Provides the second anchor for the finite-subgraph reduction; the run can treat chi(G_plane) = sup_finite chi as standard proved input.
anchor: research/sources/chen-chvatal-debruijn-erdos-survey.md
```

## Note on download

Full text blocked at network layer. Content from read_sources survey summary.
Status: **sourced via read_sources; full text not on disk.**