# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Directive 13 — immediate priority

- [x] **1. Two zero-byte captures fixed.** `code/out/genus_falsify.captured.txt`
      and `code/out/pattern_fam_seqs.captured.txt` were 0 bytes; each now carries
      a one-line explanation (`EXIT_CODE=1 — program failed silently`).
- [x] **2. Genus integrality recorded but NOT adopted.** `research/notes/genus-integrality-proved.md`
      and `code/out/genus_integrality_proved.captured.txt` hold a four-case parity
      proof that `(m-1)(n-1) + 1 - gcd(m,n)` is always even, so the closed form
      `g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2` is always integer. 1,121,253 pairs
      verified with zero exceptions. **Effective, uniform in m and n, inherits
      nothing from Faltings or Siegel, and bounds nothing.** The ten predictions
      matching the symmetric form are internal consistency (algebraically equal
      expressions), NOT independent genus confirmation — do not mark them verified
      until Singular confirms them. **This result needs independent verification
      by this run** before it can be claimed as established.
- [ ] **3. Run `check_mason_stothers_bound.py` — STILL unrrun after directive 12.**
      The script is at `code/out/check_mason_stothers_bound.py`. Run:
      ```
      timeout 540 python3 code/out/check_mason_stothers_bound.py 2>&1 | tee code/out/check_mason_stothers_bound.captured.txt; echo EXIT_CODE=$?
      ```
      It uses sympy — the container has it; the host does not, which is why this
      must run inside the container. Check the capture is non-empty before moving
      on. If slack >= 0 for every (k1,k2) tested, the claim
      `mason-stothers-vacuous-binomial` moves from `checked` (with the caveat
      "checker script was written, not run") to `checked` with captured evidence.
      This is the one remaining item from directive 12 that was not completed
      (code went from 35 to 36 files but no capture was produced).

## Ledger discipline

- **Ledger: 44 asserted, 8 checked, 2 proved.** Convert or drop asserted claims,
  do not add. Every bound must be run against `code/out/witnesses.json`. Any lemma
  implying B<8 is refuted by 3003. State counting convention on every claim.
- When the mason-stothers capture is non-empty and confirms the prediction, the
  `mason-stothers-vacuous-binomial` claim moves to `checked` with evidence. The
  approach file `research/approaches/mason-stothers-abc.md` already says `refuted`;
  the capture is the evidence that was missing from the claim block.

## Priority work — genus derivation

- [ ] **4. Independent verification of genus integrality.** The operator's proof
      (four parity cases) is recorded. This run must verify it independently
      before claiming it. Run the verification with a second engine (e.g. sympy
      symbolic parity check on `(m-1)(n-1)+1-gcd` for symbolic parities) or a
      different bound (m,n up to 2000) and capture the output. Until then, the
      integrality claim is `operator-computed`, not `proved` by this run.

- [ ] **5. Prove the genus formula from Riemann–Hurwitz/Plücker.** The integrality
      lemma removes one gap (the expression is always integer). The remaining
      gap is the derivation itself — the coprime case `g=p_a/2` via the
      involution `C(k-1-z,k) = (-1)^k C(z,k)` plus the singularity delta-invariant
      for the `gcd(m,n)` term. This is the route from `checked` (111 Singular
      values) to `proved`. The involution mechanism and the singularity count at
      the points at infinity of `P^1×P^1` are the concrete lemmas needed.

- [ ] **6. Matveev effective-bound computation.** Apply Matveev 2000 Thm 2.3
      (K=Q, D=ρ=1) to a specific small-(k1,k2) family (e.g. k2=2 hyperelliptic
      row) and compute the explicit constant numerically. State its k-dependence.
      The primary source is held; the constants C1, C2, C′0 are in
      `research/sources/matveev-2000-homogeneous-linear-form.full.md`. This is a
      GOAL-eligible partial result.

## Done (directive 9 → 10 → 11 → 12 → 13)

- [x] **Directive 13 zero-byte captures:** `genus_falsify.captured.txt` and
      `pattern_fam_seqs.captured.txt` now carry one-line explanations.
- [x] Directive 12 items 2–3: mason-stothers-abc and s-unit-subspace already
      refuted in APPROACHES.md; no new approaches opened.
- [x] **Directive 11: Lane Clark claim promoted to checked.** Ledger: 44 asserted,
      8 checked, 2 proved. Effective:yes, uniform-in-k:yes.
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