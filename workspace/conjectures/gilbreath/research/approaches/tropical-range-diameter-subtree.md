```approach
idea: tropical-range-diameter-subtree
mechanism: |
  This is an EXACT-INTEGER invariant route (the second way problem.md names:
  "an invariant forcing A_k(1) in {0,2} directly, without tracking blocks").
  It uses only the single identity

      |a - b| = max(a,b) - min(a,b),

  which is exact for every entry and involves no modulus, no congruence, and no
  lifting. Unwrapping the operator one step: |u - v| = max(u - v, v - u), a
  maximum of two SIGNED LINEAR FORMS in (u, v). Nesting this k times shows that
  every entry A_k(i) is the value of an ALTERNATING max/min (tropical)
  polynomial in the k+1 initial entries A_0(i), ..., A_0(i+k) — a max-min
  alternation of signed linear forms

      ± A_0(i) ± A_0(i+1) ± ... ± A_0(i+k)

  with coefficients in {-1, 0, 1} (each first difference uses exactly one +1
  and one -1). Equivalently, A_k(i) is the diameter (max - min of leaf values)
  of the decision tree obtained by branching at every |u-v| node into its two
  linearizations u-v and v-u.

  The conjecture in tropical terms. A_k(1) in {0,2} for all k is the statement
  that this tropical polynomial, evaluated at the window p_2, ..., p_{k+2},
  takes only the values 0 or 2. The proof mechanism to attack is PAIRING /
  CANCELLATION of tropical monomials: exhibit, at each node, a pairing of the
  max-branch against the min-branch so that their signed linear forms agree
  coefficient-by-coefficient on every p_j except a residual whose absolute
  value is <= 2. Such a pairing is a combinatorial certificate (a partial
  involution on the leaves of the decision tree) that is checkable by hand for
  small k and, if it can be shown to be preserved by the recursion, proves the
  conjecture by induction — a route that never names a block or an intruder.

  Why this is different from what was refuted. tropical-box-ball was refuted
  for its SOLITON/BBS/integrability claims; its surviving arithmetic (the
  max-min identity) is explicitly preserved in the record as "a real identity
  and may provide a useful lens" — this proposal develops exactly that
  arithmetic and makes no integrability claim. mod4-pascal died because
  |a-b| == a+b (mod 2^t) fails at t >= 3; the max-min identity is EXACT for
  every entry, so no modulus ever enters and no "ceiling" applies. p-adic
  tracks valuations and carries; this tracks the exact integer value through
  the max/min branching, a different datum.

  Speculative, flagged: that the decision tree admits the <= 2-residual pairing
  for ALL k is the open claim. It is falsifiable immediately at k = 5..8 by
  exact symbolic computation (sympy); if it fails, the run records exactly
  which monomials fail to cancel — itself a sharp structural fact about where
  the operator's non-cancellation concentrates.
status: proposed
first-step: |
  Symbolically expand the leading entry as an alternating max/min of signed
  linear forms over the first k+2 primes for k = 1..8 with sympy (exact
  integers, no floats): at every |u-v| node, replace by max(u-v, v-u), and
  carry the resulting max/min tree to the leaves. Then (a) count the number of
  surviving signed linear forms (leaves), (b) read off the max-branch and
  min-branch leaf polynomials, and (c) test the pairing conjecture: is there an
  involution on the leaves matching each +p_j in a max-branch form with an
  equal -p_j in a min-branch form, leaving a residual of absolute value <= 2?
  Report the leaf count and the residual's Newton polytope for k <= 8, and
  state the pairing lemma precisely if it holds, or the first failing k if not.
```
