# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

## State of the workspace — cold scaffold, verified this turn

No claims (ledger empty; `derived/CLAIMS.md` re-derived: "No claims recorded
yet"). `research/` holds only folder READMEs — no sources, summaries, or notes.
`code/lib/` and `code/lean/Lib/` are empty; `code/out/` has no captured output.
Cognee memory and scratch both return nothing. All 14 ledgers have 0 entries.
There is nothing to contradict and nothing ruled out: **no approach has been
tried, so no dead end exists**. Every result named in `problem.md` — Hilbert
1888 normalisation, Pfister `2^n` and its sharpness, the `n+2` lower bound, the
5-vs-8 gap for ternary forms, Reznick's `N`, LPR degree bounds — is
recalled-from-memory with no citation, and none may be treated as established
until sourced. The first work is GOAL.md's five settle-items, then
`code/lean/Lib/Statement.lean`, then the guarded oracle. The only open task is
the placeholder in `derived/TASKS.md`.

## Established

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

## Ruled out

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.
