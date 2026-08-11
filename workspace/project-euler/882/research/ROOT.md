# ROOT — what the reference library establishes

## The exact game value is a dyadic Number; S(n) = min{k : G(n)−k ≤ 0}
The board is a disjunctive sum of short partisan games
([[game-reduction-and-pass]]); strictly partisan so Sprague–Grundy does not
apply ([[partisan]]). Each single-number component is a canonical **Number**, valued
as the simplest dyadic rational between its Left/Right options (Simplicity Rule,
[[simplicity_rule_dyadic]]). Board value G(n)=Σ k·g(k) dyadic; the skip adds game −1
(zugzwang/pass self-loop, a stopper ⇒ finite S(n), [[siegel_zugzwang]]/[[loopy]]), so
**S(n)=min{k : G(n)−k≤0}**. Pass theory ([[pass_waiting]], [[mfl_pass]]) shows a pass
changes outcomes ⇒ **S(n) ≠ A−B**. The old counting surrogate (G(a,b)=a−b ⇒ value A−B)
is approximate (leading-1/drop-0 shortcut) yet reproduces S(2)=2, S(5)=17, S(10)=64;
S(n) ∉ OEIS ([[weightedsearch]]).

## Arithmetic engine is polylog
[[counting-arithmetic]]: A(n)=Σ k·popcount(k), B(n)=Σ k·zerocount(k) computed in
O(poly log n) — A via A000788, B = A059015 = A083652−A000788, Trollope–Delange
1-periodic-fluctuation structure from primary sources ([[trollopedelange]],
[[flajolet_weighted_digitalsums]], [[minabutdinov_qweighted]], [[weightedmom]]). This
lets the DP run at n=10⁵.

## L0 / L1 / L2 folds
[[L0.0]] (seal [[L1.2/L0.0.md]]) = CGT/arithmetic foundation plus dead-end/misfiled
artifacts. [[L1.2/L0.1.md]] = skip/loopy side ([[siegel_zugzwang]], [[pass_waiting]],
[[mfl_pass]], [[surreal]], [[minabutdinov_qweighted]]) making the skip a legitimate
loopy object. [[L1.0]] (seal [[L2.0/L1.0.md]]) seals ten L1.0 notes
([[a083652]], [[bitcount]], [[cgt]], [[disjsum]], [[flajolet_weighted_digitalsums]],
[[loopy]], [[mfl_pass]], [[minabutdinov_qweighted]], [[misfiled]], [[normalplay]]):
counting model, win rule, skip ⇒ S(n)≠A−B, polylog engine. [[L1.1]] (seal
[[L2.0/L1.1.md]]) seals the ten
L1.1 notes (game structure: [[partisan]], [[surreal]], [[siegel_zugzwang]],
[[pass_waiting]], [[strategy]] dead end; arithmetic: [[trollopedelange]],
[[verify_trollopedelange]], [[weightedmom]]). All seals are one-time, never revisited.
Misfiled/unrelated downloads recorded in [[misfiled]]; strategy dead end in [[strategy]].

## Standing caveat (open)
Dyadic [[simplicity_rule_dyadic]] is the exact game rule; the counting (A,B) form is
the old surrogate. The library pins down **what** to compute (dyadic G(n), S(n)=min k
with G(n)−k≤0) and **how** (polylog engine); the open piece is rapid evaluation of
G(n) at n=10⁵.
