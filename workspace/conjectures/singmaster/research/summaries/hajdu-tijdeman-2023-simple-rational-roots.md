# Hajdu–Tijdeman 2023 — "The Diophantine equation f(x)=g(y) for polynomials with simple rational roots"

Source: L. Hajdu, R. Tijdeman, "The Diophantine equation f(x)=g(y) for
polynomials with simple rational roots", J. London Math. Soc. (2023),
DOI 10.1112/jlms.12746. arXiv:2204.12345 (full text held):
`research/sources/hajdu-tijdeman-2023-simple-rational-roots.full.md`.

## What the paper establishes

The subject: f(x) = g(y) where f ∈ Q[x] has only simple rational roots (the
shape `f(x) = a₀(x−a₁)···(x−a_k)` with distinct rational aᵢ) and g ∈ Q[y] has
rational coefficients. The binomial polynomial `C(x,k)` is exactly of this
shape: its roots are 0,1,...,k−1, all simple integers. So the theorem's
hypotheses hold for the equal-binomial-coefficients family.

**Theorem 1.1 (degree-divisibility obstruction).** If f has only simple
rational roots and f(x) = g(y) has infinitely many rational solutions with
bounded denominator, then there exist m ∈ {1,2,3,4,6}, n,s ∈ ℤ>0 with
deg(f) = ms, deg(g) = ns. If additionally g has only simple rational roots and
deg(f) ≤ deg(g), then m ∈ {1,2} (deg(f) | 2·deg(g)).

For the binomial case f=C(x,k₁), g=C(y,k₂): deg = k₁, k₂. So if the pair has
infinitely many bounded-denominator solutions, k₁ | 2k₂ (or swapped).
Concretely: the infinite Fibonacci family has k₁=2 vs k₂=3 — 2 | 2·3 holds.
This is a necessary condition; it does **not** say the other pairs are finite
with a bound — the theorem only constrains which pairs can be infinite.

**PTE structure (Theorems 6.1, 9.1).** When both f,g have simple rational
roots and the equation has infinitely many bounded-denominator solutions, f is
a "PTE_m-polynomial" and g a "PTE_{ℓm/k}-polynomial" (Prouhet–Tarry–Escott
structure); the exceptional pairs are exactly those built from PTE tuples. The
infinite-solution cases are characterized in terms of standard pairs of the
third/fourth kind (Dickson-type) when degrees are large. Explicitly: for the
first/second-kind standard pairs, deg(f) | deg(g) with a specific
shift-and-scale ("similar") description.

**The equal-blocks application (Theorem 10.1).** For every positive integer N
there are only finitely many pairs of disjoint blocks of consecutive integers
A, B of size ≤ N with equal products (up to the PTE/collinear exceptional
families). This is the Erdős–Turk / Erdős–Graham-adjacent form of the
equal-products equation that underlies `C(x,k1)=C(y,k2)` — the same
consecutive-block structure Saradha–Shorey–Tijdeman and Beukers–Shorey–
Tijdeman classified.

## Bearing for this run

- **Directly applicable to the binomial family** — C(x,k) has simple rational
  roots, so HT23 Thm 1.1's hypothesis is met. It gives a *necessary*
  degree-divisibility condition (k₁ | 2k₂ for infinite families) that is
  checked by the known infinite family (k=2 vs 3) and cannot by itself bound
  the finite pairs.
- **What it does NOT give**: no bound on the number of solutions, no
  uniformity; the infinite-solution characterization is a classification, and
  the bounded-denominator setting is about rational solutions, not integral
  ones. It refines the held HPT 2022 (PTE-indecomposability) result by
  specializing to simple-rational-roots polynomials — the class containing the
  binomials.
- **Relationship to the central obstruction**: HT23 does not break the
  ineffectivity wall — it is a classification (which pairs can be infinite),
  not a count bound. It corroborates that the *only* infinite equal-binomial
  families must satisfy the divisibility condition, matching the known
  Fibonacci family.

## Status

```claim
id: ht23-simple-rational-roots-classification
statement: Hajdu-Tijdeman 2023 (JLMS; arXiv:2204.12345) Thm 1.1: if f in Q[x]
  has only simple rational roots and f(x)=g(y) has infinitely many rational
  solutions with bounded denominator, then deg(f)=ms, deg(g)=ns with m in
  {1,2,3,4,6}, s>0; if both f,g have simple rational roots and deg(f)<=deg(g),
  then m in {1,2}, i.e. deg(f) | 2 deg(g). In the binomial case C(x,k1)=C(y,k2)
  (simple rational roots 0..k-1) this forces k1 | 2 k2 for any infinite family;
  the known infinite Fibonacci family has k1=2, k2=3, so 2 | 6 — consistent.
  Theorems 6.1/9.1: infinite-solution cases are exactly the Prouhet-Tarry-Escott
  (PTE) polynomial structures; Theorem 10.1: for each N only finitely many
  disjoint equal-product blocks of size <=N (Erdos-Turk/Erdos-Graham adjacent).
hypotheses: f (and in Thm 1.1's sharpening, g) has only simple rational roots;
  equation has infinitely many bounded-denominator rational solutions.
holds-here: yes — C(x,k) has simple rational roots; the equal-binomial equation
  is exactly of this shape; the necessary divisibility condition applies to the
  infinite-family classification.
status: sourced (arXiv full text held; digest read; not re-derived here)
bearing: refines HPT 2022 (PTE-indecomposability) to the simple-rational-roots
  class; gives a necessary degree-divisibility condition on infinite
  equal-binomial families, consistent with the known Fibonacci family. Does NOT
  bound N(a) — classification only, no count bound, no uniformity; the
  ineffectivity wall stands.
anchor: research/sources/hajdu-tijdeman-2023-simple-rational-roots.full.md
```

## Note on the two-logarithm approach

This paper's scope confirms that the separated-variables/Bilu–Tichy machinery
classifies *which pairs are infinite*, and nothing in it converts that into an
effectively bounded count. Any proposed "two-logarithm linear form" attack on
the boundary must first produce a **non-zero** linear form — the held
`matveev-explicit-2-3` refutation showed the naive log-ratio is identically
zero at exact equal-values solutions. HT23 is compatible with that trap, not a
way around it.