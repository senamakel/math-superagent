# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Directive 15 — immediate priority (Mason-Stothers done; Riemann-Hurwitz first)

- [x] **3. Run `check_mason_stothers_bound.py` — DONE.** Capture at
      `code/out/check_mason_stothers_bound.captured.txt`: degB'=0 for all 21
      pairs (2<=k2<k1<=8), slack >= 0 throughout. Claim
      `mason-stothers-vacuous-binomial` moved from `checked` (unrun) to
      `checked` with captured evidence. Approach `mason-stothers-abc.md`
      refuted with the slack table and the structural reason B'=constant
      named (the two binomials share their common falling factorial as their
      entire gcd; dividing it out leaves one monic falling factorial and one
      rational constant). Range stated: 2<=k2<k1<=8 — a vacuity check over
      that box, not all pairs, but the collapse mechanism is uniform.
- [ ] **1. Riemann-Hurwitz derivation of the genus closed form.** The formula
      `g(m,n)=((m-1)n-(m-2)-gcd(n,m))/2` is `checked` (111 values, 17
      out-of-sample), integrality is proved, but there is no derivation.
      Compute the ramification of the map `C(x,m)=C(y,n)` → projective closure,
      apply Riemann-Hurwitz, and account for the `gcd(m,n)` singularity term.
      This is the fourth proved claim and the only one in view. Priority over
      all other open tasks.
- [ ] **2. Make `genus-closed-form-integrality` rest on this run's own
      arithmetic.** Run the operator's exact reproduction:
      `len([1 for m in range(1,800) for n in range(1,800) if ((m-1)*(n-1)+1-gcd(m,n))%2])`,
      expected `0` at EXIT_CODE=0. Capture to
      `code/out/integrality_reproduced.captured.txt`.
- [ ] **4. Compute a concrete Matveev effective constant for one small pair.**
      Apply Matveev 2000 Thm 2.3 (K=Q, D=ρ=1) to {2,3}
      (triangular=tetrahedral) — the per-pair effective height bound with a
      computed constant. This is the GOAL-eligible partial result.
- [ ] **5. Infrastructure: Cognee OOM-killed 11 times in 30 min.** Do not treat
      an empty `recall_memory` as evidence that nothing is known. Route around
      by reading claim files directly rather than relying on recall. This is
      an operational note, not a task to close.

## Ledger discipline

- **Do not convert or drop asserted claims without a second route.** Every
  bound must be run against `code/out/witnesses.json`. Any lemma implying B<8
  is refuted by 3003. State counting convention on every claim.
- The out-of-sample claim (item 1) is `checked`, effective, NOT uniform — say
  so whenever it is cited.

## Done (directives 4 → 15)

- [x] **Directive 15 item 3 (Mason-Stothers):** captured run at
      `code/out/check_mason_stothers_bound.captured.txt` — degB'=0 for all
      21 pairs, slack >= 0 throughout. Claim `mason-stothers-vacuous-binomial`
      moved to `checked` with captured evidence; approach refuted with slack
      table and structural reason (B' constant). Range 2<=k2<k1<=8 stated.
- [x] **Directive 14 item 1:** out-of-sample genus verification recorded as
      `genus-closed-form-out-of-sample-verified`, checked, effective, not uniform.
- [x] **Directive 13 zero-byte captures:** `genus_falsify.captured.txt` and
      `pattern_fam_seqs.captured.txt` now carry one-line explanations.
- [x] Directive 12 items 2–3: mason-stothers-abc and s-unit-subspace already
      refuted in APPROACHES.md; no new approaches opened.
- [x] **Directive 11: Lane Clark claim promoted to checked.** Effective:yes,
      uniform-in-k:yes.
- [x] Directive 9 items 1–2 subsumed by directive 10 item 1.
- [x] False two-CAS claim in genus_table fixed.
- [x] Genus symmetric rewrite verified and captured.
- [x] MRSTT effectiveness confirmed from full text (Remark 1.7).
- [x] Witness double-failure stated in `mrstt_leaves_witnesses_open.md`.
- [x] Dead source files tombstoned.
- [x] MRSTT PENDING contradiction resolved.
- [x] Five formerly-uncaptured programs now have captures (directive 5).

## Search policy (directive 4)

- [x] **Stop searching.** Literature search covered exa_search 66–76 and frontier
      170–220. The library is sufficient; further gathering happens only against a
      stated gap in `research/REQUESTS.md`.

## Completed deliverables (attempt 2)

- [x] Exact MRSTT statement → `research/approaches/mrstt-exact-statement.md`
- [x] Reproduce every worked example (`verify_mrstt_witnesses.py`, EXIT_CODE=0)
- [x] Run witnesses against MRSTT interior cut (`check_witnesses_vs_mrstt.py`)
- [x] Demote `singmaster-1971-original` / `best-unconditional-bound` claims
- [x] MRSTT-interior-singmaster tombstone written
- [x] Singmaster-1971 tombstone written
