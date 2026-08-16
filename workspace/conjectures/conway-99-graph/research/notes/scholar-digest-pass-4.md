# Scholar pass 4 — the 5-vertex condition for partial quadrangles (BIK)

Downstream pass on an already heavily-digested library (passes 1-3 in
`scholar-digest-pass*.md`). One genuine miss found and recorded.

## What this pass found

The adopted approach `research/approaches/pq-2-6-2-classification.md` rests on
the t-vertex-condition hierarchy and had flagged as UNVERIFIED the step-(4)
doubt: does any source establish that PQ point graphs satisfy the 5-vertex
condition? The BIK full text
(`research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md`,
**lines 181-185**) already carries exactly that statement, which the existing
BIK summary had completely omitted:

> "Reichard [31] showed that the collinearity graphs of generalized quadrangles
> satisfy the 5-vertex condition, and that ... GQ(s,s²) satisfy the 7-vertex
> condition. **More generally the 5-vertex condition holds for partial
> quadrangles.**"

Also confirms the ladder (lines 34-36): 3-vertex iff strongly regular,
v-vertex iff rank 3, strictly increasing between srg and rank 3.

## What it means here

A srg(99,14,1,2) has λ=1, hence is diamond-free, hence is the collinearity
graph of PQ(2,6,2). Therefore, taking BIK's assertion, a hypothetical 99-graph
**must satisfy the 5-vertex condition** — it is a NECESSARY condition, and the
first hierarchy rung the non-rank-3 99-graph (claim `srg99-not-vertex-
transitive`) does not inherit for free. Both controls are rank-3 PQs and pass
trivially, so the GOAL.md admissibility step ("must break on 9 and 243") is
absent by construction — the 5-vertex condition cannot by itself separate 99
from its controls.

## Actions taken

- Rewrote `research/summaries/brouwer-ihringer-kantor-4vertex-condition.md`
  to add the t-vertex ladder and the PQ 5-vertex fact; added claim block
  `bik-5vertex-holds-for-pq` (status `asserted` — the PQ part is asserted in
  the survey with no proof named; the GQ part is cited to Reichard [31]).
- Updated `research/approaches/pq-2-6-2-classification.md` step (4): the Pech
  verification is now moot; the fact is in-library, and step (3)'s 5-vertex
  equations become a proof obligation rather than an ad-hoc constraint.
- Verified the STS block-graph section (3.4) matches what was already recalled
  (Higman's classification; AG(2,3) the only non-PG example at v=9); the run's
  geometry is a *partial* STS, so this theorem does not apply — no contradiction.
- Stored durable finding to Cognee (note id 18109052254668500131).

## Status of the 5-vertex condition for 99

- `asserted` (BIK survey), not proved here — the PQ 5-vertex claim has no
  named proof in the source, and the underlying Reichard paper is not in the
  library. **Recommend a second source** (Reichard, or the Pech/other
  "highly regular" literature) before the 5-vertex equations are treated as a
  hard necessary condition in a nonexistence argument. Until then it is a
  lead that constrains a 99-graph *if* BIK's assertion is correct.

## Still lacking (unchanged phase-4 surface)

- Whether the 5-vertex-condition equations at (99,14,1,2) are consistent
  (approach step (3)) — the actual computation, not yet done.
- n3=0 for (99,14,1,2) still only a conjecture (Reimbayev); would need a
  k=14-specific geometric constraint.
- Existence of (99,14,1,2) open; no 9/243-surviving nonexistence claim.
