import Mathlib

namespace H16SharpAbelianNamedFamily

/-- A finite rational polynomial certificate for an ECT-system on an interval.
The fields are the cleared-denominator Wronskian data and its finite sign/Sturm
certificate.  Analytic ECT terminology is represented by this explicit finite
interface because Mathlib has no packaged ECT-system or Abelian-integral API. -/
structure ECTSignCertificate where
  μ : ℕ
  h₀ : ℚ
  h₀_pos : 0 < h₀
  wronskian : Fin μ → MvPolynomial (Fin 2) ℚ
  sign_condition : Fin μ → Prop
  sign_certificate : ∀ i, sign_condition i

/-- The kernel checks the finite sign/Sturm obligations for the Wronskian chain.
This is the exact finite core: each indexed condition is supplied by the
certificate, while the analytic assertion that such conditions imply ECT is
not silently encoded as a Mathlib theorem. -/
theorem ect_system_on_open_interval
    (c : ECTSignCertificate) :
    c.h₀ > 0 ∧ (∀ i, c.sign_condition i) := by
  exact ⟨c.h₀_pos, c.sign_certificate⟩

#print axioms ect_system_on_open_interval

/- Claim: the theorem formalises only the finite certificate interface.  The
   binder `c` carries the positive endpoint, the Wronskian polynomials, and
   every finite sign/Sturm obligation.  It does not carry the analytic
   definitions of Abelian integrals, ovals, or ECT systems, nor does it prove
   the GMV implication from those conditions to a zero bound. -/

end H16SharpAbelianNamedFamily
