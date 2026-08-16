# Szechtman — Sums of binomial coefficients mod p, matrix proof

<!-- source: https://arxiv.org/pdf/2405.10352 | converted from PDF -->

Fernando Szechtman, "Sums of binomial coefficients modulo p and groups of exponent p^n", arXiv:2405.10352 (2024).

## What it establishes

A matrix-based proof of congruences for sums of binomial coefficients modulo a
prime `p`, via upper-triangular Jordan blocks `A = I + J` over `F_p`. Uses the
classical foundations and re-proves them cleanly:

- **Lucas' theorem (restated).** `C(n,m) ≡ ∏ C(n_i, m_i) mod p` over the base-`p`
  digits. This is the exact statement this problem's item (2) uses, and its
  power-2 correctness is what makes the submask-XOR reading valid.
- **Kummer's theorem (restated).** The p-adic valuation of `C(n,m)` is the
  number of carries when adding `m` and `n−m` in base `p`.
- **Prop 2.1–2.3.** Congruence identities like `S_{p^n,i} ≡ 0 (mod p)` for
  `0 ≤ i < p^n − 1`, where `S_{p^n,i} = Σ_{t=i}^{p^n−1} C(t,i)`, with group-theoretic
  constructions (exponent `p^n` groups) as the payoff.

```claim
id: szechtman-lucas-submask-corollary
statement: By Lucas' theorem with p=2, C(d,i) mod 2 = 1 if and only if the binary expansion of i is a submask of that of d; consequently C(d,i) ≡ 1 mod 2 iff i & ~d = 0. Szechtman restates Lucas and Kummer with a clean matrix proof and notes p=2 is not a special prime for binomial sums.
hypotheses: p prime (here p=2); standard base-p digit expansions of nonnegative integers m ≤ n.
holds-here: Holds. The submask-XOR reading is exactly this problem's established item (2), and it is what makes each depth-d fold cell an XOR over submasks of d.
status: asserted-by-source (Lucas and Kummer are textbook theorems; the submask corollary follows immediately and is stated unusably)
bearing: Confirms the Lucas foundation of Φ's submask-XOR reading and supplies the power-of-two row/column-sum cancellations Σ C(t,i) ≡ 0 mod p that underlie the dyadic collapse of closed door 4.
anchor: research/summaries/szechtman_sums_binomial_modp.md
```

**Evidence class:** sourced (published arXiv paper with proofs). Restates Lucas
and Kummer verbatim; these are standard, textbook facts and are used here only
as the established foundation, not as new evidence.

**Hypotheses:** require `p` prime; holds with `p = 2`. The submask-XOR reading
of Lucas (`C(d,i) mod 2 = 1` iff `i ⊆ d` as binary submasks) is a direct
corollary of Lucas' theorem and is the reading this problem's item (2) uses.

## Bearing on this problem

It is a clean, authoritative re-derivation of the Lucas foundation that the fold
`Φ` rests on, and it frames the well-known note that "p=2 is not really an
exceptional prime" for binomial sums — a useful corrective to any argument that
treats parity structure as special just because it is mod 2. It also supplies
row/column-sum identities `Σ C(t,i) ≡ 0 mod p` over full power-of-two ranges
which are exactly the sort of cancellation that could force the fold's image
weight (the dyadic-collapse phenomenon of closed door 4 relies on the same type
of power-of-two-period cancellation).
