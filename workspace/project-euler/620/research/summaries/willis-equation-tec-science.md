# Willis equation — kinematics of epicyclic gears (tec-science)

[[research/sources/willis-equation-tec-science.full.md]] · source:
https://www.tec-science.com/mechanical-power-transmission/planetary-gear/fundamental-equation-of-planetary-gears-willis-equation/

## Claimed content (from digest + excerpt)
The planet gear's motion is the superposition of three motions: (1) carrier rotation
about the sun, (2) the planet's self-rotation from rolling on the sun, (3) the sun's
own rotation. Rolling without slip ties the angular velocities through pitch-circle
diameter ratios.

- At sun–planet contact: v_s = v_c − v_p ; at planet–ring contact: v_r = v_c + v_p.
- Rearranged: v_p = v_r/2 − v_s/2, leading to the Willis equation, e.g.
  **n_p·d_p = n_c·(d_p + d_s) − n_s·d_s** with pitch diameters d and speeds n.
- The planet's effect on the sun–ring transmission ratio is nil (it is an idler).

## Implication for PE620
"Perfectly meshing" means constant angular-velocity ratio among the gears. The Willis
equation expresses this as a linear relation between ω_s, ω_p, ω_r (sun, planet, ring).
For the ratio to be constant (independent of time) the tooth counts (c,s,p,q) must make
the pitch ratios rational and the drive must keep the contact velocities matched — this
is the kinematic half of perfect meshing; the *alignment/phase* half is the least-mesh-
angle quantization (2π/(c+s)) and the modular tooth-alignment condition. This source
establishes that the planet can have essentially any tooth count ("multiple values of
planet tooth count are possible") for a given sun/ring ratio — so p,q are free integers,
not constrained by a rigid relation.

```claim
id: planet_idler_freedom
statement: In a standard sun–planet–ring epicyclic train the planet acts as an idler:
it does not affect the sun-to-ring transmission ratio, and multiple values of the planet
tooth count are compatible with a given sun/ring ratio. The kinematic (constant angular
velocity ratio) condition is a linear Willis relation among sun, planet, ring angular
velocities via pitch-diameter ratios.
hypotheses: rolling without slip; involute (circular-pitch) gears; sun external, ring
internal.
holds-here: true — PE620's planets of circumferences p and q each mesh with S (sun,
s teeth) and C (ring, c teeth); p,q are free integers ≥5, only constrained by geometry
(tangency) and meshing alignment, not by a fixed ratio formula.
status: sourced (tec-science Willis equation; corroborated by Drivetrain Hub).
bearing: separates the "which (c,s,p,q) are valid" question from the "how many
arrangements" question; the planet tooth counts are free, so the count concentrates on
the finite set of legal planet angular positions.
anchor: research/summaries/willis-equation-tec-science.md
```
