# Shared context

What this run knows. This file is re-sent to nearly every role on every model
call, so it carries only what an agent would otherwise rebuild from disk, from
the note store, or from a session it was not present for. It is not a catalogue
of files and not a narration of what agents did.

**Token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 default). Excess is cut on
the way into a prompt with a notice. Link the file that still holds detail
compressed away rather than inflating this one. Durable findings belong in
Cognee, not here.

## The problem (from problem.md, sourced from projecteuler.net/minimal=700)

PE 700 "Eulercoin". Define the integer sequence

    a_n = 1504170715041707 · n  mod  4503599627370517   (n = 1, 2, 3, …)

An **Eulercoin** is a term strictly smaller than every previously found
Eulercoin (the running-minimum sequence, in order of occurrence). The first term
a₁ = 1504170715041707 is the first Eulercoin. Find the **sum of all Eulercoins**.

Worked examples (statement-given, arithmetic confirmed by hand):
- a₁ = 1504170715041707 (1st Eulercoin)
- a₂ = 3008341430083414 = 2·a₁ (not an Eulercoin; 3 008 341 430 083 414 < 4 503 599 627 370 517, so it equals 2a₁)
- a₃ = (3·a₁ − mod) = 8912517754604 (2nd Eulercoin: 4 512 512 145 125 121 − 4 503 599 627 370 517)
- Sum of first 2 Eulercoins = 1504170715041707 + 8912517754604 = 1513083232796311 ✓
- Modulus M = 4503599627370517; multiplier A = 1504170715041707. Both are large (~4.5e15); M and A are coprime (statement implies A odd; rotational structure expected).

These confirmed values are the brute-force oracle for any method.

## State of the workspace: fresh run, nothing prior

As of this survey, the run has **no prior investigation** — nothing established,
tried, or failed. Concretely:

- `GOAL.md` and `TASKS.md` are unfilled placeholders.
- All ledgers empty: `tasks`, `goals`, `claims`, `threads`, `approaches`,
  `weakened`, `blueprint`, `entailment`, `frontier`, `requests`, `board`.
- `code/` empty (no `brute.py`, no `solution.py`); `code/lib/` has no modules;
  `code/out/` has no captured output or claim notes.
- `research/` has only empty scaffold folders (approaches/, backward/, threads/)
  with READMEs explaining file conventions; no sources/, summaries/, notes/,
  no downloaded theory.
- Cognee memory and scratch: no related notes (recalled on "Eulercoin",
  "Project Euler 700").

## Established

(none beyond the statement's own definitions, examples, and confirmed
arithmetic above — those are marked/statement-given and hand-checked, not yet
computed by a program)

## Ruled out

(none — nothing has been attempted)

## Numbers

(no computed terms yet beyond the statement's own a₁, a₂, a₃ and sum
1513083232796311, hand-checked above)

## Recalled

(no durable memory relates this problem; first run on it)

## Contradictions

(none yet)

## Gaps / clearly next

The obvious next unresolved thing: **restate the goal precisely in GOAL.md and
write+run `code/brute.py`** — a naive forward scan computing the running minimum
of a_n and its Eulercoin sum, reproducing the given a₁/a₂/a₃ and the sum
1513083232796311 before any method work. Governing theory to identify after that
oracle is in place: a_n is the orbit of multiplication by A on Z/MZ, an
arithmetic progression under rotation. The target is not iteration to n ~ M —
that would be the "cost grows with the bound" trap — so the structural fact to
find is a way to produce the running-minimum (Eulercoin) values without scanning
every n up to ~4.5e15 (a continued-fraction / lattice / inverse-modular
structure on the minima). Do NOT iterate to the bound; the intended solution is
structural.
