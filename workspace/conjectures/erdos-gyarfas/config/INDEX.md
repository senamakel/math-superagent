# Index — config

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `config.toml` | Run configuration: declares the workspace a mathematical-research run and solver settings (show derivation, verify with code, exact arithmetic, cite external claims, 600s tool cap, forbid exponential time/space), plus artifact paths (goal/tasks/memory/scratchpad/solution). The run's plumbing, not mathematics. |
| `start.log` | Runtime startup log capturing the run's launch output (config, environment, tool startup). Operators read it; the run's agents do not treat it as mathematics. Plumbing, kept out of the research and analysis paths. |
