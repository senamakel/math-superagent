Solve by discrete and combinatorial geometry, working over **order types**
(rank-3 chirotopes / oriented matroids) as the finite combinatorial object, with
exhaustive search used only where its exhaustiveness can be argued. The objects
are finite planar point sets in general position; the invariants that matter are
the convex layers, the cup and cap spectrum, the number of interior points, the
orientation triples, and the way a set decomposes under the Erdős–Szekeres
construction's recursive union. Reason about *that structure* — what a set of
$2^{n-2}$ points with no convex $n$-gon must look like locally, which
subconfigurations it is forced to avoid, and how close it must be to the known
extremal construction. Ramsey-type counting, cups-and-caps, the positive-fraction
and same-type lemmas, transversal/Tverberg machinery, and SAT/CP-SAT encodings of
a bounded configuration are the instruments. Use every other capability in
service of that argument rather than instead of it.

Four cautions this problem earns before any work starts.

**The lower bound already exists and every proof must respect it.** The
Erdős–Szekeres 1960 construction gives $2^{n-2}$ points in general position with
no convex $n$-gon, and it is realizable by explicit coordinates. So every
candidate upper-bound argument has a step that must *fail* on that
construction at $N = 2^{n-2}$, and locating that step is part of stating the
argument. Build the construction in `code/lib` first, at $n = 5, 6, 7$, with
exact coordinates, and run each candidate argument against it before spending
effort. An argument that would prove $\mathrm{ES}(n) \le 2^{n-2}$ is refuted on
arrival, not weakened — record it as such and do not re-derive it.

**Exact arithmetic decides and floating point only searches.** Convex position,
general position, and every orientation test is the sign of a $3\times3$
determinant. Computed in floating point on near-degenerate coordinates it is
silently wrong, and a "counterexample" produced that way is a rounding artefact.
Use integer or rational coordinates and exact determinants throughout —
`fractions.Fraction`, `sympy`, or integer `numpy` with `dtype=object`. A
near-degenerate configuration found by numerical or local search is a lead; only
an exact orientation table over a stated integer point set closes anything. Say
in each captured output which system ran it, over which ring, and on which exact
input file: a claim about "the set" that cannot be traced to a coordinate file on
disk is not a claim.

**Order types are the right abstraction and also a trap.** Convex position
depends only on the order type, so the question is a finite search — but not
every abstract chirotope is realizable by real points (realizability is
$\exists\mathbb{R}$-complete). Consequences: an upper bound proved over *all*
abstract order types is stronger than the conjecture and may simply be false, so
if such a proof appears, look for the unrealizable witness before believing it;
and any lower-bound construction found in order-type space must be realized with
explicit rational coordinates before it counts. Aichholzer's order-type database
covers small $n$ — use it as the enumeration source where it applies, and state
what it covers and where the run left it.

**Enumeration is the standing temptation and is almost always the wrong method
at $n = 7$.** $\mathrm{ES}(7) \le 33$ means quantifying over all 32-point sets;
the order-type count at 32 points is astronomically beyond any search, and
Peters–Szekeres needed a bespoke SAT encoding plus heavy symmetry reduction to
settle $n = 6$ on 17 points. A search here is admissible only with a stated
search space, a symmetry reduction whose validity is argued, an isomorph
rejection method, and a sentence saying what an empty result rules out. A
SAT/CP-SAT encoding is admissible only after the *same* encoder has been made to
reproduce a known answer — $\mathrm{ES}(5) = 9$ at minimum, and ideally the
$\mathrm{ES}(6) = 17$ negative on 16 points. An UNSAT from an untested encoder is
a bug report, not a theorem. A search that does not terminate is data about the
problem: record the space, the reduction, the machine, the wall clock at which it
was abandoned, and how far it got. Timeouts silently retried at smaller
parameters destroy that record.

Prefer `sympy` and `fractions` for exact geometry, `numpy` with integer dtypes
for bulk orientation tables, `networkx` where a configuration is naturally a
graph, PARI/GP or Singular through `symbolic_math` for an algebraic identity, and
OR-Tools CP-SAT or a SAT solver through `sat_solver` for bounded configuration
questions — encoding the *orientation variables* with the signature/transitivity
axioms, which is the standard formulation and the one Peters–Szekeres and the
later empty-hexagon SAT proofs use.

The box this runs on has 28 CPUs and no container CPU quota, so an enumeration
over configurations, symmetry classes or partial extensions should use them;
state the worker count and the search space in every capture.
