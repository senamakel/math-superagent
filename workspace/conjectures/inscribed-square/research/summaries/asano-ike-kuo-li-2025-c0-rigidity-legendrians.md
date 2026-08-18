# Asano–Ike–Kuo–Li 2025 — C⁰-rigidity of Legendrians and coisotropics via sheaf quantization

**Source:** Tomohiro Asano, Yuichi Ike, Christopher Kuo, Wenyuan Li, "C⁰-rigidity of Legendrians and coisotropics via sheaf quantization," arXiv:2510.01746 [math.SG], 2 Oct 2025. Full text: `research/sources/asano-ike-kuo-li-2025-c0-rigidity-legendrians.full.md`.

## What it establishes

Rigidity of contact topology under the C⁰-topology, proved with microlocal sheaf theory (Guillermou–Kashiwara–Schapira quantization, interleaving distances):

- **Theorem 1.1 (coisotropic rigidity).** In the standard cosphere bundle (S*M, ξ_std), let C ⊆ S*M be a locally closed embedded coisotropic. Let φₙ ∈ Cont(S*M, ξ_std) have bounded conformal factor hₙ, φₙ → φ∞ in C⁰, φ∞ a homeomorphism. If φ∞(C) is smooth, then φ∞(C) is still coisotropic.
- **Theorem 1.4 (Legendrian rigidity, Maslov data).** Same setting with Λ ⊆ S*M a locally closed embedded Legendrian and φₙ in the identity component Cont₀. If φ∞(Λ) is smooth, the composition of the Lagrangian Gauss map and the delooping of the J-homomorphism is preserved.
- **Theorem 1.7.** For a proper Legendrian Λ, the sheaf category with singular support on Λ and the microstalk corepresentative are preserved under such C⁰-limits (and hence the wrapped Floer cochains of linking disks).
- **Theorem 1.11.** (Shelukhin; Dimitroglou Rizell–Sullivan, recast): the Hofer–Shelukhin distance d_HS is a non-degenerate metric on Cont₀(S*M); the Chekanov–Hofer–Shelukhin distance is non-degenerate on Leg₀(Λ) when Sh_Λ(M) is non-trivial.
- **Theorem 1.14.** For a complete Riemannian M with a contact form α whose Reeb flow is a positive Hamiltonian with positive lower bound and finite C¹-norm: there is ε > 0 and C_α > 0 such that every contactomorphism φ with d_C⁰(id, φ) < ε has a canonical sheaf quantization K_φ.

## Relation to this run's thesis (the Legendrian-lift frontier)

This paper is **adjacent to, but does NOT settle**, the sharp open question separating Asano–Ike 2024's solved class (curves with a continuous Legendrian lift) from the general Toeplitz conjecture. The theorems here are **rigidity statements about C⁰-limits whose images are assumed smooth** — they say "if the limit image of a Legendrian/coisotropic is smooth, it retains the structure." They do **not** say "every wild Jordan curve admits a continuous Legendrian lift," nor do they produce lifts for non-rectifiable curves. The bounded-conformal-factor hypothesis (hₙ bounded) is an extra regularity assumption on the approximating contactomorphisms that the Asano–Ike 2024 lift condition does not require in the same form. So:

- The frontier question **remains open**: does every Jordan curve admit a continuous Legendrian lift?
- The value of this source is methodological: it extends the microlocal-sheaf toolbox (interleaving distances, GKS quantization of C⁰-small contactomorphisms) that Asano–Ike 2024's proof rests on, and it confirms the same school of methods continues to develop. A Lean formalization of Asano–Ike's Theorem 1.1 would cite this paper for the sheaf-quantization foundations only.

## Claim blocks

```claim
id: aikl2025-coisotropic-c0-rigidity
statement: In the standard cosphere bundle, a C⁰-limit φ∞ of contactomorphisms φₙ (bounded conformal factor) sends a locally closed embedded coisotropic C to a coisotropic, provided φ∞(C) is smooth.
hypotheses: (S*M, ξ_std); C coisotropic; φₙ ∈ Cont with bounded conformal factor; φₙ → φ∞ in C⁰; φ∞ homeomorphism; φ∞(C) smooth.
holds-here: method-adjacent only — it does not bear directly on whether a given Jordan curve has a continuous Legendrian lift; it concerns rigidity of limits whose images are smooth.
evidence: full text verified (arXiv:2510.01746, Theorem 1.1); sheaf-theoretic proof via GKS quantization and interleaving distance continuity.
status: theorem (arXiv preprint, Oct 2025)
falsifies: an explicit sequence of contactomorphisms with bounded conformal factor converging in C⁰ to a homeomorphism sending a coisotropic to a smooth non-coisotropic; or a published error in the sheaf-quantization argument.
```

```claim
id: aikl2025-legendrian-rigidity-maslov
statement: Under the same C⁰-limit hypotheses (identity component, bounded conformal factor), if the image of a Legendrian Λ is smooth then the Lagrangian Gauss map/J-homomorphism composition and the sheaf category with singular support on Λ are preserved.
hypotheses: (S*M, ξ_std); Λ Legendrian; φₙ ∈ Cont₀ bounded conformal factor; φₙ → φ∞ in C⁰; φ∞(Λ) smooth.
holds-here: method-adjacent; part of the same microlocal toolbox Asano–Ike 2024 uses, but does not address existence of lifts for wild curves.
evidence: full text verified (arXiv:2510.01746, Theorems 1.4, 1.7).
status: theorem (arXiv preprint)
falsifies: a C⁰-limit of identity-component contactomorphisms (bounded conformal factor) whose smooth Legendrian image has different Maslov data; or a published error.
```

```claim
id: aikl2025-legendrian-lift-frontier-still-open
statement: Asano–Ike–Kuo–Li 2025 does not settle whether every Jordan curve admits a continuous Legendrian lift; the frontier question separating Asano–Ike 2024's rectifiable class from the general Toeplitz conjecture remains open.
hypotheses: none — a status statement about the literature.
holds-here: yes — confirms the run's standing thesis `legendrian-lift-frontier` is not refuted by 2025 work from the same school.
evidence: full text verified — the theorems concern C⁰-limits with smooth images, not lift existence for arbitrary curves; bounded-conformal-factor hypotheses differ from the AI 2024 lift condition.
status: sourced claim (absence-of-result in a verified full text)
falsifies: a statement in this paper producing a continuous Legendrian lift for every Jordan curve.
```
