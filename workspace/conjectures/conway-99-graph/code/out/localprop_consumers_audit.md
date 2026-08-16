# Audit: consumers of `code/lib/localprop.py` and the saturation branch

Date: baseline verification pass. Scope: naming every file that imports or
uses `lib.localprop.PartialGraph` / `neighbourhood_is_7k2` / `.propagate()`,
and whether its verdict could be contaminated by the historical
over-forcing soundness bug ("force a-v=0 AND b-v=0 on a saturated pair"
instead of the sound 2-SAT clause `NOT(a-v AND b-v)`).

## Headline result

**The described bug is NOT present in the current on-disk code.** The
saturation branch in `code/lib/localprop.py` (lines ~135-162) already
implements the sound form:

- candidate `v` established-adjacent to `i`, unknown to `j`  →  force
  `j-v=0` (this is exactly `NOT(a-v AND b-v)` given `a-v=1`);
- candidate established on both sides  →  true double-count contradiction;
- **both sides unknown  →  left undecided** (no over-forcing).

So nothing currently on disk over-forces both sides. The bug was found
and fixed; the notes (`research/notes/n3-seed-locally-consistent-radius1.md`,
`kill-n3-ge1-local-consistency.md`) record it as historical.

Independent confirmation: `code/out/independent_soundness_check.py` runs the
engine's forced closure against a complete 512-assignment enumeration of the
n3 seed's 8-vertex closure. Result (executed this pass):
`ENGINE == ENUMERATION on all forced values: True`,
2 satisfying assignments, no over-forced and no under-forced value. The
engine is sound **and complete** at this radius.

## Consumers (every file matched by `grep -rn localprop|PartialGraph|neighbourhood_is_7k2|.propagate(`)

### 1. `code/out/n3_local_propagation.py` — DIRECT ENGINE CONSUMER
- Imports: `from lib.localprop import PartialGraph, neighbourhood_is_7k2`.
- Calls `PartialGraph(...)`, `P.propagate(log)`, and the control checks.
- Runs the shared engine from the n3 seed. Its rendered capture
  (`n3_local_propagation.captured.txt`) is annotated SUPERSEDED — it was
  produced by the engine *before* the fix and carried the spurious
  CONTRADICTION.
- **Current verdict: not contaminated.** Re-run this pass with the fixed
  on-disk engine returns `consistent = True` (LOCALLY CONSISTENT), the
  forced closure matches the enumeration, and the n3 seed extends locally.
  The `.captured.txt` (stale, SUPERSEDED) should not be read as a theorem,
  but the *program* now runs against the sound engine.

### 2. `code/out/independent_soundness_check.py` — DIRECT ENGINE CONSUMER / VERIFIER
- Imports: `from lib.localprop import PartialGraph`.
- Runs the engine to obtain its forced closure, then compares against a
  from-scratch complete enumeration (no engine use in the checker path).
- **Verdict: not contaminated — it is the soundness oracle for the engine.**
  It detects over-forcing/under-forcing directly and would flag the bug if
  it were present. Passes: engine matches enumeration exactly (2 satisfying
  assignments).

### 3. `code/out/n3_seed_consistency.py` — NOT AN ENGINE CONSUMER (self-contained)
- Mentions `code/lib/localprop.py` only in prose (MOTIVATION / annotation).
- Imports nothing from `lib.localprop`; runs its own completeness-check
  oracle. **Verdict: not contaminated.**
- Its capture reports 0 exact-within-patch completions, which the notes
  correctly explain is NOT an obstruction (boundary-pair common neighbours
  may sit outside the patch; the upper-bound criterion is the sound one).

### 4. `code/out/n3_seed_consistency_ub.py` — NOT AN ENGINE CONSUMER
- Self-contained sound upper-bound oracle. Imports nothing from
  `lib.localprop`. **Verdict: not contaminated.**
- Reports 2 satisfying assignments (the SOUND local-consistency baseline).

### 5. Everything else — NO consumer
- All other `from lib.srg import ...` and `from lib.triangles/hexagons`
  imports in `code/out/` touch only `lib.srg` / `lib.triangles` /
  `lib.hexagons`, never `lib.localprop`. No other file constructs a
  `PartialGraph` or calls `.propagate()`.

## Would-be consumers / not yet present

- `sat_solver` (and `code/out/n3_radius_probe.py`, spawned as `sat_solver`)
  is referenced in the directive, threads, and TASKS.md as the next step
  ("push to larger radius") but **does not exist yet on disk** — no encoder,
  no solver, no `n3_radius_probe.py`. Its design calls for a faithful
  encoder; it must be validated by finding rook(3) and BvLS before any UNSAT
  at 99 is believed. Because it does not yet consume `lib.localprop`, there
  is currently no consumer whose future verdict the (fixed) engine could
  contaminate.

## Verdict summary

| Consumer | Engine consumer? | Could its verdict be contaminated? |
| --- | --- | --- |
| `n3_local_propagation.py` | yes (`PartialGraph.propagate`) | No — runs against the fixed sound engine; consistent=True. Stale `.captured.txt` flag SUPERSEDED. |
| `independent_soundness_check.py` | yes (engine + enumeration) | No — it is the engine's soundness oracle; passes, engine==enum. |
| `n3_seed_consistency.py` | no (self-contained) | No. |
| `n3_seed_consistency_ub.py` | no (self-contained) | No. |
| `sat_solver` / `n3_radius_probe.py` | not yet on disk | n/a — must be encoder-gate-validated when built. |

The current, verified baseline: the shared engine is sound and complete at
radius 1 on the n3 seed (2 satisfying assignments, engine==enumeration), and
the four oracle controls pass with the negative controls failing only on the
lambda/mu count path.
