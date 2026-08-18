# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on: is there
`f` in `Z[x]` with all `f(a)+f(b)` (`a < b >= 0`) distinct?

## What a result looks like, in descending order of value

1. **An explicit `f` in `Z[x]` with a proof** that `f(a)+f(b)=f(c)+f(d)` forces
   `(a,b)=(c,d)`. This closes the problem. For a monomial this means proving a
   case of Lander–Parkin–Selfridge, so expect the witness, if any, to be a
   perturbed monomial in the spirit of Ruzsa.
2. **An effective form of Ruzsa's theorem** — an explicit rational `c` and `n_0`,
   or a proof that no rational `c` works. This is the concrete open sub-question
   and it is within a run's reach.
3. **A new degree ruled out**, unconditionally: no quartic works, or no
   polynomial of degree `d` with a stated structural property works. Degree 4 is
   the natural next target after Dubickas–Novikas closed degree 3.
4. **A conditional witness with the hypothesis stated exactly** — e.g. `x^5`
   works given Lander–Parkin–Selfridge. Labelled conditional everywhere: in the
   claim block, in Lean (hypothesis binder or `Cited` axiom), and in
   `CONTEXT.md`. A conditional witness presented as a solution is the failure
   this file exists to prevent.
5. **The sweep's data**: which low-height polynomials of degree 4 and 5 survive a
   collision search to a stated `N`, and what structure the survivors share.

## What must exist before any claim is believed

- `code/lean/Lib/Statement.lean` typing the property "the image of `f` is a
  Sidon set" with the ordering hypothesis as a binder, ending in `sorry`.
- The exact-integer `collisions(f, N)` oracle, **calibrated** by rediscovering
  on its own: a collision family for every quadratic, a collision for `x^3`, a
  collision for `x^4`, and none for `x^5` up to the `N` reached. An uncalibrated
  oracle makes every later number worthless.
- Every reported witness carrying the `N` it survived and the arithmetic used.

## The falsification oracle

The conjecture asserts **existence**, so the dangerous failure is a false
witness — a polynomial declared Sidon after a search that was too short, or done
in floating point. Every claimed witness is re-run at the largest feasible `N`
in exact integer arithmetic before it is written into any file.

In the other direction, every claimed impossibility theorem for a degree is run
against the survivors of the sweep at that degree; a theorem contradicted by a
surviving polynomial is **refuted**, not weakened.

## Stop conditions

A witness with a proof, an effective Ruzsa parameter, a new degree ruled out, or
an exactly stated gap. Not: the search reaching a larger `N`, and not the
literature being exhausted.
