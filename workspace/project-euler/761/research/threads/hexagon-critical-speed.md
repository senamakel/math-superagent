# Thread: hexagon critical speed (PE 761 answer)

## Question
What is V_hexagon, the critical runner speed for a *regular hexagon* pool, to
8 decimals? The circle (4.60333885) and square (5.78859314) oracle values are
established; the hexagon is the actual PE 761 answer.

## What it rests on
- `stewbasic-regular-ngon-cutoff`: the general-n formula λ = 1/cos(α). For n=6
  this evaluates to V_hexagon = 2 + 2√21/3 ≈ 5.05505046 — exact closed form
  confirmed by two programs (`code/hexagon_closed_form.py`,
  `code/confirm_hexagon_closedform.py`).
- `davidk-square-closed-form`: formula validated on square (5.78859314 two
  independent ways), giving confidence in the general-n formula's correctness.
- `escaping-polygon-wellposed-exact-square-disk`: rigorous model confirms the
  mechanism but has NO hexagon exact value.

## Status — two workstreams in flight (directive 1)

**Candidate V_hexagon = 5.05505046330389… = 2 + 2√21/3 — single route
(formula), not yet independently verified by the game model.**

### Workstream A: librarian — primary-source research pass
Fetch into `research/sources/` the pursuit-evasion literature this problem
instantiates:
- lion-and-man / Besicovitch escape
- boy-escaping-teacher on regular n-gon (primary formulation beyond Math.SE)
- swimmer-in-circular-pool (Gardner/Guy origin, rigorous two-phase staging)
- optimal escape trajectories from convex domains — involutes, chase curves,
  critical speed ratio
Every source gets a claim block so it reaches `research/CLAIMS.md`.

### Workstream B: symbolic_math — independent first-principles hexagon derivation
Derive V_hexagon directly from the geometry of the regular hexagon, without
relying on the stewbasic K-index. Goal: exact expression agreeing with
5.05505046330389… to 8 dp. Write derivation to
`research/notes/hexagon-first-principles.md`. This is the missing independent
route the CONTEXT.md Gaps flag.

## Next
- Librarian: download primary sources, write claim blocks.
- symbolic_math: derive V_hexagon from boundary-time equalization on the
  hexagon directly.
- When both land: curator verifies agreement, updates CONTEXT.md, closes the
  thread.

```thread
question: What is V_hexagon to 8 decimals (PE 761 answer)?
status: candidate 5.05505046 from stewbasic n=6 formula, exact closed form confirmed; two independent workstreams in flight per directive 1
rests-on: stewbasic-regular-ngon-cutoff, davidk-square-closed-form, escaping-polygon-wellposed-exact-square-disk
workstreams: (A) librarian primary-source pass → research/sources/, (B) symbolic_math first-principles hexagon derivation
next: librarian downloads, symbolic_math derives, curator verifies and closes
```