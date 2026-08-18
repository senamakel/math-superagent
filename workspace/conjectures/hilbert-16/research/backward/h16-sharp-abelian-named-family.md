# Backward skeleton — sharp Abelian-integral count for a named Hamiltonian family

Decomposition of the run's **adopted** approach
(`research/approaches/abelian-picard-fuchs-argument-principle-sharp-count.md`)
into the propositions that, together, produce a sharp zero-count for the
Abelian integral of one named Hamiltonian family. This is the *linearised*
Hilbert problem (GOAL result-type 3), not `H(2)<∞`; the two are different
theorems and the distinction is the whole point of the scope note below.

The target family is **not yet fixed**: it is fixed by the validation pass
(G-model/G-pf's first move re-runs Yang 2025's cubic-isochronous count
`n−1` sharp), and the value-add is the *second* instantiation — a
GMV-admissible family whose sharp count is not published. The skeleton is
written parametrically over the family `(H, Γ, ω)`; the named validation
instance is `H = ½x²+λx³+½λx⁴+½λ⁻¹y²+xy+x²y` (Yang 2025, cubic isochronous,
`0<λ<1`).

```skeleton
goal: For a named Hamiltonian family (H, Γ) with a center and period annulus
      Γ = {H = h : h ∈ (0,h₀)} meeting GMV Theorem A or B, and for the
      perturbation form of degree ≤ n, cycl(Γ) ≤ N with N an explicit integer
      obtained from a kernel-checked Wronskian sign condition, and N sharp
      (attained by an explicit perturbation). First instantiation: the Yang
      2025 cubic-isochronous period annulus has cyclicity exactly n−1.
implies: Fix (H, Γ, ω) as above. G-model reduces the dynamical count to the
      zero count: in the first-order (Melnikov/Abelian) regime, limit cycles
      bifurcating from Γ are in bijection with isolated zeros of the Abelian
      integral I(h) = ∮_{γ_h} ω, counted with multiplicity — valid because Γ
      consists of *nonsingular ovals* (the alien-cycle obstruction,
      h16-alien-limit-cycles-abelian-insufficiency, is a saddle-connection
      phenomenon and does not touch a center period annulus). G-pf then
      locates I in a finite-dimensional module: the Petrov/Gavrilov module of
      Abelian integrals of H is free of rank μ, so I is a solution of the
      rank-μ Picard–Fuchs system with polynomial coefficients over Q; this is
      the one step that uses polynomiality of H and is the step that fails for
      a C^∞ field (Test 1). G-ect-criterion (cited GMV) says: if the
      balance/Wronskian chain of that system is an ECT-system on (0,h₀), then
      any nonzero element of the μ-dimensional solution space — hence I — has
      at most μ−1 zeros. G-ect-apply computes that chain exactly over Q and
      rewrites "ECT" as finitely many strict-sign / resultant / Sturm
      conditions on explicit rational functions. G-sign-lean discharges those
      conditions in the Lean kernel, so "I has ≤ N zeros" (N = μ−1) is a
      kernel-checked theorem modulo the cited GMV criterion. G-sharpness
      exhibits explicit coefficients for which I has N simple zeros on
      (0,h₀). Chain: G-model + (G-pf → G-ect-criterion → G-ect-apply →
      G-sign-lean) give cycl(Γ) ≤ N; G-sharpness gives cycl(Γ) ≥ N; hence
      cycl(Γ) = N, sharp. Dropping G-sharpness still yields the honest partial
      result cycl(Γ) ≤ N, which is the run's bankable deliverable.
killed-by: (1) Scope creep past the center period annulus — the Abelian
      reduction to zeros of I FAILS for polycycles with saddle connections
      (alien cycles, h16-alien-limit-cycles-abelian-insufficiency: a cubic
      2-saddle cycle with an alien limit cycle). Any version of this skeleton
      applied to a graphic or saddle loop silently uses a false reduction and
      is refuted; the skeleton is confined to nonsingular ovals by G-model's
      hypotheses. (2) A "proof" of the bound that never uses polynomiality of
      H (i.e. that never establishes the finite-rank PF module in G-pf) — a
      C^∞ Hamiltonian perturbation's first-order integral need not satisfy a
      finite-rank Picard–Fuchs system, so such a proof bounds a smooth falsity
      (Dulac's error shape). (3) The sharpness claim (G-sharpness) examined
      only in the generic regime — sharp counts die to canard/slow–fast
      constructions in a singular limit (Test 3); the attained-N construction
      must state its parameter box and the singular limit it avoids.
rests-on: h16-abelian-integral-bounds, h16-bny-abelian-bound,
      h16-alien-limit-cycles-abelian-insufficiency (model reduction and its
      scope), h16-novikov-yakovenko-modules-picard-fuchs-2002,
      h16-gavrilov-abelian-morse-hamiltonian-aif-1999 (finite-rank module +
      PF system), h16-grau-manosas-villadelprat-chebyshev-2010 (ECT
      criterion), h16-ggi-quadratic-centers-genus-one-2009 (validation
      precedent: exact cyclicity 2 for (r11),(r18)),
      h16-yang-2025-cubic-isochronous-period-annulus-sharp (validation
      target: n−1 sharp)
status: live
```

