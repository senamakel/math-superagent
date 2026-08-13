# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Directive 14 — immediate priority

- [x] **1. Record the out-of-sample genus verification.** Claim id
      `genus-closed-form-out-of-sample-verified`, status `checked`, anchor
      `code/out/genus_falsify.captured.txt`. Written in
      `code/out/genus_out_of_sample_verified.md`. 17/17 pairs out-of-sample,
      predicted first from the closed form then recomputed in Singular, 0
      mismatches; pairs span m in 2..16, n in 13..28. Attributes stated:
      **effective: yes**, **uniform in k: no** (17 specific pairs, not all).
- [ ] **2. Make `genus-closed-form-integrality` rest on this run's own
      arithmetic.** The proof note `research/notes/genus-integrality-proved.md`
      and `code/out/genus_integrality_proved.captured.txt` were operator-written
      and adopted without an independent capture. Run the operator's exact
      reproduction (parity of `(m-1)(n-1)+1-gcd(m,n)` over m,n up to 799):
      ```
      timeout 300 python3 -c "
      from math import gcd
      print(len([1 for m in range(1,800) for n in range(1,800) if ((m-1)*(n-1)+1-gcd(m,n))%2]))" 2>&1 | tee code/out/integrality_reproduced.captured.txt; echo EXIT_CODE=$?
      ```
      Expected output `0` (no odd values of `N`), EXIT_CODE=0. If so, the
      integrality claim's arithmetic is independently reproduced by this run —
      update its `holds-here`/`status` note to cite this capture in addition to
      the four-case proof. If nonzero, the proof is wrong and must be reopened.
- [ ] **3. Run `check_mason_stothers_bound.py` — third directive, STILL UNRUN.**
      ```
      timeout 540 python3 code/out/check_mason_stothers_bound.py 2>&1 | tee code/out/check_mason_stothers_bound.captured.txt; echo EXIT_CODE=$?
      ```
      Uses sympy (container has it; host does not — run inside the container).
      Confirm the capture is non-empty. If slack >= 0 for every (k1,k2) tested,
      move `mason-stothers-vacuous-binomial` from `checked` (with "checker
      written, not run") to `checked` with captured evidence, and mark
      `research/approaches/mason-stothers-abc.md` refuted (already stated
      refuted in the approach file; the capture supplies the missing evidence).

## Priority work — the forward direction (directive 14, solver)

- [ ] **4. Compute a concrete Matveev effective constant for one small pair,
      directly, skipping sub-agents.** Both `goals` and `tool_builder` timed out
      in attempts 2 and 3; the direct-execution salvage added nothing beyond
      CONTEXT.md. Do not spawn sub-agents for this. Write the program directly:
      apply Matveev 2000 Thm 2.3 (K=Q, D=ρ=1, applies to binomial products since
      the αⱼ are rationals/primes) to a specific small-(k1,k2) family — start
      with {2,3} (triangular=tetrahedral, Avanesov's solved case, an isolated
      collision not an infinite family). Compute the explicit constant
      numerically and state its k-dependence numerically. This is the
      GOAL-eligible partial result: an effective height bound with a computed
      constant for a specific (k1,k2), per-pair not uniform. Constants C1, C2,
      C′0 are in `research/sources/matveev-2000-homogeneous-linear-form.full.md`;
      verify the Kummer condition and state the height convention (Matveev's A_j
      are logarithms-heights).
- [ ] **5. Prove the genus formula from Riemann–Hurwitz/Plücker.** The
      integrality lemma (item 2) removes one gap. The remaining gap is the
      derivation: coprime case `g = p_a/2` via the involution
      `C(k-1-z,k) = (-1)^k C(z,k)` plus the singularity delta-invariant for the
      `gcd(m,n)` term. Route from `checked` to `proved`; the out-of-sample test
      (item 1) is evidence, not a derivation.

## Ledger discipline

- **Do not convert or drop asserted claims without a second route.** Every
  bound must be run against `code/out/witnesses.json`. Any lemma implying B<8
  is refuted by 3003. State counting convention on every claim.
- The out-of-sample claim (item 1) is `checked`, effective, NOT uniform — say
  so whenever it is cited.

## Done (directives 4 → 14)

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
