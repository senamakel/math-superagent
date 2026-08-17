# Statement.lean now compiles against the kernel

`lean_check code/lean/Lib/Statement.lean` → `compiled: true`, with exactly one
`sorry` remaining, which is the deliberate deliverable in `h16_2`.

## Elaborated statement (checked)

```lean
theorem h16_2 :
    ∀ n : ℕ, ∃ N : ℕ, ∀ f : PlanarPolyField n,
      (LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N
```

## Two import fixes (against this Mathlib image)

1. `Mathlib.Data.Set.Finite` → `Mathlib.Data.Set.Finite.Basic`.
   `Set/Finite` is a *directory*; the module is `Finite.Basic`.
2. `Mathlib.Data.Matrix.Notation` → `Mathlib.Data.Fin.VecNotation`.
   The `![x, y]` (vecCons) notation lives in `Data/Fin/VecNotation.lean`,
   not in the matrix layer.

Both were previously mis-imported, so the file had never compiled. Now it does.

## Status of the statement itself

- `PlanarPolyField n` carries two `MvPolynomial (Fin 2) ℝ` with `totalDegree
  ≤ n` — the real degree-≤ n hypothesis, now definitional via `toMap`.
- `LimitCycleSet` is the set of limit-cycle *orbits*; `IsLimitCycle` is written
  by hand (Mathlib has `Flow`, `IsIntegralCurve`, discrete `IsPeriodicPt`, but
  no "isolated periodic orbit"/limit cycle).
- **Fixed this pass:** the previous `IsLimitCycle`'s periodicity clause
  `∃ T>0, ∀ t, γ(t+T)=γ t` is also satisfied by constant curves, so an isolated
  equilibrium (stable focus, saddle) would have qualified as a limit cycle and
  `h16_2` would bound equilibria, not limit cycles. The clause now requires the
  curve to be nonconstant as well: `∃ t₁ t₂, γ t₁ ≠ γ t₂`. The isolation clause
  ranges over nonconstant periodic solutions only (`δ` in the quantifier), so
  an equilibrium outside `U` cannot sabotage the witness.
- The theorem states finiteness (`Finite`) AND the cardinal bound (`ncard ≤ N`)
  together, closing the `Set.ncard`-of-an-infinite-set-is-0 vacuity hole.
- `#print axioms`: none (the only `sorry` is `h16_2`; the statement's lemmas
  introduce no axioms).

## Findings for Mathlib (reportable)

- No "limit cycle" / "isolated periodic orbit" notion — must be stated by hand.
- No packaged flow of a polynomial field as a `Flow ℝ Plane`.
- `Set/Finite` and the vector notation are at non-obvious import paths.
