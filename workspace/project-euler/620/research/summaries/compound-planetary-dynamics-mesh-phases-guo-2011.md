# Analytical Study On Compound Planetary Gear Dynamics — Guo 2011 (OSU PhD thesis, advisor R.G. Parker)

[[research/sources/compound-planetary-dynamics-mesh-phases-guo-2011.full.md]] · source:
https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1312289370&disposition=attachment

## What it establishes (the derivation-level tier the library lacked)

**Chapter 5 (Mesh Phase Relations)** is the key one for PE620. It defines system-,
stage-, and train-level mesh phases and derives them from gear geometry and **assembly
conditions**, verifying all formulas against the geometrically-exact finite-element
benchmark Planetary2D (page 122-131, Tables 5.5-5.7).

- **Table 5.1 — train-level relative phases.** The sun–planet mesh phase of train l
  relative to train 1 is `γ̄_s = dec(Z_s^g·ψ̂_il / 2π)` (counter-clockwise sun), where
  `ψ̂_il` is the planet's angular position relative to the carrier and `dec` takes the
  fractional part. Explicit in sun/ring/planet tooth counts.
- **Equation (5.21) — the assembly condition (simple planetary gear, d_i = 1):**
  `(Z_r^g + Z_s^g)·ψ̂_il = 2π·n_il`, n_il an arbitrary integer. This is the exact
  statement the run needs: a planet meshing both sun and ring can only sit at angular
  positions that are integer multiples of **2π/(Z_ring + Z_sun)**. The least-mesh-angle
  rule, previously asserted by design guides (UTS, Gear Solutions, Drivetrain Hub), is
  here *derived* and cited to Muller, *Epicyclic Drive Trains*, 1982 [68] and
  Parker & Lin, ASME JMD 126(2):365–370 (2004) [77].
- **Equation (5.25)**: general assembly condition for d_i planets per train:
  `ψ̂_il = 2π·n_il / (Z_r^g + (−1)^{d_i+1} Z_s^g)`. For d_i = 1 (the PE620 case: each
  planet is its own train) this reduces to (5.21).
- **Equation (5.22)**: under (5.21) the train-level sun–planet and ring–planet
  relative phases are equal — a planet placed at a multiple of 2π/(Z_r+Z_s) meshes
  with ring and sun in exactly the same relative teeth positions.

**Notes for the PE620 model.** The thesis treats planets on a rigid carrier with
equal spacing per train; PE620's four planets p,p,q,q are independent (not on one
carrier) and may overlap. The quantization step 2π/(c+s) for the S–C pair is the
*per-planet* condition from (5.21)-(5.22); PE620 additionally needs the tangency
ellipse to fix each planet's centre distance from S. The chapter's inequalities for
stepped/meshed-planet stages are not needed (simple stage, d_i = 1).

```claim
id: assembly_condition_simple_planetary_guo
statement: In a simple planetary stage (one planet per planet train), the assembly
  condition is (Z_ring + Z_sun)*psi_hat = 2*pi*n for an integer n; equivalently a
  planet meshing both the internal ring and the sun can occupy only angular positions
  that are integer multiples of 2*pi/(Z_ring + Z_sun). At such positions the sun-planet
  and ring-planet train-level mesh phases are equal (Guo eq. 5.21-5.22, Table 5.1).
hypotheses: integer tooth counts; internal (ring) gear with positive tooth count
  convention as used here; ideal geometry; carrier kinematics with one planet per train.
holds-here: true — PE620's S (s teeth) and C (c teeth) give the step 2*pi/(c+s);
  each of the four planets is an independent train (d_i = 1). p and q do not enter
  the step, matching the least-mesh-angle rule asserted in three design guides.
status: sourced (Guo 2011 OSU thesis, Ch. 5, eq. 5.21-5.25, Table 5.1, citing Muller
  1982 and Parker & Lin 2004; independently verified in the thesis against
  Planetary2D numerical benchmark).
bearing: the discreteness step of PE620 — the finite lattice of legal planet angles
  that makes g(c,s,p,q) finite and countable. Corroborates claims least_mesh_angle,
  least_mesh_angle_handbook, least_mesh_angle_uts at derivation level.
anchor: research/sources/compound-planetary-dynamics-mesh-phases-guo-2011.full.md
```

## Other chapters (context, not needed for the count)

Ch. 2-4: purely rotational and rotational-translational lumped models, modal
properties, eigensensitivities, veering/crossing. Ch. 6: mesh-phasing rules for
suppressing responses (k_µ = mod(µZ_s/c_planets)); the net-force/torque/modal-force
cancellation argument — a second, independent route to the same phase conditions.
Ch. 7-8: parametric instability; back-side mesh stiffness (not relevant to a kinematic
count).

## Cross-references

- Parker & Lin 2004 (JMD 126(2):365–370): the cited primary source for mesh-phase
  relations; **full text still paywalled** (only the citation is on disk via Parker's
  publication list).
- Zou 2015 (Atlantis): derives the homogeneity-distribution condition
  (Z_R + Z_S)/n_b = N (equal spacing) from a phase-alignment argument — consistent
  with (5.21).
- UTS/Drivetrain Hub/Gear Solutions: asserted least-mesh-angle rule — now upgraded
  from assertion to derived theorem.