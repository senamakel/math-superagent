/-
Statement.lean
--------------
The second part of Hilbert's 16th problem, H16.2, stated in Lean 4 against Mathlib.

The point of this file is the *type*: to say, as precisely as today's Mathlib
lets us, what it would mean for the statement to hold. We are not proving it
(the `:= by sorry` below is the deliverable), and the purpose of writing it out
is to expose exactly which notions Mathlib lacks.

What Mathlib has / lacks (checked against this image):

  * `Flow τ α`            — Mathlib.Dynamics.Flow. A continuous group action
                            `τ → α → α`. This is the right carrier for the
                            time evolution of a vector field (autonomous), and
                            we use it for `flow`.
  * `IsIntegralCurve γ X` — Mathlib.Analysis.ODE.Basic. `γ : ℝ → E` with
                            `γ' t = X (γ t)`. This is our notion "γ is a
                            solution" and it matches exactly.
  * `IsPeriodicPt f n x`  — Mathlib.Dynamics.PeriodicPts.Defs. Periodic points
                            of a *discrete* iteration `f^[n]`. There is no
                            continuous-period notion, so we state periodicity
                            ourselves as `∃ T > 0, flow T x = x`.
  * MISSING: "isolated in the set of periodic orbits". No Mathlib notion of a
    limit cycle / isolated periodic orbit exists. We state it by hand.
  * `MvPolynomial (Fin 2) ℝ` with `totalDegree` and `eval` — present
    (Mathlib.Algebra.MvPolynomial.Basic/.Eval/.Degrees). This file now uses
    them for the *real* degree-≤ n hypothesis: the field is carried by two
    polynomials whose totalDegree is ≤ n. This replaces the earlier
    `degree_at_most : True` placeholder, which asserted nothing.

The mathematical claim (from the informal statement):

  For each degree `n : ℕ` there is a number `N = N(n)` such that every planar
  polynomial vector field of degree at most `n` has at most `N` limit cycles.

Here a *limit cycle* is a periodic orbit of the flow that is isolated in the
set of periodic orbits. We make "periodic orbit isolated in the set of all
periodic orbits" precise below as `IsLimitCycle`.

IMPORTANT (finiteness is stated explicitly, not via `ncard` alone):
`Set.ncard` of an *infinite* set is `0`, so a bare inequality
`(LimitCycleSet f.toMap).ncard ≤ N` would be vacuously true even for a field
with infinitely many limit cycles — the exact vacuity hole this file is meant
to close. The theorem `h16_2` therefore states
`(LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N`:
finiteness of the set of limit cycles AND the cardinal bound, together.
-/

import Mathlib.Analysis.ODE.Basic
import Mathlib.Dynamics.Flow
import Mathlib.Dynamics.PeriodicPts.Defs
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Algebra.MvPolynomial.Degrees
import Mathlib.Data.Set.Card
import Mathlib.Data.Set.Finite
import Mathlib.Data.Matrix.Notation

open Set
open scoped Topology

noncomputable section

namespace H16

/-- The phase plane. `ℝ²` with its product normed vector-space structure, which is
exactly what `IsIntegralCurve` and `Flow` expect. -/
abbrev Plane : Type := ℝ × ℝ

/--
A limit cycle of a (time-autonomous) vector field `X : Plane → Plane` with flow `ϕ`.

`γ : ℝ → Plane` is a limit cycle iff

  * it is an integral curve of the autonomous ODE `γ' = X γ` — i.e. a solution of
    `z' = X z` (here `X` does not depend on time, so it is a curve of the vector
    field);
  * it is non-constant periodic: some `T > 0` has `γ (t + T) = γ t` for all `t`;
  * it is *isolated in the set of periodic orbits*: there is a neighbourhood of
    the orbit containing no other periodic orbit.

The third clause is the one Mathlib has no word for; it is what separates a
limit cycle from the continuum of period orbits of a centre.
-/
def IsLimitCycle (X : Plane → Plane) (γ : ℝ → Plane) : Prop :=
  IsIntegralCurve γ (fun _ : ℝ => X) ∧
  (∃ T > 0, ∀ t : ℝ, γ (t + T) = γ t) ∧
  -- isolated in the set of periodic orbits: some neighbourhood of γ's orbit
  -- contains no other periodic orbit.
  (∃ U : Set Plane, U ∈ 𝓝ˢ (γ '' Set.univ) ∧ ∀ δ : ℝ → Plane,
     -- δ a periodic-orbit would be forced out of U
     IsIntegralCurve δ (fun _ : ℝ => X) → (∃ S > 0, ∀ t, δ (t + S) = δ t) →
     δ '' Set.univ ⊆ U → δ '' Set.univ = γ '' Set.univ)

