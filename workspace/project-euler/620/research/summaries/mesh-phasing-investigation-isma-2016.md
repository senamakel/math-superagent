# Investigation of mesh phasing in a planetary gear train using combined FE and Multibody simulations — Shweiki et al., ISMA 2016

[[research/sources/mesh-phasing-investigation-isma-2016.full.md]] · source:
https://past.isma-isaac.be/downloads/isma2016/papers/isma2016_0785.pdf

## What it establishes

A freely-available, application-level paper that uses the Parker–Lin mesh-phase
formalism as its foundation:

- Cites Parker & Lin (Journal of Mechanical Design, 2004) as the source of the
  analytical mesh-phase relations for planetary stages.
- **Three normalized phase quantities** completely describe the relative positions of
  transmission components in a planetary stage (section 1, citing P&L):
  - γ_sn: phase of the nth sun–planet mesh relative to the first sun–planet mesh,
  - γ_rn: phase of the nth ring–planet mesh relative to the first ring–planet mesh,
  - γ_rs: phase between the ring–planet and sun–planet meshes at a given planet
    (equal for all planets in a configuration).
  - These are normalized with respect to the angular pitch (2π/z of the respective
    gear), so a mesh phase of 1 corresponds to one full tooth pitch.
- Gives a concrete worked value: for their wind-turbine planetary stage, γ_rs =
  0.2805 (angular phase 2.589°), computed from geometry and assembly requirements.
- Applies in-phase vs sequentially-phased configurations to FE/MB co-simulation to
  reduce vibration; confirms that phasing rules can suppress selected harmonics but
  are not valid in chaotic/strongly nonlinear regions.

## Implication for PE620

- Corroborates, at the application level, that mesh phases are computed from tooth
  counts + planet positions and are fractions of the tooth pitch — the same mechanism
  by which the run's quantization step 2π/(c+s) arises.
- Confirms the Parker–Lin formulas are the standard toolkit; does not itself contain
  the assembly-condition derivation (that is Guo Ch.5 / P&L 2004, which stay on disk
  / recorded as paywalled respectively).

```claim
id: mesh_phase_parker_lin_formalism_isma2016
statement: The relative positions of transmission components in a planetary stage
  are completely described by three mesh-phase quantities gamma_sn, gamma_rn,
  gamma_rs (= gamma_rs same for all planets), normalized to the gear's angular tooth
  pitch 2*pi/z; they are computed from tooth counts and planet positions/assembly
  requirements (Parker & Lin 2004 formalism).
hypotheses: standard planetary stage; involute gears; mesh phases are fractions of a
  tooth pitch.
holds-here: true — the same tooth-pitch fractions are what force PE620 planet angles
  onto the 2*pi/(c+s) lattice.
status: sourced (Shweiki et al., ISMA 2016, open access; retells Parker & Lin 2004).
bearing: corroborates the phase formalism at application level; a secondary route to
  the discreteness idea.
anchor: research/sources/mesh-phasing-investigation-isma-2016.full.md
```