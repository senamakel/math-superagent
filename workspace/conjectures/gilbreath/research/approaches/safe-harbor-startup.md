```approach
idea: safe-harbor-startup
mechanism: |
  The event-rate sweep (1154 sequences, 852 deaths, ALL in rows 1..10, zero
  deaths after row 10 through depth 4000) reveals a structural fact that
  neither the original dictionary proposal nor the literature captured:
  regeneration failure is a STARTUP TRANSIENT, not an asymptotic-rate problem.
  Sequences that survive the first ~10 rows enter a "safe harbor" from which
  they never exit — the block-length process becomes self-sustaining. The
  primes survive the startup. So the conjecture is a startup-classification
  problem: prove that the prime gap sequence's first ~k0 rows place the process
  in the safe harbor.

  The mechanism that makes this work has three proved components (all from the
  run, all universal for nonnegative arrays):

  1. **Step law** (proved, `step-law-theorem-proved`): b_{k+1} ≥ b_k ⟺
     (x_k,y_k) = (2,4), else b_{k+1} = b_k − 1. The block edges down at
     exactly one per row during erosion; it grows only on the (2,4)-event.

  2. **Drain law** (corollary of step law): during erosion, y_{k+1} = y_k −
     2·[x_k = 2]. The intruder is monotone non-increasing, reaches 4 and
     sticks. Intruder-4 is absorbing: every maximal 4-run ends in a
     regeneration until finite-width exhaustion.

  3. **Recharge identity** (corollary): b_k = b_1 + Σ_{events i<k}(j_i+1) −
     (k−1). For b_1 = 2 (the primes), the conjecture is Σ(j_i+1) ≥ k−2.

  The safe-harbor claim: there exists a property P of the {0,2}-block suffix +
  intruder pair such that (a) P is entered by the prime rows within a small
  number of startup rows k0, and (b) P is FORWARD-CLOSED: once P holds at row
  k, it holds at row k+1, and it implies b_k ≥ 1 and the (2,4)-event rate is
  sufficient.

  The candidate P is: "the intruder is ≤ 4 AND the block's terminal suffix has
  a run structure that guarantees edge-flip to 2 before the intruder exceeds 4."
  The drain law says intruder-4 is absorbing, and the Rule 90 XOR interior
  determines when the edge flips from 0 to 2. The maximum edge-0 run length
  observed in the live regime is 29 (code/out/block_constancy.captured.txt),
  and in every case the flip eventually occurs — the erosion is genuine but
  bounded. A combinatorial bound on the maximum edge-0 run length in terms of
  the suffix's XOR-image would close the startup argument.

  Named mathematics: Lyapunov function (recharge identity), absorbing set
  (intruder-4), Rule 90 / Sierpinski XOR interior for edge-flip timing,
  startup-transient classification. The approach is forward, exact-integer,
  and the only prime-number-theoretic input is "the primes' first ~k0 gap
  pattern lands in P" — a finite check.

  Why it beats the refuted approaches: It is NOT a congruence (beats
  mod4-pascal), NOT a local extension automaton (beats backward-extension),
  NOT an absorption-time claim (beats rule90-absorbing), NOT a variation-
  diminishing lemma (beats tropical/total-variation which both died on the
  run-count counterexample (0,0,1,1) → (0,1,0)). It targets exactly the
  startup transient, which the sweep data shows IS the whole problem, and
  uses only proved universal combinatorial facts plus one finite check on
  primes.

  Speculative: whether the edge-0 run length admits a combinatorial bound from
  the XOR interior is open and is what the first step measures. If the maximum
  edge-0 run length can be bounded purely combinatorially from the suffix
  structure, the startup argument closes — and the bound, together with the
  finite check on the primes' first ~k0 gaps, would prove the conjecture.

status: adopted
precedent: |
  > The original gap-pattern-trigger-dictionary proposal ("find a finite set of 
  short gap patterns that provably force a (2,4)-event") was half right: it 
  correctly identified that the problem is a FORWARD classification from the 
  starting sequence, not an infinite-regeneration-rate problem. But the sweep 
  data shows two things that force a re-scope:

  (1) The finite-alphabet dictionary in gap space is vacuous for the primes:
  prime gaps are unbounded (34 in first 2000, 89 in 1.27M), so no finite gap
  alphabet covers them. Families with bounded-wide support ({2..20}, {2..100})
  die 100% even with first-gap=2.

  (2) The "startup transient" finding is the key: all deaths in first 10 rows;
  survivors of row 10 survive to depth 4000. The problem is NOT about bounding
  an infinite regeneration rate — it is about classifying which startup
  configurations lead to the safe harbor.

  The synthesis: re-target the dictionary idea at BLOCK-BOUNDARY SUFFIX patterns
  rather than raw gap patterns, and frame the goal as a forward-closure property
  entered during startup. The three proved universal components (step law, drain
  law, recharge identity) provide the algebraic engine; the Rule 90 XOR interior
  provides the edge-flip timing; the one prime-number-theoretic input is verifying
  that the primes' first ~k0 rows land in the safe harbor.

first-step: |
  Measure the startup transient on the real prime rows to determine k0 and the
  transition into the safe harbor. Specifically, from blocks_depth1000.json:

  1. Compute the intruder values y_k for rows k=1..100 (the live regime), and
     find the first row k0 after which y_k ≤ 4 for all subsequent rows.
     (The drain law + absorbing-4 property means once y ≤ 4, it stays ≤ 4.)

  2. For each row k=1..k0, record the block suffix (last L=30 halved entries)
     and whether the edge-0 run length r0 exceeds some threshold. Find the
     maximum edge-0 run length in the live regime.

  3. Compute the recharge-identity surplus S_k = Σ_{i<k}(j_i+1) − (k−2) at each
     event, and confirm it is non-decreasing (the safe-harbor property).

  4. State the precise candidate P: "y_k ≤ 4 AND b_k ≥ b_min" for some b_min,
     and verify that P is forward-closed on the prime rows (i.e., P(k) ⇒ P(k+1)).

  5. State the startup theorem: "there exists k0 ≤ K such that the prime Gilbreath
     process satisfies P at row k0, and P is forward-closed ⇒ the conjecture holds."
     Then the work reduces to (a) proving the forward-closure of P combinatorially,
     and (b) verifying the primes enter P within K rows — a finite computation.

  Code: one program, reads blocks_depth1000.json, reports k0, the P-defining
  quantities, the surplus trend, and whether P is forward-closed on the data.
```