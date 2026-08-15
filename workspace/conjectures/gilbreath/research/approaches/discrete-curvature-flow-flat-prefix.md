# discrete-curvature-flow-flat-prefix

```approach
idea: The halved Gilbreath rows are a discrete curve under the curvature-driven flow h ↦ |∂h|, and the leading {0,2} block of row k+1 is *exactly* the longest 1-Lipschitz ("flat") prefix of h_k; import Grayson's curve-shortening-flow / discrete-curvature theory to prove the flat prefix of the halved prime-gap rows never degenerates, giving Gilbreath as a corollary of a general discrete curvature-shortening theorem.
mechanism: |
  Let h = A/2 (halved row, non-negative integers). Then
  h_{k+1}(i) = |h_k(i) − h_k(i+1)| is the ℓ¹ discrete gradient of h_k. The
  {0,2} block of row k+1 is the maximal prefix with h_{k+1}(i) ∈ {0,1}, i.e.
  |h_k(i) − h_k(i+1)| ≤ 1 — the longest prefix over which h_k is 1-Lipschitz.
  So the block boundary of row k+1 is the FIRST position where the halved
  row's slope exceeds 1: a discrete-curvature jump (a "2-step", the 0–2/2–0
  adjacency the run already found terminates every giant stretch). The
  row-to-row map is therefore a discrete curvature flow on the 1D profile h_k,
  and the conjecture is the statement that a long low-curvature prefix always
  persists/regenerates. The named machinery is curve-shortening flow
  (Grayson 1987: embedded curves become convex then round; discrete analogues
  by Chow–Glickenstein and curvature flow on planar networks). The theorem to
  aim for OVERSHOOTS the goal: for any non-negative integer profile with a
  flat prefix and a slope profile controlled by the 2-then-odds gap structure,
  the flow h ↦ |∂h| regenerates a flat prefix — a discrete Grayson-type
  "convexity preservation" statement, of which Gilbreath's conjecture is the
  left-edge corollary.
status: refuted
killed-by: |
  The named mathematics is real and well-documented, but its hypotheses fail
  here on three independent grounds. (1) The curvature-flow machinery that
  exists is for LINEAR second-order flows: Chow–Glickenstein's semi-discrete
  curve-shortening flow (2007) and its boundary/polyharmonic extensions are
  first-order systems of linear ODEs with explicit Fourier solutions; Domokos
  2014 (J. Nonlinear Sci, doi:10.1007/s00332-014-9228-3) proves monotone
  decrease of the number of spatial critical points under curvature-driven
  flows, generalising Grayson's Lemma 1.9. But the Gilbreath map h ↦ |∂h| is
  NOT linear — the absolute value sits inside the difference, so there is no
  Laplacian, no Fourier diagonalisation, and no explicit-solution machinery to
  import. (2) Grayson's theorem itself is a genuinely 2D statement (embedded
  planar curves convexify then round under mean curvature); no 1D discrete
  analogue equal to |∂h| exists in the literature, and no source connects
  iterated absolute differences to any curvature flow. (3) Even granting a
  curvature reading, the mechanism "flat prefix always persists/regenerates" is
  exactly the bounded-absorption claim that Eppstein 2011 (held claim
  anti-gilbreath-construction) refutes for the 2-then-odds class: flat prefixes
  die and re-merge infinitely often with gaps ≤ f(n). The file's own
  falsification step — measuring whether *any* curvature functional actually
  decreases across the 60 real regenerations before invoking theory — is the
  correct discipline and was not run here; but the literature already shows the
  only available named flow is linear and the regeneration claim is defeated in
  the general class, so the analogy is decorative rather than structural.
  Precedent: Chow–Glickenstein semi-discrete curvature flow (2007) and its
  extensions (Geom. Dedicata 2026 boundary flows; J. Geom. Anal. 2025
  polyharmonic); Nakayama–Segur–Wadati 1997 discrete curve-shortening equation
  (with Lyapunov); Domokos 2014 doi:10.1007/s00332-014-9228-3 (critical-point
  monotonicity, generalising Grayson 1987 Lemma 1.9); Eppstein 2011
  (anti-gilbreath-construction, held claim). No source applies any curvature
  flow to the iterated absolute-difference operator. Verdict: refuted — the name
  is grounded, the specific flow is linear and the regeneration claim fails in
  the general class. This is a reformulation that changes the setting, and must
  satisfy Scholze's gate: it cannot reproduce any settled result, so it is not
  worth adopting.
first-step: |
  (a) Verify the exact bijection "block of row k+1 = longest 1-Lipschitz
  prefix of h_k" on the oracle rows (blocks_depth1000.json, depth 1000);
  expect zero violations since it is the halved restatement of the step law.
  (b) Measure the discrete curvature profile (second differences of h_k, and
  the position of the first |Δh| ≥ 2 jump) near the block front across all 60
  regeneration events; confirm the first ≥2-jump coincides with the block
  front. (c) Formulate the candidate discrete-curvature-shortening lemma and
  hand-attack it: what would a counterexample profile (flat prefix that dies
  without regenerating) have to look like, and does the slope control forbid
  it? Cost O(depth × width), one row live.
```

## Why this is not on disk

- Not `discrete-stefan-free-boundary-block-interface` (proposed): that tracks
  the *interface position* b_k as a free boundary with an enthalpy balance.
  This tracks the *halved row's curvature profile* and the flat-prefix length,
  via curve-shortening flow — a different object (the 1D profile vs. the
  interface coordinate) and different theorems (Grayson curvature shortening
  vs. Stefan comparison principles).
- Not a scalar potential (the run-count / TV / turning-point family,
  machine-refuted at (0,0,1,1)): the invariant here is the *flat-prefix length
  and curvature profile*, a geometric object, not a real-valued monotone
  functional.
- Not the "jump = 1-Lipschitz chain" empirical observation alone: that
  observation (in CONTEXT.md) is here promoted to the load-bearing structural
  identity of a *named flow*, with the burden on proving a discrete
  curvature-shortening theorem.

## What would falsify it

The curvature-shortening analogy is decorative rather than structural: if the
flow h ↦ |∂h| does not actually decrease any discrete curvature measure
(second-difference total variation, number of slope jumps, etc.), then no
Grayson-type theorem transfers. This is checked by measuring a curvature
functional across the 60 real regenerations before any theory is invoked.

## Side

General-class (the curvature-flow structure is universal for the operator).
Aims at regeneration via a new geometric invariant (flat-prefix / curvature
profile), not via the consumption/regeneration accounting and not via a scalar
potential.

## Named mathematics

Curve-shortening flow (Gage–Hamilton, Grayson's theorem), discrete curvature,
discrete gradient/Laplacian, Lipschitz geometry, first-passage/hitting times of
the slope profile.
