# Approach: discharging on a minimal 5-chromatic unit-distance graph

```approach
idea: Attack the 4-colourable direction (and the size bound) by the discharging
  method applied to a hypothetical vertex-critical unit-distance graph H with
  chi(H)=5 and chi(H-v)=4. Criticality forces min degree >= 4 (already in the
  library, claim `critical-minimum-degree`). The new ingredient is the *geometric*
  local structure: the neighbours N(v) of a vertex lie on the unit circle, and two
  neighbours are adjacent iff their directions differ by exactly 60 degrees, so
  N(v) is an induced subgraph of the 6-cycle — a disjoint union of paths and at
  most one 6-cycle (a regular hexagon around v). Charge each vertex by its degree
  and each face by the angle sums these chords force, then discharge along edges
  using Euler's formula. A global count that cannot be realised by any collection
  of valid unit-circle neighbourhoods is a contradiction; the minimal counterexample
  is either impossible below some N, or must contain a specific reducible local
  configuration (a precise search target).
mechanism: This is a change of representation from "construct a 5-chromatic graph"
  to "prove a minimal one cannot be small, by a local-count identity". The named
  mathematics is the discharging method (Wernicke 1904; Heawood 1890; Appel–Haken
  1977 for the four-colour theorem), transplanted from planar triangulations to the
  *angular* structure of a unit-distance graph: a vertex's neighbourhood is a
  subgraph of C6, every edge between neighbours subtends exactly 60°, so the angle
  of each face at a vertex is a multiple of 60° and the total angle around v is
  2π. Combining min-degree >= 4 with the fact that a vertex can have at most 6
  neighbours (unit circle + chord-1 = 60° spacing) gives each vertex degree in
  {4,5,6}, and degree 4/5 neighbourhoods have a very constrained shape (paths of
  length 4 or 5 around the circle, with forced gaps). Euler's formula plus the
  face-angle identity converts these into an exact integer system over the
  discharge coefficients, solvable symbolically — the run's census found "no
  5-chromatic UDG on <= 11 vertices" by nauty enumeration and stalls at n=12;
  discharging would prove the next rung analytically or name the exact local
  pattern any n=12+ counterexample must exhibit. It is the one line that is a
  theorem-in-waiting (an upper bound on N, or a classification of critical
  neighbourhoods), not a search.
status: refuted
killed-by: size-bound route cannot beat the census. Kostochka-Yancey gives
  f_5(n) >= (9n-5)/4 for a 5-critical graph; the unit-distance ceiling is
  u_2(n) <= C n^{4/3} (SST). Setting (9n-5)/4 <= C n^{4/3} first stops forcing a
  contradiction at n=10 even with the impossible constant C=1 (hand check:
  (90-5)/4 = 21.25 <= 10^{4/3} ~ 21.54), so the provable N is <= 9, below the
  census's n=11, and any true SST constant is C>1. A sharper unit-distance-
  specific density/angle bound is the open problem itself.
first-step: Replace the (incorrect, non-planar) "Euler's-formula face-angle
  identity" mechanism with the Gallai-forest / Kostochka-Yancey discharging that
  actually applies to k-critical graphs: extract the sharpest edge lower bound
  for a unit-distance-constrained 5-critical graph, then combine it with the
  unit-distance edge-density upper bound u_2(n)=O(n^{4/3}) (claim
  `unit-distance-upper-bound`) to obtain an analytical N below which no
  5-chromatic UDG exists. Calibrate the edge bound on the 4-colourable Moser and
  Moser+Moser, and check the 60°-angular discharging contribution.
falsifies: a discharging system that admits arbitrarily small realisations (no
  contradiction below any N), i.e. the local angular structure alone does not force
  enough — then the method only produces ever-weaker necessary conditions, and the
  run keeps the census as the strongest size bound.
precedent:
  - Wernicke 1904, Heawood 1890, Appel–Haken 1977 — the classical discharging
    method for planar graphs (sources to be pinned; NOT the applicable branch here,
    because a 5-critical graph is non-planar).
  - Kostochka–Yancey 2014, "Ore's conjecture on k-critical graphs is almost true
    for fixed k" (J. Combin. Theory B) — THE discharging-on-k-critical-graphs
    result: f_k(n) >= ((k+1)(k-2)n - k(k-3))/(2(k-1)), essentially solving
    Dirac/Ore's edge-count problem for k-critical graphs; non-planar.
  - Cranston–Rabern 2016, "Edge lower bounds for list critical graphs via
    discharging", arXiv:1602.02589 — "The method applies ... and does NOT rely on
    planarity or the four-colour theorem." Establishes discharging for k-critical
    graphs is non-planar-transplantable.
  - Krivelevich 1997, "An improved bound on the minimal number of edges in
    color-critical graphs" https://doi.org/10.37236/1342 — |E(G)| >=
    ((k-1)/2 + (k-3)/(2(k^2-2k-1))) n, built on the Gallai-forest decomposition
    of low-degree vertices.
  - Dirac 1957 bound: 2|E| >= (k-1)n + k-3 for k-critical graphs — so a 5-critical
    graph has average degree >= 4 + 2/n (the edge-density gap the angular structure
    must reconcile with u_2(n)=O(n^{4/3})).
  - claim `critical-minimum-degree`, `sharp-nbhd-local` (60° chord structure), and
    `unit-distance-upper-bound` (O(n^{4/3}) unit edges — the density ceiling the
    edge lower bound meets).
caveat:
  The mechanism as written — "Euler's formula + face-angle identity" — requires a
  planar embedding, and a 5-chromatic graph is NECESSARILY NON-PLANAR (four-colour
  theorem: every planar graph is 4-colourable). So Euler's formula does not apply
  to the whole graph, and "angle sum around a vertex = 2π over faces" is not a
  well-defined combinatorial identity on a non-planar drawing. The discharging
  METHOD is still fully viable — the k-critical discharging literature (Kostochka-
  Yancey, Cranston-Rabern, Krivelevich) does NOT use Euler's formula; it uses the
  Gallai-forest decomposition of the LOW-degree vertices. The geometric 60°
  angular structure is real (claim `sharp-nbhd-local`) and unit-distance-specific,
  but it enters via the degree/density account, not via planar face angles. This
  is a correction of mechanism, not of the method's viability.
```

