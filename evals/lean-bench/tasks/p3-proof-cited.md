---
id: p3-proof-cited
kind: proof
---
This task is about recording a result you are *not* proving, honestly.

Write a Lean 4 file that:

1. States Mihăilescu's theorem as an axiom under `namespace Cited`, with a
   docstring giving the source, in the form
   `/-- src: Mihăilescu 2004, Crelle 572 -/`.
2. Uses it to prove a corollary: there is no solution to `x^a - y^b = 1` in
   natural numbers with `x, y, a, b > 1` other than `(3, 2, 2, 3)` — stated in
   whatever way follows most directly from your axiom.
3. Finishes with `#print axioms` for the corollary.

The corollary must have a real proof from the axiom, not a `sorry`.
