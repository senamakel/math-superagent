# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Directive 16 — immediate priority: run verify_riemann_hurwitz.py

- [ ] **1. Run the Riemann-Hurwitz verification.** The program
      `code/genus/verify_riemann_hurwitz.py` exists and has never been run (no
      capture matching `riemann` in `code/out`). It checks the four ingredients
      of the genus closed form `g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2` — degree-n
      projection, m(n-1) simple finite ramification points via Rolle,
      infinity structure with gcd(m,n) branches, and the exact RH identity —
      symbolically and numerically over the grid. Run it:

      ```
      timeout 540 python3 code/genus/verify_riemann_hurwitz.py 2>&1 | tee code/out/verify_riemann_hurwitz.captured.txt; echo EXIT_CODE=$?
      wc -c code/out/verify_riemann_hurwitz.captured.txt
      ```

      Confirm the capture is non-empty before doing anything else — the
      `genus_falsify` zero-byte window is the precedent to avoid.

      **Two things to be careful about when recording the result:**

      (a) **Infinity.** Rolle gives the n-1 finite critical points cleanly; the
      contribution over x=infinity is where a Riemann-Hurwitz count usually goes
      wrong, and gcd(m,n) enters there. If the program does not compute the
      points at infinity explicitly — if the infinity term is asserted from the
      Newton-polygon branch count rather than computed via the normalization —
      say so and treat the derivation as incomplete rather than done.

      (b) **State both attributes.** A derivation of g(m,n) is effective and
      uniform in m and n. What it does NOT give is anything effective or uniform
      for Singmaster: genus ≥ 2 feeds Faltings, which is per-(k1,k2) and
      ineffective. Write that boundary into the claim so nobody later reads the
      derivation as progress on the conjecture itself.

- [ ] **2. Reproduce the integrality arithmetic independently.**
      Run `len([1 for m in range(1,800) for n in range(1,800) if ((m-1)*(n-1)+1-gcd(m,n))%2])`,
      expected `0` at EXIT_CODE=0. Capture to
      `code/out/integrality_reproduced.captured.txt`. This promotes the
      genus-closed-form-integrality claim from `operator-computed` to
      `checked` by this run.

- [ ] **3. Compute a concrete Matveev effective constant for one small pair.**
      Apply Matveev 2000 Thm 2.3 (K=Q, D=ρ=1) to {2,3}
      (triangular=tetrahedral) — the per-pair effective height bound with a
      computed constant. This is the GOAL-eligible partial result.

## Ledger discipline

- **Do not convert or drop asserted claims without a second route.** Every
  bound must be run against `code/out/witnesses.json`. Any lemma implying B<8
  is refuted by 3003. State counting convention on every claim.
- The genus closed form is `checked` (out-of-sample), effective, NOT uniform —
  say so whenever it is cited.

## Done (directives 4 → 16)

- [x] **Directive 16 item 2 (mason-stothers-vacuous):** The claim
      `mason-stothers-vacuous-binomial` is `checked` with captured evidence
      (`code/out/check_mason_stothers_bound.captured.txt`: degB'=0 for all 21
      pairs, slack ≥ 0 throughout). The approach `mason-stothers-abc.md` is
      `refuted` in APPROACHES.md with the slack table and structural reason
      (B' constant). Both were completed in the directive-15 cycle; the id
      difference (`vacuous-binomial` vs `vacuous-for-binomials`) is a hyphen.
- [x] **Directive 15 item 1 (Riemann-Hurwitz):** The program exists and is
      correct in design — directive 16 now runs it.
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

- [x] **Stop searching.** The library is sufficient; further gathering happens
      only against a stated gap in `research/REQUESTS.md`.

## Completed deliverables (attempt 2)

- [x] Exact MRSTT statement → `research/approaches/mrstt-exact-statement.md`
- [x] Reproduce every worked example (`verify_mrstt_witnesses.py`, EXIT_CODE=0)
- [x] Run witnesses against MRSTT interior cut (`check_witnesses_vs_mrstt.py`)
- [x] Demote `singmaster-1971-original` / `best-unconditional-bound` claims
- [x] MRSTT-interior-singmaster tombstone written
- [x] Singmaster-1971 tombstone written