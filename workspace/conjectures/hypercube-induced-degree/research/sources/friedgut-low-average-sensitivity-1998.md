# Ehud Friedgut, "Boolean Functions With Low Average Sensitivity Depend On Few Coordinates" (Combinatorica, 1998)

Source URL: https://doi.org/10.1007/pl00009809
Retrieved via `read_sources` (server-side); direct download blocked by the
network boundary (Springer host unreachable from the run).

Paper: Ehud Friedgut, *Boolean Functions With Low Average Sensitivity Depend On
Few Coordinates*, Combinatorica 18 (1998), no. 1, 27–35.

## What this source establishes

If a Boolean function f: {−1,1}^n → {−1,1} has small **average sensitivity**
(= total influence Σ_i I_i(f) = total edge boundary of the set it cuts, up to
normalisation), then f depends essentially on only a few coordinates: most of
its influence is concentrated on a small set of input bits. Equivalently, a
function whose total influence is small (relative to its size) is close to a
function depending on few coordinates.

Technique: Fourier-analytic methods on the Boolean cube, combined with an
influence/concentration argument — low average sensitivity forces most of the
Fourier mass to lie on low-degree / few coordinates.

## Why it is here

This is a canonical structural result on the influence side, and a distinct
technique from the others in the library (it turns small *average* sensitivity
into a *structural* statement about few coordinates). It is one of the sources
that extends the classical edge-isoperimetric/influence theory. It is cited by
the edge-isoperimetric stability literature (Keevash–Long reference Friedgut in
the influence/variance framework).

Relevance: it bounds low *total* influence (an average/outer quantity — total
edge boundary). At |S| = 2^{n-1}+1 the relevant total edge boundary can be
small, and Friedgut's theorem would then force S to be close to a
few-coordinate (subcube-like) object — but the quantity so forced is about
*total* dependence, not the *maximum* internal degree D(S) of the +1-vertex
excess. It confirms the obstruction: structural theorems for low average
sensitivity control averages, not max degree.

## Claim block

```claim
id: friedgut-low-average-sensitivity
statement: If a Boolean function f: {−1,1}^n → {−1,1} has small average
  sensitivity (total influence), then f is close to a function depending on few
  coordinates: most of its influence concentrates on a small set of inputs.
hypotheses: f Boolean, small Σ_i I_i(f) (total influence / edge boundary).
holds-here: yes as a structural statement about low-total-influence sets; but
  the quantity controlled is total influence, not max internal degree D(S).
status: asserted-by-source (Friedgut 1998, read via read_sources; primary).
bearing: structural companion to the influence route; confirms total-influence
  (average) tools yield structure on averages, not on the max degree of the
  +1-vertex excess.
falsifies: a function with small total influence whose dependence is spread
  over many coordinates beyond the stated bound.
anchor: https://doi.org/10.1007/pl00009809
```
