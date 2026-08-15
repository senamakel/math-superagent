# Approach: unit circle of a number field as P¹(K) — an algebraic construction engine

```approach
idea: Re-parametrise the problem over the projective line. The unit circle over a
  number field K is exactly P¹(K) via the standard rational parametrisation
  p(t) = ((1−t²)/(1+t²), 2t/(1+t²)). Every unit *step* in a unit-distance graph is
  a parameter t ∈ K, every vertex is a sum of such steps, and the chord/edge
  condition |p(t₁)−p(t₂)|² = 1 is a *polynomial* in t₁,t₂. Rigidity — the
  coincidences that make unit distances abundant — becomes a system of polynomial
  equations in finitely many parameters, solvable symbolically, instead of a
  search over points in the plane.
mechanism: The run's construction engine (Minkowski sums, spindling/rotations)
  treats points as pairs of coordinates and rotates by angles. But a rotation by
  cos θ = c, sin θ = s is nothing but a unit vector, hence a single parameter t.
  Concretely, the Moser rotation (c=5/6, s=√11/6) is t = 1/√11 ∈ Q(√11): solving
  (1−t²)/(1+t²) = 5/6 gives 11t² = 1. So the entire 7-vertex construction collapses
  to a few rational parameters and the edge conditions are polynomial identities
  in them. This is a genuinely different representation: a unit-distance graph on
  an algebraic point set is a finite set of P¹(K)-parameters with the pairwise
  "sum of unit steps closes / lands at unit distance" conditions as polynomial
  systems, and new constructions = new polynomial systems to solve exactly. The
  field's arithmetic controls the supply of unit vectors: over Q(√−3) the unit
  circle has only the six units (triangular lattice, rigid-but-limited); over Q(i)
  or real quadratic fields it has infinitely many K-points (rich directions), so
  the field choice is itself the rigidity lever. This rephrases "find a rigid UDG"
  as "find a small solvable polynomial system over a number field whose solution
  has χ ≥ 5" — a symbolic-optimisation problem, not a continuum search.
status: refuted
killed-by: faithful but not a new line — a bijective relabelling of the coordinate
  space the run already owns; its "field choice = rigidity lever" claim is refuted
  (P¹(K) is infinite over every number field; the finite direction set is the ring
  of integers Z[ω]^×, already the run's Eisenstein-lattice machinery).
first-step: derive the chord condition p(t₁)·p(t₂) = 1/2 as the explicit
  polynomial 2[(1−t₁²)(1−t₂²)+4t₁t₂] = (1+t₁²)(1+t₂²), which clears to
  t₁²t₂² − 3t₁² − 3t₂² + 8t₁t₂ + 1 = 0 (check: t₁=0, t₂=1/√3 gives the 60°
  neighbour and satisfies it; t₁=t₂ gives (t²+1)²=0, correctly never an edge);
  reconstruct the Moser
  spindle purely in t-parameters over Q(√3,√11) and certify its 11 edges as these
  polynomial identities (reproducing calibration by the new route); then express
  the spindling/rotation step as a substitution t ↦ (t+r)/(1−rt) (rotation by a
  unit step) and enumerate the next tier of parameter systems.
falsifies: a rotation/unit step that is not representable by some t ∈ K — but
  every unit vector with coordinates in K is hit by the parametrisation (t = s/(1+c)
  whenever c ≠ −1, and t = ∞ for the antipode), so within a fixed field the
  parametrisation is complete; the real failure mode is that the polynomial systems
  defining 5-chromatic candidates are too hard or have no solutions in accessible
  fields, a precise and reportable obstruction.
cost: polynomial in the number of parameters to *set up*; solving is symbolic
  (Groebner/resultants over Q and small extensions), whose cost grows with the
  number of parameters of the construction, not with any bound in the statement.
  No floating point, no exponential colouring search at construction time.
precedent:
  - standard rational parametrisation of the unit circle (conic x^2+y^2=1 is rational, has point (1,0)); inverse t = y/(1+x); standard algebraic-geometry fact, valid over any field of char != 2
  - chord/edge polynomial: VERIFIED symbolically this run (see verification section); Moser t = 1/sqrt(11) reproduces cos=5/6, sin=sqrt(11)/6
  - Maehara 1991 (in library): algebraic coordinates are the right field (id maehara-algebraic-rigid-distances)
  - P^1(K) conic parametrisation: any elliptic-curves/conics reference (Silverman-style); the conic has infinitely many K-points over every number field
```

## Verification status — I ran the algebra, and corrected one claim

This is the one candidate whose *mechanism* needed an arithmetic audit, and I
both audited the chord polynomial and **found and corrected a substantive error**:

