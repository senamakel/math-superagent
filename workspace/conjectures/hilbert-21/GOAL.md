# Goal — first pass

Attack what is left of Hilbert's 21st problem (`problem.md`): the
characterisation of realisable **reducible** representations, and the minimal
size of a counterexample. Bolibrukh's counterexample and the irreducible case
are settled and are **not** the target; do not re-prove either.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- **Bolibrukh's counterexample, explicitly**: the matrices, the rank, the number
  of singular points, and the obstruction that proves non-realisability. This is
  the run's single most valuable import — everything downstream is tested
  against it.
- The exact statement of Bolibrukh–Kostov for irreducible representations, and
  of Plemelj's theorem with the hypothesis that makes it Fuchsian.
- **What is known in the reducible case**: every published sufficient condition
  and every published necessary one, with the gap between them stated exactly.
  That gap is the target.
- The known bounds on the minimal rank and minimal number of points for a
  counterexample — in particular whether rank 2 is settled.
- The status of the higher-genus problem.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states a monodromy representation as a tuple of
  matrices with product `1`, a Fuchsian system as a tuple of residues, and
  realisability, ending in `sorry`. Mathlib's ODE and monodromy support is thin;
  **what is and is not statable is a reportable finding nobody has written
  down.**
- Real theorems available here: the Fuchs relation as integer arithmetic,
  irreducibility of an explicit tuple, the product-is-identity condition, and
  the exponent bookkeeping of an explicit system. Carry each to the kernel.
- Cited theorems — Plemelj, Bolibrukh, Kostov — are `axiom`s in
  `namespace Cited` with `/-- src: ... -/`, earning `conditional`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library, verified against controls before anything
rests on it:

- **Monodromy computation**: numerical continuation of a Fuchsian system around
  each loop, returning matrices *with error bounds*, and an interval-arithmetic
  mode that certifies. The uncertified and certified results must be different
  return values, never the same one with a comment.
- **Representation analysis**, exact over a number field: product-is-identity,
  irreducibility, the invariant-subspace lattice, and the conjugacy invariants.
- **The Fuchs relation and exponent bookkeeping**, on integers, applied to every
  candidate automatically.
- **Guards, asserted on at entry, every run**: a hypergeometric system must
  reproduce its known monodromy to the stated tolerance; a system with known
  exponents must satisfy the Fuchs relation exactly; Bolibrukh's counterexample
  must be reproduced and its representation confirmed reducible. A library that
  cannot reproduce a hypergeometric monodromy may not be used on anything.
- Record where continuation stops being certifiable — the rank, the point
  count, the stiffness — and why.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- Realisability for a stated class of reducible representations (a fixed rank
  and a fixed number of points, all of them enumerated), settled exhaustively
  with each case decided by an obstruction or a construction.
- Whether every rank-2 representation is realisable — small, finite-feeling, and
  decisive either way.
- A counterexample smaller than Bolibrukh's, with the obstruction proved.
- A certified reproduction of Bolibrukh's counterexample as a verified artifact.

## Rules

- **Every statement says Fuchsian or regular singular.** No exceptions; this is
  the distinction the problem is made of.
- **One canonical oracle per question.** Everything that computes a monodromy or
  tests irreducibility calls `code/lib`; nothing does it inline.
- **Certificates decide, numerics search.** An uncertified monodromy match is a
  lead, however many digits it has.
- **A failed residue search is a measurement.** Non-realisability is reported
  only with the obstruction that proved it.
- Check irreducibility before treating anything as a candidate counterexample.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

The Riemann–Hilbert *correspondence* as a general equivalence of categories
(D-modules, perverse sheaves), irregular singularities and Stokes phenomena, and
integrable-systems applications — background only unless a source shows a target
statement follows.
