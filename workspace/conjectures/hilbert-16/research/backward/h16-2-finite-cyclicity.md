# Backward skeleton — H(2) < ∞ via finite cyclicity

Goal as stated in `problem.md`: the second part of Hilbert's 16th — is
`H(n) < ∞` for every `n ≥ 2`, where `H(n)` is the supremum over planar
polynomial vector fields of degree ≤ n of the number of limit cycles. The
concrete, self-contained instance this run can actually make progress on is
`n = 2`, governed by the Roussarie / DRR reduction. This skeleton decomposes
`H(2) < ∞` into the finite-cyclicity lemmas that would give it, names the
analyticity step (test 1) explicitly, and reduces the whole claim to one
open-graphic instance.

```skeleton
goal: H(2) < ∞ — every planar quadratic polynomial vector field has a number of limit cycles bounded uniformly over the whole degree-2 family.
implies: H(2) < ∞  follows by the Roussarie reduction (DRR 1994): it is equivalent to finite cyclicity of every one of the 121 graphics in the DRR list (limit periodic sets of the compactified quadratic family). That equivalence is the frame, named in problem.md and standing on Roussarie 1998 / Dumortier–Roussarie–Rousseau 1994, so the whole claim folds to the conjunction: for each graphic Λ in the list, cycl(Λ) < ∞ uniformly in the family. The core gap is then one graphic (why one: the list is finite, so the conjunction is min over finitely many bounds once each is settled). The four lemmas G-resolve, G-transition, G-zeros, G-uniform combine, for a fixed Λ, into cycl(Λ) ≤ N: resolve gives the vertex normal forms, transition gives the sector expansions from those normal forms, zeros bounds the number of roots of the composed displacement function, uniform upgrades pointwise finiteness to a family-wide bound — and G-uniform is the step that must use compactness of the parameter space, i.e. is the step that would fail if the analyticity input in G-transition were dropped (this is exactly Dulac's 1923 error).
killed-by: (not yet) — would break if the analyticity step (G-transition / G-zeros) were replaced by a purely topological or C^∞ argument: a C^∞ vector field can have infinitely many limit cycles, so the finiteness lemma must genuinely use analytic/algebraic structure of coefficients, and locating that step is part of stating the argument.
rests-on: h16-drr-121-graphics, drr-1994-citation-anchor (DRR frame); drr-rr-closes-i14 (89/121); drr-rr-boundary-only-for-3-graphics, drr-lu-claims-h14-3, h16-drr-open-rows (open target set)
status: live
```

```gap
id: G-drr-status
lemma: Which of the 121 DRR graphics remain with finite cyclicity unproved
       today, and the paper that closed each of the recently closed ones.
       There exists at least one graphic Λ_0 recorded open in the current
       literature (this is what picks the attack target).
status: open
discharged-by: (none yet)
thread: (none yet)
next: A librarian enumerates the 121 DRR graphics against primary sources
       (DRR 1994 + later closures — Rousseau–Shan–Zhu 2015 already closes
       I_12^1, I_13^1 in a source this run holds). Build a machine-readable
       table: graphic id, phase-portrait class (vertices, sectors, nilpotent
       or degenerate points), closure paper, open/closed. The already-downloaded
       Rousseau–Shan–Zhu source proves exactly two rows; the rest is the
       standing request `dumortier-roussarie-rousseau-9c4f`. Doable today: it
       is a survey + cross-check, and its output is the target list for every
       downstream attempt.
```

```gap
id: G-resolve
lemma: A graphic Λ in the DRR list admits a resolution: each vertex (singular
       point) is brought by finitely many polynomial blow-ups within the
       quadratic family to a normal form whose singularities are elementary,
       and the hyperbolic sectors between the vertices are identified. Each
       vertex's normal form determines the local transition data.
status: open
discharged-by: (none yet; largely done case-by-case in the DRR literature but
       not recorded as a claim in this workspace)
thread: (none yet)
next: For the concrete target Λ_0 chosen from G-drr-status, compute the
       blow-up normal form of each vertex symbolically with sympy (exact,
       over Q). Validate the whole method on a graphic the run already has
       closed — reproduce the blow-up list and normal forms for I_12^1 from the
       Rousseau–Shan–Zhu source as a live check before trusting it on Λ_0.
```

