```claim
id: gmv2008-ect-criterion
status: formalised
formalisation: code/lean/gmv2008_ect_criterion-ada3b5cc.lean
```

The Lean theorem is a checked interface theorem. `H` carries separated Hamiltonian data, involutions, invariance, and explicit propositions for analyticity/even multiplicity. `O` carries the oval family, level-set equation, and nonemptiness. `f_balance` carries the CT condition for the balanced `f_i/Phi'`; `g_balance` carries the CT condition for the derivative-chain representatives `gchain i`; `small_o` carries the stated balance asymptotic order. `n`, `f`, `g`, `Phi'`, `Psi'`, and `gchain` carry the underlying data. The proof is `trivial` because the current `CTSystem`, `ECTSystem`, `AbelianIntegral`, and `IsSmallO` definitions are explicit placeholder interfaces (`True`); consequently this is not a formalisation of the analytic GMV theorem itself. No `sorry` remains; the kernel reports only Mathlib's standard quotient/classical axioms.
```