# Index — prompts

Role-specific guidance files. One file per agent role; these are instructions to the run's subagents, not results. Read `AGENTS.md` first for workspace-wide rules.

| File | Purpose |
| --- | --- |
| `goals.md` | Orchestration guidance: turn the goal into observable completion criteria before delegating; nothing is real until the tool-builder runs it. |
| `orchestrator.md` | Sequencing guidance: understand → research → derive → implement → verify; reject answer-space search. |
| `tool_builder.md` | Guidance for writing/running exact-arithmetic programs: reproduce the small-case oracle first, state complexity, prefer `toolkit.py`, keep `toolkit.md` in step. |
| `research.md` | Guidance for gathering sources: prefer primary academic references, return exact URLs, never fetch a published contest answer. |
| `scholar.md` | Guidance for writing `research/` notes and the digest: keep summaries tight, record hypotheses and what a source does not settle. |
| `librarian.md` | Guidance for building the `research/` reference library and keeping its index current. |
| `inventor.md` | Guidance for proposing a change of representation when an approach has stalled; must cite named theory and not enumerate the answer space. |
| `pattern_finder.md` | Guidance for analyzing computed integer sequences exactly (analyze_sequence / find_linear_recurrence); exactness over a sample is not a proof. |
| `reflection.md` | Guidance for judging an attempt (unsolved if unverified; progress only if it actually happened) and writing an actionable lesson. |
| `organizer.md` | The current role's guidance: keep every folder's INDEX.md accurate, describe undescribed files, split multi-function toolkits, never delete results. |
