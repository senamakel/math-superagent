# Coclique-lift line closed: a super-simple 2-(22,4,2) design EXISTS (directive 20)

The steering directive (20) settles Q2 of the coclique-lift line **constructively**:
a super-simple 2-(22,4,2) design **exists**, so the design condition a 22-coclique
would impose on a putative `srg(99,14,1,2)` is **satisfiable** and cannot rule
anything out. The line is a **sixth closed route** — closed as *non-obstructive*,
not as a refutation of the graph. It bears on neither existence nor nonexistence.

## The obstruction named

A tight 22-coclique `C` in a putative `srg(99,14,1,2)` forces the outside
neighbourhoods `{N(b) ∩ C}` to be a `2-(22,4,2)` design (b=77, r=14, k=4; claim
`coclique-alpha22-forces-22242-design`, checked). The graph lift additionally
forbids any two blocks meeting in exactly 3 points, else two outside vertices would
share 3 common neighbours in `C` (violating λ=1 if adjacent, μ=2 if not). That
extra condition is **super-simplicity** — the object is a *super-simple*
2-(22,4,2) design, not merely a 2-(22,4,2) design (claim
`super-simple-22242-gap`).

The obstruction a 22-coclique would have to run into is therefore **only** the
nonexistence of a super-simple 2-(22,4,2) design. That design **exists**, so the
obstruction is absent: the design-level condition is satisfiable and cannot
contradict α = 22.

## The constructive answer (checked)

- **Q2 = YES, constructively.** `code/out/coclique_lift_cpsat.py` (OR-Tools
  CP-SAT, exact integer) reached **OPTIMAL in 167.35s** with 7315 booleans,
  156131 branches, 596 conflicts (`code/out/coclique_lift_cpsat.captured.txt`).
- **Explicit 77-block certificate** in
  `code/out/coclique_lift_clean_design.txt`.
- **Independently verified** by direct counting (a second route): all 22 point
  degrees equal 14, all 231 pairs covered exactly twice, max triple overlap 1
  (i.e. no two blocks share a triple). So the certificate is a super-simple
  2-(22,4,2) design.

This supersedes the earlier **INCONCLUSIVE** HiGHS MILP (482.5s timeout, no
feasible point, `code/out/coclique_lift_q2.captured.txt`) and the 4000-random-draw
sampling (`code/out/coclique_lift_constructive.captured.txt`, never evidence).

## Tool lesson (keep this)

CP-SAT decided in **167 seconds** what the HiGHS MILP timed out on at **482
seconds**, and what 4000 random draws over a space this size could never have
shown in either direction. The previous pass lost a specialist to exactly this
question (the radius-2 CP-SAT setup, agent-run-81, burned wall-clock reading
instead of encoding). The lesson: when the question is a *finite existence*
question over a bounded configuration, an exact CP-SAT encoder with a symmetry
break is the right instrument, and its OPTIMAL verdict is the deciding artifact —
sampling and time-out MILP are not.

```claim
id: super-simple-22242-exists
statement: A super-simple 2-(22,4,2) design EXISTS. Constructive certificate:
  code/out/coclique_lift_clean_design.txt, 77 blocks of size 4 on 22 points,
  every point in exactly 14 blocks, every pair in exactly 2 blocks, and no two
  blocks sharing a triple (max triple overlap 1). Produced by OR-Tools CP-SAT
  (code/out/coclique_lift_cpsat.py), OPTIMAL in 167.35s, 7315 booleans, 156131
  branches; independently verified by direct integer counting (degrees all 14,
  231 pairs all covered twice). Consequence: a tight 22-coclique in a putative
  srg(99,14,1,2) would force the outside neighbourhoods to form exactly such a
  design, and that design exists — so the coclique-lift design condition is
  satisfiable and cannot rule out alpha=22. The route is closed as
  NON-OBSTRUCTIVE (a sixth closed route in solution.md §2), not as a refutation
  of the graph; it bears on neither existence nor nonexistence.
hypotheses: none needed for the design's existence (a pure design-theoretic
  fact, checked); the bearing on srg(99,14,1,2) assumes the tight-coclique force
  (claim coclique-alpha22-forces-22242-design) and lambda=1, mu=2.
holds-here: yes — the design existence is a standalone checked fact; the
  non-obstructive bearing on the coclique route follows from the force.
status: checked (CP-SAT OPTIMAL + independent integer verification).
bearing: answers super-simple-22242-gap in the affirmative, so the coclique-lift
  line cannot produce an alpha<22 constraint via the design; the line is closed.
answers: super-simple-22242-gap
anchor: code/out/coclique_lift_cpsat.captured.txt, code/out/coclique_lift_clean_design.txt,
  code/out/coclique_lift_cpsat.py
follows-from: coclique-alpha22-forces-22242-design, super-simple-22242-gap
```
