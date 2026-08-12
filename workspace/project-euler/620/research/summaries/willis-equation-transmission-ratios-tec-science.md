# Transmission ratios of planetary gears: Willis equation — tec-science

[[research/sources/willis-equation-transmission-ratios-tec-science.full.md]] ·
source:
https://www.tec-science.com/mechanical-power-transmission/planetary-gear/transmission-ratios-of-planetary-gears-willis-equation/

## What it establishes

The Willis (fundamental) equation of the planetary gear set, in the version of
the companion article:

    n_p · z_p = n_c · (z_p + z_s) − n_s · z_s

(n_x = rotational speeds of planet/carrier/sun; z_x tooth counts). Transmission
ratios for the variants: fixed sun (planetary), fixed ring (star), fixed
carrier (solar), direct drive. The stationary (carrier-fixed) transmission
ratio is the reference for the ratio n_p/n_s etc.

## Implication for PE620

The constant angular-velocity-ratio requirement ("perfectly meshing") is exactly
what the Willis equation encodes: with all gears meshing, the three tooth-count
integers and angular velocities satisfy the linear relation above. This is the
kinematic half of "perfectly meshing"; the geometric half (fixed angular
positions at multiples of the least mesh angle 2π/(c+s)) is what the gear
sources (Drivetrain/UTS/Handbook) and the tooth-alignment equations in
`code/lib/gears.py` use. So Willis fixes the *ratio* condition; the discrete
*position* condition is the least-mesh-angle theorem.

## Cross-references

- Drivetrain Hub / UTS / Handbook summaries: least-mesh-angle quantization.
- `code/lib/gears.py`: the 8 phase-alignment equations (eliminated to 3
  consistency conditions) that implement meshing in coordinates.