# Visser, "Large Gaps Between Primes" (Warwick survey)

<!-- source: https://warwick.ac.uk/fac/sci/maths/people/staff/visser/large_gaps_between_primes.pdf | full text: research/sources/warwick-visser-large-gaps-between-primes-survey.full.md -->

Warwick University survey (Visser), 1.5 MB PDF, 155 KB Markdown. A self-contained
survey of the maximal-prime-gap problem G(x) = max{p_{n+1} − p_n : p_n ≤ x}.

## What it establishes

- **Lower bound history** (unconditional): G(x) ≥ c·log x·log₂x·log₄x/log₃x
  for various c, culminating in the Ford–Green–Konyagin–Maynard–Tao 2014
  hypergraph-covering generalisation of Pippenger–Spencer, with c → 3.56
  (Pintz 1997, = 2e^γ).
- **Upper bound history** (unconditional): the best is Baker–Harman–Pintz,
  G(x) ≤ x^0.525 ultimately; under RH, Cramér-style √x·log x bounds.
- **Cramér's model and its failures**: the survey discusses Cramér's model
  (log²x gaps), alternative models, the Maier phenomenon, and why the plain
  model is not faithful.
- **Computational results**: how G(x) and the "Y(x)" (Jacobsthal) function are
  computed, up to 10^15 and beyond.
- Full proof of the FGKMT 2014 lower bound via the hypergraph-covering theorem.

## Why it matters for this run

Bridges the gap-side and the models-side that the run's sources (BFT 2023 maier-
pomerance misnomer file, BHP citations) already hold. It is a **secondary survey
that states the BHP α = 0.525 upper bound and the FGKMT lower bound**, providing
an independent secondary witness for the demand side of Granville's ν_2
reduction (Route B) without needing the BHP primary text.

## Status

- **Claim-worthy:** `visser-large-gaps-survey` — confirms G(x) ≤ x^0.525
  (BHP 2001, Theorem 1) and the FGKMT G(x) ≥ c·log x·log₂x·log₄x/log₃x lower
  bound, both unconditional.
- **Falsifier:** a source contradicting the BHP 0.525 exponent or the FGKMT lower
  bound.
- This is a survey, not the BHP primary — cite it as the secondary location of
  the bound, not as the proof of it.

```claim
id: visser-large-gaps-survey
statement: (Visser, Warwick/Cambridge Part III essay, 2020) The maximal prime
  gap G(x) = max{p_{n+1}−p_n : p_n ≤ x} satisfies, unconditionally, the lower
  bound G(x) ≫ log x·log₂x·log₄x/log₃x (Ford–Green–Konyagin–Maynard–Tao 2014,
  quantitative improvement of Rankin 1938; constant c → 2e^γ ≈ 3.56 via Pintz
  1997) and the upper bound G(x) ≤ x^0.525 for large x (Baker–Harman–Pintz 2001,
  the best unconditional upper bound; Cramér's model gives the conjectural
  (log x)² and Granville's corrected model gives ≥ 2e^−γ (log x)², so the
  plain Cramér conjecture is generally considered false).
hypotheses: primes; p_n the n-th prime; unconditional analytic number theory
  (no RH).
holds-here: yes — this is a secondary survey witnessing the BHP 0.525 upper
  bound and the FGKMT lower bound, both of which the run's Route B (Granville
  ν_2 reduction) cites for its demand side.
status: asserted-by-source (survey restating published theorems; the FGKMT bound
  is proven in full in the essay; the BHP upper bound is quoted from BHP 2001,
  whose primary text could not be downloaded on 4 routes).
bearing: independent secondary witness for the demand side α ≈ 0.525 without
  the BHP primary; also records that the plain Cramér (log x)² conjecture is
  doubted (Granville's correction) — relevant to Route C (CHT needs Cramér).
anchor: research/sources/warwick-visser-large-gaps-between-primes-survey.full.md
answers: bhp-primary-unobtainable (BHP 2001 primary text failed on 4 routes;
  its statement is carried by this survey, BFT 2023, and Li 2023)
```