## Research verdict — GROUNDED (method), with an essential mechanism correction

**The discharging method is real, published, and — decisively — does NOT require
planarity.** A 5-chromatic graph is necessarily non-planar (four-colour theorem:
every planar graph is 4-colourable; a 5-critical graph is not), so any viable
discharging attack on the minimal 5-chromatic unit-distance graph must be the
*non-planar* k-critical discharging, which is exactly what the literature does:

- **Kostochka–Yancey** essentially solve Dirac's/Ore's edge-count problem for
  k-critical graphs, proving
  `f_k(n) >= ( (k+1)(k-2)n - k(k-3) ) / ( 2(k-1) )`
  for the minimum number of edges in an n-vertex k-critical graph. For k=5 this
  is `f_5(n) >= ( (6)(3)n - 5(2) ) / 8 = (18n - 10)/8 = (9n-5)/4 ≈ 2.25 n` — an
  average degree just above 4.25.
- **Cranston–Rabern** make the non-planarity explicit: their discharging proof
  "does not rely on planarity or the four-colour theorem."
- **Krivelevich** and **Dirac** give the earlier rungs (Dirac: `2|E| >= (k-1)n +
  k-3`, so a 5-critical graph has edge count `>= 2n + 1/...` — strict average
  degree `> 4`).

### What this actually buys the size-bound rung

