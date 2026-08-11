# ROOT — what the reference library establishes

Three L2 folds hold the whole library's claims; seals [[L0.0]] and [[L0.1]]
cover the L0 originals that feed them, and [[L1.0]] (this L2.0 folder) seals
the L1.0 batch — the arithmetic engine and its CGT counting frame.

## The game's values are dyadic Numbers (exact), not the integer A−B
[[game-reduction-and-pass]] (L2.0) reduces the board to a disjunctive sum of
short partisan games; the no-skip surrogate value is **A−B**. Sprague–Grundy
does not apply (strictly partisan). The skip is a zugzwang/pass self-loop (a
stopper, so finite S(n)); pass theory (Larsson–Nowakowski–Santos;
Morrison–Friedman–Landsberg) shows a pass changes outcomes, so **S(n) ≠ A−B**.

The **exact** rule is now sourced: each single-number component is a canonical
**Number**, valued as the simplest dyadic rational strictly between its Left/
Right option values (Simplicity Rule, [[simplicity_rule_dyadic]]). So the board
value is G(n)=Σ k·g(k) with g(k) dyadic, a Right-only skip adds the game −1,
and **S(n)=min{k : G(n)−k≤0}**. This replaces the A−B counting surrogate as the
structural fact and explains S(n)>A−B.

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
three unrelated arXiv pdfs), so attempts are not repeated. [[L0.1]] (L1.2 seal)
covers the skip/loopy side — loopy/zugzwang theory ([[siegel_zugzwang]], Li's
theorem), pass theory ([[pass_waiting]], [[mfl_pass]], [[raw_mfl_pass]]),
surreal values ([[surreal]]) — and a second primary weighted Trollope–Delange
warrant ([[minabutdinov_qweighted]]), plus the strategy dead end. Together they
make the skip a legitimate loopy/zugzwang object and confirm S(n) ≠ A−B.

## L1.0 batch is sealed
[[L1.0]] (this L2.0 folder) seals the ten L1.0 notes:
[[a083652]], [[bitcount]], [[cgt]], [[disjsum]], [[flajolet_weighted_digitalsums]],
[[loopy]], [[mfl_pass]], [[minabutdinov_qweighted]], [[misfiled]], [[normalplay]].
They establish the counting model (disjunctive sum ⇒ G(a,b)=a−b ⇒ board value
A−B; [[normalplay]] win rule; [[loopy]]/[[mfl_pass]] skip ⇒ S(n)≠A−B) and the
**polylog arithmetic engine** (A(n) via [[bitcount]] A000788, B(n) via
[[a083652]]+[[zerocount]] identity, weighted-digit-sum structure from
[[flajolet_weighted_digitalsums]] and [[minabutdinov_qweighted]]), letting the
DP run at n=10⁵. [[misfiled]] records the dead-end downloads. Sealed once;
never revisited.

## Standing caveat (open)
The dyadic Simplicity Rule is the exact game rule sourced here; the counting
(A,B) form is the old approximate surrogate (its leading-1/drop-0 shortcut),
given S(2)=2, S(5)=17, S(10)=64 are reproduced by it. The library pins down
**what to compute** (dyadic G(n), S(n)=min k with G(n)−k≤0) and **how**; the
open piece is the closed-form/rapid evaluation of G(n) at n=10⁵.
