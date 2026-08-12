# Split Torque Gearboxes — Segade-Robleda, Vilán-Vilán, López-Lago, Casarejos-Ruiz (IntechOpen 2012)

[[split-torque-gearboxes-core-2012.full]] · source:
https://core.ac.uk/download/322413681.pdf (chapter DOI 10.5772/37258, open access CC-BY)

## What it establishes (the four-gear simultaneous-meshing condition)

Treats exactly the PE620 structure: a driving pinion meshes two idler pinions which
both act on a fourth gear ("four-gear meshing" = two planets meshing two central
gears). The **simultaneous-meshing discreteness** is expressed as a *curvilinear
quadrilateral* formed by portions of the pitch circles, and:

> **Meshing condition**: for perfect simultaneous engagement of the four gears the
> **pitch difference** — the sum of pitches in the input and output gears minus the
> sum of pitches in the idler gears at the curvilinear quadrilateral — must be a
> **whole number of pitches**.

Eq. (1), four-outside case: `r1·α + r2·β − r3·γ − r4·δ = n·π·m`, `n ∈ ℤ`
(pitch radius × centre-angle, signed by mesh type, = integer × π × module). This
is the *same structural object* as the PE620 thread's W-invariant
`s·φ + c·χ − t·γ ≡ 0 (mod π/2π)` — a signed sum of (angle × tooth-count/pitch)
equated to an integer multiple of π. Case 2 (three outside + one ring) gives the
ring-mesh variants with the ring terms signed differently,
`z1·α + z2·β + z3·γ − z4·δ = π·...·(z3+z4)` (crossed) and the − variant
(non-crossed).

Building the rectilinear quadrilateral of the four centres closes the system; one
angle (α) is solved from a single transcendental equation by arccos-of-cosines in
tooth counts, then β, γ, δ follow. Worked example (z1,z2,z3,z4)=(30,50,20,12):
valid `n` ∈ {−12,−11,−3,−2,−1,0,1,2,3,4,7,29,30} — **a discrete set of n-levels
crossed by the monotone transcendental**, exactly the structure the PE620 thread
expects for g (crossing of a monotone residue by integer levels).

## Implication for PE620

This is an independent derivation-level confirmation (a journal/book source, not a
design guide) that *simultaneous multi-gear meshing through idlers is counted by a
signed angle×tooth-count sum equalling an integer multiple of π*. It directly
corroborates `offcentre_dual_mesh_phase_invariant` in shape and in mechanism
(transcendental root-finding over integer levels), and confirms the counting is a
root-count over isolated `n`, not a lattice enumeration. The sign of the ring terms
matching the internal/external mesh is precisely the "-c·χ" and "+t·γ" sign freedom
the thread had to pin by the oracle.

**What it does NOT give**: a closed form or gcd-only formula for g; no guide to the
mirror-pair/Möbius structure; works with module-cm not x-zero pitch-1cm teeth (same
counting either way for ideal involutes). No sub-cubic algorithm for G(500).

```claim
id: split_torque_curvilinear_quadrilateral_condition
statement: In a coplanar simultaneous four-gear mesh (input pinion + two idler pinions acting on one output gear), the perfect-simultaneous-meshing condition is that the pitch difference around the curvilinear quadrilateral joining the pitch circles be a whole number of pitches; written r1*alpha + r2*beta - r3*gamma - r4*delta = n*pi*m for a whole n, with signs depending on internal/external mesh type.
hypotheses: coplanar spur gears; ideal involutes; module m; the four gear centres form a (rectilinear) quadrilateral.
holds-here: yes in structure — PE620 is the ring/sun/two-planets special case (two central gears instead of two idlers); the signed angle*tooth-count sum = integer*pi is the thread W-invariant form.
status: sourced (Segade-Robleda et al. 2012, IntechOpen, eq. (1)-(7); worked n-set for 30/50/20/12)
bearing: corroborates the off-centre phase-congruence discreteness at source level; confirms g is a count of integer-level crossings of a monotone transcendental in d, not a search.
anchor: research/sources/split-torque-gearboxes-core-2012.full.md
answers: off-centre-mesh-phase-model (structure corroboration)
```

## Cross-references

- Zhao & Li 2018 (torque-split idler, JSME JAMDSM): the universal design method
  that *derives* the same meshing condition for the duplex-idler case, with the
  transcendental equation and Newton solution — more general proof.
- Kurasov 2020 (gear eccentric systems): the off-centre case as integer congruence
  of angle×tooth-count.
- Thread `offcentre-mesh-phase-model`: the PE620 W-invariant this corroborates.
