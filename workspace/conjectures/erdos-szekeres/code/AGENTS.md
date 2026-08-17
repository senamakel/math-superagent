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

## The shape

This is a Python package tree, not a drawer of scripts. `/workspace/code` is on
`PYTHONPATH`, so every folder here is importable by name from any working
directory and any invocation:

```text
code/
├── lib/            what other programs import — one subject per module
├── <question>/     the programs attacking one question, with its own INDEX.md
└── out/            what those programs produced
```

```python
from lib.perms import lex_ranks      # code/lib/perms.py
from chains.walk import orbit        # code/chains/walk.py
```

Never write `sys.path.insert`. An import that fails means the file is in the
wrong place, and moving it is the fix.

A program starts at `code/` directly and moves into a folder as soon as a
second program attacks the same question. Name the folder for the mathematics —
`chains/`, `dyadic/` — never for when the files were written.

## Rules

- One job per file. A file that grew a second job is two files.
- The third time you type a routine out, it belonged in `lib/` the first time.
  Copies drift, and a check that passes against one says nothing about the
  others. Move the definition into the `lib/` module for its subject and import
  it everywhere it was copied.
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

## Capturing program output — the one idiom, used everywhere

`execute_command` runs `/bin/sh` (dash), **not** bash. `${PIPESTATUS[0]}`,
`[[ ]]` tests, and every other bash array or bashism fail with
`Bad substitution`, exit non-zero, and leave an **empty capture** — a shell
error recorded where a result was meant, which reads like a failed computation.
This defect is a habit, not a one-off; the directive has now had to fix it
repeatedly. Do not reinvent a command line. Use exactly this idiom for every
capture, with no pipe, no tee, no arrays (here `\0` is the shell's escaped
`$?`, so the captured EXIT line is the python exit status and the file carries
its own command+exit provenance):

```sh
cd /workspace && { echo "$ python code/out/X.py"; \
  timeout 550 python code/out/X.py; \
  echo "EXIT: \0"; } > code/out/X.captured.txt 2>&1
```

Then read the capture back and report the `EXIT:` value. The literal file
should contain the command echo, the program's stdout, and the `EXIT: 0` line —
no bashisms anywhere in the command.
