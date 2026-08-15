# Gain graphs over Z/6 — the coordinate-native algebra of the 60° chord structure

```approach
idea: Encode a unit-distance graph's 60°-chord structure as a gain graph (group-labelled graph) over the cyclic group Z/6 in Zaslavsky's sense, and attack the chromatic number through the gain/signed chromatic number and the associated frame matroid — a coordinate-native algebra that makes rotational rigidity explicit, where the run's bar-joint (Henneberg) rigidity only sees incidences.
mechanism: The run's own local lemma says two neighbours of a vertex are adjacent iff their directions differ by exactly 60°, so every unit equilateral triangle carries a Z/6 relation among its three edge directions (each direction is a 6th-root-of-unity rotation of the next). Labelling each edge by its direction class in Z/6 — coherent within every triangle — turns a UDG into a gain graph over Z/6: a finite, exact, algebraic relabelling of the angular data, independent of the coordinate magnitudes. Zaslavsky's theory of gain/biased graphs then supplies (i) a gain chromatic number and signed chromatic polynomial as an exact certificate, and (ii) the frame matroid of the gain graph, which captures triangle/rotational rigidity that Minkowski sums and bar-joint rigidity accumulate only implicitly. The question "does a Z/6 gain graph with gain-chromatic number ≥ 6 realise as a planar point set" becomes a finite algebraic search over gain graphs, not over point sets.
status: refuted
killed-by: z6-labelling-does-not-globalise-and-collapses-where-it-does — a unit-distance edge's direction is an arbitrary angle, not a multiple of 60°, so a *global* Z/6 direction labelling does not exist for the base case (the Moser spindle's two rhombi differ by rotation arccos(5/6) ≈ 33.6°, not a 60° multiple); the coherent Z/6 structure lives only on the triangle subcomplex, not on all edges. And exactly where the triangle-complex labelling is coherent (balanced cycles), Zaslavsky's theory gives gain-chromatic number = ordinary chromatic number, so the invariant collapses at its own falsifier. The frame matroid remains a real object but supplies no chromatic lever the run's circular-chromatic line (already refuted as "no shortcut") did not already close. Superseded by exact-ceiling-size-bound.
first-step: For the Moser spindle (coordinates already certified exactly by the run), extract the triangle complex: list all unit equilateral triangles, assign each edge a direction class in Z/6 consistent within each triangle, and record where the labelling globalises and where it only holds per-triangle. Then compute the gain-chromatic number of the resulting gain graph by an exact group-colouring SAT encoding and calibrate against the known chi = 4.
precedent: unchecked
speculation: Whether the gain-chromatic number can exceed the ordinary chromatic number at the run's sizes, and whether the frame-matroid rank distinguishes richer constructions, is open. The certain value is a new exact invariant and a new finite search object.
```

## Why this is not a closed line

- Not `rigidity-matroid-henneberg-construction` (adopted): that is the **bar-joint** rigidity matroid of the incidence graph; this is the **frame matroid** of a Z/6 gain graph, which sees the 60° angle relations that bar-joint rigidity does not.
- Not `wl-color-type-forced-pair-algebra` (refuted): WL is a graph-colouring refinement; a gain graph over Z/6 is a genuine algebraic object with its own chromatic theory (Zaslavsky), not a fixed-dimension refinement.
- Not `circular-chromatic-sharpened-bound` (refuted): that relaxed the *colour target* to circulants; this relabels the *edge structure* by a group and keeps the colour target.

Named mathematics: gain graphs, biased graphs (Zaslavsky 1982), signed/group chromatic number, the frame matroid.

## What would falsify it

If the Z/6 gain graph of the Moser spindle has gain-chromatic number < 4, the encoding is not faithful for lower bounds and the line dies there. If gain-chromatic number always equals ordinary chromatic number on every constructed UDG, the invariant is a relabelling and not a lever.
