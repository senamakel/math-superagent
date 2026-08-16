```approach
idea: Gale transform / oriented-matroid duality, via the onion (convex-layer) decomposition
mechanism: Map n planar points to their Gale transform (n vectors in R^{n-3}; oriented-matroid duality), under which faces of conv(X) correspond to cocircuits, and the convex layers (onion decomposition) correspond to a nested flag of totally-cyclic cocircuit arrangements. The anchor is trivial and exact: a set with NO convex n-gon has every convex layer of size ≤ n−1 (the vertices of any layer are themselves in convex position), so N = ∑|layer| ≤ (n−1)·(#layers). The ES construction realizes the sharp profile: exactly n−1 layers with sizes C(n-2,0),…,C(n-2,n-2), summing to 2^{n-2}. The conjecture becomes the sharp layer-profile inequality: for a general-position set with no convex n-gon, ∑|layer| ≤ 2^{n-2}. Because layer nesting is a flag in an oriented matroid, this is a rank-function/flag inequality, attackable with matroid-theoretic extremal results (nested flags, Sperner-type bounds on the lattice of flats/cocircuits) rather than Ramsey counting. Distinct from the cups/caps route: the binomial layer profile is exactly where ms-cups-caps-tight says the pure counting argument loses its factor.
status: refuted
killed-by: The run's own computed onion profiles of the verified es_construct placement refute the decisive premise — the ES construction's convex LAYERS are NOT its binomial BLOCKS T_i. pattern_layers.py (captured in pattern_finder_report.md) gives onion sizes [5,5,3,3] at n=6 and [6,6,6,5,6,3] at n=7, not C(n-2,i) = [1,4,6,4,1] / [1,5,10,10,5,1]. So the "exactly n−1 layers of binomial sizes" anchor is false, and the sharp Σ|layer| ≤ 2^{n-2} formulation loses its witness. The Gale-duality flag view itself is valid but there is nothing left to apply it to.
precedent: >
  The anchor is a true, trivially provable statement and IS supported: every convex layer of a
  planar point set is itself a set in convex position (this is the definition of the onion /
  convex-hull-peeling decomposition, standard: see Morris–Soltan survey,
  doi:10.1090/s0273-0979-00-00877-6, §convex layers; the onion algorithm of Chazelle 1985,
  Overmars–van Leeuwen 1981 and the layer literature in Ambrus–Nielsen–Wilson, Discrete Math.
  344 (2021), doi:10.1016/j.disc.2021.112424), so a no-convex-n-gon set has every layer of
  size ≤ n−1. The layer profile of the ES construction is discussed in the primary source
  (claim `es1961-construction-held`: |S_k| = C(n-2,k-1) blocks, nested with negative-slope
  bands); Duque–Fabila-Monroy–Hidalgo-Toscano (arXiv:1602.03075, held) give integer
  realizations. The Gale transform / oriented-matroid duality is established theory
  (Goodman–Pollack–Sturmfels, "Upper bounds for configurations and polytopes in R^d",
  doi:10.1007/bf02187696; Folkman–Lawrence 1978, claim `realizability-etr-complete` region)
  and the run already holds it as backdrop. CAVEATS: (1) The decisive sharp inequality
  "no convex n-gon ⟹ ∑|layer| ≤ 2^{n-2}" is NOT in the literature in this form — no published
  matroid-flag / rank-function result delivers it, and the onion-layer literature (Ambrus et
  al., peeling sequences literature) is about layer NUMBER bounds for arbitrary/evenly
  distributed sets, not about ES-type exact bounds. (2) The claimed "ES construction has
  exactly n−1 layers of sizes C(n-2,i)" IDENTIFIES the onion layers with the blocks T_i; this
  is NOT established — the blocks are a construction device, and whether they coincide with
  the convex-hull-peeling layers is an open machine-checkable claim (the machine-check is
  exactly the first-step). (3) The number of convex layers of a no-convex-n-gon set is not
  a priori ≤ n−1, so "(n−1)·(#layers)" alone cannot deliver 2^{n-2} without an independent
  layer-count or profile bound — the reduction is substantive, not the trivial anchor.
first-step: State and machine-check the Gale-dual characterization "S is a convex layer of X" (S in convex position, empty, and S = vertices of a face of conv(X)); compute the Gale transform and layer profile of the ES construction at n=5,6,7 and confirm it is the binomial profile (6 layers of sizes 1,5,10,10,5,1 at n=7); then attack the sharp inequality ∑|layer| ≤ 2^{n-2} on small order types with the oracle as referee. NOTE: the layer-vs-block identification is the first thing to falsify/confirm — do not assume the layers equal T_i.
```

## Literature report — Gale transform / convex layers

**What the reformulation is called.** The *onion decomposition* / *convex layers* /
*convex-hull peeling* of a point set, and the *Gale transform* (oriented-matroid
duality). The layer structure is a routine and well-studied object; the Gale-dual flag
view is standard in oriented-matroid theory.

**Precise statements found.**
- *Anchor (trivially proved, holds here):* the vertices of any convex hull layer are
  themselves in convex position (definition of the peeling process: repeatedly take the
  current convex hull and remove its vertices). Therefore a set with no convex n-gon has
  every convex layer of size ≤ n−1. See Morris–Soltan survey (doi:10.1090/s0273-0979-00-00877-6)
  for the layer definition and its uses; Chazelle/Overmars–van Leeuwen for the O(n log n)
  layer algorithm; Ambrus–Nielsen–Wilson (Discrete Math. 344 (2021) 112424,
  doi:10.1016/j.disc.2021.112424) for layer-number bounds of evenly distributed sets.
- *ES-construction blocks:* the canonical construction decomposes 2^{n-2} = Σ C(n-2,k-1)
  into n−1 nested blocks T_1..T_{n-1} with negative-slope bands between them; any convex
  polygon has ≤ n−1 vertices (claim `es1961-construction-held`, primary source held). The
  Duque–Fabila-Monroy–Hidalgo-Toscano paper (arXiv:1602.03075) realizes this with small
  integer coordinates.
- *Gale transform / duality:* faces ↔ cocircuits, layer nesting ↔ nested flag of
  cyclic/totally-cyclic subspaces. Established theory (Goodman–Pollack–Sturmfels 1986,
  doi:10.1007/bf02187696; Folkman–Lawrence 1978).

**Has anyone applied this to THIS problem?** The *layer* and *Gale-dual* machinery has
been applied to empty-convex-gon and k-convex generalized problems (see the k-convex
literature: Valtr 2002 doi:10.1007/s00454-002-2898-x on empty polygons in k-convex sets;
Pach–Solymosi k-convex via Aichholzer et al.), and layer number is studied for its own
sake — but **no published result proves the sharp profile inequality Σ|layer| ≤ 2^{n-2}**
for no-convex-n-gon sets, nor derives the ES bound from a matroid-flag/rank inequality.
The exact conjecture is not settled through onion decomposition in the literature.

**What it would buy.** A structural, non-Ramsey formulation: if the sharp layer-profile
bound held, it would give the exact 2^{n-2} without the cups/caps factor, and the anchor
is genuinely true. But the reduction from the trivial anchor to the sharp inequality is
exactly where the difficulty lives, and the literature supplies neither the layer-count
control nor the profile inequality.

**Verdict: grounded** on the (true) anchor and the established onion/Gale-duality
machinery, **but the decisive sharp inequality is unproved with no precedent**, and the
claim that the ES construction's *layers* are the *blocks* (the binomial profile) is
unverified and must be machine-checked before anything is built on it.
