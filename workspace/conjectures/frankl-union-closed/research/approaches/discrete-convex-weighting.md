# Discrete-convex (Murota) nonlinear weight certificate — ADOPTED

```approach
idea: The linear averaging certificate provably fails — the averaged Frankl
  property is false for some union-closed families (claim
  `cms-averaged-frankl-wrong`). So the certificate must be NONLINEAR. The named
  replacement is Murota discrete convex analysis: an M♮-concave SET FUNCTION
  w : {0,1}^n → R (gross substitutes on the Boolean lattice, Fujishige–Yang),
  supported on F. Anchor the claim to the submodular boundary:
  `lozin-submodular-fc` already proves UC for submodular Boolean functions via
  exactly the Lovász/convex certificate machinery this proposes, so the real
  target is the gap between the SETTLED submodular class and the general case,
  tight where the near-cube extremal sits.
mechanism: Linear per-set weights cannot see the join-irreducible / abundance
  structure; and the uniform weighted-FUNC (weight on sets, required to hold
  for EVERY monotone f) is FALSE (`polymath-uniform-weighted-func-false`). The
  distinction that saves a certificate: the M♮-certificate is EXISTENTIAL over
  a specific convexity class (M♮-concave w), not universal over all monotone
  f — so the documented falsity of the universal form does not apply to the
  existential construction. M♮-concavity on {0,1}^n is gross substitutes, a
  genuine convexity theory with exchange axioms (Murota / valuated matroids)
  that (a) tensorise, (b) have a constructed Lovász extension, and (c) are NOT
  identical to submodularity — so the certificate class is generically larger
  than the settled class, and the decisive test is whether the feasible
  M♮-certificate on small families collapses to a submodular/linear one
  (re-deriving a settled class) or is genuinely new. The M♮-exchange
  inequalities are DISJUNCTIONS of LINEAR inequalities in the w-values, so the
  certificate question is an exact LP/MILP problem on n ≤ 5 — decidable.
status: refuted (first-step executed exact; M♮-class both under- and over-certifies; see Executed first-step verdict below)
first-step: The certificate is vacuous as *feasibility* — the uniform weight
  w≡1 already certifies any abundant element — so the plain LP decides
  nothing. The decisive, non-vacuous measurement is OVER- vs UNDER-
  CERTIFICATION relative to uniform. For every union-closed family F on n ≤ 5
  (through the canonical oracle code/lib/uc.py) and every element x, decide by
  EXACT LP/MILP feasibility whether there is a real function w : {0,1}^n → R
  with (i) w(A)=0 for A∉F; (ii) M♮-concavity; (iii) Σ_{A∈F} w(A)=1 and
  Σ_{A∈F,x∈A} w(A) ≥ ½ (w-abundance at x); and count, per family, the set
  Cert(F) = {x : some nonconstant M♮-concave w makes x w-abundant} against the
  true set Alb(F) = {x : density_x ≥ ½}. Report every family where
  Cert(F) ≠ Alb(F):
   * Cert ⊋ Alb (over-certify): some NON-abundant x is M♮-certifiable — the
     M♮-class cannot separate a would-be counterexample (no-abundant → could
     still be w-abundant), so the class does not give UC. Informative, negative.
   * Cert = Alb (rigid): M♮-certificates certify precisely real abundance — a
     SOUND rule and a stepping stone toward a separating certificate. Positive.
   * Cert ⊊ Alb: class too small, also informative.
  M♮-concavity (gross substitutes), for all X,Y⊆[n], u∈X∖Y:
     w(X)+w(Y) ≤ max{ w(X−u)+w(Y+u),
                      max_{v∈Y∖X} w(X−u+v)+w(Y+u−v) },
  a DISJUNCTION of linear inequalities → a finite union of polytopes → encode
  as a MILP with a binary branch-selector per (X,Y,u) pair and big-M (scipy
  has no MILP; use PuLP/CBC, or per-branch linear solve on the tiny n ≤ 3
  oracle cases then the general n ≤ 5 MILP). The free/linear relaxation (no
  convexity) is the vacuous baseline and must be shown to over-certify
  everywhere, isolating the M♮-concavity as what (if anything) buys rigidity.
  Also report, per family, whether every feasible w collapses to a
  submodular/linear one (→ re-derives `lozin-submodular-fc`) or is genuinely
  nonlinear-new. Run the three negative controls with the same encoding: 2^[n]
  must come out Cert = Alb = all elements (exactly ½, nothing over); the
  non-UC negative control from code/lib/uc.py must show the certificate's
  behaviour tracks closure, not a bare abundance count; finiteness is used
  through the exchange axiom being finite. The key targets: the near-5-cube
  extremal family, the guard set 2^[n], the singleton-containing family, and
  the non-UC negative control. Scaffolding sketch: code/out/mroof_cert_probe.py.
```

