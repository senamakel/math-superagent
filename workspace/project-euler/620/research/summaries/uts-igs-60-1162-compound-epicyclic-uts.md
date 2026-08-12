# UTS IGS 60-1162 — Compound Epicyclic Gear Design (Parallel Axis)

[[research/sources/uts-igs-60-1162-compound-epicyclic-uts.full.md]] · source:
https://www.uts.com/resources/IGS/IGS60-1162.pdf

UTS Integrated Gear Software Program 60-1162, "Compound Epicyclic Gear
Design (Parallel Axis)" — companion to 1165 (simple epicyclic). A compound
unit has a sun gear meshing external **sun-planet** gears, each of which is a
two-gear cluster: the second gear of the cluster is the **ring-planet**, meshed
internally with the ring gear. Three configurations: Planetary (ring fixed),
Star (carrier fixed), Solar (sun fixed).

## What it establishes

**Equal spacing (identical compound planets).** For np identical planets
equally spaced:

    [(Nring·Npl-sun) + (Nsun·Npl-ring)] / np = integer

where Npl-sun = teeth of the sun-facing gear of the planet cluster and
Npl-ring = teeth of the ring-facing gear of the cluster.

**Unequal spacing.** Like 1165: planets must sit at multiples of the least
mesh angle

    ep / β = integer,   β = 360° / [Nring·Npl-sun + Nsun·Npl-ring]

## Why it matters for PE620

This is the **generalisation of the assembly condition beyond identical
single-gear planets** — exactly the p≠q situation of PE620 (four planets, two
of p, two of q). The 1165 simple-stage formula β = 360°/(Nring+Nsun) treats
all planets as identical; the 1162 formula shows how the count generalises
when planet meshes differ. Note the structural parallel: in both, the
denominator is a sum of (ring teeth × planet-sun teeth) + (sun teeth × planet-
ring teeth), and equal spacing requires that sum to be divisible by np.

The thread `research/threads/offcentre-mesh-phase-model.md` derives the PE620
case from first principles (each planet tangency-forced to two positions;
count over centre distance d; per-planet invariant W_j). This UTS pair (1162 +
1165) is the coaxial design-rule tier that the off-centre model must reduce to
in the d→0 limit (see claim `coaxial_limit_reproduces_lattice`).

```claim
id: compound_assembly_condition_uts_1162
statement: For a compound epicyclic train with identical planets (each planet a two-gear cluster: Npl-sun teeth on the sun-facing gear, Npl-ring teeth on the ring-facing gear), np planets assemble equally spaced iff [(Nring*Npl-sun)+(Nsun*Npl-ring)]/np is an integer; unequally spaced assembly requires planet angles to be integer multiples of the least mesh angle beta = 360/[(Nring*Npl-sun)+(Nsun*Npl-ring)]. Generalises the simple-stage formula (Nring+Nsun)/np of UTS 1165 to non-identical planet meshes.
hypotheses: coaxial carrier about the shared sun-ring axis; identical compound planets; ideal teeth.
holds-here: NO — PE620 has off-centre sun and planets of two different sizes p,q; the coaxial lattice is only the d->0 limit (thread coaxial_limit_reproduces_lattice).
status: sourced (design manual; no derivation given)
bearing: shows how the assembly-condition denominator generalises when planet meshes are not identical — the coaxial counterpart the off-centre model must reduce to.
anchor: research/summaries/uts-igs-60-1162-compound-epicyclic-uts.md
```

## Cross-references

- 1165 (simple stage): (Nring+Nsun)/np — least mesh angle 2π/(Nring+Nsun).
- Drivetrain Hub: equivalent equal-spacing condition k = (z1−z3)/N with internal
  ring teeth taken **negative**, θ̂ = 2π/(z1−z3).
- Guo 2011 eq. (5.21): (Z_r + Z_s)·ψ̂_il = 2π n — the derived form.
- thread offcentre-mesh-phase-model: the off-centre generalisation.