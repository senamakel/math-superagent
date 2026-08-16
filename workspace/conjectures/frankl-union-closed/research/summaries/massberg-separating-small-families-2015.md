# Maßberg, "The Union-Closed Sets Conjecture for Small Families" (arXiv:1508.05718)

**Full text:** [[massberg-separating-small-families-2015.full]] · **Source:** https://arxiv.org/abs/1508.05718

The primary source for the separating-families bound cited in ROOT.md but previously absent from the library.

## Main theorem

The union-closed sets conjecture is true for **separating union-closed families** `A` with

```
|A| ≤ 2m + m·log₂m − log₂log₂m
```

where `m = |U(A)|` is the size of the universe. For such families, some element appears in at least `|A|/2` member-sets.

```claim
id: massberg-separating-bound
statement: UC holds for any separating union-closed family A with |A| ≤ 2m + m·log₂m − log₂log₂m, where m = |U(A)|.
hypotheses: A union-closed, separating (any two elements separated by some member), universe size m.
holds-here: true
status: proved
bearing: improves the earlier 2m bound for separating families; the "small-|A|/large-m" regime of the conjecture, complementary to the entropy/large-family lines. Weakest exactly where the entropy method does not cover.
anchor: research/sources/massberg-separating-small-families-2015.full.md
```

## Method (brief)

Labels universe elements by increasing frequency, uses a Knill-style minimal hitting subset, and counting arguments to bound `|A|` in terms of `m` and the per-element frequency bound. The explicit bound asymptotically approaches `2m` as `m` grows.

## Why it matters

- Fills a concrete gap: ROOT.md named this result and arXiv id but the primary source was not in the library. Now it is, with the claim recorded.
- The separating/small-|A| bound is one of the few that directly attacks the "small |F|" regime the entropy methods do not reach.