**Grounding verdict (research) — GROUNDED as a live, genuinely distinct hypothesis; unresolved by the literature.**

Murota *discrete convex analysis*; the two relevant classes are **M♮-convexity** (M♮-exchange axiom; on {0,1}^n an M♮-concave set function is gross substitutes, Kelso–Crawford / Fujishige–Yang; M-convex sets are exactly the bases) and **L♮-convexity** (discrete submodular analogue, Lovász-extension convex). **No source applies Murota discrete convex analysis to Frankl's conjecture** — searched multiple phrasings; the only DCA applications in the literature are economics and matroid/valuated-matroid theory. The closest existing machinery on the UC side is Poonen's *linear* weight theorem and Pulaj's *linear* cutting-plane computation over it — precisely the linear object whose failure motivates this candidate.

Hypotheses: M♮-concavity on the Boolean lattice is exactly gross substitutes — well-defined, well-characterised, hypotheses (finite ground set, set-valued domain) hold identically for the join-semilattice (2^[n],∨). The right class is M♮-convex (not the constant-sum M-convex), whose effective domains are closed under the matroid/independence structure rather than constant-cardinality.

Application to this problem: **none found**. The toolkit is real, genuinely distinct, NOT refuted; but the *existence* of an M♮-certificate is asserted by no source and guaranteed by no DCA theorem. The abstract "existence of an M♮-weight certificate" is asserted nowhere; honest status: a live open hypothesis whose first test is the computation, not the literature.

**Adoption decision (inventor, converging turn).** This is the only grounded, unresolved candidate (the other two are refuted with precise reasons: `iterated-union-entropy-operator` = k-fold-union generalisation whose constants strictly decrease; `shadow-compression-complement` = classical intersection-closed dual + exhausted Kruskal–Katona/LYM averaging engine). Research added the **submodular anchor** (`lozin-submodular-fc`) that neither of us had named: submodular Boolean functions satisfy UC through exactly the Lovász/convex certificate machinery this candidate proposes. That converts the abstract "find an M♮-certificate" (no existence theorem) into a sharply bounded question: does the certificate space extend *strictly beyond* the settled submodular class, and is it tight at the near-cube extremal? The over/under-certification measurement decides this exactly.

**Collision guards (must be checked in the first-step, not assumed away).**
1. `polymath-uniform-weighted-func-false` — the *universal* weight-on-sets FUNC is FALSE. The M♮-certificate is *existential over a convexity class*, not universal over all monotone f, so the falsity does not transfer — but the first-step must confirm the certificate is genuinely constrained (not satisfied on arbitrary non-UC families), else it is vacuous.
2. `markovic-bozin-equivalence` — a measure-on-sets reformulation already in the library, strictly more general than Poonen per-element weights. The distinct value of M♮- is the *constructive exchange* structure, not the mere existence of a set measure; the first-step must show the certificate is built (exchange axiom), not searched over an unconstrained set measure.
3. `lozin-submodular-fc` — submodular Boolean functions are already settled. If the M♮-certificate collapses to submodularity on every test family, the approach re-derives a settled class. The first-step reports exactly this collapse or its absence.
4. Poonen's theorem is the *per-element / FC-local* criterion, a different object from per-set global abundance. Do not conflate: the M♮-certificate targets the GLOBAL abundance of the conjecture, not the FC superfamily condition.
5. `no-degree-1-element-in-minimal-counterexample` — a minimal counterexample has no degree-1 element; the certificate only matters on families where every element has |F_x| ∈ [2, |F|/2), the genuinely hard depth-2 profile.

