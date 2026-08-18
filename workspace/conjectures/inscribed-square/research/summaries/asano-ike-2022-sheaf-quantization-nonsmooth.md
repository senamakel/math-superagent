# Asano–Ike 2022 — Sheaf quantization and intersection for non-smooth objects

**Source:** Tomohiro Asano, Yuichi Ike, "Sheaf quantization and intersection of expandable objects," arXiv:2201.02598 (2022). Full text at [[research/sources/asano-ike-2022-sheaf-quantization-nonsmooth.full.md]].

## What it establishes

The technical foundation for the Asano–Ike 2024 rectifiable rectangular peg theorem. Develops microlocal sheaf theory (Tamarkin category) for **non-smooth limits of smooth objects**:

- **Theorem 1.1 (Corollary 4.5):** The Tamarkin category D(X) is complete with respect to the pseudo-distance d_D(X).
- **Theorem 1.2 (Theorem 5.11):** for compactly supported Hamiltonian diffeomorphisms φ, φ′ of T*M, d_D(M²)(K_φ, K_φ′) ≤ d_H(φ, φ′), where K_φ are GKS kernels and d_H is the Hofer metric. This is a stability result: Hamiltonian maps that are close in Hofer metric give sheaves that are close in the Tamarkin interleaving distance.
- **Consequence:** by completeness, a Cauchy sequence (φₙ) in the Hofer metric defines a limit object K_φ∞ ∈ D(M²) — a **sheaf quantization of a Hamiltonian homeomorphism** (a non-smooth object).
- **Theorem 1.3 (Theorem 6.5, Lusternik–Schnirelmann theory in microlocal sheaves):** a spectral/categorical criterion: if #Spec(F) ≤ cl(M), then some spectral value c has π_M(SS(F) ∩ Γ_dt ∩ π_t^{-1}(−c)) cohomologically non-trivial in M.
- **Theorem 1.4 (Theorem 7.1, Arnold-type):** for a compact exact Lagrangian L ⊂ T*M and a Hamiltonian homeomorphism φ∞, if the number of spectral invariants of φ∞(L) is < cl(M)+1, then 0_M ∩ φ∞(L) is cohomologically non-trivial, hence infinite.

## Why it matters here

- This is the machinery that lets the 2024 paper quantize *continuous* curves: the sheaf quantization of the smooth approximants converges in the Tamarkin category to a sheaf for the limit curve, **provided** the primitives of the Legendrian lifts converge uniformly (the continuous Legendrian lift condition of AI 2024 Theorem 1.1).
- The completeness + stability pair (Theorems 1.1 + 1.2) is exactly what turns a C⁰-limit of smooth curves into an object in the derived category; the "continuous Legendrian lift" hypothesis of AI 2024 is the specific convergence condition that makes Theorem 1.2 applicable.
- **Implication for the frontier:** the sharp question "does every Jordan curve admit a continuous Legendrian lift" is, in this language, whether every C⁰-limit of smooth curves has a convergent sequence of Legendrian-lift primitives. Non-rectifiable curves are the candidates for failure.

## Claims

```claim
id: asano-ike-2022-tamarkin-complete
statement: The Tamarkin category D(X) is complete with respect to the interleaving pseudo-distance d_D(X); Hamiltonian diffeomorphisms close in the Hofer metric quantize to sheaves close in d_D(M²).
status: asserted-by-source (peer-reviewed: published in a journal per the arXiv record's later history; as of this library, the arXiv text is the source)
evidence: Asano–Ike, arXiv:2201.02598, Theorems 1.1–1.2
holds-here: yes — the technical foundation that makes AI 2024's continuous-curve quantization work
falsifies: a failure of completeness or of the Hofer-stability inequality; a correction
anchor: research/sources/asano-ike-2022-sheaf-quantization-nonsmooth.full.md
```

```claim
id: asano-ike-2022-lift-convergence-role
statement: The continuous Legendrian lift condition of Asano–Ike 2024 (uniform convergence of the primitives fₙ of the smooth approximants) is exactly the hypothesis that makes the 2022 completeness+stability theorems applicable to a C⁰-limit of smooth curves; the sharp open question is whether every Jordan curve satisfies it.
status: sourced (this is the run's own synthesis of AI 2022 Theorems 1.1–1.2 with AI 2024 Theorem 1.1, both verified in full text)
evidence: arXiv:2201.02598 Theorems 1.1–1.2; arXiv:2412.21057 Theorem 1.1
holds-here: yes — names the precise analytic content of the frontier question
falsifies: a Jordan curve that admits a continuous Legendrian lift but whose smooth approximants fail the 2022 stability hypotheses, or vice versa
anchor: research/sources/asano-ike-2022-sheaf-quantization-nonsmooth.full.md
```
