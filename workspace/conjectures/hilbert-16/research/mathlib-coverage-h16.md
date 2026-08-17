# What Mathlib does and does not have for H16.2 (as of this run's Mathlib)

Checked against `/opt/mathlib4` on the fibre. Each is a finding about the
problem: a statement that cannot be typed yet is a reportable result.

## Present (usable)

- **Plane / vector fields.** `MvPolynomial (Fin 2) ℝ` with `totalDegree`
  (`Mathlib.Algebra.MvPolynomial.Degrees`, `def totalDegree : ℕ` at line 433)
  and pointwise evaluation `MvPolynomial.eval (fun i => x i) p`
  (`Mathlib.Algebra.MvPolynomial.Eval`, `def eval : (σ → R) →+* R`). A degree
  bound is `p.totalDegree ≤ n`. State: `PolynomialField n` carries `P Q` with
  `degP degQ`.
- **Real phase space.** `Fin 2 → ℝ` is a normed space / topological space over
  `ℝ`; no extra instance needed.
- **Integral curves.** `Mathlib.Analysis.ODE.Basic` has `IsIntegralCurveOn`,
  `IsIntegralCurveAt`, `IsIntegralCurve γ v : Prop` (global, over all of `ℝ`).
  Time-independent vector field: pass `fun _ x => v x`.
- **Periodic points (discrete).** `Mathlib.Dynamics.PeriodicPts.Defs` has
  `IsPeriodicPt f n x := f^[n] x = x` for a *self-map* `f`. Not directly usable
  for continuous-time periodic *orbits*; for those the statement in
  `Statement.lean` writes periodicity as `∀ t, f (t+T) = f t` with `0 < T`.
- **Set cardinality.** `Mathlib.Data.Set.Card` gives `Set.encard : ℕ∞` and
  `Set.ncard : ℕ` (`line 614`). `s.Finite ∧ s.ncard ≤ N` is the finiteness
  bound.
- **Neighbourhood of a set.** `Mathlib.Topology.Defs.Filter` gives `nhdsSet s`,
  notation `𝓝ˢ s`.

## Missing (each named; each is a gap)

- **Limit cycle** — no definition anywhere in the library. `Statement.lean`
  renders it as: periodic orbit whose image is separated from every other
  periodic-orbit image by an open set (isolation in the set of periodic
  orbits).
- **Return map / Poincaré map, displacement function** (the object the whole
  bifurcation theory of H16 is about) — absent. Would need a transversal +
  first-return time; requires existence+uniqueness of solutions on a compact
  transversal, then a definition of the return map as a self-map of the
  transversal.
- **Dulac function** (nonexistence certificate) — absent.
- **Polycycle, graphic, finite cyclicity, Bautin ideal, Abelian integral,
  Lyapunov quantity** — all absent; each would be its own definition file.
- **Bound: H(n) < ∞** — Mathlib has no notion; the bound is supplied by the
  `∃ N, ∀ F, … ≤ N` formulation in `h16_2`, which is the uniform statement.

No claim of any theorem rests on `Statement.lean` beyond elaboration: it has
one deliberate `sorry` (the conjecture itself) and depends only on `propext,
Classical.choice, Quot.sound, sorryAx`.
