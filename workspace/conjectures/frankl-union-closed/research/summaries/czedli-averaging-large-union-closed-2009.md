<!-- source: https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli_on-averaging-Frankl's-conjecture-for-large-union-closed-sets.pdf -->

# Czédli, "On averaging Frankl's conjecture for large union-closed-sets" (2009) — summary

**Source URL:** https://www.math.u-szeged.hu/~czedli/m/publ.pdf/czedli_on-averaging-Frankl's-conjecture-for-large-union-closed-sets.pdf
**Full text:** `research/sources/czedli-averaging-large-union-closed-2009.full.md`
**Bibliographic:** J. Combin. Theory Ser. A 116 (2009), 724–729. DOI 10.1016/j.jcta.2008.08.002 (submitted version).

## What this paper is

The paper that established the **averaged Frankl property** for large
union-closed families (a strengthening: the sum over all elements of
(n − 2s(a)) ≤ 0, which implies an abundant element exists). It uses a purely
lattice-theoretic proof for a statement stated combinatorially — one of the few
such bridges.

## Main theorem

**Theorem 1.** If F is a union-closed family over a nonempty m-element set A,
m ≥ 3, and F is *large* in the sense

  n := |F| ≥ 2^m − 2^(m/2) = 2^m − √(2^m),

then F satisfies the averaged Frankl property: ∑_{a∈A}(n − 2s(a)) ≤ 0.

This strengthens a result of Gao–Yu in two ways: it proves the averaged property
(not just existence of an abundant element), and the threshold 2^(m/2) is much
weaker than the earlier 2^(m/2) with a different base in formula (1).

## Proved lattice-theoretic engine

**Theorem 2.** Let L be a finite lattice with at least two elements, m := |J(L)| ≥ 3.
If |L| ≥ 2^m − 2^(m/2) then r(L) := ∑_{a∈J(L)}(|L| − 2|↑a|) ≤ 0, i.e. the
averaged lattice Frankl inequality holds.

The proof runs through the representation of L as a factor semilattice
P(X)/θ of the free join-semilattice, the excess e([u]) = |[u]|−1 of a θ-class,
and a key lemma bounding the height of abundant classes: if [u] ∈ L is abundant
(e([u]) > 0) then height h([u]) ≤ m/4 − 1.

The deduction of Theorem 1 from Theorem 2 uses the bijection J(D) → A given by
join-irreducibles of the closure system D = {A \ X : X ∈ F} to elements of A,
showing |{Y ∈ F : a∈Y}| ≤ |F|/2 iff |↑X| ≤ |D|/2 = n/2.

## Relation to the claim store

This is a companion to the on-disk Czédli–Maróti–Schmidt "On the scope of
averaging for Frankl's conjecture" (Order 2009, `czedli-maroti-schmidt-scope-averaging-2009.full.md`).
Together they delimit the averaging method: the averaged property holds for
large families (this paper) and fails in general (CMS).

## Claim blocks

```claim
id: czedli-averaged-frankl-large-families
statement: For a union-closed family F over an m-element set A, m ≥ 3, with
  n = |F| ≥ 2^m − 2^(m/2), the averaged Frankl property holds:
  ∑_{a∈A}(n − 2·|{B∈F : a∈B}|) ≤ 0; in particular Frankl's conjecture holds
  for such large families.
hypotheses: F finite union-closed over A, |A|=m≥3, |F| ≥ 2^m − 2^(m/2).
holds-here: yes
status: asserted-by-source (published JCTA 116 (2009) 724–729)
bearing: Primary source for the "large families" settled class: |F| close to
  2^m forces UC via the averaged inequality. Together with
  czedli-maroti-schmidt averaging-limits it delimits the averaging method.
anchor: research/sources/czedli-averaging-large-union-closed-2009.full.md
falsifies: A union-closed F with these parameters violating the averaged
  inequality, or a counterexample in the large regime.
```

```claim
id: czedli-lattice-averaged-large
statement: For a finite lattice L with m = |J(L)| ≥ 3 and |L| ≥ 2^m − 2^(m/2),
  the averaged lattice-theoretic Frankl inequality holds:
  ∑_{a∈J(L)}(|L| − 2|↑a|) ≤ 0.
hypotheses: L finite lattice, |L| ≥ 2, |J(L)| = m ≥ 3, |L| ≥ 2^m − 2^(m/2).
holds-here: yes
status: asserted-by-source (proved in the paper)
bearing: Lattice-side companion of czedli-averaged-frankl-large-families; the
  proof uses the P(X)/θ representation and height bound h([u]) ≤ m/4 − 1 for
  abundant θ-classes.
anchor: research/sources/czedli-averaging-large-union-closed-2009.full.md
falsifies: A finite lattice meeting the hypotheses with positive averaged
  excess r(L).
```