# Summary — Gowers norms for the Thue–Morse and Rudin–Shapiro sequences (Konieczny)

Source: arXiv:1611.09985, *Gowers norms for the Thue–Morse and Rudin–Shapiro
sequences*, Jakub Konieczny (2019, Annales de l'Institut Fourier, DOI
10.5802/aif.3285). Full text:
`research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md`.

## What it establishes

For the Thue–Morse sequence `t(n) = (−1)^{s₂(n)}` and the Rudin–Shapiro
sequence `r(n) = (−1)^{#(11,n)}` (`±1`-valued):

- **Corollary 3.3 (Thue–Morse).** `‖t‖_{U^s[2^L]} = O(2^{−cL})` for a fixed
  `c > 0`, for every order `s`. So on dyadic initial segments the `s`-th Gowers
  norm of Thue–Morse decays **exponentially** in `L`. Thue–Morse is Gowers
  uniform of all orders.
- The analogous bound holds for the Rudin–Shapiro sequence (its 2-kernel
  symmetry plays the role the Thue–Morse kernel plays).
- Application: asymptotic counting of `k`-term arithmetic progressions within
  the `{±1}`-index sets of Thue–Morse / Rudin–Shapiro.

**Conjecture (stated, not proved).** If `a(n)` is 2-automatic with
`E_{n<N} a(qn + r) → 0` for every `q, r` (vanishing dilation averages), then
`‖a‖_{U^s[N]} → 0` for every `s`. This is the individual case of the general
automatic Gowers uniformity that Byszewski–Konieczny–Müllner (2020) later proved.

## Why it matters for SUPPLY / the reopened question

Door 3 in `problem.md` is exactly Thue–Morse: aperiodic with sublinear `ν₂`
(measured `ν₂/n` 0.270 → 0.011 over n=100→4000). This paper quantifies *why*
Thue–Morse defeats the fold: it is Gowers-uniform of all orders, i.e. all its
higher-order correlations decay — it looks random at every finite correlation
order, yet the fold collapses on it.

This is the precise worst case for the reopened question: **an order-`K`
functional (any finite `K`) cannot use correlations of `h` to control the fold,
because Thue–Morse — a full collapse witness — has all finite-order correlations
vanishing.** Any arithmetic input strictly weaker than switch density that forces
`wt(Φ_n h) ≥ c·n` must therefore be something other than "correlations up to
order `K` are large"; the Gowers-uniform collapse witnesses kill that whole
family.

```claim
id: konieczny-thuemorse-gowers-uniform-exponential
statement: The Thue–Morse sequence t(n) = (−1)^{s₂(n)} satisfies ‖t‖_{U^s[2^L]} = O(2^{−cL}) for a fixed c > 0 and every order s (and the Rudin–Shapiro sequence analogously). Thue–Morse is Gowers-uniform of all orders with exponential dyadic decay.
hypotheses: s-th Gowers norm on dyadic initial segment [0, 2^L); t is the ±1 Thue–Morse sequence.
holds-here: Direct match to door 3: Thue–Morse is the aperiodic sublinear-ν₂ fold input. Establishes its collapse accompanies full-order Gowers uniformity (all finite correlations vanish).
status: sourced (Konieczny 2019)
bearing: Any order-K correlation functional (finite K) is blind to Thue–Morse, so correlation-order control of h cannot be the weaker input that forces wt(Φ_n h) ≥ c·n.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md
```

## Caveats

Asymptotic on dyadic segments in the limit `L → ∞`. SUPPLY needs a single fixed
prefix `h[0..n−1]` and a quantitative per-`n` bound; the transfer from asymptotic
uniformity to a per-`n` fold-weight bound is not supplied.
