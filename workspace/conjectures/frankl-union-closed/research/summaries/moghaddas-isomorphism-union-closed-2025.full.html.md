# Moghaddas Mehr — "Isomorphism in Union-Closed Sets" (arXiv:2501.02637, Jan 2025)

**Source URL:** https://arxiv.org/abs/2501.02637 (full: https://arxiv.org/html/2501.02637v3)
**Full text:** [[moghaddas-isomorphism-union-closed-2025.full.html]] (the `.full.md`
landing-page copy is only the abstract; use the `.html` copy for content)

## What it is

A structural / lattice-representation paper. It does **not** move the conjecture's
bound and proves no new restricted class for Frankl's conjecture. Its contribution
is a *faithfulness* theorem for the lattice encoding that the run's lattice angle
relies on.

## The main theorem (Theorem 4.1)

Let `K₁`, `K₂` be **pure** union-closed families of sets. For every isomorphism
`h : K₁ → K₂` (a bijection preserving union: `h(A∪B) = h(A)∪h(B)`), there is a
**hyperisomorphism** `H : ⋃K₁ → ⋃K₂` (a bijection of the union/ground sets) such
that for every `A ∈ K₁`:

```
h(A) = { H(a) : a ∈ A }.
```

So *every* isomorphism of pure union-closed families is induced by a bijection on
the underlying ground elements. Combined with the standard fact that a union-closed
family containing `∅` forms a lattice under inclusion, this means the lattice
representation is a **faithful encoding**: a pure union-closed family is uniquely
reconstructed from its lattice up to isomorphism. This is the precise sense in
which "nothing is lost" by passing a union-closed family to its inclusion lattice.

## Supporting machinery (all elementary)

- **Definitions.** An element `z` is *redundant* in `K` if deleting it from every
  member leaves `|K|` unchanged; `K` is *pure* if it has no redundant element.
  Every union-closed `K` is isomorphic to its "purified" reduction `K*`
  (Lemma 2.3, Cor 2.3). **For Frankl's conjecture this is the key observation to
  keep in mind**: a redundant element appears in *all* member sets, hence is
  trivially abundant (density 1), so any counterexample is automatically pure —
  the purity hypothesis costs nothing for the conjecture.
- **Cardinality Theorem (Thm 3.1).** An isomorphism between pure union-closed
  families preserves set sizes: `|A| = |h(A)|` for all `A`.
- **Lemma 4.1.** In a pure family, elements are separated by their "profile":
  `K^i := {A ∈ K : i ∈ A}` satisfies `i = j ⟺ K^i = K^j`. This is the exact
  statement that purity = no two elements are "twins".
- **Lemma 4.4.** Under an isomorphism, the profile of an element maps to the
  profile of a (unique) element; this is what lets `H` be defined on elements.

Theorem 4.1 follows by gathering the per-element map into one bijection `H`.

## Why it matters for this run

- **Justifies the lattice angle.** The lattice formulation gives UC as a
  statement about join-irreducibles of finite lattices (Poonen). This paper makes
  precise that the passage family → lattice loses no information (for pure
  families, and any counterexample is pure), so a lattice-class proof really is a
  statement about the original family. It adds a clean formal justification to a
  step the run has been using on faith.
- **Purity is free for the conjecture.** Since redundant elements are abundant
  (density 1), restricting attention to pure families is a legitimate
  normalisation that any UC argument may assume. Worth recording as a hypothesis
  simplification.
- It surveys (Introduction) the standard settled lattice classes — distributive,
  geometric (Rival/Poonen), relatively complemented (Poonen), modular
  (Abe–Nakano), lower semimodular (Reinhold, the strongest standard-class
  result), lower quasi-semimodular (Abe–Nakano), large + planar semimodular
  (Czédli–Schmidt), dismantlable and breadth-two (Joshi–Waphare–Kavishwar /
  Joshi–Waphare), subgroup lattices + modular coatom (Abdollahi–Woodroofe–Zaimi).
  **Upper semimodular in general remains open** — consistent with ROOT.md.

## Status

Sourced (arXiv preprint, v3). Not a bound, not a counterexample, not a new
settled class. It is a structural/foundational result on the lattice encoding;
the run should treat it as supporting the lattice approach, not as progress on the
constant. Hypotheses check out against this problem on its face; no independent
re-derivation was run (the content is elementary enough that a small brute-force
check of Thm 4.1 on `n ≤ 4` would be a cheap future cross-check if the oracle is
extended).

```claim
id: moghaddas-isomorphism-encoding
statement: An isomorphism between pure union-closed families is always induced by
  a bijection of the ground elements (a hyperisomorphism); hence a pure
  union-closed family is uniquely reconstructed from its inclusion lattice up to
  isomorphism. Since redundant elements are abundant (density 1), any
  counterexample may be assumed pure, so the lattice encoding is faithful for the
  conjecture.
hypotheses: K₁, K₂ pure union-closed families of sets; h a union-preserving
  bijection.
holds-here: yes — this is a foundational justification of the lattice formulation,
  not a bound or a settled class; it does not touch the constant.
status: asserted-by-source (arXiv preprint, elementary proof; not re-derived by the
  run's oracle).
bearing: legitimises treating a counterexample as pure (all elements non-redundant)
  and trusting the lattice representation as lossless.
anchor: research/sources/moghaddas-isomorphism-union-closed-2025.full.html.full.md
```
