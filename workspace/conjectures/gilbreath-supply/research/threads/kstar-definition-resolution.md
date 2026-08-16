# The correlation-order budget — settled at floor(n/2)

Directive 40 raised the definition question; directive 41 settles it. The
operative reading gives `K*(n) = ⌊n/2⌋`, confirmed by three independent routes
(`kstar_exact`, the sat_solver oracle, the structural check), and
`kstar_structural_capture.txt` honestly refutes its own candidate
characterisation `R(n)-1` rather than fitting it. `fold_cell_degree_correction.md`
also caught a wrong structural fact in a library source (degree is
`2^popcount(d)`, not `popcount(d)`) and checked no other source repeats it. This
thread is closed: the budget is a known number, and characterising it further
does not answer this pass's question.

```thread
id: kstar-definition-resolution
question: What is the operative definition of the correlation-order budget
  K*(n)? — SETTLED (directive 41): the operative cumulative reading gives
  K*(n) = floor(n/2), confirmed by three independent routes (kstar_exact, the
  sat_solver oracle, the structural check); the candidate characterisation
  R(n)-1 was honestly refuted rather than fitted.
status: dead
rests-on: collapse-witness-n8-kstar-ge-2,
  fold-rank-n-minus-2-binomial-proved,
  excess-is-negative-character-sum
blocked-by: none — settled, not stuck (directive 41)
next: none — closed by directive 41. K*(n) = floor(n/2) is settled; cite it
  and move on to priority 1 (the hit-set functional, thread
  hit-set-functional). Do not open more work on K* itself.
```
