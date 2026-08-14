# Shared context

Problem: consecutive perfect powers — all integer solutions of
`x^p - y^q = 1`, x,y>0, p,q>1. Believed to have exactly `(3,2,2,3)` = `3^2-2^3=1`.
Not proved. Objective (GOAL.md): a genuine partial result stated exactly; the one
outright failure is claiming the whole on an argument that has not survived attack.

## State of the run

FRESH. As of this brief: no source downloaded, no program written or run, no
claim block, no computed number, no dead end recorded. `research/` holds only
READMEs and empty `approaches/`, `backward/`, `threads/`; no `CLAIMS.md`,
`FRONTIER.md`, `REQUESTS.md` exist yet. `code/` and `code/lib/` empty. No
durable memory (`recall_memory`/`recall_scratch` return nothing).

## Established (verified in this run)

None yet. Nothing here is this run's verification; the items below are the
task-stated leads (problem.md), asserted not verified, each needing its own
proof/source and claim block before use.

## Ruled out

Nothing tried yet. The one recognised dead end (from problem.md, asserted not
verified): the effective bound from linear forms in logarithms is astronomically
too large to exhaust by computation — do not propose closing the gap by search.

## Numbers

None computed yet. The oracle target is defined in GOAL.md: `solutions(N)` must
return exactly `(3,2,2,3)` for every reachable N>=9, exact integer arithmetic
only. Report N and runtime when built.

## Recalled

None.

## Contradictions

None yet.

## Gaps / next moves

1. Build exact-integer oracle `solutions(N)` (must return exactly `(3,2,2,3)`)
   and `check_conditions(p,q)` calibrated so `(2,3)` satisfies it.
2. Prove the reduction to odd prime exponents; then redo the two exponent-2
   cases in full (factorisation in Z; in Z[i]) — the foundation everything else
   is measured against.
3. Reconstruct the exact divisibility conditions (shape `p^2 | y^{p-1}-1` and
   mirror) and record the exponent bound to which they are verified.
4. Then attack the open content: both exponents odd prime, in Z[zeta_p], where
   the obstruction is the class group. Every lemma must be evaluated at
   `3^2-2^3=1`; a lemma implying no solution at all is refuted, not weakened.
