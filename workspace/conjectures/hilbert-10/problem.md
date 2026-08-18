# Hilbert's 10th problem — over the rationals

## The original question, and its answer

> Give a procedure which decides, for an arbitrary Diophantine equation with
> integer coefficients, whether it has a solution in integers.

**No such procedure exists** — Davis, Putnam, Robinson and Matiyasevich (1970):
every recursively enumerable set is Diophantine, so the solvability of
`f(x_1, …, x_n) = 0` over `Z` is undecidable. The original question is closed
and is **not** this workspace's target.

## The target

The same question over other rings is open, and the outstanding case is the
field of rational numbers.

> **(H10.Q)** Is there an algorithm deciding whether a polynomial equation with
> rational coefficients has a rational solution?

The expected answer is no. The standard route to it is a **Diophantine
definition of `Z` in `Q`**: an existential formula `φ(t)` over `Q` with
`φ(t) ⟺ t ∈ Z`. Given one, undecidability over `Q` follows immediately from
MRDP. So the concrete target is:

> **(H10.def)** Is `Z` existentially (Diophantine-) definable in `Q`?

Recalled status — **every item to be confirmed or struck against a primary
source**:

- **Robinson (1949)** gave a *first-order* definition of `Z` in `Q`, with
  quantifier alternation — enough for undecidability of the full first-order
  theory of `Q`, **not** enough for H10.Q, which needs a purely existential
  definition.
- **Poonen** produced a `∀∃`-definition of `Z` in `Q` with a small number of
  quantifiers of each kind, using quaternion algebras and the Hasse–Minkowski
  local–global principle.
- **Koenigsmann (2016)** gave a **universal** (`∀`-only) definition of `Z` in
  `Q` — equivalently, an existential definition of the complement — and an
  explicit quantifier count. Reducing that count, and closing the gap between a
  universal definition and an existential one, is the live technical frontier.
- **Rings of integers of number fields.** Recalled as *recently settled*:
  Hilbert's tenth problem is undecidable over the ring of integers of every
  number field, by work using elliptic curves of rank one (Koymans–Pagano; and
  Alpöge–Bhargava–Shnidman by a different route). **Confirm this, and confirm
  which statement exactly was proved**, because it changes what remains open.
- **Mazur's conjecture** — that the real topological closure of the rational
  points of a variety has finitely many connected components — is the standard
  *obstruction*: it is inconsistent with `Z` being Diophantine in `Q` (since
  `Z` is discrete and infinite). So H10.def and Mazur's conjecture cannot both
  hold, and this tension is what makes the problem delicate rather than merely
  hard.

## Where a machine has traction

Everything in this circle is explicit: quaternion algebras over `Q`, Hilbert
symbols, local conditions at each place, conics and their rational points, and
formulas whose quantifier count is a finite integer that a program can verify.
The reductions are checkable, and a formula's correctness on a stated finite
test set is a real experiment.

## The cheap tests every candidate must pass first

1. **The quantifier test.** Every claimed definition of `Z` in `Q` must have its
   quantifier *shape* stated exactly — `∃`, `∀`, `∀∃`, with counts — and be
   checked against what that shape suffices for. Only a purely existential
   definition settles H10.Q; a `∀∃` definition, however elegant, does not, and
   confusing the two is the standard error here.
2. **The Mazur test.** Any claimed existential definition of `Z` in `Q`
   *refutes* Mazur's conjecture. That is allowed — but a run that produces one
   without noticing it has contradicted a widely believed conjecture has almost
   certainly erred. State the consequence explicitly and treat it as evidence
   against the argument until every step survives.
3. **The local test.** Every formula in this subject is assembled from local
   conditions at the places of `Q`. A claimed definition must be checked at each
   place, and on explicit numerical instances: does `φ(t)` actually hold for
   `t = 0, 1, −1, 1/2, 2/3, …`? A formula that fails on `t = 1/2` is refuted in
   seconds, and this check must run before any argument is written down.

## What is genuinely unknown

- H10.Q itself, and H10.def.
- The minimal number of quantifiers in a universal definition of `Z` in `Q`.
- Whether the complement of `Z` in `Q` is Diophantine (equivalent to
  Koenigsmann's direction) with a substantially simpler formula.
- Undecidability of H10 over other rings of arithmetic interest not covered by
  the number-field results: rings of integers of infinite extensions, `Z[1/p]`-
  type rings in some regimes, and function-field analogues in characteristic 0.
- Mazur's conjecture, in either direction.
- The decidability of the existential theory of `Q` in restricted degrees — even
  the case of *systems of quadratic* equations, where Hasse–Minkowski gives
  decidability, versus degree 3, where nothing is known. **The degree-3 case —
  deciding whether a cubic surface has a rational point — is an open, concrete,
  and highly computational target in its own right.**

## What counts as a result

In descending order of value.

1. An existential definition of `Z` in `Q`, or a proof that none exists. Either
   is a landmark; neither should be claimed lightly.
2. A universal definition of `Z` in `Q` with **fewer quantifiers** than the
   published record, verified numerically on a test set and proved.
3. A decidability or undecidability result for the existential theory of `Q`
   restricted to a stated class of equations — degree, number of variables, or
   shape — with the boundary of the class stated exactly.
4. A machine-verified reproduction of a published definition (Poonen's or
   Koenigsmann's), with each local condition checked and the quantifier count
   confirmed. Nobody has produced this as a verified artifact.
5. An algorithm, with its correctness proved, deciding rational solvability for
   a named family (diagonal cubics of a stated shape, say), with its ceiling
   measured.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim H10.Q.** A run that reduces a quantifier count or verifies a
published definition has done something real; one that announces undecidability
over `Q` has made an error.
