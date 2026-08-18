# Caubergh, "Hilbert's 16th problem for Liénard equations" (Oberwolfach Mini-Workshop survey talk, UAB postprint, 2012)

<!-- source: https://ddd.uab.cat/pub/artpub/2012/228095/Cau2012.pdf | converted from PDF. Full text: [[caubergh-lienard-h16-2012-uab.full]]. Claims `h16-lower-bound-catalogue-2012`. -->

## What it establishes — the Liénard sub-problem + a key uniform-finiteness theorem

Survey talk on Hilbert-16 restricted to **Liénard equations**
`x'' + f(x)x' + g(x) = 0`, degree n and m.

- **Thm 2.1**: the global number of limit cycles of (1.1) with `g(x)=x` is
  **uniformly bounded** when f is restricted to a compact set of polynomials of
  degree exactly n ([27] n even, [4] n odd).
- **Thm 3.2** (the structural fact the run uses): Let K compact in parameter
  space, S compact 2-manifold, X_λ analytic on S. There is a **uniform upper
  bound for the number of limit cycles of X_λ in S for λ∈K** **iff** every limit
  periodic set Γ of X_{λ₀} has **finite cyclicity** inside the family for λ near
  λ₀. — This is the Roussarie/DRR finite-cyclicity reduction to uniform
  bounds, restated cleanly. It is the precise statement of "uniformity comes
  from finite cyclicity of every limit periodic set", the content that separates
  H16.2 (uniform) from individual finiteness.
- p.2 records the 2012 lower-bound catalogue: H(2)≥4, H(3)≥13, H(4)≥22,
  H(5)≥28, H(6)≥35, H(7)≥50, H(n)≥kn²ln n (Christopher–Lloyd), and the
  Li–Chan–Chung refinement `H(n) ≥ 4(n+1)²(1.442695 ln(n+1) − 1/6) + n − 2/3`.

## Hypotheses / holds here

Liénard subclass; compact-parameter uniform finiteness; analytic fields on a
compact surface for Thm 3.2. **Holds here: yes** — Thm 3.2 is the cleanest
statement of the finite-cyclicity ⇔ uniform-bound equivalence the run's whole
DRR frame rests on; the catalogue corroborates the n²log n lower bounds.

**Evidence class: sourced** (full text held from UAB DDD).

## Falsifier

An upper bound on H(n) below the n²log n growth (none known; the held
Buzzi–Novaes 2024 repeats the same n²log n lower bound).

## Bearing / implication

- **Uniform-finiteness honesty check:** Thm 3.2 makes explicit WHERE uniformity
  comes from in a uniform-bound argument — it cannot be imported from pointwise
  finiteness; it must come from finite cyclicity of every limit periodic set
  (the DRR program). Any candidate H16.2 proof that quantifies over K and
  concludes uniform from pointwise is exactly the error this theorem rules out.
- Liénard catalogue refines the CONTEXT lower-bound numbers (degree 4..7).
