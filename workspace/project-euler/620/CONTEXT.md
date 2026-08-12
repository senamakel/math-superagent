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

**Working model — concrete and implemented, NOT yet run against the oracle.**
`C` at the origin, radius R=c/2π; `S` at (d,0), radius r=s/2π. The free
parameter is the centre distance d (S↔C offset); the ≥1cm gap gives
R−r−d ≥ 1. A planet of circumference m (ρ=m/2π) tangent internally to C and
externally to S has its centre on circle(O, R−ρ) ∩ circle(S, r+ρ) — up to two
points, mirror images across the line of centres. So each planet type has two
forced candidate positions; a chosen d fixes the four planet positions. This
(not a free "plane lattice") is the discrete configuration space.

**Meshing reduces to a single scalar condition (derived in `lib/gears.py`,
unverified).** The four planets give 8 tooth-alignment congruences in 6 gear
phases; eliminating the phases (integer 3-dim left nullspace of the 8×6 matrix)
leaves three consistency conditions that must all be (near-)integers:
`2F_p, 2F_q, H ∈ ℤ (mod 1)`, where F_m = β_m·R − γ_m·r − T_m and H = (β_p−β_q)·R
− (γ_p−γ_q)·r − (T_p−T_q), with β the planet's angle about O, γ its angle about
S, T the planet arc between its two contacts. `g_count` scans the d-interval and
counts d* where these hold (excluding degenerate d where a type's two positions
coincide). This is the brute/oracle route; the exact d-solver does not exist yet.

**Least mesh angle (sourced, holds-here true, reconciles with the model).** The
sourced β = 2π/(s+c) is the angular step keeping planets meshed; Drivetrain Hub
gives it as tick angle 2π/(z₁−z₃) with z₃ *negative* for an internal gear, i.e.
2π/(z₁+|z₃|) = 2π/(sun+ring) — consistent with UTS and Gear Solutions, no
contradiction. Claims `least_mesh_angle*` in `research/CLAIMS.md`.

**Planet-center locus is an ellipse (sourced, holds-here true)**, foci at C and
S centres, major semiaxis (c+s)/4π (p cancels); the equivalent two-circle
framing above is what gears.py actually uses. Claim `tangent_circle_center_ellipse`.

## Ruled out

Nothing dead yet — but nothing is trusted either. The two-circle + phase-
consistency model (`lib/gears.py`) is implemented yet has produced **no output**
(`code/out/` empty): it has not reproduced 9/9/205, so the meshing/arrangement
reading is still unconfirmed. Do not build on the model as fact until the oracle
matches.

## Numbers

Oracle values from the statement — **still UNVERIFIED by any program** (no run
output exists; `brute.py`/`solution.py` not written):
- g(16,5,5,6) = 9,  G(16) = 9,  G(20) = 205,  target G(500).
`lib/gears.py` computes g(c,s,p,q) by continuous d-grid scan (mpmath/scipy); it
must reproduce these before the exact method is trusted.

## Recalled

Durable Cognee memory holds the four gear-geometry source cards backing the
above claims (Drivetrain Hub, UTS, Gear Solutions, Cut-the-Knot). Scratch and
memory both confirm **no computed terms exist yet** — pattern/sequence analysis
is blocked until `code/out/` holds real g/G output. No prior PE620 result is
importable; the run's numbers must stand on its own computation.

## Gaps

- **Oracle not run**: gears.py exists in lib but nothing has executed it; no
  `code/brute.py`, no `code/out/` files, so 9/9/205 unconfirmed.
- **Exact method**: replacing the continuous d-grid scan with an exact/symbolic
  way to find the d at which 2F_p,2F_q,H are integers, and summing G(500) without
  enumerating all s+p+q ≤ 500 — cost must not grow with 500.
- The ≥1cm gap (R−r−d ≥ 1) is a bound on d; how g counts distinct valid d (and
  the forced four positions per d) enters the count is the model under test.
