# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

**Token budget** `MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default. Link the file
that holds any detail compressed away. Durable findings belong in Cognee.

## Starting position — read this first

This is **not** greenfield. The earlier CONTEXT.md claimed an empty workspace;
that was wrong even when written. The oracle pair is **built and calibrated**,
and the first construction attempts have been made and recorded. Agents must
not re-derive the oracle or re-run calibration; the gating check has passed.

## Established — verified results

**Oracle pair is calibrated on the 7-vertex Moser spindle: chi = 4 PASSED.**
This is the gating check from GOAL.md and it has survived four independent
routes, so it is treated as established (verified, not merely asserted):

- Exact coordinates in field `Q(sqrt3, sqrt11, sqrt33)`:
  `O(0,0), P1(1,0), P2(1/2,sqrt3/2), Q(3/2,sqrt3/2), P1'(5/6,sqrt11/6),
  P2'(5/12-sqrt33/12, sqrt11/12+5sqrt3/12), Q'(5/4-sqrt33/12, 5sqrt3/12+sqrt11/4)`.
  The two rhombi share O; the second is rotated by cos=5/6, sin=sqrt11/6 so the
  far tips Q,Q' are at distance exactly 1. (`code/out/calibrate_moser.captured.txt`)
- All **11 edges** certified exactly `|x-y|^2 = 1` (no tolerance); **no** spurious
  or missed edge (full scan of all 21 pairs). (`code/out/brute_calibration.txt`)
- `k=4` SAT with witness `[0,1,2,0,1,2,3]`; `k=3` UNSAT. **Counts of proper
  colourings agree exactly** between brute-force enumeration and SAT model
  enumeration: k=1:0, k=2:0, k=3:0, k=4:**384**, k=5:**5040**.
  (`code/out/sat_count_check.captured.txt`)
- Confirmed independently: PySAT Cadical153 and Minisat22 both give k=3 UNSAT /
  k=4 SAT with proper witness; an independent numeric+symbolic rebuild confirms
  11 edges and chi=4. (`code/out/sat_calibration.captured.txt`,
  `code/out/verify_calibration_independent.captured.txt`)

**Diamond k=3 base case (the spindling closure's base).** The 4-vertex diamond
(two unit equilateral triangles on a common edge; 5 edges; tips at squared
distance 3, i.e. |tips|=sqrt3) has tips **forced equal in every 3-colouring**:
adding the tips edge makes 3-colourability UNSAT, verified with the independent
Minisat solver. (`code/out/forced_pair.captured.txt` Stage 2, and the
commands.log diamond test). This is exactly the G-spindling-closure base fact:
spindling the diamond about a tip with theta=2 arcsin(1/(2 sqrt3)) is what
produces the 7-vertex spindle.

**A negative result — the spindle route's crux fails on the graphs tried.**
The lower-bound-via-spindle skeleton reduces chi>=5 to finding a 4-chromatic
unit-distance graph with a pair (u,v), |u-v|>=1/2, monochromatic in **every**
4-colouring (`G-forced-pair-exists`). The complete forced-pair test was run:

- Moser spindle, k=4, all 10 non-edge pairs with sqdist>=1/4: **NONE** forced
  monochromatic. (`forced_pair.captured.txt` Stage 1)
- Moser+Moser Minkowski sum (26 vertices, 69 unit edges), all 256 qualifying
  non-edge pairs, k=4: **NONE** forced, and the sum is 4-colourable.
  (`forced_pair.captured.txt` Stage 3)

So the route is **dead for the spindle itself and for a first Minkowski sum**;
a forced pair, if it exists, needs a richer base graph. This is the most
important open fact the run owns: it names exactly what the construction must
supply. See "Ruled out" below.

**Sourced results taken as inputs (asserted-by-source, not re-derived here):**
- De Bruijn–Erdős 1951: `chi(G) = sup{ chi(H) : H finite subgraph of G }`; the
  finite-to-infinite step needs a compactness/choice principle (BPIT; weaker
  than AC; valid in ZFC). Applies verbatim to the plane unit-distance graph, so
  `chi >= 5` iff some finite unit-distance graph is not 4-colourable.
  (`research/CLAIMS.md` id `debruijn-erdos-1951`)
- Spencer–Szemerédi–Trotter 1984: `u_2(n) = O(n^{4/3})` max unit distances among
  n plane points — density cannot be bought. (id `unit-distance-upper-bound`)
- Maehara 1991 (+ Homma–Maehara 1990): the distances occurring between vertices
  of a **rigid** unit-distance graph are exactly the **algebraic** numbers —
  the sourced justification for exact-arithmetic coordinates. (id
  `maehara-algebraic-rigid-distances`)
- Eisenstein integers Z[omega] form the triangular lattice; unit vectors are the
  six powers of a 6th root of unity; `N(x+y omega)=x^2-xy+y^2`. (id
  `einstein-lattice-unit-distance`)
- Minkowski sum distance-1 condition: `|(a1+b1)-(a2+b2)| = 1` iff
  `|(a1-a2)+(b1-b2)| = 1`. (id `minkowski-sum-unit-distance-condition`)
- SAT k-colourability encoding (at-least-one + properness) is correct. (id
  `sat-k-colourability-encoding`)
- Minkowski sums of small unit-distance graphs give denser large UDGs; many
  densest-known small UDGs are such sums. (id `minkowski-sum-dense-graphs`)

All seven are `asserted-by-source` in `research/CLAIMS.md`; their network-level
sourcing is recorded in `research/sources/`.

## Ruled out — closed directions and the obstruction

- **Spindle has no monochromatic-forced pair under 4 colours.** Complete SAT
  test over all 10 qualifying pairs: every pair can be 4-coloured with the two
  vertices distinct. So `G-forced-pair-exists` cannot be witnessed by the Moser
  spindle itself. The spindle-based route needs a strictly richer base graph.
- **Moser+Moser (26v, 69e) has no forced pair and is 4-colourable.** A first
  Minkowski sum does not supply the rigidity; sums of colourable graphs can
  stay colourable (the run's core open question `REQUESTS` row).
- **A floating-point `=1` edge check failed to certify the construction**
  during development (`commands.log`: sympy `simplify()` was needed to certify
  squared distances equal 1) — confirms the exact-arithmetic discipline is
  load-bearing, not cosmetic.

## Tried but NOT executed — do not trust the file descriptions

`code/scholar_verify_claims.py` and `code/verify_sources.py` were **written but
never run**: there is **no captured output** for them in `code/out/`, and
`commands.log` does not show them executing. `code/INDEX.md` claims they
upgraded three claims to `checked`; that is not supported by any captured
output. `research/CLAIMS.md` correctly still marks them `asserted`. Do not
treat the Minkowski/Eisenstein/SAT-encoding claims as machine-checked until an
actual run produces a captured verdict.

## Numbers

- Moser spindle: 7 vertices, 11 edges, chi=4; k-colouring counts
  (0,0,0,384,5040) for k=1..5. Coordinates in Q(sqrt3,sqrt11,sqrt33).
- Diamond: 4 vertices, 5 edges, tips at |·|²=3, tips forced equal in every
  3-colouring; verified via independent Minisat.
- Moser+Moser: 26 vertices, 69 unit edges, 4-colourable, no forced pair among
  256 tested.
- Hexagonal tiling exploration (`commands.log`, side=1, exploration only, not
  the tight upper-bound margin): best 7-colour pattern (1,3) gives min
  same-colour centre distance sqrt(7)·L ≈ 2.6458·L and min hexagon separation
  0.768·L. This is scratch, not an upper-bound artifact.

## Recalled (durable memory)

Two durable memories in Cognee bear on this run, both past runs' findings
(stated, signed, not re-derived here):
- **Erdős unit-distance lower/upper**: u_2(n) is between ~n^(1+O(1/loglog n))
  and O(n^{4/3}); density cannot buy chromatic number; high-chromatic UDGs must
  be rigid via algebraic structure. (source: Spencer–Szemerédi–Trotter 1984)
- **De Bruijn–Erdős reduction**: matches the asserted claim above; the
  extension needs Rado's selection / Tychonoff / BPIT (WKL0 for countable),
  i.e. weaker than AC.

Also stored: the calibration results (11 edges, chi=4, counts) as durable
memory — so they will not be recomputed. The memory graph component is
currently failing (403 on triplet completion), so `relate_memory` is
unavailable; `recall_memory` passage search still works.

## Contradictions

- `code/INDEX.md` vs the actual run state: it describes `scholar_verify_claims`
  and `verify_sources` as having promoted claims to `checked`, but no captured
  output exists and `CLAIMS.md` marks them `asserted`. The `checked` claim is
  unsupported; trust `CLAIMS.md`.
- The previous `CONTEXT.md`/`TASKS.md` wrongly described the workspace as empty
  with no oracle; the calibration artifacts disprove that. This file supersedes
  it.

## Gaps — the next unresolved thing, in order

The weakest ladder rung marked open, `R-moser-calibration`, is **done** (chi=4
reproduced). The two live directions and their first move:

1. **Forced-pair existence over richer base graphs** (`G-forced-pair-exists`,
   the crux of the spindle skeleton). The spindle and Moser+Moser failed; the
   next move is to feed **denser / more rigid candidate base graphs** through
   the same complete forced-pair SAT test: other Minkowski sums (triangle+wheel,
   rotation-coincidence sums, per `minkowski-sum-dense-graphs`), and graph
   **products/spindlings** that accumulate rigidity. Each candidate is a finite
   SAT query per pair. The exact field is Q(sqrt3,sqrt11); `code/lib/unitfield`
   has `minkowski_sum`; `code/forced_pair.py` is the ready test harness.
2. **Size-bound rung** (`R-size-bound`, the reachable stated deliverable): prove
   every unit-distance graph on at most N vertices is 4-colourable for the
   largest N the run can establish, by a structural argument (a minimal
   5-chromatic graph has min degree >= 4; each vertex neighbourhood lies on a
   unit circle with chord-1 edges at 60°). This is a theorem, not just a
   construction, and is the strongest reliably reachable result.

Secondary: a construction **census** (chromatic number of every constructed
UDG, max chi, infeasibility bound) is the cheap first artifact; and the
upper-bound direction (a 6-colouring) is much less explored but unstructured.

**Dead end to beat:** the forced-pair route needs a base graph with a pair
forced equal at distance >= 1/2 that the spindle and one Minkowski sum lack.
Any new construction's first test is whether its 4-colouring forces such a
pair — that is the measure of progress on the lower bound.
