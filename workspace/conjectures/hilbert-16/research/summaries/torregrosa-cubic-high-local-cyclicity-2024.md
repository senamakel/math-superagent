# Torregrosa, "Cubic planar vector fields with high local cyclicity" (São Paulo J. Math. Sci. 18, 2024, Sotomayor memorial)

<!-- source: https://link.springer.com/article/10.1007/s40863-024-00486-9 | converted from HTML. Full text: [[torregrosa-cubic-high-local-cyclicity-2024.full]]. Claim `h16-torregrosa-cubic-12-small-cycles-2024`. -->

## What it establishes — current best local (small-amplitude) lower bound M(3) ≥ 12

Two one-parameter cubic families whose perturbations create **twelve
small-amplitude limit cycles** from a single monodromic equilibrium, via
degenerate (higher-order) Hopf bifurcation.

**Theorem 1.1.** For α one of the two real simple roots of
`315α¹⁴+4144α¹²+4425α¹⁰−9630α⁸+1485α⁶+5580α⁴−1713α²−510 = 0`,
there exist cubic perturbations of the exhibited one-parameter cubic system (1)
such that **twelve** small-amplitude limit cycles bifurcate from the origin.

**Theorem 1.2.** For two values of β, cubic perturbations of system (2) produce
twelve small-amplitude cycles from the equilibrium
`(x₀,y₀) = ((32β²−75)/(6(8β²+25)), 35β/(3(8β²+25)))`.

## Evidence / how it is certified

All Lyapunov-coefficient computations are **exact polynomial arithmetic** (CAS);
the exceptional parameter values are located by **Sturm sequences** — so the
mathematical core is a finite, algebraic, reproducible statement (the degree-14 α
polynomial, the two systems, the equilibrium). This beats M(3) ≥ 11 (Żołądek) and
M(3) ≥ 12 is now the literature boundary for cubic focus cyclicity.

## Hypotheses / holds here

Planar cubic vector fields; small-amplitude (local) cycles about a single
monodromic equilibrium; perturbations of degree ≤ 3. **Holds here: yes** —
crosses GOAL's "twelfth small-amplitude cycle at a cubic focus" target. The α
polynomial and systems (1),(2) are Lean-statably checkable (finite algebraic
core: reproduce the focal coefficients, verify the degree-14 root, enumerate the
12 cycles — all `decide`/interval-certifiable).

**Evidence class: sourced** (open-access full text held,
DOI 10.1007/s40863-024-00486-9).

## Bearing / implication

- M(3) ≥ 12 is a concrete bound any upper-bound claim about M(n) must clear.
- The clean-room re-derivation of the Lyapunov constants for systems (1),(2) is
  an explicitly named verification task (falsifier in the claim).
- Local cyclicity 12 at a cubic focus is the sharpest local bound in the library;
  the Bautin-ideal / Lyapunov-quantity instrumentation here is exactly what the
  run's oracle (GOAL step 4) is meant to reproduce at smaller scale (M(2)=3)
  before trusting past it.
