# Goal — first pass

Attack Hilbert's twelfth problem (`problem.md`) at its first open case: explicit
generation of abelian extensions of **real quadratic** fields. Kronecker–Weber
and complex multiplication settle `Q` and the imaginary quadratic case and are
**not** the target; do not re-prove either.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- **Exactly what Dasgupta–Kakde proved**: which conjecture, over which fields,
  and whether the resulting construction is `p`-adic only. The run's target
  depends entirely on this, and it is the item most likely to be misremembered
  or overstated in a summary.
- The precise statement of the rank-one abelian Stark conjecture over a totally
  real base, with its hypotheses, and what is proved versus conjectural.
- Which Stark units have actually been **computed and verified**, for which
  fields and conductors — the existing tables, their size, and the software
  used. This is the run's baseline; anything it adds must go past it.
- What is known and what is conjectural in the `p`-adic real-multiplication
  programme, and what its archimedean counterpart would have to be.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states the target: a real quadratic `K`, a
  modulus, its ray class field, and the assertion that a named special value
  generates it — ending in `sorry`. Mathlib's class field theory is thin;
  **what is and is not statable is a reportable finding nobody has written
  down**, and stating it precisely is a deliverable of this pass.
- Real theorems are available on the algebraic side: irreducibility of an
  explicit minimal polynomial, its degree and discriminant, and that a specific
  field has a specific Galois group. Carry each verified case to the kernel.
- Cited theorems — Kronecker–Weber, CM theory, Brumer–Stark, Dasgupta–Kakde —
  are `axiom`s in `namespace Cited` with `/-- src: ... -/`, earning
  `conditional`, never `formalised`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library, verified against controls before anything
rests on it:

- **Ray class groups and conductors** for a real quadratic `K` and a given
  modulus, exactly — computed *first* in every experiment, since everything is
  checked against its prediction.
- **Stark unit computation**: partial zeta values to a requested precision, the
  unit, then recognition of its minimal polynomial with the precision, the
  coefficient height and the margin all returned — never a bare polynomial.
- **Exact field verification**: given a candidate minimal polynomial, compute
  the degree, discriminant, ramification and Galois group of the field it
  defines and compare with the ray class group's prediction. The verdict is
  *verified*, *contradicted* or *inconclusive*, in the return type.
- **Guards, asserted on at entry, every run**: for an imaginary quadratic field
  the oracle must reproduce a known Hilbert class polynomial exactly; for `Q` it
  must produce cyclotomic polynomials; a published real quadratic Stark unit
  must be reproduced with its field verified. A library that cannot reproduce a
  known Hilbert class polynomial may not be used on an open case.
- Record where precision or class-group computation stops being feasible, at
  which discriminant and conductor, and why.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- An extended, fully verified table of Stark units for real quadratic fields
  past the published range, with each field verified exactly rather than
  recognised numerically.
- A test of a stated form of Stark's conjecture in a case not previously
  computed, run as an honest hunt for a failure.
- A precise specification of what a complex-analytic counterpart of the `p`-adic
  construction must satisfy, derived from the `p`-adic side.

## Rules

- **Every statement says `p`-adic or archimedean.** No exceptions.
- **One canonical oracle per question.** Everything that computes a ray class
  group, a Stark unit, or verifies a field calls `code/lib`; nothing does it
  inline.
- **Numerics search, exact algebra decides.** A recognised polynomial is a
  candidate; the field verification is what concludes. Report precision,
  coefficient height and margin with every recognition.
- Compute the ray class group before the analysis, every time.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

Kronecker–Weber and CM theory except as controls, non-abelian Langlands, and
Stark's conjectures in higher rank unless the run's chosen target needs them.
