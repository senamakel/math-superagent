# MathWorld — Totient Function

Source: https://mathworld.wolfram.com/TotientFunction.html — full text at
`research/sources/mathworld-totient-function.full.md`
[[mathworld-totient-function.full]]

## What this source establishes

**Definition.** φ(n) = number of positive integers ≤ n relatively prime to n
(totatives of n); φ(24) = 8 (1, 5, 7, 11, 13, 17, 19, 23).

**Formulas.**
- φ(p^α) = p^α − p^{α−1} = p^{α−1}(p−1); general product form
  φ(n) = n·∏_{p|n}(1 − 1/p)  (eqs. 2–13).
- **Gauss divisor sum: Σ_{d|n} φ(d) = n (eq. 15)** — the identity behind the
  summatory recursion Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋) used as a
  sublinear route to Φ(10⁸).
- **Möbius connection: Σ_{d|n} μ(d)·(n/d) = φ(n) (eq. 16)** — φ = μ ∗ id,
  the per-n identity behind the Möbius-inversion computation of Φ(10⁸).
- Dirichlet series Σ φ(n)/n^s = ζ(s−1)/ζ(s) (eq. 17).
- n − φ(n) is the cototient.
- φ(n) even for n ≥ 3; φ(p) = p − 1; φ(n) ≥ √n except n = 2, 6 (eq. 18);
  liminf φ(n)·(ln ln n)/n = e^{−γ} (eq. 20).

## Hypotheses

n ≥ 1 integer for the identities; the asymptotics for real n. All hold here.

## What it lets this run do

- Primary source for the Gauss divisor-sum identity (eq. 15) and the φ = μ∗id
  identity (eq. 16) — the two identities on which the verification routes to
  Φ(10⁸) rest. Confirmed verbatim in the full text.

## What it does not settle

- No summatory values; no algorithm; no orchard geometry.

## Claims

```claim
id: gauss-divisor-sum-of-totient
statement: Σ_{d|n} φ(d) = n for every positive integer n (Gauss); hence
Σ_{d=1..n} Φ(⌊n/d⌋) = n(n+1)/2, which rearranges to the summatory recursion
Φ(n) = n(n+1)/2 − Σ_{d=2..n} Φ(⌊n/d⌋), evaluated in O(√n) distinct floor
values with memoisation.
hypotheses: n ≥ 1 integer.
holds-here: yes — recursion verified against the sieve values at n = 10, 10^3,
…, 10^8 by patterns.py (A063985 recursion probe).
status: checked — patterns.py verifies the recursion at every probe ≤ 10^8;
identity verbatim in MathWorld TotientFunction eq. (15).
bearing: sublinear route to Φ(10^8); second independent verification path.
anchor: research/summaries/mathworld-totient-function.md
```

```claim
id: euler-phi-mobius-convolution
statement: φ(n) = Σ_{d|n} μ(d)·(n/d) for every positive integer n
(φ = μ ∗ id); summing over n ≤ N gives
Φ(N) = (1/2)Σ_{d≤N} μ(d)⌊N/d⌋(1+⌊N/d⌋).
hypotheses: n ≥ 1 integer.
holds-here: yes — the derived summatory form is implemented in
verify_mobius.py and agrees exactly with the totient sieve at N = 10^8.
status: checked — verify_mobius.py implements this identity and agrees
exactly with the totient sieve at N = 10^8; per-n identity verbatim in
MathWorld TotientFunction eq. (16).
bearing: independent elementary derivation of the second verification route
to Φ(10^8) = 3039635516365908.
anchor: research/summaries/mathworld-totient-function.md
```
