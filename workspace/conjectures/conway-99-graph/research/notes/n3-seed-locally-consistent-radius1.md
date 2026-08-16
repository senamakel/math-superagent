# n3 seed: SOUND local-consistency result (radius 1) — retraction record

This note records the correct, sound answer to the local-closure question of
task `kill-n3-ge1-case` at radius 1, and the retraction of the capture that
carried the wrong answer.

## The bug (why the earlier CONTRADICTION was wrong)

`code/lib/localprop.py`'s arc-consistency engine had a soundness bug in its
**saturation branch**: when a pair was saturated (its required common
neighbours were already fixed), the engine forced *every* candidate common
neighbour off on **both** sides — `a-v=0 AND b-v=0`. The sound conclusion from
saturation is only the 2-SAT / at-least-one-off clause **`NOT(a-v AND b-v)`**
(at least one of the two edges off), not both.
For the n3 seed, the lambda-witness pair (a,b) (witness c) then forced the
candidate vertex `6` off both sides, flipping the already-fixed `a-6=1`
lambda-witness of edge (a,d) — producing a spurious `CONTRADICTION` with a
clean-looking log. Confirmed by direct trace.

**AUDIT CORRECTION (fresh, this run):** the over-forcing bug is **already
fixed on disk**. `code/out/localprop_consumers_audit.md` confirms the current
`lib/localprop.py` saturation branch implements the sound `NOT(a-v AND b-v)`
semantics, and `code/out/independent_soundness_check.py` (engine vs.
from-scratch full enumeration) reports `ENGINE == ENUMERATION on all forced
values: True`, `[satisfying assignments] = 2`. So the bug is **historical, not
active**: the engine now reproduces the enumeration's 2 satisfying
assignments and `consistent=True` for the n3 seed. The capture
`code/out/n3_local_propagation.captured.txt` (produced by the pre-fix engine)
is **SUPERSEDED** — its top is annotated naming this bug and the sound result.
It must not be cited as a theorem.

## The sound result (radius 1), checked

The only criterion arc-consistency may soundly conclude on a bounded patch is
the upper-bound one: an *adjacent* pair has ≤ 1 common neighbour, a
*non-adjacent* pair ≤ 2, and any remaining deficits are satisfiable by the
other **91** graph vertices outside the patch.

Under exactly that criterion, the 2-edge-joined disjoint triangle pair
(T1={a,b,c}, T2={d,e,f}, cross edges **a-d** and **b-e**, the other seven
cross pairs non-adjacent) admits **2 satisfying assignments** over the 9 free
interior edges of the 8-vertex forced closure (complete enumeration of 512
assignments, exact, no floats).

```claim
id: n3-seed-locally-consistent-radius1
statement: The n3 configuration — two disjoint triangles joined by exactly two
  edges — is locally consistent at radius 1 in a lambda=1, mu=2, locally-7K2
  graph: under the only criterion arc-consistency may soundly conclude
  (adjacent pair <=1 common neighbour, non-adjacent <=2, deficits satisfiable
  by the ~91 outside vertices), the forced 8-vertex closure admits 2
  satisfying assignments. There is NO local obstruction at this radius; the
  seed EXTENDS locally. The earlier "CONTRADICTION" was an artifact of an
  over-forcing saturation branch in code/lib/localprop.py (a-v=0 AND b-v=0
  instead of NOT(a-v AND b-v)), now retracted.
hypotheses: lambda=1, mu=2, locally-7K2 on a bounded patch around the seed;
  deficits may be resolved by vertices outside the patch.
holds-here: yes
status: checked
bearing: The correct answer to kill-n3-ge1-case at this radius is NO local
  obstruction. It tells us the obstruction, if any, is NOT local at this
  radius — real information about where to look next (larger radius, or the
  interaction with the other 91 vertices). A local obstruction at a finite
  radius is NOT a global nonexistence proof of srg(99,14,1,2).
anchor: code/out/n3_seed_consistency_ub.captured.txt
```

## Zero-within-patch is NOT an obstruction

`code/out/n3_seed_consistency.captured.txt` reports 0 completions of the
8-vertex closure that satisfy lambda=1 & mu=2 & locally-7K2 *exactly within
the patch*. That is NOT an obstruction: the required common neighbours of
boundary pairs may legitimately sit among the other 91 vertices. The sound
result above (2 satisfying assignments under the upper-bound criterion) is
the one that carries, not the 0-completions-forced-closure reading.

## The follow-up question

The operator's stated next question: **at what radius, if any, does the seed
stop extending?** At the current radius (8 vertices, 9 free interior edges =
512 assignments), keep **complete enumeration** — it is exhaustive, needs no
encoder validation, and is more trustworthy (directive 14 point 3). Reach for
sat_solver only when the grown ball's free-bit count outgrows exhaustive
enumeration (≈ 2^20 assignments); report the radius at which that happens when
the ball is grown. This is the work of task `n3-seed-stop-radius`.
