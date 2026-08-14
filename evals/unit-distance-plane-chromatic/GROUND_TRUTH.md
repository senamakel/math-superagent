# Ground truth — unit-distance-plane-chromatic

**This file must never enter the container.** It lives at the repository root,
outside `workspace/`, which is the only tree bind-mounted at `/workspace`. It is
read by `scripts/eval-report` on the host and by nothing else.

## What this problem really is

**The Hadwiger–Nelson problem**: the chromatic number of the plane, posed by
Edward Nelson in 1950. The bounds `4 <= chi <= 7` were established almost
immediately — the lower bound by the **Moser spindle** (Leo and William Moser,
1961), the seven-vertex graph the seed calls "two rhombi sharing a vertex", and
the upper bound by John Isbell's hexagonal tiling.

The gap stood for 68 years.

## The solution being withheld

**Aubrey D. N. J. de Grey, April 2018**, "The chromatic number of the plane is at
least 5", *Geombinatorics* 28, arXiv:1804.02385.

De Grey exhibited a unit-distance graph on **1581 vertices** that is not
`4`-colourable, proving `chi >= 5`. The construction:

- Start from `H`, a `121`-vertex unit-distance graph: the vertices of a
  triangular lattice of unit edge, taken as a Minkowski sum of small pieces,
  intersected with a disc.
- Build `M`, a `1345`-vertex graph, as a Minkowski sum of `H` with a rotated
  copy, chosen so that in any `4`-colouring some vertex pattern is forced.
- Assemble copies of `M` and `H` under rotations by angles `arcsin(1/(2*sqrt(3)))`
  and similar, so that the forced patterns become mutually incompatible.
- Non-`4`-colourability verified by SAT.

Coordinates live in `Q(sqrt(3), sqrt(11))` and related fields; **the whole proof
is a finite verification** and was independently confirmed within days.

Follow-up: **Polymath16** (2018–2021) reduced the vertex count to **509**
(Parts, Heule and others), and improved the lower bound on the size of the
smallest `5`-chromatic unit-distance graph. The upper bound of `7` has **never**
been improved, and `chi(G)` is still not determined — it is now known only that
`5 <= chi <= 7`.

## Why this problem is in the calibration set

It is the one where **recall does not help**. A model that remembers "de Grey
found a 1581-vertex graph in 2018" has been told nothing usable: the result is
the vertex set, and the vertex set is not memorised. To succeed the harness must
actually build exact-arithmetic machinery, actually wire a SAT oracle, and
actually search a structured construction space. Success is machine-checkable
end to end, so scoring is objective rather than a judgement about proof quality.

It is also the problem where the seed's own honesty is load-bearing: the seed
deliberately points at Minkowski sums and rotations, because that *was* the
known toolkit before 2018 and withholding it would make the time capsule
dishonest rather than harder. The gap between "has the toolkit" and "found the
graph" is exactly the capability being measured.

## De-naming assessment

**Weak.** The statement is self-identifying — any competent model recognises
"chromatic number of the unit-distance graph on `R^2`" immediately, and the
seven-vertex graph is recognisable from its description even unnamed. De-naming
here removes the attribution hook and the searchable string, nothing more.

Attribution therefore rests on the **leakage audit**, not on the de-naming.
Specifically: watch for the run naming `1581`, `1345`, `121`, `509`, `Q(sqrt(3),
sqrt(11))`, or the specific rotation angles **before** deriving them. Any of
those numbers appearing without a computation that produced it is recall, not
progress, and must be scored as a negative marker.

## Falsifiable checks for the audit

If the run claims `chi >= 5`, the claim is only credible if the workspace
contains:

- an explicit vertex list in exact coordinates,
- an edge certification that is symbolic, not tolerance-based,
- a SAT UNSAT result for `4` colours from an encoding calibrated on the
  `7`-vertex graph,
- and a re-verification not sharing arithmetic with the construction.

Absent any of those, score it as an unverified claim regardless of how
convincing the prose is. A floating-point pipeline produces false positives
here reliably, so a `5`-chromatic claim without exact arithmetic is *expected*
to be wrong, not merely unproven.
