# Goal — first pass

Attack the open arithmetic under Hilbert's 11th problem (`problem.md`):
universal quadratic forms over rings of integers, the `u`-invariant of `Q(t)`,
and effective local–global bounds. Hasse–Minkowski over fields is settled and is
**not** the target; do not re-prove it.

Choose **one** of T1, T2, T3 in `problem.md` as this run's target by the end of
phase 1, on the evidence, and say which and why. T1 (universal forms over real
quadratic fields) is the most computational and the most likely to yield.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- The 15 and 290 theorems: **exact statements**, including the
  integer-matrix / integer-coefficient distinction and both critical sets. This
  distinction is load-bearing and is the most likely thing to be misremembered.
- What is known about minimal universal ranks over `Q(√D)`: which `D` are
  settled, by whom, and the best general lower bound and its dependence on the
  continued fraction of `√D`.
- The exact statement of `u(Q_p(t)) = 8` and its hypotheses, and everything
  known about `u(Q(t))` including whether finiteness is open.
- The best published effective bounds in Hasse–Minkowski.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states a quadratic lattice over `O_K`,
  representation, universality, and the target statement, ending in `sorry`.
  Mathlib carries quadratic forms and some number-field machinery; **report
  exactly where it stops**.
- Real Lean theorems are available here and should be produced: that a specific
  form represents a specific integer (an explicit witness, `decide`), the
  determinant and local invariants of an explicit lattice, and the leaf checks
  of a small escalation tree.
- Cited theorems — 15, 290, Parimala–Suresh, Kala's bounds — are `axiom`s in
  `namespace Cited` with `/-- src: ... -/`, earning `conditional`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library, verified against controls before anything
rests on it:

- **Representation testing**: given a form over `O_K` and a totally positive
  target, decide representation exactly, with a witness when it exists and a
  local or bounded-search obstruction when it does not — and the return type
  distinguishing *not represented* from *not found within the bound*.
- **Local invariants** at every place: Jordan splitting, Hasse invariant,
  Hilbert symbols, signature.
- **An escalation engine** for universality, reporting the complete tree, its
  size, and every leaf's verdict — or reporting that the tree was truncated,
  with where.
- **Guards, asserted on at entry, every run**: the sum of four squares must come
  back universal over `Z`; the sum of three squares must not, and the oracle
  must produce `7` as an exception; the 15-theorem critical set must be
  reproduced by the escalation engine over `Z`. An engine that cannot rederive
  the 15 theorem may not be pointed at a number field.
- Record where the escalation or the field arithmetic stops being feasible.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- The minimal universal rank over `Q(√D)` for one `D` where it is unknown, with
  the lower bound argued and not merely searched.
- A complete escalation tree over a small real quadratic field, producing a
  critical set.
- An anisotropic form over `Q(t)` of larger dimension than the published record.
- An exhaustive table of universal forms of small rank over `Q(√D)` for `D` in
  a stated range.

## Rules

- **One canonical oracle per question.** Everything that decides representation
  or computes a local invariant calls `code/lib`; nothing does it inline.
- **A search bound is not a proof.** "No exception found below `N`" is reported
  as exactly that, with `N`.
- Every claim states: definite or indefinite; integer-matrix or
  integer-coefficient; over `O_K` or over a non-maximal order. The oracle
  enforces the conventions; prose does not.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

Hasse–Minkowski itself, the classification of quadratic forms over fields, and
quadratic forms in characteristic 2 unless a target statement depends on them.
