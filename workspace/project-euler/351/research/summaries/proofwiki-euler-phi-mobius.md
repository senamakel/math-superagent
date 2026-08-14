# ProofWiki — Euler Phi Function in terms of Möbius Function

Source: https://proofwiki.org/wiki/Euler_Phi_Function_in_terms_of_M%C3%B6bius_Function
— full text at `research/sources/proofwiki-euler-phi-mobius.full.md`
[[proofwiki-euler-phi-mobius.full]]

## What this source establishes

**Theorem (φ = μ ∗ id).** For every positive integer n,

    φ(n) = Σ_{d|n} μ(d) · n/d,

equivalently φ = μ ∗ I_{Z>0} in Dirichlet-convolution notation. This is the
per-n identity that, summed over n ≤ N and regrouped by d, yields the
Möbius-inversion formula

    Φ(N) = (1/2) Σ_{d=1..N} μ(d) ⌊N/d⌋ (1 + ⌊N/d⌋)

used by `code/verify_mobius.py`. The page also carries the standard notation
(μ(d) the Möbius function, φ the Euler phi).

## Hypotheses

n ∈ Z>0. Holds here.

## What it lets this run do

- A third, elementary derivation of the Möbius identity that independently
  verifies Φ(10⁸) (the page's theorem is per-n; the summation step is a
  one-line regrouping, checked in code by verify_mobius.py against the sieve).

## What it does not settle

- Nothing about summatory values or complexity; no numerical data.

## Claims

```claim
id: euler-phi-mobius-convolution
statement: φ(n) = Σ_{d|n} μ(d)·(n/d) for every positive integer n
(φ = μ ∗ id); summing over n ≤ N gives Φ(N) = (1/2)Σ_{d≤N} μ(d)⌊N/d⌋(1+⌊N/d⌋).
hypotheses: n ≥ 1 integer.
holds-here: yes — the derived summatory form is implemented in verify_mobius.py
and agrees exactly with the totient sieve at N = 10^8.
status: checked — the derived summatory form is implemented in verify_mobius.py
and agrees exactly with the totient sieve at N = 10^8; per-n theorem sourced
from ProofWiki.
bearing: independent elementary derivation of the second verification route to
Φ(10^8) = 3039635516365908.
anchor: research/summaries/proofwiki-euler-phi-mobius.md
```
