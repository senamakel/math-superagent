# Pivato–Yassawi, "Asymptotic randomization of sofic shifts by linear cellular automata"

Source: https://arxiv.org/pdf/math/0306136 (ETDS, published 2006). Full text at
[[research/sources/pivato_yassawi_sofic_randomization.full.md]].

## What it establishes

**Setting.** `A = (Z/p)^s` for p prime; `Φ = 1 + σ` is the linear cellular automaton
on `A^Z` (Rule 90 when p=2, s=1: each site becomes the XOR/sum of its two neighbours).
`η` is the Haar (uniform Bernoulli) measure. "Φ asymptotically randomizes µ" means
the weak-* iterates `Φ^j µ → η` along `J ⊂ N` of **Cesàro density one**.

**Theorem 7.1 (the load-bearing statement for this run).**
For Φ = 1+σ,   `(Φ asymptotically randomizes µ) ⟺ (µ is Lucas mixing)`.

**Lucas mixing** (Definition, §7): for every nontrivial character χ, there is a
density-one `H ⊂ N` with
`lim_{H∋h→∞} ⟨χ ◦ Φ^{h·⟨⟨χ⟩⟩}, µ⟩ = 0`,
where `⟨⟨χ⟩⟩ = p^r` with `r = ⌈log_p |[χ]|⌉` and `|[χ]| = max K − min K` the
character's support span. By Lucas' theorem `Φ^{⟨⟨χ⟩⟩} = 1 + σ^{⟨⟨χ⟩⟩}`, so the
`h`-th fold reads the character along **binary-submask (Lucas) unfoldings**: each
fold time `h·⟨⟨χ⟩⟩` spreads χ into `L(h)` disjoint translates indexed by the
non-zero ⌊h/ℓ⌋-binomial coefficients mod p.

**Lemma 7.2.** dispersion-mixing ⇒ Lucas mixing, so the "⇐" direction extends the
broader Theorem 3.1 (dispersive LCA randomizes any dispersion-mixing measure), and
the "⇒" direction is **sharp**: for this specific LCA, Lucas mixing is the *weakest*
condition forcing randomization along density-one times.

**Supporting infrastructure.**
- Lemma 4.2 restates **Lucas' Theorem** as the engine: `Φ^N = Σ_ℓ [N/ℓ]_p σ^{ℓ}`.
- Lemma 4.8: if `N = M + p^r H` then `Φ^N = Φ^M ◦ Θ_H` with `Θ = Φ^{(p^r)}`
  — the self-similarity of the fold that makes the density-one decomposition work.
- Theorem 5.2 / Cor 5.3: mixing quasi-Markov measures are dispersion-mixing, so
  randomized by any dispersive LCA.
- §8 constructs zero-entropy measures that are nonetheless Lucas-mixing
  (randomized by 1+σ).

## What it implies for SUPPLY

This is the structural bridge the run's open request `walsh-spectral-subset-b904`
*pointed towards*, and the only source found so far that names and proves the
exact weak-input condition (Lucas mixing). **It does not close the request**: the
theorem is a measure-level ergodic equivalence, and the step from it to a
weight bound on `wt(Φ_n h)` for the single fixed prime string is the finite-prefix
transfer, which is absent (explicit caveat below). Concretely:

- If `h` (the prime gap-parity string) generates a measure µ that is **Lucas
  mixing**, then `Φ^j µ → Haar` at density-one times j, i.e. on a density-one set
  of n the folded image `wt(Φ_n h)` is `≈ n/2`, giving `ν₂(n) ≥ c·n` on a
  density-1 set (GOAL priority 1 and result-tier 3).
- Lucas mixing is a **correlation-decay condition on h along binary-submask
  unfoldings** — a genuinely weaker, structurally-meaningful input than positive
  mod-4 switch density, and it reads only the submask sets that Lucas makes Φ read.
- The equivalence is in the *opposite* hardening direction from the switch-density
  reduction: it says the fold's de-randomization is driven by h's Lucas mixings,
  not by raw pair frequency.

**Caveat — do not overclaim.** The theorem concerns the infinite CA acting on a
measure and converging in the weak-* topology at density-one times. SUPPLY is about
a *single finite* fold `wt(Φ_n h)` for a **fixed deterministic** h (the primes).
Bridging "µ-randomized at density-one times" to "this particular h has
`wt(Φ_n h) ≥ c·n` at density-one n" needs a transfer argument (finite-prefix /
cylinder approximation plus a stability/quantitative condition) that is **not** in
this paper. That transfer is exactly the open step. What the source supplies is the
correct named target for the transfer: prove `h` is Lucas mixing (a prime-gap
correlation statement), then establish the finite-prefix transfer.

Claim block: [[research/notes/pivato_lucas_mixing_equivalence.md]]
