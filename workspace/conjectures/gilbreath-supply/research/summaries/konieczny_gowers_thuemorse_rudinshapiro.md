# Summary — Gowers norms for the Thue–Morse and Rudin–Shapiro sequences (Konieczny)

Source: arXiv:1905.03283, *Gowers norms for the Thue–Morse and Rudin–Shapiro
sequences*, Jakub Konieczny (2019; Annales de l'Institut Fourier 69 (2019)).
Full text: `research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md`.

## What it establishes

For the Thue–Morse sequence `t(n) = (−1)^{s₂(n)}` and the Rudin–Shapiro sequence
`r(n) = (−1)^{#(11,n)}` (both `±1`):

- **Theorem A (Thue–Morse).** For every order `s ≥ 1` there is `c(s) > 0` such that
  the `s`-th Gowers norm on the initial segment satisfies
  `‖t‖_{U^s[N]} = O(N^{−c(s)})`. So Thue–Morse is **Gowers uniform of all orders**.
- **Theorem B (Rudin–Shapiro).** Likewise `‖r‖_{U^s[N]} = O(N^{−c(s)})` — fully
  Gowers uniform of all orders.

Consequences (asymptotic counting of arithmetic progressions in the `{±1}` index
sets), and the machinery is robust enough to extend to wider automatic families.

## Why it matters for SUPPLY / the reopened question

Door 3 in `problem.md` is exactly Thue–Morse: it is aperiodic with sublinear
`ν₂` (measured `ν₂/n` falling `0.270 → 0.011` across `n = 100 → 4000`). This
paper quantifies the *reason* Thue–Morse defeats the fold: it is fully Gowers
uniform, i.e. its higher-order correlations of every order are as small as
those of a random sequence. So the fold collapses on an input that no finite
correlation order distinguishes from random.

This is the precise worst case for the reopened question: **an order-`K`
functional, for any finite `K`, cannot use correlations of `h` to control the
fold, because a fully-Gowers-uniform witness (Thue–Morse) has all its finite
correlations vanishing.** It sets the measure of what an arithmetic input
strictly weaker than switch density would have to be: something *not* of the
form "correlations up to order `K` are large/positive".

```claim
id: konieczny-thuemorse-rudinshapiro-gowers-uniform
statement: The Thue–Morse and Rudin–Shapiro sequences are Gowers-uniform of all orders: for every s ≥ 1 their s-th Gowers norm on [N] is O(N^{−c(s)}) for some c(s) > 0.
hypotheses: t(n) = (−1)^{s₂(n)}, r(n) = (−1)^{#(11,n)}; s-th Gowers norm on initial segment [N].
holds-here: Exact match to door 3: Thue–Morse is the aperiodic sublinear-ν₂ input. Establishes that its collapse on the fold is accompanied by full Gowers uniformity (all finite correlations vanish).
status: sourced (Konieczny 2019)
bearing: Sets the obstruction for any order-K functional: fully-Gowers-uniform inputs have all finite-order correlations vanish, so correlation-order control of h cannot beat them.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md
```

## Caveats

Asymptotic in `N`; SUPPLY needs a quantitative per-`n` bound. The Gowers decay
is polynomial in `N`, not exponential — relevant if one tries to use higher-order
uniformity *quantitatively*.
