# Rahman 1971 — Distinct zeros of the product of a polynomial and its successive derivatives

```claim
id: popoviciu-erdos-rahman-nplus2
statement: If p(z) is a real-rooted polynomial of degree n, the product P = p·p'·…·p^{(n-1)} has at least n+1 distinct zeros unless p ≍ (z-a)^n (pure power, 1 distinct zero). Among non-degenerate real-rooted p, P has n+1 distinct zeros exactly for p ≍ (z-a)(z-b)^{n-1}, (z-a)^2(z-b)^2, or (z-a)^3(z-b)^3, and at least n+2 otherwise. The Popoviciu-Erdős conjecture (real or complex) is the n+1 bound.
hypotheses: modern real-rooted hypothesis used in Rahman's proof (the conjecture itself is for polynomial coefficients); degree n; derivative product P over its zero-union.
holds-here: yes (the n+1/n+2 counting fact for real-rooted polynomials is what the degree-20 binomial search runs against; the union counting complements the shared-root CA hypothesis)
status: proved (for the real-rooted statements; the conjecture in general is open)
bearing: The shared-root CA hypothesis is a statement about COMMON roots; this is the dual statement about the UNION of all derivative zero sets. A genuine CA counterexample would force P to collapse to only the ≤5 distinct roots of f, far below n+1 — linking the two. The extremal shapes z(z^2-1) and z(z^2-1)^2 are non-binomial constructions for the degree-20 diversification task.
anchor: research/sources/rahman1971_distinct-zeros-product.full.md
contradicts: none
follows-from: none
answers: none
```

Q. I. Rahman, "The Distinct Zeros of the Product of a Polynomial and its Successive Derivatives", Canad. Math. Bull. **14** (2), 1971, pp. 267–269.

<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1DFE2645D96C7BF19E72108915B302AD/S0008439500058276a.pdf/the-distinct-zeros-of-the-product-of-a-polynomial-and-its-successive-derivatives.pdf
  and https://doi.org/10.4153/cmb-1971-050-9 (landing / bibliography) -->

Q. I. Rahman, "The Distinct Zeros of the Product of a Polynomial and its Successive Derivatives",
Canad. Math. Bull. **14** (2), 1971, pp. 267–269.

## The conjecture (Popoviciu–Erdős)

If `p(z)` is a polynomial of degree `n`, then the product

    P(z) = p(z) p'(z) p''(z) … p^{(n−1)}(z)

has at least `n+1` distinct zeros unless `p(z) = c(z−a)^n`.

The problem was mentioned by P. Erdős in a lecture at the University of Montréal
and attributed by him to Tiberiu Popoviciu.

## This is the dual of the Casas-Alvero hypothesis

CA asks: if `f` shares a *common* root with every derivative `f^(i)`, must `f` be a
pure power? The Popoviciu–Erdős problem asks a counting question for the *union*
of the zero sets: how many distinct zeros does `P = ∏ f^(i)` have in total? The
pure-power case is the only case where `P` is allowed to have as few as `n+1`
distinct zeros; any genuine CA counterexample would make `P` collapse to the
`n`-many distinct roots of `f` (with all the shared-derivative roots equal to them)
— far below `n+1`. So the two are linked: the "which index j fails first" question
the degree-20 search studies is, on the binomials `x^20 − c x^k`, precisely a
question about where the `P`-zero distribution is forced to be depleted.

## The theorem proved here (real zeros only)

Let `p(z)` have only real zeros. Then `P(z)` has

- (i) **1** distinct zero if `p(z) ≍ (z−a)^n` (the pure-power case);
- (ii) **n+1** distinct zeros if `p(z) ≍ (z−a)(z−b)^{n−1}`, or
  `p(z) ≍ (z−a)^2(z−b)^2`, or `p(z) ≍ (z−a)^3(z−b)^3`;
- (iii) at least **n+2** distinct zeros in any other case.

Sharply: `n=3`, `p = z(z²−1)` gives exactly 5 = n+2 distinct zeros;
`n=5`, `p = z(z²−1)²` gives exactly 7 = n+2 distinct zeros.

`n=1`: 1 zero. `n=2`: 1 distinct zero if the two zeros coincide, else 3 = n+1.

The technique is Rolle's theorem chained across the derivatives together with
explicit tracking of the extreme simple zeros `a^{(K)},…,a^{(n−2)}`,
`b^{(l)},…,b^{(n−2)}` of successive derivatives that are forced to be new and
distinct from `a,b`, plus direct calculation for the two-rooted / symmetric cases.

## Why this matters to this run

- The `n+2`-distinct-zeros bound for real-rooted non-degenerate polynomials is a
  clean, exact, *classical* statement about the distribution the degree-20 search's
  binomials `x^20−c x^k` are fighting against.
- Its extremal examples `z(z²−1)` and `z(z²−1)²` (and more generally
  `z(z²−1)^m`-type shapes with real roots) are the *non-binomial* constructions the
  steering directive asks to add to the search: they are low-scoring but genuinely
  different in structure from `x^n − c x^k`.
- It is freely readable on Cambridge Open (the 1973 Sudbery paper that motivated
  the record was paywalled and is NOT held; this is the open-access replacement).

## Relationship to what the library already holds

- Laterveer–Ounaïes (Prop 4–5, held) prove a CA polynomial of degree N has ≥5
  distinct roots and ≥4 in its open Gauss–Lucas hull. The Popoviciu–Erdős counting
  bound is a sibling statement about the *union* of all derivative zero sets rather
  than the shared roots.
- Jakubovich's real-rooted family results (held: `yakubovich2013`, `yakubovich2014`)
  are the modern descendants of Rahman's real-zeros theme: "a real-rooted CA
  polynomial (if any) has ≥5 distinct zeros" is echoed in Rahman's extremal
  configurations.
- Rahman–Schmeisser, *Analytic Theory of Polynomials* (2002), is the standard
  modern reference for these zero-distribution results, cited by several held
  sources (walch-coincidence, yakubovich, polstra).
