# Ilyashenko–Yakovenko 2000 — elementary polycycles: finiteness with explicit tools

Full text: [[ilyashenko-yakovenko-elementary-polycycles-2000.full]]
(arXiv:math/0010174v1; also held as
[[primary-ilyashenko-yakovenko-elementary-polycycles-2000.full]]).

## What the source establishes (held full text)

**Main Theorem (existential Hilbert–Arnold for elementary polycycles).** Under the
assumption that families of vector fields have elementary singularities only, the
global Hilbert–Arnold conjecture is solved: any generic finite-parameter family of
vector fields on the sphere S² with a compact base and only elementary singularities
has a uniform upper bound for the number of limit cycles (Corollary 1). Under the
assumption that all polycycles are elementary, the Main Theorem gives a solution to
the Local Hilbert–Arnold problem (Corollary 2).

**Method (the parts this run uses):** the proof is by reduction of the cyclicity
question to Khovanskii's fewnomial/real-algebraic geometry bounds. Theorems 16–18
and Corollaries 3–4 develop the Khovanskii reduction: a bound on the number of
solutions of F(x) = a in terms of the number of solutions of the differentiated
system F'(x) = (a, ε) (Rolle-type counting, #{x : f(x)=a} ≤ #{x : f'(x)=ε}), for
C² Morse f and compact/regular hypotheses. The framework is the "basic system"
(T, Sa, f) with a uniform bound B(T, Sa, f; r₀) over all parameter values (λ,ε) ∈ B_{r₀}
(Theorem 9) for an open dense set of C^{p₀} functions of sufficiently small
characteristic size. Theorem 7 (IY3) gives finitely-differentiable orbital
equivalence of a family with an elementary singular point having a hyperbolic sector
to a localization of a listed normal form family.

**Context:** the Dulac problem (individual finiteness) was solved by Ilyashenko and
Écalle, "however, both proofs do not allow any generalization to solve Existential
Hilbert Problem" (verbatim) — the pointwise/uniform gap stated by the authors
themselves. The compactification by central projection S²→R² with homogenuity of
parameters is the frame the DRR 121-graphic reduction uses for the quadratic family.

## What it lets this run conclude

- The elementary-polycycle restricted class is settled with explicit tools
  (Khovanskii reduction, Rolle-type counting). This is the instrument the run's
  `noetherian-chain-khovanskii-rolle-zero-bound` approach wanted to port to
  non-elementary graphics — the port fails because non-elementary vertices produce
  transseries (iterated logs/exponentials, parameter-dependent exponents), which are
  not Noetherian/LN functions in a uniform chart (see that approach's refutation).
- The authors' own sentence "both proofs do not allow any generalization to solve
  Existential Hilbert Problem" is a primary-source statement of the exact gap this
  run's `g-uniform` goal must bridge: uniform bounds require the Roussarie/DRR
  compactification machinery, not the individual proofs.
- The Theorem 7 normal-form families are the elementary-vertex analogue of the DR
  2009 degenerate normal forms (Props 2.1–2.3): the difference is exactly where
  elementarity is used (nonzero eigenvalues → finitely differentiable orbital
  equivalence to listed families).

```claim
id: h16-iy2000-elementary-polycycle-finiteness
statement: Ilyashenko–Yakovenko (2000): under elementary-singularities-only, the global Hilbert–Arnold conjecture holds — any generic finite-parameter family of vector fields on S^2 with compact base and only elementary singularities has a uniform upper bound for the number of limit cycles (Corollary 1); the Local Hilbert–Arnold problem is solved under all-polycycles-elementary (Corollary 2). The method is the Khovanskii reduction (Rolle-type counting: #{x: f(x)=a} ≤ #{x: f'(x)=ε} for C^2 Morse f, Theorems 16-18, Corollaries 3-4) with uniform bounds over parameter balls (Theorem 9). The authors state the individual Dulac proofs (Ilyashenko, Écalle) do not generalize to the existential problem.
hypotheses: generic finite-parameter C^infty families; elementary singularities only (all nonzero eigenvalues); compact parameter base; polycycles elementary.
holds-here: yes — restricted class; the open DRR graphics are non-elementary, so this does not close them and does not give H(2)<∞.
status: asserted
evidence: full text held at research/sources/ilyashenko-yakovenko-elementary-polycycles-2000.full.md; Corollary 1, Corollary 2, Theorems 9/16/17/18 verbatim in the held text.
falsifier: a generic finite-parameter family with elementary singularities and unbounded limit cycles over a compact base; or an error in the Khovanskii reduction application.
sources: https://arxiv.org/pdf/math/0010174v1
anchor: research/sources/ilyashenko-yakovenko-elementary-polycycles-2000.full.md
follows-from: h16-kaloshin-elementary-polycycle-bound
answers:
```
