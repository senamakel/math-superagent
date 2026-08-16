# Wilbrink & Brouwer, "A (57,14,1) strongly regular graph does not exist" (ZW 121/78, Math. Centrum, 1978; Indag. Math. 45 (1983) 117–121)

<!-- source: https://ir.cwi.nl/pub/6822/6822D.pdf -->
<!-- full text: research/sources/wilbrink-brouwer-57141-does-not-exist.full.md -->

The PRINTED predecessor of the star-complement reproof (Milošević 2008). A
genuinely close analogue of (99,14,1,2): **n=57, k=14, λ=1, μ=4**, spectrum
[1·14, 2³⁸, −5¹⁸]. Same valency and same λ=1 (hence same windmill 7K₂ local
structure) as the Conway graph; only μ differs (4 vs 2).

## The two methods

**Lemma 1 (the counting inequality).** For an induced subgraph H of an srg with
N points, M edges, degrees d_i:
```
(kN − 2M) − (λM + μ(C(N,2) − M) − Σ C(d_i,2)) ≥ n − N
```
with equality iff exactly (kN−2M)−(n−N) points of G\H are adjacent to exactly
two points of H, the rest adjacent to exactly one. This is a general second-
subconstituent counting tool, usable verbatim for any (99,14,1,2).

**Lemma 2 (coclique bound via min eigenvalue s).** A coclique S satisfies
`|S| ≤ n·(−s)/(k−s)` for s the negative root of x²+(μ−λ)x+(μ−k)=0, with
equality giving a 2-(v,K,μ) design on S. For (57,14,1,4): s=−5, coclique ≤ 15.

## The windmill / group-divisible-design structure (the part that transfers to 99)

Fix a vertex ∞. Γ(∞) has 14 points; λ=1 forces Γ(∞) to be 7 disjoint pairs
(**the groups** — the perfect matching 7K₂, identical to 99). Points outside
↔ blocks: each z outside Γ(∞) contributes B_z = {x∈Γ(∞) : x~z} of size μ.
So Γ(∞) with its groups and blocks is a **group divisible design** — for
(57,14,1,4), a GD[4,3,2;14] (blocks of size 4 = μ); for (99,14,1,2), μ=2 makes
the blocks of size 2, i.e. the 84 non-neighbours biject with the 84 non-edges
of the 7K₂ — exactly the G-reduce reduction in research/backward.

## The (57,14,1,4) contradiction machinery (two-regime)
- **15-coclique regime:** S a 15-coclique → points/blocks of a 2-(15,5,4) design;
  λ=1 forces each of the 7 triangles through a block B₀ to split 5-through-S /
  2-blocks-only; the intersection-number equations then force x₄=0, x₀+x₃=6 and
  a block-overlap argument yields a 5-common-neighbour contradiction (λ,μ≤4).
- **No-15-coclique regime:** shows G has no regular 6-vertex degree-3 subgraph
  (K₃,₃ or prism) via Lemma 1 twice; then via the GD structure shows two blocks
  meet the same four groups, forcing four common neighbours of a nonedge pair
  with intersection-3 — contradicting μ=4.

## Implication for (99,14,1,2)
The local seed (windmill 7K₂, group-divisible design Γ(∞)+with-blocks) is
**identical** for 99, with μ=2 replacing μ=4. The same Lemma-1 counting
inequality and the coclique bound apply (for 99: s=−4, coclique ≤ 99·4/18=22).
The analogue of the 2-(15,5,4)-design branch would be a 2-design on a 22-coclique
for 99. This is a concrete, fully general weapon the library had not credited —
the closest λ=1, k=14 precedent, with both the identical local geometry and a
transferable counting lemma.

## Status / caution
- Primary source (CWI report + Indag. Math. 1983); arguments read from the full
  text, not machine-reproduced here. The lemma-1 inequality and the GD structure
  are elementary and hold verbatim for any (99,14,1,2); the specific contradiction
  (2-(15,5,4) design, prism exclusion) is tuned to μ=4.
- Does not decide 99; supplies the transferable machinery (Lemma 1 counting;
  coclique design branch) and confirms 99's local structure is shared with a
  k=14 λ=1 case that was settled.

```claim
id: wilbrink-brouwer-5714ceedings
statement: srg(57,14,1,4) does not exist (CWI 1978 / Indag. Math. 1983). Key
  transferable facts: (i) Lemma 1 counting inequality kN-2M - (lambda M + mu
  C(N,2)-M - sum C(di,2)) >= n-N for an induced subgraph, equality iff
  (kN-2M)-(n-N) exterior points have exactly 2 neighbours in H; (ii) coclique
  bound |S| <= n(-s)/(k-s), equality gives a 2-(v,K,mu) design; (iii) the
  local structure is the same as 99's: G(infty) = 7 disjoint pairs (the
  groups), exterior points = blocks of size mu forming a group divisible
  design (GD[4,3,2;14] here, blocks of size 2 = 84 non-edges of 7K2 for 99).
hypotheses: srg(57,14,1,4) existence assumed then contradicted; for the
  transferable parts, any srg(v,k,1,mu) with the same local 7K2.
holds-here: yes for the local structure and Lemma 1 / coclique bound (these
  apply verbatim to (99,14,1,2)); the specific 2-(15,5,4)/prism contradiction
  is mu=4-specific and does not transfer.
status: sourced (primary CWI report full text in library; the local 7K2 and
  lemma are verified-from-parameters, not re-computed as a contradiction).
bearing: supplies the closest lambda=1, k=14 precedent (same windmill local
  geometry) and transferable counting / coclique-design tools for the derived
  design at a vertex; reframes (57,14,1,4) as the template the run should compare
  the (85,14,3,2) template against.
anchor: research/sources/wilbrink-brouwer-57141-does-not-exist.full.md
contradicts: none
```

[[wilbrink-brouwer-57141-does-not-exist.full]]
