# Tian — "Union-closed Sets Conjecture Holds for Height No More Than 3 and Height No Less Than N−1" (arXiv:2112.06659, 2021)

**Source URL:** https://arxiv.org/pdf/2112.06659 · **Full text:** [[tian-union-closed-height-2021.full]]

## What it establishes

A settled restricted class via the **height number** `H(𝓕)` of a union-closed
family — a lattice-theoretic parameter (the number of steps in a height
decomposition of `𝓕`). Main theorem: for any finite union-closed family
`𝓕(n,m)` (n elements, m sets),

```
UC holds if H(𝓕) ≤ 3  or  H(𝓕) ≥ n − 1.
```

This is the primary source for the "chain/height ≤ 3" class. It is the class
that Wikipedia's note 9 cites under the shorter "chain no more than 3 or long
chain no less than n−1" form, and it is the finite-case companion to Colbert's
paper (already in the library, arXiv:2412.07747), which extends the
chain-length-≤-3 result to infinite union-closed families and topological
spaces.

Method sketch (from the digest / full text): define height decomposition and
height number `H(𝓕)`; prove structural lemmas (height-2 properties, "tent"
sub-family construction `T(A)` with `H(T(A))=2`, intersection bound
`Int(A,B) ≤ 1`); split `H ≤ 3` into `m > 2n` (Proposition 3.2.1, an abundant
element exists) and `m ≤ 2n`; and reduce via separating families
(Fact 3.3.1: UC for height ≤ k ⟺ UC for separating families of height ≤ k),
Theorem 23 of Bruhn–Schaudt (separating on ≤ 2n sets) and its corollary.

## Verification status

This is an **asserted-by-source** result (a published-style arXiv paper whose
proof is not re-derived by this run's oracle). The class is real and matches the
independently-cross-checked Wikipedia entry. The `H ≥ n−1` direction has no
independent source in the library; the `H ≤ 3` direction is corroborated by
Colbert (arXiv:2412.07747) for chain length ≤ 3.

```claim
id: tian-height-class
statement: A finite union-closed family 𝓕(n,m) satisfies the union-closed sets
  conjecture whenever its height number H(𝓕) satisfies H(𝓕) ≤ 3 or H(𝓕) ≥ n−1.
hypotheses: 𝓕 finite union-closed, n = |union of members| = ground-set size,
  m = |𝓕|; H(𝓕) is the lattice-theoretic height number defined in the paper.
holds-here: yes — a settled restricted class; the height-near-extremal family is
  a genuine structural case.
status: asserted-by-source (arXiv:2112.06659; proof not re-derived by this run's
  oracle; the H≤3 subcase independently corroborated by Colbert 2412.07747).
bearing: adds the height-parameter class to the settled list; complements
  Colbert's chain-condition work. Note Wikipedia's "chain ≤ 3 or ≥ n−1" phrasing
  is this same result.
anchor: research/sources/tian-union-closed-height-2021.full.md
```

## Why it matters for this run

It is a **structural family classification** — proving UC by the *height* of the
family — the kind of restricted class the run's GOAL item 4 asks about. It also
gives the run a template: Tian reduces the hard `H ≤ 3, m ≤ 2n` case to
separating families and cites Theorem 23 of Bruhn–Schaudt (separating with
`m ≤ 2n` ⟹ UC), which the library already holds a generalization of
(`falgasravry-separating-weight`, `massberg-separating-bound`). The exact
boundary Chung between Tian's class and Colbert's chain-length framing is a
point the scholar could reconcile.