The discharging machinery converts "5-critical" into a strict edge-density lower
bound. The unit-distance side of the run already owns the ceiling:
`u_2(n) = O(n^{4/3})` (claim `unit-distance-upper-bound`). So the analytical
route to the size bound is:

    edge lower bound for 5-critical UDG  >=  c·n        (Dirac/Gallai/Kostochka-Yancey)
    unit edges among n points           <=  C·n^{4/3}   (Spencer–Szemerédi–Trotter)
    therefore:  c·n <= C·n^{4/3}   =>   n >= (c/C)^3,

a **constant** lower bound on the size of any 5-chromatic unit-distance graph.
This is the form in which discharging (or even just Dirac's bound) proves a
size-bound rung by pure counting — it replaces the nauty enumeration that stalled
at n=12 with an analytic inequality, and the geometric 60°-neighbourhood structure
(`sharp-nbhd-local`) can only sharpen the constant c by ruling out degree-4/5
configurations that are unit-distance-forbidden.

### What would be false — the mechanism as written is wrong

The candidate's stated mechanism ("charge each *face* by *angle sums*, then
discharge using *Euler's formula*") presupposes a planar embedding with welldefined faces and face-angle sums. A 5-critical graph has none: it is non-planar,
so there is no combinatorial planar embedding, no Euler identity `V - E + F = 2`
on the whole graph, and no well-defined "angle of each face at a vertex". The
Kostochka-Yancey/Cranston-Rabern machinery does not use Euler's formula exactly
for this reason — it uses the **Gallai forest** structure of the subgraph induced
by low-degree vertices (which is embeddable where it matters) and a local
reducibility/discharging count. So the *mechanism* must be corrected to the
Gallai-forest route; the *method* and its value survive intact.

### Verdict

`status: grounded`. The method is a genuine, heavily-published, non-planar
technique for exactly the object in question (minimal 5-critical graphs), and its
combination with the unit-distance edge-density ceiling directly produces the
analytical size-bound rung that the nauty census could not extend past n=12. The
library already holds all three ingredients: `critical-minimum-degree` (delta>=4),
`sharp-nbhd-local` (60° angular neighbourhood structure), and
`unit-distance-upper-bound` (O(n^{4/3}) edge ceiling). The one correction: the
route is the Gallai-forest / Kostochka-Yancey discharging, not Euler's formula on
a planar embedding — a 5-critical graph is non-planar by the four-colour theorem.
This is recorded as a `caveat`, not a `killed-by`: the method is not dead, only
its written mechanism was.

## Why this is not a restatement of a closed idea

- Not the neighbourhood-complex line (refuted on topology cost): discharging has
  no homotopy; it is a counting/local-reducibility argument.
- Not the kernel census (enumerative, stalled at n=12): this is the analytic route
  to the same size-bound rung — an inequality, not an enumeration.
- Not the theta/Hoffman relaxation: discharging proves edge-density facts about all
  5-critical unit-distance graphs; theta certifies individual constructed graphs.

## Decision (convergence pass) — REFUTED

Adopted instead: `rigidity-matroid-henneberg-construction`, which attacks the
forced-pair crux directly with an exact construction engine. The size-bound route
proposed here does not survive the numbers: the edge lower bound f_5(n) >= (9n-5)/4
meets the unit-distance ceiling u_2(n) <= C n^{4/3}, and even with the impossible
constant C=1 the inequality first stops forcing a contradiction between n=9 and
n=10 (hand check, no exec tool this turn: (90-5)/4 = 21.25 <= 10^{4/3} ~ 21.54),
so the provable N is <= 9 — strictly below the n=11 the nauty census already owns.
The non-planar discharging machinery (Kostochka-Yancey, Cranston-Rabern,
Krivelevich) is real, but it cannot extend the size bound without a sharp
unit-distance-specific density/angle bound, which is the open problem itself. The
one salvageable fragment — the classification of 5-critical unit-circle
neighbourhoods (degree in {4,5,6}, induced subgraph of C6) — is folded into the
adopted Henneberg search's forced-pair filter, not pursued as a standalone count.
