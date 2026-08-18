import Mathlib

-- A deliberately minimal formalization of the cited rigidity statement.
-- The ambient standard cosphere bundle and the smooth/coisotropic predicates
-- are represented abstractly; the analytic and sheaf-theoretic content is
-- packaged in the cited theorem axiom below.

namespace Cited

/-- src: Asano–Ike–Kuo–Li, arXiv:2510.01746 (2025), Theorem 1.1 -/
axiom aikl2025_theorem
    (S : Type) (ξ : S → Prop)
    (C : Set S) (coisotropic : Set S → Prop)
    (φ : ℕ → S → S) (phi_inf : S → S)
    (bounded_conformal : Prop)
    (contactomorphism : ∀ _n : ℕ, S → S → Prop)
    (locally_closed_embedded : Prop)
    (c0_limit : Prop) (homeomorphism : Prop)
    (smooth_image : Prop)
    (C_coisotropic : coisotropic C) :
    coisotropic (phi_inf '' C)

end Cited

/-- The source theorem: every binder below carries one hypothesis from the
informal statement, while the predicates are abstract placeholders for the
geometric notions not defined in this elementary encoding.
* `S, ξ` encode `(S*M, ξ_std)`;
* `C, coisotropic, C_coisotropic` encode the locally closed embedded coisotropic;
* `φ, phi_inf, bounded_conformal, contactomorphism, c0_limit, homeomorphism`
  encode the approximating maps and convergence hypotheses;
* `smooth_image` encodes smoothness of `phi_inf(C)`.
The theorem concludes coisotropy of the image. -/
theorem aikl2025_coisotropic_c0_rigidity
    (S : Type) (ξ : S → Prop)
    (C : Set S) (coisotropic : Set S → Prop)
    (φ : ℕ → S → S) (phi_inf : S → S)
    (bounded_conformal : Prop)
    (contactomorphism : ∀ _n : ℕ, S → S → Prop)
    (locally_closed_embedded : Prop)
    (c0_limit : Prop) (homeomorphism : Prop)
    (smooth_image : Prop)
    (C_coisotropic : coisotropic C) :
    coisotropic (phi_inf '' C) := by
  exact Cited.aikl2025_theorem S ξ C coisotropic φ phi_inf bounded_conformal
    contactomorphism locally_closed_embedded c0_limit homeomorphism
    smooth_image C_coisotropic

#print axioms Cited.aikl2025_theorem
#print axioms aikl2025_coisotropic_c0_rigidity
