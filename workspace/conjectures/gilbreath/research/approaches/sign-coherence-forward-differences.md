```approach
idea: Forward-difference sign coherence — reduce the absolute-difference operator to a signed linear recurrence by proving the forward differences Δ_k(i) = Σ_{j=0}^k (−1)^{k−j} C(k,j) A_0(i+j) have a consistent sign pattern for all positions (k,i) that influence the left column.

mechanism: For any starting sequence A_0, the absolute-difference triangle satisfies A_k(i) = |Δ_k(i)| where Δ_k(i) is the k-th forward difference with alternating signs. If the signs of Δ_k(i) are KNOWN and CONSISTENT across all steps — specifically, if the sign is (−1)^{k−1}·sign(g_1−2) for all (k,i) in the influence cone of position 1 — then A_k(1) = |Δ_k(1)| = ±Δ_k(1) and Δ_k(1) is a linear combination of the initial gaps. The linear recurrence Δ_{k+1}(1) = Δ_k(2) − Δ_k(1) (the unsigned forward-difference identity) becomes a genuine signed identity, and the entire left column is governed by the binomial transform of the gap sequence. The conjecture A_k(1) ∈ {0,2} would then follow from PARITY ALONE: the binomial coefficients mod 2 (Sierpinski gasket) guarantee that the linear combination is always even, and a separate argument bounds its magnitude to ≤ 2. The sign pattern conjecture is: for a 2-then-odds start with "small enough" gaps, the forward differences Δ_k(i) are positive for even k and negative for odd k (or vice versa) for all (k,i) with i + k ≤ (some bound related to the block). This is a "monotonicity of differences" property: the prime sequence, while not monotone, has differences that alternate in a controlled way when iterated.

status: refuted
first-step: Compute the sign pattern of the signed forward differences Δ_k(i) (without absolute value) for the prime triangle to depth 200. For each cell (k,i) with A_k(i) ∈ {0,2} (inside the block), check whether sign(Δ_k(i)) is determined by k alone (e.g., + for even k, − for odd k). Report the first violation and its context. Use exact integer arithmetic (sympy or Python integers); the forward difference is Σ_{j=0}^k (−1)^{k−j} C(k,j) · A_0(i+j). If signs are consistent throughout the block interior, this reduces the conjecture to a linear problem.

## Refuted at the base step (executed this run; `code/out/check_fwd_diff_identity.captured.txt`)

The load-bearing identity `A_k(i) = |Δ_k(i)|` (iterated absolute difference =
absolute value of the signed forward difference) FAILS on the real prime
triangle at the very first rows, well inside every {0,2} block:

- **first violation anywhere: k=3, i=2** — signed Δ_3(2) = 4 but the actual
  `A_3(2) = 0` (row A_3 of problem.md is `1,2,0,0,0,...`). The failure is
  *inside* the leading {0,2} block, which is fatal for the approach: the
  positions claimed to be governed by the linear recurrence include the very
  cells where it breaks.
- **first violation at position 1: k=4** — `Δ_4(1) = D_4(1) = −6` (|Δ| = 6)
  but `A_4(1) = 2`; the identity then fails at position 1 for 17 of the 20
  rows checked.
- **mechanism (one line):** `|u − v| = ||u| − |v||` holds iff `u·v ≥ 0`. The
  signed forward-difference triangle D keeps the sign that the absolute-value
  row build erases; the first adjacent opposite-sign pair feeding a violation
  is `(D_3(2), D_3(3)) = (2, −2)`. Signed rows oscillate
  `[..., 4, −4, 4, −4, ...]` around the same positions where the actual rows
  are constant `0` — the convex/alternating behaviour the signed recurrence
  insists on is exactly what the absolute values destroy.

Oracle: rows A_1..A_5 reproduce problem.md exactly (the output's first line).
Generator: sieve 400000, depth 20, width 40, exact integers — O(D·W) time,
O(W) space, no search. The proposed linear reduction of Gilbreath's
conjecture to a signed binomial-transform recurrence cannot start: the
identity `A_k(i) = |Δ_k(i)|` is false from row 3 on the actual object, not by
a large adversarial construction but at the second difference of the primes
themselves. Do not re-propose; any linearization must survive the k=3, i=2
cell.

speculative: The sign pattern might only hold inside the {0,2} block, and might fail at the intruder. That is expected and acceptable — the claim is about the entries that influence position 1, which are all inside the block. The linear reduction would be the first time the GC has been connected to a purely linear (non-absolute-value) recurrence, opening the door to generating functions, binomial transforms, and spectral methods.
```