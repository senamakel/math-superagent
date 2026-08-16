# Leaf to leaf path lengths in trees of given degree sequence

**Rautenbach, Scherer, Werner**. arXiv:2507.10351v2 (Jul 2025). Full text:
`research/sources/rautenbach-leaf-to-leaf-paths-trees.full.md`.

<!-- source: https://arxiv.org/html/2507.10351v2 -->

## What it establishes

- **Theorem 3**: If $s$ is the degree sequence of a tree $T$ with no vertex of
  degree 2, then $lp(T) \ge \mathrm{rad}(s) - \log_2(\mathrm{rad}(s))$, where
  $lp(T)$ is the number of distinct leaf-to-leaf path lengths and
  $\mathrm{rad}(s)$ is the minimum radius among trees realising $s$.
- **Conjecture 2** (the target, unproved): $lp(T) \ge \mathrm{rad}(s) - O(1)$.
- **Theorem 1** (Di Braccio et al., quoted): if $T$ has maximum degree
  $\Delta \ge 3$ and $\ell$ leaves, then
  $lp(T) \ge \log_{\Delta-1}((\Delta-2)\ell)$; shown essentially tight by the
  trees $T_{\Delta,h}$.
- **Lemma 4**: if a rooted tree has leaves of $k$ different depths then
  $lp \ge k$. **Lemma 6**: $k$ equal-depth leaves give at least
  $h(s^+,k)+1$ distinct leaf-to-leaf lengths.
- **Final observation (Kraft-type)**: for a full binary tree with $\ell$ leaves
  and multiset $\mathcal{W}$ of leaf-to-leaf path lengths of non-trivial pairs,
  $\sum_{w\in\mathcal{W}} 2^{-w} \le (\ell-1)/4$, equality iff full binary.

## Relevance to this run

- This is part of the **degree-3-critical / 1-3 tree** literature that the
  run's near-cubic structural spine rests on. The motivating construction is
  Narins–Pokrovskiy–Szabó's use of 1–3 trees (all degrees 1 or 3, i.e. no
  degree-2 vertices) to build degree-3-critical counterexamples to the
  EFGS many-short-cycles conjecture.
- The bound $lp(T) \ge \mathrm{rad}(s) - \log_2(\mathrm{rad}(s))$ quantifies
  how many distinct leaf-to-leaf path lengths a 1–3 tree is forced to realise
  — a structural input to the question of how many distinct cycle lengths a
  degree-3-critical graph (the near-cubic spine) must contain. Sparse spectra
  are nonetheless possible (cf. Di Braccio et al. $O(N^{0.91})$), so a large
  $lp$ does not collide with a sparse distribution relative to *powers of two*
  in any obvious way — record only that 1–3 trees realise many distinct
  leaf-to-leaf lengths, not that they realise a power of two.

## Status

The theorem is asserted by the source (a 6-page arXiv note, v2). Not verified
by recomputation here. It answers Rautenbach–Scherer–Werner's own question from
the Di Braccio et al. paper; it does not itself bear on Erdős–Gyárfás directly.

```claim
id: rsw-lp-tree-radius-bound
statement: For a tree T with no vertex of degree 2 and degree sequence s, the number lp(T) of distinct leaf-to-leaf path lengths satisfies lp(T) >= rad(s) - log2(rad(s)), where rad(s) is the minimum radius among trees realising s.
hypotheses: tree T, no degree-2 vertex, degree sequence s
holds-here: yes (1-3 trees are exactly trees with no degree-2 vertex, so this bounds the leaf-leaf length variety of the trees used in the NPS construction)
status: asserted (full text held)
bearing: quantifies how many distinct leaf-leaf path lengths a 1-3 tree is forced to realise (logarithmic in radius); feeds the near-cubic spine's understanding of cycle-spectrum variety in degree-3-critical graphs. Conjecture 2 (lp >= rad(s) - O(1)) left open.
anchor: research/sources/rautenbach-leaf-to-leaf-paths-trees.full.md
```

```claim
id: rsw-kraft-full-binary-leaf-lengths
statement: If T is a rooted full binary tree with ell leaves and W is the multiset of all (ell choose 2) non-trivial leaf-to-leaf path lengths, then sum_{w in W} 2^{-w} <= (ell-1)/4, with equality iff T is full binary.
hypotheses: full binary tree, ell leaves
holds-here: yes (1-3 trees are full binary after contracting degree structure)
status: asserted (full text held)
bearing: a Kraft-type density constraint on the multiset of leaf-to-leaf path lengths of a binary tree; an analytic handle on how sparse/rich that length multiset can be in the near-cubic spine's tree gadgets.
anchor: research/sources/rautenbach-leaf-to-leaf-paths-trees.full.md
```

