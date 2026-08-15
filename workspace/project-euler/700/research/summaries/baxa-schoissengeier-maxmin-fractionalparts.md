<!-- source: https://bibliotekanauki.pl/articles/1391571.pdf | converted from PDF; full text at [[baxa-schoissengeier-maxmin-fractionalparts.full.md]] -->

# Baxa–Schoissengeier: minimum and maximum order of the discrepancy of (nα)

Acta Arith. LXVIII.3 (1994). Studies the **star discrepancy** `D*_N(α)` and
`D_N(α)` of the sequence `{nα}` — deviation from uniform distribution mod 1.

## Statements it makes (verified against full text)

- **Main tool:** with α = [a₀; a₁, a₂, …] an *irrational* with convergents
  `(p_m/q_m)`, `max_{1≤N<q_{m+1}} D_N(α)` is expressed in terms of the partial
  quotients `a_i` and quantities `s_ij = q_min(i,j)(q_max(i,j) α − p_max(i,j))`,
  up to O(1) (Theorem 1.1). Corollary 1.2: `limsup D_N(α)/Σ a_i = 1/4`.
- **Theorem 4.3:** `liminf_{N→∞} D_N(α) = 1 + liminf_{m→∞} q_m|q_m α − p_m|`.
  This is the one place the paper touches best-approximation: `|qα−p|` over
  `0 ≤ q < q_{m+1}` is minimised at the convergent denominator `q_m` (used in
  Lemma 4.2, citing Schoißengeier). **Convergents of α minimise |qα−p|.**

## Why it does / does not help here

This is a paper about **discrepancy orders** (how evenly `{nα}` distributes), not
about record lows. It does **not** bear directly on computing Eulercoins, and it
is **not** needed for the answer. Its single reusable fact — convergents of α
minimise `|qα−p|` (best approximation of the second kind) — is stated more
directly and accessibly in the Cornell notes (Thm 4.14), which we already hold.

It is kept only as field context: it confirms the same underlying structure
(`q_m|q_m α − p_m|` and best-approximation of `(nα)`) that governs where
`(A·n) mod M` is forced to be a small residue at convergent-style indices.

```claim
id: eu700-discrepancy-context
statement: For irrational α with convergents (p_m/q_m), the quantity q_m|q_m α − p_m| is the minimum of q|qα−p| over 0 ≤ q < q_{m+1}; convergents are exactly the best approximations of the second kind of α.
hypotheses: α irrational; (p_m/q_m) its regular convergents.
holds-here: unchecked — α = A/M here is rational, but the discrete orbit {A n mod M} with gcd(A,M)=1 shares the convergent best-approximation structure on an extended scale.
status: sourced and proved (Baxa–Schoissengeier Thm 4.3 + Lemma 4.2; same fact as Cornell Thm 4.14).
bearing: context only. Does not compute the answer.
anchor: research/summaries/baxa-schoissengeier-maxmin-fractionalparts.md
```
