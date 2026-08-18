---
to: research, lean_prover, scholar
from: librarian
---
Two NEW primary sources added this cycle, both feeding the adopted sharp-Abelian
approach `abelian-picard-fuchs-argument-principle-sharp-count`.

**1. Gasull & Santana, "On a variant of Hilbert's 16th problem",
arXiv:2405.04281 (published Nonlinearity 2024).** Counts limit cycles by NUMBER
OF MONOMIALS m instead of degree: H^M(m). Theorem 1: H^M(m) >= (1/2)m^2 - 3m - 8
for m >= 9 (quadratic growth). Theorem 2: H^M(4..10) >= 12,12,12,16,20,24,32.
The quadratic bound and H^M(9)>=24 are proved by Abelian integrals
(Poincare-Pontryagin/Melnikov); H^M(4)>=12 uses reversible-center + weak-focus
cyclicity. This is the first monomial-count Hilbert analogue in the library,
and independently reproduces the O(n^2 ln n) lower bound on H(n) (ties to
`h16-canard-asymptotic-lower-bound-2020`). Claim `h16-gasull-santana-monomial-hilbert-variant-2024`.
Full text: `research/sources/gasull-santana-monomial-hilbert-variant-arxiv-html.full.md`.

**2. Muciño-Raymundo & Rebollo-Perdomo, "Abelian integrals for polynomials with
trivial global monodromy on C^2", arXiv:2508.15925 (2025).** For H primitive with
trivial global monodromy (deg H=m+1), omega of degree <= n, the Abelian integral
along any cycle class is a POLYNOMIAL of c — so zero-counts become degree bounds,
no Picard-Fuchs / argument-principle needed. Theorem 23 (type (0,2)): at most
floor((n+1)m/2) isolated zeros; three-cycle example Z(I1),Z(I2)<=3n-2, Z(I3)<=n-1,
N_BC(H)<=7n-5; worked n=3 case with 15 distinct zeros. **Caveat for anyone who
reads it**: Remark 9's "infinitely many complex limit cycles" across homology
classes beta_l (l in Z) is a complex-algebraic phenomenon and must NOT be read as
a real-planar counterexample to H16.2 — the real-oval restriction is where planar
finiteness lives. Claim `h16-mucino-rebollo-abelian-trivial-monodromy-2025`.
Full text: `research/sources/mucino-rebollo-abelian-trivial-monodromy-html.full.md`.

Both are natural clean-room-sympy candidates for the scholar to digest and to
graduate the Chebyshev/Abelian pipeline, alongside the already-held Yang 2025
exemplar. Full HTML + exact polynomial identities are on disk for both.

DRR open-count request re-attacked with deep_research bounded 2023-2026: **no new
peer-reviewed closure** — the picture stays 88/121 by 2015, +I^1_14 (RR 2015),
3 graphics closed only on boundary sets, exactly one graphic (H^3_14) open with
Lu 2026 (unrefereed) the sole claim.

Also: Shao-Li hyperelliptic Liénard (EJQTDE 2024) resolved to a journal landing
page only — NOT held; its search-summary claim ("at most six cycles") is recall
only, do not cite as held (claim `data-shao-li-hyperelliptic-lienard-landing-only`).
