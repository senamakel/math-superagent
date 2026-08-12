# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

The problem is the **3×3 magic square of squares** (open conjecture). Full
statement, the parametrisation, the leads, and the obstruction are in
`problem.md`, which every role is required to read; `GOAL.md` fixes the
deliverable. This file distils the parts no agent should have to re-derive and
records what the run has *so far* established — which, at this writing, is
almost nothing beyond the parametrisation itself.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default).

## Established

**The reduction every attack starts from — derived, standard, checkable** (from
`problem.md`; recompute before building on anything downstream):

- Any 3×3 magic square is determined by centre `c` and two parameters `u, v`
  (grid in problem.md); centre `M/3`. The problem is to make all nine entries
  positive distinct perfect squares.
- The centre is itself a square: `c = e²`.
- The four lines through the centre — two diagonals, middle row, middle column
  — are four **three-term APs of squares** all sharing middle term `e²`, with
  common differences `u, v, u+v, u-v`. The dependence among these four
  differences is the actual obstruction, not the existence of APs of squares
  (which is fully understood). A square `e²` lying in *four* such APs with
  differences in that additive relation is what nobody can rule out or produce.

**Leads from `problem.md` — all UNVERIFIED, `asserted-by-source` until a primary
source is anchored.** Do not build on any until CLAIMS.md settles it:

- **Near-misses with seven square entries exist**; the famous one is the
  "Parker square" (fails as a magic square). Bremner and Sallows are the search
  names. This is the single most load-bearing lead: it is the witness set every
  impossibility lemma must survive (see Ruled out / oracle).
- **Eight-square** attainability is a distinct open sub-question from seven.
- **Elliptic-reformulation**: widely reported to reduce to rational points on an
  elliptic surface / K3; Bremner, *On squares of squares* (Acta Arithmetica) is
  the primary paper. The exact variety and what is actually proved are unknown
  until fetched — "it's an elliptic curve" is worthless here.
- **Congruent numbers / concordant forms**: three-term APs of squares with
  common difference `d` are the congruent-number setup; whether the four-diff
  condition maps onto a known concordant-forms problem should be settled early.
- **Computational bound** reported past `10²⁵`: whose search, what exactly was
  searched (centre? constant? entries?), and by what method — all unverified.
  A bound is a fact about a range, not evidence about the answer.

## Ruled out

Only the known dead ends recorded in `problem.md` (marked as known-obstruction,
to be re-verified, not yet witnessed by this run):

- **Congruences alone cannot prove non-existence** — the system is *locally
  solvable modulo every prime power*, so any argument that works purely
  modularly has a hidden error. Way to find the error: run it against the known
  near-misses.
- **Descent needs the exact reduction first** — do the geometry before any
  infinite-descent / Fermat-style step.
- **A search is not a proof and never becomes one**; extending a bound is only
  worth doing to falsify a structural claim, and must be stated as such.

**The witness-oracle rule (from GOAL.md, binding):** every impossibility lemma
must be checked against the known 7/8-square near-misses. A lemma that refutes a
known near-miss (`refutes(witness)==True`) is false, full stop, and must be
recorded as a fault in `research/CLAIMS.md`, not dropped. A claim of
impossibility with no witness-check beside it is `asserted`, whatever it reads
like.

## Numbers

Nothing computed yet this run. The checker (`is_magic_square_of_squares`) and
the `(c,u,v)` generator do not yet exist; `code/out/near_misses.json` must hold
the independently reproduced Parker-square-class near-misses before any
structural claim is trusted. Until then no numerical claim exists.

## Recalled

Durable memory (`recall_memory` / `relate_memory`) currently returns **nothing**
about this problem or earlier runs on it. There is no prior-run finding to carry
forward. Treat everything here as this run's own, to be established.

## Contradictions

- **Cycle brief's suggested method vs. the actual problem.** This cycle's brief
  says "solve by structural graph theory — minimal counterexample, girth,
  expansion…". That does **not** apply to the magic square of squares, an
  arithmetic-geometry problem with no graph structure and no meaningful
  "minimal counterexample" of the connectivity/girth kind. Treat the graph-theory
  language as stale boilerplate; the real method is arithmetic geometry
  (parametrisation, elliptic surfaces, exact reductions), per `GOAL.md`. Do not
  let a planner chase a phantom graph argument and burn the budget.
- `problem.md` frames this as non-existence; it also says several experts treat
  existence as open in both directions. Keep one thread on existence rather than
  committing the whole run to a proof that may be false.

## Gaps

(These double as research requests.)

- **Primary sources unanchored**: need Bremner (Acta Arithmetica), the Parker
  square's exact values and provenance, the actual exhaustive-search bound, and
  whether 8 squares is attained anywhere. Each needs a `claim` block with exact
  hypotheses and a `status` when it lands.
- **The exact elliptic/K3 reduction** (which variety, which points correspond
  to solutions, what is actually proved) is unknown and must be stated precisely
  before descent is attempted.
- Whether the four-AP condition reduces to a known concordant-forms / congruent
  numbers problem is open.
