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

**Problem definition (sourced: `problem.md`, downloaded from
projecteuler.net/minimal=156).** Natural numbers are written consecutively in
base 10. `f(n,d)` = total occurrences of digit `d` in all integers written from
0 through `n` inclusive. Solve `f(n,d) = n` for each digit `d ∈ {1,...,9}`; let
`s(d)` be the sum of all solution `n` (counting multiplicity across `d` per the
final note). Answer required: `Σ s(d)` for d=1..9.

**Worked examples — oracle (given in the statement, NOT yet reproduced by any
program this run).** `f(n,1)` for n=0..12: 0,1,1,1,1,1,1,1,1,1,2,4,5. The
value 3 never occurs. First solutions of `f(n,1)=n`: n=0, 1, then 199981.
Given `s(1) = 22786974071`. These are the fixed targets `brute.py` must
reproduce before any real method is trusted. **Status: the run has not yet
executed these — brute.py does not exist.** This is the immediate next step.

**Governing structure (conjectured, to be confirmed by the run's own
programs).** `f(n,d)` is the digit-count function over 0..n. It is computable
exactly in O(#digits) by a standard place-value decomposition (the classical
"count occurrences of digit d in 1..n" identity); no enumeration of numbers
needed. `f(n,d) ≈ n·(#digits)/10`, so `f(n,d) − n` grows superlinearly past a
small `n`; hence for each `d` only finitely many solutions exist and the
search can be pruned by bounding `n` rather than visiting the whole range.
The given bound's shape (solutions near 2·10^8 and far larger) means a
method that enumerates numbers up to the answer is the wrong method; the
intended one evaluates `f` per candidate/interval. See `solution.md` for the
derivation the run must write.

## Ruled out

Nothing yet — no approach has been attempted this run. (First candidate to
rule in or out: naive per-`n` counting up to the answer is exponential in the
sense of the bound and is prohibited; the O(digits) closed form for `f(n,d)`
is what replaces it.)

## Numbers

None computed yet this run. Targets from the statement: `f(11,1)=4`,
`f(12,1)=5`, first solutions 0, 1, 199981, `s(1)=22786974071`. The full sum
`Σ s(d)` is what the run must produce and independently verify.

## Recalled

Durable memory (Cognee) currently returns nothing for this problem or for
digit-counting problems of this shape; `relate_memory` likewise. Nothing
carried over to check.

## Contradictions

None yet — no computation to disagree with a source

## Gaps

- Reproduce the statement's examples with a naive oracle (`code/brute.py`):
  this is step 1 and unblocks everything.
- Establish the efficient `f(n,d)` evaluation and a bound on the solution set
  per `d` (`code/solution.py`, `solution.md`), then verify the final sum by a
  second independent route (e.g. a differently-structured counter-program
  agreeing with brute.py over the range brute.py can reach).
