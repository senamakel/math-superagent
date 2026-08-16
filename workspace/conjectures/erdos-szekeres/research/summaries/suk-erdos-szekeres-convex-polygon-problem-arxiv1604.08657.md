# Suk 2017, "On the Erdős–Szekeres convex polygon problem", JAMS 30(4), 1047–1053

Source: https://arxiv.org/pdf/1604.08657 (JAMS DOI 10.1090/jams/869)
Full text: [[suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full]]

The 2010s breakthrough: the base of the exponent drops from 4 to 2.

## What it establishes

```claim
id: suk-bound
statement: ES(n) <= 2^{n + 6 n^{2/3} log n} for all n >= n0 (a large absolute constant); hence ES(n) = 2^{n+o(n)}.
hypotheses: n large
holds-here: yes
status: proved
bearing: first 2^n-base upper bound; the exact conjecture ES(n)=2^{n-2}+1 remains the 'no slack at all' gap no SUK-style method reaches.
anchor: research/sources/suk-erdos-szekeres-convex-polygon-problem-arxiv1604.08657.full.md
```

Key ingredients (for the run's structure work): positive-fraction ES theorem (Lemma 2.4 source:
Theorem 4 in [20], Bárány–Valtr/Pór–Valtr) giving a $k$-element subset in convex position when
$|P|\ge 2^{32k}$; the 4-criterion (Lemma 2.1); dense subsets $Q_{jr}$; cup/cap supports; the
separation argument that a union of disjoint caps of size $\lceil 2n^{2/3}\rceil$ is itself a cap.
Uses: every large set has a big convex subset (2^{32k} bound), then a dichotomy into an $n$-cup or
a $\lceil 2n^{2/3}\rceil$-cap on dense boxes, then cap-union separation.

## What it does not settle

Exact value; the error term $6n^{2/3}\log n$ is far from the $-(n-2)$ needed. The method is
inherently asymptotic (positive-fraction results). Does not bear on restricted-class exact
statements except as the reason no counting/positive-fraction route reaches $2^{n-2}$ exactly.
