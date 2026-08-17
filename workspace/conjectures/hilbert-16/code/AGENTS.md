# Working in `code/` — an open conjecture

Two trees, and the order between them is the whole working agreement:

**`code/lean/` carries the mathematics. Everything else is evidence for it.**

A program produces a reason to believe something. A statement the kernel
accepted *is* the thing. On an open problem nobody will grade the run's numbers,
so a result that exists only as a Python output is a result the next attempt
cannot use and no reader can check.

```text
code/
├── lean/           the mathematics — statements, and what has been proved
│   └── Lib/        one file per subject, in Lean 4 against Mathlib
├── lib/            what other programs import — one subject per module
├── <question>/     the programs attacking one question, with its own INDEX.md
└── out/            what those programs produced
```

## The rule that decides where work goes

Before writing a program, ask what statement it is evidence *for*. If there is
no such statement, write it first — in `code/lean/Lib/`, ending in `:= by
sorry` if it cannot be proved yet. A `sorry` is not a failure; it is the
statement pinned down, and pinning it down is most of the work. A hypothesis you
cannot write as a binder is one nobody has pinned down, and finding that out
costs minutes rather than an attempt.

Then write the program, and say in its index row which Lean file or claim id it
bears on. A number whose statement nobody wrote down is a number the next
attempt has to compute again.

## Rules for `code/lean/`

Its own `AGENTS.md` has the detail. The three that decide the shape:

- **A statement from the literature is an `axiom` under `namespace Cited`**,
  with a docstring naming the paper. It earns `conditional`, never
  `formalised` — the kernel checked the step *from* that paper *to* your claim,
  and nothing about the paper.
- **Generated data may not conclude anything.** Certificate data goes in
  untrusted `def`s under a `Generated/` folder, the checker is hand-written
  outside it, and a `check = true ↔ Spec` theorem joins them, closed `by
  decide`. Never `native_decide`.
- **State the conjecture itself first**, in `code/lean/Lib/Statement.lean`. If
  it cannot be stated yet, that is a finding about the problem and belongs in
  `CONTEXT.md`.

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
  reproduces, the brute force it agrees with, the size it has been run to — and
  which Lean statement or claim id it bears on.
- The third time you type a routine out, it belonged in `lib/` the first time.
- Name a program for what it computes, not for when it was written.
  `count_chains.py` survives; `try3.py` is unreadable a day later.
- Say the complexity before running anything substantial, in time *and* space.
  Exponential in either is prohibited — find a polynomial formulation.
- The naive program is not scaffolding to be deleted. It is the oracle the fast
  method is checked against, so it stays, and its row says which cases it can
  still reach.
- Exact arithmetic unless the problem is genuinely about floating point. A float
  result reported as an answer is a guess with a decimal point.
- A search that found nothing is worth its search space and nothing else.
  Record what was swept, and which published exhaustive regime it lies outside,
  as `search-frame` on the claim it supports.
- Never delete a program carrying a result. If it has been superseded, say so in
  its index row and leave it.

`sympy`, `numpy`, `scipy`, `gmpy2` and `networkx` are installed. Reach for pip
only for something genuinely absent.

## The measure

A run whose `research/` is full of prose and whose `code/lean/` is empty has
read the literature and formalised nothing. Across eighteen earlier conjecture
workspaces the ratio of Python to Lean was 21:1 by line count, and half of them
held no Lean at all. That is the failure this file exists to prevent, and it is
why the tree above puts `lean/` first.
