# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Directive 12 — immediate priority

- [ ] **1. Run `code/out/check_mason_stothers_bound.py`.** It exists and has never
      been executed. Run:
      ```
      timeout 540 python3 code/out/check_mason_stothers_bound.py 2>&1 | tee code/out/check_mason_stothers_bound.captured.txt; echo EXIT_CODE=$?
      ```
      Check the capture is non-empty before moving on. The docstring predicts the
      answer: "we verify it is always satisfied (vacuous) for binomial pairs, i.e.
      the inequality never binds". If the slack column is >= 0 for every (k1,k2)
      tested, that is a NEGATIVE result — claim `mason-stothers-vacuous-for-binomials`
      becomes `checked` with captured evidence, and `research/approaches/mason-stothers-abc.md`
      is refuted with evidence (the approach block already says `refuted`; the
      captured program output is the evidence that was missing — the claim currently
      says "script was written, not run"). A route closed with evidence is a result;
      a route left proposed is not.

- [ ] **2. Close (do not re-propose) the two approaches that are already refuted.**
      `mason-stothers-abc` (refuted; item 1 supplies the captured evidence) and
      `s-unit-subspace` (refuted; `sunit-subspace-inapplicable` is the right kind
      of claim — the directive acknowledges this). Both are already `status: refuted`
      in `research/APPROACHES.md`. No further action on the approach files is needed;
      the closure is recorded here. **Open no new approaches for this cycle.**

## Ledger and structural state

The pattern to break: claims frozen at ~62, proved stuck at 2 since the run began,
literature acquisition running ahead of conversion. The genus derivation is the
only visible route to a third proved claim.

- **Ledger: 44 asserted, 8 checked, 2 proved.** Any lemma implying B<8 is refuted
  by 3003; state the counting convention on every claim. Do not record a bound as
  checked unless `code/out/witnesses.json` has been run against it. Every new claim
  must say whether its bound is effective and whether it is uniform in k. The 44
  asserted is a backlog — convert or drop, do not add.

## Priority work — proven claims and the genus derivation

- [ ] **3. Prove the genus formula — the one item that can move `proved` off 2.**
      The formula `g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2` is `checked` (111
      Singular values, zero mismatches) but not `proved`. The symmetric rewrite is
      already captured at `code/out/genus_symmetric_form.md`. Derivation path:

      **(a)** The coprime case `gcd(m,n)=1` gives `g = (m-1)(n-1)/2 = p_a/2`
      exactly — a factor of two, which means a quotient. The curve
      `C(x,m) = C(y,n)` has bidegree `(m,n)` on `P^1×P^1` with arithmetic
      genus `p_a = (m-1)(n-1)`. The involution is:
      `C(k-1-z, k) = (-1)^k C(z,k)` — negating each of the k linear factors —
      so the curve carries `x -> m-1-x` and `y -> n-1-y` for even degrees,
      and their product when both are odd. Riemann-Hurwitz on the quotient by
      this involution should produce `g = p_a/2` for the coprime case, and the
      `gcd(m,n)` correction is the term measuring where the involutions and
      branch loci interact.

      **(b)** Do the singularity count at the points at infinity where the
      bidegree curve meets the boundary of `P^1×P^1`. The total delta invariant
      prediction is `((m-1)(n-1) - 1 + gcd(m,n))/2`. Prove that.

      **(c)** When the derivation is written and checked against the 111 Singular
      values with zero mismatches, promote the claim from `checked` to `proved`.
      This moves `proved` from 2 to 3. The genus formula remains NOT effective and
      NOT uniform in k — Faltings is still per-pair and ineffective. This is a
      proof of the genus, not progress on Singmaster, and the claim block must
      say so.

- [ ] **4. Matveev effective-bound computation.** For a specific small-(k1,k2) family
      (e.g. (2,p) hyperelliptic or k2=2 row), apply Matveev 2000 Thm 2.3 constants
      to produce a computed explicit bound; state its non-uniformity. The primary
      source is held at `research/sources/matveev-2000-homogeneous-linear-form.full.md`;
      the summary is at `research/summaries/matveev-2000-homogeneous-linear-form.md`.

## Uncaptured programs — run or delete

- [ ] **5. Run the five uncaptured programs listed under `code/out/` that have
      no `.captured.txt`:**
      ```sh
      for p in genus/verify_superelliptic_formula pattern/fam_seqs genus/test_slope_across_rows genus/test_slope_hypothesis effectivegenus/rep_pairs genus/verify_k2_5_row pattern/print_family; do
        timeout 300 python3 code/$p.py 2>&1 | tee code/out/$(basename $p .py).captured.txt
        echo EXIT_CODE=$? >> code/out/$(basename $p .py).captured.txt
      done
      ```
      Their conclusions are already operator-checked; capturing is verification,
      not discovery. Delete or tombstone any that fail.

## Done (directive 9 → 10 → 11)

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