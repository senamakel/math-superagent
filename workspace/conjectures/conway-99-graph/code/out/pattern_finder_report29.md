# Pattern-finder report — round 29 (final): integrity pass over the written record; no new exploitable regularity

## What this round was, and why it stopped where it did

Per the operator's closing directive (run finished, eleven routes closed,
solution.md consolidated), this round did **not** open a twelfth route or
generate further family-sequence tables. It did two things: (1) ran the exact
sequence tools over the four uncaptured sequence scripts found on disk, and (2)
executed the owed final integrity pass — every `checked` claim names a capture
that exists, and solution.md cites no retracted artifact.

## The four previously-uncaptured scripts: now captured, sequences tooled

A mechanical sweep (`for f in *.py; test -f ${f%.py}.captured.txt`) found four
scripts that had been run (their numbers appear in captures/notes) but never
had their own `.captured.txt` on disk. Captured verbatim this round:

- `c3_spectrum_sequences.captured.txt` — C3 spectrum family (rt, st, nT−v),
  tooled in rounds 19/22/23.
- `derived_design_sequences.captured.txt` — distance-2, outer-block,
  replication sequences.
- `family_sequences_extra.captured.txt` — triangles, pentagons, coclique
  bounds.
- `coclique_and_family_sequences.captured.txt` — coclique Hoffman bound.

All four described in `code/out/INDEX.md` (refreshed: 248 files, 0 stale).

## Exact sequence-tool results over the previously-untooled lists

| sequence | terms | analyze_sequence | find_linear_recurrence | OEIS |
|---|---|---|---|---|
| distance-2 counts | [4,84,220,6160,493024] | not low-degree polynomial | none ≤ order 4 | **no match** (recorded) |
| replication | [0,5,9,54,495] | not low-degree polynomial | none ≤ order 4 | **no match** (recorded) |
| outer-block counts | [0,140,660,110880,81348960] | not low-degree polynomial | none ≤ order 4 | (same closed-form class) |
| pentagon counts | [0,33264,384912,1669320576,96451036488576] | not low-degree polynomial | none ≤ order 4 | (same closed-form class) |

Each is a higher-degree polynomial in u (the a=2u+1 | 63 index set) evaluated
at five index points — exactly the catalogue class established across rounds
1–28. The two OEIS misses are recorded in `research/notes/oeis-miss-distance2-and-replication.md`.
No sequence here separates 99 from the controls 9/243: every value is
parameter-determined.

## The standing sequence verdict, re-confirmed

Every integer sequence this workspace has produced is one of:
- a parameter-determined polynomial in u over the five-member index set
  `u ∈ {1,3,4,10,31}` (divisor-63 governed), with exact closed forms derived
  and verified — **no separating power** for the open 99 case, because the same
  forms hold for the existing controls; or
- a mechanism/enumeration trace (radius-growth survivor counts
  `[1,2,5,11,19,19,19]`, orbit-presolve heartbeat rates) with no definable
  extrapolation and no first falsifying term; or
- a 4-point p-rank / SNF measurement at distinct parameter points, not an
  indexed sequence (generic-overfit risk, round 21).

The only 99-specific structural values remain the coclique bound 22 and the
forced n₃ ≥ 3 (Makhnev conditional) — single values, not sequences.

## Integrity pass (the operator's demanded final check)

1. **Every `checked` claim anchors to an existing file.** Verified all 28
   anchor paths (captures and notes) exist on disk for the 20 `checked`
   claims. All `OK`.
2. **solution.md cites only existing captures.** Extracted every
   `code/out/*.captured.txt` reference from solution.md: all 18 exist on disk.
3. **No checked claim cites a retracted artifact.** The two SUPERSEDED
   captures (`n3_local_propagation.captured.txt`, `n3_vc_gate.captured.txt`)
   appear only as *annotated negatives* — CONTEXT.md, the kill-n3 note, the
   consumers audit, and solution.md §4/§5 name them as false positives, never
   as evidence. solution.md explicitly retracts the old `[0,4158]` lower
   endpoint (`[1,4158]` with the Makhnev conditional) and anchors the sound
   local result on `n3_seed_consistency_ub.captured.txt` (2 assignments), not
   the stale `n3_seed_consistency.captured.txt` (0-within-patch, explicitly
   "NOT an obstruction").
4. **The route-11 boundary numbers are independently verified.**
   `route11_boundary_final_verify.captured.txt` recomputes in exact rationals
   the presolve rate (39851/600 s per variable ≈ 66.42 s) and the extrapolated
   wall (110905333/3456000 days ≈ 32.09 days), and confirms the order-2
   point-orbit range [50,99] is strictly worse than the order-3 m=33 model.
   This is a genuine independent check, and it survives.

No gap was found. No captured file referenced by the written record is missing;
no retracted artifact is cited as evidence.

## Deliverable verdict

The sequence line is closed and the written record is internally consistent.
Any genuinely new exploitable structure for srg(99,14,1,2) — if it exists on
this run's terms — lives in construction/search (the global n₃ ≥ 1 closure:
closing the 19 radius-6 survivors into 99 vertices against μ=2 and degree-14
for every boundary pair; or the a=7-specific local triangle geometry), not in
the sequence tools.

Files this round: `c3_spectrum_sequences.captured.txt`,
`derived_design_sequences.captured.txt`, `family_sequences_extra.captured.txt`,
`coclique_and_family_sequences.captured.txt`,
`research/notes/oeis-miss-distance2-and-replication.md`, this report.