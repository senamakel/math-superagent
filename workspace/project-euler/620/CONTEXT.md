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

Problem (Project Euler 620, full statement at `problem.md`). A circle C of
circumference c contains a smaller off-centre circle S of circumference s, and
four "planet" circles of circumferences p, p, q, q (p<q) inscribed in C but
outside S, each tangent to both C and S; planets may overlap; the closest gap
between the S and C boundaries must be ≥1cm. As gears of pitch 1cm, c,s,p,q are
integers ≥5, and the whole set must mesh "perfectly" (constant angular-velocity
ratio, teeth align with grooves) with each other — only discrete positions make
this possible, so g(c,s,p,q) is finite. Sums run over s+p+q≤n with p<q, p≥5,
s≥5. g(s+p+q,s,p,q) counts arrangements for that combined circumference. Sourced
from `problem.md`; not yet derived.

The governing structure is unknown a priori (run at step 1). Classical lead:
Soddy/Descartes circle theorems give the geometry of a circle tangent to two
others; perfect gear meshing imposes that arcs between contact points along each
circle are integer multiples of the tooth pitch — the discrete constraint that
makes g finite. To be verified, not assumed.

## Ruled out

Nothing yet. Run has produced no code or derivation (GOAL.md, TASKS.md, code/
still templates).

## Numbers

Oracle for verification, sourced from `problem.md`:
- g(16,5,5,6) = 9
- G(16) = 9
- G(20) = 205
- Target: G(500).

Brute-force oracle (`code/brute.py`) not yet written; these are the values it
must reproduce before the real method is trusted. Bound in statement: n=500,
so summing s+p+q≤500 is the adversarial scale.

## Recalled

Durable memory (Cognee) for this problem is empty — recall returned nothing and
then began failing with HTTP 409 (three attempts, differing queries). Treat as
infrastructure failure, not a finding. No earlier-run results to import; any
result this run produces must stand on its own computation or a fetched source.

## Contradictions

None yet — one source (the statement) only.

## Gaps

- The identity that makes G(500) computable: how g depends on (c,s,p,q)
  combinatorially (tooth-count/modular constraints coming from meshing, likely
  a finiteness/recurrence), so the sum over s+p+q≤500 is not enumerated.
- No brute-force oracle exists yet.
- Durable memory unreachable (recall failing); if it recovers, re-query for
  Project Euler 620 / gear-meshing circle problems.
