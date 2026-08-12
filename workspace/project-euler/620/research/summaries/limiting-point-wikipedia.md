# Limiting points and coaxal reduction by inversion — Wikipedia

[[research/sources/limiting-point-wikipedia.full.md]] · source:
https://en.wikipedia.org/wiki/Limiting_point_(geometry)

## What it establishes (the geometric substrate of candidate inversion-coaxial)

For two non-intersecting circles *A*, *B* in the plane, their **limiting points**
p satisfy (any one is equivalent to all three):

1. The pencil (coaxal family) of circles through *A* and *B* contains a
   degenerate (zero-radius) circle centred at p.
2. Every circle or line perpendicular to both *A* and *B* passes through p.
3. **An inversion centred at p maps *A* and *B* to concentric circles.**

The midpoint of the two limiting points is where the radical axis of *A*, *B*
crosses the line of centres; the limiting points lie on the line of centres on
either side of that crossing. They are the solutions of a quadratic in the
centre coordinates and radii (Weisstein formula); one limiting point inverts to
the other, and an inversion centred at one limiting point maps the other to the
common centre of the concentric images.

## Implication for PE620's candidate `inversion-coaxial`

This is exactly the classical fact the candidate's geometric half relies on:
C (ring, radius c/2π) and S (sun, radius s/2π, off-centre) are two
non-intersecting (nested) circles, so inversion about a limiting point DOES map
them to concentric circles C', S'. Inversion is conformal and maps circles to
circles preserving tangency — so the off-centre configuration becomes a coaxial
Steiner-chain picture with equal-radius (congruent) chain circles.

BUT — and this is the caveat every solver must weigh — inversion is NOT
length-preserving along the inverted circles. Equal 1cm tooth pitch on C maps
to *non-uniform* pitch on C', and the *number of teeth* along C' is not an
integer commensurate with an inverted angular step. So the coaxial
least-mesh-angle lattice 2π/(Z'_sun + Z'_ring) of the *inverted* train (which
needs equally pitched integer teeth) is not 2π/(c+s) of the original, and the
tooth-phase/meshing condition does not transform cleanly. The geometry reduces;
the tooth count does not. This is the structural obstruction to using the
inverted frame for the gear count.

```claim
id: inversion_does_not_preserve_tooth_mesh
statement: Circle inversion about a limiting point maps the off-centre gears C (ring) and S (sun) to concentric circles C', S', preserving tangencies and angles; but the tooth-mesh validity of a PE620 arrangement is NOT invariant under this inversion, because inversion is conformal, not an isometry — a 1cm tooth pitch on C maps to a non-uniform pitch on C', the integer tooth totals c, s of the original have no clean analogue in the inverted frame, and the coaxial least-mesh-angle step of the inverted train is not 2*pi/(c+s) of the original. Hence the tooth-count/meshing condition does not transform through the inversion, so g cannot be read off the inverted (concentric) picture.
hypotheses: ideal inversion preserving tangency and angles (classical, e.g. Coxeter 1969); gear teeth at uniform pitch-1cm in the ORIGINAL frame.
holds-here: yes — the geometry maps, but the meshing test (which is metric, arc-length/pitch-1cm, tooth-count based) is not inversive-invariant.
status: solid (classical geometry: limiting points / inversion map to concentric, conformal not isometric; the non-preservation of tooth count/pitch follows from conformality not being an isometry).
bearing: refutes candidate `inversion-coaxial` as a complete counting route: the geometric half is real, but the counting half (that the inverted coaxial train's meshing condition gives g) does not follow.
anchor: research/summaries/limiting-point-wikipedia.md
contradicts: inversion-coaxial (approach file)
```

## Cross-references

- MathWorld "Inversion" and "Limiting Point" (Coxeter 1969; Casey 1888): same
  limiting-point-to-concentric fact; inversion maps non-intersecting circles to
  concentric ones; circles to circles; angles preserved.
- Steiner chain / Steiner's porism (Wikipedia, MathWorld, Cut-the-Knot): the
  inversion-to-concentric construction is the standard proof device for
  Steiner chains; concentric case gives equal congruent chain circles spaced by
  2π/n.
- On-disk `tangent_circle_center_ellipse` / `pappus_center_ellipse_params` /
  `steiner-chain-wikipedia`: the shared-ellipse locus of chain-circle centres
  (geometry only). The tooth-count half does not invert, per claim
  `inversion_does_not_preserve_tooth_mesh`.
