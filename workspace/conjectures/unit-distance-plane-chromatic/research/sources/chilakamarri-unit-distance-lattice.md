# Unit-distance graphs on the integer lattice and a Ramsey-type result

**Source:** link.springer.com/article/10.1007/BF01831139
(Chilakamarri, K.B. 1996, Aequationes mathematicae vol. 51, 48–67; companion
paper Chilakamarri & Mahoney 1995 at 10.1007/BF01827950)
**Full text:** not on disk (download network-blocked); read via read_sources.

## What this establishes

- **Lattice embedding reduction (Chilakamarri's theorem, cited):** A finite
  simple graph G embeds as a subgraph of (R^2, 1) — i.e. is a unit-distance
  graph — **iff** G is *faithfully √2-recurring* in Z^2. Meaning: there exists a
  scale d such that for arbitrarily large r, G embeds in (Z^2, r, √2) with all
  vertex distances ≥ d·r, where (Z^2, r, √2) has edges at Euclidean distance in
  [r−√2, r+√2]. This gives a **lattice-based, exact criterion** for unit-distance
  realizability in the plane. This is a principal-source structural fact for the
  run: the search can be conducted on lattice-constrained point sets.
- **Unit-distance graphs on Gaussian Z[i] and Eisenstein Z[ω] lattices** are
  studied for their chromatic structure — the algebraic-rings thread of the
  problem. Lattice arithmetic (norm relations) governs colouring.
- **Lower bound:** χ(Z^2, r, √2) ≥ 5 for all integers r ≥ 1. This is a
  *lattice-graph* lower bound (not the plane graph's chromatic number), but it
  shows lattice-based constructions can force 5 colours in a unit-distance-like
  setting.
- **Ramsey-type result:** for integer r > 1 and any colouring of Z^2, either a
  monochromatic pair at distance in [r−√2, r+√2] or a closest-to-each-other
  triad of 3 distinct colours.

## Why it matters here

Chilakamarri's theorem is a clean, citable structural criterion the run can
build on: instead of searching continuum point sets, restrict to faithfully
√2-recurring lattice configurations. And the Eisenstein/Gaussian lattice
colourings are exactly the "algebraic structure producing rigid unit-distance
graphs" thread the problem statement lists as a lead.

```claim
id: chilakamarri-lattice-criterion
statement: A finite simple graph G is a unit-distance graph in the plane iff G is faithfully √2-recurring in Z^2 (i.e. embeds in (Z^2,r,√2) at all large scales r with pairwise distances ≥ d·r).
hypotheses: G finite simple graph; plane unit-distance embedding; (Z^2,r,√2) = Z^2 with edges at distance in [r−√2, r+√2].
holds-here: true — gives an exact lattice-restricted framework for constructing/examining unit-distance graphs.
status: asserted by source (Chilakamarri 1993 JCTB; restated in the read_sources summary of the 1996 paper)
bearing: Exacts the search: unit-distance realizability is equivalent to a lattice criterion, so lattice/algebraic point sets are a complete search class.
anchor: research/sources/chilakamarri-unit-distance-lattice.md
```

```claim
id: chilakamarri-lattice-chi5
statement: The lattice graph (Z^2, r, √2), with edges at Euclidean distance in [r−√2, r+√2], satisfies chi >= 5 for every integer r >= 1.
hypotheses: Z^2 vertex set, distance interval as specified.
holds-here: not the plane graph; a lattice-graph lower bound. Relevant as evidence that algebraic-lattice constructions can exceed 4 colours in a unit-distance analogue.
status: asserted by source (1996 paper)
bearing: Shows lattice-restricted constructions can already force 5 colours; a candidate route and a caution (the plane graph is a different, harder object).
anchor: research/sources/chilakamarri-unit-distance-lattice.md
```

## Note on download

Full text blocked at network layer. Content from read_sources summary plus
search-result excerpts. Status: **sourced via read_sources; full text not on
disk.**
