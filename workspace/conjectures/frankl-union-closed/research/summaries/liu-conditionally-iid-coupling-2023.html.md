# Jingbo Liu, "Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling" — arXiv:2306.08824v1

**Note — replaces the structural digest.** Wikilink to full text:
[[liu-conditionally-iid-coupling-2023.html.full]]

Full text: `research/sources/liu-conditionally-iid-coupling-2023.html.full.md`.
Preprint (unpublished in a journal; appeared at CISS 2024). **Not the record.**

## What it establishes (precise statements)

**Proposition 1 (the sharp iid inequality, restated).** For random `S ∈ [0,1]`,
`E[S]=u`, `T` an iid copy:
`E[h(S̄T̄)] ≥ E[h(S)]·{ h(2u−u²)/h(u), u ≤ (3−√5)/2;  (1−u)·2/(√5−1), u ≥ (3−√5)/2 }`.
(The `u ≥` branch is `2/(√5−1) = (1+√5)/2 ≈ 1.618` folded with `(1−u)`.)
Established by CL22/AHS22/Saw22, not Liu; this is the engine of the `(3−√5)/2`
iid bound. The whole UC-entropy argument runs through the chain-rule split
`H(Xⁿ∨Yⁿ) ≥ Σ H(Xᵢ∨Yᵢ|Xⁱ⁻¹,Yⁱ⁻¹) ≥ Σ H(Xᵢ|Xⁱ⁻¹,Yⁱ⁻¹) = H(Xⁿ)`.

**Proposition 2 (Sawin's scheme / the record's engine).** For analytically-
defined `c*, α*`, for any `c < c*` there is `C > 1` with
`ᾱ*E[h(S̄T̄)] + α*E[h(S∨R∨min(S+R,1/2))] ≥ C·E[h(S)]` whenever `P_SR` symmetric,
`S⊥T`, `P_S=P_T`, `E[S] ≤ c`. Here `h(·∨·∨min(·+·,1/2))` is the max-entropy OR
coupling. **The optimizer** of this two-term ratio is `P_SR(1,b)=P_SR(b,1)=a`,
`P_SR(b,b)=1−2a` with `a,b` solving `(1−2a)h(½)=(1−a)h(b)` and
`(1−a)²h(b̄²)=(1−a)h(b)`, giving `h(b)(2−h(b))=h(b̄²)`. Larger root
`b* ≈ 0.3294547385`, `a* ≈ 0.07887729`, and **`c* ≈ 0.3823455`** is the best
constant obtainable from Sawin's approach (= Yu/Cambie record). `α* ≈ 0.0356069`.

**Key fact driving Liu's improvement.** The equality case of (the two-term
Sawin bound) is a *symmetric* `P_ST` on `{b*,1}²` whose matrix
`[P_ST(s,t)]_{s,t∈{b*,1}}` is **not positive semidefinite**, hence **not** a
mixture of iid distributions. The conditionally-IID class `C₃(μ)` = couplings
of (μ,μ) ∩ closure of convex hull of symmetric rank-1 measures excludes it —
so `P_{SR₂*} ∉ C₃(P_S*)` while `P_{SR₂*} ∈ C₂(P_S*)`. This is the crux: the
restriction to conditionally-IID couplings forbids the record-attaining
coupling, so the conditionally-IID class is *strictly smaller* than the
max-entropy class, yet its best constant still strictly exceeds `c*`.

**Definition 1 (protocol).** A conditional scheme `Π_{s,t}` on `{0,1}²` with
`EX=s, EY=t`, generating `Xⁿ,Yⁿ` sequentially; includes Gilmer iid, Sawin
max-entropy, Yu maximal-correlation, and conditionally-IID couplings.

**Definition 2 (conditionally IID).** `Π_{s,t}(x,y) = ∫ Q_{u,s}(x)Q_{u,t}(y) P_U(du)`
— `X,Y` iid conditioned on auxiliary `U`. Example 5 gives the tractable form
`Π_{s,t}(0,0) = s̄t̄ + f(s̄)f(t̄)` with `0 ≤ f(s̄) ≤ s∧s̄`. The max-entropy
protocol `Π^{(2)}_{s,t}(0,0)=1−s∨t∨min(s+t,1/2)` is **not** conditionally IID
(matrix not PSD for `s=t<1/4`).

**Theorem 9 (cardinality reduction).** For any conditionally-IID protocol, the
infimum in the 3-protocol bound is achieved by `P_{SR₂}` a mixture of *two* iid
distributions: `P_{SR₂}(s,r) = E[P_{S|W}(s|W)P_{S|W}(r|W)]` for binary `W`.

**Theorem 12 (finite-dimensional reduction).** For `f(x)=lxp(x)`, `p(1)=0`,
`l` small, the bound reduces to `(P₀,P₁)` of the form (3-atom each):
`P₀ = a₁δ_{b₀}+a₂δ_{b₂}+a₃δ_{b₄}`, `P₁ = a₁δ_{b₁}+a₂δ_{b₃}+a₃δ_{b₅}`
— a **9-dimensional optimization in `(a₁,a₂,q,b₀..b₅)`**.

**Theorem 13 (the conditional record, heavily conditioned).** *Under* the
PSD hypothesis of §V-A *and* the structural hypothesis that the global minimizer
of the 9-d problem is `q=0`, `P₀=p*δ_{x*}+p̄*δ₀` with
`x*²+x*²(1+x̄*²)=1`, `p*²h(x*²)−p*h(x*)=0` — values `p*≈0.8936045`,
`x*≈0.6907876`, `β*≈0.1000526` — the constant improves to
**`c' ≈ 0.382709087918741`**. This is a **conditional** result: it depends on
(a) a numerically-verified PSD hypothesis on a 29×29 (and to 90×90) moment
matrix, and (b) the *conjectured* global-minimizer structure, relying on 10⁵
random-initialization global optimization.

