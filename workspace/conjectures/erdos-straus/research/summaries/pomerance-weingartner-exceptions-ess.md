# Pomerance & Weingartner, "Exceptions to the Erdős–Straus–Schinzel conjecture" (2025)

Source: https://arxiv.org/abs/2511.16817 (arXiv:2511.16817v1, 20 Nov 2025),
Carl Pomerance (Dartmouth) & Andreas Weingartner (Southern Utah).
Full text: `research/sources/pomerance-weingartner-exceptions-ess.full.md`

## What it establishes (sourced, primary)

**Background.** ESC is m=4; Sierpiński conjectured m=5; Schinzel's
generalisation: for every m ≥ 4 there is n_m such that m/n is a sum of three
unit fractions for all n ≥ n_m.

**Theorem 1.1 (lower bound on n_m).** If a universal bound n_m exists, it
must be at least

```
n_m ≥ exp(m^{1/3 + o(1)})
```

i.e. there *exist* n this large for which m/n is NOT a sum of three unit
fractions. (Leverages and generalises Elsholtz–Tao.)

**Theorem 1.2 (numerically explicit version).** For every m ≥ 6.52 × 10⁹,
there is a prime p ∈ (m², 2m²) such that m/p is **not** a sum of three unit
fractions. Numerical calculations support the same assertion with the much
smaller bound m ≥ 19.

**Theorem 1.3 / 1.4** generalise a result of Elsholtz–Tao (structure of
exceptional/most numbers) to the fixed-m setting: for each m, most n have
m/n representable as a sum of three unit fractions.

## Relation to the library

- **This is [PoWe25]**, the reference erdosproblems.com #242 cites for the
  m=5/generalisation background (§ of #242: "For more background and results
  on this generalisation see Pomerance and Weingartner [PoWe25]"). Now
  sourced, closing that frontier row.
- **Directly relevant to the m=4 target**: the machinery shows the
  generalised reliability picture — but *does not* settle m=4, and its
  theorems are about m ≥ 6.52×10⁹ exceptions, so m=4 remains open.
  Importantly it illustrates *why* the fixed-m=4 case is the delicate one:
  the exceptions live at scale exp(m^{1/3}) ≥ ~… for m=4 the bound is below
  the trivial range, consistent with the conjecture's empirical truth.
- 4 of its citations were added to FRONTIER.md (per the downloader).

## Consequences for this run

The ESC (m=4) is untouched by these theorems — no claim of a counterexample
for m=4. But the generalised-picture result matters for the run's framing:
a Schinzel-style covering must be sought *without* expecting a universal n_m
mechanism to provide it; the m=4-specific structure (the six open classes and
the 554-family 94.72% cover of n ≡ 1 mod 840) is where the construction must
live.

```claim
id: powe25-ess-exceptions
statement: If n_m exists for the Schinzel generalisation (m/n a sum of 3 unit fractions for all n ≥ n_m), then n_m ≥ exp(m^{1/3+o(1)}); explicitly, for every m ≥ 6.52×10⁹ there is a prime p ∈ (m², 2m²) with m/p not a sum of three unit fractions (numerical evidence for m ≥ 19). The m=4 case is untouched.
hypotheses: m fixed ≥ 4; Schinzel's conjecture setting.
holds-here: true — the theorem constrains the *generalised* problem, not the m=4 target; the six open classes and the 94.72% sub-cover remain the construction ground.
status: sourced (Pomerance–Weingartner 2025, arXiv:2511.16817, Theorem 1.1–1.2).
bearing: closes the [PoWe25] frontier row; marks the generalised-problem boundary; does not bear on 4/n except by contrast.
anchor: research/sources/pomerance-weingartner-exceptions-ess.full.md
```