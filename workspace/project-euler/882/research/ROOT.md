# ROOT — what the reference library establishes

Two L2 folds hold the whole library's claims; seal [[L0.0]] covers the L0
originals that feed one of them.

## The game reduces to counters, and S(n) is a minimax DP
[[game-reduction-and-pass]] (L2.0): the board is a disjunctive sum of short
partisan games; each number is the integer a−b, so the no-skip value is the
single integer **A−B**. Sprague–Grundy does not apply (strictly partisan). The
skip is a zugzwang/pass self-loop (a stopper, so finite S(n)); pass theory
(Larsson–Nowakowski–Santos; Morrison–Friedman–Landsberg) shows a pass changes
outcomes, so **S(n) ≠ A−B**: S(n) is the minimal skip budget for Zero to win,
computed by the (A,B) minimax DP.

## The arithmetic engine is polylog
[[counting-arithmetic]] (L2.0): A(n)=Σ k·popcount(k) and B(n)=Σ k·zerocount(k)
are computable in O(poly log n) — A via A000788 recurrences, B via
A059015=A083652−A000788, with Trollope–Delange 1-periodic-fluctuation structure
from primary sources (Girgensohn; Cheung–Flajolet–Golin–Lee; Larcher–
Pillichshammer). S(n) ∉ OEIS, so no lookup shortcut. This is what lets the DP
run at n=10⁵.

## L0 originals
[[L0.0]] (L1.2 seal) is the underlying CGT/arithmetic foundation behind
[[counting-arithmetic]] and the dead-end/misfiled artifacts (paywalled Li 1976;
three unrelated arXiv pdfs), so attempts are not repeated.

## Standing caveat (open)
Counting (A,B) is a conjectured surrogate — its moves ignore that deleting a
leading 1 can drop 0-bits. Given S(2)=2, S(5)=17, S(10)=64 are reproduced; the
real-vs-counting agreement for all n is checked empirically (brute.py vs
counting.py), and single-aggregate skip-readings were refuted (see MEMORY).
The library pins down **what and how to compute**; the open piece is the S(n)
structure itself.
