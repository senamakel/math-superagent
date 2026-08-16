# Layer-extremality of the ES construction — an executed structural lemma

**Computed by `code/out/layer_extremality.py`, captured in
`layer_extremality.captured.txt` (exact-oracle, exit 0).**

## The statement

For the verified `es_construct` realisation `X_n` of the Erdős–Szekeres
$2^{n-2}$-point, no-convex-$n$-gon construction ($n \in \{5,6,7\}$), peel the
onion layers. Every layer is **maximally convex** under the no-convex-$n$-gon
constraint:

- a layer of size $m \ge n-1$ contains $n-1$ points in convex position;
- a layer of size $m < n-1$ is entirely in convex position (a convex $m$-gon).

So the whole no-convex-$n$-gon obstruction lives **strictly across** layers:
each layer individually is as convex as the ceiling allows, and convexity is
broken only by combining points from two or more different layers. No layer
internally "wastes" convexity budget.

## The data (exact oracle, `has_convex_k_subset` / `in_convex_position`)

| n | onion profile | layer verdicts | Conjecture C |
|---|---|---|---|
| 5 | [4,4]        | both layers contain convex 4-gon                | PASS |
| 6 | [5,5,3,3]    | layers 0,1 contain convex 5-gon; 2,3 fully convex | PASS |
| 7 | [6,6,6,5,6,3]| layers 0..4 contain convex 6-gon; layer 5 (3) fully convex | PASS |

(n=4 gives [3,1]; the singleton inner layer is a fence-posting artefact — a
1-point layer has no convex position, so the "maximally convex" test is
vacuous for it. The meaningful cases are n ≥ 5, where every layer has at
least 3 points.)

## What it does and does not establish

- **Established (checked, exact arithmetic):** Conjecture C holds for the
  `es_construct` placement at n = 5, 6, 7.
- **Not established:** Conjecture C for *every* extremal set, or for other
  realisations of X_n, or for n ≥ 8. The result is scoped to this verified
  template. It is a structural lemma about the ES construction, not a claim
  about all hypothetical $2^{n-2}$-point no-$n$-gon sets.

## Bearing — the structural insight

The onion profiles are placement artifacts ([5,5,3,3] / [6,6,6,5,6,3], not the
binomial block sizes [1,4,6,4,1] / [1,5,10,10,5,1]) — see
`layer_profile_conjecture.md`. What survives placement, this run now shows, is
an extremality at the *layer* level: however the set is peeled, every layer is
as convex as the global no-$n$-gon ceiling permits. That pins the obstruction
to pairwise/triple *across-layer* geometry, exactly the structure a
split/decomposability argument (baek-balko-split) needs, and is the
layer-level analogue of the per-block cup+cap=n tightness
(`es-construct-block-tightness`).

```claim
id: es-construct-layer-extremality
statement: In the verified es_construct realisation of the ES construction X_n (n=5,6,7), every convex (onion) layer is maximally convex: a layer of size m>=n-1 contains n-1 points in convex position, and a layer of size m<n-1 is fully convex. Equivalently, no no-convex-n-gon obstruction occurs inside a single layer.
hypotheses: the es_construct XOR placement (exact Fraction coordinates); n in {5,6,7}; onion peeling via es_geom.convex_hull.
holds-here: yes — this is the run's own verified lower-bound construction.
status: checked (exact-arithmetic oracle, captured in code/out/layer_extremality.captured.txt, exit 0)
bearing: structural lemma (GOAL 2/4): the ES construction's layers are individually extremal, so the n-avoiding obstruction is entirely across-layer geometry — the layer-level analogue of es-construct-block-tightness, and the structure a split argument needs.
anchor: code/out/layer_extremality.py, code/out/layer_extremality.captured.txt
```
