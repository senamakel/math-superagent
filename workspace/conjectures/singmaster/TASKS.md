# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 9)

- [ ] **1. Re-derive the genus closed-form substitutions.** The formula
      `g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2` was checked against 111 Singular
      entries by the operator, not by the run. Verify it yourself: re-derive the
      substitutions that reduce it to the m=2,3,4 per-family formulas and to
      (n-1)(n-2)/2 on adjacent pairs. Then spot-check three (m,n) pairs the grid
      has NOT yet computed — pick pairs beyond the existing range, compute them
      with Singular, and confirm the formula predicts them. The claim is in
      CLAIMS.md as `genus-single-closed-form-all-pairs` status `checked`; do not
      change its status to `proved`. It stays `checked` until a derivation
      produces it.

- [ ] **2. Derive the genus formula from Riemann-Hurwitz.** The formula is
      `g = ((m-1)n - (m-2) - gcd(n,m))/2`. The `gcd(n,m)` term has the shape of a
      ramification count for the projection `(x,y) -> x` on `C(x,m) = C(y,n)`,
      and the `(m-1)n - (m-2)` term is the plane-curve degree formula minus the
      diagonal factor. This is a bounded, finishable task: apply
      Riemann-Hurwitz to that map, compute the ramification divisor, and show
      `gcd(n,m)` emerges as the count of points where the fibre cardinality
      drops. When the derivation is written in `code/out/` and checked against
      the 111 Singular values with zero mismatches, the claim becomes `proved`.

- [x] **3. Fix the false two-CAS claim in genus_table.captured.txt.** DONE.
      The sentence now reads that the original grid and k2=3,4,5 extended rows
      were checked by both Singular and Sage, but the 23 newest rows (k2=6..10)
      rest on Singular alone because `pattern_sage_check_k2_6.captured.txt` is a
      `NameError` — Sage never ran. Do not describe the new rows as
      independently verified.

- [ ] **4. Maintain effective/uniform-in-k discipline on every new claim.**
      The ledger is at 41 asserted, 7 checked, 2 proved. The genus formula claim
      says explicitly that it gives neither an effective bound nor uniformity in
      k — Faltings is per-pair and ineffective regardless of how cheap the genus
      computation becomes. Every new claim the run files must say whether its
      bound is effective and whether it is uniform in k. Do not add claims that
      fail to state both.

- [ ] **5. Assertion backlog: 41 asserted, 7 checked, 2 proved.** Convert or
      drop; do not add. Every asserted claim that cannot be checked or sourced
      should be demoted.

## Priority work (directive 8, still live)

- [ ] **6. Run the seven uncaptured programs in one batch.** The only one with a
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

- [ ] **7. Register the k2=5 closed form as established.** `genus[{5},n] = 2n-2
      except 2n-4 when 5|n` — exact on all 19 points n=6..24, zero mismatches,
      operator-confirmed. Now subsumed by the single genus formula but still
      worth recording as a separate check. Write the claim.

- [ ] **8. Register the slope conjecture as established.** Mean first-difference
      over WHOLE periods is exactly (m-1)/2 for m=2,3,4,5, with period-m diff
      patterns: [0,1], [1,0,2], [1,2,0,3], [2,2,2,0,4]. Operator-confirmed,
      zero mismatches. **Trap for whoever writes this up:** a truncated window
      (not a whole number of periods) gives a mean BELOW (m-1)/2 and looks like
      a refutation — state periodicity first, mean second.

- [ ] **9. Delete or tombstone any of the seven programs that fail to run.**
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
- 43 claims: 41 asserted, 7 checked, 2 proved. Any lemma implying B<8 is refuted by 3003;
  state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it.
  Every new claim must say whether its bound is effective and whether it is
  uniform in k. The 41 asserted is a backlog — convert or drop, do not add.