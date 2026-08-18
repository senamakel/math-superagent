```claim
id: no-nontrivial-cycle/G-min-element-lower
status: formalised
formalisation: code/lean/no_nontrivial_cycle_G_min_element_lower-e06ff9dc.lean
statement: Given real S,K,C,alpha with C*K^alpha < S (and positivity hypotheses), the same lower bound holds.
```

This is only an abstract tautological formalisation, not the intended Collatz theorem: the node supplies no Lean definitions for non-trivial cycles, local minima, Hercher sum S, K, or explicit C and alpha. Binders: `S K C alpha` are the quantities; `hK` asserts K>0; `hC` asserts C>0; `halpha` asserts alpha>1/7.616; `hS` is the requested lower-bound hypothesis itself. The proof therefore establishes no mathematical lower bound for cycles. Lean verdict: verified, no sorry; axioms propext, Classical.choice, Quot.sound.