# Phase Management to Reduce Gear Whine in Idler Gear Sets — White & Patil (Power Transmission Engineering, 2020)

[[idler-gear-set-phase-whine-white-patil.full]] · source:
https://ik.imagekit.io/agmamedia/issues/0420/gear-whine.pdf (AGMA, open distribution)

## What it establishes (the idler double-mesh tooth-phase condition, first-principles)

An idler gear meshes two non-contacting gears; its two meshes must be phase-consistent.
Though written for vibration, Appendix A derives the purely kinematic phase condition —
the *same* object as PE620's planet satisfying two meshes (one to each central gear).

Appendix A (nomenclature: gear 1 = driving, 2 = idler, 3 = driven; r = base radius,
η = working pressure angle, z2 = idler teeth):

- λ1, λ3 = mean roll angles between LPSTC and HPSTC for the two idler meshes
  (eqs. A.3, A.5), functions of centre distances C1, C3, pressure angles η1, η3,
  addendum radii r_Ai, base radii r_i.
- (A.7): `σ2^R = σ2^L_…`: the tooth thickness term `2·tan φ_t − 2·φ_t + t_w·cos φ_t)/r2`
  is the angle subtended by the tooth thickness at the base circle.
- **The key index condition** (A.8): the number of idler teeth indexed in rotating
  from the left-flank origin `σ2^L` to the right-flank origin `σ2^R` is
  `N = z2·(σ2^L − σ2^R)/(2π)`. **When N is an integer, both meshes occur
  simultaneously and are perfectly in phase**; the phase shift in degrees is the
  mantissa of N × 360.

So: **an idler gear meshing two central gears is simultaneously/perfectly meshed iff
`z2·(σ2^L − σ2^R)/(2π)` is an integer** — the discrete tooth-phase condition that makes
the two meshes compatible. The appendix states the two meshes are perfectly in phase
exactly when N ∈ ℤ, and derives N as an explicit function of the three centre-line
geometries and the idler tooth count.

## Implication for PE620

This is the *only source on disk that derives, from tooth geometry, the exact
discreteness of a gear satisfying two simultaneous meshes through its own tooth count*
— exactly one planet's situation. It confirms that the double-mesh compatibility is a
**modulo-integer condition on a function of the planet's tooth count and its two contact
geometries** (here z2×angular-span/2π), matching the thread's
`offcentre_dual_mesh_phase_invariant` (each planet's W invariant in ℤ-equivalence).
It independently corroborates that the discreteness is set by the *planet's own teeth*,
not only the two central tooth counts — supporting the W-model's `t·γ` planet term.

**What it does NOT give**: the A.8 index is for a straight external-external idler
chain between two fixed centre distances, with fixed positions — not PE620's
ellipse/off-centre positions or the extra freedom of sliding d; it is a whine paper so
the phase is used to size a force ellipse, not to count configurations. It establishes
the *kind* of congruence (integer N on a tooth-count×angle product), not the closed
form for g.

```claim
id: idler_double_mesh_integer_index_condition
statement: An idler gear of z2 teeth meshing two non-contacting gears is perfectly/ simultaneously in phase when N = z2*(sigma2^L - sigma2^R)/(2*pi) is an integer, where sigma2^L, sigma2^R are the origins of involute of the two tooth flanks in contact, functions of the two centre distances, working pressure angles, addendum and base radii.
hypotheses: standard spur gears; involute flank origins at pitch point; two fixed centre distances; X-zero ideal teeth.
holds-here: yes in structure — a PE620 planet is exactly such a gear meshing two central gears; the double-mesh compatibility is an integer condition on the planet's tooth count times the angular span between its two meshes.
status: sourced (White & Patil 2020, App. A eqs. A.3-A.8)
bearing: corroborates that the planet's own tooth count enters the discreteness (W-model's t*gamma term), and that the double-mesh condition is an integer-on-product congruence.
anchor: research/sources/idler-gear-set-phase-whine-white-patil.full.md
```

## Also (why this paper was downloaded)

Main body: idler gear whine from transmission-error force ellipse; phasing (relative
mesh phase) of the two idler meshes controls the ellipse; odd harmonics minimised at 180°
phase, even at 90°. Not relevant to the count — recorded so it is not re-read for PE620.
