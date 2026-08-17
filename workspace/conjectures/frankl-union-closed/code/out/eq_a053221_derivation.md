# EQ(n) = A053221 — derived decomposition

**Result.** The number of empty-free union-closed families on `[n]` achieving
the KPT Theorem 5(3) equality `f == min{N, 2k−N+1}` (where `N` = max set size,
`k` = min set size, `f` = # elements in strictly more than half the sets) is

```
EQ(n) = (2^n − 1) + n·(2^{n−1} − 1) = (n+2)·2^{n−1} − n − 1
```

which is OEIS **A053221**. Values `n=1..5`: `1, 5, 16, 43, 106`.

## The decomposition

Every such family is provably a **singleton** `{A}` or a **strict two-chain**
`{A, A∪{x}}` (with `A ≠ ∅`, `x ∉ A`).

- **Singleton `{A}`, `|A|=k`.** `m=1`, every element of `A` has count `1`,
  `2·1 > 1`, so all `k` are strict-abundant: `f = k`. And `k = N`, so
  `min{N, 2k−N+1} = min{k, 2k−k+1} = k = f`. ✓ Equality.
  Count: `2^n − 1`.

- **Two-chain `{A, A∪{x}}`, `|A|=k`, `x∉A`.** `m=2`; the `k` elements of `A`
  have count `2`, `2·2 > 2`, so `f = k`. `k = min`, `N = k+1`, so
  `min{N, 2k−N+1} = min{k+1, 2k−(k+1)+1} = min{k+1, k} = k = f`. ✓ Equality.
  (Any 2-set union-closed family has `A ⊆ B`; the equality forces `N = k+1`,
  so `B = A∪{x}` with `x∉A`.) Count: choose `A` of size `k` and one element
  from its complement: `Σ_{k=1}^{n−1} C(n,k)(n−k)`. Since
  `Σ_k (n−k)C(n,k) = n·2^{n−1}` and the `k=0` term is `n` (a chain `{∅,{x}}`
  — but ∅ is excluded in the empty-free convention, so subtract `n`),
  this is `n(2^{n−1} − 1)`.

Sum: `(2^n − 1) + n(2^{n−1} − 1) = (n+2)2^{n−1} − n − 1`. ✓

## Verification

- **Sufficiency** (singletons + two-chains all satisfy equality): **proved**
  directly above, exactly, with no search.
- **Counting**: the closed-form matches the exhaustive counts n=1..5 exactly
  (all empty-free nonempty UC families via the validated cascade).
- **Necessity** (no other family achieves the equality): **verified, not
  proved** — this is the crux, labelled a structural conjecture. Evidence:
  - exhaustive n=1..5 (all 2.77M families at n=5);
  - exhaustive n=6 over all UC families with `|F| ∈ {2,3,4}`: 186 EQ
    families, all strict two-chains; **0** EQ among the 3- and 4-set families;
  - random closure probes n=6,7,8 (~345k + ~460k families): 0 counterexamples.

## Crux / first falsifier

The necessity direction is the single step separating the derived identity (at
`n ≤ 5`, exact) from a theorem for all `n`. The KPT paper proves bound (3) by
a simple averaging argument and explicitly does *not* characterize the
equality case (it says (3) "likely has ample room for improvement").
**First falsifier:** an empty-free union-closed family on `n ≥ 6` with
`k ≤ n−1`, `f = 2k−n+1`, and a largest set of size `n ≥ k+2` (i.e. any
`≥ 3`-set family, or a 2-set family that is not a strict two-chain).

## Status labels

- Sufficiency half + closed-form identity: **derived** (proved + exhaustive
  n≤5 match).
- Necessity half: **verified-computational** n≤6 (all |F|≤4) + exhaustive
  n≤5 + random n≤8; **structural conjecture** for general n.
- The identity EQ(n) = A053221 is **verified-computational n≤5** and rests on
  the necessity conjecture beyond that.

## Files

- `code/out/eq_clean_verify.py` — clean decomposition check (n=1..5, exact).
- `code/out/eq_classify.py` — (k,N) split of EQ families (n=1..5).
- `code/out/eq_decomposition_verify.py`, `code/out/eq_len2_investigate.py` —
  prior verification/investigation of the size-2 EQ families.
- `code/out/eq_lemma_probe.py`, `code/out/eq_lemma_targeted_hunt.py` — random
  hunt at n=6..8.
- `code/out/eq_necessity_n6.py` — exhaustive n=6, |F| ∈ {2,3,4}.
