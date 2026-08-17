# Working in `code/` — a Project Euler problem

This problem has one number as its answer, and the run is not finished when a
program prints it. It is finished when something says *why* that number is
right.

```text
code/
├── lean/           the identity the answer rests on, and the answer stated
│   └── Lib/        one file per subject, in Lean 4 against Mathlib
├── lib/            what other programs import — one subject per module
├── <question>/     the programs attacking one question, with its own INDEX.md
└── out/            what those programs produced
```

Unlike an open conjecture, here the programs come first and that is correct: the
brute force is the oracle, the fast method is the result, and their agreement is
real evidence. What the Lean tree adds is the step nothing else can supply — the
recurrence, identity or bound the fast method *assumes*, written down and
checked, so the answer rests on an argument rather than on two programs that
happen to agree.

## The order that works here

1. **The brute force**, obviously correct and slow. It is the oracle, it is
   never deleted, and its index row says how far it can still reach.
2. **The fast method**, agreeing with the oracle on every case the oracle
   reaches. Disagreement is the most valuable thing a run finds; do not fix it
   by trusting the faster program.
3. **The identity in Lean.** The fast method is fast because of something —
   a recurrence, a bijection, a closed form. That something is a statement.
   Write it in `code/lean/Lib/`, ending in `:= by sorry` if it is not yet
   proved, and say which program bears on it.
4. **The answer as a statement.** `code/lean/Lib/Answer.lean` states the result
   the run is reporting. Beware the empty version of this: `theorem answer : N =
   N := by rfl` compiles, needs no axiom, and says nothing whatever — the
   runtime refuses that shape by name, and it refuses `P ↔ P` too.

## Rules for the programs

This is a Python package tree and `/workspace/code` is on `PYTHONPATH`, so every
folder is importable by name from any working directory:

```python
from lib.perms import lex_ranks      # code/lib/perms.py
from chains.walk import orbit        # code/chains/walk.py
```

Never write `sys.path.insert`. An import that fails means the file is in the
wrong place, and moving it is the fix.

- One job per file. A file that grew a second job is two files.
- Say in the index row **what established it is correct** — the examples it
  reproduces, the brute force it agrees with, the size it has been run to.
- The third time you type a routine out, it belonged in `lib/` the first time.
- Name a program for what it computes, not for when it was written.
  `count_chains.py` survives; `try3.py` is unreadable a day later.
- Say the complexity before running anything substantial, in time *and* space.
  Exponential in either is prohibited — find a polynomial formulation.
- Exact arithmetic unless the problem is genuinely about floating point. A float
  result reported as an answer is a guess with a decimal point.
- A result read from a catalogue — OEIS terms, a table — is good evidence that
  an answer is right and no evidence at all about why. File it as
  `status: catalogued`, and reproduce the terms with a program that does not
  read the catalogue before the run leans on it.
- Never delete a program carrying a result. If it has been superseded, say so in
  its index row and leave it.

`sympy`, `numpy`, `scipy`, `gmpy2` and `networkx` are installed. Reach for pip
only for something genuinely absent.

## Rules for `code/lean/`

Its own `AGENTS.md` has the detail. The two that matter most here:

- **A statement from the literature is an `axiom` under `namespace Cited`**, with
  a docstring naming the source. It earns `conditional`, never `formalised`.
- **Generated data may not conclude anything.** If the answer rests on a
  computed table, the table goes in untrusted `def`s under a `Generated/`
  folder, the checker is hand-written outside it, and a `check = true ↔ Spec`
  theorem joins them, closed `by decide` — never `native_decide`.
