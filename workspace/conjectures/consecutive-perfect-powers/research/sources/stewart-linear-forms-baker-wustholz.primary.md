# Stewart, "Linear forms in logarithms and Diophantine equations" (Baker–Wüstholz; the effective bound)

**Source URL:** https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/stewart.notes_1_0_0.pdf
**Author/venue:** C. L. Stewart, "Linear forms in logarithms and Diophantine
equations" (University of Waterloo mathematics notes). Freely hosted PDF.
**Type:** University lecture notes (primary, freely hosted).
**Status:** CAPTURED full-text excerpt via `read_sources` (server-side). Full
PDF not stored locally (download blocked); exact statements quoted from the PDF
text.

## Why this source is in the library

Second independent full-text treatment of the effective-bound machinery (with
Evertse and Tijdeman). Stewart gives the **Baker–Wüstholz (1993)** explicit
constant form — the sharpest statement of the lower bound, with the concrete
`(16 n d)^(2n+4)` exponent — which is the precise shape that makes the
algorithmically-implicit search bound on an exponential Diophantine equation
astronomically large. It lets the run state the *size* and *shape* of the
effective bound as technique, without retrieving the screen-answer's concrete
constant for `x^p - y^q = 1` itself.

## Verified content (exact statements)

### Height and the form

For algebraic numbers `α_1, …, α_n ≠ 0, 1`, logs on the principal branch,
integers `b_1, …, b_n`, put

    Λ = b_1 log α_1 + … + b_n log α_n.

Let `d = [Q(α_1, …, α_n) : Q]`; `H(α)` the naive height (max abs coefficient
of the primitive minimal polynomial); `A_i = max(H(α_i), e)`;
`B = max(|b_1|, …, |b_n|, e)`.

### Theorem 2 (Baker & Wüstholz, 1993)

If `Λ ≠ 0`, then

    |Λ| > exp( − (16 n d)^(2n+4) · (log A_1) · … · (log A_n) · log B ).

This is the explicit-est constant form, and it is the source of the double-exponential
quality: as the heights and coefficients grow, the bound shrinks so fast that
the induced upper bound on solutions is not remotely exhaustible.

### Corollary / Proposition (simplified height-only form)

If `Λ ≠ 0` then `|Λ| > exp(− C(n,d,A) · B·log(...))` for a computable `C`; the
notes also record the weaker elementary bound `|Λ| > exp(− n d (log 3A) B)`.
These are the workhorse estimates that, via a near-equality argument, convert
"two powers of integers are within 1 of each other" into an explicit but huge
upper bound on `x, y`.

## Relation to the run's problem and the falsifier

- **Technique, not answer.** Stewart's notes describe the *general* Baker
  machinery and how it bounds solutions of exponential Diophantine equations
  like `a^x − b^y = 1` for *fixed* `a, b`. They do not give a concrete
  numerical constant for the run's `x^p − y^q = 1` (that would be the
  screen-answer). They supply the shape: `max{x,y} ≤ C(a,b)`, explicit but
  astronomically large.
- **Falsifier check.** Baker bounds are one-sided (upper bounds on solutions);
  they never assert non-existence. Evaluated at the known solution
  `3^2 − 2^3 = 1` they are satisfied trivially and imply nothing about it, so
  no claim here eliminates a solution.

## Claims

```claim
id: baker-wustholz-explicit-constant
statement: >
  If Lambda = sum b_i log alpha_i != 0 (b_i integers, alpha_i algebraic
  != 0,1, principal logs) and d = [Q(alpha_1,...,alpha_n):Q], A_i =
  max(H(alpha_i), e), B = max(|b_i|, e), then
  |Lambda| > exp(-(16 n d)^(2n+4) * prod log A_i * log B). (Baker-Wustholz
  1993, Theorem 2 in Stewart's notes.)
hypotheses: Lambda != 0; logs principal; H naive height.
holds-here: yes — the concrete shape that makes the effective bound on
  x^p - y^q = 1 astronomically large and non-exhaustible.
status: sourced (primary course text, exact constant form quoted; cross-checks
  Evertse Thm 5.2 and Tijdeman survey).
anchor: research/sources/stewart-linear-forms-baker-wustholz.primary.md
bearing: the explicit constant in the lower bound; establishes the orders of
  magnitude separating the effective bound from feasibility, per GOAL.
```

```claim
id: effective-method-sketched
statement: >
  Stewart's notes sketch the four-step Baker method by which a nonzero linear
  form in logs of algebraic numbers yields an explicit upper bound on the
  integer exponents of equations such as a^x - b^y = 1 (fixed coprime bases,
  fixed c): compare a Baker lower bound |Lambda| > (eB)^-C with an upper bound
  on |Lambda| from the near-equality imposed by the equation, read off a bound
  on the exponents, then search a finite (but huge) region.
hypotheses: a, b fixed positive > 1 coprime; x, y >= 1.
holds-here: partial — the run's bases x, y are also unknown, but the shape of
  the method is the source of the "finite but not computable" property.
status: sourced (primary course text, method quoted).
anchor: research/sources/stewart-linear-forms-baker-wustholz.primary.md
bearing: the unquotable concrete bound's *shape*; lets the run say precisely
  why a computational search cannot close the gap, without storing a published
  answer.
```
