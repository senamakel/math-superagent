# Survey: coloring parameters of distance graphs (Liu 2008)

**Subject:** The survey-tier anchor of the run's **adopted**
`flat-torus-periodic-6col` approach on the upper-bound side. It records that the
plane unit-distance colouring problem is the open 4<=chi<=7 problem, and that
periodic/integral distance-graph colouring is a named, studied technique — the
context the approach operates in.

**Source (primary, retrieved via server-side `read_sources`):**
- Daphne Der-Fen Liu, *From rainbow to the lonely runner: a survey on coloring
  parameters of distance graphs*, Taiwanese J. Math. 12 (2008),
  DOI 10.11650/twjm/1500404981.
  URL: https://doi.org/10.11650/twjm/1500404981

## What it establishes (from the survey's text)

- **Periodic colourings of distance graphs.** For a distance graph G(Z,D) on
  the integers with distance set D, a D-set / colouring is *periodic* when its
  defining sequence is periodic (exists k with delta_i = delta_{i+k} for all i).
  Periodic colourings yield strong, computable bounds: for the fractional
  chromatic number chi_f(Z,D), the ratio of total weight to period size gives a
  lower bound that has been proved to be the exact value in known cases (Liu and
  Zhu). For vertex-transitive circulant graphs, chi_f(G) = |V|/alpha(G), giving
  upper bounds.
- **The plane unit-distance colouring problem.** The survey frames the plane
  unit-distance colouring (colouring all points of the plane so no two at
  distance 1 share a colour) as the open Hadwiger–Nelson problem whose value
  lies between 4 and 7, and connects the distance-graph (lattice-point) colouring
  literature to it: colouring parameters of distance graphs X(Z^2, D) and
  integer distance graphs inform lower and upper bounds for the plane
  unit-distance colouring. **No 6-colouring of the plane and no proof that one
  exists/impossible is established here** — the exact plane value remains open.

## Why it matters here

This is the survey tier that positions the flat-torus approach: the search for a
periodic 6-colouring of the plane is a named technique (periodic distance-graph
colourings), and the survey confirms the plane bound sits at the open
4<=chi<=7. It also confirms the honest caveat already recorded in the approach
note: the periodic-attainment theorems (Barajas–Serra; Liu–Zhu fractional
results) are proved for *integer/lattice* distance graphs, not directly for the
continuous plane — so the flat-torus approach's discrete-spine layer is
justified by these, but whether a periodic plane colouring beats 7 is not
settled anywhere in this survey.

## Basis and status

- Survey content: sourced from the paper's text via `read_sources`.
- Claims it reports (periodic colouring bounds for chi_f; plane problem open)
  are the survey's own; not re-derived here.

## Claim block

```claim
id: liu-distance-graph-survey
statement: For integer distance graphs G(Z,D), periodic colourings give strong
  bounds on the fractional chromatic number (periodic-weight lower bounds are
  exact in known cases; circulant/vertex-transitive graphs have chi_f = |V|/alpha),
  and the plane unit-distance colouring problem (colour all plane points so no
  two at distance 1 share a colour) is the open Hadwiger–Nelson problem with
  4 <= chi <= 7, related to but not settled by the lattice-point distance-graph
  theory.
hypotheses: distance graphs on Z (integer distance set D); the plane problem as
  its own open object.
holds-here: YES as context — the periodic-colouring technique is the adopted
  flat-torus approach's mechanism, and the survey confirms the plane bound is
  open between 4 and 7.
status: asserted-by-source (Liu survey 2008, Taiwanese J. Math.).
bearing: survey-tier anchor of the adopted flat-torus-periodic-6col approach on
  the upper-bound side; confirms periodic colouring is a named technique and the
  plane value is open.
anchor: research/sources/liu-2008-distance-graph-survey.md
falsifies: nothing — a survey; it records the open problem rather than settling
  it. The flat-torus approach's value (whether a periodic 6-colouring beats 7)
  is not decided by this source.
```
