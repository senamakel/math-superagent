# Stong, "The Average Order of a Permutation" (Electronic J. Combinatorics 5 R41, 1998; DOI 10.37236/1379)

URL: https://doi.org/10.37236/1379

## What it establishes
Let µ_n = (1/n!) Σ_{σ∈S_n} ord(σ), the average order of a uniform permutation. Refining
Erdős–Turán, Schmutz, and Goh–Schmutz, Stong proves an explicit-error refinement:

  log µ_n = C √(n/log n) + O(√n log log n / log n),

with C ≈ 2.99047… The proof bounds µ_n via coefficients of a power series and applies a
Tauberian theorem. Background law (Erdős–Turán): for a *uniform* σ, log ord(σ) is
asymptotically normal with mean (log 2)n/2 and variance (log 3)n/3 — so the *average* order
is dominated by a tiny set of rare, very-high-order permutations.

## Why it matters here
Our period-mean weight in brute2 is n!/ord(π) summed over π. ord(π) typically ≍ exp((log 2)n/2)
(the ET law), while the largest orders reach exp(C√(n/log n)) on average. So the bulk of
errors decay like ~ n!/e^{((log2)/2)n}, and the n!/ord weights are governed by the order
distribution. This is the "order-domain literature map" gap memory.md flagged for the
cycle-type summation behind A_n, B_n: it bounds the ord regime but gives no closed form for
A_n, B_n and does not compute Q(10^6).

## Verdict
Relevant mechanism/route for the n!/ord(π) weights; NOT the closed form for A_n, B_n and
does not compute the rank-sum over {π^i}. Full text: L0 `stong_average_order_permutation.full.md`
(abstract page; PDF at combinatorics.org article v5i1r41/pdf, `.pdf.full.md` is a link stub).
