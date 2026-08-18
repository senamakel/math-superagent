# Claim: cycle Diophantine bridge

```claim
id: no-nontrivial-cycle/G-cycle-diophantine-bridge-formalised
status: formalised
statement: Given natural numbers m,K,L, real delta, log2,S, a positive K, delta = log 3/log 2, and hypotheses asserting the lower and upper bridge inequalities with log2 = log 2, the two-sided bridge inequality follows.
formalisation: code/lean/no_nontrivial_cycle_G_cycle_diophantine_bridge-33fd98af.lean
```

The binders correspond as follows: `m`, `K`, and `L` carry the cycle size and odd/even counts; `delta` carries `log 3/log 2`; `S` carries the sum of the reciprocal-orbit terms. `hK` carries positivity of K, `hdelta` identifies delta, `hbridge` carries the strict lower bound, `hupper` carries the strict upper bound, and `hlog2` identifies the logarithm constant. The theorem is conditional on `hbridge` and `hupper`; it does not define accelerated cycles or prove those hypotheses, nor does it formalise the asserted exponential-smallness of S. The parameter `m` is unused in the numerical implication.

Kernel verdict: verified; no sorry; axioms `propext`, `Classical.choice`, `Quot.sound`.
