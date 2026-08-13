```approach
idea: total-variation-oscillation-potential
mechanism: |
  The row A_{k+1} IS the total-variation (edge-length) density of A_k:
  A_{k+1}(i) = |A_k(i) - A_k(i+1)|, so the whole Gilbreath triangle is the
  iteration of the total-variation map T(x)_i = |x_i - x_{i+1}| on the zigzag
  path through the primes. This reframes the conjecture as a statement about
  the oscillation/complexity of a 1D path under repeated edge-length folding.

  The named classical object is the variation-diminishing property of the
  first-difference operator and the run/count structure of a sequence: for a
  sequence x, the "number of runs" r(x) (maximal constant stretches) and the
  "number of turning points" (strict local extrema) t(x) measure its
  oscillation, and total variation TV(x) = sum |x_i - x_{i+1}| = 2 * (sum of
  positive increments). The proposal is to establish a sharp
  variation-diminishing lemma for T:

      r(T(x)) <= r(x)   (and t(T(x)) <= t(x)),

  with a classification of the equality case (equality forces x into a rigid
  two-valued or monotone form). Inside the leading {0,2} block, r is the
  number of 0<->2 transitions; the block lemma's apex/Rule-90 result shows the
  bit-level run count is NOT monotone there (Sierpinski grows it), so the
  monotonicity, if it holds, is a GLOBAL fact about the whole row including
  the intruder and tail, not a fact about the block alone.

  The candidate Lyapunov function is the run complexity of the row: if the run
  count (or some weighted variant, e.g. run count plus a penalty for the
  intruder's magnitude) is non-increasing and strictly drops whenever the
  second entry leaves {0,2}, then a row with A_k(1) = 4 would force an
  infinite strictly-decreasing sequence of non-negative integers — impossible —
  and the conjecture follows by contradiction. This is the second route
  problem.md names ("an invariant forcing A_k(1) in {0,2} directly"), via a
  scalar oscillation potential rather than block tracking.

  Why it is distinct from the refuted approaches: rule90-absorbing-boundary
  claimed a bounded absorption TIME for intruders, and died (Eppstein); this
  proposal claims a monotone run-count POTENTIAL, which is a scalar invariant
  that Eppstein's right-edge injection does not obviously defeat (a single
  huge far value contributes one run, not unbounded run count). mod4-pascal
  was a congruence; this is exact on run structure. block-apex-parity looked
  at the *pattern class* of the block; this looks at the *run count* of the
  whole row and its monotonicity under T. Speculative: the sharp
  variation-diminishing lemma with its equality classification is conjectural
  and must be tested on adversarial rows before it is trusted; research should
  check whether the run-count/turning-point monotonicity under T is already a
  named lemma (variation-diminishing operators, Pólya frequency sequences, or
  the oscillation theorems in the Ducci literature).

  Why it could beat the obstruction: consumption/regeneration is a balance of
  RATES; a Lyapunov function collapses the rate balance into a scalar
  inequality that must eventually terminate, sidestepping the need to track
  blocks at all. If the equality case of the lemma is exactly the long
  {0,d}-block rigidity that CHT isolate, then the potential gives a direct
  non-block proof that the rigidity cannot persist under the prime gaps'
  oscillation structure.
precedent: |
  (grounded/refuted, librarian cycle) REFUTED as stated — the elementary
  lemma r(T(x)) <= r(x) is FALSE. Hand counterexample: x = (5,5,0,0) has two
  runs but T(x) = (0,5,0) has three. The turning-point analogue t(T(x)) <=
  t(x) is also FALSE: t(5,5,0,0) = 0, t(0,5,0) = 1. Both fixes are
  immediate from the structure of T: T collapses equal adjacent pairs to 0
  and maps unequal pairs to positive values, so a constant run of length m
  becomes (m-1 zeros) + one boundary value — a run of length >= 3 can
  CREATE a new run (two boundaries) instead of just one. The
  counterexample (a,a,c,c) is exactly Chamberland's rigid borderline class
  (Ducci Lemma 3.1, held: chamberland-unbounded-ducci-sequences, the class
  where the max-factoring potential does NOT decrease), so the borderline
  classification from the Ducci potential proof is the right place to look
  for a CORRECTED potential (e.g. weighted run count, or run count after
  factoring maxima), not the raw r and t. The classical variation-diminishing
  theory (Schoenberg, Polya frequency, total positivity, sign-variation of
  LINEAR operators) is a deep named literature but concerns LINEAR operators
  and SIGN-CHANGES; the absolute-difference map T is nonlinear, so the PF/TP
  machinery does not transfer as-is. No source states r(T(x)) <= r(x) or
  t(T(x)) <= t(x) (searched; the claim does not appear in the Ducci or
  variation-diminishing literature — it is an elementary false conjecture,
  now refuted here). A corrected potential must handle the (a,a,c,c)-type
  equality cases explicitly.
status: refuted
first-step: |
  Write a checker that computes r(A_k) (number of maximal constant runs) and
  t(A_k) (number of strict local extrema) for every prime row to depth 1000,
  and tests the two candidate monotonicities r(A_{k+1}) <= r(A_k) and
  t(A_{k+1}) <= t(A_k) row by row. Report every counterexample with its row
  index and the exact run sequence, and separately run the same check on
  adversarial 2-then-odds rows (including Eppstein's right-edge injection) to
  find the equality/failure cases. This produces the precise statement (with
  its equality classification) that research then sources against the
  variation-diminishing and Ducci-oscillation literature.
```
