# UC via the entropy–coupling method

A reduction of Frankl's union-closed sets conjecture to one analytical gap:
a coupling entropy inequality at density `1/2`. The iid instance of that
inequality is refuted (recorded so nobody retries it), so the gap is stated for
a genuinely dependent coupling class, where the finite-dimensional machinery
already exists and has produced the current record constants.

```skeleton
goal: (UC) Every finite union-closed family F ⊆ 2^[n] with F ≠ {∅} contains an
      element lying in at least |F|/2 of the members of F.
implies: |
  Encode each member of F as its indicator vector in {0,1}^n and set
  μ = Unif(F), the uniform measure on F; then H(μ) = log|F| > 0. Argue the
  contrapositive. If F has no abundant element, every coordinate has density
  < 1/2, i.e. max_i Pr_{A∼μ}[A_i = 1] < 1/2. By (CouplingIneq) there is a
  coupling (A,B) of (μ,μ) with H(A∨B) > H(A). But A, B ∈ F a.s., and F is
  union-closed, so A∨B (the indicator of A ∪ B) lies in F a.s.; hence
  H(A∨B) ≤ log|F| = H(A), a contradiction. Therefore F has an abundant
  element.

  (CouplingIneq) is the only missing lemma. It is stated below in the
  conditionally-iid class C: since every C-coupling is in particular a
  coupling of (μ,μ), the class-C inequality directly implies (CouplingIneq).
  No "completeness of C" hypothesis is used or needed — C being a subset of
  all couplings is enough, and it is the class for which a finite-dimensional
  optimization exists (Yu, Liu).

  CHAIN: (CouplingIneq) ⟹ UC.
status: live
rests-on: (none — the reduction is spelled out in full in `implies` and uses
          only the definition of union-closure: A,B ∈ F ⟹ A∨B ∈ F. The
          entropy-coupling framework is the one initiated by Gilmer
          arXiv:2211.09055 and generalised by Sawin/Yu/Liu; the facts cited
          from those sources are asserted-by-source and will be promoted to
          ledger claims by the scholar as the notes are digested.)
killed-by: (skeleton sound; only its iid sub-instance is killed, recorded below)
```

```gap
id: G-iid-half
lemma: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, the iid coupling (A,B independent, both ∼μ)
       satisfies H(A∨B) > H(A).   [Gilmer's "Conjecture 1"]
status: refuted
discharged-by: Sawin, arXiv:2211.11504 (abstract: "We also disprove a conjecture
  of Gilmer that would have implied the union-closed set conjecture"); Liu,
  arXiv:2306.08824 (abstract: "the best constant obtainable through the i.i.d.
  coupling is (3−√5)/2 ≈ 0.38197"). Both asserted-by-source; no ledger claim
  ids exist yet (CLAIMS.md is empty).
next: none — dead end. Any entropy proof of UC through this reduction must use
  a dependent coupling; the iid coupling cannot certify density > (3−√5)/2.
```

```gap
id: G-coupling-half
lemma: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, there is a conditionally-iid coupling
       (A,B) of (μ,μ) — A,B iid conditioned on an auxiliary variable, the class
       C of Liu arXiv:2306.08824 — with H(A∨B) > H(A). Equivalently: the
       finite-dimensional C-coupling optimization of Yu arXiv:2212.00658 has
       optimal constant exactly 1/2.
status: open
next: symbolic_math + coder — implement Yu's finite-dimensional optimization
  over the conditionally-iid class (auxiliary variable with the cardinality
  bound of Yu 2212.00658; entropy computed in exact arithmetic / interval
  arithmetic, never floating point). Two runs: (i) reproduce the published
  record constants as a correctness check — 0.38234 (Yu) and ≈0.38271 (Liu);
  (ii) push the constant toward c = 1/2 and certify H(A∨B) > H(A) for all μ
  with marginals < 1/2, or exhibit the extremal μ where the class optimum
  stays below 1/2. The latter is a proved barrier for this coupling class —
  GOAL.md result class 3 — and the former is UC.
```
