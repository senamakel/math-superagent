# Index — config

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `config.toml` | Run configuration: marks the workspace a mathematical-research run, sets solver preferences (exact arithmetic, cite external claims, forbid exponential time/space), and maps artifact filenames (goal/tasks/memory/scratchpad/solution). |
| `console.log` | Runtime event log of the run's orchestration: budget (250 model calls, 4000 tool calls, 120 min, 10 min tool), the per-role agent spawns (goals, tool_builder, pattern_finder, organizer, librarian) and their model calls and tool activity timestamps. Diagnostics for operators; not part of the mathematics. |
| `problem.url` | Records the source URL of the problem statement (https://projecteuler.net/minimal=763) so the run can trace problem.md back to its origin. |
