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

## Established

**Nothing yet — fresh scaffold.** First-cycle audit (this run): all ledgers
empty (tasks, attempts, reductions, thesis, goals, claims, threads, approaches,
weakened, blueprint, entailment, frontier, requests, board); `research/` holds
only scaffolding READMEs — no `sources/`, `summaries/`, `notes/`; `code/` has
no library modules, no Lean files, no output; Cognee durable memory and scratch
both empty for this problem. Every claim in `problem.md` — MTV theorem's exact
coverage, monotone/secant conjecture status, Vakil's criterion, proper-Galois-
group records, the 3 264-conics audit — is recalled, unverified status, and is
precisely what GOAL.md phase 1 must confirm or strike. Nothing to rule out yet,
no numbers, no contradictions, no gaps beyond the unverified status list above.

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

## Ruled out

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

_None yet — no attempt has been made._

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

_None yet — no computation has been run._

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

_None — Cognee holds nothing for this problem._

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

_None yet._

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.

- The exact statement and coverage of Mukhin–Tarasov–Varchenko's theorem
  (which varieties, which flags) — the run's target is what lies outside it.
- Exact statements, proved parts, and the size of the published experiments for
  the monotone and secant conjectures.
- Vakil's criterion for Galois groups, and every recorded proper-subgroup case.
- Which classical Schubert numbers have been re-derived rigorously.
