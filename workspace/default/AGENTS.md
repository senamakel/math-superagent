# Workspace instructions

How to work *in this workspace*. How to work *on the mathematics* is the method
policy at the top of your prompt, and this file deliberately does not repeat it:
two wordings of one rule is two rules to reconcile, and it is the version you
read second that you follow.

## Where things go

- Put generated files under this workspace only.
- Externally sourced material lives in `research/`. The run's own derivations
  and programs do not.
- The objective and what would count as finishing it are in `GOAL.md`.
- A source's URL is saved beside the claim it supports, not only in the
  research folder: a claim whose source cannot be reached from it is a claim
  the next reader has to establish again.
- `derived/` is written by the runtime from the ledgers. Never edit a file in
  it — the next write re-derives it and your edit is gone without a warning.
- Never write credentials or environment values into a workspace file.
- `trace.jsonl` is the runtime's own event log and the tools refuse it. It is a
  verbatim replay of what you have already seen, so reading it would spend a
  large part of your context to learn nothing.

## Writing code here

`code/AGENTS.md` is the working agreement for that tree, and it differs by what
kind of problem this is — an open conjecture leads with the mathematics, a
Project Euler problem leads with the oracle. Read it before writing a file
there. What holds either way:

- **`code/lean/` carries the mathematics; every other program is evidence for
  it.** A program produces a reason to believe something; a statement the kernel
  accepted is the thing itself. Say which Lean file or claim id a program bears
  on, or the number it produced is one the next attempt has to compute again.
- A statement read from the literature is an `axiom` under `namespace Cited`
  with a docstring naming the source. It earns `conditional`, never
  `formalised`, and that verdict is read off the kernel rather than typed.
- `code/` is also a Python package tree, and `/workspace/code` is on
  `PYTHONPATH`, so every folder in it is importable by name from anywhere. Never
  write `sys.path.insert`: an import that fails means the file is in the wrong
  place, and moving it is the fix.
- Reusable helpers go in `code/lib/<subject>.py`, one subject per module,
  imported as `from lib.<subject> import <name>`. Everything else is grouped by
  the question it attacks, one folder per question.
- Describe a file with `describe_file` when you create it, and refresh the
  folder's index after adding, renaming or deleting one. An index that
  disagrees with its folder misleads every later reader, including you.
- `sympy`, `numpy`, `scipy`, `gmpy2` and `networkx` are already installed:
  `sympy` for exact symbolic algebra and number theory, `gmpy2` for
  large-integer arithmetic, `numpy` for arrays, `networkx` for graphs. Reach
  for pip only for something genuinely absent.
