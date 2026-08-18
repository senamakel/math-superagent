Solve by extremal and probabilistic combinatorics on tournaments, with a SAT
oracle underneath every construction and every exhaustive claim. Property `S_n`
is a first-order condition on a finite structure, so "is there a tournament on
`N` vertices in which every `n`-set is dominated?" is a satisfiability question:
one Boolean per unordered pair of vertices, and one clause-group per `n`-subset
asserting that some outside vertex beats all of it.

The oracle for this problem is that encoding plus a direct checker `hasS_n(T)`
for an explicit tournament, and it must reproduce `f(1)=3` and `f(2)=7` on its
own — and ideally the 19-vertex `S_3` witness of Szekeres and Szekeres — before
anything it later reports is trusted.

Symmetry breaking is not optional. The automorphism group of the search space is
enormous and an unbroken lower-bound search will not terminate. State which
breaking is used and whether it preserves satisfiability; a lower bound from an
unstated or unsound breaking is a search outcome, not a theorem.

Never enumerate tournaments up to isomorphism past a handful of vertices, and
never check property `S_n` by enumerating colourings of anything — the check is
over `binom(N,n)` subsets and is direct.

Both known bounds are sixty years old: the upper from the plain first-moment
method, the lower from counting. Prefer the construction side, where the oracle
can verify a claim outright, and treat derandomisation — beating the Paley
threshold with an explicit family — as a legitimate deliverable in itself.

Use sat_solver for every existence question, coder for construction families and
the direct checker, symbolic_math for the first-moment and character-sum
computations, and pattern_finder on any small-`n` data the search produces.
