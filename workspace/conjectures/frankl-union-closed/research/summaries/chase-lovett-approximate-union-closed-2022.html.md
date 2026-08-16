# Chase–Lovett, "Approximate Union Closed Conjecture" — arXiv:2211.11689 (Nov 2022)

> Re-fetched as a full text body (was abstract-only). Source:
> https://ar5iv.labs.arxiv.org/html/2211.11689 (also arxiv.org/pdf/2211.11689).
> Full text: `research/sources/chase-lovett-approximate-union-closed-2022.html.full.md`.

The paper that proves the `(3−√5)/2` constant **and** shows it is *optimal* for
approximate union-closed families — the cleanest statement of why the iid
entropy method can neither go past that value nor, in one step, reach `1/2`.

## Definitions

- **c-approximate union closed**: `ℱ` is `c`-approx-union-closed if for at
  least a `c`-fraction of the pairs `A,B ∈ ℱ`, `A ∪ B ∈ ℱ`. "Approximate" =
  `1−o(1)`-approximate.
- `ψ = (3−√5)/2 ≈ 0.38197`; `φ = 1−ψ = (√5−1)/2`.

## What it establishes

- **Theorem 1.3.** Let `ℱ` be a `(1−ε)`-approximate union-closed set system,
  `ε < 1/2`. Then some element is contained in a `ψ − δ` fraction of sets,
  where `δ = 2ε(1 + log(1/ε)/log|ℱ|)`.
- **Example 1.4 (optimality).** For `ℱ = ℱ₁ ∪ ℱ₂` with
  `ℱ₁ = {x:|x|=ψn+n^{2/3}}`, `ℱ₂ = {x:|x|≥(1−ψ)n}`: (i) `ℱ` is `1−o(1)`
  approximate union-closed (using `1−ψ = 2ψ−ψ²`); (ii) `|ℱ₂| = o(|ℱ₁|)`;
  (iii) each element is in at most `ψ + o(1)` fraction of sets. So the `ψ`
  threshold is **optimal** for approximate union-closed families.
- **Claim 2.1 (analytic core).** `min_{x∈[0,1]} h(x²)/(x·h(x))` is attained at
  `x = φ`. (Verified by computer simulation; proven rigorously in AHS.)
- The `ψ` sharpness here is what Cambie (in his re-fetched body) analyzes to
  show the dependent-coupling improvement escapes it precisely because the
  dependent union entropy can exceed the iid sharpness construction.

## Hypotheses and holds-here

- Approximate union-closed families, `ε < 1/2`. **Holds-here:** the *exact*
  union-closed case (`ε=0`) gives some element in `≥ ψ−o(1)` fraction. This is
  the `(3−√5)/2` constant.
- The optimality (Example 1.4) is a genuine construction showing the *iid*
  method cannot do better than `ψ` in the approximate setting — the structural
  reason the barrier exists for the independent-copy approach.

## What it lets the run do

- Separates the `(3−√5)/2` bound (reached exactly, optimal in the approximate
  relaxation) from the full conjecture: this is why the *same* `ψ` value that is
  the record for the iid line is simultaneously a hard cap on that line's
  methods and yet escapable by dependent couplings (Sawin → Yu → Cambie).

```claim
id: chase-lovett-psi-optimal-approximate
statement: For (1−ε)-approximate union-closed ℱ (ε<1/2), some element is in at
  least ψ−δ fraction of sets (δ=2ε(1+log(1/ε)/log|ℱ|), ψ=(3−√5)/2), and ψ is
  optimal: a family of layers at sizes ψn+n^{2/3} and ≥(1−ψ)n is 1−o(1) approx
  union-closed with every element in ≤ψ+o(1) fraction.
hypotheses: approximate union-closed, ε<1/2; exact case ε=0 gives the ψ bound
holds-here: yes (ε=0 is the union-closed hypothesis of this problem)
status: proved in-paper (Claim 2.1 verified numerically, rigorous in AHS)
bearing: shows (3−√5)/2 is optimal for the iid/approximate relaxation — the
  exact structural cap on the iid method, thereby explaining why
  (3−√5)/2 is a barrier only for that method
anchor: research/sources/chase-lovett-approximate-union-closed-2022.html.full.md
follows-from: gilmer-constant-0point01
```
