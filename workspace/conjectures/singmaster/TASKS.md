# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 3)

- [ ] **1. Nail down MRSTT effectiveness.** The run currently says "effective: yes"
      (Remark 1.7: constants too large for numerical use). The directive says this
      word is load-bearing. **Check mrstt-fulltext.full.md §1 (Remarks 1.5–1.7)
      and the proof sketch in §1.3 for whether "t sufficiently large depending on ε"
      is effective (computable function of ε exists in principle) or ineffective
      (the proof uses a non-constructive step).** Mark effective: yes/no AND
      uniform-in-k: yes/no explicitly. If ineffective, the theorem yields no
      numerical B even in the interior — state that.
- [ ] **2. State the double failure of witnesses honestly.** Every witness has
      t ≤ 24310, so they fail MRSTT's "t sufficiently large" hypothesis. They also
      all lie below the interior cut (small m). **Say both.** The region comparison
      in `code/out/mrstt_leaves_witnesses_open.md` must not be presented as proof
      that a large-t witness would also escape the interior — it is a shape-of-the-
      region statement, not a proof about the behavior of the function at large t.
      Update that file and `research/approaches/mrstt-exact-statement.md` accordingly.
- [x] **Tombstone the dead source files.** Done.
      `research/sources/singmaster-1971.full.md` → tombstone (was Fermat's Library
      comments, 8538B, zero original paper content).
      `research/sources/mrstt-interior-singmaster.full.md` → tombstone (was arXiv
      abstract page, 6954B, zero theorem/lemma/proof hits).

## Completed deliverables (attempt 2)

- [x] Exact MRSTT statement → `research/approaches/mrstt-exact-statement.md`
- [x] Reproduce every worked example (`verify_mrstt_witnesses.py`, EXIT_CODE=0)
- [x] Run witnesses against MRSTT interior cut (`check_witnesses_vs_mrstt.py`)
- [x] Demote `singmaster-1971-original` / `best-unconditional-bound` claims
      anchored to the Fermat's Library page
- [x] MRSTT-interior-singmaster tombstone written
- [x] Singmaster-1971 tombstone written

## Ledger discipline
- asserted=15, checked=4, proved=0. Any lemma implying B<8 is refuted by 3003;
  state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it.