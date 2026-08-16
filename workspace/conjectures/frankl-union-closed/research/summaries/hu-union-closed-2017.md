# Hu, "On the Union-Closed Sets Conjecture" (arXiv:1706.06167)

**Full text:** [[hu-union-closed-2017.full]] · **Source:** https://arxiv.org/abs/1706.06167

## Main theorem / contributions

- Develops tools and bounds on the **separating** union-closed case: many `B` satisfy UC if `|B| ≤ 2|U(B)|`; discusses approaches to go beyond `2` (which Maßberg did), which would imply an ε-UCSC (a constant-fraction bound).
- Defines `φ(n) = min over union-closed A with |A|=n of the maximum element frequency`; UC is equivalent to `φ(n) ≥ n/2` for all `n`. Contrasts with `β(n)`; shows the gap between `φ(n)` and certain bounds can be unbounded with explicit constructions.
- Notes that for minimal counterexamples, `|A| ≥ 4|U(A)| − 1` (consistent with Roberts–Simpson / Lo Faro already in the library).
- Establishes that the conjecture can always be assumed separating without loss (a standard reduction, confirming ROOT's usage).

```claim
id: hu-phi-beta-gap
statement: Defining φ(n) = min over union-closed A with |A|=n of max element frequency, UC is equivalent to φ(n) ≥ n/2 for all n. The gap between φ(n) and certain bounds can be unbounded via explicit constructions.
hypotheses: F union-closed, finite, nonempty.
holds-here: true
status: asserted (construction-based; the unbounded gap is the paper's contribution)
bearing: reframes UC as a numerical min-problem on φ(n); warns that constructions can make the frequency gap unbounded, so a counterexample-density argument must respect this.
anchor: research/sources/hu-union-closed-2017.full.md
```

## Why it matters

- Adjacent to Maßberg; provides the ε-UCSC framework and the separating reduction that justify focusing on separating families.
- Reinforces the verified-range/minimal-counterexample structure already in the library (|A| ≥ 4|U(A)|−1).
