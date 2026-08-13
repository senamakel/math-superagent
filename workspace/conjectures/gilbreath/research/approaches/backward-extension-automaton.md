```approach
idea: Backward extension as a finite-state automaton — prove the conjecture by
      showing the local valid-extension set eventually equals {0,2} and traps
mechanism: >
  Muney 2026 studied the sets of integers that can be appended to a prefix of a
  Gilbreath triangle while preserving the "leading column = 1" property. This is
  a backward-extension problem: given A_0(1..N) and the computed rows
  A_1..A_K(1..N−K), which integers x can be placed at A_0(N+1) such that the
  resulting (N+1)-column triangle, with A_0(N+1)=x, still has A_i(1)=1 for all
  i computed so far?

  The approach: treat the Gilbreath triangle as a deterministic transducer from
  the initial row to the left column. If the set of valid next-values at
  position N depends only on a bounded window of the recent row history, then
  the sequence of valid-extension sets forms a finite-state process. If one can
  prove that the valid-extension set eventually becomes {0,2} for the primes —
  i.e., only 0 and 2 (after the reduction to second-entry language) can be
  appended without breaking the leading-1 property — then the conjecture is a
  finite induction.

  More precisely: define the "state" at position N as the last K rows truncated
  to a window of width W (the "backward light cone" of the left column). The
  extension function e_N(S) = {x: appending x to the initial row preserves A_i(1)=1
  for all i ≤ depth(N)}. If e_N stabilizes to {x: x ≡ 0 mod 2} intersected with
  some congruence condition, and the state space is finite, then proving the
  conjecture reduces to (a) computing the state transition graph for small K,W,
  (b) showing the prime sequence stays in the "good" component, and (c) arguing
  that the good component is a trap.

  The Bhat–Cobeli–Zaharescu 2023 "quasi-periodicity" results support this: they
  found that Proth–Gilbreath triangles for various starting sequences exhibit
  filtered-ray structure — exactly the kind of regular behavior a finite-state
  model would produce. A key question: what is the minimal K,W that suffices to
  determine the extension set? If K=3, W=5 suffices, the state space is tiny and
  the conjecture may be checkable by explicit enumeration of the automaton.

status: proposed (speculative — depends on whether the extension set depends
        only on local data, which is not yet established)
first-step: >
  Compute the valid-extension sets for the prime triangle at positions N=1..100
  by brute force over candidate next-primes (using the actual next prime as the
  test value and nearby candidates as falsifiers). For each N, record the state
  = (last 2 rows, window of width 4) and the extension set e_N. Check whether
  e_N depends only on the state, i.e., whether states that reoccur have the
  same extension set. If yes, the automaton exists and the next step is to
  characterize its structure; if no, find the minimal K,W that makes it Markov.
  The code goes in code/approaches/backward_extension/.
```