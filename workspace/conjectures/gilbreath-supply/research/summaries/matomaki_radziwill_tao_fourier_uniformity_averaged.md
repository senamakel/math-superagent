# Matomäki–Radziwiłł–Tao, "Fourier uniformity ... in short intervals on average"

Source: Kaisa Matomäki, Maksym Radziwiłł, Terence Tao, *Invent. Math.* **220**
(2020) 1–58. Source URL: https://arxiv.org/pdf/1812.01224 (arXiv:1812.01224).
Full text: `research/sources/matomaki_radziwill_tao_fourier_uniformity_averaged.full.md`.

## What it establishes

**Local Fourier uniformity on average** for the Liouville function: as `X → ∞`,

```
∫_{X}^{2X} sup_α | Σ_{x<n≤x+H} λ(n) e(−αn) | dx  =  o(XH)
```

for all `H ≥ X^θ`, any fixed `θ > 0` arbitrarily small. Previously this was only
known for `θ > 5/8` (Zhan); this is the first nontrivial case below that.
Main theorem (Thm 1.4, verified lines 304–314): the contrapositive — if
`∫ sup_α |Σ_{x<n≤x+H} f(n)e(−αn)| dx ≥ ηXH` for a 1-bounded multiplicative
`f : N → C`, then `f` is pretentious: `D(f; X²/H^{2−ρ}; Q) ≪ 1` for some
`Q ≪ 1`. Corollary 1.5: correlations `f(n)a(n+h)b(n+2h)` with
`sieve-majorant` sequences `a,b` (i.e. `a(n), b(n) ≪ 1 + Λ(n)`) average to
`o(XH)`. Consequence (Cor 1.3): cancellations in
`Σ_{|h|≤H}(1−|h|/H)Σ_{n≤X} λ(n)Λ(n+h)Λ(n+2h) = o(HX)` over `h < X^θ`,
`n < X`. This is an **averaged form of Chowla's conjecture** at short intervals —
the two-point/triple correlation of a multiplicative function averages to `o(·)`
over both `n` and short shifts `h`.

## Why it matters here

This is the **quantified value-domain form** of the engine the (now refuted)
`matomaki-radziwill-index-autocorrelation` approach named for its **open step**:
the averaged L²/autocorrelation form of the prime-character string. The route
wanted `Σ_{n≤N} S(n)² = o(N²)` (which by Chebyshev gives `ν₂/n → 1/2` on a
density-1 set), expanding via the run telescope into dyadic-shift autocorrelations
`Σ_j s_j s_{j+2^g}` of `s_j = χ(q_j)`. **The approach is refuted
(research/APPROACHES.md):** the index-domain correlation is not multiplicative in
the prime index `j`, and the `g=0` (adjacent-index) stratum is exactly the
mod-4 switch-density parity barrier. The MRTF result is a value-domain statement —
the averaged correlation shape the index-domain step would need — and it does not
and cannot supply that step.

```claim
id: mrt-fourier-uniformity-averaged-correlations-vanish
statement: For λ (and any non-pretentious 1-bounded multiplicative f), the average over x∈[X,2X] of sup_α |Σ_{x<n≤x+H} f(n)e(−αn)| is o(XH) for every H ≥ X^θ with θ>0 fixed arbitrarily small; equivalently an averaged form of Chowla's conjecture holds at short intervals — two- and higher-point correlations of f over shifts h < X^θ vanish on average. Corollary: cancellation in Σ_{n≤X} λ(n)Λ(n+h)Λ(n+2h) for 1 ≤ h < X^θ.
hypotheses: f non-pretentious 1-bounded multiplicative (λ, μ included); H ≥ X^θ, θ>0 arbitrarily small; average over starting points x.
holds-here: Partial — states the averaged-correlation-shape result in the VALUE domain that the index-domain open step of `matomaki-radziwill-index-autocorrelation` would invoke. The prime-INDEX dyadic autocorrelation Σ_j s_j s_{j+2^g} for s_j=χ(q_j) is not literally covered (the shifts here are value-shifts at fixed index distance 1); the Λ-weighted passage is the bridge that is still open, as is the g=0 adjacent-index (parity-barrier) case.
status: sourced (verified verbatim against full text this pass: Thm 1.2 lines 165-178, Cor 1.3 lines 215-225, Thm 1.4 lines 304-314)
bearing: Supplies the value-domain engine that the refuted `matomaki-radziwill-index-autocorrelation` approach named, confirming averaged-short-interval machinery gives vanishing averaged correlations for multiplicative functions. The approach is refuted (index-domain object not multiplicative in the prime index; g=0 is the switch-density parity barrier). Not a proof of SUPPLY; the finite prime-index transfer is the unclosed step this source cannot provide.
anchor: research/sources/matomaki_radziwill_tao_fourier_uniformity_averaged.full.md; summaries/matomaki_radziwill_tao_fourier_uniformity_averaged.md
```

**Honest limit:** like MR(sI), this is a value-domain statement for multiplicative
functions. SUPPLY's object is the character `χ(q_j)` at **prime indices**, and the
transfer to the index domain (and the `g=0` case, which is the parity barrier)
remains unpriced and is not in this source.
