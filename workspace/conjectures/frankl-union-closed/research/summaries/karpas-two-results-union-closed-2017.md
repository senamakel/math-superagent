# Karpas, "Two results on union-closed families" (arXiv:1708.01434, 2017)

**Full text:** [[karpas-two-results-union-closed-2017.full]]

Large-family bound: UC holds when |F| is close to 2^n.

```claim
id: karpas-large-families
statement: For a universal constant c>0, if |F| ≥ (1/2 − c)·2^n for a union-closed F ⊆ 2^[n], then some element appears in at least half the sets of F.
hypotheses: union-closed F ⊆ 2^[n], |F| ≥ (½−c)2^n
holds-here: yes
status: proved
bearing: the "large families" settled class in ROOT.md; complements the small-|F| verified bound (Karpas needs |F| within a linear margin of half of 2^n).
anchor: research/sources/karpas-two-results-union-closed-2017.full.md
```

```claim
id: karpas-covering-count
statement: For any union-closed F⊆2^[n], the number of sets outside F that cover (are/contained in the union-forming of) a set in F is at most 2^(n−1), with examples sharp.
hypotheses: union-closed F
holds-here: yes
status: proved
bearing: a counting structure on the complement of F, usable in minimal-counterexample density arguments.
anchor: research/sources/karpas-two-results-union-closed-2017.full.md
```

**Bearing:** gives a large-family control; the sharp counting inequality is a candidate structural lemma.
