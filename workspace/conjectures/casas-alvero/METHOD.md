Solve by commutative algebra and elimination over a base that remembers its
characteristic. For each fixed degree `n` the conjecture is a statement about an
explicit affine scheme over `Z`: the coefficients `a_1,…,a_n` of `f` together
with shared roots `r_1,…,r_{n−1}`, cut out by `f(r_i) = f^{(i)}(r_i) = 0`.
Reason about *that scheme* — its irreducible components, its dimension, its
degeneration under scaling weights (`x` has weight 1, `a_j` weight `j`), what
its fibre over `Spec F_p` looks like, and which components survive reduction.
Resultants, Gröbner bases with a weighted order, Newton polygons of the
one-variable eliminant, and the mod-`p` reduction that proved the `p^k` case are
the instruments. Use every other capability in service of that argument rather
than instead of it.

Three cautions this problem earns before any work starts.

The conjecture is **false in characteristic `p`**, so every argument has a step
that must break there, and locating that step is part of stating the argument.
Run each candidate against the char-`p` witnesses through the oracle in
`code/lib` before spending effort on it. An argument that also proves the
char-`p` statement is refuted, not weakened, and is recorded as such.

A Gröbner computation that does not terminate is data about the problem, not a
failed run. Record the degree, the order, the machine, the wall clock at which
it was abandoned, and the intermediate degree reached. The boundary of
feasibility is one of the few honestly reportable results available in a first
pass, and it is lost if timeouts are silently retried at smaller `n`.

Exact arithmetic decides and floating point only searches. A numerically
near-common root of `f` and `f^{(i)}` is a lead; only an exact gcd, resultant
or ideal-membership certificate closes anything. Any near-miss found
numerically must be resolved exactly before it is cited.

Prefer Singular, PARI/GP and sympy through `symbolic_math` for the algebra, and
say in each captured output which system, which term order, and which base
field or ring the computation ran over — a Gröbner basis over `Q` and one over
`F_p` answer different questions here, and confusing them is the specific way
this problem produces a wrong theorem.

The box this runs on has 28 CPUs and no container CPU quota, so a search over
degrees, primes or component candidates should use them; state the worker count
and the search space in the capture.