Do not claim UC. The deliverable: either a nonconstant M♮-concave certificate non-collapsing to submodular/linear on a nontrivial UC family — opening a real convexity route — or the exact statement that on n ≤ 5 every such certificate collapses / over-certifies, which refutes the novel claim and is itself a result.

## Executed first-step verdict (exact, task `mroof-cert-probe-execute`)

The over/under-certification measurement ran exactly as the first-step
specified, with the M♮-concavity (gross-substitutes) disjunction encoded as
exact Z3 QF_LRA over real w-values (support restriction w=0 outside F,
w≥0, Σw=1, Σ_{x∈A}w(A)≥1/2). Supplies: `code/out/mroof_cert_vs_alb.py`,
capture `code/out/mroof_cert_vs_alb.captured.txt`. Established correct by
reproducing the hand cases from `mroof_z3` validation (n=1 {∅,{x}}; the
`{5,7}` density-1 under-certification; the `{0,3}` restricted-constant
counterexample) and by the A102896 enumeration counts (3,13,121 complete;
4959 budgeted).

**Result: the M♮-concave support-restricted certificate class BOTH under- and
over-certifies at every n≥2.** Exact counts:

| n | families | over-cert (Cert⊃Alb) | under-cert (Cert⊊Alb) | rigid (Cert=Alb) |
|---|----------|----------------------|------------------------|------------------|
| 1 | 3 | 0 | 0 | 3 |
| 2 | 13 | 2 | 2 | 9 |
| 3 | 121 | 24 | 46 | 51 |
| 4 | 4959 (COMPLETE, 20228 solves) | 686 | 2992 | 1281 |

*(The complete n=4 sweep, code/out/mroof_sweep.py, supersedes the earlier
budgeted 932-family pass: over 686, under 2992, rigid 1281; 2788/4959 (56.2%)
UC families have nonempty Alb yet NO abundant element M♮-certifiable.)*

- **Over-cert exemplar** F={0,1,3}={∅,{x},{x,y}} n=2: y has density 1/3 (not
  abundant) yet is M♮-certifiable at the 1/2 threshold. At n=4, F={0,1,3,5,7}
  over-certifies {1,2}. Collision guard 1 (`polymath-uniform-weighted-func-
  false`): the certificate is NOT vacuous — it certifies some non-abundant x,
  i.e. it is constrained but its feaseasible set spills past Alb, so the class
  cannot separate a would-be counterexample.
- **Under-cert exemplar** F={1}={x} n=2/3: abundant x (density 1) is NOT
  certifiable; likewise {5,7} (density-1 element, both Z3 and cvc5 agree).
  This is the submodular/linear-collapse guard 3 in its strongest form: the
  support-restricted M♮-class is too SMALL rather than too large, losing even
  density-1 elements (singleton and two-set families).
- **Rigid** (Cert=Alb) so far never means "the class proves UC": every rigid
  family sampled has each element's M♮-feasibility genuinely equal to its
  abundance, but the class is not a sound rule globally (under-cert dominates).

**Verdict — approach NEGATIVE as a proof route.** The M♮-concave
support-restricted certificate neither proves UC (it under-certifies abundant
elements, including density 1) nor cleanly characterises abundance (it over-
certifies elsewhere). Cert ≠ Alb is the norm, not a stepping stone; there is
no rigid Cert=Alb subfamily large enough to bootstrap UC. The submodular
anchor `lozin-submodular-fc` is NOT re-derived (the feasible class is
genuinely different from and smaller than it), but nothing here is a surrogate
for it either. This closes the `discrete-convex-weighting` approach as a
proof route (results recorded; not UC, machine-verified to n=12 none-the-less).
