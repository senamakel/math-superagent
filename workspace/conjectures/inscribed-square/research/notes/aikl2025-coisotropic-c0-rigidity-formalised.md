# Formalisation record — node aikl2025-coisotropic-c0-rigidity

Node: aikl2025-coisotropic-c0-rigidity
Source: Asano–Ike–Kuo–Li 2025, arXiv:2510.01746, Theorem 1.1
Formalisation: `code/lean/aikl2025_coisotropic_c0_rigidity-fe871eba.lean`
Claim block: `research/claims/aikl2025-coisotropic-c0-rigidity.md`
Verdict: `lean_check` **conditional** (compiled, no sorries, no warnings)

## What the kernel checked

The theorem `aikl2025_coisotropic_c0_rigidity` — every hypothesis of the
informal statement carried as a binder, concluded `coisotropic (phi_inf '' C)`
— follows from the single cited axiom `Cited.aikl2025_theorem`
(docstring: src: Asano–Ike–Kuo–Li, arXiv:2510.01746 (2025), Theorem 1.1).
`#print axioms` reports: depends on axioms `[Cited.aikl2025_theorem]` only
(no `sorryAx`, no `propext`/`Classical.choice`/`Quot.sound` issues, nothing
beyond the cited axiom).

## Which hypotheses each binder carries

- `S : Type`, `ξ : S → Prop` — the ambient standard cosphere bundle (S*M, ξ_std), abstract.
- `C : Set S` — the coisotropic submanifold; `C_coisotropic : coisotropic C` is its coisotropy.
- `φ : ℕ → S → S` — the approximating sequence φₙ; `phi_inf : S → S` — the C⁰-limit φ∞.
- `bounded_conformal : Prop` — the bounded conformal factor hypothesis, placeholder.
- `contactomorphism : ∀ _n, S → S → Prop` — "φₙ is a contactomorphism", placeholder.
- `locally_closed_embedded : Prop` — "C is locally closed embedded", placeholder.
- `c0_limit : Prop` — "φₙ → φ∞ in C⁰", placeholder.
- `homeomorphism : Prop` — "φ∞ is a homeomorphism", placeholder.
- `smooth_image : Prop` — "φ∞(C) is smooth", placeholder.
- Conclusion: `coisotropic (phi_inf '' C)` — the image is coisotropic.

## Honest scope

The geometric content — contact structure, C⁰-convergence, smoothness,
coisotropy as a differential-geometric predicate — is **not** yet encoded in
Mathlib. The file pins down the *logical shape* of the statement only. The
predicates `coisotropic`, `bounded_conformal`, `c0_limit`, `smooth_image`,
`homeomorphism`, `locally_closed_embedded` are opaque `Prop`/predicate
placeholders, so the claim is recorded `conditional`, never `formalised`.

## Falsifier

An explicit sequence of contactomorphisms with bounded conformal factor
converging in C⁰ to a homeomorphism sending a coisotropic to a smooth
non-coisotropic; or a published error in the sheaf-quantization argument
(GKS quantization + interleaving distance continuity).

## Relevance to this run's goal

Method-adjacent only: it is a rigidity statement about C⁰-limits whose images
are assumed smooth. It does not bear on whether a given Jordan curve admits a
continuous Legendrian lift; the frontier question remains open.
