# Internal ring gears — Gearing 101 primer (Gear Solutions)

[[research/sources/internal-ring-gears-primer-gearsolutions.full.md]] · source:
https://gearsolutions.com/departments/tooth-tips/gearing-101-a-primer-on-internal-ring-gears/

## What it establishes

Gear-industry primer on internal (ring) gears — the type of gear C is:

- An internal gear is a cylinder with teeth **on the inside** of a circular
  ring; it always mates with an external spur gear (pinion/planet).
- Spur internal gears must have the **same pitch (module) and pressure angle**
  as the mating pinion — here the 1 cm pitch makes circumference = tooth count
  for every gear, so all four (C, S, p, q planets) share one pitch.
- The internal gear's tooth profile is reentrant (concave) versus the
  convex external gear profile; the mesh is an **internal gear mesh**.
- Interference checks: involute, trochoid, and trimming interference must be
  passed; planetary systems are the standard application.

## Implication for PE620

Fixes the geometry: ring gear C of c teeth is an internal gear, and each planet
of m teeth (m ∈ {p, q}) meshes internally with C and externally with S. The
"teeth of one gear align with grooves of the other" and 1 cm pitch make each
gear's pitch circumference = its tooth count, so the pitch radius of gear with
x teeth is x/(2π). The operating pitch radii in the two meshes of a planet at
center positions imposed by tangency are then rational multiples of 1/(2π),
which is what makes the discrete phase-counting exact.

## Cross-references

- DANotes meshing summary: operating pitch radius R' = C·z_i/Σz (external
  pair); internal-mesh analog uses the ring with negative tooth count.
- Law of gearing (UNC Charlotte): constant-ratio condition.
- Drivetrain Hub / UTS / Handbook: least-mesh-angle quantization.