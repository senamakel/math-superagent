```approach
idea: Go to the tangential / weakened H16 and produce a SHARP, fully-executed
  zero count for the Abelian integral of a NAMED Hamiltonian family via its
  Picard–Fuchs system and an argument-principle / extended-Chebyshev count —
  rather than attacking a limit-cycle graphic. The displacement of the
  first-order perturbation is the Abelian integral I(h)=∮_{γ_h} ω; the number of
  limit cycles born from the ovals γ_h is the number of isolated zeros of I. The
  Picard–Fuchs system gives a linear ODE with polynomial coefficients that I(h)
  satisfies; the Chebyshev/ECT criterion (Grau–Mañosas–Villadelprat 2010/2011,
  held full) reduces "I has at most N zeros on (0,h₀)" to checking that a
  certain chain of measures / Wronskians forms an extended complete Chebyshev
  system — which is an ALGEBRAIC, resultant-checkable condition.

  The representation change: turn a transcendental zero-counting problem
  (zeros of an integral over ovals) into a finite algebraic sign/resultant
  problem (the Wronskian chain of the Picard–Fuchs solutions), which Lean can
  actually finish.

mechanism: Why this problem's structure suits it. The run already holds the
  instruments as literature: BNY 2010 double-exponential, Binyamini–Dor linear,
  and the GMV Chebyshev criterion — but has NEVER executed a sharp count itself.
  This is the one goal-area (GOAL item 3: "sharp or improved zero-count for
  Abelian integrals in a named family, with the Picard–Fuchs system written down
  and the argument-principle count carried out") that is fully within reach of a
  checkable computation, and it produces a concrete publishable number rather
  than a bound on an open graphic. The named theorem chain: the Abelian integral
  of a Hamiltonian family satisfies a Picard–Fuchs system (the integrals of
  ω, H·ω, H²·ω... close up under differentiation); the ECT criterion turns N-zeroness
  into the strict alternation of a Wronskian chain; that strict alternation is a
  sign condition on explicit polynomials over Q, decidable by the kernel.
  Test 1 is satisfied trivially (Abelian integrals are analytic in h); Test 3 is
  the regime where the count is known to be sharp.

  The RESTRICTION that keeps this line alive against the alien-cycle warning:
  the Abelian-integral control of limit cycles FAILS for polycycles with saddle
  connections (alien cycles — claim h16-alien-limit-cycles-abelian-insufficiency:
  Luca–Dumortier–Caubergh–Roussarie 2009 construct a cubic 2-saddle cycle whose
  unfolding has a limit cycle NOT controlled by any Abelian-integral zero). But
  that obstruction does not touch this approach, because the target is the
  PERIOD ANNULUS of a CENTER — nonsingular ovals γ_h around an equilibrium —
  where the Abelian→limit-cycle reduction is known to hold. The honest scope is
  the LINEARISED problem for one family, not H16.2: a genuine partial result of
  the "sharp count in a named family" type, exactly GOAL result-type 3, and the
  most directly Lean-finishable of the three lines.

first-step: (a) VALIDATE the machinery against a published sharp count before
  trusting it on anything new: take a period-annulus family whose sharp Abelian
  integral zero-count is already in the literature (e.g. one of the
  Gasull–Lázaro–Torregrosa 2010 K≤4 straight-line families, or reproduce
  Li–Liu–Yang's H(3)≥13 Abelian count), write its Picard–Fuchs system exactly
  (sympy, over Q), form the GMV balance chain ℬ_σ₁(f_i/Φ′), ℬ_σ₂(g_i), compute
  the Wronskians, and check the CT-system sign/strict-alternation conditions with
  exact arithmetic over Q; capture to code/out/ and match the published bound.
  (b) Then pick a NAMED Hamiltonian family whose sharp Abelian count is NOT yet
  published, satisfying GMV Theorem A (separable H=Φ(x)+Ψ(y)) or Theorem B
  (H=A(x)+B(x)y^{2m}) with a LOW-DIMENSIONAL Picard–Fuchs system — first candidate
  the reversible two-center quadratic class Q3^R whose hemicycle cyclicity the
  run already holds (claim drr-mv-hemicycle-cyclicity-2), or a separable
  two-saddle / four-oval Hamiltonian. Write the PF system exactly, form the
  balance chain and Wronskians, check the CT-system conditions over Q, capture
  to code/out/, and state the resulting "at most N zeros on (0,h₀)" as a Lean
  theorem under code/lean/Lib/AbelianIntegral.lean, closing the sign conditions
  with the resultant/Sturm core (decidable by ring/norm_num/decide after
  expansion). Report #print axioms and every remaining sorry.

precedent: [GROUNDED — the whole machinery is standard, named, and held by this
  run; the sharp count for a named family is an established result-type, not a
  new method.]
  - The ECT (extended complete Chebyshev) criterion: Grau, Mañosas, Villadelprat,
    "A Chebyshev criterion for Abelian integrals", Trans. AMS 363 (2011) 109–129,
    arXiv:0805.1140 (held full). Theorem A: for H(x,y)=Φ(x)+Ψ(y) with even-
    multiplicity Φ,Ψ at 0 and involutions σ₁,σ₂, the integrals I_i(h)=∫_{γ_h}
    f_i(x)g_i(y)dx form an ECT-system on (0,h₀) iff the balances
    ℬ_{σ₁}(f_i/Φ′) and ℬ_{σ₂}(g_i) are CT-systems (verified by Wronskians,
    Lemma 2.3), giving an algebraic zero bound. Theorem B handles H=A(x)+B(x)y^{2m}.
    Claim ids: h16-grau-manosas-villadelprat-chebyshev-2010 (both entries).
  - Picard–Fuchs / Petrov-module machine: Gavrilov, "Petrov modules and zeros of
    Abelian integrals" (Bull. Sci. Math. 1998, doi:10.1016/S0007449799800049,
    free finite-rank Petrov module for semiweighted-homogeneous H); Gavrilov,
    "The infinitesimal 16th Hilbert problem in the quadratic case" (Invent. Math.
    143 (2001) 449–497); Binyamini–Novikov–Yakovenko, arXiv:0808.2952
    (constructive solution via Gauss–Manin/flat connections).
  - Executed sharp counts in named families — precedent that this method yields
    numbers: Gasull, Lázaro, Torregrosa, "Upper bounds for the number of zeroes
    for some Abelian integrals", arXiv:1012.5201 (held, claim
    h16-gasull-lazaro-torregrosa-abelian-zero-bounds-2010: K straight-line factor
    G, bounds); and the near-Hamiltonian double-homoclinic-loop counts in
    Li–Liu–Yang, "A cubic system with thirteen limit cycles" (JDE 246 (2009)
    3609–3619, doi:10.1016/j.jde.2009.01.038 — H(3)≥13 by counting Abelian
    integral zeros), confirm that an executed Chebyshev/PF zero-count of a named
    family is exactly the established way one obtains sharp lower and upper
    bounds in tangential H16.
  - The Chebyshev route is exactly what the survey (Abelian Integrals and Limit
    Cycles, Qual. Theory Dyn. Syst. 2011, doi:10.1007/s12346-011-0051-z) names as
    the standard instrument for sharp per-family counts.
  - Live boundary that CONFINES this approach rather than killing it: alien
    limit cycles (h16-alien-limit-cycles-abelian-insufficiency) show the Abelian
    reduction fails for saddle-connection polycycles, which is why this approach
    restricts to center period annuli (nonsingular ovals), where it holds.
  Caveat: what is NOT held is the run's own executed execution (the run has the
  criteria as literature and has not yet run a Picard–Fuchs system + Wronskian
  sign check to code/out/); that is the first-step work, and it is where the
  run's value-add lies, not in inventing a method.
status: adopted

## Fresh validation exemplar found (librarian cycle, 2026)

Yang 2025, arXiv:2512.19046 (held full HTML) is a **sharp, fully explicit
named-family Abelian-integral count**: the asymmetric cubic isochronous
Hamiltonian normal form (1.6)–(1.7) has period-annulus cyclicity exactly n−1
for perturbations of degree n, sharpness attained. This is precisely the first
validation target this approach names — a published sharp count whose
Picard–Fuchs system, generator classification (formula-iterable vs
non-iterable Iᵢⱼ(h)), and linear-independence/Wronskian core are written out
explicitly in the paper, hence machine-checkable in principle (Chebyshev/ECT
route per GMV 2011, held). Claim `h16-yang-2025-cubic-isochronous-period-annulus-sharp`.
A clean-room re-execution of its Abelian-integral algebra (sympy over ℚ,
generator count, Wronskian/CT-system check) is the validation step that would
graduate the pipeline before anything new is attempted.
```
