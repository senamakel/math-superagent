# Erdős Problems #242 — Erdős–Straus

Source: https://www.erdosproblems.com/242
Full text: `research/sources/erdos-problems-242.full.md`

## What it establishes (sourced, problem-compendium)

- Erdos-Straus: for every `n>2` there exist distinct integers
  `1<=x<y<z` with `4/n=1/x+1/y+1/z`. First appears in Obláth [Ob50]
  (submitted 1948), described as a conjecture of Erdős.
- **Prime reduction** and verification to `n <= 10^18` cited as
  [MiDu25] (note: newer bound than Wikipedia's 10^17).
- Obláth: true if `n+1` divisible by a prime `≡ 3 mod 4` → almost all `n`.
- **Mordell [Mo69]**: true for all `n` except congruent to one of
  {1,121,169,289,361,529} mod 840.
- **Terzi [Te71]**: extended to 198 bad congruences mod 120120.
- **Vaughan [Va70]**: exceptions in [1,x] ≤ `x exp(-c (log x)^{2/3})`.
- Equivalence (BlEl22, Thm 1): the conjecture is equivalent to: for any prime
  `p`, there are `a,c,d>=1` with `p ≡ -a/c mod (4acd-1)` or
  `p ≡ -(4c^2 d+1)/k mod 4cd` for some `k | 4c^2d+1`.
- Bright–Loughran [BrLo20]: no Brauer–Manin obstruction.
- Elsholtz–Tao [ElTa13]: `sum_{p<=N} f(p) = N (log N)^{2+o(1)}`,
  `f(p) <= p^{3/5+o(1)}`.
- Elsholtz–Planitzer [ElPl20]: for almost all n, `f(n) >= (log n)^{log 6+o(1)}`.

## Implication

Confirms the six open classes and the prime reduction. Adds the newer 10^18
verification bound claim ([MiDu25]) and the BlEl22 equivalence as an alternate
(congruence-pair) formulation worth comparing with the Rosati 7-equation form.
