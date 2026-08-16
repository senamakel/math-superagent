# Correlation-order machinery for the reopened GOAL: Gowers uniformity of automatic sequences

## What these sources establish (digested 2025)

Three papers land the quantitative "correlation order" vocabulary the reopened
question (GOAL priority 2: order-`K` functionals, `1 < K ≲ n/2`) is framed in.
Their bearing is **negative for any functional controlled by finite-order
correlations of `h`** — the collapse witnesses are exactly as Gowers-uniform as
the primes are observed to be.

1. **Byszewski–Konieczny–Müllner 2020 (arXiv:2002.09509, Discrete Analysis 2023).**
   Every automatic sequence `a = a_str + a_uni` with `a_uni` highly Gowers
   uniform (`‖a_uni‖_{U^{s+1}[N]} = O(N^{−c(s)})` for every `s`). Consequence:
   automatic sequences orthogonal to periodic sequences are Gowers uniform.
2. **Konieczny 2019 (arXiv:1611.09985, Ann. Inst. Fourier).**
   Thue–Morse `t(n) = (−1)^{s₂(n)}` and Rudin–Shapiro are Gowers-uniform of all
   orders with exponential dyadic decay `‖t‖_{U^s[2^L]} = O(2^{−cL})`.
3. **Konieczny–Müllner 2023 (arXiv:2309.03180).** Refined dichotomy; classifies
   maximal-arithmetical-subword-complexity automatic sequences; the structured
   part is `F(a_per, a_fs, a_bs)` with `a_per` periodic (period coprime to k).

The fold `Φ` is Rule-90 (2-automatic); door 3 (Thue–Morse, sublinear `ν₂`) is
the canonical fully-Gowers-uniform automatic input: all its finite-order
correlations vanish, yet the fold collapses. So **correlation-order control of
`h` (any finite `K`) cannot be the weaker arithmetic input that forces
`wt(Φ_n h) ≥ c·n`** — a fully-Gowers-uniform collapse witness is invisible to
every finite-order correlation.

## Provenance correction (important)

The file previously named `research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md`
was downloaded under the wrong arXiv identity. It actually contains
**arXiv:1905.03283** (Konieczny, *Algorithmic classification of noncorrelated
binary pattern sequences*), NOT the Gowers-norms paper. The Gowers-norms paper
is **arXiv:1611.09985** and lives at
`research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md`.
Anyone citing the Gowers-norm statement must cite 1611.09985. See
`research/summaries/konieczny_gowers_thuemorse_rudinshapiro_corrigendum.md`.

```claim
id: bkm-automatic-structured-plus-gowers-uniform
statement: Any automatic sequence a : N0 → C decomposes as a = a_str + a_uni with a_uni highly Gowers uniform ((s+1)-th Gowers norm O(N^{−c(s)}) for every s ≥ 1) and a_str structured; in the strongly-connected-prolongable case a_str is rationally almost periodic. Consequently every automatic sequence orthogonal to the periodic sequences is Gowers uniform.
hypotheses: a is k-automatic (finite automaton, k ≥ 2); 1-bounded valued.
holds-here: The fold Φ is Rule-90 (2-automatic); door-3 input Thue–Morse is automatic and orthogonal to periodic, hence Gowers uniform of all orders. Bearing is negative for any order-K functional controlled by finite-order correlations of an automatic h.
status: sourced (Byszewski–Konieczny–Müllner 2020)
bearing: Names the obstruction any order-K functional must beat: a fully Gowers-uniform collapse witness (e.g. Thue–Morse) is invisible to every finite-order correlation, so the control input must come from outside finite-order correlations of h.
anchor: research/sources/bkm_gowers_norms_automatic_sequences.full.md
```

```claim
id: konieczny-thuemorse-gowers-uniform-exponential
statement: The Thue–Morse sequence t(n) = (−1)^{s₂(n)} satisfies ‖t‖_{U^s[2^L]} = O(2^{−cL}) for a fixed c > 0 and every order s (and the Rudin–Shapiro sequence analogously). Thue–Morse is Gowers-uniform of all orders with exponential dyadic decay.
hypotheses: s-th Gowers norm on dyadic initial segment [0, 2^L); t is the ±1 Thue–Morse sequence.
holds-here: Direct match to door 3: Thue–Morse is the aperiodic sublinear-ν₂ fold input. Establishes its collapse accompanies full-order Gowers uniformity (all finite correlations vanish).
status: sourced (Konieczny 2019)
bearing: Any order-K correlation functional (finite K) is blind to Thue–Morse, so correlation-order control of h cannot be the weaker input that forces wt(Φ_n h) ≥ c·n.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro_1611.09985.full.md
```

```claim
id: konieczny-1905.03283-is-noncorrelated-patterns-not-gowers
statement: The physical file research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md contains arXiv:1905.03283 (Algorithmic classification of noncorrelated binary pattern sequences), NOT the Gowers-norms paper. The Gowers-norms paper is arXiv:1611.09985.
hypotheses: file identity / provenance only.
holds-here: Corrections a mis-download. The library's Gowers-norm statement must be sourced to 1611.09985.
status: checked (file header read; this is a provenance correction)
bearing: Prevents citing noncorrelated-pattern-sequence results as Gowers-norm results.
anchor: research/sources/konieczny_gowers_thuemorse_rudinshapiro.full.md
```