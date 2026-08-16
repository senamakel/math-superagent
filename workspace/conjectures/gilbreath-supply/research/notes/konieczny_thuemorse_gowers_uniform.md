# Thue–Morse is Gowers-uniform of all orders (Konieczny 2019)

The source is arXiv:1611.09985 (*Gowers norms for the Thue–Morse and
Rudin–Shapiro sequences*, Jakub Konieczny, 2019, Ann. Inst. Fourier, DOI
10.5802/aif.3285), full text at
`research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md`.
This note mirrors the claim into `research/notes/` because the CLAIMS.md
renderer does not reliably ingest claim blocks from `research/summaries/`.

```claim
id: konieczny-thuemorse-gowers-uniform-exponential
statement: The Thue-Morse sequence t(n) = (-1)^s2(n) satisfies ||t||_{U^s[2^L]} = O(2^{-cL}) for a fixed c > 0 and every order s (and the Rudin-Shapiro sequence analogously). Thue-Morse is Gowers-uniform of all orders with exponential dyadic decay.
hypotheses: s-th Gowers norm on dyadic initial segment [0, 2^L); t is the +/-1 Thue-Morse sequence.
holds-here: Direct match to door 3: Thue-Morse is the aperiodic sublinear-nu2 fold input. Establishes its collapse accompanies full-order Gowers uniformity (all finite correlations vanish).
status: sourced (Konieczny 2019)
bearing: Any order-K correlation functional (finite K) is blind to Thue-Morse, so correlation-order control of h cannot be the weaker input that forces wt(Phi_n h) >= c.n.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md
```