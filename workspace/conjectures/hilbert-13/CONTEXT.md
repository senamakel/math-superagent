# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries established results with their basis, dead ends with
their reason, computed numbers, recalled memory, contradictions, and gaps. It
is not a catalogue of files and not a narration of what agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default).
The file is re-sent on every model call in every role that reads it; length
here is a bill the whole run pays many times over. Link the file that still
holds any detail compressed away. Durable findings belong in Cognee. A
statement nobody can trace to a source is worth less than no statement.

## Established

**Nothing.** This run starts from zero in every store:

- `search_claims` returns no match for any query; `derived/CLAIMS.md` holds 0
  entries — there is not a single claim id in the run.
- All ledgers hold 0 entries: `tasks`, `attempts`, `reductions`, `thesis`,
  `goals`, `threads`, `approaches`, `weakened`, `blueprint`, `entailment`,
  `frontier`, `requests`, `board`. `derived/FRONTIER.md`, `REQUESTS.md`,
  `THREADS.md`, `APPROACHES.md` have never rendered.
- `research/` has no `sources/`, `summaries/`, or `notes/` — no document has
  been downloaded. No `ROOT.md`.
- `code/` has no Lean files (`code/lean/Lib/` empty, `Statement.lean`
  unwritten), no library modules (`code/lib/` empty), no captured output
  (`code/out/` empty).
- Cognee durable memory and scratch are empty: `recall_memory`,
  `relate_memory`, `recall_scratch` all return no related notes.

Every mathematical statement in `problem.md` is asserted from memory and
explicitly flagged for correction. None of it is established.

## Ruled out

**Nothing has been tried.** No attempt, approach, thread, or reduction has been
proposed or closed. The three cautions in `METHOD.md` (Kolmogorov–Arnold is the
continuous problem, not this one; essential dimension does not bound RD below
because RD allows towers; a dimension count is not an elimination) are standing
warnings, not results — but they are binding: a claim that violates any of them
is refuted.

## Numbers

**None computed.** No oracle exists yet. The first numbers this run must
produce are the GOAL.md guards, by exact elimination over `Q`: quartic →
0 parameters (solvable by radicals), quintic → 1-parameter Bring form,
Hilbert degree-7 normalisation → 3.

## Recalled

Nothing. Durable memory holds no notes on resolvent degree, essential
dimension, Tschirnhaus transformations, or Hilbert's 13th problem.

## Contradictions

None — nothing has been read yet.

## Gaps

The first gate, from GOAL.md phase 1: **one fixed definition of resolvent
degree, quoted from a primary source, written into `research/ROOT.md`, and used
unchanged for the whole run** — every claim cites it, and a run drifting between
two definitions produces statements about nothing. The second gate, in the same
phase: the published upper-bound table `RD(n)` for `n ≤ 12`, each entry with its
paper and whether anyone has verified the reduction since. The exact items to
confirm or strike, each with a falsifier:

- `RD(n) = 1` for `n ≤ 5`; `RD(6) ≤ 2`; `RD(7) ≤ 3` (Hilbert); `RD(8) ≤ 4`,
  `RD(9) ≤ 4` (Hilbert / Wiman); `RD(n) ≤ n − 4` for `n ≥ 9` and improvements
  `n − 5`, `n − 6`, … with exact ranges.
- "No lower bound above 1 is known for any `n`" — if any `RD(n) ≥ 2` claim
  exists in the literature, its status decides the run's target.
- The exact proved relation between essential dimension and resolvent degree,
  and the precise reason `ed(S_n) ≥ ⌊n/2⌋` (Buhler–Reichstein) does not bound
  `RD` below.
- Whether Farb–Wolfson is the definition source to adopt, and which of its
  results (and Sutherland's, Heberle's) are verified.

`research/ROOT.md` is finished when it states the structure of a minimal
counterexample, the current verification bound, and at least three restricted
classes already settled with their hypotheses — that is GOAL.md's exit test for
phase 1, not an exhausted literature.
