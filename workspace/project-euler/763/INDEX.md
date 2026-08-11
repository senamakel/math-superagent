# Index — workspace

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | The method policy for the whole run: restate and test small cases before full size, do not search the answer space, verify with a second route, treat every number as coming from a run program. Read first in any role. |
| `CONTEXT.md` | Shared context: what the run's reference library establishes, under a thousand tokens, writing down established results, contradictions, and gaps. Research team writes it; every role reads it. |
| `GOAL.md` | The objective for Project Euler 763 (amoeba division D(N)) with the worked examples D(2)=3, D(10)=44499, D(20)=9204559704, last nine of D(100)=780166455 as the test oracle, and observable completion criteria; target is the last nine digits of D(10000). |
| `MEMORY.md` | _(undescribed)_ |
| `README.md` | Orientation for the workspace: one mathematical problem per directory, reproducible work, start with AGENTS.md then prompts/, completion in GOAL.md, work tracked in TASKS.md/SCRATCHPAD.md/MEMORY.md. |
| `SCRATCHPAD.md` | Scratchpad for temporary calculations, partial derivations, and observations not yet established enough for MEMORY.md. Currently only a section skeleton. |
| `TASKS.md` | Checklist of concrete steps toward the current goal; currently holds one unfilled step ("record the first concrete step"). |
| `brute.py` | Capped BFS oracle for D(N): drives levels up to a max depth arg, stops when the frontier exceeds 600k states, prints the full D(N) sequence and the checks D(2)=3, D(10)=44499. A sibling of code/brute.py (the standard frozenset oracle); this live-at-the-root copy is flagged as misplaced — belongs under code/ with the other oracles, kept here only because no move tool is available. |
| `problem.md` | The Project Euler 763 problem statement (converted from HTML): amoeba division rule, definition of D(N), the four worked examples, and the target D(10000) last-nine-digits. |