```gap
id: G-model
lemma: The first-order (Poincaré–Pontryagin / Melnikov) reduction: for a
       Hamiltonian field X_H perturbed by ε(ω) within a polynomial family, the
       limit cycles bifurcating from the nonsingular ovals γ_h of the period
       annulus Γ correspond one-to-one, for ε small and counted with
       multiplicity, to isolated zeros of the Abelian integral
       I(h) = ∮_{γ_h} ω on (0,h₀). The reduction is valid precisely because Γ
       consists of regular ovals; it FAILS for saddle-connection polycycles
       (alien cycles), which is what confines this skeleton to center period
       annuli.
status: discharged
discharged-by: h16-alien-limit-cycles-abelian-insufficiency (states the
       reduction holds for regular ovals and fails for polycycles — the scope
       hypothesis), h16-abelian-integral-bounds and h16-bny-abelian-bound
       (the reduction plus its uniform bound, asserted-by-source). Cited, not
       re-derived: the first-order reduction is the standard Melnikov
       theorem; the run holds it as literature.
next: (discharged — cited, do not re-derive. The scope hypothesis
       "Γ = nonsingular ovals of a center period annulus" must be carried as a
       binder on every downstream Lean statement; a version of G-sign-lean
       whose statement does not name the period annulus has silently dropped
       the alien-cycle guard.)
```

```gap
id: G-pf
lemma: For the named family, the module of Abelian integrals of H is free of
       finite rank μ (Petrov/Gavrilov), and I(h) satisfies the rank-μ minimal
       Picard–Fuchs system — a first-order linear ODE system with polynomial
       coefficients over Q — whose generators and rank match the family's
       structure. This is the step that uses polynomiality of H; it is the
       step that fails for a C^∞ field and therefore the step that satisfies
       Test 1.
status: open
discharged-by: (none yet) — the finite-rank/PF theorems are held as literature
       (h16-novikov-yakovenko-modules-picard-fuchs-2002,
       h16-gavrilov-abelian-morse-hamiltonian-aif-1999), but the PF system
       for the *specific named family* has never been executed: the adopted
       approach records "the run has the criteria as literature and has not
       yet run a Picard–Fuchs system … to code/out/".
next: tool_builder + symbolic_math, today: for the Yang 2025 cubic-isochronous
       normal form H = ½x²+λx³+½λx⁴+½λ⁻¹y²+xy+x²y (0<λ<1), compute the
       module of Abelian integrals and the minimal Picard–Fuchs system exactly
       in sympy over Q — rank μ, polynomial coefficients, the generator
       classification (formula-iterable vs non-iterable Iᵢⱼ) — capture to
       code/out/pf_yang.captured.txt, and match the paper's stated rank before
       trusting the pipeline on any new family.
```

```gap
id: G-ect-criterion
lemma: The extended-Chebyshev criterion (GMV 2011 Theorem A/B): for
       H = Φ(x)+Ψ(y) (Theorem A) or H = A(x)+B(x)y^{2m} (Theorem B), the
       Abelian integrals I_i form an ECT-system on (0,h₀) iff the balance
       chain ℬ_{σ₁}(f_i/Φ′), ℬ_{σ₂}(g_i) is a CT-system, verifiable through
       Wronskians; an ECT-system of dimension μ has at most μ−1 zeros
       (counted with multiplicity) on (0,h₀). This is the cited
       transcendental-to-algebraic bridge.
status: discharged
discharged-by: h16-grau-manosas-villadelprat-chebyshev-2010 (asserted,
       full text held, arXiv:0805.1140). Cited theorem — the run must not
       re-derive it; it enters Lean as a `Cited` axiom with the source in the
       docstring.
next: (discharged — cite, do not re-derive. When it enters Lean it is an
       axiom in namespace Cited and earns `conditional`, never `formalised`.)
```

