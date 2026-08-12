# Simple Epicyclic Gear Design (UTS Program 60-1161)

[[research/sources/simple-epicyclic-gear-design-uts.full.md]] · source:
https://www.uts.com/resources/IGS/IGS60-1161.pdf

Simple epicyclic unit: central external sun gear meshing with external planet gears,
which mesh with an enclosing internal ring gear. Types: planetary (ring fixed), star
(carrier fixed), solar (sun fixed).

## Assembly / meshing condition
For planets to assemble between sun and ring:
- **Equal spacing**: (N_ring + N_sun)/n_p must be an integer (n_p = number of planets).
- **Unequal spacing (always needed if equal fails)**: planets must be spaced at
  multiples of the **Least Mesh Angle**
  **β = 360°/(N_ring + N_sun)**;
  i.e. ep/β = integer where ep = angle between adjacent planet gears.
- Worked example: N_ring = 68, N_sun = 18 → β = 360/86 = 4.186°. Cannot place 4
  planets 90° apart ((68+18)/4 = 21.5 not integer), but 2 planets 180° apart works
  ((68+18)/2 = 43). Legal off-equal positions are integer multiples of 4.186°.

## Implication for PE620
This is the authoritative statement of the least-mesh-angle constraint: planet
angular positions must be multiples of β = 360°/(N_ring + N_sun) = 2π/(c + s) in our
notation (ring = C with c teeth, sun = S with s teeth). The finite count g comes from
intersecting the ellipse locus (tangency) with these quantized positions; overlap among
planets is allowed, so no additional spacing constraint among the four planets beyond
mesh alignment. (The PE620 problem has two equal small planets p and two equal large q,
so positions are not the rigid-carrier equal-spacing case; each planet is an independent
multiple of β.)

```claim
id: least_mesh_angle_uts
statement: Planets in a sun–ring epicyclic gear set (ring internal, N_ring teeth; sun
N_sun teeth) can only be placed at angular positions that are integer multiples of the
least mesh angle beta = 360/(N_ring + N_sun). Perfect meshing requires each planet be
such a multiple; equal spacing additionally needs (N_ring + N_sun)/n_p integer.
hypotheses: integer tooth counts; ring is internal gear; perfect meshing (teeth align
with grooves, constant angular-velocity ratio).
holds-here: true — PE620's S (sun, s teeth) and C (ring, c teeth) with N_ring + N_sun =
c + s, giving beta = 2*pi/(c + s).
status: sourced (UTS Integrated Gear Software 60-1161; corroborated by Drivetrain Hub
tick angle and Gear Solutions handbook).
bearing: the discreteness step of the problem; makes g(c,s,p,q) finite.
anchor: research/summaries/simple-epicyclic-gear-design-uts.md
```
