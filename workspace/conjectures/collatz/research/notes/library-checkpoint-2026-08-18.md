# This cycle's deliverable

## Chosen line
I choose the committed dynamical-systems/Diophantine line: separate unbounded trajectories from nontrivial cycles, use the accelerated map for cycle equations, and treat density and computation only as evidence or reductions. This is appropriate because the library's sources identify parity-frequency control and near-relations between powers of 2 and 3 as the load-bearing obstruction.

## Library sufficiency checkpoint
The minimal library requirement is met in `research/ROOT.md`: it states the counterexample structure, the 2^71 finite verification report, and more than three restricted/reduced classes (arithmetic-progression sufficiency, separate divergence/cycle sufficiency, m-cycle exclusion, and Tao's density-one theorem). This phase is therefore complete; future downloads must answer an explicit request.

## Exact claims now available
- Tao Theorem 1.3: logarithmic-density-one almost boundedness for every diverging f; not universal convergence.
- Barina 2025: finite verification below 2^71 via accelerated/sieve/distributed computation; not a proof.
- Lagarias: the principal unresolved alternatives are an unbounded orbit and a nontrivial cycle.
- Hercher: no accelerated m-cycle with m<=91 and a large odd-member lower bound, as documented in the existing source summary.
- Monks: any fixed nonconstant arithmetic progression is sufficient, including separate divergence and cycle reductions.

## Attack and limitation
The main tempting error is to infer universal convergence from Tao's density result or from the verified interval. That inference is false because a logarithmic-density-zero exceptional orbit is not excluded and finite checking has a finite hypothesis. The present cycle route also cannot exclude arbitrary cycle lengths: known Diophantine bounds leave a large gap. The proper output is a sourced library and a precise partial landscape, not a proof.

## Search failures
Citation-graph requests to OpenAlex were rate-limited with HTTP 429, so no citation-graph result is used as evidence. Duplicate downloads were refused because the relevant sources already exist locally. Cognee indexing was unavailable; the durable local trace is `research/LOCAL_MEMORY.md` and this note.
