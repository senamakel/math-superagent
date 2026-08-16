# Alweiss–Huang–Sellke, "Improved Lower Bound for Frankl's Union-Closed Sets Conjecture" — arXiv:2211.11731 (Nov 2022)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2211.11731 (also arxiv.org/pdf/2211.11731).
> Full text: `research/sources/alweiss-huang-sellke-barrier-2022.html.full.md`.
> Published: Electron. J. Combin. 31(3):P3.35 (2024), doi:10.37236/12232.

The paper that confirms Gilmer's conjecture and pins the `(3−√5)/2` constant
**and** its exact role as a barrier.

## Setting

For a probability measure `μ` on `[0,1]` with expectation `φ`, define
`F(μ) = E_{(x,y)∼μ×μ}H(xy) − E_{x∼μ}H(x)` where `H` is the binary entropy.
`F` is continuous and `ℳ_φ` (measures of expectation `φ`) is compact, so `F`
has a minimizer.

## What it establishes

- **Theorem 1.** For all `φ ∈ [0,1]`, `min_{μ∈ℳ_φ} F(μ)` is attained at a `μ`
  supported on at most two points; if a minimizer is supported on two points,
  one of them is `0`.
- **Theorem 2.** The union-closed conjecture holds with constant `1 − φ*`,
  where `φ* = min S` and `S = {φ ∈ [0,1] : φH(x²) ≥ xH(x) ∀ x ∈ [φ,1]}`.
  So some `i ∈ [n]` is in at least `1−φ*` fraction of sets.
- **Claim 3 (the one-variable inequality, computer-checked).** If
  `x ∈ [φ,1]` (with `φ=(√5−1)/2`), then `φH(x²) ≥ xH(x)`, equality iff
  `x ∈ {φ,1}`. Verified numerically, rigorous via interval arithmetic.
- **Claim 4.** `φ* = φ = (√5−1)/2`. So the constant is `1−φ = (3−√5)/2 ≈
  0.38197`.

## The barrier, exactly

The paper states: *"Assuming Claim 3 … the union-closed conjecture holds with
constant `1−φ = (3−√5)/2`. This is a **natural barrier for the method of
Gilmer** as explained therein."* So the `(3−√5)/2` value is the maximal constant
attainable **by the iid-OR entropy method of Gilmer** — `φ*` is the minimum of
`F` over independent copies. It is **not** a barrier to the full conjecture:
Sawin's dependent-coupling refinement (and Ellis's counterexample) escape it.

## Hypotheses and holds-here

- `ℱ ⊆ 2^[n]` finite, nonempty union-closed; element density = exact marginal.
  **Holds-here: yes.**
- The `(3−√5)/2` value rests on computer verification of Claim 3 (one
  one-variable inequality), made rigorous by interval arithmetic. The reduction
  (Theorem 2) is proved in-paper.

## What it lets the run do

- **The `(3−√5)/2` barrier is now sourced with its precise failing step**: it
  is the iid-OR `F(μ)` minimization, i.e. the barrier for *independent* copies
  only. This is exactly the claim `problem.md` asks to pin down ("what is
  `(3−√5)/2` a barrier *for*").
- The equality case `x ∈ {φ,1}` of Claim 3 and the minimizer structure of
  Theorem 1 are the extremal objects against which any attempted improvement
  must be measured.

```claim
id: ahs-barrier-3-minus-rt5-over-2
statement: min_μ∈ℳ_φ E[H(xy)]−E[H(x)] over independent (μ×μ) copies is
  minimized at φ* = (√5−1)/2, giving the constant 1−φ*=(3−√5)/2 for the
  union-closed conjecture; this is a natural barrier for the iid method of
  Gilmer, not a barrier to the full conjecture (dependent couplings escape it).
hypotheses: ℱ finite union-closed, ℱ≠{∅}; iid samples
holds-here: yes
status: proved (Theorem 2 / Claim 4 in-paper); Claim 3 numerically verified,
  rigorous via interval arithmetic
bearing: fixes exactly what (3−√5)/2 is a barrier for — the iid-OR entropy
  inequality — resolving the run's number-1 question; the equality cases are
  the extremal test objects for improvement
anchor: research/sources/alweiss-huang-sellke-barrier-2022.html.full.md
follows-from: gilmer-constant-0point01
```
