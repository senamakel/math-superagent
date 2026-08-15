# Giacomelli 2025 — "Ducci Matrices in p-adic Context" (arXiv:2503.04182)

**Full text:** `research/sources/giacomelli-2025-ducci-matrices-p-adic-context-html.full.md`
**Source:** Piero Giacomelli, arXiv:2503.04182v1 [math.NT]/[math.CO], Mar 2025.

## The operator it studies (— not the absolute-difference map)

Extends Ducci to the p-adic setting via the p-adic-norm operator
`δ_p(x) = |D_p x|_p` on `Q_p^n`, where `D_p` is an n×n matrix over `Q_p`, `|x_i|_p = p^{−ord_p(x_i)}`,
and `|·|_p` is applied componentwise. When `D_p` is the classical difference
matrix this specialises to the p-adic-norm Ducci map of Giacomelli 2021. It is
the p-adic *norm* operator (outputs powers of p), **not** the integer
absolute-difference map `|a−b|` of Gilbreath's conjecture.

## What it proves (spectral termination criteria, all over `Q_p`)

- **Prop 2 / Cor 3:** if all eigenvalues of `D_p` have `|λ_i|_p < 1` (resp. in
  `{p^{−1},...,p^{−n},...}`), the p-adic Ducci sequence terminates at 0.
- **Thm 4/5/6:** if all eigenvalues have `|λ_i|_p = 1`, the sequence does NOT
  converge to zero; if the eigenvalues are roots of unity in `Q_p`, the
  sequence is eventually periodic (period = lcm of the root orders).
- **Example 1:** eigenvalues with `|λ_i|_p > 1` can give unbounded (non-terminating,
  non-periodic) divergence in the p-adic norm.

## Why it does NOT close the run's REQUESTS row

This is p-adic spectral theory of a linear matrix-times-vector map with the
p-adic norm applied componentwise. The run's open question is the exact 2-adic
valuation law of iterated *integer* `|a−b|` (carries through the min branch),
which is nonlinear and not a matrix norm map. It does not appear here. The
`p-adic-valuation-carry-dynamics` direction remains the run's own and unproved;
these two Giacomelli papers (2021, 2025) and Lewis–Tefft 2024 are the closest
external treatments and all use different operators.

```claim
id: giacomelli-2025-padic-ducci-matrix-spectral
statement: For the p-adic-norm Ducci operator δ_p(x)=|D_p x|_p on Q_p^n, termination is governed spectrally: all |λ_i|_p<1 ⟹ terminates; all |λ_i|_p=1 ⟹ does not converge to 0, and roots of unity give eventual periodicity; eigenvalues with |λ_i|_p>1 can give divergence.
hypotheses: δ_p uses the p-adic norm |x|_p=p^{−ord_p(x)} on Q_p^n; D_p an n×n matrix over Q_p.
holds-here: no — the p-adic norm map, not the integer absolute-difference map |a−b| with 2-adic carry. Does not contain the run's carry/valuation law.
status: asserted (abstracted from primary text)
bearing: documents the actual p-adic Ducci literature as spectral/summing/norm theory, none of which is the run's integer-|a−b| carry direction; that direction remains open and unproved.
anchor: research/sources/giacomelli-2025-ducci-matrices-p-adic-context-html.full.md
answers: p-adic-valuation-carry-direction-grounding
```
