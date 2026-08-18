```claim
id: r-center-ideal-zero-division-conditional
statement: Conditional R-center-ideal zero-division lemma (the abstract shape
  of the run's G-remainder step for the H^3_14 route), kernel-checked in Lean:
  given a compact parameter neighbourhood K and collar, a finite
  generalized-monomial family (Fin m), a coefficient ideal presented by a
  finite generator Finset (InCoefficientIdeal: pointwise membership of each
  coefficient a_i in the ideal span of the generators on K), a uniform
  remainder bound with the remainders h_i vanishing at the section origin
  (all four packaged as Admissible), AND the analytic zero-division theorem
  (Hadamard divisibility / root uniqueness / derivation-division on the
  generalized-monomial class) as an explicit binder hypothesis, the zero set
  of the displacement V on K × collar is finite with a uniform ncard bound.
evidence: kernel-checked implication; the load-bearing analytic hypothesis is
  open
status: conditional
formalisation: code/lean/Lib/RCenterIdealZeroDivision.lean
falsifier: A family satisfying Admissible whose displacement zero set on the
  box is infinite or has no uniform bound, with the analytic zero-division
  hypothesis holding; equivalently, a proof that no such analytic
  zero-division theorem holds on the H^3_14 iterated-log transseries class
  (the run's refuted short-Dulac approach rules out the finite
  power-times-log restriction, so the class really is transseries with
  iterated logs/exponentials).
```

Verification record:

- `lean_check code/lean/Lib/RCenterIdealZeroDivision.lean` → `compiled: true`,
  `outcome: verified`, `sorry warnings: none`, `cited axioms: none`.
- `#print axioms r_center_ideal_zero_division` → exactly `[propext,
  Classical.choice, Quot.sound]` — the kernel's own three; no `sorryAx`, no
  cited axiom.
- The theorem's proof is the specialisation of the `zero_division` binder
  hypothesis to `(V, a, h)`; the kernel checks the implication and checks
  nothing about the hypothesis, which is exactly why the status is
  `conditional`, not `formalised`.
- The analytic `zero_division` theorem is deliberately NOT an `axiom` under
  `namespace Cited`: the held literature (RR 2015 Thm 5.8-style
  derivation-division) does not cover the transseries class the non-hyperbolic
  H^3_14 vertices require, so claiming it as cited would misattribute it.
  It is the run's open G-remainder gap (blueprint
  `h16-2-h14-3-finite-cyclicity/G-remainder`, `research/backward/h16-2-h14-3-finite-cyclicity.md`),
  recorded as a fenced `gap` block in the file with id
  `r-center-ideal-zero-division-analytic-theorem`.
- Hypotheses carried by binders (each is a hypothesis the run has not
  established its own claim for): `_hK : IsCompact K`,
  `_hcollar : IsCompact collar` (carried as data, unused by the
  specialisation), `hV : Admissible ...` (the named hypotheses of the task:
  finite generalized-monomial family, coefficient ideal, uniform remainder,
  remainder vanishing), and `zero_division` (the open analytic theorem).
- Does NOT claim H(2) < ∞, does NOT claim finite cyclicity of the graphic,
  does NOT claim any bound on limit cycles; it is the conditional interface
  for one algebraic-analytic step of the H^3_14 route.
