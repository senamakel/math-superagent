Solve by computational algebraic geometry with certification, with the
mathematics carried in Lean wherever it will go. Every question here reduces to
a **polynomial system**: a Schubert problem is a set of incidence conditions on
a Grassmannian or flag variety, written in Plücker or local coordinates, and its
solutions are the points of a zero-dimensional variety. So the objects are
concrete — an ideal over `Q`, its dimension, its degree, its real points, and
the monodromy of the family over the space of flags.

Reason about *that system*. The instruments: Plücker and local coordinate
charts, Gröbner bases and eigenvalue methods for exact solving, numerical
homotopy continuation for the large cases, certification by alpha-theory or
interval Newton, and monodromy loops in the parameter space for Galois groups.
Schubert's combinatorics — Littlewood–Richardson coefficients, Young tableaux,
the Pieri rules — supplies the expected complex count, which is the guard every
computation is checked against before its real content is read.

**Prefer the argument Lean can finish.** A zero-dimensional ideal's solution
count is a finite algebraic fact; a certified real root count via Sturm
sequences or a rational univariate representation is kernel-checkable; a
Littlewood–Richardson computation is a finite combinatorial theorem. State every
claim as a Lean type before spending an attempt on it, and where generated data
is involved keep it under `Generated/` with a hand-written checker and a
soundness theorem outside it.

Three cautions this problem earns before any work starts.

**A numerical count is not a count.** Homotopy continuation returns approximate
points; the number of them is the number of paths that converged, which is not
the number of solutions until each is certified and each pair is certified
distinct. Every count in this subject that has ever been wrong was wrong here.

**The complex count is the guard, always.** Compute the Littlewood–Richardson
number first and check every solve against it. A solver returning more solutions
than the complex count has a bug; returning fewer means paths were lost. Run
this check automatically, on every experiment, and assert on it.

**Genericity is a hypothesis, not a formality.** Schubert counts hold for
general flags. An experiment on special flags is measuring a degenerate problem,
which is a legitimate thing to measure and a different thing from the Schubert
number. Say which one every computation is about.
