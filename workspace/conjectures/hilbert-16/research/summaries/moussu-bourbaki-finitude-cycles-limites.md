# Moussu, "Le problème de la finitude du nombre de cycles limites" (Séminaire Bourbaki 655, 1985-86, Astérisque 145-146, 89-101)

<!-- source: https://www.numdam.org/article/SB_1985-1986__28__89_0.pdf | converted from PDF, French. Full text: [[moussu-bourbaki-finitude-cycles-limites.full]]. Claim `h16-moussu-bourbaki-1987-finitude`. -->

## What it establishes — the canonical limit-cycle definition + 1980s finiteness state

This is the run's canonical reference for **what a limit cycle is** (the
definition the Lean `h16_2` statement and the certified limit-cycle oracle must
implement), set in Poincaré's framework:

- A **cycle C** is a periodic trajectory of the vector field V.
- C is a **limit cycle** iff the germ of its **return map f** is not the identity.
- When V is analytic, f is analytic and a limit cycle is an **isolated point in
  the set of periodic orbits**.

Plus the 1980s finiteness state, before the final 1991/92 proofs:

- **Theorem 0.1 (Bamón 1985):** a quadratic vector field on R² has finitely many
  limit cycles.
- **Theorem 0.2 (Ilyashenko 1984):** the Dulac finiteness conjecture holds
  outside a proper algebraic subset of the space of vector fields.
- The **reduction of the Dulac problem to polycycles**: limits of cycles must
  accumulate on a polycycle; analytic extension of the return map in the log
  coordinate (Prop 2.1: `X ↦ f∘exp(X)` extends analytically to the
  `{X > b(1+y²)^{1/4}}` domain).
- Notes `N(2) ≥ 4` ([37] — the lower-bound 4 cycles in degree 2, see claims).

## Hypotheses / holds here

Individual fields; analytic vector fields; the finiteness problem (NOT uniform in
parameters). **Holds here: yes** — supplies the precise Poincaré limit-cycle
definition (return-map germ ≠ identity, isolation in the periodic-orbit set) that
the Lean statement and the certified limit-cycle oracle implement, and the
earliest held treatment of the Dulac→polycycle reduction.

**Evidence class: sourced** (full text held from Numdam).

## Falsifier / watch item

A retyped Dulac-1923 full text or a modern line-by-line account showing a
*different* point of failure in Dulac's argument. This 1987 exposé reflects the
1980s Bamón/Ilyashenko state and predates the final 1991/1992 proofs and the
Yeung 2024-25 gap claim.

## Bearing / implication

- The Lean `LimitCycleSet` / isolated-periodic-orbit notion must match this
  definition (germ-of-return-map ≠ id ⇔ limit cycle).
- The Dulac→polycycle reduction is the frame for the three problem.md tests:
  an argument that never uses analyticity of the return map is refuted (the
  analytic-extension step above is where analyticity enters).