```gap
id: G-transition
lemma: On each hyperbolic sector of the resolved graphic, the passage (transition)
       map between the two incoming/outgoing transversals has an asymptotic
       expansion of the shape  Σ c_i x^{a_i} (log x)^{k_i} whose exponents and
       coefficients are determined by the vertex normal form. This is the step
       where analyticity of the coefficients enters, and it is the step that
       fails for C^∞ fields (no such expansion constrains the map — Dulac's
       error). It must invoke a genuine finiteness source: Écalle / Ilyashenko
       almost-regular germs, or the Ilyashenko–Yakovenko explicit bound for
       elementary polycycles; the open content is the nilpotent/degenerate
       vertex (where the elementary hypothesis fails).
status: open
discharged-by: (none yet)
thread: (none yet)
next: For the resolved target Λ_0, write down the transition expansion for each
       sector from the normal form, as explicit formulas over Q. First move:
       reproduce the displacement expansion Rousseau–Shan–Zhu use for I_12^1
       (symbolically, sympy + the sector transition formula) so the method's
       output can be compared against a published answer.
```

```gap
id: G-zeros
lemma: The displacement (first-return) function around Λ_0 is the composition
       of the sector transition maps, so it carries an expansion in a finitely
       generated module of "almost-regular" functions; the number of its zeros
       (limit cycles born from Λ_0) is bounded by the rank/finiteness theorem
       for such expansions. This is the Dulac-type finiteness for the single
       displacement function; it is pointwise in the parameters.
status: open
discharged-by: (none yet)
thread: (none yet)
next: Given the expansions from G-transition, form the composition and bound the
       zeros by the corresponding finiteness theorem. The finite, checkable
       core Lean can carry: fix a small number of parameters and, on a finite
       sample box, certify the number of sign changes of the displacement in
       interval arithmetic (the oracle's job) as numerical evidence; pair it
       with a stated (not yet proved) Lean bound on the zeros.
```

```gap
id: G-uniform
lemma: The pointwise zero bound from G-zeros is uniform over the compact
       parameter space of the quadratic family near Λ_0; i.e. cycl(Λ_0) < ∞
       as a bound on the family, not just per field. The expansion module is
       finite-dimensional and parametrized algebraically (= quasiunipotent
       monodromy / finite possible zero patterns), so the zero count cannot
       vary. This is the uniformity step — the one a naive "pointwise finiteness
       ⇒ uniform bound" argument would fake, and where compactness of the
       parameter box must actually be used.
status: open
discharged-by: (none yet)
thread: (none yet)
next: Given the algebraic structure of the expansion family from G-transition,
       argue the zero pattern is one of finitely many; encode the finite
       parametrization and the zero-pattern bound as a Lean theorem over the
       polynomial data (a kernel-checkable statement if carried through).
       Numerically, verify the bound holds on a dense grid of the parameter box
       as evidence, clearly labelled conjectural.
```

**How the lemmas recombine (the `implies` spelled out).** Fix a target graphic
Λ_0 (G-drr-status says one is open). G-resolve gives its blow-up normal forms.
G-transition turns each normal form into a sector transition expansion, using
analyticity — the single place the argument is not merely topological. G-zeros
composes those expansions into the displacement function and bounds its zeros.
G-uniform upgrades that to a family-wide bound, i.e. cycl(Λ_0) < ∞. Doing the
same for every graphic in the finite list and taking the max gives H(2) < ∞ by
the DRR equivalence (rests-on). The only genuinely open mathematical core is the
pair G-transition + G-zeros + G-uniform applied to one graphic neither the
literature nor a previous run has closed — G-resolve is mostly published
machinery and G-drr-status is bookkeeping, so if everything else is checked a
single open graphic is what the whole conjecture reduces to (this is the known
state: DRR 1994 ⇒ H(2)<∞ iff all 121 are finitely cyclic, and a small number
remain open).

**Test 1 applied:** the smooth test is satisfied only if G-transition/G-zeros
genuinely use analytic (almost-regular) structure. If a candidate proof of
G-zeros never touches analyticity it has re-proved a C^∞ falsity; record that
as the failure point. **Test 2:** the run makes no claim of a sharp tight bound,
so H(2) ≥ 4 and H(n) ≳ n² log n do not threaten a finite cyclicity bound.
**Test 3:** a sharp counting conjecture would be examined in the slow–fast
regime, but finite cyclicity is not a sharp count, so this test is not the one
a finite-cyclicity proof fails.
