# Wasserstein–Kantorovich row distance

```approach
idea: Each cell is a Kantorovich W₁ distance between degenerate measures;
the triangle is an iterated W₁ pyramid, and A_k(1) ∈ {0,2} is a uniform
bound on the leftmost W₁ value. Attack via Kantorovich–Rubinstein duality,
replacing the (all-refuted) scalar potentials with a transport certificate —
a 1-Lipschitz test function — as the invariant object.

mechanism: |a−b| = W₁(δ_a, δ_b) exactly, and by the Kantorovich–Rubinstein
duality theorem W₁(μ,ν) = sup{ ∫f dμ − ∫f dν : f is 1-Lipschitz }. So each
Gilbreath cell A_k(i) is the cost of the optimal (trivial) coupling of two
point masses, and its dual value is witnessed by a 1-Lipschitz test function
f. Iterating, A_k(1) is a sup over 1-Lipschitz f of a signed linear
combination of the gap ancestors — a *dual certificate*, not a scalar
functional of the row. A failure A_k(1) ≥ 4 means there exists a 1-Lipschitz
f separating two ancestor windows by ≥ 4; this is a propagation constraint
on the gaps that the certificate makes explicit. This is convex duality, but
it is genuinely distinct from the refuted fenchel-duality sign-assignment
route (whose specific identity "A_k(1) = max over a static sign set" was
false): Kantorovich–Rubinstein duality is a theorem, and the certificate lives
in the space of Lipschitz functions, not in {±1}^k. Whether the extremal
certificate f_k can be propagated to f_{k+1} (which would yield a genuine
transport Lyapunov invariant, the thing every scalar potential failed to
provide) is open and speculative; the degenerate-measure identity itself is
exact and checkable.

status: refuted
precedent: The degenerate-measure identity and the duality theorem are
  real and precisely stated (the candidate's invented half is the propagation,
  and THAT half has no precedent in the literature — searches for
  "Wasserstein/Kantorovich iterated absolute differences", "transport pyramid
  Gilbreath", "Lipschitz certificate absolute-difference iterate" returned the
  optimal-transport literature generally — stationary measures of IFS
  (arXiv:1611.00092), numerical-integration error bounds via
  Kantorovich–Rubinstein duality (J. Math. Anal. Appl. 2021,
  https://www.sciencedirect.com/science/article/abs/pii/S0022247X2100264X),
  belief-function/random-set Wasserstein metrics (Internat. J. Approx. Reason.
  2021), unbalanced Kantorovich–Rubinstein distances (Appl. Math. Optim.
  2022) — and NOTHING on iterated absolute-difference (Gilbreath-type)
  pyramids):
  - The identity |a−b| = W₁(δ_a,δ_b): exact. On the line, the unique
    (trivial) coupling of δ_a,δ_b has cost |a−b|, and
    W₁(μ,ν) = sup_{f 1-Lipschitz} [∫f dμ − ∫f dν] (Kantorovich–Rubinstein
    duality, classical; see e.g. the J. Math. Anal. Appl. 2021 bound's
    statement of the duality). The extremal f for δ_a,δ_b is the
    clamped-identity (a 1-Lipschitz f with f(a)−f(b)=|a−b|). So the identity
    is checkable and would PASS the candidate's step (a).
  - Kantorovich–Rubinstein duality is a theorem; the candidate's contrast with
    the refuted fenchel route (whose identity was FALSE) is legitimate — this
    identity is true.
  - NO source applies Kantorovich–Rubinstein duality or W₁ certificates to
    the iterated absolute-difference square. Honest could-not-find on the
    application.
killed-by: The identity is exact but it is a RESTATEMENT, not an invariant,
  and the one thing the approach needs — propagation of the certificate — has
  no theorem and a structural obstruction:
  (1) W₁ between two point masses equals |a−b| with NO contraction or
  compression: it is literally the same number computed by a longer route.
  The only inequality structure W₁ adds is the metric TANGLE INEQUALITY, which
  for two adjacent cells gives |A_{k-1}(1) − A_{k-1}(2)| ≤ A_{k-1}(1) +
  A_{k-1}(2) — the trivial |a−b| ≤ a+b, which cannot establish a bound of 2
  (it grows, not shrinks). No transport inequality closes the {0,2} bound.
  (2) The single-cell KR certificate is the clamped-identity function. To
  propagate it, one must write A_{k+1}(1) = W₁(δ_{A_k(1)}, δ_{A_k(2)}) as a
  sup over 1-Lipschitz f of a signed combination, where A_k(1), A_k(2) are
  THEMSELVES suprema from the previous row — i.e. to bound a sup-of-sup by
  iterating an outer sup. Composing suprema of 1-Lipschitz functions over the
  triangle does not yield a tractable recursive certificate; it is exactly as
  hard as the reachable-sign-set / min-branch problem that killed the fenchel
  route, merely fattened from {±1}^k to the space of 1-Lipschitz functions.
  (3) The run has PROVED the mod-4 ceiling (`mod4-pascal-invariant`): any
  exact-value invariant must work at the integer level (block regeneration) or
  be augmented past mod 4, which fails. The W₁ pyramid, being a pure identity,
  supplies no integer-level information the absolute value does not already
  carry.
  What survives: the degenerate-measure identity |a−b| = W₁(δ_a,δ_b) with KR
  duality is a checkable exact fact (would pass step (a)); it is worth one
  line in the ledger as an exact restatement, but it is not a route to an
  invariant.
first-step: (superseded — see killed-by) Verify |a−b| = W₁(δ_a,δ_b) and KR
  duality on rows A_1..A_3 (oracle) — this holds and is cheap. Then attempt the
  WR dual of A_k(1) explicitly and test propagation; killed-by (2) says the
  propagation is the min-branch problem renamed, so report the obstruction
  rather than spend compute on a monotonicity conjecture.
```
