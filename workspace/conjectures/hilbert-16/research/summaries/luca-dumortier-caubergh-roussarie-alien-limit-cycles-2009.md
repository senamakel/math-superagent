# Luca, Dumortier, Caubergh, Roussarie — "Detecting alien limit cycles near a Hamiltonian 2-saddle cycle"

<!-- source: https://users.ugent.be/~stluca/Preprints/A1_2009_LUCA_Alien_Limit_Cycles.pdf | DCDS 25(4):1081–1108 (2009), doi:10.3934/dcds.2009.25.1081 -->
Full text: `research/sources/luca-dumortier-caubergh-roussarie-alien-limit-cycles-2009.full.md`

## What this is

A methodological + example paper on the **tangential/infinitesimal H16** and
the limits of the Abelian-integral method. It constructs a cubic Hamiltonian
**2-saddle cycle** L (saddles at (−1,0),(1,0), connected in the half-plane
{y ≤ 0}) whose unfolding produces an **alien limit cycle** — a limit cycle
NOT controlled by any zero of the associated Abelian integral. This is where
the naive reduction "zeros of the Abelian integral ⟺ limit cycles born from a
Hamiltonian perturbation" fails, even generically.

## The claimed results (each with its hypothesis)

- **Theorem 1**: For the explicit unfolding (X(µ,ε)) of X_H with H given in (3)
  and 2-saddle cycle L, an alien limit cycle exists under generic conditions
  on the Abelian integral and on second derivatives of the transition maps
  along the two saddle connections.
- **Theorem 5**: (saddle normal form) a C^∞ family with a hyperbolic saddle of
  rational hyperbolicity ratio p/q, (p,q)=1, can be put at every order in a
  standard integrable/reduced normal form.
- **Corollary 13 / Theorem 15**: the **first and second derivatives of the
  transition map along a saddle connection** between two hyperbolic saddles
  are given by explicit formulas in terms of the flow and the perturbation; the
  second-derivative term is what produces the alien cycle.
- **Theorem 12 / Diliberto**: transition-map derivative formulas along a
  regular orbit.

## Why it is in the library and what it establishes for THIS run

This is a **primary source on a method that failed at full power**, in the
sense the problem's own method (going after Abelian integrals) is
insufficient: **alien limit cycles are born from a Hamiltonian 2-saddle cycle
even though the Abelian integral has few/new zeros** — the return map's
second-order transition-map terms along the saddle connection, not an extra
Abelian-integral zero, create the cycle. This bears directly on GOAL step 4
("a sharp zero-count for Abelian integrals in one named Hamiltonian family via
Picard–Fuchs") and it **falsifies any claim that bounding Abelian-integral zeros
alone bounds limit cycles born from Hamiltonian perturbations in general** —
the reduction holds only for regular (non-saddle) ovals and fails for
polycycles with saddle connections where alien cycles appear.

## Bound to record / caveats

- The example is CUBIC (degree 3), not quadratic — so it does not directly
  bear on H(2), but it is the canonical demonstration that the Abelian-integral
  route to H(n) upper bounds must carry the alien-cycle caveat for n ≥ 3.
- The article proves existence of the alien cycle, not a sharp uniform bound
  on the number of cycles near L.
- Methodological core (transition-map 1st/2nd derivatives along a saddle
  connection) is exactly the machinery the displacement-function view of the
  problem wants; it complements the held Marín–Villadelprat and RR 2015
  transition-map work with a clean statement in the Hamiltonian-saddle setting.
