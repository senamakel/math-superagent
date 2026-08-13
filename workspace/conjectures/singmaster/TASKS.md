# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 8)

- [ ] **1. Run the seven uncaptured programs in one batch.** The only one with a
      capture is `genus_table`. Run the rest, adjusting paths for the three that
      sit in subdirectories:
      ```sh
      for p in genus/verify_superelliptic_formula pattern/fam_seqs genus/test_slope_across_rows genus/test_slope_hypothesis effectivegenus/rep_pairs genus/verify_k2_5_row pattern/print_family; do
        timeout 300 python3 code/$p.py 2>&1 | tee code/out/$(basename $p .py).captured.txt
        echo EXIT_CODE=$? >> code/out/$(basename $p .py).captured.txt
      done
      ```
      Anything that fails, delete or fix — a program neither run nor removed is
      dead weight that inflates code files against captured output.

- [ ] **2. Promote genus_table.captured.txt to a standalone claim.** Two
      independent CAS routes (Singular normal.lib and Sage Curve.genus())
      agreeing on every entry for 2<=k1,k2<=12, extended to k1=24 for
      k2=3,4,5, is the definitive two-parameter Faltings threshold. Genus = 1
      exactly for {2,3} and {2,4}; genus >= 2 for every other distinct pair.
      This IS the GOAL.md deliverable and it should be its own claim, marked
      `proved-by-two-CAS`, not left in a capture. Write the claim note in
      `code/out/` beside the capture and anchor the table. The operator's
      three-diagonal salvage (`code/out/genus_closed_forms.md`) is now
      corroboration only.

- [ ] **3. Register the k2=5 closed form as established.** `genus[{5},n] = 2n-2
      except 2n-4 when 5|n` — exact on all 19 points n=6..24, zero mismatches,
      operator-confirmed. The old CONTEXT.md entry "k2=5 row has no verified
      closed form yet" has been updated (this directive). Write the claim.

- [ ] **4. Register the slope conjecture as established.** Mean first-difference
      over WHOLE periods is exactly (m-1)/2 for m=2,3,4,5, with period-m diff
      patterns: [0,1], [1,0,2], [1,2,0,3], [2,2,2,0,4]. Operator-confirmed,
      zero mismatches. **Trap for whoever writes this up:** a truncated window
      (not a whole number of periods) gives a mean BELOW (m-1)/2 and looks like
      a refutation — state periodicity first, mean second.

- [ ] **5. Assertion backlog: 33 asserted, 6 checked, 2 proved, 1 unchecked.** Convert or
      drop; do not add. Every asserted claim that cannot be checked or sourced
      should be demoted. Thirty-three assertions is a backlog, not a library.

- [ ] **6. Delete or tombstone any of the seven programs that fail to run.**
      A program in the tree that has never produced a capture is not an asset.

## Done (directive 3)

- [x] MRSTT effectiveness — confirmed effective from full text (Remark 1.7),
      with an astronomically large but computable threshold. Uniform-in-k: yes
      over interior; no over boundary. Boundary remains the whole open gap.
- [x] Witness double-failure stated honestly in `mrstt_leaves_witnesses_open.md`.
- [x] Dead source files tombstoned (singmaster-1971, mrstt-interior-singmaster).
- [x] MRSTT PENDING contradiction resolved — credit to the run.

## Search policy (directive 4)

- [x] **Stop searching.** Literature search covered exa_search 66–76 and frontier
      170–220. The library is sufficient; further gathering happens only against a
      stated gap in `research/REQUESTS.md`. Do not continue browsing the frontier
      (directive 8: exa_search 16–21 and frontier 351–404 with 360 unworked —
      stop).

## Completed deliverables (attempt 2)

- [x] Exact MRSTT statement → `research/approaches/mrstt-exact-statement.md`
- [x] Reproduce every worked example (`verify_mrstt_witnesses.py`, EXIT_CODE=0)
- [x] Run witnesses against MRSTT interior cut (`check_witnesses_vs_mrstt.py`)
- [x] Demote `singmaster-1971-original` / `best-unconditional-bound` claims
      anchored to the Fermat's Library page
- [x] MRSTT-interior-singmaster tombstone written
- [x] Singmaster-1971 tombstone written

## Ledger discipline
- 42 claims: 33 asserted, 6 checked, 2 proved, 1 unchecked. Any lemma implying B<8 is refuted by 3003;
  state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it.
  The 33 asserted is a backlog — directive 8: convert or drop, do not add.