# gantmacher-krein-oscillatory-matrix-sign-regularity

```approach
idea: Prove A_k(1) ∈ {0,2} by bounding the sign changes in the signed
forward-difference sequence Δ_k via the variation-diminishing property of
totally positive (oscillatory) matrices — a classical theorem of
Gantmacher–Krein (1950) and Schoenberg (1930).

mechanism: The signed k-th forward difference Δ_k(i) = Σ_{j=0}^k (−1)^{k−j} ·
binom(k,j) · A_0(i+j) satisfies A_k(i) = |Δ_k(i)| WHEN the signs of
Δ_k(i) and Δ_{k−1}(i) agree in the right way (specifically, when no sign
change forces the min branch). The matrix M_{k,j} = (−1)^{k−j} · binom(k,j)
is a totally positive kernel: it is sign-regular, and Gantmacher–Krein's
"variation-diminishing theorem" says that the number of sign changes in the
transformed sequence Δ_k is at most the number of sign changes in the
original sequence A_0 (restricted to the relevant window).

Now the obstruction to A_k(i) = |Δ_k(i)| is exactly at points where Δ_k
changes sign — because there the min-branch correction in |a−b| = a+b −
2·min(a,b) activates with a nontrivial carry. If the sign-change count of
Δ_k can be bounded independently of k (using that the prime gaps, while
irregular, have a "coherence length" beyond which variations are smoothed),
then the correction −2·min is confined to a bounded zone. In particular, if
the sign-change count at position 1 is zero for all k (i.e., Δ_k(1) never
changes sign), then A_k(1) = |Δ_k(1)| is a pure linear binomial transform of
the gaps, and the conjecture reduces to: does a specific signed binomial sum
of prime gaps stay in {0,2}?

More precisely, the variation-diminishing theorem gives:
    S^−(Δ_k) ≤ S^−(A_0) = bounded,
where S^− counts sign changes (with zeros handled by a standard convention).
This means Δ_k has at most S^−(A_0) sign-change blocks, independent of k.
Within each block the sign is constant, so the absolute-value operation
on that block is just (±) the signed value — no min correction. The min
correction only occurs at block boundaries, and there are at most S^−(A_0)
of them. For position 1, the correction at each boundary is an even integer
(the min of two even numbers), and the total correction at position 1 after
k steps is a sum of at most S^−(A_0) such boundary terms, each damped by
binomial coefficients from the Pascal convolution.

The program: prove that for a sequence starting (2 followed by odds) whose
initial halved-gap row has bounded sign variation, the cumulative boundary
correction at position 1 never pushes A_k(1) past 2. The engine is the
Gantmacher–Krein oscillation theorem, which is a standard tool in
approximation theory, splines, and the moment problem — never applied to
Gilbreath.

Why this is genuinely different: it does not track blocks, intruders,
erosion, or regeneration. It replaces the nonlinear |a−b| with its
linear signed cousin + a boundary correction whose count is controlled by
a classical matrix-property theorem. It attacks the valency of the min
branch directly, using the sign-regularity of the Pascal matrix. No other
approach on disk uses oscillation theory.

Named mathematics: Gantmacher–Krein oscillation theorem, totally positive
matrices, variation-diminishing property, Schoenberg's spline theory,
sign-regular kernels, Chebyshev systems, the Descartes rule of signs
(generalised).

status: proposed

first-step: Compute the signed forward differences Δ_k(i) for the real prime
triangle to depth 200 (using exact sympy integers — no floats). For each k,
count the number of sign changes in the row Δ_k, and verify that S^−(Δ_k)
is non-increasing in k (as the variation-diminishing theorem predicts) and
bounded by S^−(A_0). Specifically, compute the sign-change profile:
(a) total S^−(Δ_k) for each k;
(b) the sign at position 1 for each k;
(c) the positions where Δ_k changes sign (the boundary indices) and track
their movement as k increases.
The oracle rows are in code/out/witnesses.json (depth 600); the first
violation of A_k(1)=|Δ_k(1)| is at (k=3,i=2) (already known), so use the
identity |a−b| = a+b−2·min(a,b) to compute the correction term exactly and
verify it is confined to the sign-change boundaries. If S^−(Δ_k) grows with
k despite the variation-diminishing theorem, the whole approach is dead
at this step.
```