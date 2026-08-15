# Lower bound via the spindle closure

Skeleton of a reduction of `chi(G) >= 5` to three lemmas: the De Bruijn–Erdős
lift, the spindling closure lemma, and the existence of a 4-chromatic
unit-distance graph with a monochromatic-forced pair. The first is standard
theory, the second is provable structure (and its base case is the 7-vertex
Moser spindle), and the third is where the decades of difficulty live — but it
is a *finite* question per candidate pair, which is exactly what the SAT oracle
decides.

```skeleton
goal: chi(G) >= 5 for G the unit-distance graph on R^2 (vertices all points, x ~ y iff |x-y| = 1) — equivalently a finite unit-distance graph that is not 4-colourable, the machine-checkable deliverable in GOAL.md.
implies: G3 supplies H with chi(H)=4 and vertices u,v, d=|u-v|>=1/2, monochromatic in every proper 4-colouring. G2 builds S = H ∪ rho_theta(H) with the two copies sharing u, theta chosen so 2d sin(theta/2)=1; then rho_theta(v) is at distance exactly 1 from v, S is a unit-distance graph (rotation is an isometry, and theta has algebraic coordinates in a finite extension of the field of H). Any 4-colouring of S restricts to 4-colourings of both copies, and G3 forces c(v)=c(u) in copy one and c(rho_theta(v))=c(u) in copy two, hence c(v)=c(rho_theta(v)); but v ~ rho_theta(v), a contradiction. So S is not 4-colourable, chi(S)>=5, and G1 lifts the finite subgraph S to chi(G)>=5.
status: sketched
rests-on: none
```

```gap
id: G-de-bruijn-erdos-reduction
lemma: chi(G) equals the supremum of chi(H) over finite subgraphs H of the unit-distance graph on R^2; in particular chi(G) >= 5 iff some finite unit-distance graph has chi >= 5. (The exact compactness/choice hypothesis must be recorded, not assumed.)
status: open
next: librarian/research fetch the de Bruijn–Erdős (1951) primary source and have scholar write a claim block with the exact hypotheses and holds-here: true for the unit-distance graph on R^2; once sourced, theorem_prover can be handed the finite->infinite direction as a first-order statement.
```

```gap
id: G-spindling-closure
lemma: If H is a unit-distance graph with chi(H)=4 and vertices u,v, u≠v, d=|u-v|>=1/2, such that every proper 4-colouring of H has c(u)=c(v), then S = H ∪ rho_theta(H) (two copies identified at u, rho_theta a rotation about u with 2d sin(theta/2)=1) is a unit-distance graph with chi(S)>=5, and its coordinates stay in a finite algebraic extension of the field of H's coordinates.
status: open
next: symbolic_math verify the k=3 base case exactly — the diamond D (two unit equilateral triangles on a common edge; tips p,q at distance sqrt(3) are forced equal in every 3-colouring) spindled about p with theta = 2 arcsin(1/(2 sqrt(3))) produces the 7-vertex Moser spindle; certify all 11 edges symbolically and chi=4 by the SAT oracle. Then lean_prover/theorem_prover formalise the general step |v - rho_theta(v)| = 2d sin(theta/2), so theta = 2 arcsin(1/(2d)) works iff d >= 1/2.
```

```gap
id: G-forced-pair-exists
lemma: There exists a 4-chromatic unit-distance graph H and two vertices u,v with |u-v|>=1/2 that receive the same colour in every proper 4-colouring of H.
status: open
next: sat_solver — after the oracle is calibrated on the 7-vertex graph, run the forced-pair test on the Moser spindle: for each pair (u,v) with |u-v|>=1/2, add edge uv and ask the 4-colouring oracle; UNSAT certifies (u,v) is monochromatic in every 4-colouring. If no pair of the 7-vertex graph works, run the same test over Minkowski sums H+H and iterated spindles — a finite SAT query per pair each time.
```

## Attack surface

- **G3 is the crux and may be false for the Moser spindle.** The forced-pair
  test above is the cheap refutation: if every pair of the 7-vertex graph comes
  back SAT, it has no monochromatic-forced pair, and the route is dead unless a
  richer base graph (Minkowski sums, iterated spindles) supplies one. The test
  direction is: `H + edge(u,v)` is not 4-colourable iff (u,v) is forced equal
  in every 4-colouring — a 4-colouring with c(u)≠c(v) is exactly a proper
  4-colouring of `H + edge(u,v)`.
- **G2's hypothesis d >= 1/2 is a boundary, not a convenience.** A forced pair
  at distance < 1/2 cannot be brought to distance 1 by the shared-vertex
  rotation, and the lemma does not cover it; the hypothesis must not be quietly
  dropped to make a construction appear.
- **G1 must not be imported from a measurable-colour-class variant.** That
  variant has its own, larger lower bounds and a different compactness story.
  The reduction needed here is for the unrestricted colouring of all points.
- The inference uses that rho_theta fixes the shared vertex u (rotation about
  u), so the two copies are genuinely isomorphic subgraphs and the
  forced-equal property transfers to rho_theta(v) in copy two.

The upper-bound direction (a 6-colouring of the plane) is a separate skeleton
and is not covered here.