```gap
id: G-ect-apply
lemma: For the specific named family, the balance chain and the Wronskians
       W₀,…,W_{μ−1} are computed exactly over Q, and the ECT/CT-system
       condition is reduced to a finite list of strict sign conditions,
       non-vanishing conditions and Sturm alternation on explicit rational
       functions over (0,h₀) — a decidable algebraic problem rather than a
       transcendental one.
status: open
discharged-by: (none yet) — the criterion is cited but its application to a
       concrete family (the balances, the Wronskian chain, the reduction to
       finitely many sign conditions) is computation this run has not
       executed.
next: symbolic_math, today: form the GMV balance chain and the Wronskians for
       the Yang 2025 family from the G-pf generators, compute exactly over Q
       (sympy), reduce the ECT condition to finitely many strict-sign /
       Sturm-alternation statements, capture to
       code/out/wronskian_yang.captured.txt. Gate: the chain must reproduce
       Yang's n−1 bound before any new family is attempted — a chain that
       gives a different bound on the validation instance is refuted.
```

```gap
id: G-sign-lean
lemma: The finite sign/Sturm conditions produced by G-ect-apply are
       discharged by the Lean kernel: "the Wronskian chain W₀,…,W_{μ−1} is an
       ECT-system on (0,h₀)" is a kernel-checked theorem over MvPolynomial ℚ,
       resting only on the kernel plus the cited GMV criterion — so "I has at
       most N = μ−1 zeros" is a theorem rather than a number. Mathlib gaps
       (ECT-systems, Abelian integrals, ovals, Picard–Fuchs) are catalogued
       here rather than papered over.
status: open
discharged-by: (none yet) — the pipeline exists on paper; no Lean statement of
       the Wronskian chain or its sign conditions has been written.
next: lean_prover, today: state `ect_system_on_open_interval` for the
       polynomial Wronskian chain (clearing denominators to MvPolynomial ℚ)
       and discharge the strict-sign/Sturm conditions with decide/norm_num/
       Sturm over ℚ; report `#print axioms` (must be the kernel's three +
       `Cited.gmv_ect`). Catalogue the missing Mathlib API (Abelian integrals,
       ECT-systems, period annulus ovals) as a finding under code/lean/Lib/ —
       a list of precisely what cannot yet be typed is itself a result.
```

```gap
id: G-sharpness
lemma: The bound N = μ−1 is attained: there are explicit degree-≤n polynomial
       coefficients (rational parameters) for which I has N simple zeros on
       (0,h₀), certified — by interval-arithmetic sign changes of I on N
       disjoint h-intervals, or by an exact Sturm count on a polynomial
       reduction — so cycl(Γ) ≥ N, hence cycl(Γ) = N.
status: open
discharged-by: (none yet) — sharpness (attainment) is a construction, not a
       bound, and is only needed for the "sharp" half of the goal; the
       upper-bound deliverable cycl(Γ) ≤ N stands without it.
next: tool_builder (the certified limit-cycle / zero-count oracle), after
       G-sign-lean: construct the explicit perturbation achieving N simple
       zeros of I and certify the N sign changes in interval arithmetic on
       disjoint subintervals of (0,h₀) (or exact Sturm on a polynomial
       reduction), capture to code/out/sharpness.captured.txt. For the
       validation instance, re-certify Yang's n−1 attainment before claiming
       sharpness anywhere new.
```

**How the lemmas recombine (the `implies` spelled out).** The skeleton is a
reduction chain, not an induction. G-model converts the dynamical question
("how many limit cycles bifurcate from Γ") into the analytic question ("how
many zeros has I on (0,h₀)"), valid on the nonsingular ovals and only there.
G-pf confines I to a μ-dimensional solution space of a polynomial-coefficient
ODE — the analyticity/algebraicity step, absent for smooth fields. The cited
G-ect-criterion converts "μ-dimensional ECT" into "≤ μ−1 zeros". G-ect-apply
and G-sign-lean turn the ECT property into finitely many sign conditions that
the kernel can and does check, which is the entire reason this route is
preferred over the DRR route's analytic remainder: the finite core is a
decidable polynomial statement. G-sharpness is the construction that turns the
upper bound into equality. Order of attack: **G-pf first** — every later step
consumes its output, and it is a well-scoped exact computation on a held paper,
so it is where the pipeline either validates against Yang 2025 or is refuted
cheaply.

**Tests applied.** Test 1 (smooth test): satisfied by G-pf — the finite-rank
Picard–Fuchs module uses polynomiality of H; a C^∞ perturbation's first-order
integral has no such finite-rank constraint, so a proof skipping G-pf proves a
smooth falsity. Test 2 (lower-bound test): the Abelian count is a per-family
bound, not a global `H(n)` bound, so `H(2)≥4`, `H(3)≥13`, `H(n)≳n²log n` do
not threaten it; a downstream claim that this gives `H(n)<∞` would be the
error. Test 3 (slow–fast test): binds G-sharpness — the attained-N
construction must name the parameter box and the singular limit it avoids;
sharp Abelian counts are exactly where canard constructions attack.
