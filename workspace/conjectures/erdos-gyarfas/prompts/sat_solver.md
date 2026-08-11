The finite questions this run will hand you are almost all of one shape:

> Does there exist a simple graph on $n$ vertices with minimum degree at least
> 3, [extra structural hypotheses], and no cycle of length 4, 8, 16, or 32?

`UNSAT` on that is a theorem: no counterexample of that order and that shape
exists. It is worth more than any model you could return, so treat an
unsatisfiable encoding as the good outcome rather than a failed run.

Two things about this encoding in particular.

**Graph symmetry is brutal here and the break must be sound.** A graph on $n$
labelled vertices has up to $n!$ isomorphic copies, so an unbroken encoding
spends the entire budget re-discovering the same graph. Lex-leader constraints
on the adjacency matrix rows, or a canonical degree ordering, are the standard
break — state which group you are quotienting by and why the break preserves
satisfiability. An unsound break turns a real counterexample into a false
`UNSAT`, which on this problem would be the most expensive error the run could
make. If you cannot argue the break is sound, run without it and report the
smaller $n$ you reached.

**Cycle-length constraints are not local.** "No cycle of length 8" is not a
clause over adjacency variables; it is a statement about walks. Encode it
explicitly — over closed walks with a distinctness condition, or via a
path-index formulation with position variables — and say which, because the two
have different sizes and different failure modes. Check your encoding against a
brute-force cycle enumerator on every $n$ the enumerator can reach before you
trust it at a larger $n$. An encoding that quietly forbids closed *walks* of
length 8 rather than *cycles* is a different problem, and it will happily
return `UNSAT`.

Consider `nauty`-style canonical generation as the cross-check rather than the
method: if the run has an exhaustive generator for small orders, its answer and
your `UNSAT` must agree exactly, and disagreement is the finding.

Report the $n$ you reached, the wall clock, the solver status, and the
encoding's size in variables and clauses. A bound is only a result if someone
else could reproduce it.
