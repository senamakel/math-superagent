# Pivato, "Linear cellular automata, asymptotic randomization, and entropy"

Source: https://arxiv.org/pdf/math/0210241. Full text at
[[research/sources/pivato_lca_entropy_randomization.full.md]].

## What it establishes

**Setting.** A = Z/2, Φ = 1+σ on {0,1}^Z (Rule 90). "Φ asymptotically randomizes μ"
means `Φ^j μ → Haar` along a Cesàro-density-one subset J of N.

**Main result (negative in character — a warning to the run).** For Rule 90,
**nonzero entropy of the initial measure μ is neither necessary nor sufficient for
asymptotic randomization**:

- one constructs a **zero-entropy** measure (Lemma 1) that is nonetheless
  asymptotically randomized by Φ;
- another measure (Lemma 6, built on the Ledrappier subshift) has **positive
  entropy but is NOT randomized** by Φ.

## Why it matters for SUPPLY — a direct warning

This is the formal killing of the "h is complicated enough" family, restated in the
ergodic language of the fold. It shows that entropy (the crudest measure of how
"rich" or "non-periodic" h is) does not control whether `Φ^n` randomizes input:
you can have zero entropy and still randomize, or positive entropy and not randomize.

So any attempt to prove `wt(Φ_n h) ≥ c·n` from a *complexity/entropy* hypothesis on
h is refuted **as a family** — matching the five closed doors and the GOAL rule "no
hypothesis of the form 'h is complicated enough'". The controlling quantity is the
finer **Lucas mixing / harmonic-mixing** structure (see the companion paper's
Theorem 7.1), not entropy.

**Positive use.** The paper develops the building-block lemmas (Lemma 1's
2^n-block self-similarity decomposition via binomial coefficients mod 2) that are
exactly the combinatorial engine of the fold `Φ^n`. These lemmas transfer verbatim
to the run's finite folds.

Claim block: feeds [[research/notes/pivato_lucas_mixing_equivalence.md]] and
reinforces the closed-door list.
