# Summary — Gowers norms for automatic sequences (Byszewski–Konieczny–Müllner)

Source: arXiv:2002.09509, *Gowers norms for automatic sequences*, Jakub Byszewski, Jakub
Konieczny, Clemens Müllner (2020; Discrete Analysis 2021). Full text:
`research/sources/bkm_gowers_norms_automatic_sequences.full.md`.

## What it establishes

Every automatic (finite-automaton-computable) sequence `a : N0 → C` separates as

```
a = a_str + a_uni
```

where `a_uni` is **highly Gowers uniform** — for each order `s ≥ 1`, its
`(s+1)`-th Gowers norm `‖a_uni‖_{U^{s+1}[N]} = O(N^{−c(s)})` with `c(s) > 0` — and
`a_str` is **structured**:

- for a strongly connected, prolongable automaton, `a_str` is rationally almost
  periodic;
- in general `a_str` is built from a periodic part plus forward/backward
  synchronising automatic parts (the fuller form, see Konieczny–Müllner 2023).

**Corollary (the load-bearing statement for this problem):** every automatic
sequence orthogonal to the periodic sequences is Gowers uniform. Small Gowers
norm means the sequence looks random at every finite order of correlation —
it correlates with no bounded-degree polynomial phase.

Applications include: for any `2 ≤ l ≤ 4` and any automatic set `A ⊆ N0`, at
least `(α^l − ε)N` values of the common difference admit `(α^l−ε)N`-many
`l`-term APs inside `A ∩ [N]` when `A` has density `α`; the analogous statement is
**false for `l ≥ 5`**.

## Why it matters for SUPPLY / the reopened question

This is the standard quantitative language for "correlation order `K`". The
reopened GOAL asks whether a fold functional sensitive to correlation order
`1 < K ≲ n/2` can be controlled by an input weaker than switch density. This
paper sharpens what that means: the automatic inputs are exactly the ones with
a strong dichotomy — structured part (which low-order correlation already
detects) plus a *fully* Gowers-uniform part (invisible to *every* finite
correlation order). Door 3 (Thue–Morse, sublinear `ν₂`) is the canonical fully
Gowers-uniform automatic input: it is orthogonal to periodic sequences, hence
Gowers uniform of all orders, hence indistinguishable from random by any
finite-order correlation — yet the fold collapses on it. So **no functional
controlled by any finite correlation order of `h` can separate the primes from
a Gowers-uniform collapse witness** unless it uses something beyond finite-order
correlations of `h`. That is a precise obstruction a candidate order-`K`
functional must face.

```claim
id: bkm-automatic-structured-plus-gowers-uniform
statement: Any automatic sequence a : N0 → C decomposes as a = a_str + a_uni with a_uni highly Gowers uniform ((s+1)-th Gowers norm O(N^{−c(s)}) for every s≥1) and a_str structured; in the strongly-connected-prolongable case a_str is rationally almost periodic. Consequently every automatic sequence orthogonal to the periodic sequences is Gowers uniform.
hypotheses: a is k-automatic (finite automaton, k ≥ 2); 1-bounded valued.
holds-here: The fold Φ is Rule-90 (2-automatic); door-3 input Thue–Morse is automatic and orthogonal to periodic, hence Gowers uniform of all orders. Bearing is negative for any order-K functional controlled by finite-order correlations of an automatic h.
status: sourced (Byszewski–Konieczny–Müllner 2020)
bearing: Names the obstruction any order-K functional must beat: a fully Gowers-uniform collapse witness (e.g. Thue–Morse) is invisible to every finite-order correlation, so the control input must come from outside finite-order correlations of h.
anchor: research/sources/bkm_gowers_norms_automatic_sequences.full.md
```

## Caveats

Infinite-sequence / N → ∞ statements. SUPPLY needs a single fixed prefix `h[0..n−1]`
and a quantitative bound for all large `n`; the Gowers-norm decay here is
asymptotic in `N`. The transfer from asymptotic uniformity to a per-`n` bound on
`wt(Φ_n h)` is not supplied by these sources.
