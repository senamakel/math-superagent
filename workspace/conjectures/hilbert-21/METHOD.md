Solve by explicit linear algebra over number fields against certified numerical
continuation, with the mathematics carried in Lean wherever it will go. There
are exactly two objects and one map between them: a **representation** — an
`n`-tuple of matrices with product the identity, up to simultaneous
conjugation — and a **Fuchsian system** — an `n`-tuple of residues summing to
zero. The map is monodromy, and every question is about its image.

Reason about *the obstruction*. Realisability is controlled by the holomorphic
vector bundle on `CP¹` that a system with the given monodromy defines: the
splitting type of that bundle, the admissible exponents at each singular point,
and the Fuchs relation tying them together. Bolibrukh's counterexample is a
representation whose every compatible bundle splits too unevenly for a
first-order pole. So the instruments are: invariant-subspace computation over a
number field, Levelt filtrations and exponents, bundle splitting types and
elementary transformations, and the integer arithmetic of the Fuchs relation.

**Numerics search, certificates decide.** The monodromy of an explicit system is
computable by numerical continuation of the ODE around each loop — fast, and the
right way to *test* a candidate. It concludes nothing: a matrix agreeing with a
target to twelve digits is a lead until an interval-arithmetic continuation
brackets it or the residues are exhibited exactly over a number field.

**Prefer the argument Lean can finish.** The Fuchs relation is integer
arithmetic; irreducibility is a finite linear-algebra check; a specific
representation's realisability by a specific explicit system, once the exponents
are known, is a finite verification. State every claim as a Lean type before
spending an attempt on it, and record what today's Mathlib cannot carry — its
ODE and monodromy support is the thing to probe first.

Three cautions this problem earns before any work starts.

**Regular singular is not Fuchsian.** Plemelj's theorem, stated for regular
singularities, is true; Hilbert's question, about simple poles, is false. Every
statement in this workspace says which it is about, and an argument that never
controls the pole order has proved the wrong theorem. This is the exact error
that stood unnoticed for eighty years.

**Every counterexample is reducible.** Bolibrukh–Kostov is a theorem: check
irreducibility before anything else, and an irreducible candidate counterexample
is a bug, not a discovery.

**A failed search for residues proves nothing.** The residue space is
high-dimensional and the search is delicate. Non-realisability comes from a
bundle-splitting obstruction and the Fuchs relation, and every claim states
which obstruction closed it.
