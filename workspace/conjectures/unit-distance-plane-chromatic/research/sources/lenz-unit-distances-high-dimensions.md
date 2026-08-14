# The Lenz construction for many unit distances — statement and planar restriction

**Subject:** the Lenz construction, named from memory in `research/approaches/lenz-roots-of-unity.md`, now stated precisely from a held-adjacent source.

## What the construction is (sourced)

**Swanepoel, K.J., "Unit Distances and Diameters in Euclidean Spaces", Discrete & Computational Geometry (2008), doi:10.1007/s00454-008-9082-x** — read via read_sources (full text not on disk; publication-adjacent to this run's subject but about the extremal *counting* problem, d ≥ 4, not the chromatic problem, so not screened). Matching passages stored verbatim in this cycle's read:

> "For d ≥ 4 (the subject of this paper), the situation changes drastically. Lenz, as reported in [5], observed that if we take p := d/2 circles in pairwise orthogonal 2-dimensional subspaces, each with center at the origin and radius 1/√2, then any two points on different circles are at unit distance."

> "if n points are chosen by taking n/p + O(1) points on each circle, (p−1)/(2p)·n² − O(1) unit distances are obtained."

The referenced [5] is Erdős 1946 (the library holds `erdos-sets-of-distances-1946.md`); Swanepoel cites the Lenz observation "as reported in [Erdős 1946]" — the run does not hold Lenz's own note, and the primary Lenz reference remains unverified.

**Consequences that bear on the run (all from the sourced passage above):**

1. The Lenz trick — "any two points on *different* circles are at unit distance" — is a **d ≥ 4 phenomenon**: it needs p ≥ 2 pairwise orthogonal 2-planes, and d = 2p. In the plane there is exactly one 2-plane, p = 1, and the cross-circle construction has nothing to act on.
2. In the plane, the construction degenerates to points on a **single circle of radius 1/√2**. On that circle unit distances are exactly the 90° chords (derivation below), so each point has exactly two unit neighbours. Max degree ≤ 2; the induced graph is a union of cycles/paths, χ ≤ 3.
3. For a **two-concentric-circle** planar configuration (the `lenz-roots-of-unity` proposal's shape: {ζ_m^i} ∪ {ρ ζ_n^j}), cross pairs at unit distance satisfy, per fixed i, |ζ^i − ρ w| = 1 with |w| = 1, i.e. Re(ζ^i w̄) = ρ/2 — the intersection of a line with the unit circle, **at most two solutions j per i**. Within-circle unit pairs likewise at most 2 per vertex (ρ = 1 case: Re = 1/2). Hence the whole configuration has maximum degree ≤ 4.

**Derived planar restriction (elementary, exact — mechanical check script filed but NOT yet executed by the runtime):** on the circle of radius r = 1/√2, the chord between two points at central angle θ has length 2r·sin(θ/2); setting this equal to 1 gives sin(θ/2) = 1/√2, θ = π/2. So unit segments are exactly quarter-circle chords; from any point exactly two others (at ±90°) are reachable. Script: `code/check_lenz_planar.py` — sympy, exact, no floats; awaiting a tool_builder/coder run (librarian has no shell).

## What this does to the lenz-roots-of-unity approach

`research/approaches/lenz-roots-of-unity.md` proposed circle/product-of-circles root-of-unity point sets as a 5-forcing family "disjoint from the run's recorded attempts". The sourced statement overturns the premise in the plane:

- the high-density cross-circle mechanism is dimension ≥ 4 only;
- in the plane, any single-circle or two-concentric-circle configuration has Δ ≤ 4, so it cannot contain a 5-critical subgraph (a 5-critical graph has minimum degree ≥ 4 AND, by Brooks' theorem — standard, to be sourced — a graph with Δ ≤ 4 that is not K5 is 4-colourable; K5 is not a unit-distance graph since two unit circles meet in ≤ 2 points; hence χ ≤ 4).

**Status: the circle form of the Lenz approach is a closed direction in the plane** (per the definition of the approach note: "whether this family is already known to cap at 4"). The modular/character techniques in the note survive as *machinery* (eigenvalue bounds for finite abelian Cayley graphs), but not as a new point-set family for forcing 5 — unless a planar analogue of Lenz with more than two concentric circles is proposed, which the same line-intersection argument would need to beat.

## Open ends

- The primary Lenz reference (Lenz's own note, reported via Erdős 1946) is not on disk.
- Brooks' theorem is used in the χ ≤ 4 step; it should be sourced into the library before the step is relied on.

```claim
id: lenz-construction-statement
answers: lenz-construction-planar-scope
statement: The Lenz construction for many unit distances: p = d/2 circles of radius 1/sqrt(2) centred at the origin in pairwise orthogonal 2-planes of R^d; any two points on different circles are at unit distance, giving (p-1)/(2p) n^2 - O(1) unit distances for n points (d = 2p even, d >= 4). Reported in Erdos 1946, formalised by Swanepoel 2008. In the plane (d = 2, p = 1) the construction degenerates to a single circle of radius 1/sqrt(2): unit chords are exactly 90-degree chords, every vertex has at most two unit neighbours, and any single- or two-concentric-circle root-of-unity configuration has maximum degree <= 4, hence cannot force chi = 5 (5-critical graphs of max degree 4 would be 4-regular, impossible by Brooks + K5 not unit-distance).
hypotheses: Euclidean R^d, d = 2p even >= 4 for the cross-circle density statement; plane for the restriction; points on concentric circles of exact radius.
holds-here: true — pins the dimensional scope of the Lenz idea and refutes the circle form of the lenz-roots-of-unity approach in the plane.
status: sourced for the d >= 4 statement (Swanepoel 2008 passages verbatim; Lenz observation as reported in Erdos 1946, which the library holds); derived for the planar restriction (elementary chord geometry; mechanical check script filed but not yet executed).
bearing: closes the lenz-roots-of-unity approach in its circle form in the plane; keeps the modular/character machinery (Cayley eigenvalue bounds) as a technique.
anchor: research/sources/lenz-unit-distances-high-dimensions.md
```

```claim
id: planar-lenz-max-degree-4
statement: Any planar unit-distance graph whose vertices lie on one or two concentric circles (in particular any {zeta_m^i} union {rho zeta_n^j} root-of-unity configuration) has maximum degree at most 4: within-circle unit chords are 90-degree chords on radius-1/sqrt(2) circles (at most 2 neighbours), and cross-circle unit pairs satisfy Re(zeta^i wbar) = rho/2, a line-cap-circle condition with at most 2 solutions per fixed i. A graph of max degree <= 4 that is not K5 is 4-colourable (Brooks 1941), and K5 is not a plane unit-distance graph, so every such configuration is 4-colourable.
hypotheses: plane; vertices on one or two concentric circles; distances exact.
holds-here: true — a theorem-level cap on the proposed construction family.
status: derived (chord geometry + line-circle intersection, both elementary); Brooks step asserted-standard, source not yet in library.
bearing: refutes the circle form of lenz-roots-of-unity as a 5-forcing family; frees the run's construction search to the genuinely planar engines (Minkowski sums, spindles, lattices).
anchor: research/sources/lenz-unit-distances-high-dimensions.md
```