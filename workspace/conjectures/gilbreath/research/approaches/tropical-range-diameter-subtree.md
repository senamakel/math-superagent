```approach
idea: tropical-range-diameter-subtree
mechanism: |
  This is an EXACT-INTEGER invariant route (the second way problem.md names:
  "an invariant forcing A_k(1) in {0,2} directly, without tracking blocks").
  It uses only the single identity

      |a - b| = max(a,b) - min(a,b),

  iterated. Every entry A_k(i) is therefore the difference of two "tropical"
  (max-plus / min-plus) polynomials in the initial row A_0(i), ..., A_0(i+k).
  Concretely, iterating max/min gives

      A_k(i) = max_{sigma in S} L_sigma(A_0(i),...,A_0(i+k))
             - min_{sigma in S} L_sigma(A_0(i),...,A_0(i+k))

  where S is a set of sign patterns and each L_sigma is a SIGNED LINEAR FORM
  (+-A_0(i) +- A_0(i+1) +- ... +- A_0(i+k)). Equivalently, A_k(i) is the
  DIAMETER (range) of the multiset of the 2^k signed sums of the (k+1)-window
  of initial data, restricted to the sign patterns that survive the max/min
  branching. This is pure max-plus algebra: no congruence, no modulus, no
  lifting — the exact object the mod-4/p-adic routes could not reach.

  Why this is different from what was refuted. The tropical-box-ball proposal
  was refuted for its SOLITON/BBS/integrability claims; the pure tropical
  arithmetic was explicitly preserved as "a real identity and may provide a
  useful lens". This proposal develops exactly that surviving arithmetic and
  makes no integrability claim. It is also not a congruence lift: mod4-pascal
  died because |a-b| == a+b (mod 2^t) fails at t>=3; the max-min identity is
  EXACT for every entry, no modulus ever enters.

  The conjecture in tropical terms. A_k(1) in {0,2} for all k is equivalent to
  the statement that the tropical diameter of the leading subtree — the range
  of the signed-sum multiset over the window p_2,...,p_{k+2} — never exceeds 2.
  The mechanism to prove this is a PAIRING argument: exhibit, for every
  surviving max-term +-p, a surviving min-term with the SAME coefficient on
  every p_j except at most a residual of total size 2. Such a pairing is a
  combinatorial certificate (an involution on the sign-pattern set S) that is
  checkable by hand for small k and, if it can be shown to persist under the
  recursion, proves the conjecture by induction — a route that never names a
  block or an intruder.

  Named mathematics: the max-plus (tropical) semiring, max-plus polynomials
  and their Newton polygons, and the cancellation/pairing of tropical monomials
  (the tropical analogue of "the diameter is small because the polytope is
  almost a point"). The first step below produces the explicit tropical
  polynomial of A_k(1) for small k and tests the pairing conjecture on it.

  Speculative part, flagged: that the sign-pattern set S admits the pairing for
  ALL k is the open claim; it is falsifiable immediately at k = 5..8 by exact
  symbolic computation (sympy), and if it fails the run records exactly which
  monomials fail to cancel — itself a sharp structural finding about the
  operator.
status: proposed
first-step: |
  Symbolically expand the leading entry as a max/min of signed sums over the
  first k+2 primes for k = 1..8 with sympy (exact integers, no floats):
  write A_k(1) = |A_{k-1}(1) - A_{k-1}(2)| and, at every |u-v|, replace by
  max(u,v) - min(u,v) to build the full piecewise-linear expansion as a
  difference of two max-plus polynomials. Then (a) count the number of
  surviving signed linear forms (this is the size of the sign-pattern set S),
  (b) read off the max and min coefficients, and (c) test the pairing
  conjecture: does there exist an involution on S matching every +p_j in a
  max-term with an equal -p_j in a min-term, leaving a residual whose absolute
  value is <= 2? Report the tropical polynomial and the Newton polygon of the
  residual for k <= 8, and state the pairing lemma precisely if it holds.
```
