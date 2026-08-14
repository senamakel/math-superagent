# Flat torus quotients: the plane as a Cayley graph of rank-2 lattices

```approach
idea: Replace the plane by its compact flat quotients. For every rank-2 lattice
L the flat torus T_L = R^2/L carries an infinite unit-distance graph whose
vertices are all cosets and whose edges are pairs at torus distance exactly 1.
A colouring of T_L lifts (via the projection R^2 -> T_L) to an L-periodic
colouring of the plane, so chi(plane) <= chi(T_L) for every lattice L — the
hexagonal 7-colouring is exactly such a lift. Attacking chi <= 6 therefore
becomes: find a flat torus with a 6-colouring of positive margin. Conversely
every finite plane unit-distance graph embeds as a subgraph of
some T_L (choose L generically avoiding all point differences and all
difference-minus-unit vectors), so finite quotient Cayley graphs
Cay(T_L/(mL), S_L) are a complete ambient in which to hunt dense
vertex-transitive unit-distance graphs. The problem is thereby re-cast as the
chromatic numbers of Cayley graphs of rank-2 abelian groups, where character
theory gives exact eigenvalue bounds.
mechanism: The projection R^2 -> T_L is a graph homomorphism from the plane's
unit-distance graph onto the torus unit-distance graph, so colourings descend
one way and lift the other. This converts "is there a 6-colouring of the
continuum plane" into "does some flat torus admit a 6-colouring with a
certified margin", which is a search over a 4-real-parameter lattice family
rather than over colouring schemes. On the finite side, a quotient by a
sublattice m L gives a finite vertex-transitive Cayley graph whose connection
set S_L = {cosets containing a unit vector} is exactly computable in the
coordinate field; its chromatic number and independence number are attackable
by Fourier/character methods (Hoffman bound, Lovasz theta) in exact arithmetic,
turning a blind SAT search into a rank-2 lattice search with a polynomial-time
screen.
status: proposed
first-step: For candidate lattices L (hexagonal, square, and oblique with exact
basis vectors), build the exact connection set S_L and the finite Cayley graph
Cay(T_L/(mL), S_L) for growing m in exact field arithmetic, and compute chi and
an exact eigenvalue independence bound for each. In parallel, establish from the
literature whether a periodic 6-colouring is already known to be impossible, so
this search is not run against a closed door.
```

## Established vs speculation

- **Established (standard, to be sourced/checked by research):** the projection
  lift `colouring of T_L -> L-periodic colouring of R^2` is valid for every
  lattice, giving `chi(plane) <= chi(T_L)`; the hexagonal 7-colouring is a
  periodic lift. Also that every finite plane UDG embeds as a subgraph of some
  flat torus (generic lattice avoids finitely many circles).
- **Speculation:** that the torus search surfaces a *new* upper-bound idea. The
  7-colouring is the periodic optimum for hexagonal structure, but non-hexagonal
  torus colourings are far less explored than tilings, and the search is over a
  different object (a quotient graph, not a polygon tiling).
- **Boundary to respect:** any *measurable* (hence periodic) colouring of the
  plane needs >= 5 colours (recorded in the library, `measurable-variant-
  separate`). This approach sits strictly between the measurable variant and the
  full problem; it does not import the measurable hypothesis, it searches within
  the periodic class for a *6*-colouring, which the measurable bound does not
  forbid.
