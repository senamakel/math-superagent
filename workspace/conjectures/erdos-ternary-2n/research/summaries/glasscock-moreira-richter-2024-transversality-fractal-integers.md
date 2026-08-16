<!-- source: https://arxiv.org/pdf/2007.05480 | Glasscock, Moreira & Richter, "Additive transversality of fractal sets in the reals and the integers" -->

# Glasscock, Moreira & Richter, "Additive and geometric transversality of fractal sets in the integers"

Source: arXiv:2007.05480 (2020 preprint); published JLMS (2024). Full text: `research/sources/glasscock-moreira-richter-2024-transversality-fractal-integers.full.md`.

## Framework

An **integer base-r restricted digit Cantor set** is `{ Σ a_i r^i : a_i ∈ D ⊆ {0,…,r-1} }` with (mass) dimension `dim A = log|D|/log r`. The digit-{0,1} set `S ⊂ Z_3` of this problem restricts (at each finite precision) to exactly such a base-3 restricted-digit Cantor set with D={0,1}, dim `log2/log3`.

## What it establishes (integer analogues of ×2×3 transversality)

Let `r, s` be multiplicatively independent, `A,B ⊆ N0` base-r and base-s restricted digit Cantor sets.

- **Thm A / Corollary:** if `A ⊆ B` then either `A = {0}` or `B = N0`. So restricted-digit Cantor structures in multiplicatively independent bases are mutually incompatible (integer analogue of Furstenberg: ×2- and ×3-invariant set ⊆ [0,1] that is ×2×3-invariant is finite or all of [0,1]).
- **Thm B / Corollary (intersections):** for all ε>0, large N,
  - if `dim A + dim B ≥ 1`: `|A∩[0,N) ∩ B∩[0,N)| / N ≤ N^ε · (|A∩[0,N)|/N)·(|B∩[0,N)|/N)`;
  - if `dim A + dim B < 1`: `|A_N ∩ B_N| ≤ N^ε`.
- **Thm C (sumsets):** `|A_N + B_N| ≫ min(N, |A_N|·|B_N|)`, i.e. near-maximal, up to `N^ε`.
- **Thm D (iterated sumsets / dimension growth to 1):** under a divergence condition on dims, iterated sumsets of ×r-invariant sets grow in dimension toward 1.

## Relevance to this run — and its precise limit

GOAL.md's directed route asks: *what does a dimension / measure statement about the digit-{0,1} set `S` give, and not give, about which integers lie in it?* These theorems are the **geometric-transversality answer**: two digit-restricted Cantor sets in multiplicatively independent bases intersect as if independent, and the sumset is near-maximal. Intuitively the orbit `{2^n}` and `S` should be "transverse."

**But they do not apply to the conjecture.** The critical mismatch is that **`{2^n}` is not a restricted digit Cantor set, nor a ×r-invariant fractal set of integers**, in any base. These theorems bound the intersection of *two digit-restricted Cantor sets* (or ×r-invariant sets). The Erdős conjecture is the intersection of one such Cantor set `S` with a *single thin multiplicative orbit* `{2^n : n ∈ N}` — a set of size ~log N, far below any `N^ε` scale the counting arguments reach. So this paper's bounds are statements about `S`'s measure/dimension and `S`'s typical intersections; they say nothing about whether the specific points `2^0, 2^2, 2^8` (or others) lie in `S`. This is exactly the "density trap" of GOAL.md, now in fractal form.

It **does** establish the ambient fact that plays on the run's side: digit-restricted sets in mutually independent bases are genuinely transverse/unusually thin-intersecting — there is independent structural reason (beyond the naive probabilistic heuristic) to expect `S` and the powers-of-2 to be "generic" against each other. But the run needs a **mechanism that targets the orbit**, which neither this paper nor any dimension statement provides.

## Status

Sourced (JLMS 2024). Theorems quoted with constants made explicit. Directly supplies the vocabulary (mass dimension, transversality, restricted digit Cantor sets) for the run's fractal/dynamics framing, and a precise statement of why dimension bounds cannot close Erdős: the orbit of `2^n` has cardinality `~log N`, invisible to `N^ε`-type intersection bounds.

```claim
id: GMR-TRANSVERSALITY-LIMIT
statement: Restricted-digit Cantor sets A (base r) and B (base s), r,s
  multiplicatively independent, are geometrically transverse: |A_N ∩ B_N| ≤
  N^ε · |A_N||B_N|/N when dim A + dim B >= 1, else |A_N ∩ B_N| ≤ N^ε;
  sumset near-maximal (Theorems A-C).
hypotheses: A,B integer restricted-digit Cantor sets in multiplicatively
  independent bases r,s, with dims as stated.
holds-here: NO for the conjecture directly — {2^n} is not a restricted digit
  Cantor set and has cardinality ~log N, invisible to N^ε intersection bounds.
  The digit-{0,1} set S is itself such a Cantor set (base 3), but its
  intersection with the thin orbit {2^n} is not what these theorems bound.
status: sourced (peer-reviewed, JLMS 2024)
bearing: fractal transversality supports the heuristic that S and powers of 2
  are "generic" against each other, but dimension/measure statements about S
  cannot reach which integers lie in it — this is the density trap in fractal
  form. Supplies vocabulary for the dynamics framing; not a proof route.
anchor: research/summaries/glasscock-moreira-richter-2024-transversality-fractal-integers.md
```
