# Eccles, "A Stability Result for the Union-Closed Size Problem" (arXiv:1311.2298, 2013; CP&C 25(3):399-418, 2016)

**Source URL:** https://arxiv.org/html/1311.2298 (full body at
`research/sources/eccles-stability-result-2015-html.full.md`) and
https://ar5iv.labs.arxiv.org/html/1311.2298 (identical body, separate download;
`research/sources/eccles-stability-result-2015-ar5iv.full.md`).

## DEFECT CORRECTED (librarian, this run)

The original `research/sources/eccles-stability-result-2015.full.md` was **the
wrong paper**: it contained arXiv:1210.2044, "On a Chain of Harmonic and
Monogenic Potentials in Euclidean Half-space" (Brackx, De Bie, De Schepper,
cond-mat/Clifford analysis), NOT Eccles' stability result. The summary and
claim `eccles-stability` were anchored to a body that did not say what they
claimed. The correct full body is now in the library as
`eccles-stability-result-2015-html.full.md` (680 lines, complete with Theorem
1.1, Corollary 1.2, Theorem 1.3, Corollary 1.4, and all proofs through Section
6). **Read the correct file; ignore the old wrong-body file.**

## What it is
Tom Eccles, *A stability result for the union-closed size problem*. The
union-closed **size problem**: how small can the total size `‖A‖ = Σ_{A∈𝒜}|A|`
of a union-closed family 𝒜 of m subsets of [n] be? Answered exactly by
Balla–Bollobás–Eccles; this paper adds a **stability** refinement and uses it
to slightly widen the large-family range where the union-closed conjecture
holds.

## What it establishes (from the body, this run)
- **Theorem 1.1.** Let m > 0, n the unique integer with 2^{n-1} < m ≤ 2^n,
  m′ = 2^n − m. Then `f(m) = ‖P(n)‖ − ‖I(m′)‖ − m′`, where I(m′) is the
  initial segment of P(n) in colex order and f(m) is the min total size. The
  extremal family has P(n)\𝒜 = {B∪{n} : B ∈ I(m′)} (a single element n is in
  every set of the complement).
- **Corollary 1.2.** UC holds for all union-closed 𝒜 ⊆ P(n) with |𝒜| ≥ (2/3)2^n
  (recoverable by averaging alone; this is the Balla–Bollobás–Eccles threshold).
- **The stability insight (Section 3, Theorem 3.1).** If 𝒜 is union-closed with
  |𝒜| ≥ 2^{n−1} and ‖𝒜‖ is near-maximal, then P(n)\𝒜 has an element of high
  degree. This is what lets the argument escape the 2/3 barrier that pure
  averaging cannot beat: the extremal examples are highly asymmetric (one
  element in every complement set), so they are far from being
  counterexamples to UC itself.
- **Theorem 1.3.** ∃ c₁ > 0: if 𝒜 is a *counterexample* to UC in P(n) and
  ℬ = P(n)\𝒜 with |ℬ| = m, then `‖I(m)‖ > m(n/2 − 1 + c₁)`.
- **Corollary 1.4.** ∃ c₂ > 0: UC holds for all union-closed 𝒜 with
  |𝒜| ≥ 2^{n(2/3 − c₂)}. Explicitly **c₁ ≥ 1/24 and c₂ ≥ 1/104 (proved in §6)**.
- Methods: down-compressions and simply rooted families.

## Why it matters to this run
- It is the **large-family regime** canon alongside the threshold progression
  Czédli 2^n − 2^{n/2} → Balla–Bollobás–Eccles (2/3)2^n → Eccles (2/3 − c₂)2^n
  → Karpas 2^{n−1}. A counterexample must be *far* from these extremal shapes
  (the stability content).

## Status
Sourced (arXiv:1311.2298, 2013; published CP&C 25(3), 2016, DOI
10.1017/S0963548315000176). Theorems are stated as in the source; not
re-verified computationally here. The explicit constants c₁ ≥ 1/24, c₂ ≥ 1/104
are proved in §6 of the source.

```claim
id: eccles-stability
answers: (corrected) eccles-stability
statement: Stability result for the union-closed size problem: near-extremal
  union-closed families (max total size) cluster around the explicit extremal
  form P(n)\𝒜 = {B∪{n}: B∈I(m′)} (one complement-universal element), far from
  any UC counterexample. Consequences: (Cor 1.2) UC holds for |𝒜| ≥ (2/3)2^n;
  (Thm 1.3) a counterexample 𝒜 with ℬ=P(n)\𝒜, |ℬ|=m satisfies
  ‖I(m)‖ > m(n/2−1+c₁); (Cor 1.4) UC holds for |𝒜| ≥ 2^{n(2/3−c₂)}, with
  c₁≥1/24, c₂≥1/104 explicit.
hypotheses: union-closed 𝒜⊆P(n); |𝒜| above the stated thresholds.
holds-here: yes (large-family settled class; Karpas 2^{n−1} is the best
  threshold in this progression).
status: asserted (theorems in the source; not re-checked here).
bearing: a counterexample must be FAR from these extremal shapes; the stability
  structure feeds the minimal-counterexample programme.
anchor: research/sources/eccles-stability-result-2015-html.full.md
```
