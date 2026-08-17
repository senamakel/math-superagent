# Scholar digest — pass 8: survey and record the two checked gate closures

This pass re-surveyed the whole library against the goal (exact partial results
on srg(99,14,1,2), never a whole claim), the current tasks, and the durable
beliefs. The library is phase-1 complete and was thoroughly digested in passes
1-7 plus the consolidation/assimilation passes; **no new source was acquired**
(library CLOSED per ROOT.md) and none was warranted. This pass found nothing
genuinely undigested.

## What this pass added (the gap it closed)

The two open algorithmic gate tasks — `verify-twograph-gate` and
`incidence-prank-parameter-determinism` — were in fact **done** (their ledgers
show `done`, their captures exist), but neither checked computation carried a
formal claim block, so neither surfaced in the planning reads of CLAIMS.md even
though both are load-bearing closed directions. This pass added the claim blocks:

1. **`seidel-twograph-descendant-closed-checked`** (checked) — appended to
   research/approaches/seidel-twograph-descendant.md. The regular-two-graph
   descendant reformulation of 99 is closed by exact code arithmetic: k=14 !=
   2mu=4 and v=99 != 2(2k-lambda-mu)=50, so the reformulation is inert for 99
   (same failure as the 243 control; rook(3) alone descends from the Paley
   two-graph on 10). Also records the reconciliation: the loose "BvLS descends
   from a 244-point two-graph" claim concerns a NON-regular two-graph, so it
   does not contradict the gate.

2. **`incidence-2rank-not-parameter-determined-but-unprovable`** (checked) —
   appended to research/threads/incidence-code.md. The incidence 2-rank of the
   triangle matrix N is not parameter-determined (spectral rule violated on
   doily and GQ(2,4)), so it *could* separate 99 from 243 — but it is
   unprovable this way (a 99 value needs an actual 99 system, circular), and
   the only same-parameter test (Shrikhande vs rook(4)) gives no split. Line
   closed as unusable. Also records the premise correction: the full-rank 243
   is rank_2(N), not rank_2(A+I)=133.

Both are stored durably (remember_memory).

## Reconciliation vs recalled/durable beliefs

- **No contradictions** between any new content and the recalled/durable
  beliefs or on-disk claims. The only apparent tension — BvLS "descending from
  a 244-point two-graph" vs the selected k=2mu gate telling 243 it is *not* a
  regular-two-graph descendant — is resolved, not papered over: the 244-point
  object is a non-regular two-graph. Recorded in the twograph claim.
- The rendered `derived/TASKS.md` was stale (both gate tasks shown `open`); the
  ledgers record both `done`. That is a runtime re-derivation artifact, not a
  content gap.

## Sources that do not help (maintained from prior passes)

`brouwer-haemers-srg-chapter` (paywalled, nothing beyond the definition),
`makhnev-2013-local-subgraphs-srg-99` (paywalled, body absent),
`vanlint-brouwer-srg-partial-geometries-1984` (garbled OCR),
`zehavi-oliveira-not-conway-99` (solves a variant),
`bagchi-mu2-correct` (wrong download — a Lie-algebra paper, never cite for
graphs), `keramatipour-sat-conway99` (no reportable boundary), the duplicate
landing pages (index.full, cesarz-woldar-arxiv dup, makhnev-1988-lambda1), and
all OEIS rows (partition/necklace/SYT sequences; the 1,3,4,10,31 SYT coincidence
is numeric, not a connection).

## What the run still lacks (unchanged from GOAL and prior passes)

1. Existence of srg(99,14,1,2) — open (Brouwer `?`; no 9/243-surviving claim).
2. **Proving n3>=1 at 99** (would settle via Makhnev 1988 Thm 2); n3=0 branch
   kills via infeasible srg(33,12,1,6), but n3>=1 must still be forced by
   k=14-specific geometry (order-6 counting is n3-agnostic — checked).
3. Whether G(=Aut) is trivial — only surviving automorphism uncertainty; Z_7
   singled-fixed-point sub-case open (both the forced-structure preprint and
   this run's automorphism ledger agree CP-SAT does not decide it).
4. Shpectorov-Zhao (85,14,3,2) is an un-refereed preprint whose segment
   enumeration the run has not re-verified; transfer to lambda=1 untested.
