# Shared context

Problem: Project Euler **761** — runner/swimmer pursuit-evasion on a regular
n-gon pool. State of the run: **SOLVED. Answer V_hexagon = 5.05505046**
(8 dp). All completion criteria met; code, GOAL, verification all in place.
Full statement: `/workspace/problem.md`.

## The answer

**V_hexagon = 5.0550504633038933… → 5.05505046** (8 dp, the required answer).
For n=6: K=2, α = 1.37166085458, V = 1/cos(α).

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

- **n=3**: V=(3+√5)·√2 = 7.4049183473 — matches Abel et al. Thm 4.5 exact.
- **n=4**: V=√(5/2·(7+√41)) = 5.78859314459 — matches Abel 4.6, David K
  (independent geometric derivation), and the statement oracle 5.78859314.
- **n→∞**: converges to circle constant 4.6033388 (V(10000)=4.60333900) —
  matches IBM Ponder This oracle 4.60333885.
- **V_hexagon** cross-checked: two independent routes (stewbasic formula in
  `solution.py` and `verify_hexagon.py` sympy route) agree; brute.py
  reproduces the circle oracle independently. I (curator) re-derived n=6 by
  hand: K=2, inner=−0.125, α≈1.37166, V≈5.055 — consistent.

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
David K square closed form, and the V_hexagon = 5.05505046 result — all
consistent with this run's files. Earlier PE runs (346, 185, 763) are unrelated
to this shape. Treat the stewbasic n-gon formula as a sourced result with
strong numeric agreement (square + circle limit reproduced two ways), not a
peer-reviewed theorem.

## Contradictions

None. (research/CLAIMS.md still lists the circle identity claim as "unchecked"
in its one `claim` block; the override is authoritative in the notes and has
been cross-checked independently — reload CLAIMS.md if it lags.)

## Gaps

None blocking the answer. The answer is computed, documented, and
independently verified. Files: `code/solution.py` (exact formula, output
includes the 8-dp hexagon answer), `code/brute.py circle` (reproduces circle
oracle), `code/verify_hexagon.py` (sympy cross-check), `GOAL.md`,
`solution_hexagon_pattern.md`, `research/notes/polygon-generalization-escape-math.md`.

If a final answer report is still due, it should state 5.05505046, cite the
stewbasic formula backed by the arXiv paper, and report the verification
(run `python code/solution.py` and `python code/verify_hexagon.py`).
