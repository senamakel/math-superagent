# Colbert, "Chain Conditions and Optimal Elements in Generalized Union-Closed Families of Sets" (arXiv:2412.18740, 2024)

**Full text:** [[colbert-chain-conditions-2412.full]] · **Source URL:** https://arxiv.org/pdf/2412.18740

**Attribution:** last name **Colbert** (distinct from Bouchard's arXiv:2310.02482, which was
mislabeled "colbert" in an earlier download; this is the real Colbert paper).

## What it establishes

Introduces **optimal elements**: `x ∈ U_F` is *optimal* if `F_x` is a maximal element of
`N(F) = {F_x : x ∈ U_F}` under inclusion. Optimal elements are the selection device that
recover finite results in general settings, including infinite ones.

**Infinite/finiteness line (GOAL negative control #3):** UC is false for arbitrary infinite
families, but the conjecture is recovered under chain conditions:

```claim
id: colbert-dim-at-most-2
statement: Every nontrivial union-closed family of dimension at most two (every chain of
  sets has length (number of elements minus one) ≤ 2) has an abundant element. Dimension
  at most one is a lemma; both finite and infinite.
hypotheses: F nontrivial union-closed; dim F = sup over chains of (|C|−1) ≤ 2.
holds-here: yes (finite union-closed families of dimension ≤ 2 are a restricted class).
status: proved (Thm in source).
bearing: a *new restricted class settled*: union-closed families whose chain length is
  bounded by 3 (sets in a chain) satisfy UC. Distinct from the lattice classes already in
  ROOT — this is a chain-length condition, not a lattice-theoretic one.
anchor: research/sources/colbert-chain-conditions-2412.full.md
```

```claim
id: colbert-topological-dcc
statement: Let (X, τ) be a topological space satisfying the descending chain condition on
  its open sets, τ ≠ {∅}. Then X has an abundant element of τ (some open set U has more
  ∪-related open sets containing x than not, in the injective-map sense).
hypotheses: (X,τ) topological space, DCC on opens, τ ≠ {∅}.
holds-here: not directly (this run is finite-set UC; recorded as a sourced infinite-side result).
status: proved (Thm in source).
bearing: gives the *formalised* sense in which finiteness can be relaxed if chain conditions
  replace it — the recorded boundary of negative control #3.
anchor: research/sources/colbert-chain-conditions-2412.full.md
```

```claim
id: colbert-infinite-uc-false
statement: UC (every nontrivial union-closed family has an abundant element) is FALSE for
  arbitrary infinite families — the abstract states the conjecture "is known to be false in
  the infinite setting" — motivating the chain-condition recovery.
hypotheses: infinite union-closed families.
holds-here: no (this run is finite; recorded as the reason chain conditions are needed).
status: asserted by source (known; the infinite family {{i,i+1,…}} has no abundant element
  per the Bruhn–Schaudt survey already held).
bearing: pins negative control #3 — finiteness must be used, or a chain condition must
  replace it in exactly this way.
anchor: research/sources/colbert-chain-conditions-2412.full.md, bruhn-schaudt survey
```

## Bearing for this run
Two distinct values: (1) a brand-new *settled restricted class* — union-closed families of
dimension ≤ 2 (chain length ≤ 3) satisfy UC, both finite and infinite — worth adding to
ROOT's "restricted classes already settled" list with its hypotheses; (2) a precise,
sourced statement of when and how the finite/infinite divide can be crossed, which is the
right formalisation of GOAL negative control #3. The optimal-element machinery is a new
structural handle the run had not held.
