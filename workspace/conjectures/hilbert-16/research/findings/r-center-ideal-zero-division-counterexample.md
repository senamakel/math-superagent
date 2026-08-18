# Counterexample: R-center-ideal zero-division rung

The new file `code/lean/Lib/RCenterIdealZeroDivisionRefuted.lean` formalises the intended counterexample skeleton. It defines

`point n = 1 / ((n+1) * π)` and `V z = if z = 0 then 0 else z * sin (1/z)`.

`point_zero` is kernel-checked using Mathlib's `Real.sin_nat_mul_pi`; `point_ne_zero` is also checked. The theorem `zero_set_infinite` is structurally checked from `Set.infinite_of_injective_forall_mem`, once supplied with the two explicitly isolated elementary facts that every point lies in `Set.Ioc 0 1` and that the point map is strictly antitone.

## Lean verdict

`lean_check code/lean/Lib/RCenterIdealZeroDivisionRefuted.lean`:

- `compiled: true`
- `outcome: failed` only because the file intentionally contains two `sorry`s.
- Remaining sorries: lines 41 and 45, `point_mem_collar` and `point_strictAnti`.
- No cited axioms.

The printed axioms for the completed downstream declarations include `sorryAx` because they depend on those two gaps; the elementary closed declarations `point_ne_zero` and `point_zero` depend only on Mathlib's standard kernel axioms `[propext, Classical.choice, Quot.sound]`.

This refutes the *bare stated rung hypotheses* as a route to finite zero bounds: a finite one-element monomial family and zero remainder do not by themselves impose an ECT, quasianalytic, or Noetherian condition. It makes no claim about H(2).
