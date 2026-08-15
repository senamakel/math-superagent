=== R-weighted-excess-potential REFUTED ===

Claim attacked (excess-energy-ladder, open rung):
  "There exists a summable weight sequence (w_i)_{i>=1} with w_1 > 0, w_i >= 0,
   and defect d_k(i) = max(0, A_k(i) - 2) such that the weighted potential
   P_k = sum_i w_i * d_k(i) is non-increasing under the row operator:
   P_{k+1} <= P_k for every nonnegative-integer absolute-difference array."

REFUTATION (one line, no search):
A single interior spike (0,...,0,v,0,...) with v >= 4 at position p >= 2
doubles under the operator: the child has v at positions p-1 AND p, so its
defect mass (v-2) sits at two positions with total weight w_{p-1} + w_p
versus the parent's w_p.

Smallest instance: A = (0,4,0) -> A' = (4,4).
  P(A)  = 2*w2   (defect of (0,4,0) is (0,2,0))
  P(A') = 2*w1 + 2*w2   (defect of (4,4) is (2,2))
  P(A') - P(A) = 2*w1.
Non-increase for this single array requires 2w1 <= 0, i.e. w1 <= 0,
contradicting the claim's hypothesis w1 > 0.

Genuineness: (0,4,0) is a valid row; it is the child of (4,4,8)
(|4-4|=0, |4-8|=4). The full trajectory (4,4,8) -> (0,4,0) -> (4,4) is real.

General version: for ANY p >= 2 and v >= 4, the spike (0,...,0,v,0,...) at
position p gives P(child) - P(parent) = (v-2)*w_{p-1}, so non-increase forces
w_{p-1} = 0.  Over all p >= 2, every weight w_1..w_{L-1} = 0, contradicting
w_1 > 0.

So NO summable weight sequence with w1 > 0 makes P non-increasing on all rows.
The all-w1-...=0 constant-zero sequence trivially satisfies P' <= P but
violates w1 > 0.  The existential claim is false.

MECHANISM: same as the already-known failures R-excess-total-nonincrease and
R-adjacent-defect-energy-nonincrease — the cancellation/min-branch of |a-b|,
which merges separated mass into a solid block (doubling a spike) instead of
damping it. The operator sharpens, and the weighting correction cannot rescue
a total-mass potential because even a single deep spike forces the left
neighbours' weights to zero.

CONSEQUENCE for the ladder: R-weighted-excess-potential (as stated) is dead.
The ladder's surviving invariant direction is the max-factored / Chamberland
Ducci-template potential only — no weighted total excess. This also closes the
"weighted defect" child of the excess-energy axis.

STATUS: refuted. Counterexample = spike (0,4,0) -> (4,4), requires w1 = 0.
Encodings: code/refute/weighted_excess_potential.p (find_counterexample ->
undecided, finite-model finder cannot handle the continuous arithmetic);
decisive exact algebra in code/refute/weighted_excess_check.py.
