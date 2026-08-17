# fake-saddle transition maps — uniform expansion for degenerate DRR graphics

A thread on the degenerate-singularity machinery needed for the open degenerate
DRR graphics (the DI₂a / D-families at infinity), which the nilpotent methods of
RR 2015 do not directly reach.

## What this holds

- **Marín 2026** (EJQTDE 2026 no.5, doi:10.14232/ejqtde.2026.1.5, open access;
  held full text `research/sources/marin-fake-saddles-transition-maps.full.md`
  from the UAB DDD PDF): a *fake saddle* (zero linear part, two separatrices on a
  smooth invariant curve, two hyperbolic sectors — also "impassable grain") is
  characterized by d=4(1−c)−(a−b)²>0 or (c=1,a=b), and its Poincaré transition
  map has a UNIFORM-in-µ asymptotic expansion
  Πω_α(y;µ) = e^{γ±(µ)} y + flat remainder. The uniformity is what lets it
  certify zero cyclicity at a centre — a concrete division-in-flat-class /
  Bautin-trick template. It also corrects Coll–Gasull–Prohens 2025.
- This is the same normal-form family as De Maesschalck–Rebollo-Perdomo–
  Torregrosa 2015 (JDE 258:588–620), which proved cyclicity ≤ 2 for a fake
  saddle inside quadratic fields (reference [3], cited but not held).

## Why it matters

The DRR program's open rows are the nilpotent AND degenerate families. The
henceforth-held uniform transition-map expansion is exactly the machinery a
finite-cyclicity proof of the open degenerate graphics (DI₂a and the ≥11 open
degenerate rows) would rest on — the degenerate analogue of what RR 2015 build
for the nilpotent center graphics. The Darboux/bridge algebraic core of Lu's
H₁₄³ paper (which this thread's sibling verification targets) is a degenerate-
adjacent center-graphics computation.

## Status / next

```thread
id: fake-saddle-uniform-transition-map
question: Does the uniform fake-saddle transition-map expansion of Marín 2026,
  combined with a division-in-flat-class step, certify finite cyclicity of an
  open degenerate DRR graphic (e.g. DI₂a)?
status: open
rests-on: marín-2026 (held); DMRT 2015 fake-saddle cyclicity ≤2 (not held, cited)
next: obtain DMRT 2015 (JDE 258:588-620) or its open preprint; identify which
  DRR degenerate graphic has fake saddles and whether the uniform expansion
  closes it; re-derive the division-in-flat-class step in Lean.
blocked-by: DMRT 2015 full text not held; no execution tool in this pass to
  certify the worked-example calculation.
```

## Durable record (memory server down)

The load-bearing claim is filed as `fake-saddle-uniform-transition-map-marin2026`
in `research/summaries/marin-fake-saddles-transition-maps.md` and reaches
derived/CLAIMS.md. Store to Cognee when the memory server recovers.