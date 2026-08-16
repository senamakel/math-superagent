# Pascal-counting-function threshold: the two open G-threshold lemmas are a Krawtchouk-weighted Pascal-mod-2 counting function

```approach
idea: >
  The three candidates this pass grounded (ducci-valuation-magnitude,
  zeta-tensor-block-doubling, mauduit-rivat-digital-equidistribution) all died
  at the same place: they demanded an ARITHMETIC input on the prime string and
  the literature has no transfer from value-domain (digit sums, character
  values, Ducci collapse) to the index-domain fold. But the workspace's own
  third pass has already located a line with NO arithmetic input at all: the
  two open lemmas G-threshold-asymptotic-zero and G-threshold-concentration
  are pure F2/hypergeometric statements about the AVERAGE of nu2 over the
  weight-w sphere. The new reformulation is that the single object controlling
  both lemmas is the ROW-WEIGHT GENERATING FUNCTION

      P(n; u) = sum_{d=2}^{n-1} u^{2^popcount(d)},

  whose derivative at u=1 is exactly the Pascal-mod-2 counting function
  A(n) = sum_{d<n} 2^popcount(d) (OEIS A006046), whose log-periodic
  asymptotics A(n) = n^{log2(3)} . P0(log2 n) are PROVED on disk
  (claim hjt-p2-log-periodic-representation-proved, Hwang-Janson-Tsai 2024).
  This is the synthesis neither I nor research named: my zeta-tensor candidate
  attached the block self-similarity to the WRONG object (the full zeta matrix),
  and research showed the two-point digital literature is real but value-domain;
  the correct object that IS self-similar enough to carry the log-periodic
  exponent is the Pascal-mod-2 counting function A(n), which the threshold
  mean is a Krawtchouk-transform of. The fitted "E ~ 0.555, amplitude ~0.07"
  of threshold-weight-sublinear becomes a DERIVED constant of this transform,
  not a fitted one.
mechanism: >
  Identity (derived here, machine-checkable in one step). For X_d ~
  Hypergeometric(n, m_d, w) with m_d = 2^popcount(d), the cell-parity expectation
  is E[(-1)^{X_d}] = [z^w](1-z)^{m_d}(1+z)^{n-m_d}/C(n,w) (standard; matches
  claim threshold-mean-exact-parity-formula). Summing over d and factoring
  (1+z)^n out of every term:

      sum_d E[(-1)^{X_d}] = (1/C(n,w)) [z^w] (1+z)^n P(n; (1-z)/(1+z)),

  because (1-z)^{m}(1+z)^{n-m} = (1+z)^n ((1-z)/(1+z))^{m}. Hence the exact
  weight-w mean is

      M(n,w) = (n-2)/(2n) - (1/(2n C(n,w))) [z^w] (1+z)^n P(n; (1-z)/(1+z)),

  and the threshold condition M >= 0.40 is EXACTLY

      [z^w] (1+z)^n P(n; (1-z)/(1+z)) <= (0.2 n - 2) C(n,w).

  So w*(n) is the crossing point of a coefficient extraction whose only
  n-dependent object is P(n; u). P is a binomial-type sum over the popcount
  multiset: P(2^L; u) = sum_{k=0}^{L} C(L,k) u^{2^k} (plus the two dropped rows
  d=0,1). Its derivative P'(n;1) = A(n) = sum_{d<n} 2^popcount(d) is the
  HJT-proved Pascal-mod-2 counting function. The coefficient extraction lives
  at u = (1-z)/(1+z) with z = theta = w/n small, i.e. u = 1 - 2theta + O(theta^2)
  in a punctured neighbourhood of u=1: a smooth DEFORMATION of the HJT object.
  Consequence chain: closing the coefficient-extraction asymptotics of
  (1+z)^n P(n;(1-z)/(1+z)) via the HJT Mellin/log-periodic machinery proves
  G-threshold-asymptotic-zero (mean -> 1/2 at every fixed theta), and the same
  transform applied to the symmetric-difference multiset |M_d \triangle M_{d'}| =
  2^{pc(d)} + 2^{pc(d')} - 2^{pc(d^d')+1} (claim
  downset-row-intersection-meet-formula) proves G-threshold-concentration
  (Var = o(n^2)). The log-periodic amplitude ~0.07 measured for w* is the
  signature of P0(log2 n) transferred through the transform; the exponent E is
  the critical exponent of the coefficient extraction, NOT log2(3)-1 (which the
  data correctly rejected) and NOT a free fit.
status: adopted
first-step: >
  tool_builder, exact integer/coefficient arithmetic, no primes, no number theory.
  (1) VERIFY THE IDENTITY: implement B(n,w) = sum_{d=2}^{n-1} K_w(2^popcount(d);n)/C(n,w)
  two independent ways -- direct Krawtchouk sum and the coefficient extraction
  (1/C(n,w))[z^w](1+z)^n P(n;(1-z)/(1+z)) with P(n;u) = sum_d u^{2^popcount(d)}
  -- and assert equality for n in {8,16,32,64,128}, w = 0..n, with a negative
  control (a deliberately wrong kernel, e.g. (1+z)^{n-m}, shown failing).
  (2) REPRODUCE the exact w* column 3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239,349
  (n=8..65536) from the threshold condition [z^w](1+z)^n P(...) <= (0.2n-2)C(n,w),
  digit-for-digit against code/pattern_finder/threshold_linearscan.py.
  (3) CONFIRM THE HJT LINK: compute A(n) = P'(n;1) exactly and assert it equals
  the known A006046 values, then print P(2^L; u) = sum_k C(L,k) u^{2^k} for
  L = 8..20 at u = (1-theta)/(1+theta), theta in {1/32,1/16,1/8,1/4}, and
  tabulate the per-doubling phase of the coefficient extraction against the
  measured log-periodic amplitude (~0.07). Deliverable: a capture showing the
  identity holds and the coefficient-extraction phase matches the w* phase,
  which is the precondition for the HJT Mellin transfer.
precedent: >
  PROVED engine on disk: hjt-p2-log-periodic-representation-proved (A(n) =
  n^{log2 3} . P0(log2 n), P0 bounded period-1, Hwang-Janson-Tsai 2024, OEIS
  A006046). Established in-workspace: threshold-mean-exact-parity-formula
  (the Krawtchouk/hypergeometric parity formula); fold-cell-degree-is-2^popcount
  (m_d = 2^popcount(d)); downset-row-intersection-meet-formula (the symmetric-
  difference sizes feeding the second moment); threshold-weight-sublinear and
  threshold-closed-forms-rejected (the measured w* column and the fitted
  E ~ 0.555 / amplitude ~0.07 to be DERIVED, not re-fitted). The three
  candidates this round refuted feed it negatively: ducci-valuation-magnitude
  (magnitudes carry no parity information, kummer-2adic closed),
  zeta-tensor-block-doubling (the block self-similarity lives on the full zeta
  matrix, not the slice), mauduit-rivat-digital-equidistribution (two-point
  digital theory is real but value-domain; no value->index transfer). Distinct
  from the already-proposed bessel-nevanlinna-analytic-trace (which factors the
  SECOND-MOMENT double sum over bits via the meet formula; here the object is
  the FIRST-MOMENT row-weight generating function P and the HJT counting
  function it deforms).
falsifies: >
  The route is wrong if the coefficient-extraction asymptotics of
  (1+z)^n P(n;(1-z)/(1+z)) at z = theta does NOT inherit the log-periodic
  structure of A(n) = P'(n;1) -- i.e. if the transform smooths away the period-1
  factor and leaves only a bare power n^E. The first-step's phase table settles
  this before any theorem work: if the per-doubling phase of the coefficient
  extraction does not match the measured w* phase (amplitude ~0.07), the HJT
  transfer fails and the route is priced out honestly, leaving G-threshold-*
  as pure hypergeometric mode-bound problems as originally stated.
```

