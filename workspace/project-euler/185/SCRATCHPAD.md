# Scratchpad

## pattern_finder

Notes on each run's findings, provisional and confirmed. Promote durable
results to Cognee via remember_memory (done for the falsifications and the
c=1 conjecture).

### New results from this run (pattern finder)

Workspace had real output on disk: L5 oracle 39542 and L16 MILP secret
4640261571849533 (code/out/solution2_run.log; all 22 counts + uniqueness).

Ran the three existing scripts again plus a new one (code/pat_minmult_c1.py):

- **Min-multiplicity conjecture FALSIFIED** (was never recorded before —
  code/pat_extract.py printed it but no one had stated the verdict): secret[p]
  is a least-frequent digit of its column at only 2/16 positions on L=16,
  and 2/5 on the L=5 oracle. Column-minimum is NOT a lead.
- Column-majority re-confirmed dead: 1/16 (L=16), already in memory.
- Four sequences never analyzed before — parity
  [0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1], adjacent abs-diff, adjacent sums, and the
  44-term flattened match-position list — each shows NO polynomial structure
  and NO constant-coefficient linear recurrence (order <= 8 checked for the
  44-term list). No exploitable sequence structure.
- **Survivor (weak, 2-instance conjecture):** the c=1 single-hit guesses match
  at PAIRWISE DISTINCT positions — L16 six c=1 guesses at positions
  {0,2,4,6,8,15} (distinct), L5 two at {0,2} (distinct). The stronger "all
  even" form is FALSIFIED on L16 by odd position 15. The distinctness is NOT
  forced by the problem definition (nothing forbids two c=1 guesses matching
  at the same position), so it is an empirical coincidence over exactly two
  instances — worth one line of memory, not a derivation lead.

### Earlier confirmed (kept for context)
- Secret digits / hitcounts / c-vector / column sequences: no polynomial, no
  CC recurrence of order <= 6/8, not in OEIS.
- Definition-forced identities (hold by construction, not conjecture):
  sum(hitcounts) == sum(c_i) == 44; every per-guess match count == c_i.
- Column-majority rule H1 dead (1/16); H2 pair-design near-uniform dead.
