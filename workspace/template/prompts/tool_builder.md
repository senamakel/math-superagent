# Workspace tool-builder guidance

Inspect `AGENTS.md`, `config.toml`, `goal.md`, and `memory.md` before
substantial work.

Before running anything at full size, state the method, the mathematical result
it rests on, and its time and space complexity. Reproduce every small case and
worked example from the statement first; a program that cannot match the given
example is not ready to run at scale.

Prefer exact integer or rational arithmetic. Save programs and their relevant
output, and update `memory.md` before finishing.

Edit with `apply_patch` rather than rewriting a file. Re-emitting a whole
script to change a few lines spends the turn restating code that was already
correct. Reach for it above all when one change spans files — a function and
the row describing it — since the envelope applies completely or not at all.
Keep `write_tool_file` for a new file or a genuine full rewrite.

Build a toolkit rather than a pile of scripts. Anything a second program would
repeat — a verified recurrence, an exact-arithmetic routine, a parser for the
statement's format, a checker against the brute-force oracle — belongs in
`toolkit.py` as a named function with a docstring, imported by the scripts that
need it (`from toolkit import ...`). Write each one so it can be called without
reading its source: an explicit signature, one job, no reliance on globals or
on a file having been written earlier in the run.

Record every function in `toolkit.md` with its signature, what it returns, and
what established that it is correct. Update that row in the same step as the
code; a description that has drifted from the function is worse than no
description, because the next agent will trust it instead of reading the
source. Check `toolkit.md` before writing a helper — the run may already have
one.

Do not write a program that searches the answer space or iterates to the bound
in the statement. Do not write or run an algorithm with exponential time or
space complexity.
