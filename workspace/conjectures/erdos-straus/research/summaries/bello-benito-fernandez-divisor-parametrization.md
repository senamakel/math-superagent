# Bello-Hernández, Benito & Fernández, "A Divisor Parametrization for the Erdős–Straus Conjecture"

Source: arXiv:2606.10922 (9 Jun 2026), HTML: https://arxiv.org/html/2606.10922v1
Full text: `research/sources/bello-benito-fernandez-divisor-parametrization.full.md`

## What it establishes (sourced, primary)

Studies `1/n` as a sum of three unit fractions whose denominators are all
divisible by a prescribed m — after scaling this is `m/n = 1/...`. For m = 4
(Erdős–Straus): introduces a divisor-based function `fab(n, a, b)` and proves
its admissible parameters recover **exactly** the decompositions of `1/n` with
all three denominators divisible by 4.

- Connection: the decomposition parametrisation relates to a shifted cubic
  surface `P(u,v,w) = uvw − u − v`, with the subfamily
  `P(α+1, 4β+3, 4γ+3)` giving many examples but **containing no perfect
  squares** (relevant to the squares-obstruction).
- Computational evidence: all primes `p ≡ 1 (mod 4)` with `p < 10^14` are
  detected by `fab(p, a, b)` with `1 ≤ a, b ≤ 11` (some composites need larger
  parameters).
- Extends to the 5/n (Sierpiński) setting via `fabfive`, recovering Bradford's
  two-variable reduction; proves translation invariance and a modular sieve.

## Consequence

A completeness statement for the "all denominators divisible by 4" shape —
which is one natural ansatz family. The "no perfect squares" remark for the
subfamily aligns with the Schinzel/quadratic-residue obstruction: families
whose structure forces a perfect square at the critical value are exactly
those that fail on the open classes. The `fab` parametrisation is another
candidate shape for the run's symbolic search (small a,b parameters), with an
independent completeness proof.

```claim
id: bello-fab-completeness
statement: The divisor-based parametrisation fab(n,a,b) recovers exactly the decompositions of 1/n with all three denominators divisible by 4 (the m=4/Erdős–Straus case after scaling); all primes p ≡ 1 mod 4 with p < 10^14 are detected with 1 ≤ a,b ≤ 11.
hypotheses: primes p ≡ 1 (mod 4), p < 10^14 (computational evidence); shape: denominators all divisible by 4.
holds-here: true — an alternative (divisor) parametrisation of the same solution set.
status: sourced (arXiv:2606.10922; computational evidence for the a,b ≤ 11 claim, completeness proved).
bearing: candidate ansatz shape for the symbolic search; completeness of this shape means it does not lose solutions, so a search over small (a,b) is exhaustive for the divisor-counting view.
anchor: research/sources/bello-benito-fernandez-divisor-parametrization.full.md
```