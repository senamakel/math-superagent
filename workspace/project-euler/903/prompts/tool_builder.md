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
`toolkits/<name>.py` as a single named function with a docstring. One function
per file, so reading the one you need costs almost nothing. Write each so it
can be called without reading its source: an explicit signature, one job, no
reliance on globals or on a file having been written earlier in the run.

Scripts import it with `from toolkits.<name> import <name>`; `/workspace` is
the working directory, so no path setup is needed.

Call `describe_file` on every function file you add, recording the signature,
what it returns, and what established that it is correct. Do it in the same
step as the code: a description that has drifted from its function is worse
than none, because the next agent calls it as described instead of reading it.
Read `toolkits/INDEX.md` before writing a helper — the run may already have
one.

Do not write a program that searches the answer space or iterates to the bound
in the statement. Do not write or run an algorithm with exponential time or
space complexity.
