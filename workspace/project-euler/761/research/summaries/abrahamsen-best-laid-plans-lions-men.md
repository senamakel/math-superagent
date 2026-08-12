# Abrahamsen–Holm–Rotenberg–Wulff-Nilsen, "Best Laid Plans of Lions and Men" (SoCG 2017)

Source: LIPIcs-SoCG-2017, article 6, DOI 10.4230/LIPIcs.SoCG.2017.6 (also arXiv:1703.03687).
Full text: `research/sources/abrahamsen-best-laid-plans-lions-men.full.md` → [[abrahamsen-best-laid-plans-lions-men.full]]

## What the paper establishes

A peer-reviewed (SoCG 2017, LIPIcs) contribution to the *lion and man* pursuit
family — the equal-speed, multiple-lion capture game, not the
runner-swimmer *critical speed* game PE 761 models.

- **Definitions (following Bollobás et al.).** Man/lion paths are Lipschitz
  functions into the region R with the given speed bound. A *strategy* for the
  man is causal (depends only on the lion's position up to the current time); a
  winning man strategy must avoid equality with every lion at all t; a winning
  lion strategy must force equality at some t. A *locally finite* man strategy
  commits for a positive time depending only on the current state. Key
  fact (Bollobás et al.): if the man has a locally finite winning strategy the
  lion has no winning strategy — so the two-can-both-win pathologies of
  Bollobás–Leader–Walters are excluded for these strategies.
- **Theorem 6 (main two-lion result).** There exists a *polygonal region in the
  plane with holes* (11 lakes; exterior and all interior boundaries pairwise
  disjoint simple polygons, hence rectifiable) in which **two unit-speed lions
  cannot catch a unit-speed man**: the man has a locally finite winning strategy
  (runs quarter-to-quarter on a thickened dodecahedron, keeping a constant
  safety distance to each lion).
- **Theorem 8 (fast man).** In the whole plane, a man of speed 1+ε (any ε>0)
  has a locally finite strategy to escape the convex hull of *any* finite
  number of unit-speed lions, provided he does not start on a lion, keeping a
  minimum safety distance.

## Why it matters for this run

It is the modern computational-geometry resolution of the *unbounded /
many-lion / catches-or-not* side of the lion-man canon, and it supplies the
formal locally-finite/winning-strategy definitions that several of this run's
other sources (ABG, Bollobás–Leader–Walters) cite. But it does **not** bear on
PE 761's question:

- PE 761, and the Abel et al. model the run relies on, are about a *single*
  runner on the *boundary* whose *speed ratio* vs a speed-1 swimmer is the
  unknown threshold. Abrahamsen et al. study *catch-or-survive-forever* (not a
  critical speed ratio) with *equal speeds* and a man in the *interior* being
  approached by lions — a different game with a different quantity.
- The man in their Theorem 8 is strictly *faster* (1+ε); PE 761's swimmer is
  speed 1 against a faster runner. Opposite regime.

```claim
id: abrahamsen-two-lions-region-man-survives
statement: There is a polygonal region with holes, all boundaries pairwise-disjoint simple polygons (hence rectifiable), in which two unit-speed lions cannot catch a unit-speed man — the man has a locally finite winning strategy; and in the whole plane a man of speed 1+eps for any eps>0 can escape the convex hull of any finite number of unit-speed lions, given he does not start on a lion.
hypotheses: lion-and-man game on a rectifiable planar region (Thm 6) or the whole plane (Thm 8), equal speeds for the lions, man speed 1 (Thm 6) or 1+eps (Thm 8), causal (locally finite) strategies, unit-speed bound.
holds-here: no — this is the equal-speed (or faster-man) multi-lion capture game, not PE 761's single-boundary-runner critical-speed-ratio game; the pool is convex with no holes, whereas their survival region requires holes.
status: proved (peer-reviewed SoCG 2017, LIPIcs).
bearing: canonical background & formal strategy definitions; confirms the rectifiability/well-posedness framing in which Abel et al. (the run's governing model) sits; no hexagon value and it does not constrain the run's V_hexagon.
anchor: research/sources/abrahamsen-best-laid-plans-lions-men.full.md
```
