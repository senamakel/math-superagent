# Hilbert's 12th problem — Kronecker's Jugendtraum

## The question

> Extend the Kronecker–Weber theorem to an arbitrary base number field: describe
> explicitly the analytic functions whose special values generate the abelian
> extensions of a given number field `K`, as the exponential does for `K = Q`
> and elliptic/modular functions do for imaginary quadratic `K`.

The two solved cases, and the shape they set:

- **`K = Q`** — Kronecker–Weber: every finite abelian extension of `Q` lies in
  a cyclotomic field `Q(ζ_n)`, so the values `e^{2πi/n}` of the exponential
  generate everything.
- **`K` imaginary quadratic** — the theory of complex multiplication: values of
  the `j`-function at CM points generate the Hilbert class field, and torsion of
  the corresponding elliptic curve (Weber functions) generates the ray class
  fields.

Class field theory describes the abelian extensions of any `K` *abstractly* —
the Galois group is a ray class group — but gives no generators. **The explicit
question is open for every other `K`, and the first open case is the simplest
one imaginable: a real quadratic field.**

> **(H12.rq)** Give explicit analytic functions and special values generating
> the abelian extensions of a real quadratic field `K = Q(√D)`.

## The state of the art

Recalled — **every item to be confirmed or struck against a primary source**:

- **Stark's conjectures** predict that the leading term of an Artin `L`-function
  at `s = 0` is a regulator built from an explicit unit — the **Stark unit** —
  living in the abelian extension, and that this unit generates it. The rank-one
  abelian case over a totally real field is the sharpest and most tested form.
- **Brumer–Stark**: recalled as proved (away from 2, then completely) by
  **Dasgupta–Kakde**, who also give a `p`-adic analytic construction of the
  Brumer–Stark units and, with it, an explicit `p`-adic answer to Hilbert's
  twelfth for totally real fields. **Confirm exactly what was proved, over
  which fields, and whether the construction is `p`-adic only** — that last
  point decides what remains open.
- **Shintani**, **Hayes**, **Darmon–Dasgupta–Pollack–Vonk** and others supply
  `p`-adic constructions (real quadratic singular moduli, "`p`-adic RM theory")
  whose complex-analytic counterparts are conjectural.
- The **archimedean/complex-analytic** case of real quadratic fields — the
  original Jugendtraum shape, functions on the upper half plane whose values at
  real quadratic points generate class fields — remains **open**.
- Stark units are computable to high precision and their minimal polynomials
  are then recognisable over `Q`. This is the mechanism that makes the subject
  testable at all, and it is what a machine can do well.

## Where a machine has traction

- **Compute a Stark unit numerically** from partial zeta values to high
  precision, form its minimal polynomial, and **verify exactly** that the field
  it generates is the predicted ray class field — degree, discriminant, Galois
  group, ramification. Each verified case is a genuine data point and several
  published tables are small.
- **Class field theory itself is computable**: ray class groups, conductors,
  and defining polynomials of abelian extensions come from standard algorithms.
- **The verification step is exact.** A numerical unit is a guess; the minimal
  polynomial it produces either does or does not cut out the right field, and
  that is decidable over `Q`.

## The cheap tests every candidate must pass first

1. **The class-group test.** Any claimed generator of an abelian extension must
   produce a field of exactly the degree the ray class group predicts, with the
   right conductor and ramification. Compute the ray class group *first*; a
   candidate whose degree disagrees is refuted before its analysis is read.
2. **The recognition test.** A numerically computed unit is a lead. It becomes a
   claim only when its minimal polynomial is recognised over `Q` (or over `K`)
   **and** verified exactly — the polynomial's roots checked to match the
   numerics, its splitting field checked to be the target. Report the precision
   used and the height of the coefficients; a recognition at the edge of the
   precision is not a recognition.
3. **The `p`-adic/complex test.** A `p`-adic construction is not an answer to
   the archimedean question, and the two are routinely conflated in summaries.
   Every statement must say which it is about, and a claim of "Hilbert 12 for
   totally real fields" must carry the qualifier the theorem carries.

## What is genuinely unknown

- H12.rq in the complex-analytic sense, for every real quadratic field.
- Explicit generation for any `K` that is neither `Q` nor imaginary quadratic,
  outside the `p`-adic results.
- Stark's conjecture itself in the general (higher rank, non-abelian) cases.
- Whether the `p`-adic constructions have complex-analytic counterparts, and
  what the correct "real quadratic `j`-function" would be.
- Extensive verified tables: for how many real quadratic fields and conductors
  has a Stark unit actually been computed and its field verified? The answer is
  small, and enlarging it is real work.

## What counts as a result

In descending order of value.

1. A complex-analytic construction, proved, generating a class field of a real
   quadratic field — the Jugendtraum itself. Do not claim this.
2. A verified extension of the Stark-unit tables: new fields and conductors,
   each with the unit computed, its minimal polynomial recognised, and the
   generated field **verified exactly** against the ray class group. This is
   reachable and is the run's most likely real contribution.
3. A counterexample or a precise failure of a stated form of Stark's conjecture
   in a case the literature has not tested — with the numerics reproducible and
   the precision reported.
4. An algorithmic improvement — computing Stark units to a given precision
   faster or in cases where the standard method stalls — with measurements.
5. A precise statement of what a complex-analytic counterpart of the
   Dasgupta–Kakde construction would have to satisfy, derived from the `p`-adic
   one, with the obstruction to producing it named.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim Hilbert's twelfth problem**, and do not report a `p`-adic
statement as an archimedean one. A recognised minimal polynomial with its field
verified is a result; a high-precision number is not.
