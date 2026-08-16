# Justin Gilmer, "A Constant Lower Bound for the Union-Closed Sets Conjecture" — arXiv:2211.09055 (Nov 2022)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2211.09055 (also arxiv.org/pdf/2211.09055).
> Full text: `research/sources/gilmer-constant-lower-bound-2022.html.full.md`.

The breakthrough paper that started the entropy era.

## What it establishes

- **Theorem 1 (constant lower bound).** For any union-closed family
  `ℱ ⊆ 2^[n]`, `ℱ ≠ {∅}`, there is an element `i ∈ [n]` contained in at least a
  `0.01` fraction of the sets in `ℱ`. This is the **first known constant lower
  bound**, improving on the `Ω(log₂|ℱ|⁻¹)` bounds of Knill and Wójcik.
- **Method (the core idea).** Given a union-closed `ℱ`, take `A, B` independent
  uniformly random samples from `ℱ`. Then `A ∪ B ∈ ℱ`, so
  `H(A ∪ B) ≤ log₂|ℱ| = H(A) = H(B)`. If every element of `A` has marginals
  `< c`, an entropy inequality forces `H(A ∪ B) > H(A)`, a contradiction. Hence
  some element has marginal density `≥ c`. The entire content becomes a
  one-variable inequality relating binary entropy `h(x)` to `h(2x − x²)`.
- **Information-theoretic strengthening (Gilmer's Lemma 1).** If `A,B` are
  independent subsets of `[n]` (arbitrary distribution, not necessarily a
  union-closed family) with `Pr[i ∈ A] < 0.01` for all `i` and `H(A) > 0`, then
  `H(A ∪ B) > H(A)`.

## Relation to the rest of the field

- Gilmer conjectured his technique could be pushed to `(3−√5)/2 ≈ 0.3819`. That
  was confirmed within days by Alweiss–Huang–Sellke, Chase–Lovett, Sawin, and
  Pebody (all downloaded as bodies).
- Gilmer also posed Conjecture 1 (an attempt to reach `1/2` via a KL-divergence
  refinement). That conjecture was **refuted** by Ellis (arXiv:2211.12401, in
  library) and by Sawin (arXiv:2211.11504, in library).

## Hypotheses and holds-here

- `ℱ` finite union-closed, `ℱ ≠ {∅}`. **Holds-here: yes** — this is exactly the
  object in `problem.md`.
- The `0.01` value is the historical first constant; later papers (Sawin,
  Yu, Cambie) push it well beyond. This paper is the foundation of the entropy
  line, not the record.

## What it lets the run do

Colocates the exact statement of the entropy reduction (`H(A∪B) ≤ H(A)` with
independent uniform samples) that the whole barrier / record discussion rests
on. It fixes that the entropy argument is *sourced here*, and that the
`(3−√5)/2` value is a later, separate result.

```claim
id: gilmer-constant-0point01
statement: Every union-closed family ℱ⊆2^[n], ℱ≠{∅}, has an element in at
  least 0.01 fraction of the sets; proven via the entropy inequality that if
  A,B independent uniform in ℱ have all marginals <0.01 and H(A)>0, then
  H(A∪B)>H(A), contradicting A∪B∈ℱ (H(A∪B)≤log|ℱ|=H(A)).
hypotheses: ℱ finite union-closed, ℱ≠{∅}
holds-here: yes
status: proved (in-paper)
bearing: foundation of the entropy line and of the (3−√5)/2 barrier that
  Gilmer conjectured and others confirmed
anchor: research/sources/gilmer-constant-lower-bound-2022.html.full.md
```
