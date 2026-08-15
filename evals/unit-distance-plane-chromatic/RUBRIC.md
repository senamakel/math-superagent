# Rubric — unit-distance-plane-chromatic

Scored host-side by `scripts/eval-report`, against the workspace and
`config/trace.jsonl`. Milestones are **ordered and cumulative**: `M3` without
`M1` is not `M3`, it is an unverified claim.

Every milestone requires an **artifact in the workspace**, not a statement in a
report. "A number nobody ran is not a result" is the repository's own standard
and it is the standard here.

## Milestone ladder

### M0 — reproduced the known bounds with its own verified constructions

- The `7`-vertex graph built in the workspace, all `11` edges certified.
- `chi = 4` on it established by a run of the run's own colouring code, with
  captured output.
- The `7`-colouring of the plane described with its separation margin actually
  computed, not asserted.

Evidence: files under `code/`, captured output under `code/out/`, a claim block
in `research/CLAIMS.md` for each with evidence class `executed`.

### M1 — built the two oracles and calibrated them

- An edge certifier working in **exact** arithmetic over an algebraic number
  field. Floating point anywhere in this path fails M1 outright.
- A **complete** `k`-colourability test — SAT with a real solver, or exhaustive
  search — that returns a witness colouring on SAT.
- **Both calibrated on the `7`-vertex graph**, with the actual output recorded:
  `4`-colourable SAT, `3`-colourable UNSAT, all edges exactly unit.

This is the milestone that separates a real attempt from a plausible one. Most
of the value of this problem as a calibration instrument is in whether the
harness reaches M1 unprompted.

### M2 — searched a structured construction space

- Minkowski sums and/or rotations implemented, with the set of unit-distance
  pairs in `A + B` worked out rather than discovered empirically.
- A search over *constructions* with stated parameters, not over random point
  sets.
- A census: graphs built, sizes reached, chromatic number attained by each.

Partial credit: implementing the machinery but only testing hand-built examples
is M2-minus. Random point sampling is **not** M2 at any level.

### M3 — produced a machine-verified `5`-chromatic unit-distance graph

- Explicit vertex list, exact coordinates.
- SAT UNSAT for `4` colours, from the M1-calibrated encoding.
- Re-verified by a second route not sharing arithmetic with the construction.

### M4 — reduced it, or explained it

- A smaller graph than the first one found, or
- a human-legible account of which structural feature forces the fifth colour.

## Alternative ladders that score equally

The seed deliberately does not assume the answer is `> 4`. Two other
trajectories score as M3-equivalent and must not be penalised for going the
other way:

- **Upper bound.** An explicit `6`-colouring of the plane with the margin
  computed. This would be a larger result than the lower bound.
- **Size bound.** A proof that all unit-distance graphs on at most `N` vertices
  are `4`-colourable, for an `N` the run actually established. Score by `N`:
  any proved `N` is M2-equivalent, and a substantial one is M3-equivalent.

## Negative markers

Scored separately and reported alongside the ladder. These are the failures the
calibration set exists to detect.

| marker | what it looks like |
|---|---|
| **unverified claim** | a bound asserted with no executed program producing it |
| **float contamination** | tolerance-based edge detection anywhere in the path; a `5`-chromatic claim without exact arithmetic is presumed false |
| **uncalibrated oracle** | a SAT UNSAT reported without the `7`-vertex calibration ever having been run |
| **self-verification** | the construction code and the checking code sharing arithmetic |
| **searched for the answer** | screen-ledger hits, or a research query aimed at retrieving a published result rather than a technique |
| **recall without derivation** | `1581`, `1345`, `121`, `509`, or the specific field/angles appearing before any computation produced them — see `GROUND_TRUTH.md` |
| **random search** | time spent confirming that sparse random point sets are `4`-colourable |

## What a good run looks like even if it fails

Reaching **M1 and M2 with an honest negative census** is a success for the
harness, and should be scored well above a run that claims M3 without M1. The
question this calibration answers is not "can it solve Hadwiger–Nelson" — it is
"does it build the right instrument, calibrate it, and search structurally".
