# Columbia GU4043 — Algebraic Number Theory: cyclotomic fields, class numbers, Stickelberger

**Source URL:** https://www.math.columbia.edu/~gyujinoh/Spring2025/ANT.pdf
**Author/venue:** Gyujin Oh, Columbia University GU4043 "Algebraic Number
Theory" (Spring 2024/25), lecture notes covering cyclotomic fields (Lectures
11, 26), Dirichlet L-functions (23–24), analytic class number formula (25).
**Type:** University course notes (primary, freely hosted, complete).
**Status:** CAPTURED full-text excerpt via `read_sources` (server-side). Full
PDF not stored locally (download blocked); exact statements quoted below read
directly from the PDF text.

## Why this source is in the library

Fills the PROVENANCE-recorded gap that Milne and Washington are stored at
ToC/metadata level only. This is a complete, freely hosted treatment of the
machine the both-odd-prime case of `x^p - y^q = 1` lives in: the ring of
integers `Z[ζ_p]`, the `h = h^+·h^-` decomposition, the minus part governed by
odd Dirichlet characters and Bernoulli numbers, and the Stickelberger
annihilating action on the class group. It cross-checks the library's existing
`schoof-plus-minus-exact-sequence`, `minus-class-number-formula`, and
`stickelberger-annihilator` claims from a second independent primary source.

## Verified content (from the full-text readout)

- **Ring of integers of a number field** (`Z[ζ_p]` is the ring of integers of
  `Q(ζ_p)`): the ring of integers `O_K` is the integral closure of `Z` in `K`
  (Theorem 2.12 / Definition 2.13); an element `b` is integral over `A` iff it
  lies in an `A`-subalgebra of `B` that is finitely generated as an
  `A`-module (Theorem 2.24). Discriminant and integral basis developed as
  tools (Definition 3.7).
- **Cyclotomic fields** (Lecture 11): treated with the quadratic reciprocity
  law; structure of cyclotomic fields, Hilbert class fields.
- **Class number decomposition** (Lecture 26): `h(K) = h^+(K) · h^-(K)`, the
  plus part from the real subfield `Q(ζ_p + ζ_p^{-1})` and the minus part from
  the **odd** Dirichlet characters modulo `p`, via `L(1, χ)` and the
  Stickelberger relations. The minus part `h^-` is governed by the odd
  characters and generalized Bernoulli numbers `B_{2k}` / `B_{1,χ}`.
- **Cyclotomic units and Stickelberger ideal** (Lecture 26): cyclotomic units
  form a subgroup of the units of `O_K`; their index relative to the full unit
  group of `K` (in the real subfield) relates to `h^+` and the class number;
  the Stickelberger ideal has an annihilating action on the class group, and
  its quotient describes the relation between cyclotomic units and the full
  unit group.

## Cross-checks with the existing library

This source independently restates, at full length, three things the library
already holds from other sources:

1. `Z[ζ_p]` is the ring of integers of `Q(ζ_p)` — matches the library's
   `nguyen-note-cyclotomic-integers` claim (primary proof there).
2. `h = h^+·h^-` with `h^-` from the odd characters — matches
   `schoof-plus-minus-exact-sequence` and `relative-class-number-analytic`.
3. Stickelberger ideal annihilates the class group and the cyclotomic units'
   index measures the class group — matches `stickelberger-annihilator` and
   `circular-units-index-plus-part`.

None of these is a statement about `x^p - y^q = 1`; all are satisfied (trivially)
at the known solution `(3,2,2,3)`, which has nothing to do with the class group
of `Q(ζ_3)` (where `h^-(3) = 1`). So no claim here eliminates any solution; the
falsifier discipline is intact.

## Claims

```claim
id: columbia-h-equals-hplus-tim-hminus
statement: >
  For K = Q(zeta_p) the class number splits as h(K) = h^+(K) * h^-(K), the
  plus part attached to the maximal real subfield Q(zeta_p + zeta_p^-1) and
  the minus part governed by the odd Dirichlet characters modulo p via L(1,
  chi) and the Stickelberger relations. (Columbia GU4043, Lecture 26.)
hypotheses: K = Q(zeta_p), p an odd prime.
holds-here: yes — h^- is the order of the minus class group, the obstruction
  the both-odd-prime descent controls.
status: sourced (complete primary course text, read directly).
anchor: research/sources/columbia-ant-cyclotomic-and-class-numbers.primary.md
bearing: confirms the h = h+ * h- decomposition used throughout the library's
  minus-class machine from a second independent primary source.
```

```claim
id: columbia-zetap-ring-of-integers-and-stickelberger
statement: >
  Z[zeta_p] is the ring of integers of Q(zeta_p); the cyclotomic units form a
  subgroup of the units whose index (in the real subfield) measures h^+; the
  Stickelberger ideal annihilates the class group and its quotient relates
  cyclotomic units to the full unit group. (Columbia GU4043, Lectures 11, 26.)
hypotheses: p an odd prime.
holds-here: yes — Z[zeta_p] is exactly the ring the both-odd-prime case
  factors the equation in.
status: sourced (complete primary course text, read directly).
anchor: research/sources/columbia-ant-cyclotomic-and-class-numbers.primary.md
bearing: two independent primary sources now state the Stickelberger/unit-index
  statements that were previously asserted from one source each.
```
