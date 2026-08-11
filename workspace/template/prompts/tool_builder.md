# Workspace tool-builder guidance

Inspect `AGENTS.md`, `config.toml`, `GOAL.md`, and `MEMORY.md` before
substantial work.

Before running anything at full size, state the method, the mathematical result
it rests on, and its time and space complexity. Reproduce every small case and
worked example from the statement first; a program that cannot match the given
example is not ready to run at scale.

Prefer exact integer or rational arithmetic. Save programs and their relevant
output, and update `MEMORY.md` before finishing.

Edit with `apply_patch` rather than rewriting a file. Re-emitting a whole
script to change a few lines spends the turn restating code that was already
correct. Reach for it above all when one change spans files — a function and
the row describing it — since the envelope applies completely or not at all.
Keep `write_tool_file` for a new file or a genuine full rewrite.

Build a library rather than a pile of scripts. `code/` is a Python package
tree and `/workspace/code` is on `PYTHONPATH`, so every folder in it is
importable by name from any working directory and any invocation: `from
lib.perms import lex_ranks`, `from chains.walk import orbit`. Never write
`sys.path.insert` — an import that fails means the file is in the wrong place.

Anything a second program would repeat — a verified recurrence, an
exact-arithmetic routine, a parser for the statement's format, a checker
against the brute-force oracle — belongs in `code/lib/<subject>.py`: one
subject per module, each function named for what it computes and carrying a
docstring. Write each so it can be called without reading its source: an
explicit signature, one job, no reliance on globals or on a file having been
written earlier in the run. Keep a module small enough to read whole; a second
subject is a second module. The third time you type a routine out, it belonged
in `lib/` the first time.

Every other program is grouped by the question it attacks: `code/<question>/`,
one folder per question, each with its own `INDEX.md`, and what those programs
produced under `code/out/`.

Call `describe_file` on every file you add, recording the signature, what it
returns, and what established that it is correct. Do it in the same step as the
code: a description that has drifted from its function is worse than none,
because the next agent calls it as described instead of reading it. Read
`code/INDEX.md` and `code/lib/INDEX.md` before writing anything — the run may
already have what you are about to write.

Do not write a program that searches the answer space or iterates to the bound
in the statement. Do not write or run an algorithm with exponential time or
space complexity.
