# Index — config

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `config.toml` | Run configuration: marks the workspace a mathematical-research run, sets solver preferences (exact arithmetic, cite external claims, forbid exponential time/space), and maps artifact filenames (goal/tasks/memory/scratchpad/solution). |
| `console.log` | Runtime plumbing: console output log for the run captured to disk. Not part of the mathematics; kept for operation/debugging outside the run. |
| `problem.url` | Records the source URL of the problem statement (https://projecteuler.net/minimal=763) so the run can trace problem.md back to its origin. |