**Chord condition (verified).** `p(t₁)·p(t₂) = ½` does clear to
`t₁²t₂² − 3t₁² − 3t₂² + 8t₁t₂ + 1 = 0`. Cross-checks: `t₁=0, t₂=1/√3` (the 60°
neighbour, |p(0)−p(1/√3)|² = 1) makes the polynomial zero; `t₁=t₂` gives
`(t²+1)² ≠ 0`, i.e. never an edge (no self-loop) ✓. The Moser rotation,
`c=5/6, s=√11/6`, corresponds to `t = 1/√11` ✓. So the *corrected* polynomial
form is right (the inventor's own correction was correct), and the Moser
reconstruction in t-space is a valid, cheap test of the engine. This is a
sourced+computed claim: the polynomial is a verified computation of this run
(and a direct symbolic derivation from p(t₁)·p(t₂) = ½).

**Correction to the "six unit directions" claim (the speculative part that was
wrong).** The approach file claims that over Q(√−3) "the unit circle has only the
six units (triangular lattice, rigid-but-limited); over Q(i) or real quadratic
fields it has infinitely many K-points, so the field choice is itself the
rigidity lever." **This conflates field points with ring units.** The six-element
*unit group* Z[ω]^× = {±1, ±ω, ±(1+ω)} is a statement about the **ring of
integers**, not about the field. Over *every* number field K, the conic
x²+y²=1 is rational (it has the K-point (1,0)) and hence has **infinitely many**
K-points — P¹(K) is infinite. So in a parametrised construction over K, the field
choice does **not** restrict the available unit directions at all: every field
gives a full P¹(K) of circle points, so there are always plenty of K-rational
unit steps (indeed infinitely many even over Q). The "rigidity lever" described
in the mechanism is therefore not a field-lever at all. The place where a finite
direction set genuinely bites is *lattice / integral* construction (points in a
ring of integers Z[ω], fewer embeddings, denser coincidences) — the `einstein-
lattice-unit-distance` structure. That is a real lever, but it is about the ring,
not about K-points of the circle.

This error matters because the mechanism's advertised pay-off — "field choice is
the rigidity lever" — is partly void; but the *core* mechanism survives: the
parametrisation is a faithful, complete encoding of unit steps (every unit vector
with coordinates in K is hit, t = y/(1+x) or t = ∞), and it genuinely turns
constructions into polynomial systems over the coordinate field. The Moser
spindle collapsing to a handful of t-parameters is a real, checkable claim.

## Value risk — stated honestly

The parametrisation is standard and faithful; the conversion buys a *different
representation* of the same construction space. What it does **not** buy is a new
graph: any point set with algebraic coordinates has a t-parameterisation, so no
new unit-distance graph is created — the value is purely that the edge/coincidence
conditions become *polynomial identities* amenable to symbolic elimination (and
the field arithmetic, e.g. which fields give many coincidences under the chosen
construction, is a genuine design lever). Whether the polynomial systems defining
5-chromatic candidates are small enough to solve symbolically is the real, and
unanswered, question — and the cheap Moser-reconstruction test in the first step
decides it.

**Verdict: grounded** as an *encoding* (correct, faithful, cheap to build, and
the polynomial/field machinery is standard), **with a stated correction**: the
"finite directions over Q(√−3)" rigidity-lever claim is wrong for field points,
and the true generator of rigidity is lattice/ring-of-integers structure, not the
P¹-parametrisation. The engine is worth one cheap test (reconstruct the spindle
in t-space), but the run should not expect it to produce new graphs that the
coordinate/Minkowski machinery cannot.

## What would refute it (killed-by)

The genuine failure mode is value-shaped: the polynomial systems describing
5-chromatic candidates are too hard or have no solutions in accessible fields
(i.e. the Moser-reconstruction does not collapse to a handful of t-identities),
which would mean the representation is wrong for this problem and should be
dropped; or it reproduces exactly the graphs the run already has (the coordinate
engine) and buys nothing new. Note the claimed complement: it does NOT fail by
missing unit steps — the parametrisation is complete (bijection P¹(K) → circle),
so irreducibility of the polynomial systems for 5-chromatic candidates is the
only real obstruction.

## Killed-by (converging decision)

The parametrisation is faithful, but faithful is not useful here: it is a bijective
relabelling of exactly the coordinate construction space the run already owns, so it
produces no graph the coordinate/Minkowski engine cannot, and its advertised payoff —
"field choice is the rigidity lever" — is refuted. Over every number field K the conic
x²+y²=1 is rational (it has the K-point (1,0)) and P¹(K) is infinite, so field choice
does not restrict unit directions at all; the finite direction set lives in the *ring
of integers* Z[ω]^×, which is already the run's Eisenstein-lattice machinery
(einstein-lattice-unit-distance). As a line of attack it is a re-encoding, not a new
idea; its one correct residue — integral structure is the rigidity lever — is inherited
by the adopted theta/Hoffman approach, which applies exactly there.
