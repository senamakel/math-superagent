Solve by extremal graph theory with a SAT oracle as the main line, not as
support. The asymptotics of `f(n)` are already known to within `1 + o(1)`, and
the open question is whether a specific integer sequence ever decreases — so no
estimate answers it and the exact sequence is the object of study.

The oracle for this problem is `exists(n, d)`: is there a `C_4`-free graph on `n`
vertices with minimum degree at least `d`? Encode as SAT — one Boolean per
vertex pair, a clause forbidding each potential 4-cycle, a cardinality
constraint per vertex — and derive `f(n) = 1 + max{d : exists(n,d)}`. State the
clause count and the symmetry breaking before running, and classify the breaking
as complete or partial: a lower bound from an unsound breaking is a search
outcome, not a theorem.

Every table entry is two separate claims — a witness graph (verified `C_4`-free
by an independent checker) and an unsatisfiability result — and each must be
labelled by which was actually established.

The search for a counterexample has a known address. `C_4`-free extremal graphs
are the Erdős–Rényi polarity graphs of `PG(2,q)`, which exist only at
`n = q^2+q+1` for prime powers `q` and have irregular degrees at their absolute
points. If `f` ever drops, it drops just past such an `n`. Construct those graphs
explicitly, verify them, and compute the windows around them first.

Use sat_solver for every existence question, coder for the polarity-graph
constructions and the independent checkers, symbolic_math for the finite
projective plane arithmetic, and pattern_finder on the sequence `f(n)` and on
`f(n) - sqrt(n)`.
