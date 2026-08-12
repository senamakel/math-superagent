# Steiner's Porism (Steiner's Chain) — Cut-the-Knot

[[research/sources/steiner-porism-cut-the-knot.full.md]] · source:
https://www.cut-the-knot.org/Curriculum/Geometry/SteinerChain.shtml
(Alexander Bogomolny)

## What it establishes

**Steiner's porism:** for two concentric circles, either there exists a closed
chain of circles tangent to both parent circles and to their neighbours, or no
such chain exists; and in the former case the chain can be started at *any*
point of the annulus between the two given circles. The transparent proof is by
circle inversion: invert a symmetric (concentric) packing to get a general
Steiner chain.

## Implication for PE620

This is the *existence/variety* half of the geometry: it confirms there is a
continuous one-parameter family of circle arrangements tangent to both given
circles (a *porism* — infinitely many rotate into each other), exactly the
continuous freedom that the PE620 "perfectly meshing" discreteness must cut to a
finite set. It also reaffirms the inversion-to-concentric device (chain circles
become equal and equally spaced 2π/n in the concentric frame).

It does **not** decide which of the continuous family are meshing positions —
that is the gear/teeth half (least-mesh-angle / phase congruence), which is
orthogonal to Steiner-chain theory. So it supports candidate `inversion-coaxial`
only on the geometry side, not on the tooth-count side (which the notes on
`limiting-point-wikipedia` argue inversion does not preserve).

## Cross-references

- Steiner chain (Wikipedia) / MathWorld: inversion → concentric; equal chain
  circles in the annular case; porism statement.
- Eppstein Geometry Junkyard "Steiner's Porism": same porism, inversion proof.
- On-disk `tangent_circle_center_ellipse` / `pappus_center_ellipse_params` /
  `steiner-chain-wikipedia`: ellipse locus of chain-circle centres.
