# Hilbert's 11th problem — quadratic forms, and what is still open

## The original question, and its answer

> Classify quadratic forms in any number of variables with algebraic numerical
> coefficients — over a number field and over its ring of integers.

Over a **field**, the answer is the Hasse–Minkowski local–global principle: two
quadratic forms over a number field `K` are equivalent iff they are equivalent
over every completion of `K`, and a form represents a value globally iff it does
so everywhere locally. Over `Q` this is classical; over number fields it is
Hasse. So the field case is closed and is **not** this workspace's target.

Over **rings of integers** the local–global principle fails, and what is left is
open, concrete, and highly computational. That is the target.

## The targets

### T1. Universal quadratic forms over number fields

A positive definite integral quadratic form over `O_K` is **universal** if it
represents every totally positive element of `O_K`.

Recalled — **to be confirmed or struck against sources**:

- Over `Z`: the **15 theorem** (Conway–Schneeberger, with Bhargava's proof) —
  a positive definite integer-*matrix* form representing `1, 2, 3, 5, 6, 7, 10,
  14, 15` represents every positive integer; and the **290 theorem**
  (Bhargava–Hanke) for integer-*coefficient* forms, with an explicit critical
  set. Lagrange's four-square theorem is the ancestor.
- Over real quadratic fields `Q(√D)`: the minimal **rank** of a universal form
  grows with `D`, and the growth rate is only partially known —
  Blomer–Kala and Kala's work show it is unbounded, with lower bounds tied to
  the continued fraction expansion of `√D`. **Exact minimal ranks are known for
  only finitely many `D`, and each new one is a result.**
- The analogue of the 15/290 theorem over number fields — a finite critical set
  proving universality — is known in some cases and open in general.

> **(H11.U)** For a given totally real number field `K`, what is the minimal
> rank of a universal quadratic form over `O_K`, and is there a finite critical
> set deciding universality?

### T2. The `u`-invariant

`u(K)` is the largest dimension of an anisotropic quadratic form over `K`.
Recalled: `u(Q_p) = 4`; `u(Q_p(t)) = 8` (Parimala–Suresh, `p` odd);
**`u(Q(t))` is unknown**, and even whether it is finite. Merkurjev showed every
even value is attained by some field. This is a clean open question about
polynomials over `Q`.

### T3. Effective local–global

Hasse–Minkowski is effective in principle. The explicit bounds — how small a
solution must exist if one exists (Cassels' theorem and its descendants), and
how large the coefficients of an equivalence can be forced to be — are open to
improvement, and every improvement is checkable computationally.

## The cheap tests every candidate must pass first

1. **The local test.** Every claim about representation or equivalence must be
   checked at every place first: real places (signature), and each finite place
   dividing the discriminant. A global claim contradicting a local obstruction
   is an arithmetic error, found in seconds, and the check is cheap.
2. **The escalation test.** Universality claims are established by *escalation*:
   build up the lattice by repeatedly adjoining a vector representing the
   smallest unrepresented value, and check every resulting form. A universality
   claim not backed by a complete escalation tree, with the tree's size
   reported, is a conjecture. Bhargava's proofs are exactly this and their
   content is the completeness of the tree.
3. **The definiteness test.** Positive definite and indefinite forms behave
   completely differently over rings of integers — indefinite forms of rank ≥ 3
   satisfy strong approximation and a local–global principle, definite ones do
   not. Every statement must say which case it is about; conflating them is the
   standard error.

## What is genuinely unknown

- The minimal rank of a universal form over `Q(√D)` for all but finitely many
  `D`, and the exact growth rate in `D`.
- A 290-type theorem over a general totally real number field.
- `u(Q(t))`, including whether it is finite.
- Effective bounds in Hasse–Minkowski better than the published ones.
- Which totally positive elements are represented by named forms over named
  fields — the "exceptions" tables, which are finite and computable but largely
  uncomputed.
- Class numbers of quadratic lattices and the failure of local–global,
  quantified: how large the genus of a form can be relative to its
  discriminant.

## What counts as a result

In descending order of value.

1. A minimal universal rank determined exactly for a real quadratic field where
   it was unknown, with the lower bound *proved* (not merely a failed search)
   and the upper bound exhibited as an explicit form.
2. A 290-type critical set for a named number field, with the escalation tree
   complete and its size reported.
3. Any bound on `u(Q(t))`, or a new anisotropic form over `Q(t)` of dimension
   larger than the published record.
4. An improved effective bound in a local–global statement, with the
   improvement verified computationally on a generated family.
5. An exhaustive table — universal forms of a given rank over `Q(√D)` for `D`
   in a stated range, with the search bound and the ceiling recorded.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim universality from a search.** A form representing everything the
program tested is a form with no known exception, which is a different statement
and must be labelled as one.
