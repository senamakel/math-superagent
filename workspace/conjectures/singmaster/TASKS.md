# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority deliverables (operator's steer, attempt 2)

- [x] **Exact MRSTT statement** written as its own claim with effective and
      uniform-in-k on separate lines →
      `research/approaches/mrstt-exact-statement.md`. (Verbose theorem 1.3,
      Remark 1.5 gap, loose end.) This is done and is the main deliverable.
- [x] Demote `singmaster-1971-original` / `best-unconditional-bound` claims that
      were anchored to the Fermat's-Library page; tombstone recorded in
      CONTEXT.md. The real 1971 paper (AMM 78) is NOT held — do not quote a
      constant or exponent from the truncated Fermat's comments.
- [x] Reproduce every worked example with an executed program
      (`code/verify_mrstt_witnesses.py`, EXIT_CODE=0): 3003 eight-fold,
      six N=6 witnesses, infinite Fibonacci family j=1..12, k<=log2(a) bound.
- [x] Run the faithful-bounds ledger against the witnesses
      (`code/check_witnesses_vs_mrstt.py`): all high-multiplicity witnesses are
      in the MRSTT-OPEN boundary, so the interior bound of 4 is not contradicted;
      no asserted lemma implying B<8 survives (record refuted not weakened).

## Ledger discipline
- asserted=15, checked=4, proved=0. Any lemma implying B<8 is refuted by 3003;
  state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it.
