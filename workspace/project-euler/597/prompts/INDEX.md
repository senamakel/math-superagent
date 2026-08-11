# Index — prompts

Role-specific guidance files, one per agent role, used by the run's agents when
spawned. Read the one matching the role before delegating work. The parent
workspace's `AGENTS.md` sets the cross-cutting method and evidence rules.

| File | Purpose |
| --- | --- |
| `goals.md` | Goal-setting guidance: turn the objective into observable completion criteria, delegate to research/tool-builder, and make the first spawned run produce a working program before writing notes. |
| `inventor.md` | Inventor role: when the current approach stalls, propose one concrete change of representation/theory (bijection, generating function, invariant) rather than a variation on the existing approach. |
| `librarian.md` | Librarian role: maintain the `research/` source library — descriptive filenames, `research/INDEX.md` current, documents indexed for `search_documents`. Never store a published contest answer. |
| `orchestrator.md` | Orchestrator role: sequence the work understand → research → derive → implement → verify; spawn agents in parallel, retain run IDs, and combine their outputs into one derivation. |
| `pattern_finder.md` | Pattern-recognition role: mine the run's computed integer sequences with exact `analyze_sequence` / `find_linear_recurrence` tools; report a verified recurrence as a conjecture, not a proof. |
| `reflection.md` | Reflection role: judge each attempt, not the problem; flag unverified answers as UNSOLVED and phantom progress as NO; give a lesson actionable by the next attempt. |
| `research.md` | Research role: prefer primary sources and return exact URLs; several search angles; return plain statements with hypotheses; never fetch a published contest answer. |
| `scholar.md` | Scholar role: read downloaded sources (summary then `.full.md`), write the one short summary per source, describe_file it, and flag where a source contradicts `memory.md`. |
| `tool_builder.md` | Tool-builder role: implement and run programs; reproduce worked examples before scale; prefer exact arithmetic; build one-function-per-file toolkit helpers in `toolkits/` and describe each. |
