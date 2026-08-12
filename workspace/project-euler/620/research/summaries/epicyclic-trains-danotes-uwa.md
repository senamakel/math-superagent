# Epicyclic gear trains — DANotes (University of Western Australia)

[[epicyclic-trains-danotes-uwa.full]] · source:
https://danotes.mech.uwa.edu.au/gears/epicyclic/epicyclic.html (Douglas Wright, UWA)

## What it establishes (the 3-component force/velocity relations, with the internal-gear sign convention)

Defines an epicyclic element: central gear (external = sun, or **internal** = ring),
rotating arm (spider/carrier), freely-rotating planet on the arm's axle. The central
tooth count z_c is **positive for an external central gear, negative for an internal
central gear** — the sign convention the run's W-model needs. Then the two "element"
relations:

    (2a)  (ω_c − ω_a)·z_c + (ω_p − ω_a)·z_p = 0
    (2b)  T_c/z_c = T_p/z_p = −T_a/(z_c + z_p)

(velocity relation for the external case Ra=Rc+Rp; internal case Ra=Rc−Rp; the single
equation covers both once z_c is signed). One kinetic (torque) degree of freedom, two
kinematic degrees; energy/torque-balance checks pass. Multiple identical planets are
analytically irrelevant to (2a)/(2b) (the total planet torque T_p is shared equally).

## Implication for PE620

PE620's ring C is an **internal gear** (teeth on the inside): under this convention
z_c is negative, which is exactly where the "-c·χ" sign in the thread's W-invariant
`s·φ + c·χ − t·γ` comes from — the internal-ring mesh accumulates tooth phase with the
opposite sign to the external sun mesh. The single velocity relation (2a) with signed
z_c is the cleanest statement of the internal-ring sign rule the run's residue variants
had to pin empirically. **Confirmed by three independent kinematic routes** (Wikipedia
carrier-speed denominator, tec-science Willis, this element equation).

**What it does not give**: no assembly/meshing discreteness (it is a kinetics-only
treatment), so it bears only on the sign convention, not on the finite count.

```claim
id: internal_ring_negative_tooth_count_convention
statement: In the epicyclic element relation (omega_c - omega_a)*z_c + (omega_p - omega_a)*z_p = 0 with torques T_c/z_c = T_p/z_p = -T_a/(z_c+z_p), the central-gear tooth count z_c is taken positive for an external (sun) gear and negative for an internal (ring) gear; this single signed equation covers both Ra=Rc+Rp and Ra=Rc-Rp in one form, and the internal ring therefore enters all ratios with opposite sign to the sun.
hypotheses: ideal epicyclic element; rolling-without-slip pitch circles; negligible friction; X-zero teeth.
holds-here: yes — PE620's C is the internal ring (z_c = -c), S the sun (positive s); fixes the sign of the ring-mesh phase (-c*chi) in the W-invariant.
status: sourced (DANotes/Wright, UWA; corroborated by Wikipedia carrier-speed formula and tec-science Willis)
bearing: pins the ring-term sign in the off-centre phase model, matching the oracle-checked residue variant (sigma=-1, eta=-1).
anchor: research/sources/epicyclic-trains-danotes-uwa.full.md
```
