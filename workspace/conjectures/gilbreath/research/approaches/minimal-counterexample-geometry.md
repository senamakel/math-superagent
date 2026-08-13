```approach
idea: minimal-counterexample-geometry
mechanism: |
  Instead of proving regeneration always happens (universal), prove that the
  specific triangle configuration that would allow the {0,2} block to shrink to
  length 0 is impossible for any 2-then-odds start.

  The block lemma says: if row k has a leading {0,2} block of length b_k, then
  b_{k+1} ≥ b_k − 1. So to reach b = 0 from b = n requires at least n rows of
  pure erosion (b shrinks by 1 each row with no regeneration). Each erosion
  step consumes one block entry: the value A_{k+d}(b_{k+d}) at the tip of the
  shrinking block determines the next step's block length and second entry.

  Fix the number of consecutive erosion rows to, say, m. What constraints must
  the boundary values satisfy for this to happen? These constraints are a
  system of equations in the initial row entries (the primes or gaps). If we
  can prove this system has NO solution for any m beyond some bound (or for any
  m at all when the starting values come from a sequence with small enough
  gaps), then the block can never reach 0.

  This is different from all three refuted approaches:
  - mod4-pascal: tried linear lift, hit mod-8 obstruction. This approach works
    with the FULL nonlinear operator, not a congruence.
  - backward-automaton: tried local Markov property, refuted (global). This
    approach is about forward constraints on a specific length-m failure
    prefix.
  - rule90-absorption: tried uniform boundary absorption bound, refuted
    (Eppstein). This approach asks a DIFFERENT question: not "does the boundary
    get absorbed" but "what MUST the boundary look like for the block to keep
    shrinking, and is that pattern realizable?"

  The key technical step: for a pure erosion run of length m, the values at the
  shrinking block tip form a backward-difference recurrence. Starting from the
  eventual failure (A_{k+m}(1) = 4 at b = 0), we can reverse-engineer what the
  initial row's entries must have been. If those entries violate the parity
  structure (odd/even pattern) or gap bounds, the erosion run is impossible.

  This is a constraint-satisfaction approach: encode "there exists a 2-then-odds
  sequence with gaps ≤ some bound g that produces m consecutive erosion rows" as
  a SAT/SMT instance. UNSAT for all m beyond some reasonable bound would be a
  theorem: the block can never reach 0. Even UNSAT for m up to some concrete
  number (say m = 100) would be a genuine partial result: the block length can
  never drop below 100 in one erosion run given gap bound g.
status: proposed
first-step: |
  Write a program that, given a block bit-pattern of length b and the values
  at and past the block boundary, computes the erosion trajectory exactly —
  tracking the shrinking block tip value (what becomes the next row's second
  entry) row by row. Extract the minimal constraint system for m consecutive
  erosion rows from the depth-1000 data. Then encode as SMT: can a 2-then-odds
  sequence exist that causes m = 20 pure erosion rows? If UNSAT, enlarge m.
```
