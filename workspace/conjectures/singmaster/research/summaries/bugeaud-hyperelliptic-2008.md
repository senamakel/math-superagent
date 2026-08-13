# Integral points on hyperelliptic curves (effective method)

Source: Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, Sz. Tengely,
"Integral points on hyperelliptic curves", Algebra & Number Theory 2:8 (2008)
859–885; arXiv:0801.4459.
Full text: `research/sources/bugeaud-hyperelliptic-2008.full.md`.

## What it establishes

For a hyperelliptic curve `C: Y^2 = a_n X^n + ... + a_0` with `n >= 5` and the
right-hand polynomial squarefree/irreducible, this gives:

1. **A completely explicit upper bound** on the integral points, combining
   Matveev's bounds for linear forms in logarithms, refined height estimates
   (Voutier, Bugeaud), and regulator estimates (Landau). The bound is usable
   *provided* one knows a rational point on `C` and a Mordell–Weil basis for
   the Jacobian `J(Q)`.
2. **A refined Mordell–Weil sieve** that, combined with the bound, can
   determine *all* integral points.

Illustrated by completely determining the integral points on the genus-2
models `Y^2 - Y = X^5 - X` and `Y^2 = X^5`.

Remark (from the paper's introduction) that underlies how these bounds were
historically seen as "astronomical": even with improvements the constants are
enormous. This paper's contribution is to make the bound *explicit* (hence
usable) and then drive it down with the sieve.

## Relevance to this run

This is the **method paper** behind the `C(x,2)=C(y,5)` binomial case
(Bugeaud–Mignotte–Siksek–Stoll–Tengely, credited in de Weger/MRSTT): the
binomial-equality curve for that pair is hyperelliptic and this is how its
integral points were settled. It is the machine that would produce *one specific
effective bound with a computed constant* for a chosen `(k1,k2)` family — one
of the four GOAL deliverables.

It does **not** give a bound uniform in `(k1,k2)`: every constant depends on
the specific curve (height, discriminant, regulator, Mordell–Weil rank), and
the Mordell–Weil-basis requirement is not effective uniformly in `n`. So this
confirms the shape of the obstruction: effective per-pair, not uniform in the
pair, via an explicitly-compu-table route when the curve data is available.

Evidence class: sourced (full text read).

```claim
id: bmsst-hyperelliptic-effective-method
statement: Bugeaud-Mignotte-Siksek-Stoll-Tengely 2008 (Algebra & Number Theory
  2:8, 859-885; arXiv:0801.4459): for a hyperelliptic curve C: Y^2 = a_n X^n +
  ... + a_0 with n >= 5 and squarefree/irreducible RHS, a COMPLETELY EXPLICIT
  upper bound on the integral points follows from Matveev's linear-forms bounds,
  refined height estimates (Voutier, Bugeaud), and regulator estimates (Landau),
  PROVIDED one knows a rational point on C and a Mordell-Weil basis for J(Q);
  combined with a refined Mordell-Weil sieve this determines ALL integral
  points. Their Theorem 3 gives log|x| <= 8A*_1 log(4A*_1) + 8A*_2 + H* + ...
  with A*_1 containing C(L,2r+1)(c*_1)^2 d R^2 (regulator squared, unit ranks,
  Matveev constants of K = Q(alpha)); worked examples have log x bounds
  10^263-10^565, reduced by the sieve (index ~10^3240 over ~10^5 primes).
hypotheses: hyperelliptic with irreducible RHS of degree n>=5; a rational point;
  explicit MW basis of the Jacobian; explicit canonical-height-difference
  bounds (available only for genus 2 at present - BMSST p.2 verbatim: no such
  bounds are known for genus >= 3).
holds-here: yes for the solved (2,5) pair (the curve C(x,2)=C(y,5) is BMSST
  equation (4), genus 2, Jacobian rank 3); the genus>=3 gap means the family
  beyond a small initial segment is inaccessible to this route.
status: asserted-by-source (primary full text read)
bearing: the method engine behind the (2,5) complete solution and a concrete
  template for an effective per-pair bound with computed constants (GOAL
  deliverable); confirms the effective-methods-wall obstruction (per-curve
  data required, not uniform in (k1,k2)).
anchor: research/sources/bugeaud-hyperelliptic-2008.full.md
```
