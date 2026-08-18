# Statement.lean — H16.2 stated in Lean, verdict

Date: this pass. File: `code/lean/Lib/Statement.lean`.

`lean_check` verdict (verbatim):

```
compiled: true
outcome: failed
sorry warnings:
  /workspace/code/lean/Lib/Statement.lean:150:8: warning: declaration uses `sorry`
#print axioms:
  'H16.h16_2' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
  'H16.h16_2' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
cited axioms: none
checked:
  theorem h16_2 : ∀ n : ℕ, ∃ N : ℕ, ∀ f : PlanarPolyField n,
    (LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N
```

`outcome: failed` is exactly the intentional-`sorry` verdict ("declaration uses `sorry`").
The only extra axiom is `sorryAx` from the deliberate `:= sorry`. The other three
(`propext`, `Classical.choice`, `Quot.sound`) are the kernel's own three.

## Task `fix-statement-lean-compile` — both requirements satisfied, no edit needed

1. **Real degree hypothesis**: `PlanarPolyField n` carries `P Q : MvPolynomial (Fin 2) ℝ`
   with `degP : P.totalDegree ≤ n`, `degQ : Q.totalDegree ≤ n` (no more
   `degree_at_most : True` placeholder). The `Plane → Plane` map `toMap` evaluates
   the two polynomials pointwise, so the map is definitionally the field.
2. **ncard hole closed**: `Set.ncard` of an infinite set is `0`, so a bare
   `ncard ≤ N` would be vacuous. `h16_2` states `(LimitCycleSet f.toMap).Finite ∧
   (LimitCycleSet f.toMap).ncard ≤ N` — finiteness explicitly, then the bound.

Do not redo and do not revert (`CONTEXT.md` gap 3's anti-revert discipline extends
here: the file compiles and must not be rebuilt hostilely).

## Where the statement could differ from problem.md (audit notes)

- (a) `∀ n : ℕ` rather than `n ≥ 2`. Stronger as written, but H(0)=H(1)=0 so not
  false. State as-is.
- (b) Only the **bound** half of H16.2 is formalised. The second half ("what are
  the possible configurations / nestings") is NOT stated here. That is a separate
  statement nobody has written in Lean yet.
- (c) `IsIntegralCurve γ (fun _ => X)` uses the derivative relation directly;
  Mathlib does not package the Picard–Lindelöf flow of a concrete polynomial field
  as a `Flow ℝ Plane`. A proof would need that construction.
- (d) `IsLimitCycle`'s isolation clause is written by hand (Mathlib has no limit-cycle
  notion). It reads: any non-constant periodic integral curve of the same field whose
  orbit lies in a neighbourhood (`𝓝ˢ`, the neighbourhood filter of a set) of γ's orbit
  equals γ's orbit. This is the clause most in danger of not matching the intended
  notion — audit it before building anything on it.

## Claims ledger

No row in the claims ledger for the H16.2 statement itself. If a row is wanted, it
must be `status: asserted` (the verdict does not pass `formalised` because of the
deliberate `sorry`), `formalisation: code/lean/Lib/Statement.lean`.
