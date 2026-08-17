# Pattern-finder round 31 — independent exact re-certification + one fresh cross-check

This is an independent sweep by the pattern-recognition specialist over the
already-computed sequence surface. It does not repeat rounds 19–30's closed-form
derivations; it re-verifies the catalogue with fresh tool runs and adds one new
exact cross-check that was not in the recorded catalogue.

## 1. Fresh exact cross-check: incidence-matrix identities (NEW)

For the triangle geometry (points × triangles incidence `N`), two identities
were re-verified here **exactly on both controls**, matching
`research/approaches/incidence-code-of-triangle-geometry.md`:

```
NN^T = (k/2)I + A ,      N^TN = 3I + C3
```

computed over exact integer numpy arrays (no floats) for rook(3) (v=9,k=4) and
bvls (v=243,k=22). Both hold (`True` on every check). Anchor:
`code/out/pf_rank_svd_identity.captured.txt`, program
`code/out/pf_rank_svd_identity.py`.

**Consequence (parameter-determined, NOT a separator):** at k=14 the graph
eigenvalues are {14,3,-4}, so `7I+A` has eigenvalues {21,10,3}, all nonzero.
Hence `NN^T = 7I+A` is invertible and **rank_Q(N) = 99** (full row rank) for
any putative srg(99,14,1,2). Exactly the same argument gives rank_Q(N)=243 at
BvLS (11I+A has {33,16,7}, all nonzero). So *rational* full-row rank of the
incidence matrix is parameter-determined and cannot distinguish 99 from 243.
This is consistent with, and distinct from, the *2-rank* result
(`incidence-2rank-not-parameter-determined-but-unprovable`): the 2-rank varies
(5 vs 243) while the rational rank is fixed at min(v,nT).

## 2. Sequence tools re-run, verdict unchanged

| sequence | analyze_sequence | find_linear_recurrence (≤4) | OEIS |
|---|---|---|---|
| triangles [6,231,891,117096,81842481] | not low-degree poly | none | (closed-form, no match, recorded) |
| coclique [3,22,45,561,15408] | not low-degree poly | none | (closed-form, no match, recorded) |
| distance-2 [4,84,220,6160,493024] | not low-degree poly | none | no match (recorded) |
| n3-seed survivor trace [1,2,5,11,19] | — | none ≤ 4 | OEIS matches are spurious coincidences |

The survivor trace `[1,2,5,11,19,19,19]` (radius-growth of the n3 seed: 2 at
radius 1, 5 at r2, 11 at r3, 19 at r4+, stable fixpoint) is a **mechanism
trace**, not an indexed sequence — the new `oeis_lookup([1,2,5,11,19])` hits
(A208970 necklaces, A327265, A097008, A319859) are combinatorial coincidence,
none is this process. Recorded as an OEIS miss (distinct).

## 3. Statement of standing (conjecture status)

Every sequence on disk is one of:
- a divisor-63-governed polynomial/rational-in-u, integer-valued at the five
  feasible index points — **parameter-determined**, holds for any member, so no
  separating power for 99; or
- a mechanism/enumeration trace with no definable extrapolation; or
- a small list of p-rank/SNF measurements at distinct parameter points.

No sequence separates srg(99,14,1,2) from its controls. This is a **fit over a
closed 5-point family**, so the closed forms are exhaustive *over the family*
(the next candidate a=129 ∤ 63 is infeasible); they are not proofs about any
single graph, and the 6th term is not computable. The genuinely 99-specific
structure remains the coclique bound 22 and the forced 1 ≤ n₃ ≤ 4158 — single
values, not sequence lines.

## Files
- `code/out/pf_rank_svd_identity.py`, `.captured.txt` — the new incidence check.
- This note.
