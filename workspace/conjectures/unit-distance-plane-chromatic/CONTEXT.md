# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). Link
the file that still holds any detail compressed away. Durable findings belong in
Cognee. A statement nobody can trace to a source is worth less than no
statement.

## Starting position — read this first

This is a **greenfield run**. Nothing has been established, computed, or
attempted yet:

- `code/` empty — no `unit_graph`, no colouring test, no SAT encoding. See
  `code/lib/INDEX.md` (no modules) and `code/index.md`.
- `research/` holds only template READMEs; `research/CLAIMS.md` says "No
  claims recorded yet". No sources, summaries, notes, threads, approaches, or
  backward files exist.
- Cognee (durable memory) and scratch hold nothing on this problem.
- `CONTEXT.md`'s established/ruled-out/numbers/recalled sections are empty by
  fact, not by omission.

Agents must not assume the oracle exists. It does not. Building and calibrating
it is the gating next step.

## Established

Nothing has been independently established by this run. The following are **task
inputs from `problem.md`**, none yet verified here, and each must be reproduced
or sourced before it is treated as known:

- **Bounds** `4 <= chi(G) <= 7`, decades old, both reproduced as elementary
  constructions in `problem.md` but not yet recomputed in this workspace.
- **The 7-vertex graph** (two unit rhombi sharing a vertex, rotated so their
  far vertices are at unit distance; two unit triangles per rhombus) is claimed
  `chi = 4`, with `11` edges. This is the **calibration pair**.
- **De Bruijn–Erdős reduction**: `chi(G) >= k` iff some finite subgraph has
  `chi >= k` (needs a choice principle). Makes the whole infinite problem a
  finite-object lower-bound question.
- **`O(n^{4/3})` unit-distance bound** among `n` plane points: density cannot be
  bought; high-chromatic graphs must be rigid via algebraic structure.
- **Construction engine**: Minkowski sums `A + B` and rotations create far more
  unit distances than size suggests; exact which pairs land at unit distance is
  the calculation the approach rests on.
- **The trap**: floating-point coordinates manufacture spurious edges, which can
  only *raise* apparent chromatic number (no self-correcting pressure). Exact
  algebraic arithmetic is mandatory from the first line. A false `5`-chromatic
  graph is the failure mode to guard against; independent re-verification of any
  claimed `5`-graph is required.

## Ruled out

Nothing has been tried and failed yet — no direction has been closed. The
first recorded failure will be the oracle failing calibration, if it does.

## Numbers

`4 <= chi(G) <= 7` (unverified input). The calibration target is the `7`-vertex,
`11`-edge graph needing `chi = 4`. No computed terms exist yet.

## Recalled

Nothing. Cognee and scratch hold no prior runs on this problem or its shape.

## Contradictions

None recorded.

## Gaps

The next unresolved thing, in order:

1. **Build the oracle pair** — exact edge certifier `unit_graph(points)`
   proving `|x-y|^2 = 1` symbolically over an algebraic number field, and a
   complete `k`-colourability test returning a witness colouring.
2. **Calibrate both on the 7-vertex graph**: certify all `11` edges exactly;
   confirm `4`-colourable and not `3`-colourable (SAT for `4`, UNSAT for `3`).
   Nothing measured downstream is trusted until this passes.
3. Only then: a search over structured Minkowski-sum/rotation constructions, and
   the upper-bound direction (a `<7` colouring) which `problem.md` notes is much
   less explored.
