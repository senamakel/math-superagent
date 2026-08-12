# Planetary Gears — Geometry (Drivetrain Hub)

[[research/sources/planetary-gears-geometry-drivetrainhub.full.md]] · source:
https://drivetrainhub.com/notebooks/gears/geometry/Chapter%204%20-%20Planetary%20Gears.html

Standard-planetary geartrain: sun gear (z1) + planet gears (z2) + ring gear (z3,
signed *negative* for internal gear). Carrier V. All non-zero angular velocities possible.

## Constraints
- **Center distance**: sun–planet and planet–ring working center distances equal:
  |a12| = |a23|, i.e. |d_w1 + d_w2| = |d_w2' + d_w3|. Ring teeth are taken negative.
- **Planet interference**: planet center distance l = 2a·sin(π/N) must exceed planet
  tip diameter d_a2.
- **Meshing teeth**: integer tooth counts required; each planet must mesh with both
  sun and ring. Assembly: position sun, add first planet, position ring, then a second
  planet fits only at certain carrier angles.
  - *Equal spacing*: k = (z1 − z3)/N must be an integer.
  - *Unequal spacing*: the **tick angle** (== least mesh angle) is
    **θ̂ = 2π/(z1 − z3)**. Legal planet positions are multiples of θ̂. Since z3 < 0,
    z1 − z3 = z_sun + z_ring. For our problem that is **2π/(s+c)** where s = sun
    tooth count and c = ring tooth count (both positive; ring contributes additively).
- **Mesh phasing**: ring tooth pitch ψ_t3 = 2π/z3; phase angle of planet i from
  q_3i = θ_i/ψ_t3 mod 1. Phasing type from k_φ = |z3| mod N.

## Implication for PE620
The discreteness that makes g finite is exactly this: each planet's angular position
around the sun (S) must be a multiple of the least mesh angle 2π/(s+c). This is the
quantization constraint. (The source treats planets on a rigid carrier; the problem
generalizes to four planets of two sizes p,p,q,q allowed to overlap, so positions are
independent multiples of the least mesh angle, subject to tangency l(center) conditions.)

```claim
id: least_mesh_angle
statement: In a sun–ring–planet geartrain with sun tooth count z1 and ring tooth
count z3 (taken negative for an internal gear), the smallest allowable relative
angular step between planet positions that keeps every planet meshed with both sun
and ring is the tick angle theta_hat = 2*pi/(z1 - z3) = 2*pi/(z_sun + z_ring); legal
planet angular positions are integer multiples of it.
hypotheses: perfect meshing (constant angular-velocity ratio, teeth align with
grooves); internal ring gear (negative z3); integer tooth counts.
holds-here: true — this is exactly the PE620 "perfectly meshing" condition applied
to the C/S coaxal pair with tooth counts c and s.
status: sourced (Drivetrain Hub planetary notebook; corroborated by UTS and Gear
Solutions handbook).
bearing: gives the quantization step 2*pi/(s+c) that makes g finite and countable.
anchor: research/summaries/planetary-gears-geometry-drivetrainhub.md
```
