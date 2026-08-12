# Contact dynamics of a three-gear system and idler vibration — You, Luo, Xu (Frontiers Mech. Eng. 2026)

[[idler-three-gear-mesh-phase-frontiers-2026.full]] · source:
https://www.frontiersin.org/articles/10.3389/fmech.2026.1721474/full (DOI 10.3389/fmech.2026.1721474, open access CC-BY)

## What it establishes

A contact-dynamics model of a three-gear (input-idler-output) system: involute tooth
profiles, a 9-DoF dynamical model, and a contact-judgment method (meshing-line ×
profile intersections → penetration → normal/friction forces). The three gears mesh
through the idler, which meshes both others. Key kinematic observation for assembly:

- To assemble the input-idler pair the idler must be rotated by an angle that depends
  on whether it has an **odd or even number of teeth** (the "even-teeth extra rotation"
  in Sec. 2) — the parity dependence of the assembly phase, which the PE620 thread also
  flagged (its cross-type congruence shifts by π in the coaxial limit when p, q have
  opposite parity).
- The idler simultaneously meshes two gears; its acceleration/times are dominated by
  the mesh-in/out of both meshes (four transient events per cycle).

## Implication for PE620

Marginal. The paper is a dynamics/FEM treatment, not a kinematic *counting* source,
and its meshing-phase content is limited to: assembly rotation angles for involute
profiles, and the odd/even-teeth parity effect at the assembly phase. It confirms at
the application level that a gear meshing two others has a tooth-parity-dependent
assembly phase, corroborating the parity term `p·γ_p − q·γ_q` in the thread's
cross-type congruence; it does NOT add a new assembly-counting statement beyond
what Zhao-Li 2018 and the idler double-mesh sources already give. **Not load-bearing
for the count**; recorded so it is not re-read.

```claim
id: idler_three_gear_parity_effect
statement: In a three-gear (input-idler-output) system the idler's initial assembly rotation angle differs depending on whether the idler has an odd or even number of teeth; the parity of the meshing gear enters the assembly phase.
hypotheses: involute spur gears; ideal geometry.
holds-here: yes as a parity remark — PE620's cross-type congruence shows a pi shift for opposite-parity planet sizes; corroborates that parity survives in the off-centre phase model.
status: sourced (You, Luo, Xu 2026, Sec. 2)
bearing: minor; corroborates the parity term in the W-model's cross-type congruence.
anchor: research/sources/idler-three-gear-mesh-phase-frontiers-2026.full.md
```
