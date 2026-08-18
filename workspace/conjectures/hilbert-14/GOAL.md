# Goal — first pass

Attack the dimension-4 case of Hilbert's 14th problem (`problem.md`): is the
kernel of every locally nilpotent derivation on a four-variable polynomial ring
finitely generated? Nagata's counterexample settles the original question and is
**not** the target; do not re-prove it.

## What this pass is for

### 1. Establish the frontier, from primary sources

Every item in `problem.md` is recalled from memory. Confirm or strike each with
its citation and exact hypothesis. Settle in particular:

- **The exact dimension frontier**: the smallest published `n` with a
  non-finitely-generated `ker D`, the paper, and whether that kernel is *proved*
  non-finitely-generated or only computed to be large. The whole run points at
  `n = 4` only if `n = 5` and `n = 3` are genuinely settled.
- What is proved for `n = 3`, and by which argument — a proof that generalises
  is the run's single most valuable import.
- Weitzenböck's exact hypothesis (linear? triangularisable?).
- The best variable count for Nagata-type counterexamples for other unipotent
  groups, kept separate from the `G_a` record.
- Whether any dimension-4 claim has been made anywhere — published, preprint,
  withdrawn. If one stands, this run's target becomes stress-testing it.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states H14.4: a locally nilpotent derivation
  on `MvPolynomial (Fin 4) k`, its kernel as a subalgebra, and
  `Algebra.FiniteType` on it, ending in `sorry`.
- Expect Mathlib gaps — local nilpotence, kernels as subalgebras, the plinth
  ideal. For each, either state the notion yourself under `code/lean/Lib/` or
  record precisely what is missing and what a statement would require.
- Cited results become `axiom`s in `namespace Cited` with `/-- src: ... -/`,
  earning `conditional`, never `formalised`.
- The finite parts — an ideal membership, a Gröbner certificate, a degree bound
  on a named derivation — go all the way to a kernel-checked theorem. Report
  `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library over `Q`, verified against controls before
anything rests on it:

- **Kernel computation** for a given derivation (van den Essen's algorithm or
  equivalent), returning generators up to a stated degree bound *and* whether
  the computation is complete or truncated. That distinction belongs in the
  return type, not in a comment.
- **Guards, asserted on at entry, every run**: `D = ∂/∂x` must return the
  polynomial ring in the remaining variables; a derivation with a slice must be
  detected and its kernel returned as a polynomial ring; the Daigle–Freudenburg
  dimension-5 derivation must reproduce the published generator degrees as far
  as the literature records them. A library that gets `n = 5` wrong may not be
  used on `n = 4`.
- **Slice and local-slice detection**, exactly — test 2 in `problem.md` runs on
  every candidate.
- Record where the Gröbner computation stops being feasible, at what degree and
  why. That wall is a fact about the problem worth writing down.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- Finite generation for a named dimension-4 subclass — check first whether it
  is already a theorem, and if so take the next class up.
- A degree bound on kernel generators for a stated slice-free subclass.
- A transport of the dimension-5 counterexample's structure down to four
  variables, run as an honest hunt for the obstruction that stops it — the
  obstruction, found and proved, is the better result.
- An explicit kernel computation for a named dimension-4 derivation the
  literature leaves open.

## Rules

- **One canonical oracle.** Everything that computes a kernel or tests for a
  slice calls `code/lib`; nothing does it inline.
- **A truncated computation is a measurement.** Never conclude non-finite
  generation from a computation that did not terminate; say what it reached.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- Apply the three tests in `problem.md` to every candidate and record which
  step failed. The dimension test is not optional.
- Keep characteristic zero and characteristic `p` strictly apart, and say which
  every claim is about.
- **`problem.md` is written from memory and expects correction.** When a source
  disagrees, print both and say which won.

## Out of scope

Nagata's original counterexample as such (background only), invariant theory of
reductive groups (finite generation there is a theorem), and Zariski's
dimension-2 problem beyond what informs dimension 4.
