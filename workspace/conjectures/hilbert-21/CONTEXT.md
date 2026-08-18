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

**Nothing.** This is a fresh scaffold: the claims ledger, all other ledgers, and
Cognee are empty; `code/lean/Lib/` and `code/lib/` hold no files; there are no
captured outputs under `code/out/`. There is not one sourced, verified, or
computed statement in the workspace.

Everything substantive in `problem.md` — Plemelj 1908 (regular-singular proof,
Fuchsian only under an extra hypothesis), Bolibrukh 1989 (rank-3, 4-point
counterexample), Bolibrukh–Kostov (irreducible case is realisable), reducible
case unclassified, rank-2 status unknown — is **asserted-by-recall only**.
`GOAL.md` says it in one line: "problem.md is written from memory and expects
correction." No source has been fetched; no claim id exists. Nothing here may be
cited as known until it is confirmed against a primary source and filed.

## Ruled out

Nothing has been tried. All ledgers (`tasks`, `attempts`, `reductions`,
`thesis`, `goals`, `threads`, `approaches`, `weakened`, `blueprint`,
`entailment`, `frontier`, `requests`) hold 0 entries. There is no dead end to
avoid and no prior run's failure to beat.

## Numbers

None computed. No oracle exists; there is nothing to reproduce a bound against.

## Recalled

Cognee is empty — `recall_memory` and `recall_scratch` return nothing for the
problem's own vocabulary. No earlier run left durable findings.

## Contradictions

None recorded. The only tension is internal to `problem.md` and is its own
caveat: it is written from memory and expects correction, so its status block
cannot be trusted until sourced.

## Gaps

The entire phase-1 import (GOAL.md), all currently unfilled, each a research
request:

- Bolibrukh's counterexample **explicitly**: the matrices, rank 3, the 4
  singular points, and the bundle-splitting obstruction that proves
  non-realisability. This is the run's single most valuable import — everything
  downstream is tested against it.
- The exact statement of Bolibrukh–Kostov for irreducible representations, and
  of Plemelj's theorem with the hypothesis that makes it Fuchsian.
- Every published sufficient and necessary condition in the reducible case, and
  the gap between them stated exactly.
- The known bounds on minimal rank and minimal point count for a
  counterexample — in particular whether rank 2 is settled.
- The status of the higher-genus problem.

## Next

Two first steps run together, per GOAL.md phase 1–2 and `code/AGENTS.md`:

1. Write `code/lean/Lib/Statement.lean`: the conjecture H21.red as a type
   carrying every hypothesis, ending `:= by sorry`. If it cannot be stated yet,
   that is a reportable finding about Mathlib's ODE/monodromy support.
2. Fetch and digest primary sources on the status block above, filing each as a
   fenced `claim` block with its source; the first is Bolibrukh's
   counterexample.
