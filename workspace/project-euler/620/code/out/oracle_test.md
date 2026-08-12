# Oracle test of the gears.py meshing model — FAILED on all three values

`code/oracle_test.py` ran `lib/gears.py` against the PE620 oracle values.
Full output: `code/out/oracle_test.txt`.

```claim
id: gears_model_fails_oracle
statement: The continuous-d phase-elimination meshing model in lib/gears.py
  (planet centre forced to circle(O,R-rho) ∩ circle(S,r+rho), arrangement
  parameterised by centre distance d, valid iff 2Fp, 2Fq, H are integers mod 1)
  disagrees with the PE620 oracle on all three published values:
  g_count(16,5,5,6)=0 vs 9; G_sum(16)=0 vs 9; per-pair sum over G(20)=0 vs 205
  (G(20) pass at grid_points=50000, G(16) and g(16,5,5,6) at the default
  400000 grid).
hypotheses: g_count faithfully implements the model described in gears.py's
  docstring; the residual 2Fp,2Fq,H in Z is the exact phase-solvability
  condition of the 8 tooth-alignment congruences.
holds-here: true (the implementation is the model under test, and the oracle
  values are the statement's published values)
status: checked
bearing: the continuous-d model is NOT the intended discretization; the
  least-mesh-angle lattice model (research claims least_mesh_angle*) is the
  promising replacement route.  This failure kills the current gears.py route
  and stops any further work trying to make it reproduce the examples.
anchor: code/out/oracle_test.txt
```

## Why the model returns 0 (diagnosis, same-module probe)

Sampling `consistency(16,5,5,6,d)` over the valid interval
d in [1/(2*pi) ≈ 0.159155, 0.750704] cm shows the residual
|sin(4*pi*Fp)|+|sin(4*pi*Fq)|+|sin(2*pi*H)| is O(1) throughout, except at the
**lower endpoint** d = 1/(2*pi) where the two p-planets coincide (degenerate
tangent position, 2Fp%1 = 2Fq%1 = H%1 = 0 to 4e-24).  `g_count` deliberately
excludes endpoint-degenerate d, so it finds zero valid *interior* arrangements
for every one of the 22 (c,s,p,q) pairs in G(20): the phase-elimination
conditions have no interior roots at small integer tooth counts.

This is not a resolution artifact: the primary case runs at the full default
grid, and the residual is smoothly O(1) between degenerate endpoints, so no
narrow zero could be missed.

## What failed vs. what remains plausible

- **Failed (checked):** the "arrangement = continuous centre distance d, mesh iff
  phase congruences solvable" model.  Zero solutions at 400000-grid resolution
  for (16,5,5,6) where the problem says 9.
- **Still plausible (unchecked):** the least-mesh-angle model in the research
  claims: planets sit only at angular multiples of beta = 2*pi/(s+c) about S's
  centre, and the planet-centre locus is the two-focus ellipse.  That model
  naturally yields small integer counts (9, 205) and is the intended structural
  route; it has NOT yet been implemented or tested.

## Timing (for budgeting the next attempt)

- g_count(16,5,5,6) at grid 400000: 29–32 s.
- G_sum(16) (1 pair, grid 400000): 28.8 s.
- G(20) 22 pairs at grid 50000: 78.1 s total (3.4–4.8 s per pair); the
  default-grid G_sum(20) would take ~11 min, over the 600 s tool cap (why the
  per-pair pass used the coarser grid).