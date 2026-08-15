# What ends this run, and what counts as a result

## The deliverable

A **shift in one of the two bounds, with a machine-verified artifact**, or a
precisely stated account of what blocks the route actually pursued.

The bounds `4 <= chi(G) <= 7` have stood for decades, so the working assumption
is that you will not move them. Claiming a bound on an argument that has not
survived attack is the one outright failure available here — and in this problem
it is unusually easy to do by accident, because a floating-point pipeline
manufactures convincing false lower bounds. See the trap in `problem.md`.

Results that would count, in rough order of value:

- a **unit-distance graph that is not `4`-colourable**, given as an explicit
  vertex list in exact algebraic coordinates, with every edge verified exactly
  and non-`4`-colourability verified by a complete method;
- a **proof that every unit-distance graph is `4`-colourable**, which settles
  the problem in the other direction and would be at least as large a result;
- a **colouring of the plane with `6` colours**, given explicitly with the
  separation margin computed;
- a **proved lower bound on the size** of any `5`-chromatic unit-distance graph
  — that is, a theorem that all unit-distance graphs on at most `N` vertices are
  `4`-colourable, for the largest `N` you can actually establish. This is a real
  result and it is reachable;
- a **construction engine with proved properties**: exactly which pairs in a
  Minkowski sum `A + B` are at unit distance, and what the operation does to
  chromatic number, stated as a theorem rather than observed on examples;
- a **census**: the chromatic numbers actually attained by the unit-distance
  graphs the run can construct, with the maximum reached, the size at which the
  search became infeasible, and why.

A result stated without the bound it was established under is not a result. "No
`5`-chromatic graph found" is a fact about the search performed, and the search
must be described precisely enough that someone could repeat it.

## The oracle is an exact-arithmetic verifier and a complete colouring test

There is no numeric answer to recompute. The oracle is:

1. **`unit_graph(points)`** — takes exact algebraic coordinates and returns the
   graph, with every edge certified `|x - y|^2 = 1` **symbolically**. Not
   `abs(d - 1) < eps`. This function is the foundation of everything and it must
   be written before any construction is attempted.

2. **`chromatic_number(graph, k)`** — a **complete** `k`-colourability test. A
   SAT encoding with a solver, or exhaustive search with symmetry breaking. It
   must return a colouring when one exists, so that a claimed UNSAT can be
   contrasted with a real SAT answer on a graph known to be colourable.

3. **The calibration pair, which is the check that matters.** Both oracles must
   be run against the `7`-vertex graph in `problem.md` before either is trusted:
   the edge verifier must certify all `11` of its edges exactly, and the
   colouring test must report `4`-colourable and **not** `3`-colourable.
   Record the actual output. A pipeline that cannot reproduce `chi = 4` on that
   graph is broken, and every number it produces afterwards is worthless.

> **Every claimed `5`-chromatic graph must survive a re-verification written
> independently of the code that produced it.** The construction code and the
> verification code must not share the arithmetic. This is the specific
> discipline that catches the floating-point trap, and it is not optional.

## The trap specific to this problem

Stated again because it is the failure mode this problem actually has:

**A spurious edge can only raise the apparent chromatic number.** So every
numerical error, every tolerance, every rounding, pushes the answer in exactly
the direction the run wants it to go. There is no self-correcting pressure. A
run using floating-point coordinates will find `5`-chromatic graphs, will find
them quickly, and will be wrong every time.

Exact arithmetic from the first line. If the construction cannot be done
exactly, change the construction.

The second trap is subtler: **searching at random.** Unit-distance graphs on
randomly chosen points have almost no edges, so a random search will spend the
whole run confirming that sparse graphs are `4`-colourable. The graphs that
matter come from algebraic structure. If the search is not over constructions,
it is not a search.

## Compute policy — light, parallel, bounded

- **The colouring test is the expensive step and it is exponential in the worst
  case.** Bound it. A SAT solver on a few hundred vertices is fast; on a few
  thousand it may not be. Say what a run will cost before running it.
- **The container has an 8 GiB cap and an OOM kill writes nothing to the
  console.** An OOM is a finding about the method, not a reason to ask for more
  memory. Stream, do not materialise.
- **Parallelise over constructions, not over the solver.** Testing many
  candidate point sets is exactly the shape `code/lib/parallel.py` and
  `parallel_map` are for; the box has 28 CPUs and no container CPU quota. One
  hard SAT instance does not parallelise usefully, but a thousand candidate
  graphs do.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.

`sat_solver` is the natural role for the colouring test and `symbolic_math` for
the exact coordinates — use both early. The verification here is genuinely
mechanical, which is rare, so the run should be spending its thinking on
constructions and almost none of it on checking.

## Ending

Stop and report when you have an artifact of the kind listed above, or when you
can state precisely what blocks **the route you actually pursued** and why.

Report: the exact-arithmetic field the coordinates live in; the calibration
output on the `7`-vertex graph; the constructions attempted and the chromatic
number each reached; the largest graph the colouring test completed on and the
time it took; and, for every claim, whether it is proved or verified on
instances, with the instances named.
