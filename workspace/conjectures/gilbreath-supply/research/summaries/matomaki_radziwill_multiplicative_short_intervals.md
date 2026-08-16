# Matomäki–Radziwiłł, "Multiplicative functions in short intervals"

Source: Kaisa Matomäki & Maksym Radziwiłł, *Ann. of Math.* (2) **183** (2016)
1015–1056. Source URL: https://arxiv.org/html/1501.04585 (arXiv:1501.04585;
DOI 10.4007/annals.2016.183.3.6). Full text:
`research/sources/matomaki_radziwill_multiplicative_short_intervals.full.md`.

## What it establishes

A general result relating the **short averages** of a multiplicative function
`f : N → [−1,1]` over bounded-length intervals to its well-understood **long
averages**. Theorem 1 (full statement, verified lines 25–40): there are absolute
`C, C′ > 1` such that for `2 ≤ h ≤ X` and `δ > 0`,
`|(1/h)Σ_{x<n≤x+h} f(n) − (1/X)Σ_{X<n≤2X} f(n)| ≤ δ + C′·loglogh/logh`
for all but at most `CX((log h)^{1/3}/(δ²h^{δ/25}) + 1/(δ²(log X)^{1/50}))`
integers `x ∈ [X,2X]`; `C′ = 20000`. (The digest's earlier "O(δ h) for all but
`O_C(X(log h)^{−1/100})`" was the special case `δ = (log h)^{−1/200}`.) Consequences:

- **Möbius:** `Σ_{x<n≤x+h} μ(n) = o(h)` along almost all intervals `[x, x+ψ(x)]`
  with `ψ(x) → ∞` arbitrarily slowly — unconditional, going beyond what was known
  conditionally on the Density or Riemann hypotheses.
- **Smooth numbers:** existence of `x^ε`-smooth numbers in `[x, x + c(ε)√x]`
  unconditionally (previously conditional on RH, Soundararajan).
- **Liouville two-point:** `|Σ_{n≤x} λ(n)λ(n+1)|` is bounded away from the trivial
  `x` by a positive fraction — `≤ (1−δ)x` for some `δ > 0`, a folklore folklore
  conjecture and progress toward Chowla's.

## Why it matters here

This is the **value-domain engine** the (now refuted)
`matomaki-radziwill-index-autocorrelation` approach named. That approach recast
SUPPLY's averaged form as a second moment `Σ_{n≤N} S(n)²` of the endpoint
character sum, expanding via the run telescope into correlations
`Σ_j s_j s_{j+2^g}` of the prime-residue character `s_j = χ(q_j)` at dyadic
**index** separations. **The approach is refuted (research/APPROACHES.md):** the
index-domain object `Σ_j χ(q_j)χ(q_{j+2^g})` is not a multiplicative function in
the prime index `j`, and the `g=0` (index-adjacent) stratum is exactly the
mod-4 switch-density parity barrier. This paper supplies value-domain
cancellations only; the index-domain transfer it would need is exactly what the
refutation says it cannot provide.

```claim
id: mr-short-averages-of-multiplicative-functions-cancel
statement: For a multiplicative f : N → [−1,1], the short sums (1/h)Σ_{x<n≤x+h} f(n) agree with the long average on average over x: for every δ > 0, the short sum in [x,x+h] is within O(δ) of the long mean for all but o(X) of x ≤ X, with h growing slowly. Unconditional conclusions: Σ_{x<n≤x+ψ(x)} μ(n) = o(h) for almost-all x with ψ(x)→∞ arbitrarily slowly; and |(1/x)Σ_{n≤x} λ(n)λ(n+1)| ≤ 1 − δ′ for some δ′ > 0.
hypotheses: f 1-bounded multiplicative; short interval length h → ∞ with X.
holds-here: Partial — the one-point object Σ_j s_j along the prime index is reachable via the Λ-weighting bridge, but the two-point dyadic INDEX autocorrelation Σ_j s_j s_{j+2^g} is not literally a short interval in the VALUE domain. This is the open transfer; the paper supplies the value-domain cancellations the transfer would need, not the transfer itself.
status: sourced (verified verbatim against full text this pass: Thm 1 lines 25-40, Cor 1 lines 49-64, Cor 2 lines 75-100, abstract line 19)
bearing: Supplies the value-domain engine that the refuted `matomaki-radziwill-index-autocorrelation` approach named, and confirms the averaged-short-interval machinery gives vanishing correlations for multiplicative functions — but that approach is refuted (the index-domain object is not multiplicative in the prime index; g=0 is the switch-density parity barrier). Not a proof of SUPPLY; the finite prime-index transfer is the unclosed step that this source cannot provide.
anchor: research/sources/matomaki_radziwill_multiplicative_short_intervals.full.md; summaries/matomaki_radziwill_multiplicative_short_intervals.md
```

The open index-domain transfer (whether the dyadic-shift autocorrelation
`Σ_j s_j s_{j+2^g} = o(N)` holds for `s_j = χ(q_j)`, and in particular the `g=0`
adjacent-index case which is the parity barrier) remains unpriced and is not in
this source — it is a genuine gap, not a settled step.
