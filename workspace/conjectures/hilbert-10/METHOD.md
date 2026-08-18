Solve by explicit arithmetic geometry and definability, with the mathematics
carried in Lean wherever it will go. The object is a **formula** — a first-order
formula over the language of rings, in a stated quantifier shape, whose
truth-set in `Q` is `Z` — and everything else is machinery for building one and
for checking it.

Reason about *that formula*. It is assembled from local conditions, and the
instruments are quaternion algebras over `Q` and their ramification sets,
Hilbert symbols and the product formula, the Hasse–Minkowski theorem for
quadratic forms, conics and their rational points, and the norm forms that turn
a local condition into an existential sentence. Koenigsmann's and Poonen's
constructions are the models to reproduce exactly before anything new is
attempted: each is a finite assembly whose every step is checkable.

**Prefer the argument a machine can check.** A Hilbert symbol is computable; a
local solvability condition is decidable; a quantifier count is an integer. So
every claim here has a checkable core, and the pipeline is fixed: state the
formula, evaluate it on an explicit test set of rationals, verify each local
condition symbolically, then state the result in Lean. Where Mathlib carries
Hilbert symbols and quadratic forms, use them; where it does not, record what is
missing — that is a reportable finding.

Three cautions this problem earns before any work starts.

**Quantifier shape is the whole content.** First-order definability of `Z` in
`Q` has been known since 1949 and settles nothing about H10.Q. Every statement
must carry its shape — `∃`, `∀`, `∀∃`, with counts — and every citation must be
checked for which shape it proved. This is the error that has to be designed out
rather than watched for.

**An existential definition of `Z` in `Q` contradicts Mazur's conjecture.** If
an argument here produces one, that is not a bonus: it is a warning that a step
is wrong, and the argument is guilty until every step has survived attack.

**Undecidability over rings of integers and over `Q` are different theorems.**
The number-field results do not transfer to `Q`, and the reason they do not — no
rank-one elliptic curve argument is available over `Q` in the needed form — is
worth stating precisely. Quoting a ring-of-integers result as progress on `Q` is
the second standard error.
