# Hu, "On the Union-Closed Sets Conjecture" (arXiv:1706.06167, 2017)

**Source URL:** https://arxiv.org/html/1706.06167
**Full body:** `research/sources/hu-union-closed-2017.full.md` (222 lines)

## What it establishes (verified against this body)

- **Theorem 1** (§2): if a separating union-closed family 𝒜 is a
  *minimal-cardinality* counterexample to UC, then `|𝒜| ≥ 4m − 1`, where
  `m = |U(𝒜)|` is the ground-set size. Proof sketch: a minimal counterexample
  has `|𝒜| = 2n+1` (odd, since removing a basis set from a `2n+2` family drops
  the maximal frequency below `n+1` and gives a smaller counterexample); the
  most-frequency element `a` has `|a|_𝒜 = n`; via the structural sub-collection
  𝒮 (Corollary 1) one gets an `a` with `|a|_𝒜̄_m ≥ (n+1)/2` and `|a|_𝒮 = m−1`,
  so `(n+1)/2 + (m−1) ≤ n`, giving `n ≥ 2m−1` and `|𝒜| = 2n+1 ≥ 4m−1`. ∎
- **Final paragraph of §2 (the 47→51 correction):** Bošnjak–Marković proved a
  minimal counterexample has `m ≥ 12`; Živković–Vučković improved it to `13`.
  So Hu's Theorem 1 gives **a minimal counterexample contains at least 51 sets**
  (`4·13−1 = 51`).
- **Theorem 2** (§3, ε-union-closed): for `c > 2`, if UC holds for all
  separating union-closed 𝒜 with `|𝒜| ≤ c·|U(𝒜)|`, then every union-closed ℬ
  has an element in `≥ (c−2)/(2(c−1))·|U(ℬ)|` sets. (A structural bridge: a
  low-`|F|`-vs-`|U|` result would imply the ε-UC conjecture, not Frankl itself.
  Proving UC for `|F| ≤ 3|U|` would only give frequency `≥ |U|/4`, far from
  `|F|/2`.)

## Hypotheses check

- **Theorem 1** requires 𝒜 *separating* (elements pairwise separable) and
  *minimal-cardinality* counterexample. Both are the standard conventions for
  counterexample bounds (duplicating elements is forbidden because it would
  inflate `m` trivially); holds for this run's minimal-counterexample line.
- **Theorem 2**'s hypothesis is UC on a restricted (low-`|F|/|U|`) class — a
  conditional, not directly an established UC class.

## Bearing for this run

- Upgrades the minimal-counterexample member-set bound to **|F| ≥ 51** (with
  Živković–Vučković `m ≥ 13`), correcting the older `≥ 47` (which used
  Bošnjak–Marković `m ≥ 12`). This also means **UC is verified for all
  families with `|F| ≤ 50`** (since a counterexample needs ≥ 51 sets).
- Corroborates `verified-m-small` and `faro-roberts-simpson-40`; the `4m−1`
  lemma is Roberts–Simpson's / Lo Faro's, which Hu reproves, so this is a
  second source agreeing with the `4m−1` form.

```claim
id: hu-theorem1-4m-minus-1
statement: For a separating union-closed minimal-cardinality counterexample 𝒜
  on an m-element ground set, |𝒜| ≥ 4m−1. With Živković–Vučković's m≥13, a
  minimal counterexample has |𝒜| ≥ 51; hence UC holds for all families with
  |𝒜| ≤ 50.
hypotheses: 𝒜 separating, union-closed, minimal-cardinality counterexample,
  m = |U(𝒜)|.
holds-here: yes (standard separating/minimal-counterexample conventions).
status: proven-in-source (Theorem 1 and its closing estimate).
bearing: minimal-counterexample |F| ≥ 51; the |F|≤50 verified range. Upgrades
  the older |F|≥47.
answers: none (confirms search_claims verified-m-small, already on disk).
anchor: research/sources/hu-union-closed-2017.full.md
```

## What it does not settle
Does not give UC for any family; the ε-UC bridge (Thm 2) is conditional and its
conclusion is a `|U|/something` frequency, not `|F|/2`. Wikilink:
[[hu-union-closed-2017.full]]
