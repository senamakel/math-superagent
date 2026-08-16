# Boppana, "A useful inequality for the binary entropy function" (arXiv:2301.09664)

**Full text:** [[boppana-entropy-inequality-2023.full]]

Gives a clean differential-calculus proof of the binary-entropy inequality used in the entropy line: for the golden ratio φ = (1+√5)/2, h(x²) ≥ φ·x·h(x) on [0,1] (where h is binary entropy), the inequality whose tightness at (3−√5)/2 is the barrier.

```claim
id: boppana-entropy-inequality
statement: h(x²) ≥ φ·x·h(x) for all x∈[0,1], φ = (1+√5)/2, h binary entropy; equality precisely where the (3−√5)/2 barrier saturates.
hypotheses: x ∈ [0,1]
holds-here: yes
status: proved
bearing: The one-variable inequality is the engine of the entire entropy line; its equality case is exactly the extremal distribution behind (3−√5)/2. A run computing the barrier can check any candidate inequality against this.
anchor: research/sources/boppana-entropy-inequality-2023.html.full.md
follows-from: ahs-barrier-3-minus-rt5-over-2
```

**Bearing:** the inequality restates the iid barrier as a clean analytic fact; it is the natural object to verify numerically/symbolically if this run attempts any entropy-method computation.
