# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk, from the
note store, or from a session it was not present for: established results with
their basis, approaches that died and why, computed numbers, durable memory that
bears on the problem, and where two accounts disagree. It is not a catalogue of
files — `research/INDEX.md` is that — and not a narration of what agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000). The file is re-sent on
every model call in every role that reads it; length here is a bill paid many
times over. Link the file holding any detail compressed away. Durable findings
belong in Cognee; a statement nobody can trace to a source is worth none.

## Established

**Problem (PE 620, statement `problem.md`, restatement `GOAL.md`).** C: internal
ring gear, circumference c. S: sun gear, circumference s, off-centre inside C.
Four distinct planets, circumferences p,p,q,q (p<q), each tangent internally to C
and externally to S; planets may overlap each other; closest gap between S and C
boundaries ≥1cm. c,s,p,q integers ≥5. "Perfectly meshing" = constant angular
velocity ratio, teeth align with grooves. `g(c,s,p,q)` = number of valid
arrangements (finite; only discrete positions mesh). `G(n)=Σ_{s+p+q≤n} g(s+p+q,
s,p,q)`, p<q, p,s ≥5. Worked: g(16,5,5,6)=9, G(16)=9, G(20)=205; target G(500).

**Governing structure — now identified** (run past step 1; top of GOAL.md done):

1. **Least mesh angle (sourced, holds-here true)**. In a sun–ring mesh, a planet
   meshes with both gears only at angular positions that are integer multiples of
   β = 2π/(s+c) about S's center (ring C = c teeth, sun S = s teeth). Three
   independent sources: Drivetrain Hub, UTS IGS 60-1161, Gear Solutions handbook.
   Claims `least_mesh_angle` / `least_mesh_angle_uts` in `research/CLAIMS.md`.
2. **Planet-center locus is an ellipse (sourced, holds-here true)**. A circle of
   radius p tangent internally to C (radius c/2π) and externally to S (radius
   s/2π) has its center on the ellipse with foci at the centers of C and S; sum
   of focal distances = (c−p + s+p)/2π = (c+s)/2π (p cancels) ⇒ major semiaxis
   (c+s)/4π, focal separation = d = offset between centers. Source: Cut-the-Knot
   / AMM 1947; claim `tangent_circle_center_ellipse` in `research/CLAIMS.md`.
3. **Discreteness / reduction (conjectured, not yet verified)**: each planet's
   center must lie both on its ellipse AND on the angular lattice (multiples of β
   about S's center); the finite intersection is what makes g finite. This is
   believed to be the intended structural route — a counting method independent
   of the 500 bound. **Not yet confirmed against the oracle.**

The two least-mesh-angle sources agree on the same β — no contradiction.

## Ruled out

Nothing dead yet. The whole model (ellipse ∩ lattice) is unconfirmed: `code/` is
empty, so no `brute.py` oracle has been written and the model has not reproduced
any worked value. Nothing should be trusted until it does.

## Numbers

Oracle values from the statement — **still UNVERIFIED by any program** (no
`code/brute.py` exists yet):
- g(16,5,5,6) = 9,  G(16) = 9,  G(20) = 205,  target G(500).
These are the values `brute.py` must reproduce before the real method is trusted
(completion criteria in `GOAL.md`).

## Recalled

Durable memory (Cognee) now holds the three gear-geometry source cards backing
the claims above (Drivetrain Hub, UTS, Cut-the-Knot), plus a pattern_finder
session note recording that no computed data existed early on. There is still no
prior PE620 *result* to import — only sources; this run's numbers must stand on
its own computation. Earlier recall failures were transient HTTP 409s, now
resolved.

## Gaps

- **No oracle exists**: `code/` (incl. `code/out/`) is empty; steps 1 of the
  plan (understand-by-executing, reproduce 9/9/205) are incomplete.
- The exact discrete count of g from ellipse ∩ lattice, and how G(500) is summed
  without enumerating all s+p+q ≤ 500.
- Whether/how d (S↔C offset) is fixed and how the ≥1cm gap enters the count —
  geometry detail for the solver, not yet pinned down.
