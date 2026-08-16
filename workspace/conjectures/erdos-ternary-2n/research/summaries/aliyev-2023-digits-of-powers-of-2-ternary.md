# Aliyev, "Digits of powers of 2 in ternary numeral system"

Source: Notes on Number Theory and Discrete Mathematics 29(3) (2023) 474–485, DOI 10.7546/nntdm.2023.29.3.474-485. Open access (CC BY 4.0). Full text: `research/sources/aliyev-2023-digits-of-powers-of-2-ternary.full.md`.

## What it establishes

A doubling algorithm in ternary and a structural study of the ternary digits of powers of 2.

**Lemma 3.1 / 3.2.** `3^k | (2^(3^(k-1)) + 1)` and `3^(k+1) ∤ (2^(3^(k-1))+1)`; and `3^k | (2^(2·3^(k-1)) − 1)`, `3^(k+1) ∤ (2^(2·3^(k-1))−1)`. This restates the 3-adic valuation/order facts: `ord_{3^(n+1)}(2) = 2·3^n = φ(3^(n+1))`, i.e. 2 is a primitive root of the full unit group `(Z/3^(n+1)Z)^×` (which is cyclic of order `2·3^n`). Lemma 3.2 gives `2^(2·3^(k-1)) ≡ 1 + 3^k (mod 3^k)` style lift behavior (LTE with exponent exactly 1).

**Lemma 3.3 / 4.1.** Except those ending in 0 (resp. starting in 0), any finite sequence of ternary digits occurs infinitely often at the end (resp. beginning) of ternary representations of powers of 2 — consequences of uniform distribution of `{n·log_3 2}` mod 1.

**Theorem 5.1.** In the vertical array of `2^n` ternary expansions, triangular blocks of only 0s or only 2s occur with unbounded size.

## Relevance

- Aliyev's Lemma 3.2 is exactly the LTE step the run's `|A_k| = 2^(k-1)` computation relies on (gives the "residue 1 + 3^(k-1)" lift). Good as an independent statement of the needed mechanism.
- Lemma 3.3/4.1: any finite digit sequence (not ending/starting in 0) appears infinitely often among trailing/leading digits of `2^n`. This means, in particular, infinitely many `2^n` start with any given non-zero-leading block — illustrating why leading-digit arguments alone can never prove absence of digit 2.

## Status

Sourced, peer-reviewed journal (NNTDM, open access). The lemmas are stated and proved in the paper; use as sourced statements of the LTE/order facts.

```claim
id: ALIYEV-LTE-ORDER-AND-BLOCK-OCCURRENCE
statement: 3^k | 2^(3^(k-1))+1 and 3^(k+1) ∤ it; 3^k | 2^(2·3^(k-1))−1 and 3^(k+1) ∤ it (so ord_{3^{n+1}}(2) = 2·3^n = φ(3^{n+1}), 2 primitive root). Except sequences ending in 0, any finite ternary digit block occurs infinitely often at the end of (2^n)_3; except sequences starting in 0, infinitely often at the beginning. Triangular blocks of only-0s or only-2s occur with unbounded size.
hypotheses: n,k positive integers; digit blocks not ending/starting in 0.
holds-here: yes
status: asserted
bearing: independently restates the LTE/order mechanism behind |A_k|=2^(k-1) (SIEVE-EXACT-COUNT); the leading-digit occurrence lemma shows leading/trailing block arguments alone can never prove absence of digit 2 (infinitely many 2^n start with any given non-0-leading block).
anchor: research/summaries/aliyev-2023-digits-of-powers-of-2-ternary.md
```
