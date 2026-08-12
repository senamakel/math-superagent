# A general mathematical design method of the torque-split gear transmission with idler pinion — Zhao & Li (JSME JAMDSM 2018)

[[torque-split-idler-mesh-zhao-li-2018-pdf.full]] · source:
https://www.jstage.jst.go.jp/article/jamdsm/12/7/12_2018jamdsm0127/_pdf/-char/en
(DOI 10.1299/jamdsm.2018jamdsm0127, open access)

## What it establishes (the most explicit published analogue of PE620's count)

A *universal* method for the **simultaneous meshing design** of a torque-split
transmission: input pinion (1) meshes two idler gears (2,4) that drive an output
gear (6) through two more idlers (3,5) — the duplex-idler chain, i.e. planets
meshing central gears. Redundant constraints make simultaneous meshing non-trivial;
the paper derives the meshing condition from first principles.

## The meshing condition (Sec. 3)

Work along the duplex shaft: mark the same-phase teeth on the two gears of the
duplex idler (location phase = 0 by interchangeability). Under the naming of
Fig. 5, measure the **pitch numbers** of gear 6, gear 3, gear 5 contained in the
angles θ1, θ3, the green segment; the **meshing condition is that the pitch number
between the two contact points F and H along gear 6's pitch circle is a whole number**:

    NUM6 − NUM5 − NUM3 = Z ∈ ℤ     (eq. 4)

Substituting the pitch-number definitions and the quadrilateral angle relation
θ1+θ2+θ3+θ4 = 2π gives the reduced form (eq. 6):

    z4·θ2 + z6·θ1 + z1·θ1 + z5·θ2 − z3·θ4 − z4·θ4 + (…) = 2π·N,   N ∈ ℤ

Then cosine-law on the quadrilateral diagonals gives two more relations (eq. 11-12),
all four reduce to a **single transcendental equation in θ1** (eq. 13),
`θ1 = arccos[(c−a·cos β)/(d·sin β)] + …`, solved by Newton iteration; θ2, θ3, θ4 then
follow linearly (eqs. 28-30). **For each integer N the transcendental may have 0, 1,
or 2 solutions** (the curve has a turning point, e.g. N=402 gives two θ1 values);
each valid (N, θ1) is a distinct simultaneous-meshing configuration — and in
general **numerous discrete solutions coexist for one tooth-number design**.

Internal-mesh duplex idler (Sec. 3.2) — the ring/sun/planet sign case — has its own
starting equation (eq. 39: `z4·θ2 + z6·θ1 − z1·θ1 − z5·θ2 − z3·θ4 − z4·θ4 = 2π·N`)
and the same transcendental machinery. Planetary duplex idler (Sec. 4.1, q planets
on a carrier) reduces to `z1 − z3·(z2+z6)/z2 = q·N` (eq. 75): **the
(Z_sun+Z_ring) divisibility-type condition**, matching Guo (5.21).

## Implication for PE620

This is the strongest available precedent: a *derived*, source-level statement that
simultaneous multi-planet meshing is counted by (i) signing the angle×tooth-count
sums by mesh type (internal vs external — the ring terms carry the opposite sign),
(ii) requiring the sum to equal an integer multiple of 2π, and (iii) counting the
discrete θ1-solutions of the resulting transcendental over integer N levels — with
multiple N, and multiple solutions per N. Every element matches the thread
`offcentre-mesh-phase-model` (W-invariant, discrete d, count over crossings).
It validates the sign convention (ring teeth negative on internal mesh) that the
oracle had to pin.

**What it does not settle**: a closed form for g (the transcendental is solved
numerically per N; the paper never aggregates counts); no guidance on the
upper/lower bound of the N range beyond the curve's limit positions; no
multiplicativity/gcd structure.

```claim
id: zhao_li_2018_duplex_idler_meshing_condition
statement: For a torque-split transmission through two duplex idlers meshing input and output gears, the simultaneous-meshing condition is that the pitch number between the two contact points on the output gear is a whole number; after substitution this becomes a signed sum of (central-angle × gear tooth-count), signed + for external mesh and - for internal mesh, equal to an integer multiple of 2*pi; the geometric closure gives a single transcendental in one centre-angle whose roots over integer N are the (discrete, possibly two-per-N) simultaneous-meshing configurations.
hypotheses: standard spur gears; ideal involute; location phase of duplex idlers set to zero (interchangeability); module m.
holds-here: yes in structure — PE620's planets are the idlers, its sun and ring the input/output gears; the signed angle*tooth-count = integer*2pi sum is the thread W-invariant; the per-N two-solution structure matches the interior-vs-boundary multiplicity the run must count.
status: sourced (Zhao & Li 2018, JSME, Section 3 eqs. 4,6,13 & Sec. 3.2 eq. 39; Newton solutions for the 21/30/30/17/17/100 example)
bearing: strongest independent derivation that PE620's g is a count of discrete roots of a signed angle*tooth-count transcendental over integer levels — i.e. the W-model, not a lattice, is the right discreteness.
anchor: research/sources/torque-split-idler-mesh-zhao-li-2018-pdf.full.md
answers: off-centre-mesh-phase-model (sign convention + counting mechanism)
```

## Cross-references

- Segade-Robleda 2012 (IntechOpen) — same condition for the coplanar four-gear
  case, less general derivation; Zhao-Li cites and generalises it.
- Kurasov 2020 — off-centre eccentric case as integer angle×tooth-count congruence.
- Guo 2011 eq. 5.21-5.25 — the coaxial assembly lattice; this paper's planetary
  duplex-idler case reduces to the same (Z_s+Z_r)/q form.
