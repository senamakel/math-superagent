# Fold: game theory core

Reduces the board to counting. Each number with `a` 1-bits and `b` 0-bits is
the partisan game `G(a,b)={G(a-1,b)|G(a,b-1)}`, `G(0,0)=0`.

- [[cgt]] — CGT recursive position form (Left/Right move sets), disjunctive
  sums, numbers as games; the board decomposes into a sum of subgames.
- [[disjsum]] — structural result: `G(a,b)` = the integer `a-b`, so the whole
  board's no-skip value is `A-B` (A = total 1-bits, B = total 0-bits).
- [[surreal]] — why `a-b` is EXACT (simplest surreal strictly between the two
  options); skips lie outside short-game numbers, so `A-B` alone does not give
  `S(n)`.
- [[partisan]] — Sprague–Grundy does NOT apply (disjoint move sets), so the
  run uses minimax over `(A,B)`, not nimbers.
- [[normalplay]] — unable-to-move loses; `A-B>0` ⇒ One wins always without
  skips ⇒ Zero cannot win without a skip budget.

What this yields: the game reduces to the two totals (A,B), which is what the
counting DP iterates over.
