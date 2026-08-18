# Rousseau & Zhu, "PP-graphics with a nilpotent elliptic singularity in quadratic systems and Hilbert's 16th problem" (JDE 196, 2004, 169-208)

<!-- source: http://www.dms.umontreal.ca/~rousseac/epp3_18.pdf | converted from PDF. Full text: [[rousseau-zhu-pp-graphics-nilpotent-elliptic-jde-2004.full]]. Claim `drr-zhu-rousseau-2004-15-pp-graphics-16-total`. -->

## What it establishes — finite cyclicity of the pp-graphics through nilpotent elliptic points

Part of the DRR program (finite cyclicity of the 121 quadratic graphics ⇒
uniform H(2) bound):

- **Thm 1.1** restates the DRR reduction: uniform bound on the number of limit
  cycles of a quadratic field **iff** all limit periodic sets surrounding the
  origin have finite cyclicity inside the quadratic family.
- **Thm 2.2**: **all 16 pp-graphics** have finite cyclicity.
- **Thm 3.1**: a pp-graphic through a multiplicity-3 nilpotent elliptic point
  with a hyperbolic saddle of hyperbolicity **σ≠1** has cyclicity **≤ 2**.
- **Cor 3.2**: graphics (I²₂₃),(I²₂₄),(I²₂₅) have cyclicity ≤ 2.
- Altogether: **finite cyclicity of 15 DRR graphics** (pp-type, not surrounding
  a center). Includes a pp-graphic with an elliptic nilpotent point + hyperbolic
  saddle (σ≠1) in generic 3-parameter families (Kotova–Stanzo zoo).

Key machinery (cyclicity ≤ n from an nth derivative): **Thm 2.1** — a pp-graphic
(Epp) with 2 parabolic/2 hyperbolic sectors has `Cycl(Epp) ≤ n` if the regular
transition map R (normalizing coordinates) has non-vanishing nth derivative.
Also the saddle-node C^k normal form `{ẋ=x²−ε, ẏ=±y(1+ax)}` (Prop 2.6), and
the nilpotent/triple-singularity normal forms (Thms 2.10, 2.11, 2.8).

## Hypotheses / holds here

Quadratic systems; pp-graphics through a multiplicity-3 **nilpotent** singularity
of elliptic type NOT surrounding a center. **Holds here: yes** — this fixes the
boundary inside the DRR program between the closed pp-graphics (not surrounding a
center) and the OPEN graphics that DO surround a center (I⁶b₁, H³₁₃, DI₂b full
rows).

**Evidence class: sourced** (full text held from Rousseau's site).

## Falsifier

A pp-graphic of this class with cyclicity > 2 for σ≠1.

## Bearing / implication

- Supplies the derivation–division method and the `Cycl ≤ n`-from-a-derivative
  principle as the run's model for DRR-graphic finite-cyclicity attacks.
- The blow-up / transition-map normal forms are Lean-statably checkable finite
  algebraic objects (normalizing-coordinate transition maps).
- Independent confirmation of Zhu 2005 (all 16 pp-graphics finite).
