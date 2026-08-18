# Inventor decision — three-approach grounding round (2026-08-18)

## Verdicts

- **ADOPTED (narrowed): `inverse-integrating-factor-divisor-harnack`.** The local
  IIF vanishing-multiplicity ⇒ cyclicity theorem is grounded (García–Llibre–Maza
  JDE 2013; Gasull–Giacomini; Zhang). The unrestricted global Harnack cap is
  NOT claimed: no source produces a global polynomial IIF or a uniform degree
  bound for the open DRR graphics, and a formal Bautin-core IIF does not imply
  convergence, algebraicity, a degree bound, or global coverage. What is adopted
  is the local theorem plus the Harnack cap ONLY on a named family where a
  polynomial/algebraic IIF is explicitly verified.
- **REFUTED: `degenerate-hamiltonian-irregular-picard-fuchs-borel`.** No theorem
  that the Borel transforms are rational; no identification of the open DRR
  Hamiltonians with a rational-Borel regime; no conversion of the nonlinear
  four-Dulac displacement into a finite vector of Abelian-integral solutions
  (the cited Abelian results are first-variation/Melnikov, not the full return map).
- **REFUTED: `artin-mazur-zeta-finite-type-return-map`.** Artin–Mazur gives
  exponential growth (positive radius), not rationality; rationality needs
  Axiom-A/no-cycle, shift-of-finite-type, or toral structure. "Rational ζ
  numerator degree bounds |Fix|" is false; a 1-D analytic germ is not a compact
  global dynamical system; finite determinacy of a germ does not imply
  finite-type dynamics.

## Why the IIF route won

1. It is the only candidate that survived research with a live restriction
   rather than a flat refutation.
2. Its finite core is already computed by this run: the order of the formal IIF
   at a focus is the index of the first nonzero Lyapunov quantity — an
   ideal-membership/sign-condition computation discharged in
   `code/out/membership.captured.txt` (the ⟨L4,L6,L8⟩ ideal, focal values through
   degree 14) with the cofactor-certificate pattern already kernel-checked in
   `code/lean/Lib/BautinRecurrence.lean`.
3. It is the only candidate whose *counting* object (not a nonexistence
   certificate) connects the two halves of H16: oval count of {V=0} (Part I,
   Harnack/Gudkov) and order of V at a focus (Part II, Bautin ideal).

## The new step (the gap between the reformulation and the literature)

Research grounded the LOCAL IIF theorem and left the GLOBAL Harnack cap
unsupported. The synthesis targets one OPEN center graphic whose unperturbed
field is Darboux-integrable, so V₀ is explicit and algebraic; the perturbed
formal V is then computed by the same recurrence as the validated focus case,
and the run's existing Darboux cofactor work (Lu H³₁₄: X(L)=(x+dy)L,
X(F)=(2Bx+dy)F, kernel-checked) feeds it directly. First step:
(a) validate ord(V) = first-nonzero-Lyapunov-index on the quadratic focus family
(reproduce Bautin M(2)=3, i.e. V has order 4 since L1=L2=L3=0, L4≠0);
(b) then read cyclicity off the Newton polygon of the perturbed V for the
Darboux-integrable open graphic, applying Harnack only where V is proved
polynomial/algebraic of known degree on the relevant domain.
