# Brown–Shiue, "Sums of Fractional Parts of Integer Multiples of an Irrational" (J. Number Theory 50 (1995) 181–192)

Source: https://www.sfu.ca/~vjungic/tbrown/tom-27.pdf (author's page, SFU); full text at `research/sources/brown-shiue-sums-fractional-parts-multiples-irrational.full.md`. Peer-reviewed: J. Number Theory 50 (1995) 181–192, doi:10.1006/jnth.1995.1012.

## What it establishes

For α irrational, 0 < α < 1, define C_α(n) = Σ_{1≤k≤n} ({kα} − 1/2). The paper gives an **explicit formula for C_α(n) in terms of the simple continued fraction of α**, via the Zeckendorf/Ostrowski-type expansion m = z_t q_{t-1} + ⋯ + z_1 q_0 (q_i the continued-fraction denominators). Concretely (Theorem 1): for m = z_t q_{t-1} + ⋯ + z_1 q_0,

  C_α(m) = Σ_{i=1..t} (−1)^i · (1/2) z_i (1 − |ε_{i-1}| (m_i + m_{i-1} + 1))

with the ε_i, m_i defined from the continued fraction — and it recovers, as special cases, results of Ostrowski (1922), Hardy–Littlewood, and V. T. Sós. It gives the growth bounds (Theorem 2): if the partial quotients a_j of α are bounded by A, then |C_α(m)| oscillates like (const)·log m infinitely often, with explicit constants.

Key lemmas for the mechanics: Lemma 1 (⌊kα⌋ = ⌊k·p_n/q_n⌋ for 1 ≤ k ≤ q_n, i.e. the rational convergent reproduces the floor values up to the denominator), Lemma 2 (exact S_α(q_n) = Σ_{k≤q_n} {kα} at convergent denominators), Lemma 3 (⌊Nα⌋ = b·p_n + ⌊kα⌋ for N = b·q_n + k with 1 ≤ k < q_n) — these are the building blocks that make floor/fractional-part sums of multiples of an irrational evaluable from the continued fraction alone.

## Why it is in the library for PE1006

The adopted second route (`pe1006-ostrowski-sawtooth-closed-form`) evaluates Ψ(k) as a second moment over the k+1 mechanical representatives x_m = frac(−m·a), a = F(n−2)/F(n) → 1/φ². Sums of the digits (floor differences of mechanical words) over the orbit {m·a} reduce to sums like Σ {kα} or Σ floor(kα) — exactly the objects of this paper. This is the primary, citable, *openly downloadable* statement of the explicit continued-fraction closed form (Ostrowski 1922 itself is paywalled; this is its modern, explicit, peer-reviewed treatment). It does NOT by itself give the decimal second moment Ψ — that still needs the geometric (10^j) weight and the squaring — but it is the closed-form engine the Ostrowski route needs, alongside Pinner's non-homogeneous version (with the shift γ) in `research/sources/pinner-sums-fractional-parts-nα+γ-1997.full.md`.

## Caveats

- The formula sums {kα} − 1/2 (first moment of fractional parts), not {kα}² or a 10^j-weighted second moment; extending to the squared/weighted sum is the run's own work, not claimed by this source.
- The Zeckendorf-type expansion used is the continued-fraction denominator system q_i; for the Fibonacci slope (all partial quotients 1) this is the ordinary Fibonacci/Zeckendorf system, so the formula specialises cleanly.
