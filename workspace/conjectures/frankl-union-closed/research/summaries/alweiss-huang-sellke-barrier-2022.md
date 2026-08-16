# Alweiss–Huang–Sellke, "Improved Lower Bound for Frankl's Union-Closed Sets Conjecture" — arXiv:2211.11731 (Nov 2022; published EJC 31(3):P3.35, 2024)

The full precise note is at `research/summaries/alweiss-huang-sellke-barrier-2022.html.md`
with claim `ahs-barrier-3-minus-rt5-over-2`. Full body:
[[alweiss-huang-sellke-barrier-2022.html.full]] (also the non-html `.full.md`,
identical content).

## What it establishes (verified in body)

- **Theorem 1.** For all `φ∈[0,1]`, `min_{μ∈ℳ_φ} F(μ)` (with
  `F(μ)=E[H(xy)]−E[H(x)]` over independent `μ×μ` copies) is attained at a `μ`
  supported on at most two points; if a minimizer is supported on two points,
  one of them is `0`.
- **Theorem 2.** UC holds with constant `1−φ*`, where
  `φ*=min S`, `S={φ∈[0,1]: φH(x²) ≥ xH(x) ∀x∈[φ,1]}`.
- **Claim 3 (computer-checked).** If `x∈[φ,1]` with `φ=(√5−1)/2`, then
  `φH(x²) ≥ xH(x)`, equality iff `x∈{φ,1}` (via interval arithmetic).
- **Claim 4.** `φ* = (√5−1)/2`, so the constant is `1−φ = (3−√5)/2 ≈ 0.38197`.
- **The barrier, exactly.** (3−√5)/2 is "a natural barrier for the method of
  Gilmer" — the maximal constant of the *iid-OR entropy inequality*. It is
  **not** a barrier to the full conjecture: dependent couplings (Sawin → Yu →
  Cambie) escape it.

## Hypotheses and holds-here

`ℱ` finite union-closed, `ℱ≠{∅}`; element densities = exact marginals.
**Holds-here: yes.** The (3−√5)/2 value rests on interval-arithmetic
verification of one one-variable inequality (Claim 3); the reduction is
proved in-paper.

## What it lets the run do

Resolves the run's number-1 question: *what (3−√5)/2 is a barrier for* — the
iid-OR `F(μ)` minimization, i.e. for independent copies only. The equality
cases `x∈{φ,1}` and the two-point-minimizer structure are the extremal objects
against which any improvement must be measured.

```claim
id: ahs-barrier-3-minus-rt5-over-2
statement: min_μ∈ℳ_φ E[H(xy)]−E[H(x)] over independent (μ×μ) copies is minimized
  at φ*=(√5−1)/2, giving constant 1−φ*=(3−√5)/2 for UC; a natural barrier for
  the iid method of Gilmer, not a barrier to the full conjecture (dependent
  couplings escape it).
hypotheses: ℱ finite union-closed, ℱ≠{∅}; iid samples
holds-here: yes
status: proved (Theorem 2/Claim 4 in-paper); Claim 3 numerically verified,
  rigorous via interval arithmetic
bearing: fixes exactly what (3−√5)/2 is a barrier for — the iid-OR entropy
  inequality; equality cases are the extremal test objects for improvement
anchor: research/sources/alweiss-huang-sellke-barrier-2022.html.full.md
follows-from: gilmer-constant-0point01
```
