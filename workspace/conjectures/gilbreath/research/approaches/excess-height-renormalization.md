```approach
idea: excess-height-renormalization — the tail is a self-similar copy of the same operator one level down
mechanism: |
  Halve the interior (A_k(i) = 2·h_k(i), i >= 1; h_k(0) = 1 boundary marker).
  The halved map is h_{k+1}(i) = |h_k(i) - h_k(i+1)|. The leading {0,2} block
  of row k is the leading run of indices i with h_k(i) in {0,1}; write
  b_k = its length, edge x_k = h_k(b_k) in {0,1}, intruder y_k = h_k(b_k+1) >= 2.

  The NEW object is the tail height (the "excess above 1"):

      t_k(i) := max(0, h_k(i) - 1)  >= 0.

  Then t_k(i) = 0 exactly on the block (h in {0,1}), and t_k(b_k+1) = y_k - 1 >= 1
  is the intruder's excess. The conjecture A_k(1) in {0,2} is exactly
  t_k(1) = 0 for all k.

  The key EXACT identity (this is the renormalization, not a conjecture):

      wherever both parents are off the floor (h_k(i), h_k(i+1) >= 1, i.e.
      t_k(i), t_k(i+1) >= 0 with h not 0), one has

          t_{k+1}(i) = max(0, |t_k(i) - t_k(i+1)| - 1)
                     =: E(t_k)(i)   with  E(t) := (D t - 1)_+,  D = |. - .|.

  Proof sketch: h_k(i) = 1 + t_k(i) there, so |h_k(i)-h_k(i+1)| = |t_k(i)-t_k(i+1)|,
  and t_{k+1}(i) = max(0, |h_k(i)-h_k(i+1)| - 1). Done. Hand-checked on
  h=(0,1,2,4) -> (1,1,2): interior columns agree exactly.

  So the operator E is THE SAME absolute-difference map D, followed by a unit
  decrement and a clamp at 0. This is a genuine self-similarity / RG statement:
  the tail of the triangle is a Gilbreath triangle of the excess profile under
  the same operator shifted down by one, and every height level is a nested
  copy of the same object. The three refuted candidates died on "unbounded
  jumps", "unbounded alphabet", "non-monotone level sets" — the excess profile
  is where all three become tame: the floor is at 0, and the max-excess is
  NON-INCREASING (max principle on the halved values: max_i t_k(i) =
  max(0, max_i h_k(i) - 1), and max h is non-increasing). Whether the
  decrement-by-one grinds the tail down following the Ross 2026 digit-sum law
  (c_i ~ C lambda^{s_2(i)}/i, s_2 = binary digit sum of the ROW index) is an
  open question this representation can test directly — it is NOT assumed.

  The wall is a 1-column boundary layer carrying exactly ONE extra bit. The
  only information t discards is the 0-vs-1 distinction inside the block, and
  that is precisely the edge bit x_k = h_k(b_k). At the wall the transition is
  the proved drain law: the intruder excess t_k(b_k+1) = y_k - 1 drops by 1 each
  erosion row (edge x_k = 1) and, when it reaches t = 1 with x_k = 1, the next
  step produces h' = |1-2| = 1, i.e. t' = 0 — that is EXACTLY the (2,4)-event
  (regeneration), and the block then extends rightward over the new leading
  zero-run of E(t). So the full state is (t_k, x_k): a self-similar tail plus a
  one-bit interface.

  Subadditive domination (also exact, provable): t_{k+1}(i) <= t_k(i) + t_k(i+1)
  for every i. For both parents off the floor this is |a-b|-1 <= (a-1)+(b-1)
  (true for a,b >= 2); the floor cases are direct. So E is pointwise dominated
  by the max-plus linear forward-difference map t_i + t_{i+1}.

  What this buys: the open content (regeneration rate) becomes a statement about
  a MONOTONE (max non-increasing), SELF-SIMILAR, floor-clamped operator on the
  nonnegative cone, instead of the raw triangle where jumps/alphabet are
  unbounded. A partial result would be a height-level bound: a tail disturbance
  of excess-height M is ground down one unit per layer, so its leftmost cell
  cannot stall at height >= 2 for more than O(log M) rows without either draining
  to the regeneration threshold t=1 or being re-fed — a quantitative lower bound
  on (2,4)-event frequency under a stated hypothesis on the tail profile.
status: adopted
side: general-class / dynamical (attacks regeneration directly; the block lemma,
  step law and drain law are inputs, not targets)
named-mathematics: renormalization / self-similarity of the absolute-difference
  operator; max-plus (tropical) decrement-and-clamp E(t) = (Dt - 1)_+; 1-column
  boundary layer; the proved max principle (max t_k non-increasing); Ross 2026
  digit-sum decay law as a TESTABLE target (not assumed); Lucas mod-2 /
  Sierpinski structure of the decrement.
speculative: the interior identity E(t) = (Dt-1)_+ is exact (proved above); the
  height-level grind bound and the rate lower bound are NOT yet proved and are
  the target. The interface being fully reducible to (t_k, x_k) with no other
  state is a conjecture to test.
falsifier: (a) a real oracle row where the interior identity fails (would refute
  the renormalization); (b) a row where the interface state needs more than the
  edge bit to predict regeneration; (c) a tail disturbance whose leftmost cell
  stalls above the regeneration threshold indefinitely without draining.
first-step: |
  tool_builder, today (O(depth x width), one row live; report depth and width):
  1. Load witnesses.json (depth 600) and blocks_depth1000.json (depth 1000),
     compute h_k and t_k = max(0, h_k - 1).
  2. VERIFY interior self-similarity: for every k and every i with
     h_k(i) >= 1 and h_k(i+1) >= 1, assert
        t_{k+1}(i) == max(0, |t_k(i) - t_k(i+1)| - 1).
     Report mismatch count (expect 0).
  3. VERIFY subadditive domination t_{k+1}(i) <= t_k(i) + t_k(i+1) for all k,i
     (expect 0 violations).
  4. CHARACTERIZE the wall: for each row, find the columns i with h_k(i) = 0
     and h_k(i+1) >= 1; tabulate (edge x_k, intruder excess t_k(i+1)) against
     t_{k+1}(i); confirm the drain law t_k(i+1) -> t_{k+1}(i) = t_k(i+1) - 1
     when x_k = 1, and regeneration when (x_k, t_k(i+1)) = (1,1).
  5. MEASURE the layer grind: track M_k = max_i t_k(i) (max principle: expect
     non-increasing outside regeneration) and the number of rows for the
     leftmost tail cell to drop by one unit; report whether the decay follows
     the dyadic/digit-sum pattern.

## Why this is not already on disk

- **Not `lipschitz-excess-lyapunov` (proposed):** that candidate hunts a SCALAR
  Lyapunov functional E(h) = sum_i max(0, |h_i-h_{i+1}|-1) and whether it is
  non-increasing. This approach keeps the same local excess quantity but is NOT
  looking for a scalar potential — it promotes the excess PROFILE t_k(i) to the
  state of a SELF-SIMILAR operator E(t) = (Dt - 1)_+, and the deliverable is the
  renormalization identity plus a height-level grind bound, not a Lyapunov
  function. The scalar Lyapunov program is known to fail on XOR zigzag; the
  profile-level identity is exact and does not compete with it.
- **Not `max-plus-tropical-spectral-dynamics` (refuted):** that entry was killed
  because a max-plus functional dominated by the tail cannot see A_k(1) <= 2.
  The subadditive domination here is used the other way round: it is a
  pointwise FORWARD bound t_{k+1}(i) <= t_k(i) + t_k(i+1) that upper-bounds how
  far the tail can propagate leftward, combined with the exact decrement-and-
  clamp identity. It does not claim any tropical spectral eigenvalue certifies
  the conjecture.
- **Not the level-set/percolation candidate (refuted):** no comparison to an
  external percolation process is claimed. The monotone object here is the
  max-excess of the tail, which is non-increasing by the elementary max
  principle, a fact about THIS operator rather than an imported coupling.
