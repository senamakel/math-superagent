# Index — config

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `config.toml` | Run configuration: marks the workspace a mathematical-research run, sets solver preferences (exact arithmetic, cite external claims, forbid exponential time/space), and maps artifact filenames (goal/tasks/memory/scratchpad/solution). |
| `console.log` | Orchestrator's run event log: timestamps of spawned agents, model calls, and tool calls across the run. Operators read it; tools refuse it, so it is not a workspace artifact to act on. |
| `problem.url` | Records the source URL of the problem statement (https://projecteuler.net/minimal=763) so the run can trace problem.md back to its origin. |
