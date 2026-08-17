# Binyamini–Novikov–Yakovenko 2010 — explicit Abelian-integral bound

Full text: [[binyamini-novikov-yakovanko-abelian-integrals.html.full]]. Invent. Math. 181(2) (2010). arXiv:0808.2952.

## What the source establishes

**Tangential / infinitesimal H16 (constructive).** For H a Hamiltonian of degree
≤ n+1 and ω a polynomial 1-form of degree ≤ n, the number of isolated zeros of the
Abelian integral I_H,ω(t), counted with multiplicities and summed over all real
nonsingular ovals, is uniformly bounded by a **double exponential** of the degree:

- **Theorem 2:** 𝓝(n,n) ≤ 2^{2^{Poly(n)}}, Poly(n) = O(n^p), **p ≤ 61** (in fact
  O⁺(n^60) is what is proved).
- **Theorem 1:** the number of limit cycles generated from nonsingular energy-level
  ovals in a small non-conservative perturbation is bounded by the same
  double-exponential expression.

**Where the bound comes from:** the Abelian integrals are horizontal sections of a
regular flat meromorphic (Gauss–Manin) connection over ℚ with a **quasiunipotent
monodromy group**; the bound follows from a general theorem (Theorem 8) on zeros of
sections of such connections. This is a genuinely different mechanism from the
DRR/Roussarie reduction — it is specific to the linearised (first-order
perturbation) problem.

**What it does NOT cover (Remark 3):** conservative/integrable perturbations where
the Poincaré integral vanishes identically (higher variations → the center problem,
unknown); it only bounds first-order (Melnikov) zeros, not the full displacement.

## What it lets this run conclude

- Confirms and sharpens problem.md's recalled BNY bound (doubly exponential).
- **Lower bounds are quadratic/linear** (Remark 2): no good conjecture on the true
  asymptotics of 𝓝(n,m); improving the exponent from 61 toward 2 is open but
  "reducing below two exponential orders would require new ideas".
- It does NOT settle H16.2: it is the linearised problem. For the run's rung
  R-tangential-abelian it gives the explicit bound; the gate to the full problem
  (rung that switches on full nonlinearity) remains.

```claim
id: h16-bny-abelian-bound
statement: The number of isolated zeros of an Abelian integral I_{H,omega}(t),
  summed over nonsingular ovals and counted with multiplicity, deg H <= n+1,
  deg omega <= n, is bounded by 2^{2^{Poly(n)}} with Poly(n) = O(n^61) (proved
  O^+(n^60)). Hence limit cycles born from nonsingular ovals in a small
  non-conservative Hamiltonian perturbation are likewise bounded.
hypotheses: nonsingular ovals; non-conservative perturbation (Poincare integral
  not identically zero); deg H, deg omega bounded.
holds-here: yes (linearised/tangential problem only).
status: asserted
bearing: settles the tangential H16 with an explicit double-exponential bound;
  the linearised zero-count the full problem must turn into a bound on the full
  displacement.
anchor: research/sources/binyamini-novikov-yakovenko-abelian-integrals.html.full.md
```

## Does not help

This source alone does not bound H(2) or any graphic cyclicity — it bounds
first-order Melnikov zeros, not the full return map. It is the linchpin of the
Abelian-integral rung, not of the degenerate-graphics attack.
