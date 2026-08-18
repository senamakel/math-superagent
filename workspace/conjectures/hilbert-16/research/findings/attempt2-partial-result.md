# Attempt 2 partial result (2026-08-18)

The exact oracle `code/brute.py` reproduced all seven worked examples in `problem.md`.

`code/df2a_slow_divergence_symbolic.py` computes, exactly, the Wronskians of the toy family `{1,t,t^2,t^2 log t}`: `1, 1, 2, 4/t`; hence this genuine-log model is ECT on `t>0`. This is only a sanity model, not the published DF2a or I^1_6b displacement.

`code/lean/Lib/ECTSlowDivergence.lean` compiles with no sorry and proves the finite ECT consequence: if a finite family is ECT and a displacement is a nontrivial linear combination, its zero set has cardinality at most `Fintype.card ι - 1`. `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound`.

The exact refutation `code/refute/i6b_ect_symbolic_guard.py` shows ECT is not preserved by addition: `(1,x)` and `(-1,-x)` each have nonzero Wronskian, while their sum is zero. A parameter family can also lose rank at specialization. Therefore the proposed route needs, for the actual four second-type Dulac maps: exact expansions; a uniform analytic/quasianalytic zero-controlled remainder class; noncancellation and fixed rank; treatment of every vanishing slow-divergence stratum; and uniform endpoint/Wronskian conditions. The open graphic remains undecided; no H(2) finiteness claim is made.