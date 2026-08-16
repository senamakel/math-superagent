# Justin Gilmer, "A Constant Lower Bound for the Union-Closed Sets Conjecture" — arXiv:2211.09055 (Nov 2022)

The breakthrough that started the entropy era. Full body (all versions identical
content): [[gilmer-constant-lower-bound-2022.html.full]]. The full precise note
with the claim block is at `research/summaries/gilmer-constant-lower-bound-2022.html.md`
(claim `gilmer-constant-0point01`); this file is kept as a short pointer.

## What it establishes (verified in body)

- **Theorem 1.** If `A,B` are independent samples from a distribution over
  subsets of `[n]` with `Pr[i∈A] ≤ 0.01` for all `i`, then
  `H(A∪B) ≥ 1.26·H(A)`.
- **Theorem 2.** Any union-closed `ℱ ⊆ 2^[n]`, `ℱ ≠ {∅}`, has an element in at
  least a `0.01` fraction of the sets — the **first constant lower bound**,
  improving Knill's and Wójcik's `Ω(log₂|ℱ|⁻¹)`.
- **Method (core reduction).** Sample `A,B` iid uniform from `ℱ`; since
  `A∪B ∈ ℱ`, `H(A∪B) ≤ log₂|ℱ| = H(A)`. If every marginals `< c`, an entropy
  inequality forces `H(A∪B) > H(A)`, a contradiction; so some element has
  density `≥ c`. The whole content becomes the one-variable inequality relating
  `h(x)` to `h(2x−x²)`.

## Why it matters here

This is the *foundation* of the entropy line and of the `(3−√5)/2` barrier
Gilmer conjectured and AHS/Chase–Lovett/Sawin/Pebody confirmed days later. Not
the record; the historical first constant.

## Hypotheses and holds-here

`ℱ` finite union-closed, `ℱ≠{∅}`. **Holds-here: yes** — exactly `problem.md`'s
object.

```claim
id: gilmer-constant-0point01
statement: Every union-closed family ℱ⊆2^[n], ℱ≠{∅}, has an element in at least
  0.01 fraction of the sets; via H(A∪B) ≥ 1.26·H(A) for independent samples with
  all marginals ≤0.01, contradicting A∪B∈ℱ (whence H(A∪B) ≤ log|ℱ| = H(A)).
hypotheses: ℱ finite union-closed, ℱ≠{∅}
holds-here: yes
status: proved (in-paper, Theorem 1–2)
bearing: foundation of the entropy line and of the (3−√5)/2 barrier that Gilmer
  conjectured and others confirmed; the reduction is the spine of the whole
  barrier/record discussion
anchor: research/sources/gilmer-constant-lower-bound-2022.html.full.md
follows-from: (initiates the entropy line)
```