## Hypotheses and holds-here

- **Theorem 6 / Lemma 8 (strict improvement over c*, unconditional offer):**
  this part is **proved** — for small convex-combination weight `β`, the
  conditionally-IID protocol strictly exceeds `c*`. So "the entropy method can
  do strictly better than 0.3823455" is **theorem**, not conjecture. **Holds-here:
  yes** (it is the same finite UC family setting).
- **Theorem 13 / value 0.38271:** **conditional**, rests on two unproved
  hypotheses (PSD of a finite moment matrix; global-minimizer shape). **Holds-here:
  conditional** — do **not** report 0.38271 as an established constant.
- **Theorem 12's reduction** to 9-d: proved *given* Lemma 11's concavity
  (itself conditional on the PSD hypothesis being true for the chosen `f`).

## What this lets the run do

- **Bears directly on `G-coupling-half`.** The attack wants to know whether
  the conditionally-IID class's optimum reaches `1/2`. Liu shows: (i) the class
  optimum **does strictly exceed the `(3−√5)/2` and `0.38234` records** (proved,
  unconditional), and (ii) the class optimum's best-found value is `≈0.38271`
  (conditional). The exact 9-d objective (84)–(87), the 3-atom `(P₀,P₁)` form,
  and the claimed global minimizer `p*,x*` are the concrete objects to optimize.
- **Reproducing `c' ≈ 0.382709`** (equivalently the Sawin `c* ≈ 0.3823455`) is
  the correctness check for the run's own solver before seeking any larger `c`.
- The **non-PSD-at-optimum fact** is a *structural* warning: the extremal
  coupling for the record is excluded from the conditionally-IID class, so the
  class's true optimum is an open analytic question, not something a generic
  solver finds by symmetry.

## What it does not settle

Does not prove the class optimum reaches `1/2`; the proven/unconditional part
only establishes strict improvement over the record, and the conditional best
value `0.38271` is still far below `1/2`. Does not settle whether a *larger*
conditionally-IID protocol family or a different auxiliary structure reaches a
bigger constant. The `1/2` gap remains entirely open.

```claim
id: liu-conditionally-iid
statement: The conditionally-IID coupling class (X,Y iid given an auxiliary
  variable U) strictly exceeds the Sawin/Yu/Cambie record c*≈0.3823455; its
  best-found conditional value is c'≈0.382709087918741 (Theorem 13), attained
  at q=0, P₀=p*δ_{x*}+p̄*δ₀ with p*≈0.8936045, x*≈0.6907876, β*≈0.1000526.
hypotheses: finite union-closed family; conditionally-IID protocol class C₃;
  strict-improvement part unconditional; the 0.38271 value needs (a) a
  numerically-verified PSD hypothesis on a moment matrix and (b) a conjectured
  global-minimizer structure
holds-here: yes (strict improvement), conditional (0.38271 value)
status: asserted (the unconditional strict improvement is proved in-paper; the
  0.38271 value rests on the two stated hypotheses, not checked here)
bearing: the attack object for G-coupling-half; reproducing c* (Sawin) and c'
  (cond. IID) is the solver correctness check; the non-PSD-at-optimum fact shows
  the class optimum is an open analytic question, and that a generic solver
  cannot assume symmetry at the optimum
anchor: research/sources/liu-conditionally-iid-coupling-2023.html.full.md
contradicts: nothing (resolves against yu-record-0-38234; see contradiction
  thread — record is Yu 0.38234 / Sawin c*, Liu 0.38271 is conditional, not a
  contradiction)
follows-from: sawin-dependent-coupling, liu-strict-improvement
answers: exact-current-published-c8b8 (partially: confirms current published
  record is Yu 0.38234, Liu 0.38271 conditional)
```

```claim
id: liu-strict-improvement
statement: Under small convex-combination weight β with a conditionally-IID
  protocol, the entropy bound for the union-closed constant is strictly larger
  than c*≈0.3823455 (Lemma 8 + Proposition 3); the record optimizer's coupling
  is not positive semidefinite, hence not in the conditionally-IID class.
hypotheses: finite union-closed family; protocol framework of Liu Definition 1;
  P_S supported not only on {0,1} (Lemma 7 handles the degenerate case)
holds-here: yes
status: proved
bearing: proves no "iid/dependent barrier" caps the entropy method at the
  record; the conditionally-IID class is a strictly smaller coupling class whose
  optimum is an open question worth optimizing
anchor: research/sources/liu-conditionally-iid-coupling-2023.html.full.md
follows-from: sawin-dependent-coupling, liu-conditionally-iid
```

```claim
id: liu-9dim-reduction
statement: The union-closed constant bound for the conditionally-IID class with
  f(x̄)=x̄x reduces to a 9-dimensional optimization (Theorem 12): over
  (a₁,a₂,q,b₀..b₅) with P₀,P₁ 3-atom, objective (84); value ≥1 certifies c as
  a lower bound — the concrete finite problem the run can solve.
hypotheses: f(x̄)=x̄x, positive-semidefiniteness of the quadratic form (Lemma 11,
  numeric for l=1)
holds-here: conditional (the PSD hypothesis is numerically verified, not proved)
status: asserted
bearing: the exact finite-dimensional optimization object for G-coupling-half
anchor: research/sources/liu-conditionally-iid-coupling-2023.html.full.md
follows-from: liu-conditionally-iid
```
