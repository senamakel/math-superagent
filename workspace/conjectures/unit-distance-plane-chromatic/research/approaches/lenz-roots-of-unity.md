# Lenz-type distance graphs from cyclotomic rings and roots of unity

```approach
idea: Construct unit-distance graphs whose vertex set is a finite subgroup of a
product of unit circles (points of the form zeta_m^i or sums zeta_m^i + rho
zeta_n^j for roots of unity, all coordinates in cyclotomic fields Q(zeta_m)),
rather than Minkowski sums of a spindle. The unit-distance graph of such a set
is a vertex-transitive Cayley graph of a finite abelian group, and its edges are
governed by the trigonometric identity |zeta^i - zeta^j| = 1 <=> the difference
of exponents hits a specific residue class mod m. Lenz's classical constructions
(1951) exploited exactly this: distance graphs on root-of-unity point sets whose
chromatic number is forced by modular arithmetic, quadratic-residue (Paley-type)
arguments and Gauss sums, with no reliance on accumulated rigidity of spindles.
mechanism: The change of representation is from "accumulated rigidity of a
Minkowski/spindle closure" to "number-theoretic forcing in a cyclotomic ring".
For H a finite subgroup of (R/Z)^2 the unit-distance Cayley graph has connection
set S = {h : some lift of h has Euclidean norm 1}, a finite exactly-computable
subset of Q(zeta_m); its chromatic number and independence number are then
functions of the exponent structure (circulant/Paley graphs over F_p, tensor
products of circulants), where eigenvalue bounds and explicit quadratic-residue
arguments can push chi up. This is a construction family disjoint from the run's
recorded attempts (Minkowski powers stayed chi=4, lattice patches stayed
chi<=3): the seeds are torsion subgroups of high order, not sums of the 7-vertex
spindle, and the forcing is modular rather than geometric.
status: proposed
first-step: For small exact parameters m, n and radii rho chosen so that
cross-circle pairs land at unit distance exactly, construct the unit-distance
graph on {zeta_m^i} union {rho zeta_n^j} (and on the full subgroup
<zeta_m, zeta_n> of the torus) in Q(zeta_lcm) with exact arithmetic, compute its
edge set, and run the calibrated complete colouring test to find whether any
reaches chi >= 5; simultaneously pin down in the literature what Lenz's theorem
actually guarantees and which root-of-unity families are already known to be
4-colourable.
```

## Established vs speculation

- **Established (to be sourced by research):** the identity
  `|zeta_m^i - zeta_m^j|^2 = 2 - 2 cos(2 pi (i-j)/m)` is elementary and gives
  unit edges exactly when `i - j` lies in the residues solving
  `cos(2 pi t/m) = 1/2`, i.e. `t = +- m/6` (requires `6 | m`). Cayley graphs of
  finite abelian groups have eigenvalues given by character sums of the
  connection set — standard and exactly computable in cyclotomic fields.
- **Speculation:** that a suitable Lenz/Paley-type root-of-unity configuration
  attains chi >= 5. I am naming "Lenz" from memory and have not here stated the
  exact theorem; research must supply the precise statement and confirm whether
  this family is already known to cap at 4 before any computation is built on
  it. The value of the proposal is the *family and the forcing mechanism*, not a
  citation I have not verified.
