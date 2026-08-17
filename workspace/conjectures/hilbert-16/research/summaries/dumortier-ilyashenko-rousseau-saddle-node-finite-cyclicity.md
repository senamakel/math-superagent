# Dumortier–Ilyashenko–Rousseau 2002, "Normal forms near a saddle-node and applications to finite cyclicity of graphics" (ETDS 22:783–818)

Source: `research/sources/dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full.md` [[dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full]] — from `http://www.dms.umontreal.ca/~rousseac/DIR.pdf`.

## What the source establishes

The **saddle-node normal-form machinery** used across the DRR program's
semi-hyperbolic and nilpotent closures.

- **Theorems 1–3** (normal forms): a real analytic germ of a saddle-node with
  one zero and one negative eigenvalue, of even (resp. odd) multiplicity, is C^∞
  **orbitally equivalent to its polynomial normal form**, analytic outside the
  stable manifold; any C^∞ unfolding has a finitely smooth orbital equivalence
  to the polynomial normal form (2.2), analytic at the critical parameter value
  outside the stable manifold. These are the viola: **non-flatness comes from
  analyticity outside the stable manifold** — the exact step that is absent in
  a purely C^∞ setting (Dulac's error).
- **Theorem 3.1** (lips ensembles): given a C^∞ field with an ensemble "lips"
  (two saddle-nodes of opposite attractivity, one hh-connection, a continuum of
  pp-connections), if the regular pp-transition in normalizing coordinates has a
  nonzero derivative of order n ≥ 2 at a point a, then the graphic through a has
  finite cyclicity **≤ n**.
- **Theorem 3.2**: lips-ensemble graphics with a pp-boundary through a
  hyperbolic saddle have absolute finite cyclicity when the hyperbolicity ratio
  r ≠ 1 or there is no analytic first integral; bp-boundary graphics always do.
  In particular the **malignant frown** and **spadesuit** graphics have finite
  cyclicity.
- **Theorem 3.3**: a graphic with four saddle-nodes of even multiplicity,
  alternately attracting and repelling, has finite cyclicity.
- Connects to **Ilyashenko–Yakovenko** (elementary polycycles, generic
  families) and Roussarie's conjecture as the two currents the saddle-node
  machinery reconciles.

## What it implies here

Anchor for claim `drr-saddle-node-normalforms-dir2002`. It is the source of the
**finite-smooth normal-form reduction**: a saddle-node graphic is C^∞
finitely-cyclicity-reducible to its polynomial normal form, which means the
cyclicity bound is decided by finitely many Taylor coefficients — the natural
home for Lean's kernel-checkable statements.

Evidence class: sourced-held — read from the held full text. Hypotheses: planar
analytic vector fields; saddle-node singular points in graphics; ensembles in
the sense of the paper. Falsifier: a saddle-node graphic contradicting the
normal form / cyclicity bounds.

Claim id `drr-saddle-node-normalforms-dir2002` (full statement in
`research/notes/claims.md`).