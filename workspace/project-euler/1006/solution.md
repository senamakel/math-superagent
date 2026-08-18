# Efficient-method status

## Structural reduction

The governing theorem is Sturmian factor complexity: the Fibonacci fixed point has exactly k+1 length-k factors. Mechanical-word coding parameterizes those factors by the k+1 cells of the irrational rotation orbit. For a cell representative x, the corresponding binary word has digits

 d_j(x)=⌊x+(j+1)α⌋−⌊x+jα⌋,  α=1/φ².

Its decimal value telescopes to

 v(x)=⌊x+kα⌋−10^{k−1}⌊x⌋+9 Σ_{j=1}^{k−1}10^{k−1−j}⌊x+jα⌋.

Therefore Ψ(k)=Σ_cells v(x)^2. This is an exact integer/rational floor-sum formulation.

## Why the obvious fast primitive is insufficient

Universal Euclidean/Chtholly recursion evaluates weighted moments for one fixed intercept in logarithmic coefficient complexity. Ψ needs a *joint* second moment over all k+1 intercept cells. Existing local derivations and tests show that replacing this joint observable by one pinned intercept is false already at k=1; a low-dimensional additive block summary also has a k=2 collision. Thus no justified O(log k) full-size evaluator is currently established in this workspace.

Consequently an honest implementation cannot compute Ψ(10^18) yet. The existing `code/solution.py` is intentionally non-answering until this missing aggregation theorem is proved. Reporting a numerical final answer would be unsupported.

## Oracle evidence

The naive oracle is `code/brute.py`, with exponential cost and intended only for small k. It reproduces F_3, Ψ(3)=20302, and Ψ(10)≡10699667 mod 101001001. Mechanical implementations in the existing workspace independently agree with the oracle on their tested small ranges and with large finite anchors, but those are evidence for the reduction, not a proof of the missing joint aggregation.
