# Goal

Attack the **3×3 magic square of squares**: nine distinct positive integers
whose squares form a magic square. Primary direction is a **proof of
non-existence**; the statement, the parametrisation every attack starts from,
the obstruction, and the leads into the literature are in `problem.md`. Read it
before deciding anything.

## The oracle here is a generator and a falsifier, not a function

This is the part that differs from every Project Euler run in this repository,
and getting it wrong wastes the whole budget.

On a Euler problem `code/brute.py` is a *function*: it recomputes a value the
statement already gives, and agreeing with that value is what earns trust. Here
there is no value to recompute. The answer is a **proof**, and a proof cannot be
checked by comparing a number. So `code/brute.py` is a **search and a checker**:

1. **`is_magic_square_of_squares(grid)`** — a verifier. Given nine integers, it
   decides magic, all-square, distinct, positive. Trivial, exact, no floating
   point, and it is the ground truth every other program is measured against.
2. **A generator** — enumerate over the parametrisation $(c, u, v)$ in
   `problem.md`, count how many of the nine entries are perfect squares, and
   emit the best grids found. Run it far enough to produce **7-square
   near-misses independently**.

`code/out/` must hold that generator's output before any structural claim is
believed.

### The falsification oracle, which is the one that matters

A proof of non-existence is a claim that a certain set is empty. The failure
mode is an argument that proves too much — a modular sieve or a descent step
that also forbids configurations which **demonstrably exist**. Nothing in the
runtime catches that automatically, so it is built in here:

> **Every claimed impossibility lemma must be run against the known
> near-misses.** If a lemma forbids a 7-square or 8-square grid that actually
> exists, the lemma is false. Full stop.

So `code/brute.py` also exposes a **witness set**: the known near-misses,
reproduced by the generator and confirmed against the literature, held in
`code/out/near_misses.json` with provenance for each. Every sieve, congruence
argument, or descent step gets a function `refutes(witness) -> bool` run over
that set, and the result is captured into `code/out/`. A lemma that survives is
worth pursuing; a lemma that kills a witness is a **fault**, and the run says so
in `research/CLAIMS.md` rather than dropping it silently.

Record the outcome of that check as a `claim` block with `status: checked`
beside the output. A claim of impossibility with no witness-check beside it is
`status: asserted` and must be labelled as such, however convincing it reads.

## The method this run is committed to

**Arithmetic geometry, checked by computation and formalised where it
stabilises.**

- **`symbolic_math`** does the parametrisation algebra: eliminate variables from
  the nine square conditions, reduce to a variety, and simplify to zero rather
  than by hand. A simplify-to-zero is a result; a plausible rearrangement is not.
- **`sat_solver` / `smt_solver`** take the *finite* questions the structure
  throws off — does a grid exist with these residues modulo this modulus, with
  entries in this range, with this many square entries? `UNSAT` with a stated
  encoding size and an unsat core is a theorem about that range. `unknown`,
  `ResourceOut` and `GaveUp` are not answers and must never be reported as one.
- **`lean_prover`** makes a lemma true rather than persuasive. Formalise the
  *statement* early — getting the distinctness and positivity conditions right
  is itself work — then each lemma as it stabilises. A Lean claim is only
  established with a `#print axioms` showing no `sorry`; a file asserting
  "kernel-checked" with no artifact beside it is worth nothing, and a previous
  run in this repository did exactly that.
- **`librarian` / `scholar` / `research`** come first and never stop. Most of
  what is written about this problem online is recreational restatement. Prefer
  Bremner in *Acta Arithmetica*, anything in a refereed journal, and the actual
  search papers over blog summaries. A source that only restates the puzzle goes
  in the notes as "does not help" with the reason, so nobody reads it twice.

## Completion criteria

This run does not end by resolving the conjecture. It ends by having, written
down and defended:

1. `research/ROOT.md` — what the literature actually establishes: every partial
   result with exact hypotheses and conclusion, every known failed approach with
   the reason it failed, and the real computational bound with its method and
   what it covered.
2. `code/out/near_misses.json` — the known near-misses, reproduced by this run's
   own generator, each with provenance, plus this run's best independently found
   grids and how many square entries they have.
3. `MEMORY.md` — the structural facts this run has **established** about the
   parametrised system, each with a falsifier: what observation would show it
   false. Seed text that never became a belief is a failed run.
4. `research/CLAIMS.md` — every lemma, with `holds-here`, `status`, and for any
   impossibility lemma, the witness-check result beside it.
5. A **stated partial result**: either an impossibility theorem under explicit
   extra hypotheses (say exactly which, and why they are not vacuous), or a
   precise reduction showing what the full problem is equivalent to, or a
   documented refutation of a line of attack with the reason it dies.

## What would count as failure

- Reporting non-existence "proved" without a Lean artifact or an unsat core.
- A congruence argument that was never run against the near-miss witness set.
- A library of downloaded recreational pages with `asserted` claims and nothing
  established.
- Extending a search bound and calling it progress.
