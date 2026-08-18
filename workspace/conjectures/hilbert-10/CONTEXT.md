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

Nothing yet — this run starts from a bare scaffold. Surveyed this cycle:
`research/` holds only READMEs (no `sources/`, `summaries/`, `notes/`, no
thread files, no approach files); all 14 ledgers at 0 entries;
`derived/CLAIMS.md` re-derives "No claims recorded yet"; `code/lean/Lib/`,
`code/lib/`, `code/out/` contain no files; Cognee memory and scratch are both
empty. Every factual statement in `problem.md` is recalled, not sourced — see
the next section.

## Asserted but unverified

`problem.md` says of itself that it "is written from memory and expects
correction", and `GOAL.md` phase 1 is exactly the confirm-or-strike list below.
None of these has a primary source in this workspace:

- **Robinson (1949)** — first-order definition of `Z` in `Q`, with quantifier
  alternation; the exact shape and count are not stated in `problem.md`.
- **Poonen** — a `∀∃`-definition of `Z` in `Q`, "small number of quantifiers";
  `problem.md` gives **no paper and no year** (run's recollection: ~2009 —
  unconfirmed).
- **Koenigsmann (2016)** — universal definition of `Z` in `Q`; the "explicit
  quantifier count" is claimed but **not stated** in `problem.md`.
- **Rings of integers of number fields** — recalled as settled 2024–25 by
  Koymans–Pagano and Alpöge–Bhargava–Shnidman (rank-one elliptic curves);
  which statement exactly, and whether refereed, unconfirmed.
- **Mazur's conjecture** — exact statement and the precise implication to
  H10.def unverified.
- **Degree frontier** — quadratic case decidable via Hasse–Minkowski
  (uncited); cubic case asserted open.

Four research requests filed this cycle for exactly these; see
`research/REQUESTS.md`.

## Ruled out

Nothing. No approach has been tried, no earlier run exists in memory to learn
from, so no dead end is recorded. The first direction to close (per GOAL.md) is
the one that does not need the literature: `code/lean/Lib/Statement.lean`, the
conjecture as a type carrying every hypothesis, ending in `sorry`.

## Numbers

None. No oracle, no formula, no computed bound exists yet.

## Recalled

Cognee and scratch are empty for this problem (checked this cycle; queries
"Hilbert's tenth problem rationals", "Poonen Koenigsmann Hilbert symbol"). The
survey result is stored in memory so a later run need not re-survey.

## Contradictions

None recorded yet. Standing warning carried from `problem.md` (not established
here): an existential definition of `Z` in `Q` would refute Mazur's conjecture,
so any argument producing one is guilty until every step survives.

## Gaps

The GOAL.md phase-1 items, in order: (1) the quantifier-shape/count table of
every published definition of `Z` in `Q` from primary sources — this is the
run's target inventory; (2) the exact statement and refereed status of the
rings-of-integers resolutions; (3) Mazur's conjecture, exact form and
implication; (4) the degree-2/degree-3 decidability boundary. Once phase 2
starts: `code/lean/Lib/Statement.lean` and the `code/lib` oracle (Hilbert
symbols, local solvability, formula evaluator, quantifier counter).
