# Exact certification of algebraic coordinate fields of unit-distance graphs

**Subject:** The exact-arithmetic verification machinery the run's oracle must
implement — this paper is the technique tier for how to certify that a given
unit-distance graph's coordinates lie in a stated number field and all edges
are exactly unit. Answers the run's exact-coordinate backbone question with a
concrete, published method.

## Source
- *Exact certification of the coordinate fields of the triangle-free
  Exoo–Ismailescu unit-distance graphs EI17 and EI19 (HoG 51375, 51376): a
  solvable–non-solvable dichotomy (origami vs. S20) and the Laman-number
  conjecture*, arXiv:2607.19995. Retrieved via `read_sources` (server-side).

## What it establishes (the technique, not a Hadwiger–Nelson answer)

- Coordinates of a **faithful** realization of a unit-distance graph are
  **algebraic** — they solve a polynomial system with rational coefficients
  (each edge `|p(u) - p(v)|^2 = 1` is quadratic with rational data). Confirms
  the Maehara theorem's forward direction in a concrete setting.
- The paper gives an **explicit, constructive, algebraic-coordinate
  certificate**: it reduces the realisation problem to a triangular chain of
  equations (linear and unit-distance constraints), enabling **exact symbolic
  verification** — no numeric approximation.
- Concrete certificate: for EI17 the coordinates lie in a number field of
  degree 20 with Galois group S20, and the realisation is uniquely determined
  by a small set of unit-distance and radical-axis constraints.
- **Verification runs in O(n^2)** using precise (exact/symbolic) arithmetic:
  check planarity (rank of coordinate matrix = 2 via SVD with two singular
  values exceeding tolerance), `e_max = max | |p(u)-p(v)| - 1 |` over edges
  (the exact unit-distance check), minimal pairwise separation > 0, and no
  extra unit distance among non-edges.
- Situates this within the broader `exists-R`-universality framework (Mnëv,
  Kapovich–Millson): realising arbitrary algebraic distances via Kempe linkages
  (antiparallelogram, reverser, n-fan) — the constructive converse of Maehara.

## Why it matters here

- This is the **exact-arithmetic discipline of GOAL.md made concrete**: a
  published, peer-style method for certifying "every edge is exactly unit, no
  spurious edge, coordinates in field F" that is the run's oracle requirement.
- The O(n^2) exact verification (planarity + exact unit-distance + separation +
  no-extra-unit-distance) is precisely what the run's `unit_graph(points)`
  certifier should mirror, using symbolic `|x-y|^2 = 1` checks over its field
  (Q(sqrt3, sqrt11, sqrt33)).
- It confirms that **floating-point is never legitimate**: the coordinates are
  algebraic by Maehara, the verification is exact by construction, and a
  tolerance-based check would risk spurious edges — the exact trap GOAL.md names.

## Basis and status
- Method, algebraic-coordinate certificate, and exact O(n^2) verification
  procedure = sourced (retrieved verbatim).
- Not re-run here (the target graphs EI17/EI19 are not this run's; the run's
  own exact oracle is locally verified on the 7-vertex Moser spindle).

## Claim block
```claim
id: exact-coordinate-certification
statement: A faithful unit-distance graph realisation has algebraic coordinates
  (solutions of a rational-coefficient polynomial system with each edge a
  quadratic), and its exactness is certified by an O(n^2) procedure: rank-2
  planarity check, e_max = max | |p(u)-p(v)| - 1 | = 0 over edges (exact),
  positive minimum separation, and no extra unit distance among non-edges —
  all in exact arithmetic, never floating-point.
hypotheses: finite unit-distance graph in the plane with a faithful (rank-2,
  no-extra-unit-distance) realisation; coordinates algebraic.
holds-here: YES — exactly the run's oracle discipline: the edge certifier must
  prove |x-y|^2 = 1 symbolically and must certify no spurious/missed edge,
  which is what the run's 7-vertex calibration checks.
status: asserted-by-source (arXiv 2607.19995 method; it is the run's own oracle
  design giving a published analogue).
bearing: the blueprint for the unit_graph(points) edge-certifier: exact
  algebraic-coordinate verification with the e_max=0 and no-extra-edge checks,
  matching the run's calibrated oracle.
anchor: research/sources/exact-coordinate-certification-unit-distance.md
falsifies: a faithful unit-distance realisation with a transcendental
  coordinate — would contradict Maehara's theorem; none known.
```
