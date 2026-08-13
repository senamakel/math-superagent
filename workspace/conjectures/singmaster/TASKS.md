# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 7)

- [ ] **1. Promote genus_table.captured.txt to a standalone claim.** Two
      independent CAS routes (Singular normal.lib and Sage Curve.genus())
      agreeing on every entry for 2<=k1,k2<=12, extended to k1=24 for
      k2=3,4,5, is the definitive two-parameter Faltings threshold. Genus = 1
      exactly for {2,3} and {2,4}; genus >= 2 for every other distinct pair.
      This IS the GOAL.md deliverable and it should be its own claim, marked
      `proved-by-two-CAS`, not left in a capture. It **supersedes** the
      operator's three-diagonal salvage (`code/out/genus_closed_forms.md`), which
      is now corroboration only.
- [ ] **2. Register the k2=5 closed form as established.** `genus[{5},n] = 2n-2
      except 2n-4 when 5|n` — exact on all 19 points n=6..24, zero mismatches,
      operator-checked. The old CONTEXT.md entry "k2=5 row has no verified
      closed form yet" is stale.
- [ ] **3. Register the slope conjecture as established.** Mean first-difference
      over WHOLE periods is exactly (m-1)/2 for m=2,3,4,5, with period-m diff
      patterns: [0,1], [1,0,2], [1,2,0,3], [2,2,2,0,4]. Operator-checked, zero
      mismatches. **Trap for whoever writes this up:** a truncated window (not
      a whole number of periods) gives a mean BELOW (m-1)/2 and looks like a
      refutation — state periodicity first, mean second.
- [ ] **4. Run or delete the five uncaptured programs.** `test_slope_across_rows.py`,
      `test_slope_hypothesis.py`, `effectivegenus/rep_pairs.py`,
      `genus/verify_k2_5_row.py`, `pattern/print_family.py` — all have ZERO
      captures. A program never executed is not evidence. The operator says run
      them or delete them. `verify_k2_5_row.py` and the slope tests already
      have their conclusions confirmed by independent operator check, so they
      can be captured as verification; `rep_pairs.py` confirms the geometric
      type of (2,3) and (2,5). `print_family.py` prints the infinite family.
      Capture all five or tombstone the ones superseded by the operator's
      check.

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
      stated gap in `research/REQUESTS.md`.

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