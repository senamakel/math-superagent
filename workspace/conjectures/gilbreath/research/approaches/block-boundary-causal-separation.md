```approach
idea: block-boundary-as-right-shifted-difference-matrix
mechanism: |
  The Gilbreath triangle A_k(i) can be seen as a "difference table" of the
  starting sequence. A classical fact (easily verified): the entries
  A_k(i) are the absolute values of the k-th forward differences of the
  sequence A_0, with signs governed by the min(a,b) branch. Concretely,
  the standard forward difference Δ_k(i) = Σ_{j=0}^k (−1)^{k−j} C(k,j) A_0(i+j)
  satisfies |Δ_k(i)| = A_k(i) when the signs all agree (which happens when
  the sequence is monotone in the relevant window), but the absolute value
  breaks the linearity.

  Now the key observation: the CONJECTURED shape of the triangle is that
  every row has A_k(1) ∈ {0,2} and A_k(0) = 1. This means the difference
  between the first term (always 1) and the second term (0 or 2) is 1, so
  the next row starts with 1. The whole triangle has the structure of a
  "carryless" difference table with a protected left column.

  The NEW representation: treat the absolute-difference operator as a
  **right-shift of the tail** of each row, composed with a "boundary
  adjustment" at the {0,2} block edge. Specifically:

  Let row A_k be split as A_k = (1, B_k, T_k) where B_k is the leading
  {0,2} block of length b_k and T_k is the tail (values ≥ 4). Then

      A_{k+1} = (1, |B_k − shift_right(B_k)|_boundary, ...)

  The difference within B_k is the XOR/{0,2} closure, which stays in {0,2}.
  The boundary at position b_k involves the last entry of B_k (which is 0 or 2)
  and the first entry of the tail T_k(0) (the intruder y). The tail itself
  shifts left: the new tail is T_{k+1} = |T_k − shift_right(T_k)| with the
  first entry modified by the boundary.

  The CRUCIAL structural observation (verified to depth 1000): the tail T_k,
  when viewed from the left edge, is "the same" as the tail of some EARLIER
  row, shifted rightward. This is because the Gilbreath operator on the tail
  is the same operator as on the whole row, but with a different starting
  value — the intruder y at the boundary. And the intruder evolves by the
  drain law: it drops by exactly 2 when the edge is 2, and stays when the
  edge is 0.

  This suggests a FACTORIZATION: the row A_k can be reconstructed from
  (1) the block B_k, (2) the intruder y_k, and (3) a REFERENCE to an earlier
  row's tail. Specifically, the tail T_k is (up to boundary adjustments at
  the left) the forward-difference triangle of the subsequence of gaps
  starting from the intruder's position.

  If this factorization can be made exact, then the conjecture reduces to:
  **the factorization never produces a carry that reaches position 1.** The
  tail always stays to the right of the block, and the block always absorbs
  the boundary interactions. This is a "tail absorption" picture: the tail
  is a right-shifted copy of an autonomous Gilbreath triangle that never
  influences the left column.

  The MATHEMATICAL CONTENT: prove that the Gilbreath triangle of a sequence
  S = (2, odd, odd, ...) has the property that the leftmost entry > 2 in
  any row is ALWAYS preceded by a leading {0,2} block that "protects" the
  left column from perturbation. This is not the block lemma (which says
  the block protects the left column from WITHIN) — it's a stronger claim:
  that the ENTRIES BEYOND the block cannot influence position 1 at any
  future row. I.e., the influence cone of position i ≥ b_k+1 never reaches
  the left column before the block erodes away — and by the time the block
  has eroded, the intruder has drained to 4 and a regeneration has occurred.

  This is a "causal separation" theorem: the triangle decomposes into a
  left part (the protected block + its descendants) and a right part (the
  tail), and information flows only LEFT→RIGHT within the block and only
  RIGHT→LEFT through the single boundary cell. The boundary cell is the
  only coupling, and its dynamics (drain + edge-flip) determine whether
  the right part ever "breaks through" to position 1.

  The theorem to prove: **the influence of the tail on position 1 is bounded
  by the time it takes the block to erode to the boundary cell.** Since the
  block erodes at exactly one per row, and the boundary cell's drain law
  moves the intruder monotonically toward 4, the tail cannot reach position
  1 before the boundary cell has processed the intruder down to 4. And when
  the intruder is 4 and the edge is 2, regeneration extends the block
  rightward, pushing the tail further away.

  This is a **Lyapunov function** approach in a different guise: the pair
  (block_length, intruder_value) is the state, and the transition is:
  - Erosion: (b, y) → (b−1, y') where y' = y − 2·[edge=2]
  - Regeneration: (b, 4) with edge=2 → (b + j, y') where j ≥ 0

  The Lyapunov function L(b, y) = b − (some function of y) might be provably
  non-decreasing in expectation (or always). If L never reaches 0 (i.e., b
  never reaches 0 while y is still ≥ 4), the conjecture holds.

  **Speculative**: the exact form of L and the proof that it never decreases
  must be found. The data (depth 1000) shows b never reaches 0 while the
  intruder exists; b=2 occurs only at k=1, and the minimum after that is 7.
  So L(b,y) = b is itself bounded away from 0 empirically, and the task is
  to prove that b_k ≥ 1 for all k given the prime gap sequence as input.

  Why this beats existing approaches:
  - NOT the refuted potential approaches (runcount, total-variation): those
    used global potentials on the row structure and failed on (a,a,c,c)
    counterexamples. This approach uses a LOCAL state (b, y) at the boundary
    and a causal-separation argument that the rest of the row is irrelevant.
  - NOT ducci-potential-max-decrease: that approach looks for a Lyapunov
    function on the entries themselves; this looks for a Lyapunov function
    on the BLOCK/INTRUDER pair.
  - NOT p-adic-valuation: that approach tracks carries through the whole
    triangle; this approach isolates the left column from the right via the
    block boundary.
  - The "causal separation" claim is a new structural statement that, if
    proved, reduces the conjecture to a 2-state process (b, y) with well-
    understood dynamics.
status: proposed
first-step: |
  Verify the causal separation hypothesis on the real data. For each row k
  in the live regime (k = 1..161), compute the "influence cone" of the
  intruder position on the left column: starting from row k at column
  i = b_k + 1 (the intruder), track which cells in subsequent rows depend
  on this value. Specifically, cell (k+d, j) depends on (k, i) if there is
  a path through the difference dependencies connecting them. Mark all cells
  that are reachable from the intruder. Then check: does the left column
  (position 0 or 1) EVER become reachable from the intruder before the
  block length b_{k+d} drops to 0? In the depth-1000 data, this should
  NEVER happen (the conjecture is verified, so position 0 stays 1). But the
  STRUCTURAL claim is stronger: that the influence cone of the intruder is
  always strictly to the right of the block boundary at every row, i.e.,
  the intruder's descendants never enter the {0,2} block from the right at a
  rate faster than the block erodes from the left. Write a program that
  computes the dependence cone widths and checks this claim for all k ≤ 161.
  If it holds, state the precise causal-separation lemma that would prove it
  for all k.
```
