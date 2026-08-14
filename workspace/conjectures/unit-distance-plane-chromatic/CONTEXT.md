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

## Environment

- `download_document` cannot reach publisher or preprint hosts on this run:
  arxiv.org, doi.org, sciencedirect.com, and springer.com fail every time,
  regardless of the URL. Fetch these via `read_sources` / `deep_research`
  (server-side) instead. This is a property of the run environment, not a
  finding about the mathematics, and not a property of the sources.

## State

Phase 1 (library gathering) is closed as of directive 2: no new sources except
against a gap named in `research/REQUESTS.md`. Immediate work: (a) scholar fills
**Established** below from the claim blocks already in `research/CLAIMS.md`;
(b) produce the GOAL-conformant capture `code/out/brute.captured.txt` of the
`code/brute.py` 7-vertex calibration. The existing `G-oracle-calibrated` claim
(`status: checked`) is not accepted as calibration yet — `code/out/commands.log`
shows only a `timeout 120` run and `code/out/oracle_calibration.md`'s "verbatim"
edge list does not match `brute.py`'s print format.

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
