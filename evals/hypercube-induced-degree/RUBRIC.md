# Rubric — hypercube-induced-degree

Scored host-side by `scripts/eval-report`. Milestones are **ordered and
cumulative**. Every milestone requires an artifact in the workspace, not a
statement in a report.

This is the **invention** problem. The compute is trivial and the literature is
two standard facts, so a run that produces a lot of activity and no idea should
score low, and a run that produces one good idea and little else should score
high. The ladder is weighted accordingly.

## Milestone ladder

### M0 — knows the object exactly

- `f_exact(n)` implemented as a decision problem and run. Correct values are
  `f(1..5) = 1, 2, 2, 2, 3`.
- The method's limit stated with the runtime at the last `n` completed.
- Degree distributions, not only maxima, recorded for the optimal sets found.

Failing to reach M0 is a serious harness finding: this is a small SAT/ILP
encoding and the seed's `GOAL.md` names it explicitly.

### M1 — reproduced both known bounds

- The `sqrt(n)` construction rebuilt and its `D(S)` measured directly, not
  inferred from its recursion.
- The `Omega(log n)` argument re-derived with an explicit constant, checked
  against the M0 values.

### M2 — named the obstruction as its own finding

- An explicit account of *why* averaging, edge-counting, isoperimetry and
  coordinate induction stop at `log n`, established here rather than restated
  from the seed.
- Best form: a **proof** that one of those techniques cannot exceed `O(log n)`.
  That is a real result and scores as M3-equivalent.

Restating the seed's obstruction paragraph is not M2. M2 is establishing it.

### M3 — a genuinely new mechanism, correct or not

The run identifies a quantity that is a maximum by construction and applies it
to `S`. Scored on whether the mechanism is *sound and new to the run*, not on
whether it closes the gap. Sub-levels:

- **M3a** — proposes a spectral approach and establishes Cauchy interlacing and
  the cube's spectrum as proved inputs, then correctly identifies that `Q_n`'s
  own adjacency spectrum gives nothing.
- **M3b** — reaches the idea of a **different matrix on the same support**.
- **M3c** — constructs a signing with `A^2 = nI` and closes the argument.

**M3b is the hinge of this entire calibration exercise.** It is the step that no
amount of computation or literature reading produces. Record precisely which
role proposed it, at which attempt, and from what prompt or context — that is
the single most valuable datum any of the three runs will yield.

### M4 — the full result

`f(n) = ceil(sqrt(n))`, proved, with the construction and the lower bound
matching, and checked against M0.

## Alternative ladders that score equally

- **Improved upper bound.** A construction with `D(S) = o(sqrt(n))` would refute
  the expected answer and is M4-equivalent. The seed deliberately does not
  assert which side is wrong.
- **Extended exact values.** Pushing `f_exact` substantially past `n = 5` with a
  good encoding is M2-equivalent — it is genuinely hard and it is the only
  mechanical check the problem has.
- **A proved barrier.** A theorem that a named technique cannot exceed
  `O(log n)` is M3-equivalent.

## Negative markers

| marker | what it looks like |
|---|---|
| **unverified claim** | a bound asserted with no executed program and no complete proof |
| **wrong-quantity proof** | an argument bounding average or total degree presented as bounding the maximum — the characteristic failure of this problem |
| **universal-quantifier slip** | a bound established for the sets considered and treated as holding for all `S` |
| **refuted-but-kept** | a claimed bound exceeding a computed `f(n)`, weakened rather than recorded refuted |
| **subset enumeration** | time spent enumerating subsets of `{0,1}^n` instead of posing a decision problem |
| **searched for the answer** | screen-ledger hits, or a query aimed at retrieving a published result |
| **recall without derivation** | "sensitivity", "block sensitivity", `A_n^2 = nI`, the block recursion, or `sqrt(n)` asserted as the answer before any derivation produced it — see `GROUND_TRUTH.md` |

## The recall discriminator, stated precisely

This problem has a clean test that separates recall from derivation, and
`eval-report` must apply it:

- Computing `f(1..5) = 1,2,2,2,3` and **then** conjecturing `ceil(sqrt(n))` is
  **derivation**. It is exactly what the data supports and it scores well.
- Asserting `sqrt(n)` before computing anything, or naming the signed matrix
  before proposing a spectral approach, is **recall**. It scores as a negative
  marker regardless of correctness.

The ordering in `config/trace.jsonl` is what decides this, and the trace is
host-readable. Check the order, not the content.
