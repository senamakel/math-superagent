# UC via the entropy–coupling method

A reduction of Frankl's union-closed sets conjecture to one analytical gap:
a coupling entropy inequality at density `1/2`. The iid instance is refuted
(recorded so nobody retries it), and the Yu/Sawin **two-atom** restricted class
is now proved *capped* at φ/2 < 1 at t = 1/2 (see below) — so the surviving gap
is stated for the genuinely larger conditionally-iid class (Liu's C₃), where a
finite-dimensional (9-dimensional) optimization exists and nobody has yet shown
it cannot reach 1/2. This file corrects an earlier version whose `G-coupling-half`
claimed "the Yu optimization has optimal constant exactly 1/2" — that
equivalence is refuted and recorded as a barrier, not restated.

```skeleton
goal: (UC) Every finite union-closed family F ⊆ 2^[n] with F ≠ {∅} contains an element lying in at least |F|/2 of the members of F.
implies: | Encode each member of F as its indicator vector in {0,1}^n and set μ = Unif(F), the uniform measure on F; then H(μ) = log|F| > 0. Argue the contrapositive. If F has no abundant element, every coordinate has density < 1/2, i.e. max_i Pr_{A∼μ}[A_i = 1] < 1/2. By (CouplingIneq) there is a coupling (A,B) of (μ,μ) with H(A∨B) > H(A). But A, B ∈ F a.s., and F is union-closed, so A∨B (the indicator of A ∪ B) lies in F a.s.; hence H(A∨B) ≤ log|F| = H(A), a contradiction. Therefore F has an abundant element. (CouplingIneq) is the only missing lemma. It is stated below for the conditionally-iid class C (A,B iid conditioned on an auxiliary variable — the class C₃ of Liu arXiv:2306.08824, strictly larger than Yu's two-atom class). Since every C-coupling is in particular a coupling of (μ,μ), the class-C inequality directly implies (CouplingIneq); C being a subset of all couplings is enough and gives a finite-dimensional optimization (Liu's 9-dimensional reduction, claim `liu-9dim-reduction`). CHAIN: (CouplingIneq) ⟹ UC.
killed-by: skeleton sound; its iid sub-instance refuted (ellis-gilmer-conjecture-refuted) and its Yu-two-atom sub-instance capped at phi/2<1 at t=1/2 (yu-gamma-half-is-phi-over-2, yu-gamma-hat-nonincreasing); surviving gap is posed on the strictly larger conditionally-iid class C3 (liu-9dim-reduction)
rests-on: reduction needs only union-closure + H(mu)=log|F|. Gap facts: ellis-gilmer-conjecture-refuted (iid false); yu-gamma-hat-nonincreasing + yu-gamma-half-is-phi-over-2 (two-atom capped); liu-conditionally-iid + liu-9dim-reduction (surviving class object).
status: live
```

```gap
id: G-iid-half
lemma: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, the iid coupling (A,B independent, both ∼μ)
       satisfies H(A∨B) > H(A).   [Gilmer's "Conjecture 1"]
status: refuted
discharged-by: ellis-gilmer-conjecture-refuted (counterexample on n=2, marginals
  exactly 1/2 and a perturbation below); Sawin arXiv:2211.11504 and
  Liu arXiv:2306.08824 disprove it; iid-OR entropy certifies nothing above
  (3−√5)/2 (claims ahs-barrier, iid-barrier-exact).
next: none — dead end. Any entropy proof of UC through this reduction must use a
  dependent coupling.
```

```gap
id: G-yu-twoatom-half
lemma: The Yu/Sawin two-atom symmetric conditionally-iid coupling class reaches
       density 1/2: sup_α inf_{P two-atom} g(P,α)/Eh ≥ 1 at t = 1/2.
status: refuted
discharged-by: yu-gamma-half-is-phi-over-2 (Γ̂(1/2)=φ/2≈0.809<1, proved by exact
  algebra on the collapsed α=0 extremal) and yu-gamma-hat-nonincreasing
  (Γ̂ non-increasing, so Γ̂(1/2) ≤ Γ̂(t̂_max) < 1 at the crossing ≈0.38235).
next: none for extending this class — it is capped. This is the quantitative
  barrier: the two-atom relaxation certifies nothing at density 1/2. Recorded so
  the surviving gap is not re-stated at the two-atom ceiling.
```

```gap
id: G-coupling-half
lemma: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, there is a conditionally-iid coupling
       (A,B) of (μ,μ) — A,B iid conditioned on an auxiliary variable, the class
       C₃ of Liu arXiv:2306.08824, strictly larger than the refuted two-atom
       class — with H(A∨B) > H(A). Equivalently: the 9-dimensional
       C₃-coupling optimization of Liu (claim `liu-9dim-reduction`) has optimal
       constant exactly 1/2.
status: open
next: symbolic_math + coder — implement Liu's 9-dimensional conditionally-iid
  optimization (Theorem 12 of arXiv:2306.08824, objective (84) over
  (a₁,a₂,q,b₀..b₅), P₀,P₁ 3-atom) in exact/interval arithmetic, never floating
  point. Two runs: (i) reproduce the conditional record c'≈0.382709087918741 as
  a correctness check against claim `liu-conditionally-iid`; (ii) push toward
  c = 1/2 and certify H(A∨B) > H(A) for all μ with marginals < 1/2 — or exhibit
  the extremal μ where the C₃ class optimum stays below 1/2 (a proved barrier
  for the largest known tractable coupling class, itself a GOAL.md result of
  class 3). A correctness trap to keep off the two-atom ceiling: the Yu class is
  already capped (G-yu-twoatom-half), so the search must live in the full C₃
  class, and any candidate certifying above t̂_max=0.3823455334 must be checked
  against the degenerate-atom hole the run already found in the scorer.
```
