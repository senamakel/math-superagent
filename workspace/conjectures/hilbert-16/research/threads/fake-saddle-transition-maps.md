# fake-saddle transition maps — uniform expansion for degenerate DRR graphics

A thread on the degenerate-singularity machinery needed for the open degenerate
DRR graphics (the DI₂a / D-families at infinity), which the nilpotent methods of
RR 2015 do not directly reach.

## What this holds

- **Marín 2026** (EJQTDE 2026 no.5, doi:10.14232/ejqtde.2026.1.5, open access;
  held full text `research/sources/marin-fake-saddles-transition-maps.full.md`):
  a *fake saddle* (zero linear part, two separatrices on a smooth invariant
  curve, two hyperbolic sectors — also "impassable grain") is characterized by
  d=4(1−c)−(a−b)²>0 or (c=1,a=b), and its Poincaré transition map has a
  UNIFORM-in-µ asymptotic expansion Πω_α(y;µ) = e^{γ±(µ)} y + flat remainder.
  The uniformity is what lets it certify zero cyclicity at a centre — a concrete
  division-in-flat-class / Bautin-trick template. It also corrects
  Coll–Gasull–Prohens 2025.
- **DMRT 2015** (JDE 258(2):588–620, held postprint): proves the cyclicity of
  the quadratic fake saddle is **≥ 2** (configurations (2:0), (1:1)); the
  paper explicitly states an upper bound "turned out to be too difficult".
  The only at-most-two result is for the symmetric-restricted family in
  configuration (1:1). So "fake-saddle cyclicity ≤ 2" is a misstatement of a
  lower bound as an upper bound — corrected this cycle (claim
  `drrt-2015-fake-saddle-cyclicity-lower-bound`).

## Why it matters

The DRR program's open rows are the nilpotent AND degenerate families. The
uniform transition-map expansion is exactly the machinery a finite-cyclicity
proof of the open degenerate graphics (DI₂a and the ≥11 open degenerate rows)
would rest on — the degenerate analogue of what RR 2015 build for the nilpotent
center graphics. The Darboux/bridge algebraic core of Lu's H₁₄³ paper (which
this thread's sibling verification targets) is a degenerate-adjacent
center-graphics computation.

## Status / next

```thread
id: fake-saddle-uniform-transition-map
question: Does the uniform fake-saddle transition-map expansion of Marín 2026,
  combined with a division-in-flat-class step, certify finite cyclicity of an
  open degenerate DRR graphic (e.g. DI₂a)?
status: closed — DRR-closure direction refuted by the primary source
rests-on: drrt-2015-fake-saddle-cyclicity-lower-bound,
  drrt-2015-fake-saddle-no-drr-contribution,
  fake-saddle-uniform-transition-map-marin2026
blocked-by: DMRT 2015 (held, verified) states the fake saddle has NO contribution
  to the DRR degree-2 programme — homogeneous fields avoided by rescalings
  (lines 72–75). No DRR 121-graphic row is closed by fake-saddle cyclicity.
next: the uniform expansion survives only as a division-in-flat-class template
  for the slow-divergence/ECT route; identify a concrete degenerate graphic
  whose finite cyclicity the expansion actually closes, or drop the thread.
```

## Durable record

- DMRT 2015 full postprint held:
  `research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md`
  (source URL https://ddd.uab.cat/pub/artpub/2015/gsduab_3787/joudifequ_a2015v258n2p588preprint.pdf).
- Claims: `drrt-2015-fake-saddle-cyclicity-lower-bound`,
  `drrt-2015-fake-saddle-no-drr-contribution` in
  `research/claims/drrt-2015-fake-saddle-cyclicity.md`.
- Cognee: stored 2026-08-18 (research note 5533942024073640677).
- Corrected: the earlier thread phrasing "proved cyclicity ≤ 2 for a fake
  saddle inside quadratic fields" overstated — the primary text proves ≥ 2.
