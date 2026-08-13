# max-plus-tropical-spectral-dynamics

```approach
idea: Treat the halved Gilbreath operator as a piecewise-linear (tropical) map on sequence space and prove the safe set {0,1} (halved; original {0,2}) is forward-invariant and absorbing via a tropical Lyapunov function / max-plus spectral argument, rather than via congruence or combinatorial potentials.
mechanism: The halved operator is H(u,v) = |u-v| = max(u,v) - min(u,v). A whole row step is the piecewise-linear map T(a)_i = max(a_i, a_{i+1}) - min(a_i, a_{i+1}), built from the tropical operations max/min with integer slopes in {-1,0,1}; each cell A_k(i) is a tropical polynomial of degree 1 (a max/min combination with coefficients +-1) in the initial halved gaps. Piecewise-linear maps of this shape are the object of max-plus (tropical) algebra and tropical dynamical systems: their orbits are governed by the max-plus spectral radius / cycle-time of the associated min-plus matrix, and invariant sets are characterised by tropical eigenvectors and superharmonic (subharmonic) potentials. The program: exhibit a tropical Lyapunov functional Phi(a) = max_i (a_i + c_i) or Phi(a) = max_{i<j} (a_i - a_j + d(j-i)) that is non-increasing along the orbit, Phi(T(a)) <= Phi(a), with the safe set exactly where Phi is minimal (the "tropical zero locus"). Non-increase of such a Phi plus the proved step law would certify A_k(1) in {0,2}: an escape to value >= 2 (halved) would raise Phi, contradicting monotonicity. This is the *spectral/dynamical* axis — it does not name blocks, intruders, or events, and it does not require any congruence.
status: refuted
killed-by: |
  The identity |u−v| = max(u,v) − min(u,v) is exact, and the Gilbreath operator
  is indeed piecewise-linear (tropical). But the approach provides no mechanism
  connecting max-plus spectral theory (max-plus eigenvalues, cycle-time,
  tropical Lyapunov functions Φ(a) = max_i(a_i + c_i)) to the conjecture's
  specific claim A_k(1) ∈ {0,2}. A max-plus functional is dominated by the
  largest entries in the row — the tail/intruder, which in the prime triangle
  reaches values of order the prime gap (~O(log p_k)). The conjecture is about
  the second entry, which is ≤ 2. A functional that tracks the maximum cannot
  constrain the minimum. The tropical language is a description of the
  operator's algebraic structure, not a mechanism for bounding the left edge:
  every tropical Lyapunov function Φ(T(a)) ≤ Φ(a) with the safe set {0,1}
  (halved) as the zero locus would need to be sensitive to the second entry
  while being dominated by values O(b_k) at the right — an order-of-magnitude
  mismatch no max-plus functional can bridge, since max_i(a_i + c_i) is
  monotone in every coordinate. The approach is the same structural mismatch
  that killed the tropical-box-ball attempt (which also correctly identified a
  tropical structure but had no mechanism linking it to the {0,2} second-entry
  claim). The max/min identity itself is a useful algebraic fact, but a
  tropical-dynamical proof of the conjecture would need either a fundamentally
  different class of tropical functional (min-max, order-preserving on a
  different lattice) or a reduction to known tropical integrability that no
  source establishes for the absolute-difference operator.
first-step: Formulate the exact max/min recursion for a cell (already known: A_k(i) = |A_k(i)-A_k(i+1)|, iterate). Then run a numerical search (numpy/scipy LP) for a max-plus functional Phi(a) = max_i (a_i - c*i) or a two-point form Phi(a) = max_{i<j} (a_i - a_j + d(j-i)) that is non-increasing on (i) all depth-1000 prime rows and (ii) a batch of random non-prime 2-then-odds arrays, to test universality of any candidate. Report the candidate coefficients or the refutation of the search over a stated parameter range.
```

## Why this is not on disk

- Not `tropical-box-ball-ultradiscrete-integrable` (refuted): that claimed a BBS/soliton integrability link and died on the missing connection. This uses only the exact |a-b| = max - min identity and the *spectral/Lyapunov* theory of piecewise-linear maps — no integrable structure is claimed.
- Not `tropical-range-diameter-subtree` (refuted): that sought a pairing certificate and collapsed with the run-count lemma. This seeks a tropical (max-plus) potential whose non-increase is checked directly, not a leaf-pairing.
- Not `ducci-potential-max-decrease` (proposed): that hunts a numeric windowed max that decreases. This is the structural theory of the map as a tropical dynamical system — a tropical eigenvector/Lyapunov object with named spectral content (max-plus cycle-time, Baccelli-Cohen-Olsder-Quadrat), not a single hand-picked numeric potential.
- Not `p-adic-valuation-carry-dynamics` (proposed): that tracks 2-adic valuations; this tracks the max/min value structure directly, exact over the reals/integers, no completion.

## What would falsify it

If no max-plus functional of the stated form is non-increasing even on the real prime rows (or the search refutes all candidate forms up to a stated parameter bound), the tropical-Lyapunov route is dead at that order — a recorded negative result. The approach assumes no theorem yet; the first step is a falsification probe, exactly as the run requires.

## Side

General-class side: the map T and any tropical Lyapunov function found for it are operator-level objects, independent of primality; the primes enter only as the orbit whose safety is to be certified.
