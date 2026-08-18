# Goal — first pass

Attack the open half of Hilbert's 15th problem (`problem.md`): the limits of
validity of Schubert calculus — enumerative reality, Galois groups of Schubert
problems, and an audit of the classical numbers. The foundational question is
settled by intersection theory and is **not** the target.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- The exact statement of the Shapiro–Shapiro conjecture and of Mukhin–Tarasov–
  Varchenko's theorem — **including precisely which varieties it covers**, since
  the run's target is what lies outside it.
- The monotone and secant conjectures, stated exactly, with what is proved,
  what is experimentally supported, and the size of the existing experiments.
- What is known about Galois groups of Schubert problems: Vakil's criterion,
  which problems are known to have full symmetric group, and every recorded case
  of a proper subgroup.
- Which classical Schubert numbers have been re-derived rigorously and which
  have not.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states a Schubert problem — the Grassmannian,
  the flags, the incidence conditions — and the enumerative count, ending in
  `sorry`. Mathlib has Grassmannians only partially; **what is and is not
  statable is a reportable finding.**
- Littlewood–Richardson coefficients are finite combinatorics and can be
  *proved* in Lean for the cases this run uses. Do that: it makes the complex
  count a theorem rather than a table lookup.
- Cited theorems are `axiom`s in `namespace Cited` with `/-- src: ... -/`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library, verified against controls before anything
rests on it:

- **Schubert problem setup**: from a partition list, generate the polynomial
  system over `Q` in local coordinates, and independently compute the expected
  complex count from Littlewood–Richardson.
- **Solving**, with a typed result: exact (Gröbner / rational univariate
  representation) where feasible, numerical-with-certificates where not, and
  never an uncertified point count.
- **Certification** as a separate, mandatory step: alpha-theory or interval
  Newton for each solution, plus certified separation of distinct solutions.
- **Guards, asserted on at entry, every run**: the 2 lines meeting 4 general
  lines in `P³` must return 2; a problem with known Littlewood–Richardson
  number must match it exactly; a solve returning more solutions than the
  complex count must fail loudly rather than report. A library that misses the
  four-lines problem may not be used on anything.
- **Monodromy** for Galois groups: loops in flag space, tracked and certified,
  with the permutations they induce recorded exactly.
- Record where solving stops being feasible — the problem size, the path count,
  the wall clock.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- A certified real-solution-count table for a family the monotone or secant
  conjecture covers, run to a size beyond the published experiments, hunting the
  counterexample as hard as the confirmation.
- A Schubert problem with a proper Galois group, found by certified monodromy
  and then explained structurally.
- An exact solution over `Q` of a Schubert problem the literature solves only
  numerically.
- A verified audit of a set of classical numbers.

## Rules

- **One canonical oracle per question.** Everything that solves a Schubert
  problem or certifies a solution calls `code/lib`; nothing does it inline.
- **Every computation is checked against the complex count**, automatically, at
  entry. A mismatch is a failure, not a finding, until the mismatch itself is
  proved.
- **Certification is mandatory.** An uncertified numerical solution is a lead.
- Say whether every claim is about general or special flags, and over which
  field.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

The foundations of intersection theory itself, quantum cohomology and
Gromov–Witten theory unless a source shows a target statement follows, and
numerical solver engineering beyond what the oracle needs.
