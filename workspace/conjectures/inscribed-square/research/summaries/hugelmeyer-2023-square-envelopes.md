# Inscribed Squares and Relation Avoiding Paths

**Source:** Cole Hugelmeyer, arXiv:2301.01340 (math.MG), Jan 2023  
**URL:** https://doi.org/10.48550/arxiv.2301.01340  
**Full text:** `research/sources/hugelmeyer-2023-square-envelopes.full.md`

## What it establishes

Develops a connection between the inscribed square problem and "relation avoiding paths" in a complex vector space. The main result:

- **Theorem:** If a Jordan curve γ has no inscribed square, then γ has a structure called a *square envelope* — a continuous family of pairs of edges (ordered 2-tuples of distinct points on γ) that avoid certain linear relations. This is presented as a seeming impossibility.

- **Conditional result (Theorem 3):** Assuming a *spiral conjecture* about relation-avoiding paths in vector spaces, any Jordan curve that is smooth except at finitely many points (with arbitrarily complicated singularities) has an inscribed square.

- **Classification of square types:** Squares inscribed in Jordan curves are classified into types I (gracing), II, and III based on vertex order around the curve vs around the square. These correspond to distinct components of a configuration space, giving invariant parities under generic homotopies.

- **Spiral conjecture:** The key open conjecture in the paper — a statement about paths in C^2 avoiding a certain linear relation (the "first two corners of one square touching the second two corners of another"). The conjecture would fill the gap between the square-envelope structural result and actual square existence.

## Relevance to this run

This is a novel attack on the inscribed square problem that does **not** use the Mobius-band parity argument, Stromquist's locally-monotone condition, or any rectifiability. Instead it reformulates the problem as a statement about avoiding linear relations in a vector space. The conditional result (Theorem 3, assuming the spiral conjecture) targets curves with finitely many singularities — a class strictly larger than locally monotone and larger than rectifiable (since rectifiable curves can have infinitely many singular points). **However, the result is fully conditional on an unproven conjecture**, so nothing here is load-bearing. The square-envelope concept and the type-I/II/III classification could be useful framing devices.
