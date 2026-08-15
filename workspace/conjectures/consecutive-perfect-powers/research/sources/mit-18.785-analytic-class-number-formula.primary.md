# MIT 18.785, Lecture 18 — The analytic class number formula (cyclotomic case)

**Source URL:** https://math.mit.edu/classes/18.785/2015fa/LectureNotes18.pdf
**Author/venue:** MIT 18.785 "Number Theory I" (Fall 2015), Lecture 18 notes.
**Type:** University course notes (primary, freely hosted).
**Status:** CAPTURED full-text excerpt via `read_sources` (server-side). Full
PDF not stored locally (download blocked by network boundary); the exact
theorem statements quoted below were read directly from the page.

## Why this source is in the library

PROVENANCE.md records that the canonical text references (Milne ANT, Washington
GTM 83) were captured only at ToC/metadata level. This MIT lecture is a freely
hosted primary source for the same machinery the both-odd-prime case of
`x^p - y^q = 1` sits in: the analytic class number formula, and how the
Dedekind zeta function of the cyclotomic field factors as a product of
Dirichlet L-functions. It is the foundation of the relative class number
formula `h^-(Q(ζ_p)) = 2p·∏_{χ odd} (-½ B_{1,χ})` that the run's
`minus-class-number-formula` claim uses, and it is exactly the "how" that a
catalogue (OEIS A000927) cannot supply.

## Verified content (exact statements quoted from the notes)

### Cyclotomic zeta function factors over Dirichlet L-functions

Let `ζ_m` be a primitive `m`-th root of unity, `K = Q(ζ_m)`. The Galois group
`Gal(K/Q) ≅ (Z/mZ)^×` sends `σ ∈ Gal(K/Q)` to the `a ∈ (Z/mZ)^×` with
`σ(ζ_m) = ζ_m^a`; for primes `p ∤ m`, the Frobenius `σ_p` maps to `p mod m`.

**Theorem 18.2.** Let `K = Q(ζ_m)`. Then

    ζ_K(s) = ∏_χ L(s, χ)

where `χ` ranges over the primitive Dirichlet characters of conductor dividing
`m`.

### The analytic class number formula (general statement)

Let `K` be a number field of degree `n` with `r` real and `s` complex places.
`h_K = #cl(O_K)` is the class number, `R_K` the regulator, `w_K` the number of
roots of unity in `K`, `D_K` the discriminant. The Dedekind zeta function has a
simple pole at `s = 1` with residue

    ρ_K = (2^r (2π)^s R_K h_K) / (w_K · |D_K|^{1/2}).

Equivalently,

    h_K R_K = (w_K · |D_K|^{1/2} / (2^r (2π)^s)) · Res_{s=1} ζ_K(s).

### Why it matters for the run

For `K = Q(ζ_p)` with `p` odd prime: `r = 0`, `s = (p-1)/2`, `w_K = 2p`,
`D_K = (-1)^{(p-1)/2} p^{p-2}`. Combined with Theorem 18.2 and the
plus-minus split `h = h^+·h^-`, this is exactly the route to the relative
class number formula in terms of the Dirichlet L-values `L(1, χ)` for `χ` odd,
and hence the generalized Bernoulli numbers `B_{1,χ}`. The `minus-class-number-formula`
claim in this library (`h^- = 2p·∏_{χ odd} (-½ B_{1,χ})`) is the explicit
evaluation of this factorization; this source supplies the analytic
scaffolding it rests on.

## Falsifier note

The analytic class number formula is a theorem about any number field and gives
the *size* of the class group; it neither asserts nor denies the existence of a
second solution of `x^p - y^q = 1`. Evaluated at the known solution
`(3,2,2,3)` it is satisfied (it just computes class numbers), so it is
consistent with the falsifier discipline — it never implies "no solution
exists."

## Claims

```claim
id: mit-zeta-factors-over-L-series
statement: >
  For K = Q(zeta_m), the Dedekind zeta function factors as
  zeta_K(s) = prod over primitive Dirichlet characters chi of conductor
  dividing m of L(s, chi). (MIT 18.785 Lecture 18, Theorem 18.2.)
hypotheses: K = Q(zeta_m), m >= 1; chi runs over primitive characters mod a
  divisor of m.
holds-here: yes — for the run's K = Q(zeta_p) (p odd prime) this is the L-series
  factorization underlying the relative class number formula h^-(Q(zeta_p)).
status: sourced (primary course notes, exact statement quoted).
anchor: research/sources/mit-18.785-analytic-class-number-formula.primary.md
bearing: analytic lever from Dedekind zeta to Dirichlet L-values at s = 1; the
  structural step behind every formula in the minus-class machinery.
```

```claim
id: analytic-class-number-formula
statement: >
  For a number field K of degree n with r real and s complex places, the
  Dedekind zeta function has a simple pole at s = 1 with residue
  rho_K = 2^r (2 pi)^s R_K h_K / (w_K |D_K|^1/2), where h_K, R_K, w_K, D_K are
  the class number, regulator, number of roots of unity, and discriminant.
  (MIT 18.785 Lecture 18.)
hypotheses: K any number field.
holds-here: yes — applies to K = Q(zeta_p) with r = 0, s = (p-1)/2, w = 2p,
  D_K = (-1)^((p-1)/2) p^(p-2).
status: sourced (primary course notes, exact statement quoted).
anchor: research/sources/mit-18.785-analytic-class-number-formula.primary.md
bearing: the structural theorem that turns a zeta residue into the class
  number; the root of the analytic class number formula in the relative-class
  machine.
```
