# Damásdi, Dong, Scheucher, Zeng 2024, "Saturation results around the Erdős–Szekeres problem", SoCG 2024

Source: https://arxiv.org/pdf/2312.01223
Full text: [[damasdi-dong-scheucher-zeng - Saturation results around the Erdos-Szekeres problem - SoCG 2024 full.full]]

## What it establishes

```claim
id: damasdi-saturation
statement: For each n >= 7 there is a planar set of (7/8)·2^{n-2} points that is saturated for convex n-gons (no n in convex position, adding any one point creates one); the ES construction itself is saturated. Saturation number < Ramsey number for ES.
hypotheses: n >= 7, planar general position
holds-here: yes
status: proved
bearing: killing the naive stability direction — an extremal-size set that is saturated can be much smaller than 2^{n-2}, so near-extremal/(anti)extreme sets need not be tight against the recursive construction; the ES construction is nonetheless saturated (maximal without the property).
anchor: research/sources/damasdi-dong-scheucher-zeng - Saturation results around the Erdos-Szekeres problem - SoCG 2024 full.full.md
```

Also improves the saturation version of cups-versus-caps, and shows that in the abstract ordered
3-uniform-hypergraph generalization, saturation number EQUALS the Ramsey number (contrast with the
geometric ES case). Based on monotone-path/cup-cap saturation.

## Significance

Structural constraint for a hypothetical extremal set: saturation alone does not pin a 2^{n-2}-set
to the ES construction. Any "extremal sets are ≈ the ES construction" stability lemma must be
argued against this (7/8)·2^{n-2} saturated example. If the run proves a structural claim assuming
the set is exactly of size 2^{n-2} AND saturated, this source matters; if only size, it matters less.