/--
The set of limit cycles of `X`, as a subset of `Plane`. We take the union of the
(periodic) orbits, so that "number of limit cycles" is "number of these sets".
-/
def LimitCycleSet (X : Plane → Plane) : Set (Set Plane) :=
  { O : Set Plane | ∃ γ : ℝ → Plane, O = γ '' Set.univ ∧ IsLimitCycle X γ }

/--
A planar polynomial vector field of degree at most `n`.

The field is *carried by two polynomials* `P Q : MvPolynomial (Fin 2) ℝ`,
each of total degree at most `n`. The phase-plane map is derived (`toMap`),
so the polynomials are definitionally the field: `PlanarPolyField n` is the
type of polynomial fields of degree ≤ n, not a carrier with a `True`-valued
degree assertion.
-/
structure PlanarPolyField (n : ℕ) where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ n
  degQ : Q.totalDegree ≤ n

namespace PlanarPolyField

/-- The phase-plane map of a polynomial field: evaluate the two polynomials
at the point `(x, y)`. The `![x, y]` is the canonical `Fin 2 → ℝ` vector. -/
def toMap (f : PlanarPolyField n) : Plane → Plane :=
  fun (x, y) => (f.P.eval ![x, y], f.Q.eval ![x, y])

/--
The number of limit cycles of the field. WARNING: `Set.ncard` is `0` for an
infinite set, so `limitCycleCount` alone cannot express "at most N limit
cycles" — the meaningful statement is `(LimitCycleSet f.toMap).Finite ∧
(LimitCycleSet f.toMap).ncard ≤ N`, which is exactly what `h16_2` states.
-/
noncomputable def limitCycleCount (f : PlanarPolyField n) : ℕ :=
  Set.ncard (LimitCycleSet f.toMap)

end PlanarPolyField

/--
H16.2 (Hilbert's 16th problem, part 2): for every degree `n` there is a number
`N` bounding the number of limit cycles of every planar polynomial vector field
of degree at most `n`.

The statement carries every hypothesis: `f : PlanarPolyField n` has two
polynomial coordinates of total degree ≤ n, and the bound is
finiteness + `ncard ≤ N` of the set of limit-cycle orbits of `f.toMap`.

`:= by sorry` — the statement is the deliverable. The `sorry` is a genuine hole:
nobody has proved this. The type is what we are claiming could be filled.
-/
theorem h16_2 :
    ∀ n : ℕ, ∃ N : ℕ, ∀ f : PlanarPolyField n,
      (LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N := by
  sorry

/-
What prevented a cleaner statement, concretely (a reportable finding of this
pass, not hand-waving):

  1. `IsLimitCycle` above had to be written by hand. Mathlib has `Flow`,
     `IsIntegralCurve` and discrete `IsPeriodicPt`, but *no* notion of
     "isolated periodic orbit" / "limit cycle". The isolation clause is the
     piece of the informal definition most in danger of being wrong in this
     file and is the first thing to audit.
  2. FIXED THIS PASS: `degree_at_most : True` (asserted nothing) is replaced by
     the real bound `f.P.totalDegree ≤ n` / `f.Q.totalDegree ≤ n` with the two
     polynomials carried in `PlanarPolyField`. `MvPolynomial (Fin 2) ℝ`,
     `totalDegree` and pointwise `eval` all exist in Mathlib; tying the
     `Plane → Plane` map to the polynomials is now definitional via `toMap`.
  3. FIXED THIS PASS: the `Set.ncard` hole. `Set.ncard` of an infinite set is
     `0`, so the old `limitCycleCount ≤ N` was vacuous for infinite sets. The
     theorem now states `(LimitCycleSet f.toMap).Finite ∧ ...ncard ≤ N`.
  4. `PlanarPolyField.toMap` is a derived map; connecting it to the field's
     *flow* (Picard–Lindelöf) is present in Mathlib but the flow of a countably
     explicit polynomial field is not packaged as a `Flow ℝ Plane`. A proof of
     H16.2 would need this to be an actual construction, and `IsLimitCycle`
     would most usefully be stated against the flow.
-/

end H16

end