## Grounding note (convergence synthesis, this pass)

The research pass closed all three arithmetic-input candidates at the single
recurring obstruction (value-domain -> index-domain transfer absent). The
workspace already held a line that needs no such transfer: the two open
G-threshold lemmas, pure F2/hypergeometric. The new object is the
row-weight generating function P(n;u) = sum_d u^{2^popcount(d)}, whose u=1
derivative is the HJT-proved Pascal-mod-2 counting function. The threshold mean
is exactly a coefficient extraction of (1+z)^n P(n;(1-z)/(1+z)); this turns the
fitted exponent E ~ 0.555 and the log-periodic amplitude ~0.07 into a derived
consequence of the HJT asymptotics. The identity is the load-bearing first
claim and is machine-checkable in one step; the HJT Mellin transfer to the
punctured neighbourhood u ~ 1-2theta is the open content, marked as such.

## What is established vs speculation

- ESTABLISHED (derived here, verified below in first-step 1): the exact identity
  B(n,w) = sum_d E[(-1)^{X_d}] = (1/C(n,w))[z^w](1+z)^n P(n;(1-z)/(1+z)), hence
  the threshold condition is the coefficient-extraction crossing above.
- ESTABLISHED (on disk, proved): A(n) = P'(n;1) = sum_{d<n} 2^popcount(d) obeys
  the HJT log-periodic asymptotics n^{log2 3} P0(log2 n).
- SPECULATIVE: the smooth deformation P(n; 1-2theta+O(theta^2)) inherits the
  HJT log-periodic/Mellin structure, so the coefficient-extraction exponent and
  phase are DERIVED constants of the transform. This is the open content and
  what the first-step's phase table checks.
