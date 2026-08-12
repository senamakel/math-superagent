# UTS IGS 60-1165 — Coupled and Series Epicyclic Gears

[[research/sources/uts-igs-60-1165-epicyclic-units-uts.full.md]] · source:
https://www.uts.com/resources/IGS/IGS60-1165.pdf

UTS Integrated Gear Software Program 60-1165, "Coupled and Series Epicyclic
Gears" — a design-manual style source that states the **assembly condition and
least-mesh-angle rule for a simple epicyclic train** with a fully worked
numerical example. This is the derivation-level treatment the library was
missing for the coaxial case (the 1161 summary had the rule; this adds the
explicit mechanism and example).

## What it establishes

Definitions: a simple epicyclic unit = central external sun gear, one or more
external planet gears, enclosing internal ring gear; the planet carrier rotates
about the unit's geometric centre.

**Equal spacing (identical planets).** For np planets to assemble equally
spaced around the centre:

    (Nring + Nsun) / np = integer

where Nring = ring gear teeth, Nsun = sun gear teeth, np = number of planets.

**Unequal spacing.** Planets need not be equally spaced, but to make assembly
possible they must be placed at multiples of the *least mesh angle*:

    ep / β = integer,   β = 360° / (Nring + Nsun)

where ep is the angle between adjacent planet gears. (β = 2π/(c+s) in PE620
notation: c = ring teeth, s = sun teeth.)

**Worked example (verbatim values, directly testable).** Nring = 68, Nsun = 18:
- (68+18)/4 = 21.5 not integer ⇒ 4 planets at 90° apart **cannot** assemble;
- (68+18)/2 = 43 integer ⇒ 2 planets at 180° apart **can** assemble;
- β = 360°/86 = 4.186°; placing a planet 90° from the first = 21.5 β ⇒
  impossible; the nearest legal positions are 21 β = 87.907° and 22 β = 92.093°;
  the 4 planets then sit at 0°, 87.907°, 180°, 267.907° (two opposed pairs,
  radial loads on sun and ring still sum to zero).

Also stated: planet-centre spacing must exceed the planet outside diameter
(tooth-tip interference); "It is not necessary (or even desirable) that
Nring = Nsun + 2·Nplanet" (standard centre distance only makes the operating
pressure angles equal to nominal); operating pressure angle at the sun/planet
external mesh vs the planet/ring internal mesh can be tuned independently.
Sister documents 60-1162/60-1164 give the compound-epicyclic generalisation
β = 360° / [Nring·N'pl-sun + Nsun·N'pl-ring].

```claim
id: least_mesh_angle_uts_1165
statement: For a simple epicyclic gear set (sun Nsun, internal ring Nring, np planets on a carrier about the common centre), np identical planets assemble equally spaced iff (Nring+Nsun)/np is an integer; planets need not be equally spaced but assembly forces every planet onto the lattice of integer multiples of the least mesh angle beta = 360/(Nring+Nsun). Worked example: Nring=68, Nsun=18, beta=4.186 deg, 4 planets at 90 deg impossible (21.5 beta), legal placements 21 beta = 87.907 deg etc.
hypotheses: coaxial carrier about the shared sun-ring axis; one planet per train (compound case needs the 1162/1164 generalisation); ideal teeth.
holds-here: UNVERIFIED — PE620 has the sun OFF-CENTRE (no common centre; no carrier even); the lattice is only the coaxial limit; the off-centre generalisation is the thread offcentre-mesh-phase-model.
status: sourced (design manual, no derivation given, but with a fully worked numerical example)
bearing: fixes the standard coaxial assembly condition as the d->0 limit that any correct off-centre model must reproduce; gives testable numbers (68+18=86, beta=4.186 deg).
anchor: research/summaries/uts-igs-60-1165-epicyclic-units-uts.md
```

## Implication for PE620

The source is the coaxial cousin of the run's problem: c ↔ Nring, s ↔ Nsun.
The equality (c+s)/np ∈ ℤ for equal spacing and the lattice
{2πk/(c+s)} for unequal spacing are the design-guide statements the earlier
summaries (drivetrainhub tick angle, UTS 1161, Gear Solutions handbook,
least_mesh_angle*) already carried; 1165 adds the worked 68/18 example and the
explicit "multiples of β" mechanism. What it does NOT give — no source in the
library does — is the off-centre generalisation, which the thread
offcentre-mesh-phase-model derives from first principles (positions forced by
tangency to two non-concentric circles; count over the centre distance d).