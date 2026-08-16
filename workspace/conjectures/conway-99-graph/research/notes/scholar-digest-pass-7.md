# Scholar digest — pass 7: survey, close the last placeholder summaries, flag the spurious OEIS coincidence

Cognee recall is still down (404 on recall_memory; remember_memory writes land).
Prior passes (1–6, consolidation 4) had already digested the library thoroughly, so
this pass did **not** re-digest; it surveyed `research/` against the goal (exact
partial results on srg(99,14,1,2), never a whole claim), verified the state of the
ledger, and closed the remaining loose ends.

## What was actually incomplete and what this pass did

1. **`research/summaries/assmus-2ranks-sts-fulltext.md`** — was an un-processed
   "Digest only" placeholder. Completed: Assmus 1995 carrier theorem (rank_2 of an
   STS depends only on order+2-rank; deficient systems coexist with full-rank; the
   quadruple-system analogue is a repeated Reed–Muller dual). Bearing: rank_2 of the
   triangle-incidence matrix varies within the λ=1,μ=2 family — 5 (defect 4) on
   rook(3) vs 243 (full) on BvLS (`code/out/incidence_p_rank.captured.txt`) — so
   rank_2(N) is not parameter-determined and can separate 99. Claim `assmus-sts-2rank-grounded`
   kept canonical in `research/notes/assmus-sts-2rank-acquisition.md` (removed the
   duplicate block I first placed in the summary). Caveat recorded: Assmus is about
   COMPLETE STSs; the 99 triangle geometry is a partial STS, so the transfer is the
   run's own extension.

2. **`research/summaries/mohammadian-tayfehrezaie-diamond-free-srg.md`** — was an
   un-processed "Digest only" placeholder for the same paper already fully digested
   at `mohammadian-diamond-free-srg-ar5iv.md`. Resolved it to a pointer note:
   diamond-free ⟺ PQ, giving PQ(2,6,2) for (99,14,1,2); the paper's own main theorem
   does not apply to 99 (g=44≠k=14). Prevents a second re-fetch of the same paper.

3. **The six OEIS placeholder rows.** All flagged **does not help**:
   - A208970 (necklaces), A097008 (sigma∘phi cycles), A319859 (partition-gen
     product), A327265 (tau-identification) — each plainly unrelated to srg(99,14,1,2).
   - **A218293 / A219272 (standard Young tableaux, distinct parts)** — the one worth
     a dedicated note: their entries include the values **1,3,4,10,31**, which
     coincide with the `u ∈ {1,3,4,10,31}` in the run's divisor-63 family
     characterization (k = u²+u+2). This is a **numerical coincidence, not a
     mathematical connection** (the SYT sequences count tableaux; no theorem links
     them to srg feasibility). The family's own vertex counts (9,99,243,6273,494019)
     are not a catalogued OEIS sequence (`oeis-miss-family-vertex-counts.md`).

## Contradictions / flags
- **None** between sources, and none with recalled memory (recall unavailable, so
  verified against on-disk full texts and captures as in earlier passes).
- The two open REQUESTS rows (`exact-list-prime-051a`, `published-mechanism-ruling-5cf8`)
  remain genuinely open; nothing this pass read closed them.

## Durable findings stored (remember_memory)
Assmus carrier theorem + the rank_2(N) control split; the Mohammadian-Tayfeh-Rezaie
diamond-free⟺PQ grounding for PQ(2,6,2); and this pass's survey outcome including the
spurious SYT-coincidence flag.

## What the run still lacks (unchanged from GOAL/previous passes)
1. Existence of srg(99,14,1,2) — open (Brouwer `?`; no 9/243-surviving claim).
2. Proving n3≥1 at 99 (would settle via Makhnev); seed extends locally to every
   radius, obstruction if any is global.
3. The super-simple 2-(22,4,2) existence fact (coclique-lift line, `super-simple-22242-gap`).
4. Whether G is trivial.
5. Durable-memory recall down this session (writes land, reads 404).
