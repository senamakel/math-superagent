# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 3)

- [x] **1. Nail down MRSTT effectiveness — RESOLVED.** Confirmed directly from the
      full text (`research/sources/mrstt-fulltext.full.md`, Remark 1.7): "The implied
      quantitative bounds in the hypothesis 't is sufficiently large depending on ε'
      are effective; however, we have made no attempt whatsoever to optimize them ...
      will likely be too large to be of use in numerical verification". So the
      threshold IS a computable (astronomically large) function of ε — NOT
      non-constructive. The interior theorem therefore yields a numerical B in
      principle. Uniform-in-k: yes over the interior; no over the boundary. The
      boundary `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}` remains the whole open gap.
      (Updated in `research/approaches/mrstt-exact-statement.md` and
      `code/out/mrstt_leaves_witnesses_open.md`.)
- [x] **2. State the double failure of witnesses honestly.** Every witness has
      t ≤ 24310, so they fail MRSTT's "t sufficiently large" hypothesis. They also
      all lie below the interior cut (small m). **Both are now said** in
      `code/out/mrstt_leaves_witnesses_open.md`: the region comparison is a
      shape-of-the-region statement, not a proof that a large-t witness would also
      escape the interior. The PENDING item about effectiveness is resolved.
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