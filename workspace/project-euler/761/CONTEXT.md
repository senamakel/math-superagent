# Shared context

Problem: Project Euler **761** — runner/swimmer pursuit-evasion on a regular
n-gon pool. Answer candidate **V_hexagon = 5.05505046** (8 dp). State of the
run: **computed by ONE route (stewbasic exact formula); the final verification
— a genuinely second route to the hexagon value — is NOT yet done.** Do not
report 5.05505046 as independently verified until that route exists. Full
statement: `/workspace/problem.md`.

## The answer (candidate, single-route)

**V_hexagon = 5.0550504633038933… → 5.05505046** (8 dp, the required answer).
For n=6: K=2, α = 1.37166085458, V = 1/cos(α).
**Status: computed via the stewbasic formula only. The two "independent" code
routes (solution.py mpmath and verify_hexagon.py sympy) implement the SAME
formula at different precisions — that is not a second derivation, and the run
must not claim it is.**

## Method (sourced, exact formula)

For a regular n-gon (swimmer at center, runner at an edge midpoint, speed ≤v),
the critical speed is V(n) = 1/cos(α) where, with θ=π/n and t=tanθ:

```
K   = largest integer in [0,n] with  sin(Kθ) − (K+n)·t·cos(Kθ) < 0
      (== floor of the unique root of tan(xθ) − (x+n)t in [1, n/2))
α   = ½·( Kθ + acos( 2·sin(Kθ)/((K+n)·t) − cos(Kθ) ) )
```

Source: stewbasic, Math.SE q.1762665 (via Wayback); corroborated by Abel et
al., "Escaping a Polygon", arXiv:2007.08965. **Not peer-reviewed-formal but
validated** (below). The mechanism is the same boundary-time identity as the
circle: equalize the swimmer's straight-line escape time to an exit point
against the runner's perimeter time to that point; the safe region is the
pool **scaled homothetically** (perimeter v× smaller) — on a polygon the
runner's angular speed is non-constant, so the safe region is a scaled copy,
not a circle.

## Validation (all checked, by program)

- **n=3**: V=(3+√5)·√2 = 7.4049183473 — matches Abel et al. Thm 4.5 exact
  (anchors the formula, but n=3 is NOT independently re-derived here either).
- **n=4**: V=√(5/2·(7+√41)) = 5.78859314459 — matches Abel 4.6, David K
  (an INDEPENDENT geometric derivation), and the statement oracle 5.78859314.
  This is the strongest evidence the general-n formula is correct: the square
  case is confirmed by two genuinely different routes.
- **n→∞**: converges to circle constant 4.6033388 (V(10000)=4.60333900) —
  matches IBM Ponder This oracle 4.60333885.
- **V_hexagon** computed by the stewbasic formula (solution.py mpmath, and the
  separately-noted sympy re-implementation). The two agree, but both are the
  SAME formula — NOT an independent second route, so the hexagon value is
  **single-route and still unverified** as a derivation. The circle oracle is
  reproduced independently by brute.py's two-phase geometric model; a
  hand-recheck of n=6 (K=2, inner=−1/8, α≈1.37166, V≈5.055) is consistent.

### Circle case (established, sourced, CLOSED — do not re-derive)
V_circle from cos B=1/V, sin B=(π+B)/V, i.e. tan B=π+B, V=1/cos B ≈ 4.60333885.
Source: IBM Ponder This May 2001, `research/summaries/ponder-this-goblin-pool-circle.md`.
Mechanism two-phase: stage on radius-1/v arc keeping diametrically opposite the
runner, then tangent chord to a shore point offset by B. This is the template
the n-gon generalizes.

## Ruled out / dead ends

- **Naive "stage at antipode + straight dash"** gives only π+1 ≈ 4.1416, NOT
  the circle oracle — the documented red herring. The correct model is the
  two-phase staging-arc + tangent-chord. Falsifying check kept in
  `code/explore_general_dash.py`.
- **K(n) = floor(3n/7) for all n** is FALSE beyond n=85 (first deviation n=86,
  off by +1); the period-7 recurrence pattern also breaks. K is only an
  auxiliary index in the V(n) formula and does not affect the 8-dp answer.
  OEIS A057357. Bounded conjecture, not a theorem.

## Numbers / anchors (cheap to restate, expensive to recompute)

| n | K | α | V |
|---|---|---|---|
| 3 | 1 | — | 7.4049183473 |
| 4 | 1 | 1.397 | 5.78859314459 |
| 6 | 2 | 1.37166085458 | **5.0550504633** |
| ∞ | — | — | 4.6033388 |

## Recalled (durable memory, cross-run)

Durable memory holds the circle identity, the stewbasic general-n formula, the
David K square closed form, and the V_hexagon = 5.05505046 value — all
consistent with this run's files. Note: durable memory itself labels the
hexagon value "single-route/unverified" — the run's earlier GOAL/CONTEXT went
beyond that and called it independently verified, which was wrong. Treat the
stewbasic n-gon formula as a sourced result with strong numeric agreement
(square + circle limit reproduced two ways — genuinely two derivations for
n=4), not a peer-reviewed theorem, and the hexagon value as single-route until
a second derivation exists. Earlier PE runs (346, 185, 763) are unrelated to
this shape.

## Contradictions

Research/CLAIMS.md lists the circle identity claim as "unchecked" in its one
`claim` block; the override in the notes is authoritative and has been
cross-checked independently — reload CLAIMS.md if it lags. No numeric
contradictions yet. (The only cross-run tension is that the hexagon value is
marked VERIFIED in the run's own earlier context/GOAL but is genuinely
single-route — this file now corrects that.)

## Gaps

**The decisive open gap: a genuinely second independent route to V_hexagon.**
Per the thread `research/threads/hexagon-critical-speed.md`, the needed route is
(a) a numerical solver that encodes the polygon game directly — min/max over
the swimmer's dash-landing boundary point of (runner-perimeter-time ÷
swimmer-distance), i.e. max over landings P of (runner_perimeter_dist(P) ÷
swim_dist(P)) at stage = 1/V — which must NOT import the K/α closed form
(a direct encoding, not over the bound — that is the legitimate brute force);
or (b) a David-K-style geometric construction specialized to n=6. It must agree
with 5.05505046 to 8 dp. **If it is not built, the final report must state
5.05505046 as computed-by-one-route, not as independently verified.** The
naive straight-dash orbit (`brute_polygon_naive.py`) is a LOWER BOUND and is
the wrong tool here (on a polygon it undershoots like the circle's pi+1 red
herring).

Files: `code/solution.py` (exact formula), `code/brute.py circle` (reproduces
circle oracle via two-phase geometry), `code/brute_polygon_naive.py` (naive
lower bound only), `code/verify_hexagon.py` (same formula, NOT a second route),
`GOAL.md`, `research/notes/polygon-generalization-escape-math.md`.

A final answer report, if any, must cite the stewbasic formula backed by the
arXiv paper, and state honestly that the hexagon value is as yet verified by a
single route only, pending the independent solver/construction above.
