# Working in `code/`

Every program the run writes lives here, and everything a program produces
lives in `code/out/`. The workspace root is for the run's prose — the goal, the
beliefs, the derivation — and a program written there is filed here
automatically. That is a rule in the runtime, not a request: a run that put its
thirty-first Python file at the root buried the two Markdown files that said
what it had actually worked out.

`INDEX.md` says what each program is for. Describe a file when you create it
with `describe_file`; a program nobody described is a program the next agent
re-writes rather than re-uses. The most useful thing a row can say is not what
the code does — that is readable — but **what established it is correct**: the
examples it reproduces, the brute force it agrees with, the size it has been
run to.

## Rules

- One job per file. A file that grew a second job is two files.
- Name a program for what it computes, not for when it was written.
  `count_chains.py` survives; `try3.py` is unreadable a day later.
- Say the complexity before running anything substantial, in time *and* space.
  Exponential in either is prohibited — find a polynomial formulation.
- The naive program is not scaffolding to be deleted. It is the oracle the
  fast method is checked against, so it stays, and its row says which cases it
  can still reach.
- Exact arithmetic unless the problem is genuinely about floating point. A
  float result reported as an answer is a guess with a decimal point.
- Never delete a program carrying a result. If it has been superseded, say so
  in its index row and leave it.
- A program that produced a number worth keeping should say in `code/out/`
  which file holds it, so the number is traceable to the run that made it.
