# Epicyclic Gearing: A Handbook (Gear Solutions)

[[research/sources/epicyclic-gearing-handbook-gearsolutions.full.md]] · source:
https://gearsolutions.com/features/epicyclic-gearing-a-handbook/

A practical design handbook for planetary (epicyclic) gear trains. (No claim blocks
here — this is corroborating qualitative background, not a distinct theorem source.)

## Content
- Types and arrangements (planetary 3:1–12:1, star, solar), relative speeds of sun/
  planet/ring/carrier, torque splits, multiple-mesh considerations, assembly constraints.
- **Assembly**: planet placement creates fixed angular relationships; the **least mesh
  angle equals 360° divided by (sun teeth + ring teeth)**; additional planets must sit
  at multiples of this angle; equal spacing needs (sun teeth + ring teeth) divisible by
  the number of planets.
- Relative speeds: with the carrier as reference, sun/planet/ring speeds relate via
  tooth counts (Willis-type relations).
- Design notes: planets act as idlers (do not set the sun-to-ring ratio); tweaking the
  planet tooth count can improve meshing; avoid extreme center distances.

## Implication for PE620
Corroborates the least-mesh-angle = 360°/(sun + ring) rule (with ring= C, sun= S,
i.e. 360°/(c+s)) from an independent authoritative gear-design source, consistent with
the Drivetrain Hub "tick angle" 2π/(z1 − z3) and the UTS least-mesh-angle formula.
Treats ~60 planet sizing as a free adjustable choice, consistent with the idler freedom.

```claim
id: least_mesh_angle_handbook
statement: In planetary gears, the least mesh angle (smallest legal angular step
between planet positions) is 360 degrees/(sun teeth + ring teeth); planets must be
placed at multiples of it; equal spacing additionally requires (sun+ring)/n_planets
an integer.
hypotheses: integer tooth counts; epicyclic (sun-ring-planet) gear train; perfect
meshing.
holds-here: true — PE620 with sun=S (s teeth) and ring=C (c teeth) gives least mesh
angle 360/(s+c).
status: sourced (Gear Solutions handbook; corroborated by Drivetrain Hub, UTS).
bearing: independent third confirmation of the discreteness step.
anchor: research/summaries/epicyclic-gearing-handbook-gearsolutions.md
```
