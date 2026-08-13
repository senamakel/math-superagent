# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Priority work (directive 11)

- [x] **0. Lane Clark claim promoted to checked.** `lane-clark-normal-array-bound`
      verified against witnesses.json and brute force 2<=a<=60, EXIT_CODE=0,
      capture at `code/out/verify_lane_clark_bound.captured.txt`.
      Now `checked` with effective:yes, uniform-in-k:yes. PENDING marker resolved.
      Ledger: 44 asserted, 8 checked, 2 proved.

- [ ] **1. Prove the genus formula — the one item that can move `proved` off 2.**
      The formula `g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2` is `checked` (111
      Singular values, zero mismatches) but not `proved`. Directive 10 supplies
      the derivation path, which is bounded and finishable:

      **(a)** Verify the symmetric rewrite is an algebraic identity (one line):
      `(m-1)n - (m-2) = mn - n - m + 2 = (m-1)(n-1) + 1`, so
      `g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2`. Symmetry in m,n is now on the
      face of it. Already done in `code/out/genus_symmetric_form.md`.

      **(b)** The coprime case `gcd(m,n)=1` gives `g = (m-1)(n-1)/2 = p_a/2`
      exactly — a factor of two, which means a quotient. The curve
      `C(x,m) = C(y,n)` has bidegree `(m,n)` on `P^1×P^1` with arithmetic
      genus `p_a = (m-1)(n-1)`. The involution is:
      `C(k-1-z, k) = (-1)^k C(z,k)` — negating each of the k linear factors —
      so the curve carries `x -> m-1-x` and `y -> n-1-y` for even degrees,
      and their product when both are odd. Riemann-Hurwitz on the quotient by
      this involution should produce `g = p_a/2` for the coprime case, and the
      `gcd(m,n)` correction is the term measuring where the involutions and
      branch loci interact.

      **(c)** Do the singularity count at the points at infinity where the
      bidegree curve meets the boundary of `P^1×P^1`. The total delta invariant
      prediction is `((m-1)(n-1) - 1 + gcd(m,n))/2`. Prove that.

      **(d)** When the derivation is written in `code/out/` and checked against
      the 111 Singular values with zero mismatches, promote the claim from
      `checked` to `proved`. This moves `proved` from 2 to 3. The genus formula
      remains NOT effective and NOT uniform in k — Faltings is still per-pair
      and ineffective. This is a proof of the genus, not progress on Singmaster,
      and the claim block must say so.

- [ ] **2. The assertion backlog is now 44 asserted, 8 checked, 2 proved.**
      Converting one checked claim to proved (item 1) is the single highest-
      value ledger operation. After that, convert or drop asserted claims;
      do not add new ones. Every asserted claim that cannot be checked or
      sourced should be demoted.

- [ ] **3. Run the five uncaptured programs.** The only one with a capture is
      `genus_table`. Run the rest, adjusting paths for the three in
      subdirectories:
      ```sh
      for p in genus/verify_superelliptic_formula pattern/fam_seqs genus/test_slope_across_rows genus/test_slope_hypothesis effectivegenus/rep_pairs genus/verify_k2_5_row pattern/print_family; do
        timeout 300 python3 code/$p.py 2>&1 | tee code/out/$(basename $p .py).captured.txt
        echo EXIT_CODE=$? >> code/out/$(basename $p .py).captured.txt
      done
      ```
      Delete or tombstone any that fail — a program never executed is not evidence.

- [ ] **4. Register the k2=5 closed form and slope conjecture as established.**
      Already operator-checked, zero mismatches. Subsumed by the single genus
      formula but worth recording as separate corroboration. Trap: a truncated
      (non-whole-period) window gives mean BELOW `(m-1)/2` and looks like a
      refutation — state periodicity first, mean second.

- [ ] **5. Maintain effective/uniform-in-k discipline on every claim.**
      The genus formula claim already says it gives neither an effective bound
      nor uniformity in k. Every new claim must state both. Do not add claims
      that fail to state either.

## Done (directive 9 → directive 10 → directive 11)

- [x] **Directive 11: Lane Clark claim promoted to checked (asserted→checked).**
      PENDING file resolved; effective:yes, uniform-in-k:yes stated. Ledger: 44 asserted,
      8 checked, 2 proved.
- [x] Directive 9 items 1–2 (re-derive substitutions, Riemann-Hurwitz derivation plan) now
      subsumed by directive 10 item 1, which is sharper — the symmetric rewrite
      `((m-1)(n-1)+1-gcd(m,n))/2` and the involution `C(k-1-z,k)=(-1)^k C(z,k)`
      supply the exact mechanism. The coprime case `g=p_a/2` is the lever.
- [x] False two-CAS claim in genus_table fixed.
- [x] Genus symmetric rewrite verified and captured at `code/out/genus_symmetric_form.md`.
- [x] MRSTT effectiveness — confirmed effective from full text (Remark 1.7),
      with an astronomically large but computable threshold. Uniform-in-k: yes
      over interior; no over boundary.
- [x] Witness double-failure stated honestly in `mrstt_leaves_witnesses_open.md`.
- [x] Dead source files tombstoned (singmaster-1971, mrstt-interior-singmaster).
- [x] MRSTT PENDING contradiction resolved.

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
- 44 asserted, 8 checked, 2 proved. Any lemma implying B<8 is refuted by 3003;
  state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it.
  Every new claim must say whether its bound is effective and whether it is
  uniform in k. The 44 asserted is a backlog — convert or drop, do not add.