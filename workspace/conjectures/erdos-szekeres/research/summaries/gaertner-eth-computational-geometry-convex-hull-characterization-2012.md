# Gärtner, ETH Computational Geometry course notes — convex hull extremal characterization (2012)

<!-- source: https://ti.inf.ethz.ch/ew/Lehre/CG13/lecture/cg-2012.pdf | full text at research/sources/gaertner-eth-computational-geometry-convex-hull-characterization-2012.full.md -->

**Publication.** Bernd Gärtner, ETH Zürich *Computational Geometry* course notes, version 2012 (lecture PDF). University course notes; a standard, authoritative exposition of convex hulls and their characterization.

## What it establishes (and why it matters here)

This is the reference that **closes the `staircase-convexity-unsourced` gap** in the allowable-sequence thread: the surviving, machine-confirmed criterion "p is a hull vertex of S ⟺ p is extreme-in-projection (first-or-last in some S-restricted projection order)" is an instance of a standard folklore fact, now anchored to a held source.

- **Definition 3.6.** A *vertex* (extremal point) of `conv(P)` is a point `p ∈ P` with `p ∉ conv(P ∖ {p})`. The vertices of a convex polytope are its extreme points.
- **Proposition 3.17.** A point `p ∈ P = {p1,…,pn} ⊂ R²` is **extremal for P ⇔ there is a directed line g through p such that P∖{p} is to the left of g.**

The directed line g is a supporting line of the hull at p. If `u` is the unit normal to g, then projecting P onto the direction `u` puts `p` at the *first or last* position of the projected order (p is maximal along `+u` or `−u`). Hence:

> **EPS criterion (extreme-in-projection = hull vertex).** For a planar point set S in general position, `p` is a convex-hull vertex of S iff there is a direction such that `p` is the unique first (or unique last) element of the orthogonal-projection order of S onto that direction.

This is exactly the characterization the admissible-sequence/extremal line verified against the exact oracle `lib/es_geom` on `es_construct` (agreement on every |S|≥4 subset; 3-subsets trivially all convex). The theorem also connects to the partition-into-half-planes view used by the rotating-line (k-set) enumerator (`gsplit`): a supporting line is a half-plane with p on the boundary, and "p is first in some projection" is the same as "there is a half-plane whose boundary is a supporting line through p".

**Caveat on wording.** Proposition 3.17 states the supporting-line form. The projection/maximal form ("first-or-last in projection order") is the equivalent restatement the thread uses; that equivalence (extreme in direction u ⟺ maximal dot-product ⟺ on the supporting line with normal u) is standard and is what the oracle checked. For a formal statement, cite Prop 3.17 plus the dot-product equivalence.

## Relation to the run

- Lifts the "pointwise extreme-in-projection ⟺ hull vertex" branch of the allowable-sequence thread from machine-confirmed-but-unsourced to **sourced** (university course notes, faithful to the geometric definition used in GP80/GP93). `staircase-convexity-unsourced` core is closed: the property is a standard hull-vertex characterization, not a special property of `es_construct`.
- It does **not** make load-bearing the (refuted) reversal-depth = ES block-index mechanism, nor the (refuted) contiguous-block staircase convexity form. Those remain closed.
- It is a characterization of a *single* hull vertex, not of "n points in convex position" globally; the latter is the 4-point-criterion / cup-cap route already held.

## claim block (for CLAIMS.md)
> This source **closes the core of `staircase-convexity-unsourced`**: the surviving criterion of the allowable-sequence thread — "p is a hull vertex of S ⟺ p is extreme-in-projection (first-or-last in some S-restricted projection order)" — is a standard hull-vertex characterization, now anchored to a held source rather than machine-confirmed-but-unsourced.

```claim
id: hull-vertex-extreme-in-projection-sourced
statement: For a planar point set S in general position, a point p is a convex-hull vertex (extremal point) of S iff there is a direction u such that p is the unique first (or unique last) element of the orthogonal-projection order of S onto u — equivalently p is maximal along u. Supporting-line form: p is extremal for S iff there is a directed line g through p with S∖{p} to the left of g (Gärtner, ETH Computational-Geometry course notes, Prop 3.17). The direction of the normal u to g is the direction of maximality.
hypotheses: S ⊂ R² finite, general position (no three collinear); p ∈ S; the projection direction generic (u not orthogonal to any line spanned by two points of S).
holds-here: true — this is exactly the pointwise extreme-in-projection criterion the allowable-sequence thread verified against lib/es_geom on es_construct (agreement on every |S|≥4 subset; 3-subsets trivially all convex). The criterion is standard, not a property of the es_construct template.
status: sourced (university course notes, faithful to the standard convex-hull definition used throughout GP80/GP93); the EPS property itself was machine-confirmed.
bearing: closes the core of the staircase-convexity-unsourced source gap. It does NOT reopen the refuted reversal-depth = ES block-index mechanism or the refuted contiguous-block/staircase convexity form — those remain closed. It supplies the vocabulary for the live allowable-sequence/extremal-structure direction: convex position of a subset S is equivalent to every element of S being extreme-in-projection, i.e. every element a hull vertex of conv(S).
anchor: research/sources/gaertner-eth-computational-geometry-convex-hull-characterization-2012.full.md
```
