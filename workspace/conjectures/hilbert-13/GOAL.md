# Goal — first pass

Attack the algebraic form of Hilbert's 13th problem (`problem.md`) through
resolvent degree. The continuous form is closed by Kolmogorov–Arnold and is
**not** the target; do not spend the run on it.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- **A single fixed definition of resolvent degree**, quoted from its source,
  written into `research/ROOT.md`, and used unchanged for the rest of the run.
  Definitions differ between authors on what a tower may do; a run that drifts
  between two is producing statements about nothing.
- The exact table of published upper bounds `RD(n)` for `n ≤ 12`, each with its
  paper and whether the reduction has been verified by anyone since.
- **Confirm the absence of lower bounds.** Is `RD(n) ≥ 2` really unknown for
  every `n`? If any lower bound has been claimed, its status decides this run's
  target.
- The precise relation between essential dimension and resolvent degree — what
  is proved in each direction, and the exact reason `ed` does not bound `RD`
  below. Get this right first; every lower-bound attempt depends on it.
- Which enumerative problems have had their resolvent degree computed.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states resolvent degree itself — the tower, the
  base dimension bound, and `RD(7) ≤ 2` as the target proposition — ending in
  `sorry`. Expect this to be hard to type; **where it cannot be typed, say
  exactly what is missing.** Which parts of resolvent degree are statable over
  today's Mathlib is a reportable finding nobody has written down.
- Every Tschirnhaus reduction this run reproduces goes in as a polynomial
  identity with a `ring`-closed proof — a real theorem, not a statement.
- Cited bounds are `axiom`s in `namespace Cited` with `/-- src: ... -/`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library over `Q`, verified against controls before
anything rests on it:

- **Tschirnhaus machinery**: apply an explicit transformation to a general
  degree-`n` polynomial, compute the resulting coefficient ideal, and return
  the exact number of surviving essential parameters by elimination — with the
  ideal, not a count in a docstring.
- **Guards, asserted on at entry**: the quartic must reduce to zero parameters
  (solvable by radicals); the quintic must reduce to the one-parameter Bring
  form; Hilbert's degree-7 normalisation must come back with three. A library
  that cannot reproduce Bring may not be used on anything.
- **Galois group computation** for the covers involved, exactly, so an
  enumerative problem's resolvent degree question is well posed before it is
  attacked.
- Record where elimination stops being feasible — the degree, the variable
  count, the wall clock. That wall is a fact about the problem.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- A verified reproduction of the best published reduction for one `n` in
  `7 ≤ n ≤ 10`, followed by an honest attempt to remove one parameter.
- Resolvent degree of a named enumerative problem with a computable Galois
  group.
- A precise statement and proof of where an essential-dimension argument fails
  against a tower — the clearest thing that can be said about the missing
  lower-bound technology.

## Rules

- **One fixed definition of resolvent degree for the whole run.** Every claim
  cites it. A claim under a different definition is a different claim.
- **One canonical oracle.** Everything that counts parameters calls `code/lib`;
  nothing counts them inline or in prose.
- **Eliminate, do not estimate.** A parameter count not backed by an
  elimination ideal is a conjecture and is labelled one.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- Apply the three tests in `problem.md` to every candidate and record which
  step failed. The tower test is not optional.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

The continuous Kolmogorov–Arnold theory, neural-network superposition results
that cite it, and Hilbert's 12th problem. Essential dimension is in scope only
as it bears on the lower-bound question.
