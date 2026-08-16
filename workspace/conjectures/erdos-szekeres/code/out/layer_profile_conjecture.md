# Layer-profile conjecture — the extremal construction's onion structure

The run's own data (`code/out/pattern_layers.py`, captured in
`code/out/pattern_finder_report.md`) gives the convex-layer (onion) profiles of the
verified `es_construct` placement of the Erdős–Szekeres construction X_n:

| n | |X_n| | onion layers (outer first) | outer layer |
|---|---|---|---|---|
| 4 | 4  | [3,1]        | 3 |
| 5 | 8  | [4,4]        | 4 |
| 6 | 16 | [5,5,3,3]    | 5 |
| 7 | 32 | [6,6,6,5,6,3]| 6 |

Two observations, and one precise conjecture.

**Observation 1 (computed).** The outer layer has exactly n−1 vertices (3,4,5,6 at
n=4..7). This is consistent with the construction placing the n−1 blocks T_0..T_{n-2} on
a downward-convex arc with decreasing polar angle: the hull should pick up the extreme
point of each block.

**Observation 2 (computed, decisive).** The onion profiles are **not** the binomial
profile. The gale-transform/convex-layers approach assumed the onion layers of X_n equal
the binomial blocks T_i (sizes C(n-2,i) — i.e. [1,4,6,4,1] at n=6, [1,5,10,10,5,1] at
n=7). The computed profiles [5,5,3,3] and [6,6,6,5,6,3] refute that identification: the
onion layers are an artifact of the radial arc placement, not the block structure. This
is the `killed-by` line of `research/approaches/gale-transform-convex-layers.md`.

## Precise conjecture (to attack)

**Conjecture A.** In the verified `es_construct` placement of X_n (n in {5,6,7}), the
convex hull consists of exactly one point from each block T_0,...,T_{n-2} — hence exactly
n−1 hull vertices — and the hull vertices appear in block-index order around the hull.

- **Evidence:** outer-layer sizes 4,5,6 at n=5,6,7 equal n−1 = number of blocks; the arc
  placement gives each block a distinct polar-angle sector, so exactly one point per block
  should be extreme.
- **Falsifier:** if `convex_hull(es_set(n))` contains two vertices from the same block, or
  zero vertices from some block, or the hull order is not block-index order, Conjecture A
  is false at that n.
- **Machine check (first-step for the tool_builder):** `es_construct.es_set_blocks(n)`
  returns the blocks; report the block index of each vertex returned by
  `es_geom.convex_hull(es_set(n))`. One vertex per block, in order ⇒ Conjecture A holds.

## Why it matters

If Conjecture A holds, the outer onion layer is exactly the "top spine" of the
construction (one point per block), and the non-trivial n-avoiding structure lives one
layer in. That pins down where the *placement-invariant* depth must live: block index =
arc position, and the adopted approach (`allowable-sequence-circular-representation`) asks
whether block index coincides with reversal-depth in the allowable sequence. Conjecture A
is the cheap preliminary that confirms the onion layer is a secondary statistic and the
reversal-depth statistic is the one carrying the binomial structure.

```claim
id: layer-profile-outer-hull-one-per-block
statement: In the verified es_construct placement of the ES construction X_n (n in {5,6,7}), the convex hull consists of exactly one point from each block T_0..T_{n-2}, so the outer onion layer has exactly n-1 vertices in block-index order.
hypotheses: es_construct.es_set placement (exact Fraction coordinates); n in {5,6,7}
holds-here: yes
status: checked — machine-verified by code/out/layer_conjecture_A.py (exact Fraction block matching of convex_hull vertices; exit 0). At n=5,6,7: hull vertices 4,5,6 = n-1; one point per block (all n-1 blocks); hull block sequence exactly [0,1,...,n-2] forward around the hull. PASS at all three n.
bearing: locates the binomial block structure at reversal depth (arc position), not onion depth; the onion profile [5,5,3,3] / [6,6,6,5,6,3] is a placement artifact, which is the exact premise the gale-transform approach assumed and the run's data refuted.
anchor: code/out/pattern_layers.py, code/out/pattern_finder_report.md, research/approaches/gale-transform-convex-layers.md
```
