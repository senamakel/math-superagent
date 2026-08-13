# Tasks

Current goal: produce a genuine partial result on Singmaster's conjecture, stated
exactly with its bound and evidence class, OR name precisely what blocks the
argument.

## Riemann-Hurwitz genus derivation — extend and claim

The capture already exists and is non-empty —
`code/out/verify_riemann_hurwitz.captured.txt` at 48 KiB, ALL CHECKS PASSED
for 2<=m<=9, m<n<=10, plus (3,25),(4,25),(6,9). The old polyroots crash at
(2,8) was fixed by switching to bisection (critical_points_of_q uses bisection
on each Rolle-guaranteed interval, not mpmath polyroots). The directive's
"option b" is already in place.

- [ ] **1. Extend the range to 2 <= m < n <= 20.**
      Edit `code/genus/verify_riemann_hurwitz.py` line 77: change the pairs list
      from `range(2, 10) ... range(m+1, 11)` to `range(2, 20) ... range(m+1, 21)`.
      Keep the `critical_points_of_q` bisection guard at `if n <= 15` (bisection
      works for any n but is linear in n; the structural Rolle argument already
      covers all n). Then run:
      ```
      timeout 540 python3 code/genus/verify_riemann_hurwitz.py 2>&1 | tee code/out/verify_riemann_hurwitz_full.captured.txt; echo EXIT_CODE=$?
      ```
      State the range covered and the number of pairs verified in the capture.

- [ ] **2. Record the claim.**
      After the extended run passes, create
      `research/notes/genus-closed-form-derived-by-riemann-hurwitz.md` with:
      - The closed form: `g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2`
      - Status: **proved** — the Riemann-Hurwitz argument is general in m,n:
        (a) degree = n, (b) finite ramification = m(n-1) points each index 2
        (Rolle guarantees n-1 simple real critical points of Q; smoothness
        checked explicitly), (c) fibre at x=infinity computed explicitly via
        Puiseux: n/gcd(m,n) branches each of index gcd(m,n), total I_inf = n-gcd,
        (d) 2g-2 = -2n + m(n-1) + (n-gcd) → the closed form.
      - Effective: yes (exact integer formula)
      - Uniform in (m,n): yes (one formula for all distinct m,n)
      - Singmaster bearing: gives NOTHING effective or uniform — genus >= 2
        feeds Faltings, which is per-(k1,k2) and ineffective. The closed form
        makes genus decidable for any pair but does not bound N(a).
      - Evidence class: proved (the argument is structural, not instance-counting)
      - Store with `remember_memory`.

## Matveev effective constant for {2,3}

- [ ] **3. Apply Matveev 2000 Thm 2.3 (K=Q, D=ρ=1) to triangular=tetrahedral.**
      GOAL-eligible partial result: an effective height bound with a **computed**
      constant for C(x,2)=C(y,3). The primary source is held
      (`research/sources/matveev-2000-homogeneous-linear-form.full.md`), and
      Avanesov already solved the (2,3) curve finitely — the deliverable is
      making the constant explicit. Verify the Kummer condition for the
      rational-integer case (αⱼ are rationals, so [K(√α₁..√αₙ):K] = 2ⁿ holds
      automatically when the αⱼ are positive and squarefree).

## Integrality repro

- [ ] **4. Reproduce integrality independently.**
      Run parity check over 1..799, capture to
      `code/out/integrality_reproduced.captured.txt`.

## Completed / no further action

- [x] **4. Reproduce integrality independently — DONE.** `code/genus/repro_integrality.py`, EXIT_CODE=0: 638401 pairs over 1<=m,n<=799, ZERO odd values of N=(m-1)(n-1)+1-gcd(m,n) in all four parity classes; both algebraic forms agree on 1..399. Capture `code/out/integrality_reproduced.captured.txt` (replaces 2-byte placeholder); independently re-verifies claim genus-closed-form-integrality (proved) and the operator's 1,121,253-pair check.
- [x] **verify_superelliptic_formula.py EXECUTED — DONE.** EXIT_CODE=0, ALL literature cross-checks PASS for {2,n} and {3,n} against the Sutherland 2020 superelliptic genus formula; {4,n} correctly reported as non-superelliptic. Capture `code/out/verify_superelliptic_formula.captured.txt`; closes the "NOT yet executed" row in code/genus/INDEX.md.
- [x] verify_riemann_hurwitz.py already runs and passes (bisection fix applied;
      capture at code/out/verify_riemann_hurwitz.captured.txt, EXIT_CODE=0)
- [x] Mason-Stothers refuted (capture, claim, approach all closed)
- [x] Search stopped; library sufficient
- [x] MRSTT effectiveness confirmed; witness double-failure stated

## Ledger discipline

- asserted=22, checked=4, proved=0 (genus R-H claim will be the first `proved`)
- Every bound must be run against `code/out/witnesses.json`. Any lemma implying
  B<8 is refuted by 3003. State counting convention on every claim.
- The genus closed form is effective and uniform in (m,n), but gives nothing
  for Singmaster (Faltings is per-pair and ineffective). Say so whenever cited.