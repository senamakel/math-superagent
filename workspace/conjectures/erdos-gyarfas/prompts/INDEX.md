# Index — prompts

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `goals.md` | Prompt guidance for the goals agent: translate the objective into observable completion criteria before delegating, spawn the tool-builder early (nothing is real until a program has run), reject candidate-enumerating plans, require a small-case check against the statement's worked example, and record blockers in MEMORY.md. The orchestrator-level role that sets completion criteria. |
| `inventor.md` | Prompt guidance for the inventor agent, called when the current approach stalls: propose a change of representation (generating function, bijection, transform, invariant, recursive decomposition, reformulation matching a known theorem), one specific proposal with its cost and first step, marked established-vs-speculation. Never propose enumerating the answer space. The structural-creativity role for the theory. |
| `lean_prover.md` | Prompt guidance for the lean_prover agent: formalise the conjecture's statement first against Mathlib's SimpleGraph/Walk/IsCycle/minDegree API (a workable shape given), check the conventions (empty vertex type, Walk.length counts edges, IsCycle's length bound), then formalise the small sharp structural lemmas; never attempt the conjecture itself. Keeps imports narrow. The formalisation role. |
| `librarian.md` | Prompt guidance for the librarian agent: since the run attacks an open conjecture, gather steadily and deliberately in phase 1 — primary statement, every partial result with exact hypotheses, the computational verification work (oracle + where a counterexample could still be), adjacent cycle-length machinery, and surveys. Return the arXiv abstract only when the paper itself is unreachable. Later reverts to fetch-on-gap. |
| `orchestrator.md` | Prompt guidance for the orchestrator agent: sequence understand->research->derive->implement->verify, do not implement before the governing theory is identified, split into mathematical/research/computational parts, spawn independent work in parallel and track run IDs, reject answer-space-searching plans, and combine results into one derivation. The run's coordinator role. |
| `organizer.md` | _(undescribed)_ |
| `pattern_finder.md` | Prompt guidance for the pattern-finder agent: work from computed result files, extract the integer sequences that matter, and run analyze_sequence / find_linear_recurrence exactly on them rather than eyeballing. Exact-over-a-sample is still not proof; a verified recurrence is a conjecture to hand on, and an invented pattern is worse than none. The sequence-analysis role. |
| `reflection.md` | _(undescribed)_ |
| `research.md` | Prompt guidance for the research agent: prefer original papers and official references, return exact URLs, search from several angles (named theorem, algorithm, classical theory, standard treatment), and return precise statements with hypotheses. Stores everything downloaded under research/ and never mixes gathered material with the run's own derivations. The external-facts role. |
| `sat_solver.md` | _(undescribed)_ |
| `scholar.md` | _(undescribed)_ |
| `tool_builder.md` | _(undescribed)_ |
