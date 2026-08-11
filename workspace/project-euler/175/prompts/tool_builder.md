# Workspace tool-builder guidance

Inspect `AGENTS.md`, `config.toml`, `GOAL.md`, and `MEMORY.md` before
substantial work.

Before running anything at full size, state the method, the mathematical result
it rests on, and its time and space complexity. Reproduce every small case and
worked example from the statement first; a program that cannot match the given
example is not ready to run at scale.

Prefer exact integer or rational arithmetic. Save programs and their relevant
output, and update `MEMORY.md` before finishing.

Do not write a program that searches the answer space or iterates to the bound
in the statement. Do not write or run an algorithm with exponential time or
space complexity.
