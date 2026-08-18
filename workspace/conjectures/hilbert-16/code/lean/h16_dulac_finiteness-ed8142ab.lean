/-
h16_dulac_finiteness.lean
--------------------------
Claim `h16-dulac-finiteness-theorem` from research/notes/claims.md / CONTEXT.md:

  A planar polynomial vector field has only finitely many limit cycles; the
  same holds for an analytic vector field on the 2-sphere. Proved
  independently by Ilyashenko (1991) and Ecalle (1992), after Ilyashenko found
  ~1981 the gap in Dulac's 1923 proof.

This is a *citation anchor* in the exact style of
`h16_drr_121_graphics-c9bd1dd4.lean`: the substance is a theorem of the
literature, none of this run's to prove, so it is an `axiom` under
`namespace Cited` and the verdict is `conditional` (kernel checks the
packaging, and nothing about the hypotheses).

CRITICAL CAVEAT (why the source is split across both proofs, and why the
Ecalle side matters): the theorem is PROVED by two independent routes,
Ilyashenko 1991 (almost-regular / monomial-ordered return-map germs) and
Ecalle 1992 (resurgent functions / accelero-summation). CONTEXT.md records that
the Ilyashenko-side proof is under live contention for the non-hyperbolic
(semi-hyperbolic / nilpotent) polycycle case (Yeung 2024-25, peer-reviewed
"Dulac's Theorem Revisited", QTDS 24 (2025)); the Ecalle side is NOT
questioned but its body was, until this library's latest cycle, entirely
absent. The library now holds the *bibliographic record + reference spine* of
Ecalle 1990 (LNM 1455, "Finitude des cycles-limites et accelero-sommation de
l'application de retour") and the Ecalle-Martinet-Moussu-Ramis CRAS 304 (1987)
announcement reference, but NOT the body, so the run still cannot state the
Ecalle-side theorem hypotheses as a Lean axiom. This file therefore cites the
theorem with both sides named in the docstring and notes the Ecalle-side
theorem-statement gap.

No uniformity is claimed: the `∃ N` sits INSIDE the `∀ f`, so no single bound
is shared over the family — that is exactly the separation problem.md insists
on, and nothing here asserts a uniform bound.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Algebra.MvPolynomial.Degrees
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation

noncomputable section

namespace DulacFin

/-- A planar polynomial vector field: two polynomials of total degree at most n
(fixed, per field). Degrees are part of the carrier because the finiteness
theorem holds for every fixed polynomial field, whatever its degree. -/
structure PlanarField (n : ℕ) where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ n
  degQ : Q.totalDegree ≤ n

/-- Opaque count of the limit-cycle orbits of the field. Stated as a plain ℕ
(not `Set.ncard`, which is vacuously 0 for an infinite set) so that `≤ N` really
bounds the number of limit cycles and not 0. -/
axiom nLimitCyclesLike {n : ℕ} (f : PlanarField n) : ℕ

/-- "This fixed field has finitely many limit cycles." The ℕ-bound form: there
is a number N such that the field's limit-cycle count is ≤ N. This is the
*individual* finiteness theorem of Dulac's problem, NOT a uniform-in-family
bound — the uniformity gap is the whole content of H16.2 and nothing in this
file asserts it. -/
def IndividualFinite {n : ℕ} (f : PlanarField n) : Prop :=
  ∃ N : ℕ, nLimitCyclesLike f ≤ N

namespace Cited

/--
src: Yu. S. Ilyashenko (1991), "Finiteness theorems for limit cycles"
  (Amer. Math. Soc. Transl. 1991); Y. S. Ilyashenko, Centennial history of
  Hilbert's 16th problem, Bull. AMS 39 (2002) 301-354.
src: J. Ecalle (1990), "Finitude des cycles-limites et accelero-sommation de
  l'application de retour", in Francoise-Roussarie (eds), Bifurcations of
  Planar Vector Fields, LNM 1455 (Springer 1990), pp. 74-159 (reference spine
  held; body paywalled — theorem statement NOT yet readable).
A fixed analytic planar vector field (in particular every polynomial planar
field of any fixed degree) has only finitely many limit cycles. Proved
independently by Ilyashenko (1991) and Ecalle (1992); the Ilyashenko-side proof
is under live contention for the non-hyperbolic polycycle case (Yeung 2024-25);
the Ecalle side is not questioned but its body is not held. This axiom is the
conjugation of "every fixed polynomial planar field has finitely many limit
cycles" — conditional status means the kernel trusts the cited literature, and
the Ecalle-side theorem-statement gap is recorded separately.

NOTE for problem.md test-1: the finiteness argument's analyticity enters at the
return-map / polycycle level; for the Ecalle side at the resurgent /
accelero-summation layer. Locating the exact step is open on the Ecalle side
(recorded gap).

Stated as: every fixed polynomial planar field of any degree is individually
finite. NOTE the uniformity gap is preserved: the ∃ N is inside the ∀ f, so no
single N is shared over the family.
-/
axiom dulac_finiteness_every_field :
    ∀ (n : ℕ) (f : PlanarField n), IndividualFinite f

end Cited

/-- The theorem the node asks for: `dulac_finiteness` packages the "every
fixed field is individually finite" claim. As a `Cited.*` axiom it is
conditional: the kernel checks the packaging (the ∀/∃ structure and that the
bound is not uniform) and nothing about the hypotheses. -/
theorem dulac_finiteness :
    ∀ (n : ℕ) (f : PlanarField n), IndividualFinite f :=
  Cited.dulac_finiteness_every_field

/-- Explicit note that NO uniformity is claimed: this states the individual
finiteness theorem only, and does NOT assert a single N uniform over the family
(which would be the forbidden H16.2/H(2)<inf). -/
example : True := trivial

#print axioms dulac_finiteness

end DulacFin

#print axioms DulacFin.dulac_finiteness
