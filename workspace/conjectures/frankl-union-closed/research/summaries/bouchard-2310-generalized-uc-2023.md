# Bouchard, "Union-closed families of sets" (arXiv:2310.02482, 2023)

**Full text:** `research/sources/colbert-chain-conditions-generalized-uc-2025.full.md`
(full text was auto-filed under the mislabeled name "colbert-… " by the downloader;
its content is Bouchard's arXiv:2310.02482 paper, which this summary covers) ·
**Source URL:** https://arxiv.org/pdf/2310.02482

> **Attribution correction.** This paper (arXiv:2310.02482, also published via
> Colbert chain-conditions line) is by **Chris Bouchard (2023)**, the same author
> as the later 2025 lattice paper already held
> (`bouchard-lattice-formulation-minimal-counterexample-2025`). It is an earlier,
> *different* work. It is NOT Colbert's survey (which is unpublished and not
> held); the filename's "colbert" is a mislabel I introduced; the content is
> Bouchard's UCx paper.

## What it establishes — the UCx ladder

For a union-closed family `A` on ground set `[n]`, define for `B ⊆ [n]`:
`A_B = {A ∈ A : B ⊆ A}` and `A_{B} = {A ∈ A : A ∩ B = ∅}`. For `x ∈ [n]` the
conjecture

```
UCx : ∃B, |B| = n−x+1, such that |A_B| ≥ |A_B|   (complementary class dominates)
```

has `UCn` as the extremal case `|B| = 1`, which is exactly Frankl's conjecture.
So UCx is a *parameterised ladder* climbing from small x to the full conjecture.

```claim
id: bouchard-ucx-ladder
statement: For any union-closed family A on [n], UCx holds for all x ∈ [⌈n/3⌉ + 1];
  i.e. there is B with |B| = n−x+1 and |A_B| ≥ |A_B|. An affirmative answer to
  an open question (Question 2.2) would extend this to all x ∈ [⌊n/2⌋ + 1].
hypotheses: A finite nonempty union-closed family on [n], n ≥ 1.
holds-here: yes (statement about all union-closed families; UCn is Frankl).
status: proved for the stated range (Theorem 2.1 in source).
bearing: UCn−1 ⟹ UCn gives a *reduction*: to prove Frankl it suffices to prove it
  one step down the ladder. Proves UCx for all x up to ⌈n/3⌉+1, i.e. covers all
  B of size ≥ n − (⌈n/3⌉+1) + 1 = n − ⌈n/3⌉.
anchor: research/sources/bouchard-2310-generalized-uc-2023.full.md
```

```claim
id: bouchard-ucn-minus1-to-ucn
statement: For any union-closed family A with n > 1, UC_{n−1} ⟹ UC_n. (Proving the
  conjecture for the second-to-largest complementary class forces the full one.)
hypotheses: A finite nonempty union-closed family on [n], n > 1.
holds-here: yes
status: proved (Theorem 2.4 in source).
bearing: a concrete reduction of the size of the question — Frankl would follow
  from a statement about (n−1)-sets' complementary classes.
anchor: research/sources/bouchard-2310-generalized-uc-2023.full.md
```

```claim
id: bouchard-conj33-implies-uc
statement: Conjecture 3.3 (if an element y of maximum frequency has
  A = A_{y} ∪ A_{z} for some z, then |A_{y}| ≥ 2·|A_{\underline{y}}|) implies
  Frankl's conjecture (Theorem 3.6). Also Conjecture 1.1 ⟹ Reimer's theorem
  (Proposition 3.2), and Poonen's separating conjecture (Conjecture 4.1) implies
  Frankl's.
hypotheses: the stated strengthenings.
holds-here: conditional (open questions in source; they would settle UC).
status: proved implications (source proves each strengthening ⟹ UC).
bearing: gives two conditional routes to UC via strengthenings that constrain the
  nested/maximum-frequency structure — candidates for the structural line.
anchor: research/sources/bouchard-2310-generalized-uc-2023.full.md
```

## Bearing for this run
The `UCx` ladder and the `UC_{n−1} ⟹ UC_n` reduction are a distinct structural
handle not otherwise in the library: they reformulate the target as a family of
complementary-class inequalities and let one reduce n. Relevant to the
minimal-counterexample line (the run's GOAL class 5) because a counterexample
would have to fail UCₙ while passing UC_{n−1}, pinning its structure.
