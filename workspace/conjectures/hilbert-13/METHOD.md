Solve by explicit Galois theory and elimination, with the mathematics carried in
Lean wherever it will go. There are two objects and they need opposite methods.

**Upper bounds are constructions.** A bound `RD(n) ≤ d` is a *tower* of
Tschirnhaus transformations, each step an explicit change of variable that kills
coefficients and leaves an `≤ d`-parameter family. The content is the surviving
parameter count, so the instruments are resultants, elimination ideals, Gröbner
bases over `Q(a_1, …, a_k)`, and exact dimension computations of the resulting
varieties. Never count parameters in prose: eliminate, and read the dimension
off the ideal. A construction is checkable, and every one this run touches —
published or new — should be reproduced exactly before it is believed.

**Lower bounds are obstructions, and none exist.** The instruments there are
essential dimension and its cohomological invariants, the structure of `S_n` and
its subgroups, versal torsors, and the behaviour of all of these under towers.
The whole difficulty is the tower: an invariant that drops under one pullback
but not under a composite is useless. Any lower-bound attempt must begin by
saying what it does with towers, and must be tested against `n = 5`, where the
answer is known to be 1.

**Prefer the argument Lean can finish.** A Tschirnhaus reduction is a polynomial
identity: it can be stated and verified by `ring` once the transformation is
written down, and the parameter count is a statement about an ideal. State every
claim as a Lean type before spending an attempt on it; a claim whose hypotheses
will not go into binders is one nobody has pinned down. Cited results are
`axiom`s under `namespace Cited` with their source in the docstring, and are
`conditional`, never `formalised`.

Three cautions this problem earns before any work starts.

**The continuous problem is solved and is not this problem.** Kolmogorov–Arnold
is about continuous superpositions. Any argument that would apply to continuous
functions has proved a theorem from 1957, and citing Kolmogorov–Arnold as
progress on the algebraic question is the standard error here.

**Essential dimension is not a lower bound for resolvent degree.** `ed(S_n) ≥
⌊n/2⌋` is a theorem and does *not* give `RD(n) ≥ ⌊n/2⌋`. Any argument reaching a
lower bound through essential dimension must state exactly where it beats the
tower, or it is refuted.

**A dimension count is not an elimination.** Most wrong upper bounds in this
subject are parameter counts that ignore a degeneration. Run the elimination,
over `Q`, and report the ideal.
