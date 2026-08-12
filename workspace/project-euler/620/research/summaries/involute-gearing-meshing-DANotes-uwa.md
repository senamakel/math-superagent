# Involute gearing: gear meshing — DANotes (UWA)

[[research/sources/involute-gearing-meshing-DANotes-uwa.full.md]] · source:
https://danotes.mech.uwa.edu.au/gears/meshing/meshing.html

## What it establishes

University (UWA) notes on the meshing geometry of involute spur gears:

- **Operating pitch radius formula**: R'_i = C·z_i/Σz — at a given center
  distance C between two meshing gears of tooth counts z_1, z_2, the operating
  pitch radii are proportional to tooth count: R'_1 = C·z_1/(z_1+z_2),
  R'_2 = C·z_2/(z_1+z_2). The pitch circles preserve the velocity ratio
  (ω₁R₁ = ω₂R₂).
- The **extended center distance** C = (R_1+s_1)+(R_2+s_2) = m(½Σz + Σs) with
  profile shifts s_i; the actual pitch point P is the line-of-action ∩
  line-of-centers.
- Contact occurs along the line of action between the two addendum circles
  (path of contact); contact ratio ε_γ = path length / base pitch; ε_γ ≥ ~1.2
  recommended; 12 teeth is the usual minimum (undercutting below).
- Gears with involute profiles preserve conjugate action under center-distance
  variation (within limits).

## Implication for PE620

The **operating pitch radius formula** is exactly what the planet position
equations need: for a sun–planet mesh at center distance a_12 = r_s + r_ρ (the
planet tangent to the sun), the operating pitch radius of the sun in that mesh
is a_12·s/(s+m) and of the planet a_12·m/(s+m), m = planet circumference; for
the internal ring–planet mesh at center distance a_23 = R_c − r_ρ, analogous
internal-gear formulas apply (ring teeth negative). These operating radii enter
the tooth-alignment (phase) equations that decide whether all four planets mesh
with both S and C simultaneously — the "perfectly meshing" condition. The
1 cm pitch and circumference = tooth count make every radius a rational
multiple of 1/(2π), keeping the eventual count exact.

## Cross-references

- Law of gearing (UNC Charlotte): why constant ratio ⟺ pitch point fixed.
- Involute tooth form (DANotes): involute profile construction.
- Internal ring gears primer (Gear Solutions): internal-mesh analogs and
  interference.