# Transversal-convexity of es_construct — adjudicated claim

Adjudication mandated by directive 13. This note decides, and records into the
claim, whether the finding below is a structural consequence of the construction
or a genuine discovery, and states where the line's value actually lies.

## The finding (exact arithmetic, verified)

In the verified `es_construct` ES construction X_n (2^{n-2} points, blocks
T_0..T_{n-2} with |T_i| = C(n-2,i), no convex n-gon), **every full transversal**
— choosing exactly one point from each block — lies in **convex position**.
Consequently the number of convex (n-1)-subsets that are full transversals equals
the total number of full transversals, prod_i C(n-2,i) = OEIS A001142(n-2).

| n | full transversals | all convex? | source |
|---|---|---|---|
| 4 | 2 | yes | seq_extract.py |
| 5 | 9 | yes | seq_extract.py |
| 6 | 96 | yes | seq_extract.py |
| 7 | 2500 | yes | seq_extract.py |
| 8 | 162000 | yes | transversal_convex_n8.py |
| 9 | 26471025 | yes | transversal_convex_n9.py, EXIT 0, zero non-convex |

All exact Fraction/integer-scaled arithmetic against `lib/es_geom.in_convex_position`.
n=9 capture: `code/out/transversal_convex_n9.captured.txt`.

## The adjudication: (a) or (b)?

**Decision: (a) — a structural consequence of the construction, status
"structural consequence, verified", NOT a discovery.** Here is the step of the
construction that implies it:

- The blocks T_i are **cup-free and cap-free by design**: block T_i is free of an
  (i+2)-cap and an (n−i)-cup (`es-construct-block-tightness`: longest_cup(T_i) =
  n−i−1, longest_cap(T_i) = i+1, so cup+cap = n). The radial placement on a
  strictly (downward-)convex arc, with each block a minuscule cluster around a
  center and centers spread ~1000 apart, means a full transversal — one point per
  block — samples each block once and follows the strictly convex arc in block
  order. Conjecture A (`layer-profile-outer-hull-one-per-block`, confirmed PASS at
  n=5,6,7) pins that the outer hull is exactly one point per block in block order,
  and the same "strictly convex arc, one point per cluster" geometry that makes
  the hull one-point-per-block also makes *any* one-point-per-block choice sit on
  the convex chain. The design forces convexity of every transversal; there is no
  step of the construction that does not already imply it, and specifically the
  cup/cap-free block design plus radial arc placement is exactly the positive-
  fraction "transversal-convex" mechanism instantiated with the blocks as the
  subsets Y_i.

So the honest status is **structural consequence, verified** — an instance of the
`barany-valtr-positive-fraction` phenomenon on this one set, not a discovery about
extremal sets in general, and not a theorem (the general lemma "tiny clusters on a
strictly convex arc ⇒ every transversal convex" is not proved here, only verified
on this placement through n=9).

## Mechanical confirmation of (a) — two exact experiments (this run)

The verdict (a) is not merely plausibility; it is forced by observable scale
separation in the construction and confirmed by a placement-breaking control.

**Experiment 1 — margin analysis** (`code/out/transversal_adjudicate_margin.py`).
Placing n-1 blocks on the arc (centers spread x-spacing 1000 apart with strictly
decreasing successive slopes, drop = 0.1), the arc's convexity corridor
(slope-drop × spacing = 100 in y-units) exceeds the largest cluster diameter
(measured ~2.3e-5 at n=7, ~9.7e-5 at n=9) by more than **eight orders of
magnitude**. A one-point-per-block transversal is therefore a tiny (~1e-4)
perturbation of a strictly convex n-1-gon in block order (Conjecture A), and
convexity is preserved by the margin. The property is a scale artifact of the
arc placement, not an intrinsic property of the block decomposition.

**Experiment 2 — placement-breaking control** (`code/out/transversal_breaking.py`).
Keep the EXACT SAME blocks (identical coordinates), but replace the convex-arc
centers by scrambled / random y's at n=6 (16 pts, blocks [1,4,6,4,1], 96 full
transversals, exact arithmetic):

| centers | all 96 transversals convex? | convex 6-gon present? |
|---|---|---|
| convex arc (original) | yes (0 non-convex) | no (n-avoiding) |
| scrambled y on the arc x's | **no (96/96 non-convex)** | **yes** |
| random y | **no (96/96 non-convex)** | **yes** |

Identical blocks off the convex arc destroy BOTH transversal-convexity and
n-avoidance at once. So transversal-convexity is a property of the *arc
placement* (the design), not of the block decomposition alone — confirming (a)
and showing the property does not hold for an arbitrary placement of the same
blocks. The converse question (does transversal-convexity of a block
decomposition *force* n-avoidance) remains open and is not settled by this
control: in these ruptured placements the two properties fail together, which is
consistent with, but does not prove, characterization.

## What this line is worth, and the real next question

This is a property **of the known template**, not a statement about extremal sets
in general. Its only value is whether transversal-convexity across a block
decomposition **characterizes** n-avoiding sets or merely **describes this one**:
does every 2^{n-2}-point set with no convex n-gon that admits such a block
decomposition have all full transversals convex — or is that a specific feature of
es_construct's construction and, conversely, does transversal-convexity force the
n-gon-avoidance? If it describes only es_construct, record it as a scoped template
property and stop: it is exactly the kind of finding the run must not present as a
generality. (Kept in task `adjudicate-transversal-convexity`.)

## claim block
```claim
id: es-construct-transversal-convexity
statement: In the verified es_construct ES construction X_n (n≤9), every full transversal — exactly one point from each block T_0..T_{n-2} — lies in convex position; the number of such convex (n-1)-subsets equals prod_i C(n-2,i) = A001142(n-2). ADJUDICATED (directive 13): this is (a) a STRUCTURAL CONSEQUENCE of the construction's design — the blocks are cup-free/cap-free by design and Conjecture A places the hull one-point-per-block in order, which together force any one-point-per-block transversal onto the strictly-convex arc — status "structural consequence, verified", NOT a discovery, NOT a theorem (the general lemma is unproved, only verified on this placement through n=9), and NOT a statement about extremal sets in general. It is an instance, on this specific set, of the positive-fraction ES phenomenon barany-valtr-positive-fraction.
hypotheses: verified es_construct placement (exact Fraction/integer coordinates); n ≤ 9; full-transversal = one point per block; exact convex-position test via lib/es_geom.
holds-here: yes — the construction is exactly the set this run has verified, but as a structural-consequence-of-template, NOT as a general claim about n-avoiding sets.
status: checked (verified numerically n=4..9, exact arithmetic) — with the adjudication that this is a structural consequence of the template, not a discovery.
bearing: the characterization question — does transversal-convexity across a block decomposition characterise n-avoiding sets, or merely describe es_construct — is the only open part with value (task adjudicate-transversal-convexity); the raw finding alone carries none as a generality.
anchor: code/out/transversal_convex_n9.captured.txt (EXIT 0, zero non-convex); code/out/transversal_convex_claim.md
```
