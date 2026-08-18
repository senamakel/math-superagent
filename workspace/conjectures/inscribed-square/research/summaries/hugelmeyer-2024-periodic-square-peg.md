# Hugelmeyer 2024 — A Solution to the Periodic Square Peg Problem

**Source:** Cole Hugelmeyer, arXiv:2407.20412 [math.SG], submitted 29 Jul 2024. Full text: `research/sources/hugelmeyer-2024-periodic-square-peg.full.md`.

**Status: verified against full text on disk. Not yet peer-reviewed as far as this library knows (arXiv preprint).**

## What it establishes

The **periodic square peg problem** — the variant Tao (2017) singled out as *not subject to arbitrarily small squares* — is **resolved**.

**Theorem 1 (Periodic Square Peg Problem).** Suppose f, g : ℝ → ℝ² are injective continuous functions with disjoint images, satisfying f(x+1) = f(x) + (0,1) and g(x+1) = g(x) + (0,1) for all x. Then im(f) ∪ im(g) contains four distinct points forming the corners of a square in the plane.

**Theorem 2 (smooth case).** Let f, g be smooth embeddings S¹ → ℂ/ℤ[i], both isotopic to the circle ℝ/ℤ, with disjoint images. Then there exist a₁, a₂, b₁, b₂ ∈ S¹ such that
f(a₂) = f(a₁) + i·(g(b₁) − f(a₁)) and g(b₂) = g(b₁) + i·(g(b₁) − f(a₁)).

## The mechanism (why it matters for this run)

- Inscribed squares are intersections between the Lagrangian torus f×g and its image τ(f×g) under the symplectomorphism τ(a,b) = (a+i(b−a), b+i(b−a)) of the symplectic 4-torus ((ℂ/ℤ[i])², ω±).
- **Non-displaceability** is proved by a 4-fold covering argument reducing to circle-pair Floer homology in 2-tori: dim HF(m×p, m×q; Λ) = 2·2 = 4 ≠ 0.
- Theorem 1 follows from Theorem 2 by **C⁰ approximation with an explicit side-length lower bound**: ε = inf d(f_n(x), g_n(y)) > 0 from the disjointness of the images, so the inscribed squares on approximants have side ≥ ε and a compactness limit is **non-degenerate**.
- **This is the same anti-shrinkout mechanism as Stromquist's Theorem 3.36** (via the Rius Casado thesis): a *parameter-space or scale certificate* precludes collapse of the limiting square.

## Claim blocks

```claim
id: hugelmeyer2024-periodic-square-peg
statement: If f, g : ℝ → ℝ² are injective continuous, im f ∩ im g = ∅, f(x+1) = f(x)+(0,1), g(x+1) = g(x)+(0,1), then im(f) ∪ im(g) contains the four vertices of a plane square.
hypotheses: f, g injective continuous; disjoint images; period 1 with vertical (0,1) translation.
holds-here: The periodic setting, not the plain Jordan-curve setting; a solved variant of the square peg problem.
evidence: full text verified (arXiv:2407.20412); Lagrangian Floer homology, non-displaceable tori.
status: theorem (arXiv preprint, not yet peer-reviewed as far as this library knows)
falsifies: a counterexample pair of periodic disjoint curves without an inscribed square; or a published retraction/error in the Floer computation.
```

```claim
id: hugelmeyer2024-shrinkout-scale-certificate
statement: In the periodic square peg problem the inscribed square can be chosen non-degenerate because the disjointness of the two periodic curves provides a positive lower bound on side length (ε = inf distance), inherited by the C⁰ approximants.
hypotheses: same as the periodic theorem.
holds-here: Demonstrates a scale certificate in a setting without shrinkout; pattern for the general problem.
evidence: full text, proof of Theorem 1.
status: theorem (as part of the preprint)
falsifies: a periodic pair whose only inscribed squares have side length → 0.
```

## Why this source entered the library

Tao (2017) identified the periodic variant as one *not subject to the shrinkout problem* — the same obstruction that blocks the general conjecture. Its resolution (Hugelmeyer 2024) confirms that the periodic setting has an independent scale certificate, and the Floer method here is the same family of techniques (Greene–Lobb, Asano–Ike) the library already tracks. This is a solved *adjacent problem* whose mechanism is directly relevant to the run's central obstruction.

## Citations of interest (added to frontier)

Fukaya–Oh–Ohta–Ono (Lagrangian intersection Floer theory); Greene–Lobb 2021 (Annals); Greene–Lobb 2023 (Invent.); Griffiths 1991 (PLMS); Greene–Lobb 2024 (Floer homology and square pegs); Greene–Lobb 2024 (square pegs between two graphs); Matschke 2014 survey; Tao 2017.
