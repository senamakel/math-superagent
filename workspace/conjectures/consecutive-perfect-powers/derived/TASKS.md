# Tasks

## Case B complete closure via Nagell-Ljunggren (this run)

- [x] `code/caseB/caseB_complete_closure.py`: Complete Case B of Catalan
      (x^p - y^2 = 1, p odd prime >= 3) via the Nagell-Ljunggren theorem,
      exact for the slice. Reduction (claim exp2-caseB-reduction) and
      mod-8 classification (claim exp2-caseB-t-mod8-classification, leaves
      only c even & p ≡ 1 mod 8) are the PROVED in-workspace premises.
      Slice: n = p odd prime (>=3), X = c^2+1 (>=5), residual class
      X ≡ 1 mod 4. Both N-L exceptions excluded exactly: (4,7,20) n=4 even;
      (5,3,11) X=3 needs c^2=2 impossible, and X=3,7 fail X ≡ 1 mod 4.
      Exact oracle: T(c,p)=((c^2+1)^p-1)/c^2 not square for c even in
      [2,200000], odd p in [3,199] (4.5e6 pairs, 0 squares, 7.78s parallel);
      direct enumeration (X^n-1)/(X-1)=Y^2 for n in {2,3,4,5}, X in [2,1e6]
      finds exactly (4,7,20) and (5,3,11), none else in odd indices 3,5.
      Run: code/out/caseB_complete_closure.captured.txt (EXIT 0, 8.49s);
      claim caseB-complete-closure-nagell-ljunggren in
      code/out/caseB_complete_closure.note.md. Ljunggren theorem itself is
      ASSERTED-CLASSICAL (standard citation, not fetched/re-proved) — the
      single remaining sorry; Case B proved conditional on it.

## Attempt 3 — elementary Cassels chain in Z (rising-sea ground-change)

Goal: re-derive the Cassels divisibility `p|y, q|x` for `x^p - y^q = 1`
(p,q odd primes) with proofs in this workspace, by the elementary Z-route
(gcd lemma + perfect-power structure + reduced system), then derive the
double-Wieferich congruences from it. Foundation status: oracle to 10^8,
h^- formula, Cassels valuation machinery all `checked` already; Cassels full
divisibility is the open load-bearing rung (research/threads/cassels-divisibility.md).

- [x] tool_builder: `code/cassels/elementary_structure.py` — exact checks:
      gcd lemma (1,199,994 cases, 0 failures), Fermat equivalence (same
      range, 0 failures), reduced-system sweep `Φ_p(a^q+1)` never a perfect
      q-th power (202,886 (p,q,a) cases, ZERO hits), mirror for q|x (46,480
      cases, ZERO non-degenerate), calibration at (3,2,2,3) PASS, gmpy2.iroot
      cross-check (258 samples) PASS. OVERALL ALL CHECKS PASS, 1.15s.
      Run: code/out/cassels_elementary.captured.txt; claim
      cassels-reduced-system-sweep in code/out/cassels_elementary.note.md.
- [ ] symbolic_math: derive the Cassels descent `Φ_p(a^q+1) ≠ b^q` and
      mirror; close p|x-1, q|y+1 or name the exact gap. [spawned]
- [ ] lean_prover: formalize p|x-1 ⟺ p|x^p-1 and gcd(x-1, Φ_p(x)) | p,
      no sorry, report #print axioms. [spawned]
- [ ] If Cassels closes: derive double-Wieferich `p^{q-1}≡1 (mod q^2)`,
      `q^{p-1}≡1 (mod p^2)` from p|x-1, q|y+1 (currently
      reconstructed/heuristic in the library) — p-adic expansion of
      q^p x_1^p - p^q y_1^q = 1 with x = qx_1, y = py_1.
- [ ] Verify the resulting condition set with check_conditions over a wide
      exponent range (parallel_map, 28 CPUs); confirm (2,3) is
      excluded-by-hypothesis at the known solution.
- [ ] Update research/backward/cassels-selfcontained.md: mark cv-lte,
      cv-cyclo-coprime, cv-vp-transfer, cv-vq-transfer statuses.

## Done (earlier attempts)

- Oracle `solutions(N) == {(3,2,2,3)}` exact to N = 10^8.
- exp2-xq and exp2-yp verified to 10^8; exp2-even proved; case-B reduced to
  T(c,p) non-square (verified c ≤ 1e5, p ≤ 101).
- h^-(Q(ζ_p)) checked by two independent routes to p=43, A000927 to p=97;
  Kummer criterion verified to p=700; irregular primes < 100 = {37,59,67}.
- Cassels valuation/LTE/cyclotomic-coprimality machinery checked (exact).
- Double-Wieferich minimal pair (83,4871) found; cross-prime h^- forcing
  dead-ended at it (chisel board).
- hminus_check (the pending check from attempt 2's lesson) already
  ALL-MATCH: True — claim `minus-class-number-formula` is checked.

## Done (this attempt)

- Ramification claim `zeta-p-ring-of-integers-and-ramification` (previously
  `asserted`): the three previously-written-never-run verifiers executed this
  run, ALL PASS, exact integer arithmetic. `(1-ζ)^(p-1) ≡ 0 (mod p)` in
  Z[ζ_p] with integral unit quotient for all odd primes p ≤ 97;
  N(1-ζ_p)=Φ_p(1)=p and Φ_p(X)≡(X-1)^(p-1) (mod p) for p ≤ 19; exact
  resultant norm N(u)=±1 for p ≤ 23. Claim `ramification-check-exact` in
  code/out/ramification_check.note.md; anchors
  code/out/verify_ram_fast.captured.txt,
  code/out/verify_ramification.captured.txt,
  code/out/scholar_ramification_check.captured.txt. Evidence upgraded to
  checked on the stated ranges (not a proof for all p; ring-of-integers
  equality still asserted by Conrad).
