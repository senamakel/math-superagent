# Novikov–Yakovenko, "Modules of Abelian integrals and Picard–Fuchs systems"

**Source**: arXiv:math/0110126v3 (published Nonlinearity 15 (2002) 1435–1450).
Held full text: `research/sources/novikov-yakovenko-modules-abelian-picard-fuchs.arxiv.full.md`
(URL: https://arxiv.org/pdf/math/0110126).
Claim: `h16-novikov-yakovenko-modules-picard-fuchs-2002`.

## What it establishes

For a bivariate polynomial `H` with nondegenerate highest homogeneous part
(regular at infinity):

- **Module isomorphism (Theorem 1 and preamble)**: the `C[t]`-module of relative
  cohomologies `Λ²/(dH ∧ Λ¹)` is isomorphic to the `C[t]`-module of Abelian
  integrals of polynomial 1-forms on the fibers `{H = t}`. This is the module-of-
  Abelian-integrals/Petrov-module structure that makes the whole Picard–Fuchs
  approach work.
- **Irredundant Picard–Fuchs system of rank μ**: for `ω₁,…,ω_μ` with
  `μ = tr D = Σᵢ deg ωᵢ/(n+1)` (n = deg H), whose `dωᵢ/(dx∧dy)` are linearly
  independent modulo the gradient ideal `⟨Hx, Hy⟩`, the period matrix `X(t)` is a
  nondegenerate solution of the first-order linear system
  `(∂/∂t + (B₀ + tB₁)⁻¹B₁) X = 0` — the *minimal* (irredundant) Picard–Fuchs
  system, whose dimension is the first Betti number of a generic fiber.
- **Period-matrix polynomiality (Corollary 1)**: `det X(t)` is a polynomial of
  degree `≤ m = tr D = Σ deg ωᵢ/(n+1)`.
- **Eigenvalue structure (Proposition 2 / Corollary 2)**: the matrix `A` is
  diagonalizable; its eigenvalues are exactly the **critical values of H** (with
  multiplicities), and the corresponding eigenvectors are the vanishing cycles.
- **Triangularity (Proposition 3)**: for homogeneous `dωᵢ` ordered by degree,
  `B₀` and `B₁` are lower triangular, the diagonal of `B₀` is `deg ωᵢ/deg H`,
  `B₁² = 0`, and `B₀ + tB₁` is invertible for **all** t.

## Why it matters for this run

This is the load-bearing existence/structure theorem for the **adopted approach**
(`abelian-picard-fuchs-argument-principle-sharp-count`) — the minimal rank-μ
linear ODE that the Abelian integrals of a named Hamiltonian family satisfy,
whose Wronskian/Chebyshev chain (GMV 2010/2011, held) reduces the transcendental
zero-count to a resultant/sign condition. The explicit rank formula
`μ = Σ deg ωᵢ/deg H` and the eigenvalue–critical-value correspondence are what
make the Picard–Fuchs system *writable by hand* for a concrete family: choose a
monomial basis, compute B₀, B₁ over Q, and the system is explicit. Previously the
library only cited this paper (Ilyashenko–Yakovenko lectures, BNY); now the
primary full text is held.

**Known limitation**: the isomorphism requires H regular at infinity with
nondegenerate highest homogeneous part. Degenerate / non-generic H (the
semiweighted-homogeneous-but-degenerate cases, iterated integrals) fall outside —
that is where GN 2008 (Gavrilov–Novikov, open period annuli) and the
Gavrilov–Iliev higher-variation work take over.