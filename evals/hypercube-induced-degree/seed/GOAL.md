# What ends this run, and what counts as a result

## The deliverable

A **proof, or a genuine partial result stated exactly**, on the gap between
`c log n` and `sqrt(n)`.

The gap has stood for thirty years and the problem is elementary to state, which
means it has been attacked by capable people with the obvious tools. The working
assumption is that you will not close it. Claiming it on an argument that has
not survived attack is the one outright failure available here.

Results that would count, in rough order of value:

- a **lower bound `f(n) = omega(log n)`** — any superlogarithmic lower bound at
  all, proved, is a thirty-year result and the primary target;
- a **matching lower bound `f(n) = Omega(sqrt(n))`**, which closes the problem;
- an **improved upper bound**: a construction with `D(S) = o(sqrt(n))`, which
  closes it from the other side and would be just as large;
- the **exact values of `f(n)`** for more `n` than were previously computed
  here, with the method and its limit stated — this is real and reachable, and
  it is what everything else gets falsified against;
- a **proved obstruction**: a theorem that some named class of arguments
  (averaging, edge-counting, isoperimetry, coordinate induction) *cannot* give
  more than `O(log n)`. Proving a technique is stuck is a genuine result and is
  more valuable here than another attempt that gets stuck without saying why;
- the **`Omega(log n)` argument re-derived with its constant made explicit**,
  rather than cited, and checked against the exact values;
- a **Lean 4 formalisation** of `f(n)`, the construction, and the induction step
  in the known lower bound, with `#print axioms` reported and every remaining
  `sorry` listed.

A result stated without the bound it was established under is not a result. A
bound verified for `n <= 5` is a fact about `n <= 5` unless it is proved.

## The oracle is an exact optimiser and a falsifier, not a search

There is no value to recompute — the answer is a proof. The oracle is:

1. **`f_exact(n)`** — the exact minimum over all `S` of size `2^{n-1} + 1` of
   the maximum internal degree. Exhaustive for `n <= 4`; as a decision problem
   (`is there S with |S| = 2^{n-1}+1 and D(S) <= d?`) it is a clean SAT or ILP
   instance and reaches further. Use `sat_solver`. **State exactly how far it
   got and by what method**, and give the runtime at the last `n` completed.

2. **`degree_profile(S)`** — given an explicit `S`, verify `|S|` and return the
   full degree distribution inside `S`, not only the maximum. The distribution
   is what shows whether an averaging argument could ever have worked.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed bound must be run against the exact values.** A claimed lower
> bound that exceeds a computed `f(n)` is **false** — record it refuted, not
> weakened. A claimed construction must be built and its `D(S)` measured
> directly, not inferred from the recursion it was defined by.

Note the asymmetry, because it decides where the danger is. The target is a
**lower** bound on a **minimum over all `S`** — a universally quantified
statement. So the dangerous failure is an argument that establishes the bound
for the sets it happened to consider and treats that as all sets. Every claim
must say precisely which `S` it covers.

The exact values will be small and will not distinguish `log n` from `sqrt(n)`.
Compute them anyway. They are the only mechanical check available, and the
failure mode they catch — a plausible argument bounding the wrong quantity — is
the one this problem actually produces.

## Compute policy — light, parallel, bounded

- **The search space is doubly exponential if approached naively**: subsets of
  `{0,1}^n` of size `2^{n-1}+1`. Never enumerate subsets. Pose it as a decision
  problem and hand it to a solver, or the run will spend itself on `n = 4`.
- **The container has an 8 GiB cap and an OOM kill writes nothing to the
  console.** Say what a run will cost before running it. An OOM is a finding
  about the method, not a reason to ask for more memory.
- **Parallelise over `(n, d)` pairs and over candidate constructions, not over
  a single solver call.** `code/lib/parallel.py` with `code/lib/PARALLEL.md` is
  in this workspace; the box has 28 CPUs and no container CPU quota.
- **Bound every run.** Launch as
  `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
  Output that only reaches the model is destroyed when the attempt ends.

`sat_solver` is the right role for `f_exact`, and `lean_prover` is unusually
well suited to the induction step in the known lower bound — the statement is
small, finite and elementary. Report `#print axioms` and every `sorry`; a Lean
file asserting the theorem with no artifact beside it is worth nothing.

## Ending

Stop and report when you have a partial result of the kind listed above, or when
you can state precisely what blocks **the route you actually pursued** and why.

Report: the exact values of `f(n)` obtained and the method's limit; the degree
distributions observed; which claims are proved versus verified numerically,
with the range named; every technique tried and the exact point at which it
stopped giving more than `log n`; and every remaining `sorry`.
