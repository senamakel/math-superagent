# Finite-field transfer: prove all UDGs are 4-colourable via a mod-p "liftable colouring"

```approach
idea: Attack the direction the run has not touched — the possibility that
  chi(plane) = 4 — by trying to prove a FINITE restricted-class 4-colouring
  theorem whose proof transfers to the continuum. The mechanism is a change of
  colouring domain: a 4-colouring of a unit-distance graph is a homomorphism
  G → K4, and the question "does a finite graph admit one" is equivalent, over
  a finite field, to the non-existence of a low-degree polynomial certificate.
  The named mathematics: the polynomial-method/Combinatorial Nullstellensatz
  (Alon 1999), and specifically the technique — used for the classical
  Alon–Tarsi and for distance-graph colourings — of proving a graph is
  k-colourable by exhibiting a nonzero coefficient in a colouring polynomial,
  then LIFTING that proof to a geometric statement via the run's own local
  structure lemma.
mechanism: A unit-distance graph's 4-colourability has a well-known equivalent:
  every vertex neighbourhood is 2-colourable (a disjoint union of paths and
  6-cycles — ALREADY certified by this run's `sharp-nbhd-local`), and this
  local 2-colourability is precisely the classical "list-colourability of the
  neighbourhoods" sufficient condition (Reed's theorem / the
  "kernel-perfect" framework: if every neighbourhood induces a bipartite graph,
  the graph is 4-colourable by a greedy argument). If the neighbourhood is a
  single 6-cycle, it is 2-colourable but a 6-cycle carries a C6-obstruction; the
  polynomial method turns "G has no 4-colouring" into a concrete polynomial
  identity that a geometric coincidence (a 60° rotation, i.e. a 6th root of
  unity) would have to satisfy. The line is: prove the colouring polynomial is
  nonzero by evaluating it over a finite field F_p where the 6th-root-of-unity
  structure (the only angles a UDG neighbourhood can close up on) is split, and
  read off a 4-colouring or a forbidden configuration over C. SPECULATIVE,
  stated as such: this is the least certain of the three — no located source
  proves chi ≤ 4 for any infinite plane-distance class by this route, and the
  gap between "every neighbourhood is bipartite" and "the whole graph is
  4-colourable" is exactly the content of the four-colour-type theorem that does
  NOT hold for general non-planar graphs. The certain value is the exact
  negative/positive datum: either the run produces a nontrivial RESTRICTED class
  (e.g. all unit-distance graphs whose every neighbourhood is a PATH, not a
  6-cycle) that is PROVABLY 4-colourable by the polynomial method, or it
  records precisely why the 6-cycle neighbourhood is the sole obstruction —
  which would explain, in a theorem, why the plane is hard.
status: proposed
first-step: Write `code/lib/nbhd_polynomial_colour.py`: (1) for a candidate UDG,
  build the neighbourhood graph N(v) for each vertex from exact coordinates and
  verify it is a disjoint union of paths and 6-cycles (already in
  `sharp_nbhd_cert`); (2) implement the "colour a graph greedily when all
  neighbourhoods are bipartite" bound and find the first unit-distance graph the
  run owns where this greedy bound FAILS to produce a 4-colouring (the 6-cycle
  neighbourhood is the expected culprit — the Moser spindle's two rhombi create
  exactly such cycles); (3) then specialise the colouring polynomial over F_p
  for p ≡ 1 mod 6 (so 6th roots split) and test whether the non-existence of a
  4-colouring becomes a vanishing-coefficient identity that the 6-cycle
  structure contradicts. Report the restricted class that falls, and the
  obstruction that does not.
falsifies: the entire line dies if the "every neighbourhood bipartite ⇒
  4-colourable" heuristic is refuted by a concrete unit-distance graph the run
  owns (the Moser spindle has bipartite neighbourhoods and is 4-colourable, so
  it is consistent; a would-be counterexample is a UDG with bipartite
  neighbourhoods that is NOT 4-colourable, which would be a candidate
  5-chromatic graph — exactly the deliverable). It also dies if the
  polynomial-method evaluation over F_p produces no information beyond what the
  run's complete SAT oracle already gives (i.e. it is a re-verifier, the same
  failure that closed the Nullstellensatz line — the distinguishing claim to
  defend is that it PROVES a restricted class, not that it re-checks a graph).
precedent: Alon 1999 Combinatorial Nullstellensatz (the coefficient-vanishing
  criterion); the polynomial method in graph colouring (the colouring
  polynomial, Alon–Tarsi — but here the DIRECTION is colourability, the
  direction the closed alon-tarsi line got backwards); Reed's
  "omega, Delta, chi" conjecture and the bipartite-neighbourhood / greedy
  colouring bounds (Brélaz/DSATUR-type; Brooks' theorem for Delta ≤ 5); the
  run's own `sharp-nbhd-local` (checked: neighbourhoods are paths+6-cycles,
  hence bipartite). NULL precedent for a mod-p transfer proving a restricted
  4-colouring theorem for a plane-distance class — research must check; the
  classical results are about list-colouring and greedy bounds, not about the
  finite-field evaluation of the colouring polynomial.
```
